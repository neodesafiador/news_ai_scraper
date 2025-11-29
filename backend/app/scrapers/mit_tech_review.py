"""
MIT Technology Review scraper
"""
from typing import List, Dict, Optional
from datetime import datetime
from .base import BaseScraper
import feedparser
import logging

logger = logging.getLogger(__name__)


class MITTechReviewScraper(BaseScraper):
    """Scraper for MIT Technology Review AI news"""

    def __init__(self):
        super().__init__(
            source_name="MIT Technology Review",
            base_url="https://www.technologyreview.com"
        )
        self.rss_url = "https://www.technologyreview.com/topic/artificial-intelligence/feed/"

    def scrape_articles(self, max_articles: int = 10) -> List[Dict]:
        """Scrape articles from MIT Tech Review RSS feed"""
        articles = []

        try:
            feed = feedparser.parse(self.rss_url)

            for entry in feed.entries[:max_articles]:
                try:
                    article_data = self.extract_article_content(entry.link)

                    if article_data:
                        article = {
                            'title': self.clean_text(entry.title),
                            'url': entry.link,
                            'content': article_data.get('content', ''),
                            'published_at': self._parse_date(entry),
                            'author': entry.get('author', 'MIT Technology Review'),
                            'image_url': self._extract_image(entry),
                            'tags': ['AI', 'MIT', 'Research']
                        }
                        articles.append(article)
                        logger.info(f"Scraped: {article['title']}")

                except Exception as e:
                    logger.error(f"Error processing entry: {str(e)}")
                    continue

        except Exception as e:
            logger.error(f"Error scraping MIT Tech Review: {str(e)}")

        return articles

    def extract_article_content(self, url: str) -> Optional[Dict]:
        """Extract full article content"""
        soup = self.fetch_page(url)
        if not soup:
            return None

        try:
            # Find article content
            article_body = soup.find('div', class_='content-body')
            if not article_body:
                article_body = soup.find('article')

            if article_body:
                # Remove unwanted elements
                for element in article_body(['script', 'style', 'iframe', 'aside']):
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

    def _parse_date(self, entry) -> datetime:
        """Parse publication date from entry"""
        if hasattr(entry, 'published_parsed') and entry.published_parsed:
            return datetime(*entry.published_parsed[:6])

        if hasattr(entry, 'updated_parsed') and entry.updated_parsed:
            return datetime(*entry.updated_parsed[:6])

        return datetime.now()

    def _extract_image(self, entry) -> Optional[str]:
        """Extract image URL from RSS entry"""
        if hasattr(entry, 'media_content') and entry.media_content:
            return entry.media_content[0].get('url')

        if hasattr(entry, 'links'):
            for link in entry.links:
                if link.get('type', '').startswith('image/'):
                    return link.get('href')

        return None
