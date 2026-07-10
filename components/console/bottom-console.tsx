"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { BookOpen } from "lucide-react";
import { cn } from "@/lib/utils";
import {
  useLearningSessions,
  type SessionEvent,
} from "@/lib/use-learning-sessions";

function humanVerb(ev: SessionEvent | Record<string, unknown>): string {
  const verb = String(ev.verb || "");
  const stage = String(ev.stage || "");
  const map: Record<string, string> = {
    Searching: "Searching",
    Connector: "Searching",
    Downloading: "Reading",
    "Document Queue": "Reading",
    Reading: "Reading",
    Understanding: "Understanding",
    Pipeline: "Extracting",
    Extracting: "Extracting",
    Validator: "Validating",
    Validating: "Validating",
    Review: "Validating",
    Publishing: "Publishing",
    "Knowledge Updated": "Knowledge Added",
    "Knowledge Added": "Knowledge Added",
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
  return verb || "Learning";
}

const verbClass: Record<string, string> = {
  Searching: "text-blue-600 dark:text-sky-400",
  Reading: "text-violet-600 dark:text-violet-300",
  Understanding: "text-fuchsia-600 dark:text-fuchsia-300",
  Extracting: "text-amber-600 dark:text-amber-300",
  Validating: "text-yellow-600 dark:text-yellow-300",
  Publishing: "text-emerald-600 dark:text-emerald-400",
  "Knowledge Added": "text-emerald-700 dark:text-emerald-300",
  "Learning Completed": "text-emerald-700 dark:text-emerald-300",
};

export function BottomConsole() {
  const { events, dashboard, activity } = useLearningSessions();
  const [extra, setExtra] = useState<SessionEvent[]>([]);
  const [local, setLocal] = useState<SessionEvent[]>([]);
  const endRef = useRef<HTMLDivElement>(null);
  const [autoScroll, setAutoScroll] = useState(true);

  // Merge session events + live journal from publish queue
  useEffect(() => {
    const id = setInterval(async () => {
      try {
        const res = await fetch("/api/publish-queue", { cache: "no-store" });
        const data = await res.json();
        const tail = (data.journal_tail || []) as SessionEvent[];
        if (tail.length) setExtra(tail);
      } catch {
        /* ignore */
      }
    }, 2000);
    return () => clearInterval(id);
  }, []);

  useEffect(() => {
    const map = new Map<string, SessionEvent>();
    for (const e of [...extra, ...events]) {
      const key = `${e.ts}-${e.verb}-${e.detail}`;
      map.set(key, e);
    }
    setLocal(
      [...map.values()].sort((a, b) =>
        String(a.ts || "").localeCompare(String(b.ts || ""))
      )
    );
  }, [events, extra]);

  useEffect(() => {
    if (autoScroll) endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [local, autoScroll]);

  const view = useMemo(() => local.slice(-120), [local]);
  const status = dashboard.github_actions?.running
    ? "running"
    : dashboard.status || "idle";

  return (
    <div className="flex h-[var(--console-h)] shrink-0 flex-col border-t border-[var(--border)] bg-[var(--bg-elevated)]">
      <div className="flex h-9 items-center justify-between border-b border-[var(--border)] px-4">
        <div className="flex items-center gap-2 text-xs text-[var(--text-muted)]">
          <BookOpen className="h-3.5 w-3.5 text-[var(--text-faint)]" />
          <span className="font-medium text-[var(--text)]">
            IDA Learning Journal
          </span>
          <span className="text-[var(--text-faint)]">·</span>
          <span
            className={cn(
              status === "running"
                ? "text-emerald-600 dark:text-emerald-400"
                : "text-[var(--text-faint)]"
            )}
          >
            {status === "running" ? "Learning" : "Standing by"}
          </span>
        </div>
        <label className="flex items-center gap-1.5 text-[11px] text-[var(--text-faint)]">
          <input
            type="checkbox"
            checked={autoScroll}
            onChange={(e) => setAutoScroll(e.target.checked)}
            className="accent-blue-500"
          />
          Auto-scroll
        </label>
      </div>
      <div className="flex-1 overflow-y-auto px-4 py-2 font-mono text-[11px] leading-6 scrollbar-thin">
        {view.length === 0 ? (
          <div className="text-[var(--text-faint)]">
            {activity.current_thought ||
              "Waiting for the next learning moment… Start a mission to fill the journal."}
          </div>
        ) : (
          view.map((line, idx) => {
            const verb = humanVerb(line);
            return (
              <div
                key={`${line.seq ?? idx}-${line.ts}`}
                className="flex gap-3"
              >
                <span className="w-14 shrink-0 text-[var(--text-faint)]">
                  {String(line.ts || "").slice(11, 19)}
                </span>
                <span
                  className={cn(
                    "w-36 shrink-0 font-medium",
                    verbClass[verb] || "text-[var(--text)]"
                  )}
                >
                  {verb}
                </span>
                <span className="min-w-0 flex-1 truncate text-[var(--text-muted)]">
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
