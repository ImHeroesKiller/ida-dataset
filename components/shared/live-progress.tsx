"use client";

import { cn } from "@/lib/utils";
import type { LiveActivity } from "@/lib/use-live-learning";

const TIMELINE = [
  "Mission",
  "Searching",
  "Downloading",
  "Reading",
  "Understanding",
  "Extracting",
  "Validating",
  "Review",
  "Publishing",
  "Learning Completed",
] as const;

function stageIndex(activity: LiveActivity, events: { verb?: string; stage?: string }[]) {
  const last = events[events.length - 1];
  const verb = String(last?.verb || "");
  const map: Record<string, number> = {
    "Mission Accepted": 0,
    Mission: 0,
    Scheduler: 0,
    Planner: 1,
    "Gap Analysis": 1,
    Policy: 1,
    Connector: 1,
    Searching: 1,
    "Document Queue": 2,
    Downloading: 2,
    Pipeline: 3,
    Reading: 3,
    Understanding: 4,
    Extracting: 5,
    Validator: 6,
    Validating: 6,
    Review: 7,
    Publishing: 8,
    "Knowledge Updated": 8,
    "Mission Completed": 9,
    "Learning Completed": 9,
  };
  if (verb in map) return map[verb];
  const stage = String(last?.stage || "");
  const stageMap: Record<string, number> = {
    mission: 0,
    scheduler: 0,
    planner: 1,
    policy: 1,
    connector: 1,
    document_queue: 2,
    pipeline: 5,
    validate: 6,
    review: 7,
    publish: 8,
    complete: 9,
  };
  return stageMap[stage] ?? (activity.status === "idle" ? -1 : 0);
}

export function LiveProgress({
  activity,
  events = [],
}: {
  activity: LiveActivity;
  events?: { verb?: string; stage?: string }[];
}) {
  const idx = stageIndex(activity, events);
  const pct = Math.min(100, Math.max(0, Number(activity.progress ?? 0)));
  const running = activity.status === "running" || activity.status === "progress";

  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-end justify-between gap-2">
        <div>
          <div className="text-[10px] uppercase tracking-wide text-zinc-500">
            What is IDA doing right now?
          </div>
          <div className="text-sm font-medium text-zinc-100">
            {activity.current_thought || activity.current_task || "Standing by"}
          </div>
        </div>
        <div
          className={cn(
            "text-xs font-medium",
            running ? "text-sky-400" : "text-zinc-500"
          )}
        >
          {running ? "LIVE" : activity.status || "idle"} · {pct}%
        </div>
      </div>

      <div className="h-2 overflow-hidden rounded-full bg-zinc-900">
        <div
          className={cn(
            "h-full rounded-full transition-all duration-500",
            running ? "bg-sky-500" : "bg-emerald-600"
          )}
          style={{ width: `${pct}%` }}
        />
      </div>

      <div className="grid grid-cols-2 gap-2 text-[11px] text-zinc-400 sm:grid-cols-4">
        <div>
          <div className="text-zinc-600">Task</div>
          <div className="truncate text-zinc-200">
            {activity.current_task || "—"}
          </div>
        </div>
        <div>
          <div className="text-zinc-600">Entity</div>
          <div className="truncate text-zinc-200">
            {activity.current_entity || "—"}
          </div>
        </div>
        <div>
          <div className="text-zinc-600">Document</div>
          <div className="truncate text-zinc-200">
            {activity.current_document || "—"}
          </div>
        </div>
        <div>
          <div className="text-zinc-600">Dataset</div>
          <div className="truncate text-zinc-200">
            {activity.current_dataset || "—"}
          </div>
        </div>
        <div>
          <div className="text-zinc-600">Source</div>
          <div className="truncate text-zinc-200">
            {activity.current_source || "—"}
          </div>
        </div>
        <div>
          <div className="text-zinc-600">Relationship</div>
          <div className="truncate text-zinc-200">
            {activity.current_relationship || "—"}
          </div>
        </div>
        <div>
          <div className="text-zinc-600">Confidence</div>
          <div className="truncate text-zinc-200">
            {activity.current_confidence != null
              ? `${Math.round(Number(activity.current_confidence) * 100)}%`
              : "—"}
          </div>
        </div>
        <div>
          <div className="text-zinc-600">Stage</div>
          <div className="truncate text-zinc-200">
            {TIMELINE[Math.max(0, idx)] || "—"}
          </div>
        </div>
      </div>

      <div className="flex flex-wrap gap-1.5">
        {TIMELINE.map((label, i) => {
          const done = idx > i || (idx === i && pct >= 100);
          const active = idx === i && running;
          return (
            <span
              key={label}
              className={cn(
                "rounded-full px-2 py-0.5 text-[10px] ring-1 ring-inset transition-colors",
                done && "bg-emerald-500/15 text-emerald-300 ring-emerald-500/30",
                active && "bg-sky-500/20 text-sky-300 ring-sky-500/40 animate-pulse",
                !done && !active && "bg-zinc-900 text-zinc-600 ring-zinc-800"
              )}
            >
              {label}
            </span>
          );
        })}
      </div>
    </div>
  );
}
