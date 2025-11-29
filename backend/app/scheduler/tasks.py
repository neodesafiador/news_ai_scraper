"""
Scheduled tasks for news scraping and processing
"""
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from sqlalchemy.orm import Session
import logging
import os

from ..database import SessionLocal
from ..models import Article
from ..scrapers import (
    TechCrunchScraper,
    VentureBeatScraper,
    MITTechReviewScraper,
    ArxivScraper
)
from ..ai import ArticleSummarizer, ArticleTranslator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NewsScraperScheduler:
    """Scheduler for automated news scraping and processing"""

    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scrapers = [
            TechCrunchScraper(),
            VentureBeatScraper(),
            MITTechReviewScraper(),
            ArxivScraper()
        ]

        # Load article limits from environment variables
        self.min_articles = int(os.getenv("MIN_ARTICLES_PER_SOURCE", "3"))
        self.max_articles = int(os.getenv("MAX_ARTICLES_PER_SOURCE", "5"))
        logger.info(f"Article limits configured: min={self.min_articles}, max={self.max_articles}")

        # Initialize AI components only if OpenAI API key is available
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            self.summarizer = ArticleSummarizer()
            self.translator = ArticleTranslator()
        else:
            logger.warning("OPENAI_API_KEY not found. AI features will be disabled.")
            self.summarizer = None
            self.translator = None

    def scrape_and_process(self):
        """Main task: scrape articles and process them with AI"""
        # Skip if AI components are not available
        if not self.summarizer or not self.translator:
            logger.warning("Skipping scraping task: AI components not initialized (missing OpenAI API key)")
            return

        logger.info("Starting scheduled scraping task...")

        db = SessionLocal()
        try:
            new_articles_count = 0

            for scraper in self.scrapers:
                logger.info(f"Scraping {scraper.source_name}...")

                try:
                    # Fetch articles with configured limits
                    articles = scraper.scrape_articles(max_articles=self.max_articles)

                    # Log article count
                    articles_count = len(articles)
                    logger.info(f"Fetched {articles_count} articles from {scraper.source_name}")

                    if articles_count < self.min_articles:
                        logger.warning(
                            f"Only {articles_count} articles fetched from {scraper.source_name}, "
                            f"which is below the minimum of {self.min_articles}"
                        )

                    for article_data in articles:
                        # Check if article already exists
                        existing = db.query(Article).filter(
                            Article.source_url == article_data['url']
                        ).first()

                        if existing:
                            logger.info(f"Article already exists: {article_data['url']}")
                            continue

                        # Process with AI
                        processed = self.process_article(article_data)

                        if processed:
                            # Create article record
                            article = Article(
                                source=scraper.source_name,
                                source_url=article_data['url'],
                                title_en=article_data['title'],
                                content_en=article_data['content'],
                                summary_en=processed['summary_en'],
                                title_ja=processed['title_ja'],
                                summary_ja=processed['summary_ja'],
                                key_points_ja=processed['key_points_ja'],
                                published_at=article_data['published_at'],
                                author=article_data.get('author'),
                                image_url=article_data.get('image_url'),
                                tags=article_data.get('tags', []),
                                category='AI',
                                is_processed=True,
                                is_published=True,
                                translated_at=datetime.now()
                            )

                            db.add(article)
                            db.commit()
                            new_articles_count += 1
                            logger.info(f"Saved article: {processed['title_ja'][:50]}...")

                except Exception as e:
                    logger.error(f"Error scraping {scraper.source_name}: {str(e)}")
                    continue

            logger.info(f"Scraping task completed. Added {new_articles_count} new articles.")

        except Exception as e:
            logger.error(f"Error in scraping task: {str(e)}")
            db.rollback()
        finally:
            db.close()

    def process_article(self, article_data: dict) -> dict:
        """
        Process article with AI: summarize and translate

        Args:
            article_data: Raw article data from scraper

        Returns:
            Processed article data with translations
        """
        try:
            # 1. Summarize in English
            logger.info("Summarizing article...")
            summary_en = self.summarizer.summarize(
                article_data['title'],
                article_data['content']
            )

            if not summary_en:
                logger.error("Failed to generate summary")
                return None

            # 2. Extract key points in English
            logger.info("Extracting key points...")
            key_points_en = self.summarizer.extract_key_points(
                article_data['title'],
                article_data['content']
            )

            if not key_points_en:
                logger.error("Failed to extract key points")
                return None

            # 3. Translate to Japanese
            logger.info("Translating to Japanese...")
            translation = self.translator.translate_article(
                article_data['title'],
                summary_en,
                key_points_en
            )

            if not translation:
                logger.error("Failed to translate article")
                return None

            return {
                'summary_en': summary_en,
                'title_ja': translation['title_ja'],
                'summary_ja': translation['summary_ja'],
                'key_points_ja': translation['key_points_ja']
            }

        except Exception as e:
            logger.error(f"Error processing article: {str(e)}")
            return None

    def start(self, interval_hours: int = 24):
        """
        Start the scheduler

        Args:
            interval_hours: Hours between scraping runs (default: 24)
        """
        # Schedule the scraping task
        self.scheduler.add_job(
            self.scrape_and_process,
            'interval',
            hours=interval_hours,
            id='scrape_news',
            name='Scrape and process AI news',
            replace_existing=True
        )

        # Run once immediately on startup
        self.scheduler.add_job(
            self.scrape_and_process,
            'date',
            run_date=datetime.now(),
            id='initial_scrape',
            name='Initial scraping run'
        )

        self.scheduler.start()
        logger.info(f"Scheduler started. Will run every {interval_hours} hours.")

    def stop(self):
        """Stop the scheduler"""
        self.scheduler.shutdown()
        logger.info("Scheduler stopped.")
