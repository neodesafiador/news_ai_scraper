/**
 * Search bar component with modern design
 */
'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function SearchBar() {
  const [keyword, setKeyword] = useState('');
  const [isFocused, setIsFocused] = useState(false);
  const router = useRouter();

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (keyword.trim()) {
      router.push(`/search?keyword=${encodeURIComponent(keyword)}`);
    }
  };

  return (
    <form onSubmit={handleSearch} className="w-full max-w-3xl mx-auto">
      <div className={`relative transition-all duration-300 ${isFocused ? 'scale-105' : 'scale-100'}`}>
        {/* Search Icon */}
        <div className="absolute left-6 top-1/2 transform -translate-y-1/2 text-gray-400">
          <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>

        {/* Input Field */}
        <input
          type="text"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          onFocus={() => setIsFocused(true)}
          onBlur={() => setIsFocused(false)}
          placeholder="記事を検索... (例: GPT, 機械学習, DeepMind)"
          className="w-full pl-16 pr-32 py-5 text-lg text-gray-900 bg-white border-2 border-white rounded-full focus:outline-none focus:ring-4 focus:ring-blue-300/50 shadow-2xl placeholder:text-gray-400 transition-all duration-200"
        />

        {/* Search Button */}
        <button
          type="submit"
          className="absolute right-2 top-1/2 transform -translate-y-1/2 bg-gradient-to-r from-blue-500 to-indigo-600 text-white px-8 py-3 rounded-full hover:from-blue-600 hover:to-indigo-700 transition-all duration-200 font-semibold shadow-lg hover:shadow-xl flex items-center gap-2 group"
        >
          <span>検索</span>
          <svg className="w-5 h-5 transform group-hover:translate-x-1 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
          </svg>
        </button>
      </div>

      {/* Quick Search Suggestions */}
      {isFocused && !keyword && (
        <div className="mt-4 flex flex-wrap justify-center gap-2 animate-in fade-in duration-200">
          <button
            type="button"
            onClick={() => setKeyword('GPT')}
            className="px-4 py-2 bg-white/90 text-gray-700 rounded-full text-sm hover:bg-white hover:shadow-md transition-all duration-200"
          >
            GPT
          </button>
          <button
            type="button"
            onClick={() => setKeyword('機械学習')}
            className="px-4 py-2 bg-white/90 text-gray-700 rounded-full text-sm hover:bg-white hover:shadow-md transition-all duration-200"
          >
            機械学習
          </button>
          <button
            type="button"
            onClick={() => setKeyword('DeepMind')}
            className="px-4 py-2 bg-white/90 text-gray-700 rounded-full text-sm hover:bg-white hover:shadow-md transition-all duration-200"
          >
            DeepMind
          </button>
          <button
            type="button"
            onClick={() => setKeyword('AI研究')}
            className="px-4 py-2 bg-white/90 text-gray-700 rounded-full text-sm hover:bg-white hover:shadow-md transition-all duration-200"
          >
            AI研究
          </button>
        </div>
      )}
    </form>
  );
}
