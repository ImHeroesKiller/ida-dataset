import { cn } from "@/lib/utils";

export function Input({
  className,
  ...props
}: React.InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      className={cn(
        "h-9 w-full rounded-xl border border-[var(--border)] bg-[var(--panel)] px-3 text-sm text-[var(--text)] outline-none transition-colors placeholder:text-[var(--text-faint)] focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20",
        className
      )}
      {...props}
    />
  );
}
