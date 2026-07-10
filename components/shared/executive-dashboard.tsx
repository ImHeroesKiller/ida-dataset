"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { Card, CardBody } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { useLearningSessions } from "@/lib/use-learning-sessions";
import { cn } from "@/lib/utils";

export type ExecutiveKpis = {
  knowledge_coverage: number;
  knowledge_added_today: number;
  knowledge_updated_today: number;
  knowledge_rejected: number;
  pending_review: number;
  knowledge_quality_score: number;
  average_confidence: number | null;
  growing_count: number;
  gaps_count: number;
  coverage_message: string;
  growth_message: string;
};

export function ExecutiveDashboard({ kpis: initial }: { kpis: ExecutiveKpis }) {
  const { dashboard, activity, startLearning, loading } = useLearningSessions(6000);
  const [kpis, setKpis] = useState(initial);
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);

  useEffect(() => {
    const id = setInterval(async () => {
      try {
        const res = await fetch("/api/journal", { cache: "no-store" });
        const data = await res.json();
        const k = data.kpis || data;
        if (k) {
          setKpis((prev) => ({
            ...prev,
            knowledge_added_today:
              k.added_today ?? k.knowledge_added_today ?? prev.knowledge_added_today,
            pending_review: k.pending_review ?? prev.pending_review,
            knowledge_coverage: k.coverage ?? k.knowledge_coverage ?? prev.knowledge_coverage,
          }));
        }
      } catch {
        /* ignore */
      }
    }, 8000);
    return () => clearInterval(id);
  }, []);

  const status = dashboard.github_actions?.running
    ? "running"
    : dashboard.status || "idle";
  const mission =
    dashboard.current_mission ||
    activity.current_thought ||
    "Standing by for the next learning session";

  const nextAction =
    kpis.pending_review > 0
      ? {
          label: `Review ${kpis.pending_review} waiting candidate${kpis.pending_review === 1 ? "" : "s"}`,
          href: "/review",
          tone: "amber" as const,
        }
      : status === "running"
        ? {
            label: "Learning in progress — monitor journal",
            href: "/",
            tone: "green" as const,
          }
        : {
            label: "Start a learning session",
            href: null,
            tone: "blue" as const,
          };

  async function onStart() {
    setBusy(true);
    setMsg(null);
    try {
      const res = await startLearning(
        "Continue continuous learning — expand knowledge coverage",
        true
      );
      setMsg(res.ok ? res.message || "Learning started" : res.reason || res.message || "Failed");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="mx-auto max-w-6xl space-y-8">
      <header className="space-y-2">
        <p className="text-xs font-medium uppercase tracking-[0.2em] text-zinc-500">
          IDA Executive Learning
        </p>
        <h1 className="text-3xl font-semibold tracking-tight text-zinc-50 sm:text-4xl">
          What is IDA learning now?
        </h1>
        <p className="max-w-2xl text-base leading-relaxed text-zinc-400">
          {loading
            ? "Loading learning status…"
            : activity.current_task || mission}
        </p>
        <div className="flex flex-wrap items-center gap-2 pt-1">
          <StatusPill status={status} />
          <span className="text-sm text-zinc-500">
            {dashboard.session_duration != null
              ? `Last session ${Math.round(Number(dashboard.session_duration))}s`
              : "Continuous learning via GitHub Actions"}
          </span>
        </div>
      </header>

      {/* Primary metrics */}
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <StatCard
          label="Knowledge today"
          value={`+${kpis.knowledge_added_today}`}
          hint={kpis.growth_message}
          tone="green"
        />
        <StatCard
          label="Knowledge coverage"
          value={`${kpis.knowledge_coverage}%`}
          hint={kpis.coverage_message}
          tone="blue"
        />
        <StatCard
          label="Waiting review"
          value={String(kpis.pending_review)}
          hint={
            kpis.pending_review > 0
              ? "Action needed"
              : "Queue clear"
          }
          tone={kpis.pending_review > 0 ? "amber" : "neutral"}
          href="/review"
        />
        <StatCard
          label="Learning quality"
          value={`${kpis.knowledge_quality_score}`}
          hint={
            kpis.average_confidence != null
              ? `Avg confidence ${Math.round(kpis.average_confidence * 100)}%`
              : "Quality score"
          }
          tone="neutral"
        />
      </div>

      <div className="grid gap-4 lg:grid-cols-3">
        <Card className="border-zinc-800/50 bg-zinc-950/40 lg:col-span-2">
          <CardBody className="space-y-4 p-6">
            <div>
              <p className="text-xs uppercase tracking-wider text-zinc-500">
                Current mission
              </p>
              <p className="mt-2 text-lg font-medium text-zinc-100">
                {dashboard.current_mission || "No active mission"}
              </p>
            </div>
            <div>
              <p className="text-xs uppercase tracking-wider text-zinc-500">
                Current task
              </p>
              <p className="mt-2 text-base text-zinc-300">
                {activity.current_task || activity.current_thought || "Idle"}
              </p>
            </div>
            <div className="grid grid-cols-2 gap-3 pt-2 sm:grid-cols-3">
              <Mini
                label="Knowledge growth"
                value={`+${kpis.knowledge_added_today} today`}
              />
              <Mini label="Growing datasets" value={String(kpis.growing_count)} />
              <Mini label="Knowledge gaps" value={String(kpis.gaps_count)} />
            </div>
          </CardBody>
        </Card>

        <Card className="border-zinc-800/50 bg-zinc-950/40">
          <CardBody className="flex h-full flex-col justify-between gap-4 p-6">
            <div>
              <p className="text-xs uppercase tracking-wider text-zinc-500">
                What should I do next?
              </p>
              <p
                className={cn(
                  "mt-3 text-lg font-medium leading-snug",
                  nextAction.tone === "amber" && "text-amber-200",
                  nextAction.tone === "green" && "text-emerald-300",
                  nextAction.tone === "blue" && "text-sky-300"
                )}
              >
                {nextAction.label}
              </p>
            </div>
            <div className="flex flex-col gap-2">
              {nextAction.href ? (
                <Link href={nextAction.href}>
                  <Button className="w-full">Open Review</Button>
                </Link>
              ) : (
                <Button className="w-full" disabled={busy} onClick={onStart}>
                  Start Learning
                </Button>
              )}
              <Link href="/knowledge">
                <Button variant="secondary" className="w-full">
                  Browse Knowledge
                </Button>
              </Link>
              {msg ? (
                <p className="text-[11px] text-zinc-500">{msg}</p>
              ) : null}
            </div>
          </CardBody>
        </Card>
      </div>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <StatCard
          label="Average confidence"
          value={
            kpis.average_confidence != null
              ? `${Math.round(kpis.average_confidence * 100)}%`
              : "—"
          }
          hint="Across recent candidates"
          tone="blue"
        />
        <StatCard
          label="Updated today"
          value={String(kpis.knowledge_updated_today)}
          hint="Knowledge refreshes"
          tone="neutral"
        />
        <StatCard
          label="Rejected"
          value={String(kpis.knowledge_rejected)}
          hint="Human quality gate"
          tone="neutral"
        />
        <StatCard
          label="Sessions"
          value={String(dashboard.history?.today?.sessions ?? 0)}
          hint="Learning runs today"
          tone="green"
        />
      </div>
    </div>
  );
}

function StatusPill({ status }: { status: string }) {
  const running = status === "running" || status === "queued";
  const failed = status === "failed" || status === "error";
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-xs font-medium",
        running && "bg-emerald-500/15 text-emerald-300",
        failed && "bg-red-500/15 text-red-300",
        !running && !failed && "bg-sky-500/15 text-sky-300"
      )}
    >
      <span
        className={cn(
          "h-1.5 w-1.5 rounded-full",
          running && "bg-emerald-400 animate-pulse",
          failed && "bg-red-400",
          !running && !failed && "bg-sky-400"
        )}
      />
      {running ? "Running" : failed ? "Attention" : "Ready"}
    </span>
  );
}

function StatCard({
  label,
  value,
  hint,
  tone,
  href,
}: {
  label: string;
  value: string;
  hint?: string;
  tone: "green" | "blue" | "amber" | "neutral";
  href?: string;
}) {
  const tones = {
    green: "text-emerald-300",
    blue: "text-sky-300",
    amber: "text-amber-200",
    neutral: "text-zinc-100",
  };
  const inner = (
    <Card className="border-zinc-800/50 bg-zinc-950/40 transition-colors hover:border-zinc-700/80">
      <CardBody className="p-5">
        <p className="text-xs uppercase tracking-wider text-zinc-500">{label}</p>
        <p className={cn("mt-2 text-3xl font-semibold tracking-tight", tones[tone])}>
          {value}
        </p>
        {hint ? <p className="mt-2 text-xs text-zinc-500">{hint}</p> : null}
      </CardBody>
    </Card>
  );
  if (href) return <Link href={href}>{inner}</Link>;
  return inner;
}

function Mini({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl bg-zinc-900/50 px-3 py-2">
      <div className="text-[10px] uppercase tracking-wider text-zinc-600">
        {label}
      </div>
      <div className="mt-0.5 text-sm font-medium text-zinc-200">{value}</div>
    </div>
  );
}
