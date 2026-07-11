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
        "h-1.5 overflow-hidden rounded-full bg-[var(--panel-2)]",
        className
      )}
      role="progressbar"
      aria-valuenow={Math.round(pct)}
      aria-valuemin={0}
      aria-valuemax={100}
    >
      <div
        className="h-full rounded-full bg-[var(--blue)] transition-all duration-500"
        style={{ width: `${pct}%` }}
      />
    </div>
  );
}
