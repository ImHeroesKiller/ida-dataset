"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { ChevronDown, ChevronUp, BookOpen } from "lucide-react";
import { cn } from "@/lib/utils";
import {
  useLearning,
  type SessionEvent,
} from "@/hooks/learning-provider";
import { formatWibTime } from "@/lib/time-wib";

type Filter =
  | "all"
  | "search"
  | "extraction"
  | "validation"
  | "publishing"
  | "github"
  | "huggingface"
  | "export"
  | "errors"
  | "warnings";

const FILTER_MATCH: Record<Filter, (ev: SessionEvent) => boolean> = {
  all: () => true,
  search: (e) =>
    /search|connector|planner|scheduler|mission|session|gap|discovery|tavily|acquisition/i.test(
      `${e.verb} ${e.stage} ${e.detail}`
    ),
  extraction: (e) =>
    /extract|pipeline|understand|entity|reading|document/i.test(
      `${e.verb} ${e.stage} ${e.detail}`
    ),
  validation: (e) =>
    /validat|review|policy|confidence/i.test(`${e.verb} ${e.stage} ${e.detail}`),
  publishing: (e) =>
    /publish|append|knowledge/i.test(`${e.verb} ${e.stage} ${e.detail}`),
  github: (e) =>
    /github|actions|gha|commit|push|worktree|certif/i.test(
      `${e.verb} ${e.stage} ${e.detail}`
    ),
  huggingface: (e) =>
    /hugging|hf_|hf |dataset card|hub/i.test(
      `${e.verb} ${e.stage} ${e.detail}`
    ),
  export: (e) =>
    /export|packag|jsonl|parquet|openai|csv/i.test(
      `${e.verb} ${e.stage} ${e.detail}`
    ),
  errors: (e) =>
    /error|fail|reject/i.test(`${e.verb} ${e.stage} ${e.detail} ${e.status}`),
  warnings: (e) =>
    /warn|skip|waiting/i.test(`${e.verb} ${e.stage} ${e.detail} ${e.status}`),
};

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
    batch_publish: "Publishing",
  };
  if (map[verb]) return map[verb];
  if (stage === "publish" || stage === "knowledge") return "Publishing";
  if (stage === "complete") return "Learning Completed";
  return verb || "Event";
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

const LS_KEY = "ida-factory-journal-expanded";

export function BottomConsole() {
  const { events, dashboard, activity } = useLearning();
  const [extra, setExtra] = useState<SessionEvent[]>([]);
  const [local, setLocal] = useState<SessionEvent[]>([]);
  const [filter, setFilter] = useState<Filter>("all");
  const [expanded, setExpanded] = useState(false);
  const [autoScroll, setAutoScroll] = useState(true);
  const endRef = useRef<HTMLDivElement>(null);
  const scrollerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    try {
      const v = localStorage.getItem(LS_KEY);
      if (v === "1") setExpanded(true);
      if (v === "0") setExpanded(false);
    } catch {
      /* ignore */
    }
  }, []);

  useEffect(() => {
    try {
      localStorage.setItem(LS_KEY, expanded ? "1" : "0");
    } catch {
      /* ignore */
    }
  }, [expanded]);

  // Reuse existing poll path via publish-queue journal tail (not faster than 5s shared architecture)
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
    }, 5000);
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
    if (expanded && autoScroll) {
      endRef.current?.scrollIntoView({ behavior: "smooth" });
    }
  }, [local, autoScroll, expanded]);

  function onScroll() {
    const el = scrollerRef.current;
    if (!el) return;
    const atBottom = el.scrollHeight - el.scrollTop - el.clientHeight < 48;
    setAutoScroll(atBottom);
  }

  const filtered = useMemo(
    () => local.filter(FILTER_MATCH[filter]).slice(-200),
    [local, filter]
  );

  const latest = filtered[filtered.length - 1];
  const status = dashboard.github_actions?.running
    ? "running"
    : dashboard.status || activity.status || "idle";

  // Group by mission/session for display headers
  const grouped = useMemo(() => {
    const out: Array<{ key: string; label: string; items: SessionEvent[] }> = [];
    let curKey = "";
    for (const ev of filtered) {
      const key = `${ev.session_id || "—"}|${ev.mission_id || "—"}`;
      if (key !== curKey) {
        curKey = key;
        out.push({
          key,
          label: `${ev.session_id || "session"} · ${ev.mission_id || "mission"}`,
          items: [ev],
        });
      } else {
        out[out.length - 1].items.push(ev);
      }
    }
    return out;
  }, [filtered]);

  return (
    <div
      className={cn(
        "border-t border-[var(--border)] bg-[var(--panel)] transition-[height] duration-300 ease-out",
        expanded ? "h-[min(42vh,420px)]" : "h-12"
      )}
    >
      {/* Collapsed bar ~48px */}
      <div className="flex h-12 items-center gap-3 px-4">
        <BookOpen className="h-4 w-4 shrink-0 text-[var(--text-faint)]" />
        <span
          className={cn(
            "h-2 w-2 shrink-0 rounded-full",
            status === "running" ? "animate-pulse bg-[var(--green)]" : "bg-[var(--text-disabled)]"
          )}
        />
        <p className="min-w-0 flex-1 truncate text-xs text-[var(--text-muted)]">
          {latest ? (
            <>
              <span className={cn("font-medium", verbClass[humanVerb(latest)])}>
                {humanVerb(latest)}
              </span>
              <span className="text-[var(--text-faint)]"> · </span>
              <span>{latest.detail || "—"}</span>
              <span className="text-[var(--text-faint)]">
                {" "}
                · {formatWibTime(latest.ts)}
              </span>
            </>
          ) : (
            <span className="text-[var(--text-faint)]">
              Journal idle · waiting for production events
            </span>
          )}
        </p>
        <button
          type="button"
          onClick={() => setExpanded((v) => !v)}
          className="inline-flex items-center gap-1 rounded-lg bg-[var(--panel-2)] px-2.5 py-1 text-[11px] font-medium text-[var(--text-muted)] hover:text-[var(--text)]"
        >
          {expanded ? (
            <>
              Collapse <ChevronDown className="h-3.5 w-3.5" />
            </>
          ) : (
            <>
              Expand <ChevronUp className="h-3.5 w-3.5" />
            </>
          )}
        </button>
      </div>

      {expanded ? (
        <div className="flex h-[calc(100%-3rem)] flex-col border-t border-[var(--border)]">
          <div className="flex flex-wrap items-center gap-1.5 px-4 py-2">
            {(
              [
                "all",
                "search",
                "extraction",
                "validation",
                "publishing",
                "github",
                "huggingface",
                "export",
                "errors",
                "warnings",
              ] as Filter[]
            ).map((f) => (
              <button
                key={f}
                type="button"
                onClick={() => setFilter(f)}
                className={cn(
                  "rounded-full px-2.5 py-0.5 text-[10px] font-medium uppercase tracking-wide",
                  filter === f
                    ? "bg-emerald-500/15 text-emerald-700 dark:text-emerald-300"
                    : "bg-[var(--panel-2)] text-[var(--text-faint)] hover:text-[var(--text-muted)]"
                )}
              >
                {f}
              </button>
            ))}
            <span className="ml-auto text-[10px] text-[var(--text-faint)]">
              {autoScroll ? "auto-scroll on" : "auto-scroll paused"}
            </span>
          </div>
          <div
            ref={scrollerRef}
            onScroll={onScroll}
            className="min-h-0 flex-1 overflow-y-auto px-4 pb-3 font-mono text-[11px] scrollbar-thin"
          >
            {!grouped.length ? (
              <p className="text-xs text-[var(--text-faint)]">No journal events.</p>
            ) : (
              grouped.map((g) => (
                <div key={g.key} className="mb-3">
                  <p className="mb-1 text-[10px] font-semibold uppercase tracking-wider text-[var(--text-faint)]">
                    {g.label}
                  </p>
                  {g.items.map((ev, i) => (
                    <div
                      key={`${g.key}-${i}`}
                      className="flex gap-2 border-b border-[var(--border)]/40 py-1 text-[var(--text-muted)]"
                    >
                      <span className="w-24 shrink-0 text-[var(--text-faint)]">
                        {formatWibTime(ev.ts)}
                      </span>
                      <span
                        className={cn(
                          "w-28 shrink-0 font-medium",
                          verbClass[humanVerb(ev)] || "text-[var(--text)]"
                        )}
                      >
                        {humanVerb(ev)}
                      </span>
                      <span className="w-20 shrink-0 truncate text-[var(--text-faint)]">
                        {ev.stage || "—"}
                      </span>
                      <span className="min-w-0 flex-1 truncate">{ev.detail}</span>
                    </div>
                  ))}
                </div>
              ))
            )}
            <div ref={endRef} />
          </div>
        </div>
      ) : null}
    </div>
  );
}
