"use client";

import { useEffect, useRef, useState } from "react";
import { BookOpen, Trash2, Radio } from "lucide-react";
import { cn } from "@/lib/utils";
import {
  useLearningSessions,
  type SessionEvent,
} from "@/lib/use-learning-sessions";

const verbClass: Record<string, string> = {
  "Mission Accepted": "text-indigo-300",
  Mission: "text-indigo-300",
  "Mission Completed": "text-emerald-300",
  Session: "text-indigo-300",
  Scheduler: "text-violet-300",
  Planner: "text-sky-400",
  "Gap Analysis": "text-cyan-300",
  Policy: "text-pink-300",
  Connector: "text-amber-300",
  "Document Queue": "text-orange-300",
  Pipeline: "text-yellow-300",
  Validator: "text-lime-300",
  Review: "text-fuchsia-300",
  Publishing: "text-emerald-400",
  "Knowledge Updated": "text-lime-300",
  "Learning Completed": "text-emerald-300",
  Searching: "text-sky-400",
  Downloading: "text-cyan-400",
  Reading: "text-violet-300",
  Understanding: "text-fuchsia-300",
  Extracting: "text-amber-300",
  Validating: "text-yellow-300",
};

/**
 * Learning Session Journal — real logs from stored GHA sessions.
 * No fake streaming of a local runtime.
 */
export function BottomConsole() {
  const { events, dashboard, activity, activeSessionId } = useLearningSessions();
  const [local, setLocal] = useState<SessionEvent[]>([]);
  const endRef = useRef<HTMLDivElement>(null);
  const [autoScroll, setAutoScroll] = useState(true);

  useEffect(() => {
    setLocal(events);
  }, [events]);

  useEffect(() => {
    if (autoScroll) endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [local, autoScroll]);

  const view = local.slice(-150);
  const status = dashboard.github_actions?.running
    ? "running"
    : dashboard.status || "idle";
  const connected = Boolean(dashboard.sessions || dashboard.github_actions);

  return (
    <div className="flex h-[var(--console-h)] shrink-0 flex-col border-t border-zinc-800/90 bg-[#070708]">
      <div className="flex h-8 items-center justify-between border-b border-zinc-900 px-3">
        <div className="flex items-center gap-2 text-[11px] text-zinc-400">
          <BookOpen className="h-3.5 w-3.5" />
          <span className="font-medium text-zinc-300">
            Learning Session Journal
          </span>
          <span className="text-zinc-600">·</span>
          <span
            className={cn(
              "inline-flex items-center gap-1",
              status === "running" ? "text-sky-400" : "text-zinc-500"
            )}
          >
            <Radio className="h-3 w-3" />
            {status === "running" ? "session running (GHA)" : status}
          </span>
          {activeSessionId ? (
            <span className="hidden font-mono text-[10px] text-zinc-600 sm:inline">
              · {activeSessionId}
            </span>
          ) : null}
          <span className="hidden text-zinc-600 md:inline">
            · real logs · mission events · knowledge events
          </span>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-[10px] text-zinc-600">
            {connected ? "monitor" : "offline"} ·{" "}
            {activity.current_task?.slice(0, 40) || "—"}
          </span>
          <label className="flex items-center gap-1 text-[10px] text-zinc-500">
            <input
              type="checkbox"
              checked={autoScroll}
              onChange={(e) => setAutoScroll(e.target.checked)}
              className="accent-zinc-400"
            />
            Auto-scroll
          </label>
          <button
            className="inline-flex items-center gap-1 text-[10px] text-zinc-500 hover:text-zinc-300"
            onClick={() => setLocal([])}
            title="Clear local view only"
          >
            <Trash2 className="h-3 w-3" />
            Clear view
          </button>
        </div>
      </div>
      <div className="flex-1 overflow-y-auto px-3 py-2 font-mono text-[11px] leading-5 scrollbar-thin">
        {view.length === 0 ? (
          <div className="text-zinc-600">
            No session logs loaded. Start Learning (GitHub Actions dispatch) or
            open a completed session from the dashboard. Journal shows real
            stored events — not a simulated stream.
          </div>
        ) : (
          view.map((line, idx) => {
            const verb = String(line.verb || "Learning");
            return (
              <div key={`${line.seq ?? idx}-${line.ts}`} className="flex gap-2">
                <span className="shrink-0 text-zinc-700">
                  {String(line.ts || "").slice(11, 19)}
                </span>
                <span
                  className={cn(
                    "shrink-0 font-medium",
                    verbClass[verb] || "text-zinc-300"
                  )}
                >
                  {verb}
                </span>
                <span className="text-zinc-400">{String(line.detail || "")}</span>
                {line.progress != null ? (
                  <span className="text-zinc-600">{line.progress}%</span>
                ) : null}
              </div>
            );
          })
        )}
        <div ref={endRef} />
      </div>
    </div>
  );
}
