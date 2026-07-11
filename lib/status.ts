export type ModuleStatus = "healthy" | "waiting" | "running" | "error" | "disabled";

/** WCAG-friendly status styles using design tokens (no low-contrast zinc). */
export const STATUS_META: Record<
  ModuleStatus,
  { label: string; color: string; bg: string; ring: string }
> = {
  healthy: {
    label: "Healthy",
    color: "text-[var(--badge-healthy-fg)]",
    bg: "bg-[var(--badge-healthy-bg)]",
    ring: "ring-[var(--green)]/30",
  },
  waiting: {
    label: "Waiting",
    color: "text-[var(--badge-warning-fg)]",
    bg: "bg-[var(--badge-warning-bg)]",
    ring: "ring-[var(--orange)]/30",
  },
  running: {
    label: "Running",
    color: "text-[var(--badge-running-fg)]",
    bg: "bg-[var(--badge-running-bg)]",
    ring: "ring-[var(--blue)]/30",
  },
  error: {
    label: "Error",
    color: "text-[var(--badge-error-fg)]",
    bg: "bg-[var(--badge-error-bg)]",
    ring: "ring-[var(--red)]/30",
  },
  disabled: {
    label: "Disabled",
    color: "text-[var(--badge-idle-fg)]",
    bg: "bg-[var(--badge-idle-bg)]",
    ring: "ring-[var(--border)]",
  },
};

export function statusFromCounts(opts: {
  error?: boolean;
  running?: boolean;
  disabled?: boolean;
  hasData?: boolean;
}): ModuleStatus {
  if (opts.error) return "error";
  if (opts.running) return "running";
  if (opts.disabled) return "disabled";
  if (opts.hasData) return "healthy";
  return "waiting";
}
