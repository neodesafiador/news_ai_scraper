/**
 * API client for backend communication
 */

// Server-side: Use internal Docker network (backend container)
// Client-side: Use localhost (browser access)
function getAPIURL() {
  // Server-side rendering
  if (typeof window === 'undefined') {
    return process.env.API_URL || 'http://backend:8000';
  }
  // Client-side rendering
  return process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
}

const API_URL = getAPIURL();

export interface Article {
  id: number;
  source: string;
  source_url: string;
  title_ja: string;
  summary_ja: string;
  key_points_ja?: string[];
  tags?: string[];
  category?: string;
  image_url?: string;
  published_at: string;
  scraped_at: string;
  author?: string;
  is_published: boolean;
  created_at: string;
}

export interface ArticleDetail extends Article {
  title_en: string;
  summary_en?: string;
  content_en: string;
  translated_at?: string;
  updated_at?: string;
}

export interface ArticleList {
  total: number;
  articles: Article[];
  page: number;
  page_size: number;
}

export interface SearchParams {
  keyword?: string;
  tags?: string;
  category?: string;
  source?: string;
  date_from?: string;
  date_to?: string;
  page?: number;
  page_size?: number;
}

class APIClient {
  private baseURL: string;

  constructor(baseURL: string = API_URL) {
    this.baseURL = baseURL;
  }

  private async request<T>(endpoint: string, options?: RequestInit): Promise<T> {
    // Recalculate URL each time to handle SSR vs CSR
    const baseURL = getAPIURL();
    const url = `${baseURL}${endpoint}`;

    try {
      const response = await fetch(url, {
        ...options,
        headers: {
          'Content-Type': 'application/json',
          ...options?.headers,
        },
        // Prevent caching issues
        cache: 'no-store',
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.error('API request failed:', error, 'URL:', url);
      throw error;
    }
  }

  // Get articles with pagination
  async getArticles(page: number = 1, pageSize: number = 20): Promise<ArticleList> {
    return this.request<ArticleList>(`/articles/?page=${page}&page_size=${pageSize}`);
  }

  // Get latest articles
  async getLatestArticles(limit: number = 10): Promise<Article[]> {
    return this.request<Article[]>(`/articles/latest?limit=${limit}`);
  }

  // Get article by ID
  async getArticle(id: number): Promise<ArticleDetail> {
    return this.request<ArticleDetail>(`/articles/${id}`);
  }

  // Get articles by source
  async getArticlesBySource(source: string, limit: number = 20): Promise<Article[]> {
    return this.request<Article[]>(`/articles/source/${source}?limit=${limit}`);
  }

  // Get articles by category
  async getArticlesByCategory(category: string, limit: number = 20): Promise<Article[]> {
    return this.request<Article[]>(`/articles/category/${category}?limit=${limit}`);
  }

  // Get articles by tag
  async getArticlesByTag(tag: string, limit: number = 20): Promise<Article[]> {
    return this.request<Article[]>(`/articles/tags/${tag}?limit=${limit}`);
  }

  // Search articles
  async searchArticles(params: SearchParams): Promise<ArticleList> {
    const queryParams = new URLSearchParams();

    Object.entries(params).forEach(([key, value]) => {
      if (value !== undefined && value !== null) {
        queryParams.append(key, value.toString());
      }
    });

    return this.request<ArticleList>(`/search/?${queryParams.toString()}`);
  }

  // Get all tags
  async getTags(): Promise<string[]> {
    return this.request<string[]>('/search/tags');
  }

  // Get all categories
  async getCategories(): Promise<string[]> {
    return this.request<string[]>('/search/categories');
  }

  // Get all sources
  async getSources(): Promise<string[]> {
    return this.request<string[]>('/search/sources');
  }
}

export const apiClient = new APIClient();
