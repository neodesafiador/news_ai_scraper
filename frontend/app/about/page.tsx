/**
 * About page
 */
export default function AboutPage() {
  return (
    <div className="py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold text-gray-900 mb-8">
          AI News Japan について
        </h1>

        <div className="prose prose-lg max-w-none">
          <section className="mb-12">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              サービス概要
            </h2>
            <p className="text-gray-700 leading-relaxed mb-4">
              AI News Japan は、海外の主要なAI・機械学習ニュースを自動収集し、
              やさしい日本語で配信するWebサービスです。
            </p>
            <p className="text-gray-700 leading-relaxed">
              最新のAI技術を使って、英語の専門記事を分かりやすく翻訳・要約し、
              日本語で読めるようにしています。
            </p>
          </section>

          <section className="mb-12">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              収集ソース
            </h2>
            <ul className="list-disc list-inside space-y-2 text-gray-700">
              <li>
                <strong>TechCrunch:</strong> テクノロジースタートアップのニュース
              </li>
              <li>
                <strong>VentureBeat:</strong> AIとビジネスの最新情報
              </li>
              <li>
                <strong>MIT Technology Review:</strong> 技術的な深掘り記事
              </li>
              <li>
                <strong>arXiv:</strong> 最新の研究論文（AI/ML分野）
              </li>
            </ul>
          </section>

          <section className="mb-12">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              技術スタック
            </h2>
            <div className="bg-gray-50 p-6 rounded-lg">
              <h3 className="font-bold text-gray-900 mb-2">バックエンド</h3>
              <ul className="list-disc list-inside mb-4 text-gray-700">
                <li>Python + FastAPI</li>
                <li>LangChain + OpenAI GPT-5</li>
                <li>PostgreSQL</li>
                <li>BeautifulSoup & Feedparser（スクレイピング）</li>
              </ul>

              <h3 className="font-bold text-gray-900 mb-2">フロントエンド</h3>
              <ul className="list-disc list-inside mb-4 text-gray-700">
                <li>Next.js 15 (App Router)</li>
                <li>TypeScript</li>
                <li>Tailwind CSS</li>
              </ul>

              <h3 className="font-bold text-gray-900 mb-2">インフラ</h3>
              <ul className="list-disc list-inside text-gray-700">
                <li>Docker & Docker Compose</li>
              </ul>
            </div>
          </section>

          <section className="mb-12">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              主な機能
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="bg-blue-50 p-6 rounded-lg">
                <h3 className="font-bold text-blue-900 mb-2">
                  自動ニュース収集
                </h3>
                <p className="text-gray-700">
                  毎日自動で海外のAIニュースサイトから最新記事を収集
                </p>
              </div>

              <div className="bg-green-50 p-6 rounded-lg">
                <h3 className="font-bold text-green-900 mb-2">
                  AI要約・翻訳
                </h3>
                <p className="text-gray-700">
                  GPT-5で英語記事を要約し、やさしい日本語に翻訳
                </p>
              </div>

              <div className="bg-purple-50 p-6 rounded-lg">
                <h3 className="font-bold text-purple-900 mb-2">
                  ポイント解説
                </h3>
                <p className="text-gray-700">
                  記事の重要なポイントを箇条書きで分かりやすく解説
                </p>
              </div>

              <div className="bg-orange-50 p-6 rounded-lg">
                <h3 className="font-bold text-orange-900 mb-2">
                  高度な検索
                </h3>
                <p className="text-gray-700">
                  キーワード、タグ、カテゴリーで記事を簡単に検索
                </p>
              </div>
            </div>
          </section>

          <section className="mb-12">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              更新頻度
            </h2>
            <p className="text-gray-700 leading-relaxed">
              記事は毎日自動で更新されます。最新のAI・機械学習ニュースを
              いち早く日本語で読むことができます。
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              免責事項
            </h2>
            <p className="text-gray-700 leading-relaxed text-sm">
              本サービスで提供される記事は、AIによって自動的に翻訳・要約されています。
              翻訳の正確性については保証いたしかねますので、
              重要な情報については元記事をご確認ください。
            </p>
          </section>
        </div>
      </div>
    </div>
  );
}
