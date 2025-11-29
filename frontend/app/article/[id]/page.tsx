/**
 * Article detail page with modern design
 */
import { apiClient, ArticleDetail } from '@/lib/api';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import Badge from '@/components/Badge';
import KeyPoints from '@/components/KeyPoints';

async function getArticle(id: number): Promise<ArticleDetail | null> {
  try {
    return await apiClient.getArticle(id);
  } catch (error) {
    console.error('Failed to fetch article:', error);
    return null;
  }
}

export default async function ArticlePage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const article = await getArticle(parseInt(id));

  if (!article) {
    notFound();
  }

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('ja-JP', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="py-12 bg-gradient-to-br from-gray-50 to-blue-50 min-h-screen">
      <article className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Breadcrumb */}
        <nav className="mb-8">
          <Link
            href="/"
            className="inline-flex items-center gap-2 px-4 py-2 bg-white rounded-xl text-gray-700 hover:text-blue-600 hover:bg-blue-50 transition-all duration-200 shadow-md hover:shadow-lg group"
          >
            <svg
              className="w-5 h-5 transform group-hover:-translate-x-1 transition-transform duration-200"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M15 19l-7-7 7-7"
              />
            </svg>
            記事一覧に戻る
          </Link>
        </nav>

        {/* Article Card Container */}
        <div className="bg-white rounded-3xl shadow-2xl overflow-hidden">
          {/* Article Header */}
          <header className="p-8 md:p-12">
            {/* Badges */}
            <div className="flex flex-wrap items-center gap-3 mb-6">
              <Badge variant="primary" size="md">
                {article.source}
              </Badge>
              {article.category && (
                <Badge variant="info" size="md">
                  {article.category}
                </Badge>
              )}
            </div>

            {/* Title */}
            <h1 className="text-4xl md:text-5xl font-extrabold text-gray-900 mb-6 leading-tight">
              {article.title_ja}
            </h1>

            {/* Meta Information */}
            <div className="flex flex-wrap items-center gap-6 text-gray-600 mb-8">
              <div className="flex items-center gap-2">
                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                <time className="font-medium">{formatDate(article.published_at)}</time>
              </div>
              {article.author && (
                <div className="flex items-center gap-2">
                  <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                  <span className="font-medium">{article.author}</span>
                </div>
              )}
            </div>

            {/* Featured Image */}
            {article.image_url && (
              <div className="mb-8 rounded-2xl overflow-hidden shadow-lg">
                <img
                  src={article.image_url}
                  alt={article.title_ja}
                  className="w-full h-auto"
                />
              </div>
            )}
          </header>

          {/* Article Body */}
          <div className="px-8 md:px-12 pb-12">
            {/* Summary */}
            <section className="mb-8 p-8 bg-gradient-to-br from-blue-50 to-indigo-50 rounded-2xl border-2 border-blue-100 shadow-lg">
              <div className="flex items-center gap-3 mb-4">
                <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-xl flex items-center justify-center">
                  <svg className="w-6 h-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                </div>
                <h2 className="text-2xl font-bold text-gray-900">
                  要約
                </h2>
              </div>
              <p className="text-gray-800 text-lg leading-relaxed">
                {article.summary_ja}
              </p>
            </section>

            {/* Key Points */}
            {article.key_points_ja && article.key_points_ja.length > 0 && (
              <KeyPoints points={article.key_points_ja} />
            )}

            {/* Tags */}
            {article.tags && article.tags.length > 0 && (
              <section className="mb-8">
                <h3 className="text-xl font-bold text-gray-900 mb-4 flex items-center gap-2">
                  <svg className="w-6 h-6 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
                  </svg>
                  タグ
                </h3>
                <div className="flex flex-wrap gap-3">
                  {article.tags.map((tag, index) => (
                    <Badge
                      key={index}
                      variant="secondary"
                      size="lg"
                      href={`/search?tags=${encodeURIComponent(tag)}`}
                    >
                      #{tag}
                    </Badge>
                  ))}
                </div>
              </section>
            )}

            {/* Original Article Link */}
            <section className="mb-8 p-8 bg-gradient-to-br from-gray-50 to-gray-100 rounded-2xl border-2 border-gray-200 shadow-lg">
              <h3 className="text-xl font-bold text-gray-900 mb-4 flex items-center gap-2">
                <svg className="w-6 h-6 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                元記事（英語）
              </h3>
              <p className="text-gray-700 mb-4 text-lg">
                <strong>タイトル:</strong> {article.title_en}
              </p>
              <a
                href={article.source_url}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-indigo-600 text-white font-semibold rounded-xl hover:from-blue-600 hover:to-indigo-700 transition-all duration-200 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
              >
                元記事を読む
                <svg
                  className="w-5 h-5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
                  />
                </svg>
              </a>
            </section>

            {/* AI Notice */}
            <section className="border-t-2 border-gray-200 pt-8">
              <div className="flex items-start gap-3 text-gray-600">
                <svg className="w-6 h-6 flex-shrink-0 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <p className="leading-relaxed">
                  この記事は AI によって自動翻訳・要約されています。重要な情報については、必ず元記事をご確認ください。
                </p>
              </div>
            </section>
          </div>
        </div>
      </article>
    </div>
  );
}
