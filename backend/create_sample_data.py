"""
Create sample data for testing
"""
from datetime import datetime, timedelta
from app.database import SessionLocal, engine, Base
from app.models import Article

# Create tables
Base.metadata.create_all(bind=engine)

# Sample articles data
sample_articles = [
    {
        "source": "TechCrunch",
        "source_url": "https://techcrunch.com/sample-1",
        "title_en": "OpenAI Launches GPT-5 with Revolutionary Capabilities",
        "content_en": "OpenAI has announced the launch of GPT-5, its most advanced language model to date. The new model demonstrates unprecedented understanding and reasoning capabilities...",
        "summary_en": "OpenAI releases GPT-5 with major improvements in reasoning, context understanding, and multimodal capabilities.",
        "title_ja": "OpenAIが革新的な機能を持つGPT-5を発表",
        "summary_ja": "OpenAIが最新の大規模言語モデルGPT-5を発表しました。推論能力、文脈理解、マルチモーダル機能において大幅な改善が見られます。",
        "key_points_ja": [
            "GPT-4の10倍の推論能力を実現",
            "動画、音声、画像を統合したマルチモーダル処理が可能",
            "より正確で信頼性の高い回答を生成"
        ],
        "published_at": datetime.now() - timedelta(hours=2),
        "author": "TechCrunch Staff",
        "image_url": "https://via.placeholder.com/400x200?text=GPT-5",
        "tags": ["AI", "OpenAI", "GPT", "Language Model"],
        "category": "AI",
        "is_processed": True,
        "is_published": True,
        "translated_at": datetime.now()
    },
    {
        "source": "VentureBeat",
        "source_url": "https://venturebeat.com/sample-2",
        "title_en": "Google DeepMind Achieves Breakthrough in Protein Folding",
        "content_en": "Google DeepMind's latest AI system has achieved a major breakthrough in predicting protein structures...",
        "summary_en": "DeepMind's new AI model can predict complex protein structures with 99% accuracy.",
        "title_ja": "Google DeepMindがタンパク質折り畳みで画期的な成果",
        "summary_ja": "Google DeepMindの最新AIシステムが、複雑なタンパク質構造を99%の精度で予測することに成功しました。",
        "key_points_ja": [
            "従来のモデルより10倍高速な処理を実現",
            "創薬研究に革命をもたらす可能性",
            "オープンソースとして公開予定"
        ],
        "published_at": datetime.now() - timedelta(hours=5),
        "author": "VentureBeat Team",
        "image_url": "https://via.placeholder.com/400x200?text=DeepMind",
        "tags": ["AI", "DeepMind", "Protein", "Bioinformatics"],
        "category": "AI",
        "is_processed": True,
        "is_published": True,
        "translated_at": datetime.now()
    },
    {
        "source": "MIT Technology Review",
        "source_url": "https://technologyreview.com/sample-3",
        "title_en": "The Rise of Autonomous AI Agents in Enterprise",
        "content_en": "Autonomous AI agents are transforming how businesses operate, handling complex tasks without human intervention...",
        "summary_en": "Enterprise adoption of autonomous AI agents is accelerating, with major companies reporting significant productivity gains.",
        "title_ja": "企業における自律型AIエージェントの台頭",
        "summary_ja": "自律型AIエージェントの企業導入が加速しており、大手企業が大幅な生産性向上を報告しています。",
        "key_points_ja": [
            "業務プロセスの自動化により生産性が40%向上",
            "人間の監督を最小限に抑えた自律動作が可能",
            "2025年までに市場規模が200億ドルに達する見込み"
        ],
        "published_at": datetime.now() - timedelta(hours=8),
        "author": "MIT Tech Review",
        "image_url": "https://via.placeholder.com/400x200?text=AI+Agents",
        "tags": ["AI", "Enterprise", "Automation", "Agents"],
        "category": "AI",
        "is_processed": True,
        "is_published": True,
        "translated_at": datetime.now()
    },
    {
        "source": "arXiv",
        "source_url": "https://arxiv.org/sample-4",
        "title_en": "Transformer-XL: Attention Mechanisms Beyond Fixed-Length Context",
        "content_en": "We propose a novel transformer architecture that enables learning dependency beyond a fixed length without disrupting temporal coherence...",
        "summary_en": "Researchers introduce Transformer-XL, a new architecture that overcomes context length limitations in traditional transformers.",
        "title_ja": "固定長コンテキストを超えた注意機構を持つTransformer-XL",
        "summary_ja": "研究者たちが、従来のTransformerの文脈長制限を克服する新しいアーキテクチャ「Transformer-XL」を発表しました。",
        "key_points_ja": [
            "固定長の制約なしに長期依存関係を学習可能",
            "従来のTransformerより450%高速な推論速度",
            "言語モデリングタスクで新記録を達成"
        ],
        "published_at": datetime.now() - timedelta(hours=12),
        "author": "Dai et al.",
        "image_url": "https://via.placeholder.com/400x200?text=Research",
        "tags": ["Research", "Transformer", "NLP", "Machine Learning"],
        "category": "AI",
        "is_processed": True,
        "is_published": True,
        "translated_at": datetime.now()
    },
    {
        "source": "TechCrunch",
        "source_url": "https://techcrunch.com/sample-5",
        "title_en": "Anthropic Raises $4B to Compete with OpenAI",
        "content_en": "AI safety-focused company Anthropic has secured $4 billion in funding to accelerate development of its Claude AI assistant...",
        "summary_en": "Anthropic secures major funding round to expand Claude AI development and compete with OpenAI's ChatGPT.",
        "title_ja": "AnthropicがOpenAIと競争するため40億ドル調達",
        "summary_ja": "AI安全性に注力するAnthropic社が、Claude AIアシスタントの開発加速のため40億ドルの資金調達に成功しました。",
        "key_points_ja": [
            "Amazonが主要投資家として参加",
            "Claude 3が企業向けAI市場でシェアを拡大中",
            "安全性と信頼性を重視した開発方針"
        ],
        "published_at": datetime.now() - timedelta(hours=15),
        "author": "TechCrunch Staff",
        "image_url": "https://via.placeholder.com/400x200?text=Anthropic",
        "tags": ["AI", "Anthropic", "Claude", "Funding"],
        "category": "AI",
        "is_processed": True,
        "is_published": True,
        "translated_at": datetime.now()
    },
    {
        "source": "VentureBeat",
        "source_url": "https://venturebeat.com/sample-6",
        "title_en": "Computer Vision Advances Enable Real-Time 3D Reconstruction",
        "content_en": "New computer vision techniques allow for instant 3D scene reconstruction from 2D images...",
        "summary_en": "Breakthrough in computer vision enables real-time 3D reconstruction with applications in AR/VR and robotics.",
        "title_ja": "コンピュータビジョンの進歩によりリアルタイム3D再構築が可能に",
        "summary_ja": "最新のコンピュータビジョン技術により、2D画像から瞬時に3Dシーンを再構築できるようになりました。AR/VRやロボティクスへの応用が期待されます。",
        "key_points_ja": [
            "従来の1000倍の速度で3D再構築を実現",
            "スマートフォンでもリアルタイム処理が可能",
            "自動運転車やドローンへの応用が進行中"
        ],
        "published_at": datetime.now() - timedelta(hours=18),
        "author": "VentureBeat Team",
        "image_url": "https://via.placeholder.com/400x200?text=Computer+Vision",
        "tags": ["Computer Vision", "3D", "AR", "VR"],
        "category": "AI",
        "is_processed": True,
        "is_published": True,
        "translated_at": datetime.now()
    }
]

def create_sample_data():
    """Create sample articles in database"""
    db = SessionLocal()

    try:
        # Check if data already exists
        existing_count = db.query(Article).count()

        if existing_count > 0:
            print(f"Database already has {existing_count} articles. Skipping sample data creation.")
            return

        # Insert sample articles
        for article_data in sample_articles:
            article = Article(**article_data)
            db.add(article)

        db.commit()
        print(f"Successfully created {len(sample_articles)} sample articles!")

    except Exception as e:
        print(f"Error creating sample data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_sample_data()
