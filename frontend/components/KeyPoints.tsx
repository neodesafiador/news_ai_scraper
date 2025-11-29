/**
 * Key points list component for article details
 */

interface KeyPointsProps {
  points: string[];
}

export default function KeyPoints({ points }: KeyPointsProps) {
  if (!points || points.length === 0) {
    return null;
  }

  return (
    <section className="mb-8 p-8 bg-gradient-to-br from-emerald-50 to-teal-50 rounded-2xl border-2 border-emerald-100 shadow-lg">
      {/* Header */}
      <div className="flex items-center gap-3 mb-6">
        <div className="w-10 h-10 bg-gradient-to-br from-emerald-500 to-teal-600 rounded-xl flex items-center justify-center">
          <svg className="w-6 h-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
        <h2 className="text-2xl font-bold text-gray-900">
          重要ポイント
        </h2>
      </div>

      {/* Points list */}
      <ul className="space-y-4">
        {points.map((point, index) => (
          <li
            key={index}
            className="flex items-start gap-4 group"
          >
            {/* Number badge with gradient */}
            <span className="flex-shrink-0 w-8 h-8 bg-gradient-to-br from-emerald-500 to-teal-600 text-white rounded-lg flex items-center justify-center text-sm font-bold shadow-md group-hover:scale-110 transition-transform duration-200">
              {index + 1}
            </span>

            {/* Point text */}
            <span className="text-gray-800 leading-relaxed pt-1 flex-1">
              {point}
            </span>

            {/* Check icon on hover */}
            <svg
              className="flex-shrink-0 w-5 h-5 text-emerald-500 opacity-0 group-hover:opacity-100 transition-opacity duration-200 mt-1"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                fillRule="evenodd"
                d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                clipRule="evenodd"
              />
            </svg>
          </li>
        ))}
      </ul>
    </section>
  );
}
