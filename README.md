# AI News Japan 🤖📰

海外のAIニュースを自動収集し、日本語で配信するWebアプリケーション

## 📋 概要

AI News Japanは、TechCrunch、VentureBeat、MIT Technology Review、arXivなどの主要なAI関連ニュースソースから記事を自動収集し、GPT-5を使って日本語に翻訳・要約するWebアプリケーションです。

### 主な機能

- 🔍 **自動ニュース収集**: 複数のソースから毎日AIニュースを自動収集
- 🌏 **AI翻訳**: OpenAI GPT-5を使った高品質な日本語翻訳
- 📊 **要約とポイント解説**: 記事の重要なポイントを分かりやすく提示
- 🔎 **高度な検索**: キーワード、タグ、カテゴリー、ソースで検索可能
- 📱 **レスポンシブデザイン**: モバイル・タブレット・デスクトップ対応

## 🏗️ アーキテクチャ

### バックエンド
- **言語**: Python 3.11+
- **フレームワーク**: FastAPI
- **AI/ML**: LangChain + OpenAI API (GPT-5)
- **データベース**: PostgreSQL
- **スクレイピング**: BeautifulSoup, Feedparser, Requests
- **スケジューラー**: APScheduler

### フロントエンド
- **フレームワーク**: Next.js 15 (App Router)
- **言語**: TypeScript
- **スタイリング**: Tailwind CSS
- **UI**: React Server Components

### インフラ
- **コンテナ**: Docker + Docker Compose
- **データベース**: PostgreSQL 15

## 📁 プロジェクト構造

```
news_scraper/
├── backend/
│   ├── app/
│   │   ├── api/              # API エンドポイント
│   │   │   ├── articles.py   # 記事API
│   │   │   └── search.py     # 検索API
│   │   ├── scrapers/         # ニュースクローラー
│   │   │   ├── base.py       # ベーススクレイパー
│   │   │   ├── techcrunch.py
│   │   │   ├── venturebeat.py
│   │   │   ├── mit_tech_review.py
│   │   │   └── arxiv.py
│   │   ├── ai/               # AI処理
│   │   │   ├── summarizer.py # 要約
│   │   │   └── translator.py # 翻訳
│   │   ├── scheduler/        # 自動更新
│   │   │   └── tasks.py
│   │   ├── models.py         # データベースモデル
│   │   ├── schemas.py        # Pydanticスキーマ
│   │   ├── database.py       # DB接続
│   │   └── main.py           # FastAPIアプリ
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── app/
│   │   ├── page.tsx          # ホームページ
│   │   ├── article/[id]/     # 記事詳細ページ
│   │   ├── search/           # 検索ページ
│   │   └── about/            # Aboutページ
│   ├── components/           # Reactコンポーネント
│   ├── lib/
│   │   └── api.ts            # APIクライアント
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🚀 セットアップ

### 前提条件

- Docker & Docker Compose
- OpenAI API キー

### インストール手順

1. **リポジトリのクローン**

```bash
cd news_scraper
```

2. **環境変数の設定**

バックエンドの環境変数を設定：

```bash
cd backend
cp .env.example .env
```

`.env` ファイルを編集して、OpenAI API キーを設定：

```env
DATABASE_URL=postgresql://ainews:ainews_password@postgres:5432/ai_news_db
OPENAI_API_KEY=your_openai_api_key_here
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=http://localhost:3000
SCRAPING_INTERVAL_HOURS=24
# Number of articles to fetch per source (minimum: 3, maximum: 5)
MIN_ARTICLES_PER_SOURCE=3
MAX_ARTICLES_PER_SOURCE=5
```

**記事収集設定の説明**:
- `MIN_ARTICLES_PER_SOURCE`: 各ニュースソースから取得する最低記事数（デフォルト: 3）
- `MAX_ARTICLES_PER_SOURCE`: 各ニュースソースから取得する最大記事数（デフォルト: 5）
- これらの値を変更することで、記事の収集数を調整できます

3. **Dockerコンテナの起動**

プロジェクトルートディレクトリで：

```bash
docker-compose up --build
```

これにより以下が起動します：
- PostgreSQLデータベース (ポート 5432)
- FastAPIバックエンド (ポート 8000)
- Next.jsフロントエンド (ポート 3000)

4. **アプリケーションへアクセス**

- フロントエンド: http://localhost:3000
- バックエンドAPI: http://localhost:8000
- API ドキュメント: http://localhost:8000/docs

## 🔧 開発

### バックエンド開発

```bash
cd backend

# 仮想環境の作成
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存関係のインストール
pip install -r requirements.txt

# 開発サーバーの起動
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### フロントエンド開発

```bash
cd frontend

# 依存関係のインストール
npm install

# 開発サーバーの起動
npm run dev
```

## 📡 API エンドポイント

### 記事取得

- `GET /articles/` - 記事一覧（ページネーション）
- `GET /articles/latest` - 最新記事
- `GET /articles/{id}` - 記事詳細
- `GET /articles/source/{source}` - ソース別記事
- `GET /articles/category/{category}` - カテゴリー別記事
- `GET /articles/tags/{tag}` - タグ別記事

### 検索

- `GET /search/` - 記事検索（キーワード、タグ、カテゴリー、ソース、日付範囲）
- `GET /search/tags` - 全タグ取得
- `GET /search/categories` - 全カテゴリー取得
- `GET /search/sources` - 全ソース取得

### ヘルスチェック

- `GET /health` - アプリケーションの状態確認

## 🔄 自動更新

アプリケーションは起動時にすぐに記事の収集を開始し、その後24時間ごとに自動で新しい記事を収集します。

収集間隔は環境変数 `SCRAPING_INTERVAL_HOURS` で変更可能です。

## 🎨 カスタマイズ

### 新しいニュースソースの追加

1. `backend/app/scrapers/` に新しいスクレイパーファイルを作成
2. `BaseScraper` を継承してクラスを実装
3. `backend/app/scrapers/__init__.py` にインポートを追加
4. `backend/app/scheduler/tasks.py` の `scrapers` リストに追加

### AI モデルの変更

`backend/app/ai/summarizer.py` と `translator.py` の `__init__` メソッドで使用するモデルを変更：

```python
def __init__(self, model: str = "gpt-4-turbo", temperature: float = 0.3):
```

## 📊 データベーススキーマ

### Articles テーブル

| カラム | 型 | 説明 |
|--------|------|------|
| id | Integer | 主キー |
| source | String | ニュースソース |
| source_url | String | 元記事URL |
| title_en | String | 英語タイトル |
| content_en | Text | 英語本文 |
| summary_en | Text | 英語要約 |
| title_ja | String | 日本語タイトル |
| summary_ja | Text | 日本語要約 |
| key_points_ja | Array[String] | 重要ポイント |
| published_at | DateTime | 公開日時 |
| tags | Array[String] | タグ |
| category | String | カテゴリー |
| image_url | String | 画像URL |
| author | String | 著者 |
| is_processed | Boolean | 処理済みフラグ |
| is_published | Boolean | 公開フラグ |

## 🛠️ トラブルシューティング

### データベース接続エラー

PostgreSQLコンテナが起動していることを確認：

```bash
docker-compose ps
```

### フロントエンド "fetch failed" エラー

Next.js 15のServer Componentsはサーバーサイドでレンダリングされます。以下を確認：

1. **Dockerで実行している場合**：
   - docker-compose.ymlに`API_URL=http://backend:8000`が設定されているか確認
   - バックエンドコンテナが起動しているか確認：`docker-compose ps`

2. **ローカル開発の場合**：
   - `.env.local`に以下が設定されているか確認：
     ```
     API_URL=http://localhost:8000
     NEXT_PUBLIC_API_URL=http://localhost:8000
     ```
   - バックエンドが http://localhost:8000 で起動しているか確認

3. **CORS エラーの場合**：
   - バックエンドのCORS設定を確認
   - docker-compose.ymlの`CORS_ORIGINS`に正しいフロントエンドURLが含まれているか確認

### OpenAI API エラー

- APIキーが正しく設定されているか確認
- APIクォータが残っているか確認
- レート制限に達していないか確認

### スクレイピングエラー

- 対象サイトがアクセス可能か確認
- RSSフィードURLが変更されていないか確認
- robots.txtに準拠しているか確認

## ⚠️ 免責事項

- このアプリケーションは自動翻訳を使用しているため、翻訳の正確性は保証されません
- 重要な情報については必ず元記事を確認してください
- スクレイピングは各サイトの利用規約とrobots.txtに従ってください

