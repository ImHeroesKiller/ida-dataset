import { cn } from "@/lib/utils";

type Variant = "primary" | "secondary" | "danger" | "ghost" | "outline" | "success" | "warning" | "default";

/**
 * Enterprise buttons — solid primary, outline secondary, danger, ghost.
 * WCAG-safe contrast via design tokens.
 */
const variants: Record<Variant, string> = {
  default:
    "bg-[var(--btn-primary-bg)] text-[var(--btn-primary-fg)] hover:brightness-110 shadow-sm",
  primary:
    "bg-[var(--btn-primary-bg)] text-[var(--btn-primary-fg)] hover:brightness-110 shadow-sm",
  secondary:
    "bg-[var(--btn-secondary-bg)] text-[var(--btn-secondary-fg)] border border-[var(--border)] hover:bg-[var(--panel-2)]",
  outline:
    "bg-transparent border border-[var(--border)] text-[var(--text)] hover:bg-[var(--panel-2)]",
  ghost:
    "bg-transparent text-[var(--text-secondary)] hover:bg-[var(--panel-2)] hover:text-[var(--text)]",
  danger:
    "bg-[var(--btn-danger-bg)] text-[var(--btn-danger-fg)] hover:brightness-110 shadow-sm",
  success:
    "bg-[var(--btn-success-bg)] text-[var(--btn-success-fg)] hover:brightness-110 shadow-sm",
  warning:
    "bg-[var(--btn-warning-bg)] text-[var(--btn-warning-fg)] hover:brightness-110 shadow-sm",
};

export function Button({
  className,
  variant = "primary",
  size = "md",
  loading,
  ...props
}: React.ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: Variant;
  size?: "sm" | "md" | "lg";
  loading?: boolean;
}) {
  const sizeCls =
    size === "sm"
      ? "h-8 px-3 text-sm gap-1.5"
      : size === "lg"
        ? "h-12 px-6 text-base gap-2"
        : "h-10 px-4 text-sm gap-2";

  return (
    <button
      className={cn(
        "inline-flex items-center justify-center rounded-[var(--radius-lg)] font-semibold transition-all duration-150",
        "focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--blue)]",
        "disabled:cursor-not-allowed disabled:opacity-50",
        sizeCls,
        variants[variant],
        className
      )}
      disabled={props.disabled || loading}
      aria-busy={loading || undefined}
      {...props}
    >
      {loading ? (
        <span className="inline-block h-4 w-4 animate-spin rounded-full border-2 border-current border-r-transparent" />
      ) : null}
      {props.children}
    </button>
  );
}
