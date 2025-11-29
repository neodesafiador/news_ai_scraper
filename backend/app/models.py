"""
SQLAlchemy database models
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.types import TypeDecorator, String as SQLString
from .database import Base, DATABASE_URL
import json


# Custom type for storing arrays as JSON in SQLite, or native ARRAY in PostgreSQL
class JSONEncodedList(TypeDecorator):
    """Store list as JSON string in SQLite, use native ARRAY in PostgreSQL"""
    impl = SQLString
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        if dialect.name == 'postgresql':
            return value
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        if dialect.name == 'postgresql':
            return value
        return json.loads(value) if value else []


class Article(Base):
    """Article model for storing news articles"""
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)

    # Source information
    source = Column(String(100), nullable=False, index=True)  # TechCrunch, VentureBeat, etc.
    source_url = Column(String(500), unique=True, nullable=False)

    # Original content (English)
    title_en = Column(String(500), nullable=False)
    content_en = Column(Text, nullable=False)
    summary_en = Column(Text)

    # Translated content (Japanese)
    title_ja = Column(String(500), nullable=False)
    summary_ja = Column(Text, nullable=False)
    key_points_ja = Column(JSONEncodedList(500))  # ポイント解説を配列で保存

    # Metadata
    published_at = Column(DateTime, nullable=False)
    scraped_at = Column(DateTime, server_default=func.now())
    translated_at = Column(DateTime)

    # Categorization
    tags = Column(JSONEncodedList(500))  # AI, Machine Learning, etc.
    category = Column(String(100), index=True)

    # Status
    is_processed = Column(Boolean, default=False)
    is_published = Column(Boolean, default=False)

    # SEO
    image_url = Column(String(500))
    author = Column(String(200))

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Article {self.id}: {self.title_ja[:30]}>"
