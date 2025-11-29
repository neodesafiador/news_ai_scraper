"""
Base scraper class for news sources
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaseScraper(ABC):
    """Abstract base class for news scrapers"""

    def __init__(self, source_name: str, base_url: str):
        self.source_name = source_name
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def fetch_page(self, url: str, timeout: int = 30) -> Optional[BeautifulSoup]:
        """Fetch a webpage and return BeautifulSoup object"""
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return None

    @abstractmethod
    def scrape_articles(self, max_articles: int = 10) -> List[Dict]:
        """
        Scrape articles from the source

        Returns:
            List of dictionaries with keys:
            - title: Article title
            - url: Article URL
            - content: Article content
            - published_at: Publication datetime
            - author: Author name (optional)
            - image_url: Image URL (optional)
            - tags: List of tags (optional)
        """
        pass

    @abstractmethod
    def extract_article_content(self, url: str) -> Optional[Dict]:
        """Extract full article content from URL"""
        pass

    def filter_ai_related(self, title: str, content: str) -> bool:
        """Check if article is AI-related"""
        ai_keywords = [
            'ai', 'artificial intelligence', 'machine learning', 'deep learning',
            'neural network', 'gpt', 'llm', 'generative', 'chatbot',
            'computer vision', 'nlp', 'natural language', 'robotics',
            'automation', 'algorithm', 'model', 'training', 'inference'
        ]

        text = (title + ' ' + content).lower()
        return any(keyword in text for keyword in ai_keywords)

    def clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        if not text:
            return ""
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text.strip()
