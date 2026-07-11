import { cn } from "@/lib/utils";

export function Input({
  className,
  ...props
}: React.InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      className={cn(
        "h-8 w-full rounded-[var(--radius-md)] border border-[var(--border)] bg-[var(--panel)] px-2.5 text-xs text-[var(--text)] outline-none transition-colors",
        "placeholder:text-[var(--text-muted)]",
        "focus:border-[var(--blue)] focus:ring-1 focus:ring-[var(--blue)]/25",
        "disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      {...props}
    />
  );
}
