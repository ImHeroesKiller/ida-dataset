import { cn } from "@/lib/utils";

/** Linear progress bar — design-system source of truth. */
export function Progress({
  value,
  className,
}: {
  value: number;
  className?: string;
}) {
  const pct = Math.min(100, Math.max(0, value));
  return (
    <div
      className={cn(
        "h-2 overflow-hidden rounded-full bg-[var(--panel-2)]",
        className
      )}
    >
      <div
        className="h-full rounded-full bg-blue-500 transition-all duration-500"
        style={{ width: `${pct}%` }}
      />
    </div>
  );
}
