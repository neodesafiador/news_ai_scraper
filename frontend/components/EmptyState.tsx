/**
 * Empty state component for when no articles are available
 */

interface EmptyStateProps {
  title?: string;
  description?: string;
  icon?: 'articles' | 'search' | 'loading';
}

export default function EmptyState({
  title = '記事がまだありません',
  description = 'バックエンドサーバーが起動し、記事を収集するまでお待ちください',
  icon = 'articles'
}: EmptyStateProps) {
  const icons = {
    articles: (
      <svg className="w-24 h-24 mx-auto text-gray-300 mb-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z" />
      </svg>
    ),
    search: (
      <svg className="w-24 h-24 mx-auto text-gray-300 mb-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
      </svg>
    ),
    loading: (
      <svg className="w-24 h-24 mx-auto text-blue-500 mb-6 animate-spin" fill="none" viewBox="0 0 24 24">
        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
      </svg>
    )
  };

  return (
    <div className="text-center py-20 px-4">
      <div className="max-w-md mx-auto">
        {/* Icon */}
        {icons[icon]}

        {/* Title */}
        <h3 className="text-2xl font-bold text-gray-900 mb-3">
          {title}
        </h3>

        {/* Description */}
        <p className="text-gray-600 text-lg mb-8 leading-relaxed">
          {description}
        </p>

        {/* Decorative pulse animation for loading state */}
        {icon === 'loading' && (
          <div className="flex justify-center gap-2">
            <div className="w-3 h-3 bg-blue-500 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
            <div className="w-3 h-3 bg-blue-500 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
            <div className="w-3 h-3 bg-blue-500 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
          </div>
        )}
      </div>
    </div>
  );
}
