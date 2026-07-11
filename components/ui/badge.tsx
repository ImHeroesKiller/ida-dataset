import { cn } from "@/lib/utils";
import type { ModuleStatus } from "@/lib/status";
import { STATUS_META } from "@/lib/status";
import type { BadgeRole } from "@/lib/design-tokens";

const ROLE_STYLES: Record<BadgeRole, string> = {
  healthy:
    "bg-[var(--badge-healthy-bg)] text-[var(--badge-healthy-fg)] border-transparent",
  warning:
    "bg-[var(--badge-warning-bg)] text-[var(--badge-warning-fg)] border-transparent",
  error:
    "bg-[var(--badge-error-bg)] text-[var(--badge-error-fg)] border-transparent",
  idle: "bg-[var(--badge-idle-bg)] text-[var(--badge-idle-fg)] border-transparent",
  running:
    "bg-[var(--badge-running-bg)] text-[var(--badge-running-fg)] border-transparent",
  publishing:
    "bg-[var(--badge-publishing-bg)] text-[var(--badge-publishing-fg)] border-transparent",
  completed:
    "bg-[var(--badge-completed-bg)] text-[var(--badge-completed-fg)] border-transparent",
};

export function Badge({
  children,
  className,
  role,
}: {
  children: React.ReactNode;
  className?: string;
  role?: BadgeRole;
}) {
  return (
    <span
      className={cn(
        "inline-flex items-center rounded-md border border-[var(--border)] bg-[var(--panel-2)] px-2 py-0.5 text-caption font-medium text-[var(--text-secondary)]",
        role && ROLE_STYLES[role],
        className
      )}
    >
      {children}
    </span>
  );
}

/** Semantic status badge (Healthy / Warning / Error / …) */
export function RoleBadge({
  role,
  children,
  className,
}: {
  role: BadgeRole;
  children?: React.ReactNode;
  className?: string;
}) {
  const labels: Record<BadgeRole, string> = {
    healthy: "Healthy",
    warning: "Warning",
    error: "Error",
    idle: "Idle",
    running: "Running",
    publishing: "Publishing",
    completed: "Completed",
  };
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-caption font-semibold",
        ROLE_STYLES[role],
        className
      )}
    >
      <span
        className={cn(
          "h-1.5 w-1.5 rounded-full",
          role === "running" && "animate-pulse bg-[var(--blue)]",
          role === "healthy" || role === "completed"
            ? "bg-[var(--green)]"
            : role === "warning"
              ? "bg-[var(--orange)]"
              : role === "error"
                ? "bg-[var(--red)]"
                : role === "publishing"
                  ? "bg-[var(--purple)]"
                  : "bg-[var(--text-muted)]"
        )}
      />
      {children ?? labels[role]}
    </span>
  );
}

export function StatusBadge({ status }: { status: ModuleStatus }) {
  const meta = STATUS_META[status];
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-caption font-semibold ring-1 ring-inset",
        meta.bg,
        meta.color,
        meta.ring
      )}
    >
      <span
        className={cn(
          "h-1.5 w-1.5 rounded-full",
          status === "healthy" && "bg-[var(--green)]",
          status === "waiting" && "bg-[var(--orange)]",
          status === "running" && "animate-pulse bg-[var(--blue)]",
          status === "error" && "bg-[var(--red)]",
          status === "disabled" && "bg-[var(--text-muted)]"
        )}
      />
      {meta.label}
    </span>
  );
}
