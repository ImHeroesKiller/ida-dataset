import { cn } from "@/lib/utils";

type Variant =
  | "primary"
  | "secondary"
  | "danger"
  | "ghost"
  | "outline"
  | "success"
  | "warning"
  | "default";

/**
 * Operator buttons — compact solid primary, outline secondary.
 */
const variants: Record<Variant, string> = {
  default:
    "bg-[var(--btn-primary-bg)] text-[var(--btn-primary-fg)] hover:brightness-110",
  primary:
    "bg-[var(--btn-primary-bg)] text-[var(--btn-primary-fg)] hover:brightness-110",
  secondary:
    "bg-[var(--btn-secondary-bg)] text-[var(--btn-secondary-fg)] border border-[var(--border)] hover:bg-[var(--panel-2)]",
  outline:
    "bg-transparent border border-[var(--border)] text-[var(--text)] hover:bg-[var(--panel-2)]",
  ghost:
    "bg-transparent text-[var(--text-secondary)] hover:bg-[var(--panel-2)] hover:text-[var(--text)]",
  danger:
    "bg-[var(--btn-danger-bg)] text-[var(--btn-danger-fg)] hover:brightness-110",
  success:
    "bg-[var(--btn-success-bg)] text-[var(--btn-success-fg)] hover:brightness-110",
  warning:
    "bg-[var(--btn-warning-bg)] text-[var(--btn-warning-fg)] hover:brightness-110",
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
      ? "h-7 px-2.5 text-[11px] gap-1"
      : size === "lg"
        ? "h-9 px-4 text-xs gap-1.5"
        : "h-8 px-3 text-xs gap-1.5";

  return (
    <button
      className={cn(
        "inline-flex items-center justify-center rounded-[var(--radius-md)] font-semibold transition-all duration-100",
        "focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-1 focus-visible:outline-[var(--blue)]",
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
        <span className="inline-block h-3 w-3 animate-spin rounded-full border-2 border-current border-r-transparent" />
      ) : null}
      {props.children}
    </button>
  );
}
