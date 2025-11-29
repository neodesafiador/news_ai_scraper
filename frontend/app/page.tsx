/**
 * Home page - Display latest AI news articles
 */
import { apiClient, Article } from '@/lib/api';
import ArticleCard from '@/components/ArticleCard';
import Hero from '@/components/Hero';
import EmptyState from '@/components/EmptyState';
import FeatureCard from '@/components/FeatureCard';

async function getLatestArticles(): Promise<Article[]> {
  try {
    return await apiClient.getLatestArticles(20);
  } catch (error) {
    console.error('Failed to fetch articles:', error);
    return [];
  }
}

export default async function Home() {
  const articles = await getLatestArticles();

  return (
    <div>
      {/* Hero Section */}
      <Hero />

      {/* Articles Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-20">
        {/* Section Header */}
        <div className="mb-12 text-center">
          <h2 className="text-4xl md:text-5xl font-extrabold text-gray-900 mb-4">
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600">
              最新記事
            </span>
          </h2>
          <p className="text-xl text-gray-600">
            毎日更新される最新のAI・機械学習ニュース
          </p>
          <div className="mt-4 w-24 h-1 bg-gradient-to-r from-blue-500 to-indigo-600 mx-auto rounded-full"></div>
        </div>

        {articles.length === 0 ? (
          <EmptyState />
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {articles.map((article) => (
              <ArticleCard key={article.id} article={article} />
            ))}
          </div>
        )}
      </section>

      {/* Features Section */}
      <section className="bg-gradient-to-br from-gray-50 to-blue-50 py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          {/* Section Header */}
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-extrabold text-gray-900 mb-4">
              <span className="bg-clip-text text-transparent bg-gradient-to-r from-purple-600 to-pink-600">
                機能
              </span>
            </h2>
            <p className="text-xl text-gray-600">
              最先端のAI技術で実現する、次世代ニュース体験
            </p>
            <div className="mt-4 w-24 h-1 bg-gradient-to-r from-purple-500 to-pink-600 mx-auto rounded-full"></div>
          </div>

          {/* Feature Cards Grid */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <FeatureCard
              icon="🤖"
              title="AI自動収集"
              description="TechCrunch、VentureBeat、MIT Tech Review、arXivなど主要なAIニュースサイトから、最新情報を自動で収集します。"
              gradient="from-blue-500 to-cyan-600"
            />
            <FeatureCard
              icon="🌏"
              title="日本語翻訳"
              description="最新のGPTモデルを使用して、英語記事を自然でわかりやすい日本語に翻訳。技術的な内容も正確に理解できます。"
              gradient="from-purple-500 to-pink-600"
            />
            <FeatureCard
              icon="📊"
              title="ポイント解説"
              description="記事の重要なポイントを自動抽出し、箇条書きで分かりやすく解説。短時間で核心を理解できます。"
              gradient="from-orange-500 to-red-600"
            />
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 text-center">
          <div className="p-6">
            <div className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600 mb-2">
              {articles.length}+
            </div>
            <div className="text-gray-600 font-medium">記事</div>
          </div>
          <div className="p-6">
            <div className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-pink-600 mb-2">
              4
            </div>
            <div className="text-gray-600 font-medium">ニュースソース</div>
          </div>
          <div className="p-6">
            <div className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-green-600 to-teal-600 mb-2">
              24h
            </div>
            <div className="text-gray-600 font-medium">自動更新</div>
          </div>
          <div className="p-6">
            <div className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-orange-600 to-red-600 mb-2">
              100%
            </div>
            <div className="text-gray-600 font-medium">AI翻訳</div>
          </div>
        </div>
      </section>
    </div>
  );
}
