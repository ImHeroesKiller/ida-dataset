import { cn } from "@/lib/utils";
import type { ModuleStatus } from "@/lib/status";
import { STATUS_META } from "@/lib/status";

export function Badge({
  children,
  className,
}: {
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <span
      className={cn(
        "inline-flex items-center rounded-md border border-[var(--border)] bg-[var(--panel-2)] px-1.5 py-0.5 text-[11px] text-[var(--text-muted)]",
        className
      )}
    >
      {children}
    </span>
  );
}

export function StatusBadge({ status }: { status: ModuleStatus }) {
  const meta = STATUS_META[status];
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[11px] font-medium ring-1 ring-inset",
        meta.bg,
        meta.color,
        meta.ring
      )}
    >
      <span
        className={cn(
          "h-1.5 w-1.5 rounded-full",
          status === "healthy" && "bg-emerald-400",
          status === "waiting" && "bg-amber-300",
          status === "running" && "bg-sky-400 animate-pulse",
          status === "error" && "bg-red-400",
          status === "disabled" && "bg-zinc-500"
        )}
      />
      {meta.label}
    </span>
  );
}
