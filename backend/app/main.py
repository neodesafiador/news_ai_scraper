"""
FastAPI main application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

from .database import engine, Base
from .api import articles, search
from .scheduler import NewsScraperScheduler

load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize scheduler
scheduler = NewsScraperScheduler()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events"""
    # Startup
    scraping_interval = int(os.getenv("SCRAPING_INTERVAL_HOURS", "24"))
    scheduler.start(interval_hours=scraping_interval)
    yield
    # Shutdown
    scheduler.stop()


# Create FastAPI app
app = FastAPI(
    title="AI News Scraper API",
    description="API for AI news aggregation, summarization, and translation",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
cors_origins_str = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:3001")
cors_origins = [origin.strip() for origin in cors_origins_str.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(articles.router)
app.include_router(search.router)


@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "AI News Scraper API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "scheduler_running": scheduler.scheduler.running
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", "8000")),
        reload=os.getenv("DEBUG", "True") == "True"
    )
