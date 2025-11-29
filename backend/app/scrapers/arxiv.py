"""
arXiv scraper for AI/ML papers
"""
from typing import List, Dict, Optional
from datetime import datetime
from .base import BaseScraper
import feedparser
import logging

logger = logging.getLogger(__name__)


class ArxivScraper(BaseScraper):
    """Scraper for arXiv AI/ML papers"""

    def __init__(self):
        super().__init__(
            source_name="arXiv",
            base_url="https://arxiv.org"
        )
        # Search for AI/ML categories
        self.search_query = "cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.CV"
        self.api_url = f"http://export.arxiv.org/api/query?search_query={self.search_query}&sortBy=submittedDate&sortOrder=descending"

    def scrape_articles(self, max_articles: int = 10) -> List[Dict]:
        """Scrape papers from arXiv API"""
        articles = []

        try:
            feed = feedparser.parse(f"{self.api_url}&max_results={max_articles}")

            for entry in feed.entries:
                try:
                    article = {
                        'title': self.clean_text(entry.title),
                        'url': entry.link,
                        'content': self.clean_text(entry.summary),
                        'published_at': datetime(*entry.published_parsed[:6]),
                        'author': self._extract_authors(entry),
                        'image_url': None,  # arXiv doesn't provide images in feed
                        'tags': self._extract_categories(entry)
                    }
                    articles.append(article)
                    logger.info(f"Scraped: {article['title']}")

                except Exception as e:
                    logger.error(f"Error processing entry: {str(e)}")
                    continue

        except Exception as e:
            logger.error(f"Error scraping arXiv: {str(e)}")

        return articles

    def extract_article_content(self, url: str) -> Optional[Dict]:
        """
        For arXiv, the abstract is already in the feed
        This method would be used to fetch the full PDF content if needed
        """
        # The abstract is sufficient for our purposes
        # If you want to extract text from PDFs, you'd need additional libraries
        return None

    def _extract_authors(self, entry) -> str:
        """Extract author names from entry"""
        if hasattr(entry, 'authors') and entry.authors:
            authors = [author.name for author in entry.authors[:3]]
            if len(entry.authors) > 3:
                authors.append('et al.')
            return ', '.join(authors)

        if hasattr(entry, 'author'):
            return entry.author

        return 'arXiv'

    def _extract_categories(self, entry) -> List[str]:
        """Extract categories from entry"""
        tags = ['arXiv', 'Research', 'AI']

        if hasattr(entry, 'tags'):
            for tag in entry.tags:
                # Extract category codes like cs.AI, cs.LG
                term = tag.term
                if term.startswith('cs.'):
                    category_map = {
                        'cs.AI': 'Artificial Intelligence',
                        'cs.LG': 'Machine Learning',
                        'cs.CL': 'Natural Language Processing',
                        'cs.CV': 'Computer Vision',
                        'cs.RO': 'Robotics'
                    }
                    mapped = category_map.get(term, term)
                    if mapped not in tags:
                        tags.append(mapped)

        return tags[:5]  # Limit to 5 tags
