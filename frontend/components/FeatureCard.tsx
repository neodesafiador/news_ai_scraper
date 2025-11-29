/**
 * Feature card component for showcasing app features
 */

interface FeatureCardProps {
  icon: string;
  title: string;
  description: string;
  gradient?: string;
}

export default function FeatureCard({
  icon,
  title,
  description,
  gradient = 'from-blue-500 to-indigo-600'
}: FeatureCardProps) {
  return (
    <div className="group relative bg-white rounded-2xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2">
      {/* Gradient border effect on hover */}
      <div className={`absolute inset-0 bg-gradient-to-br ${gradient} rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-300 -z-10 blur-xl`}></div>

      <div className="relative">
        {/* Icon with gradient background */}
        <div className={`w-16 h-16 bg-gradient-to-br ${gradient} rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300`}>
          <span className="text-4xl">{icon}</span>
        </div>

        {/* Title */}
        <h3 className="text-2xl font-bold text-gray-900 mb-4 group-hover:text-transparent group-hover:bg-clip-text group-hover:bg-gradient-to-r group-hover:from-blue-600 group-hover:to-indigo-600 transition-all duration-300">
          {title}
        </h3>

        {/* Description */}
        <p className="text-gray-600 leading-relaxed">
          {description}
        </p>

        {/* Decorative element */}
        <div className={`mt-6 h-1 w-0 bg-gradient-to-r ${gradient} rounded-full group-hover:w-full transition-all duration-500`}></div>
      </div>
    </div>
  );
}
