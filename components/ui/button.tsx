import { cn } from "@/lib/utils";

type Variant =
  | "default"
  | "primary"
  | "secondary"
  | "success"
  | "warning"
  | "danger"
  | "ghost"
  | "outline";

/**
 * Solid accent buttons with WCAG-safe contrast in light + dark mode.
 * Never transparent text on transparent backgrounds.
 */
const variants: Record<Variant, string> = {
  default:
    "bg-[var(--btn-primary-bg)] text-[var(--btn-primary-fg)] hover:opacity-90",
  primary:
    "bg-[var(--btn-primary-bg)] text-[var(--btn-primary-fg)] hover:opacity-90",
  secondary:
    "bg-[var(--btn-secondary-bg)] text-[var(--btn-secondary-fg)] border border-[var(--border)] hover:opacity-90",
  success:
    "bg-[var(--btn-success-bg)] text-[var(--btn-success-fg)] hover:opacity-90",
  warning:
    "bg-[var(--btn-warning-bg)] text-[var(--btn-warning-fg)] hover:opacity-90",
  danger:
    "bg-[var(--btn-danger-bg)] text-[var(--btn-danger-fg)] hover:opacity-90",
  ghost:
    "bg-transparent text-[var(--text)] hover:bg-[var(--panel-2)]",
  outline:
    "bg-transparent border border-[var(--border)] text-[var(--text)] hover:bg-[var(--panel-2)]",
};

export function Button({
  className,
  variant = "primary",
  size = "md",
  ...props
}: React.ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: Variant;
  size?: "sm" | "md";
}) {
  return (
    <button
      className={cn(
        "inline-flex items-center justify-center gap-1.5 rounded-xl font-medium transition-all duration-150 disabled:cursor-not-allowed disabled:opacity-45",
        size === "sm" ? "h-8 px-3 text-xs" : "h-10 px-4 text-sm",
        variants[variant],
        className
      )}
      {...props}
    />
  );
}
