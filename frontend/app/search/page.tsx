/**
 * Search page with filters
 */
'use client';

import { useState, useEffect, Suspense } from 'react';
import { useSearchParams } from 'next/navigation';
import { apiClient, Article, SearchParams } from '@/lib/api';
import ArticleCard from '@/components/ArticleCard';
import SearchBar from '@/components/SearchBar';

function SearchContent() {
  const searchParams = useSearchParams();
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(true);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);

  const [tags, setTags] = useState<string[]>([]);
  const [categories, setCategories] = useState<string[]>([]);
  const [sources, setSources] = useState<string[]>([]);

  const [selectedTags, setSelectedTags] = useState<string>('');
  const [selectedCategory, setSelectedCategory] = useState<string>('');
  const [selectedSource, setSelectedSource] = useState<string>('');

  useEffect(() => {
    // Load filter options
    const loadFilters = async () => {
      try {
        const [tagsData, categoriesData, sourcesData] = await Promise.all([
          apiClient.getTags(),
          apiClient.getCategories(),
          apiClient.getSources(),
        ]);
        setTags(tagsData);
        setCategories(categoriesData);
        setSources(sourcesData);
      } catch (error) {
        console.error('Failed to load filters:', error);
      }
    };

    loadFilters();
  }, []);

  useEffect(() => {
    const keyword = searchParams.get('keyword') || '';
    const tagsParam = searchParams.get('tags') || '';
    const categoryParam = searchParams.get('category') || '';
    const sourceParam = searchParams.get('source') || '';

    setSelectedTags(tagsParam);
    setSelectedCategory(categoryParam);
    setSelectedSource(sourceParam);

    const searchArticles = async () => {
      setLoading(true);
      try {
        const params: SearchParams = {
          keyword: keyword || undefined,
          tags: tagsParam || undefined,
          category: categoryParam || undefined,
          source: sourceParam || undefined,
          page,
          page_size: 20,
        };

        const result = await apiClient.searchArticles(params);
        setArticles(result.articles);
        setTotal(result.total);
      } catch (error) {
        console.error('Search failed:', error);
        setArticles([]);
        setTotal(0);
      } finally {
        setLoading(false);
      }
    };

    searchArticles();
  }, [searchParams, page]);

  const handleFilterChange = (filterType: string, value: string) => {
    const params = new URLSearchParams(searchParams.toString());

    if (value) {
      params.set(filterType, value);
    } else {
      params.delete(filterType);
    }

    window.location.href = `/search?${params.toString()}`;
  };

  return (
    <div className="py-8">
      {/* Search Header */}
      <section className="bg-gradient-to-r from-purple-600 to-purple-800 text-white py-12 mb-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-bold mb-6 text-center">記事を検索</h1>
          <SearchBar />
        </div>
      </section>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Filters */}
        <div className="mb-8 bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-bold mb-4">絞り込み</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {/* Source filter */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                ソース
              </label>
              <select
                value={selectedSource}
                onChange={(e) => handleFilterChange('source', e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              >
                <option value="">すべて</option>
                {sources.map((source) => (
                  <option key={source} value={source}>
                    {source}
                  </option>
                ))}
              </select>
            </div>

            {/* Category filter */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                カテゴリー
              </label>
              <select
                value={selectedCategory}
                onChange={(e) => handleFilterChange('category', e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              >
                <option value="">すべて</option>
                {categories.map((category) => (
                  <option key={category} value={category}>
                    {category}
                  </option>
                ))}
              </select>
            </div>

            {/* Tags filter */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                タグ
              </label>
              <select
                value={selectedTags}
                onChange={(e) => handleFilterChange('tags', e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              >
                <option value="">すべて</option>
                {tags.map((tag) => (
                  <option key={tag} value={tag}>
                    {tag}
                  </option>
                ))}
              </select>
            </div>
          </div>
        </div>

        {/* Results */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">
            検索結果 ({total}件)
          </h2>

          {loading ? (
            <div className="text-center py-16">
              <div className="text-gray-500">読み込み中...</div>
            </div>
          ) : articles.length === 0 ? (
            <div className="text-center py-16">
              <div className="text-gray-500 text-lg">
                記事が見つかりませんでした
              </div>
            </div>
          ) : (
            <>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {articles.map((article) => (
                  <ArticleCard key={article.id} article={article} />
                ))}
              </div>

              {/* Pagination */}
              {total > 20 && (
                <div className="mt-8 flex justify-center gap-2">
                  <button
                    onClick={() => setPage(Math.max(1, page - 1))}
                    disabled={page === 1}
                    className="px-4 py-2 bg-gray-200 rounded-md hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    前へ
                  </button>
                  <span className="px-4 py-2">
                    {page} / {Math.ceil(total / 20)}
                  </span>
                  <button
                    onClick={() => setPage(page + 1)}
                    disabled={page >= Math.ceil(total / 20)}
                    className="px-4 py-2 bg-gray-200 rounded-md hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    次へ
                  </button>
                </div>
              )}
            </>
          )}
        </div>
      </div>
    </div>
  );
}

export default function SearchPage() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <SearchContent />
    </Suspense>
  );
}
