"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import List, Optional


class ArticleBase(BaseModel):
    """Base article schema"""
    source: str
    title_ja: str
    summary_ja: str
    key_points_ja: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    category: Optional[str] = None
    image_url: Optional[str] = None


class ArticleCreate(BaseModel):
    """Schema for creating an article"""
    source: str
    source_url: str
    title_en: str
    content_en: str
    published_at: datetime
    author: Optional[str] = None
    image_url: Optional[str] = None


class ArticleResponse(ArticleBase):
    """Schema for article response"""
    id: int
    source_url: str
    published_at: datetime
    scraped_at: datetime
    author: Optional[str] = None
    is_published: bool
    created_at: datetime

    class Config:
        from_attributes = True


class ArticleDetailResponse(ArticleResponse):
    """Schema for detailed article response"""
    title_en: str
    summary_en: Optional[str] = None
    content_en: str
    translated_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ArticleList(BaseModel):
    """Schema for article list response"""
    total: int
    articles: List[ArticleResponse]
    page: int
    page_size: int


class SearchQuery(BaseModel):
    """Schema for search query"""
    keyword: Optional[str] = None
    tags: Optional[List[str]] = None
    category: Optional[str] = None
    source: Optional[str] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    page: int = 1
    page_size: int = 20
