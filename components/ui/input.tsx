import { cn } from "@/lib/utils";

export function Input({
  className,
  ...props
}: React.InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      className={cn(
        "h-11 w-full rounded-[var(--radius-lg)] border border-[var(--border)] bg-[var(--panel)] px-4 text-small text-[var(--text)] outline-none transition-colors",
        "placeholder:text-[var(--text-muted)]",
        "focus:border-[var(--blue)] focus:ring-2 focus:ring-[var(--blue)]/20",
        "disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      {...props}
    />
  );
}
