"use client";

import { useMemo, useState } from "react";
import { Card, CardBody } from "@/components/ui/card";
import { cn } from "@/lib/utils";

type SessionSummary = {
  session_id: string;
  start_time?: string | null;
  end_time?: string | null;
  duration_seconds?: number | null;
  status?: string;
  mission?: string;
  knowledge_added?: number;
  knowledge_updated?: number;
  knowledge_rejected?: number;
  summary?: string;
};

type History = {
  today: Period;
  this_week: Period;
  this_month: Period;
  total: Period;
  knowledge_growth: { added: number; updated: number; rejected: number };
};

type Period = {
  sessions: number;
  success: number;
  failed: number;
  success_rate: number;
  knowledge_added: number;
  knowledge_updated: number;
  knowledge_rejected: number;
  avg_duration_seconds: number;
  avg_knowledge_added: number;
};

export function ReportsClient({
  initialHistory,
  initialSessions,
}: {
  initialHistory: History | null;
  initialSessions: SessionSummary[];
}) {
  const [tab, setTab] = useState<"today" | "week" | "month">("today");

  const history = initialHistory;
  const sessions = initialSessions;

  const period = useMemo(() => {
    if (!history) return null;
    if (tab === "today") return history.today;
    if (tab === "week") return history.this_week;
    return history.this_month;
  }, [history, tab]);

  const filtered = useMemo(() => {
    const now = Date.now();
    const day = 86400000;
    return sessions.filter((s) => {
      if (!s.start_time) return false;
      const t = Date.parse(s.start_time);
      if (Number.isNaN(t)) return false;
      if (tab === "today") {
        const start = new Date();
        start.setUTCHours(0, 0, 0, 0);
        return t >= start.getTime();
      }
      if (tab === "week") return now - t < 7 * day;
      return now - t < 30 * day;
    });
  }, [sessions, tab]);

  return (
    <div className="mx-auto max-w-6xl space-y-8">
      <header>
        <h1 className="text-3xl font-semibold tracking-tight text-zinc-50">
          Reports
        </h1>
        <p className="mt-2 text-base text-zinc-400">
          Knowledge growth and learning quality — kept simple.
        </p>
      </header>

      <div className="flex gap-2">
        {(
          [
            ["today", "Today"],
            ["week", "This Week"],
            ["month", "This Month"],
          ] as const
        ).map(([id, label]) => (
          <button
            key={id}
            type="button"
            onClick={() => setTab(id)}
            className={cn(
              "rounded-full px-4 py-2 text-sm font-medium transition-colors",
              tab === id
                ? "bg-zinc-100 text-zinc-900"
                : "bg-zinc-900 text-zinc-400 hover:text-zinc-200"
            )}
          >
            {label}
          </button>
        ))}
      </div>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <Metric
          label="Sessions"
          value={String(period?.sessions ?? 0)}
          tone="neutral"
        />
        <Metric
          label="Success rate"
          value={`${period?.success_rate ?? 0}%`}
          tone="green"
        />
        <Metric
          label="Knowledge added"
          value={`+${period?.knowledge_added ?? 0}`}
          tone="blue"
        />
        <Metric
          label="Avg knowledge / session"
          value={String(period?.avg_knowledge_added ?? 0)}
          tone="neutral"
        />
      </div>

      <Card className="border-zinc-800/50 bg-zinc-950/40">
        <CardBody className="p-6">
          <h2 className="text-sm font-medium uppercase tracking-wider text-zinc-500">
            Quality snapshot
          </h2>
          <div className="mt-4 grid gap-4 sm:grid-cols-3">
            <div>
              <p className="text-2xl font-semibold text-emerald-300">
                +{history?.knowledge_growth?.added ?? 0}
              </p>
              <p className="text-xs text-zinc-500">Total knowledge added</p>
            </div>
            <div>
              <p className="text-2xl font-semibold text-sky-300">
                ~{history?.knowledge_growth?.updated ?? 0}
              </p>
              <p className="text-xs text-zinc-500">Total updated</p>
            </div>
            <div>
              <p className="text-2xl font-semibold text-zinc-300">
                ×{history?.knowledge_growth?.rejected ?? 0}
              </p>
              <p className="text-xs text-zinc-500">Total rejected</p>
            </div>
          </div>
        </CardBody>
      </Card>

      <Card className="border-zinc-800/50 bg-zinc-950/40">
        <CardBody className="p-0">
          <div className="border-b border-zinc-800/60 px-6 py-4">
            <h2 className="text-base font-medium text-zinc-100">
              Learning sessions
            </h2>
          </div>
          {filtered.length === 0 ? (
            <p className="px-6 py-10 text-sm text-zinc-500">
              No sessions in this period yet.
            </p>
          ) : (
            <ul className="divide-y divide-zinc-900/80">
              {filtered.slice(0, 20).map((s) => (
                <li
                  key={s.session_id}
                  className="flex flex-wrap items-center justify-between gap-3 px-6 py-4"
                >
                  <div className="min-w-0">
                    <p className="truncate text-sm font-medium text-zinc-100">
                      {s.mission || s.summary || s.session_id}
                    </p>
                    <p className="mt-0.5 font-mono text-[11px] text-zinc-600">
                      {s.session_id}
                    </p>
                  </div>
                  <div className="flex items-center gap-4 text-xs text-zinc-500">
                    <span
                      className={cn(
                        s.status === "completed" && "text-emerald-400",
                        s.status === "failed" && "text-red-400"
                      )}
                    >
                      {s.status}
                    </span>
                    <span>+{s.knowledge_added ?? 0}</span>
                    <span>
                      {s.duration_seconds != null
                        ? `${Math.round(Number(s.duration_seconds))}s`
                        : "—"}
                    </span>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </CardBody>
      </Card>
    </div>
  );
}

function Metric({
  label,
  value,
  tone,
}: {
  label: string;
  value: string;
  tone: "green" | "blue" | "neutral";
}) {
  return (
    <Card className="border-zinc-800/50 bg-zinc-950/40">
      <CardBody className="p-5">
        <p className="text-xs uppercase tracking-wider text-zinc-500">{label}</p>
        <p
          className={cn(
            "mt-2 text-3xl font-semibold",
            tone === "green" && "text-emerald-300",
            tone === "blue" && "text-sky-300",
            tone === "neutral" && "text-zinc-100"
          )}
        >
          {value}
        </p>
      </CardBody>
    </Card>
  );
}
