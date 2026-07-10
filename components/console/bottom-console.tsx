"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { BookOpen } from "lucide-react";
import { cn } from "@/lib/utils";
import {
  useLearningSessions,
  type SessionEvent,
} from "@/lib/use-learning-sessions";

/** Map internal verbs/stages → executive learning verbs */
function humanVerb(ev: SessionEvent): string {
  const verb = String(ev.verb || "");
  const stage = String(ev.stage || "");
  const map: Record<string, string> = {
    Searching: "Searching",
    Connector: "Searching",
    Downloading: "Reading",
    "Document Queue": "Reading",
    Reading: "Reading",
    Understanding: "Understanding",
    Pipeline: stage === "pipeline" ? "Extracting" : "Understanding",
    Extracting: "Extracting",
    Validator: "Validating",
    Validating: "Validating",
    Review: "Validating",
    Publishing: "Publishing",
    "Knowledge Updated": "Publishing",
    "Learning Completed": "Learning Completed",
    "Mission Completed": "Learning Completed",
    "Mission Accepted": "Searching",
    Mission: "Searching",
    Session: "Searching",
    Scheduler: "Searching",
    Planner: "Searching",
    "Gap Analysis": "Searching",
    Policy: "Validating",
  };
  if (map[verb]) return map[verb];
  if (stage === "publish" || stage === "knowledge") return "Publishing";
  if (stage === "complete") return "Learning Completed";
  if (stage === "validate" || stage === "review") return "Validating";
  if (stage === "pipeline") return "Extracting";
  if (stage === "document_queue" || stage === "connector") return "Reading";
  return verb || "Learning";
}

const verbClass: Record<string, string> = {
  Searching: "text-sky-400",
  Reading: "text-violet-300",
  Understanding: "text-fuchsia-300",
  Extracting: "text-amber-300",
  Validating: "text-yellow-300",
  Publishing: "text-emerald-400",
  "Learning Completed": "text-emerald-300",
};

/**
 * IDA Learning Journal — human-readable learning verbs only.
 */
export function BottomConsole() {
  const { events, dashboard, activity } = useLearningSessions();
  const [local, setLocal] = useState<SessionEvent[]>([]);
  const endRef = useRef<HTMLDivElement>(null);
  const [autoScroll, setAutoScroll] = useState(true);

  useEffect(() => {
    setLocal(events);
  }, [events]);

  useEffect(() => {
    if (autoScroll) endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [local, autoScroll]);

  const view = useMemo(() => local.slice(-120), [local]);
  const status = dashboard.github_actions?.running
    ? "running"
    : dashboard.status || "idle";

  return (
    <div className="flex h-[var(--console-h)] shrink-0 flex-col border-t border-zinc-800/60 bg-[#08080a]">
      <div className="flex h-9 items-center justify-between border-b border-zinc-900/80 px-4">
        <div className="flex items-center gap-2 text-xs text-zinc-400">
          <BookOpen className="h-3.5 w-3.5 text-zinc-500" />
          <span className="font-medium text-zinc-200">IDA Learning Journal</span>
          <span className="text-zinc-700">·</span>
          <span
            className={cn(
              status === "running" ? "text-emerald-400" : "text-zinc-500"
            )}
          >
            {status === "running" ? "Learning" : "Standing by"}
          </span>
          <span className="hidden text-zinc-600 sm:inline">
            · Searching · Reading · Understanding · Extracting · Validating ·
            Publishing
          </span>
        </div>
        <label className="flex items-center gap-1.5 text-[11px] text-zinc-500">
          <input
            type="checkbox"
            checked={autoScroll}
            onChange={(e) => setAutoScroll(e.target.checked)}
            className="accent-zinc-400"
          />
          Auto-scroll
        </label>
      </div>
      <div className="flex-1 overflow-y-auto px-4 py-2 font-mono text-[11px] leading-6 scrollbar-thin">
        {view.length === 0 ? (
          <div className="text-zinc-600">
            {activity.current_thought ||
              "Waiting for the next learning moment…"}
          </div>
        ) : (
          view.map((line, idx) => {
            const verb = humanVerb(line);
            return (
              <div
                key={`${line.seq ?? idx}-${line.ts}`}
                className="flex gap-3"
              >
                <span className="w-14 shrink-0 text-zinc-700">
                  {String(line.ts || "").slice(11, 19)}
                </span>
                <span
                  className={cn(
                    "w-36 shrink-0 font-medium",
                    verbClass[verb] || "text-zinc-300"
                  )}
                >
                  {verb}
                </span>
                <span className="min-w-0 flex-1 truncate text-zinc-400">
                  {String(line.detail || line.current_task || "")}
                </span>
              </div>
            );
          })
        )}
        <div ref={endRef} />
      </div>
    </div>
  );
}
