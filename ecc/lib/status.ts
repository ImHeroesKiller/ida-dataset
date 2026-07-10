export type ModuleStatus = "healthy" | "waiting" | "running" | "error" | "disabled";

export const STATUS_META: Record<
  ModuleStatus,
  { label: string; color: string; bg: string; ring: string }
> = {
  healthy: {
    label: "Healthy",
    color: "text-emerald-400",
    bg: "bg-emerald-500/15",
    ring: "ring-emerald-500/40",
  },
  waiting: {
    label: "Waiting",
    color: "text-amber-300",
    bg: "bg-amber-500/15",
    ring: "ring-amber-500/40",
  },
  running: {
    label: "Running",
    color: "text-sky-400",
    bg: "bg-sky-500/15",
    ring: "ring-sky-500/40",
  },
  error: {
    label: "Error",
    color: "text-red-400",
    bg: "bg-red-500/15",
    ring: "ring-red-500/40",
  },
  disabled: {
    label: "Disabled",
    color: "text-zinc-400",
    bg: "bg-zinc-500/15",
    ring: "ring-zinc-500/30",
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
