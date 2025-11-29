"""
Search API endpoints
"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, desc, func, text
from typing import Optional, List
from datetime import datetime

from ..database import get_db
from ..models import Article
from ..schemas import ArticleList, SearchQuery

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/", response_model=ArticleList)
def search_articles(
    keyword: Optional[str] = Query(None, description="Search keyword"),
    tags: Optional[str] = Query(None, description="Comma-separated tags"),
    category: Optional[str] = Query(None, description="Filter by category"),
    source: Optional[str] = Query(None, description="Filter by source"),
    date_from: Optional[datetime] = Query(None, description="Start date"),
    date_to: Optional[datetime] = Query(None, description="End date"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Search articles with various filters

    Args:
        keyword: Search in title and summary (Japanese)
        tags: Filter by tags (comma-separated)
        category: Filter by category
        source: Filter by source
        date_from: Filter articles from this date
        date_to: Filter articles until this date
        page: Page number
        page_size: Number of results per page
    """
    query = db.query(Article).filter(Article.is_published == True)

    # Keyword search (search in Japanese title and summary)
    if keyword:
        search_filter = or_(
            Article.title_ja.ilike(f"%{keyword}%"),
            Article.summary_ja.ilike(f"%{keyword}%")
        )
        query = query.filter(search_filter)

    # Tag filter
    if tags:
        tag_list = [tag.strip() for tag in tags.split(',')]
        for tag in tag_list:
            query = query.filter(Article.tags.contains([tag]))

    # Category filter
    if category:
        query = query.filter(Article.category == category)

    # Source filter
    if source:
        query = query.filter(Article.source == source)

    # Date range filter
    if date_from:
        query = query.filter(Article.published_at >= date_from)

    if date_to:
        query = query.filter(Article.published_at <= date_to)

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


@router.get("/tags", response_model=List[str])
def get_all_tags(db: Session = Depends(get_db)):
    """Get all unique tags used in articles"""
    # Get all articles with tags
    articles = (
        db.query(Article.tags)
        .filter(Article.is_published == True, Article.tags.isnot(None))
        .all()
    )

    # Flatten and deduplicate tags using Python
    all_tags = set()
    for article in articles:
        if article[0]:  # article[0] is the tags array
            all_tags.update(article[0])

    # Return sorted unique tags
    return sorted(list(all_tags))


@router.get("/categories", response_model=List[str])
def get_all_categories(db: Session = Depends(get_db)):
    """Get all unique categories"""
    categories = (
        db.query(Article.category)
        .filter(Article.is_published == True, Article.category.isnot(None))
        .distinct()
        .order_by(Article.category)
        .all()
    )

    return [cat[0] for cat in categories if cat[0]]


@router.get("/sources", response_model=List[str])
def get_all_sources(db: Session = Depends(get_db)):
    """Get all unique sources"""
    sources = (
        db.query(Article.source)
        .filter(Article.is_published == True)
        .distinct()
        .order_by(Article.source)
        .all()
    )

    return [source[0] for source in sources]
