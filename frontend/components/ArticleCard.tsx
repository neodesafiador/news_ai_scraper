/**
 * Article card component for displaying article preview
 */
import Link from 'next/link';
import { Article } from '@/lib/api';
import Badge from './Badge';

interface ArticleCardProps {
  article: Article;
}

export default function ArticleCard({ article }: ArticleCardProps) {
  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('ja-JP', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  };

  return (
    <Link href={`/article/${article.id}`}>
      <article className="group bg-white rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden cursor-pointer transform hover:-translate-y-1">
        {/* Image with overlay gradient */}
        {article.image_url && (
          <div className="relative h-52 w-full bg-gradient-to-br from-gray-200 to-gray-300 overflow-hidden">
            <img
              src={article.image_url}
              alt={article.title_ja}
              className="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>

            {/* Floating source badge */}
            <div className="absolute top-4 left-4">
              <Badge variant="primary" size="sm">
                {article.source}
              </Badge>
            </div>
          </div>
        )}

        <div className="p-6">
          {/* Date with icon */}
          <div className="flex items-center gap-2 text-sm text-gray-500 mb-4">
            <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
            <time>{formatDate(article.published_at)}</time>
          </div>

          {/* Title with gradient on hover */}
          <h2 className="text-xl font-bold text-gray-900 mb-3 line-clamp-2 group-hover:text-transparent group-hover:bg-clip-text group-hover:bg-gradient-to-r group-hover:from-blue-600 group-hover:to-indigo-600 transition-all duration-300">
            {article.title_ja}
          </h2>

          {/* Summary */}
          <p className="text-gray-600 mb-5 line-clamp-3 leading-relaxed">
            {article.summary_ja}
          </p>

          {/* Tags */}
          {article.tags && article.tags.length > 0 && (
            <div className="flex flex-wrap gap-2 mb-4">
              {article.tags.slice(0, 3).map((tag, index) => (
                <Badge key={index} variant="secondary" size="sm">
                  #{tag}
                </Badge>
              ))}
              {article.tags.length > 3 && (
                <Badge variant="outline" size="sm">
                  +{article.tags.length - 3}
                </Badge>
              )}
            </div>
          )}

          {/* Footer with author and read more */}
          <div className="flex items-center justify-between pt-4 border-t border-gray-100">
            {article.author && (
              <div className="flex items-center gap-2 text-sm text-gray-600">
                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
                <span>{article.author}</span>
              </div>
            )}

            <div className="flex items-center gap-2 text-blue-600 font-semibold text-sm group-hover:gap-3 transition-all duration-300">
              <span>続きを読む</span>
              <svg className="w-4 h-4 transform group-hover:translate-x-1 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </div>
          </div>
        </div>
      </article>
    </Link>
  );
}
