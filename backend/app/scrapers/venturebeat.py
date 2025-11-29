"""
VentureBeat scraper
"""
from typing import List, Dict, Optional
from datetime import datetime
from .base import BaseScraper
import feedparser
import logging

logger = logging.getLogger(__name__)


class VentureBeatScraper(BaseScraper):
    """Scraper for VentureBeat AI news"""

    def __init__(self):
        super().__init__(
            source_name="VentureBeat",
            base_url="https://venturebeat.com"
        )
        self.rss_url = "https://venturebeat.com/category/ai/feed/"

    def scrape_articles(self, max_articles: int = 10) -> List[Dict]:
        """Scrape articles from VentureBeat RSS feed"""
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
                            'published_at': datetime(*entry.published_parsed[:6]),
                            'author': entry.get('author', 'VentureBeat'),
                            'image_url': self._extract_image(entry),
                            'tags': ['AI', 'VentureBeat']
                        }
                        articles.append(article)
                        logger.info(f"Scraped: {article['title']}")

                except Exception as e:
                    logger.error(f"Error processing entry: {str(e)}")
                    continue

        except Exception as e:
            logger.error(f"Error scraping VentureBeat: {str(e)}")

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
                if not article_body:
                    article_body = soup.find('div', {'class': 'entry-content'})

            if article_body:
                # Remove unwanted elements
                for element in article_body(['script', 'style', 'iframe', 'aside', 'figure']):
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

        # Try to get from enclosures
        if hasattr(entry, 'enclosures') and entry.enclosures:
            for enclosure in entry.enclosures:
                if 'image' in enclosure.get('type', ''):
                    return enclosure.get('href')

        return None
