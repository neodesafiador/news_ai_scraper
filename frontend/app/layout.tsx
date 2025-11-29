import type { Metadata } from "next";
import { Noto_Sans_JP } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";

const notoSansJP = Noto_Sans_JP({
  subsets: ["latin"],
  weight: ["400", "500", "700"],
});

export const metadata: Metadata = {
  title: "AI News Japan - 最新のAIニュースを日本語で",
  description: "海外のAIニュースを自動収集し、やさしい日本語で配信します",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja">
      <body className={`${notoSansJP.className} antialiased bg-gray-50`}>
        <Header />
        <main className="min-h-screen">
          {children}
        </main>
        <footer className="bg-gradient-to-br from-gray-900 via-blue-900 to-indigo-900 text-white py-12 mt-20">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            {/* Footer Content */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
              {/* Brand */}
              <div>
                <div className="flex items-center gap-3 mb-4">
                  <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-xl flex items-center justify-center">
                    <svg className="w-6 h-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                    </svg>
                  </div>
                  <span className="text-xl font-bold">AI News Japan</span>
                </div>
                <p className="text-gray-300 text-sm leading-relaxed">
                  最新のAIニュースを、やさしい日本語で配信します。
                </p>
              </div>

              {/* Links */}
              <div>
                <h3 className="font-bold mb-4 text-blue-300">サイト</h3>
                <ul className="space-y-2 text-sm">
                  <li>
                    <a href="/" className="text-gray-300 hover:text-white transition-colors">ホーム</a>
                  </li>
                  <li>
                    <a href="/search" className="text-gray-300 hover:text-white transition-colors">検索</a>
                  </li>
                  <li>
                    <a href="/about" className="text-gray-300 hover:text-white transition-colors">について</a>
                  </li>
                </ul>
              </div>

              {/* Tech Stack */}
              <div>
                <h3 className="font-bold mb-4 text-blue-300">技術スタック</h3>
                <div className="flex flex-wrap gap-2">
                  <span className="text-xs bg-white/10 text-gray-200 px-3 py-1 rounded-full">Next.js 15</span>
                  <span className="text-xs bg-white/10 text-gray-200 px-3 py-1 rounded-full">FastAPI</span>
                  <span className="text-xs bg-white/10 text-gray-200 px-3 py-1 rounded-full">OpenAI</span>
                  <span className="text-xs bg-white/10 text-gray-200 px-3 py-1 rounded-full">LangChain</span>
                </div>
              </div>
            </div>

            {/* Bottom Bar */}
            <div className="border-t border-white/10 pt-8 text-center">
              <p className="text-gray-400 text-sm">
                © 2024 AI News Japan. All rights reserved.
              </p>
              <p className="text-xs text-gray-500 mt-2">
                Powered by OpenAI GPT & LangChain
              </p>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
