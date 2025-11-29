"""
News scrapers for various sources
"""
from .base import BaseScraper
from .techcrunch import TechCrunchScraper
from .venturebeat import VentureBeatScraper
from .mit_tech_review import MITTechReviewScraper
from .arxiv import ArxivScraper

__all__ = [
    "BaseScraper",
    "TechCrunchScraper",
    "VentureBeatScraper",
    "MITTechReviewScraper",
    "ArxivScraper",
]
