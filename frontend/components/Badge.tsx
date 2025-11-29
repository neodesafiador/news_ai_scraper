/**
 * Badge component for tags, categories, and labels
 */
import Link from 'next/link';

export type BadgeVariant = 'primary' | 'secondary' | 'success' | 'info' | 'outline';
export type BadgeSize = 'sm' | 'md' | 'lg';

interface BadgeProps {
  children: React.ReactNode;
  variant?: BadgeVariant;
  size?: BadgeSize;
  href?: string;
  className?: string;
}

const variantStyles: Record<BadgeVariant, string> = {
  primary: 'bg-gradient-to-r from-blue-500 to-blue-600 text-white hover:from-blue-600 hover:to-blue-700',
  secondary: 'bg-gray-100 text-gray-700 hover:bg-gray-200',
  success: 'bg-gradient-to-r from-green-500 to-emerald-600 text-white hover:from-green-600 hover:to-emerald-700',
  info: 'bg-gradient-to-r from-purple-500 to-indigo-600 text-white hover:from-purple-600 hover:to-indigo-700',
  outline: 'border-2 border-gray-300 text-gray-700 hover:border-gray-400 hover:bg-gray-50',
};

const sizeStyles: Record<BadgeSize, string> = {
  sm: 'px-2 py-0.5 text-xs',
  md: 'px-3 py-1 text-sm',
  lg: 'px-4 py-2 text-base',
};

export default function Badge({
  children,
  variant = 'secondary',
  size = 'md',
  href,
  className = ''
}: BadgeProps) {
  const baseStyles = 'inline-flex items-center font-medium rounded-full transition-all duration-200 whitespace-nowrap';
  const styles = `${baseStyles} ${variantStyles[variant]} ${sizeStyles[size]} ${className}`;

  if (href) {
    return (
      <Link href={href} className={styles}>
        {children}
      </Link>
    );
  }

  return (
    <span className={styles}>
      {children}
    </span>
  );
}
