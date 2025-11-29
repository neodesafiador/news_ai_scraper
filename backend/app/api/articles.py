"""
Article API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List, Optional
from datetime import datetime

from ..database import get_db
from ..models import Article
from ..schemas import ArticleResponse, ArticleDetailResponse, ArticleList

router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("/", response_model=ArticleList)
def get_articles(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    source: Optional[str] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Get paginated list of published articles

    Args:
        page: Page number (starting from 1)
        page_size: Number of articles per page
        source: Filter by source (e.g., TechCrunch)
        category: Filter by category
    """
    query = db.query(Article).filter(Article.is_published == True)

    if source:
        query = query.filter(Article.source == source)

    if category:
        query = query.filter(Article.category == category)

    # Get total count
    total = query.count()

    # Get paginated results
    articles = (
        query.order_by(desc(Article.published_at))
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

    return ArticleList(
        total=total,
        articles=articles,
        page=page,
        page_size=page_size
    )


@router.get("/latest", response_model=List[ArticleResponse])
def get_latest_articles(
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    """Get latest published articles"""
    articles = (
        db.query(Article)
        .filter(Article.is_published == True)
        .order_by(desc(Article.published_at))
        .limit(limit)
        .all()
    )

    return articles


@router.get("/{article_id}", response_model=ArticleDetailResponse)
def get_article(article_id: int, db: Session = Depends(get_db)):
    """Get detailed article by ID"""
    article = db.query(Article).filter(Article.id == article_id).first()

    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    return article


@router.get("/source/{source_name}", response_model=List[ArticleResponse])
def get_articles_by_source(
    source_name: str,
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Get articles from a specific source"""
    articles = (
        db.query(Article)
        .filter(Article.source == source_name, Article.is_published == True)
        .order_by(desc(Article.published_at))
        .limit(limit)
        .all()
    )

    return articles


@router.get("/category/{category_name}", response_model=List[ArticleResponse])
def get_articles_by_category(
    category_name: str,
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Get articles by category"""
    articles = (
        db.query(Article)
        .filter(Article.category == category_name, Article.is_published == True)
        .order_by(desc(Article.published_at))
        .limit(limit)
        .all()
    )

    return articles


@router.get("/tags/{tag}", response_model=List[ArticleResponse])
def get_articles_by_tag(
    tag: str,
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Get articles by tag"""
    articles = (
        db.query(Article)
        .filter(Article.tags.contains([tag]), Article.is_published == True)
        .order_by(desc(Article.published_at))
        .limit(limit)
        .all()
    )

    return articles
