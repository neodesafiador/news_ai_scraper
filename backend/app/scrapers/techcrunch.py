"""
TechCrunch scraper
"""
from typing import List, Dict, Optional
from datetime import datetime
from .base import BaseScraper
import feedparser
import logging

logger = logging.getLogger(__name__)


class TechCrunchScraper(BaseScraper):
    """Scraper for TechCrunch AI news"""

    def __init__(self):
        super().__init__(
            source_name="TechCrunch",
            base_url="https://techcrunch.com"
        )
        self.rss_url = "https://techcrunch.com/category/artificial-intelligence/feed/"

    def scrape_articles(self, max_articles: int = 10) -> List[Dict]:
        """Scrape articles from TechCrunch RSS feed"""
        articles = []

        try:
            feed = feedparser.parse(self.rss_url)

            for entry in feed.entries[:max_articles]:
                try:
                    article_data = self.extract_article_content(entry.link)

                    if article_data and self.filter_ai_related(
                        entry.title,
                        article_data.get('content', '')
                    ):
                        article = {
                            'title': self.clean_text(entry.title),
                            'url': entry.link,
                            'content': article_data.get('content', ''),
                            'published_at': datetime(*entry.published_parsed[:6]),
                            'author': entry.get('author', 'TechCrunch'),
                            'image_url': self._extract_image(entry),
                            'tags': self._extract_tags(entry)
                        }
                        articles.append(article)
                        logger.info(f"Scraped: {article['title']}")

                except Exception as e:
                    logger.error(f"Error processing entry: {str(e)}")
                    continue

        except Exception as e:
            logger.error(f"Error scraping TechCrunch: {str(e)}")

        return articles

    def extract_article_content(self, url: str) -> Optional[Dict]:
        """Extract full article content"""
        soup = self.fetch_page(url)
        if not soup:
            return None

        try:
            # Find article content
            article_body = soup.find('div', class_='article-content')
            if not article_body:
                article_body = soup.find('article')

            if article_body:
                # Remove scripts and styles
                for element in article_body(['script', 'style', 'iframe']):
                    element.decompose()

                # Extract paragraphs
                paragraphs = article_body.find_all('p')
                content = ' '.join([p.get_text() for p in paragraphs])

                return {
                    'content': self.clean_text(content)
                }

        except Exception as e:
            logger.error(f"Error extracting content from {url}: {str(e)}")

        return None

    def _extract_image(self, entry) -> Optional[str]:
        """Extract image URL from RSS entry"""
        if hasattr(entry, 'media_content') and entry.media_content:
            return entry.media_content[0].get('url')

        if hasattr(entry, 'media_thumbnail') and entry.media_thumbnail:
            return entry.media_thumbnail[0].get('url')

        return None

    def _extract_tags(self, entry) -> List[str]:
        """Extract tags from RSS entry"""
        tags = ['AI']

        if hasattr(entry, 'tags'):
            tags.extend([tag.term for tag in entry.tags[:5]])

        return tags
