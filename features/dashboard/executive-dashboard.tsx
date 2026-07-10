"use client";

import Link from "next/link";
import { useCallback, useEffect, useState } from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { MetricCard } from "@/components/ui/metric-card";
import { Progress } from "@/components/ui/progress";
import { EmptyState } from "@/components/ui/empty-state";
import { useLearning } from "@/hooks/learning-provider";
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
  sources_count?: number;
  mode?: string;
  auto_publish?: boolean;
  /** Industry Library growth metrics (Sprint Knowledge v1.0) */
  total_industries?: number;
  industries_learned?: number;
  field_coverage_pct?: number;
  coverage_progress_pct?: number;
  verified_sources?: number;
  knowledge_freshness_pct?: number;
  duplicate_rate?: number;
  dataset_version?: string;
  last_successful_session?: string | null;
  current_source?: string | null;
  current_document?: string | null;
  current_mission?: string | null;
  latest_industry?: string | null;
  industry_names?: string[];
};

type PublishView = {
  status?: string;
  total?: number;
  published?: number;
  remaining?: number;
  speed?: number;
  unit?: string;
  eta_seconds?: number | null;
  current_dataset?: string | null;
  current_knowledge?: string | null;
  next_knowledge?: string | null;
  mode?: string;
  auto_publish?: boolean;
  queue?: Array<{
    candidate_id: string;
    name: string;
    dataset: string;
    confidence: number;
  }>;
  feed?: Array<{
    ts: string;
    knowledge_type: string;
    name: string;
    dataset: string;
    source: string;
    confidence: number;
    published_at: string;
  }>;
  journal_tail?: Array<Record<string, unknown>>;
};

export function ExecutiveDashboard({ kpis: initial }: { kpis: ExecutiveKpis }) {
  const { dashboard, activity, startLearning, loading } = useLearning();
  const [kpis, setKpis] = useState(initial);
  const [pub, setPub] = useState<PublishView>({});
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);
  const [publishing, setPublishing] = useState(false);

  const refreshPublish = useCallback(async () => {
    try {
      const res = await fetch("/api/publish-queue", { cache: "no-store" });
      const data = await res.json();
      if (data.ok !== false) setPub(data);
    } catch {
      /* ignore */
    }
  }, []);

  useEffect(() => {
    void refreshPublish();
    const id = setInterval(() => void refreshPublish(), 1500);
    return () => clearInterval(id);
  }, [refreshPublish]);

  // Poll only — progressive rate is enforced in GET /api/publish-queue (backend)
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
            knowledge_coverage:
              k.coverage ?? k.knowledge_coverage ?? prev.knowledge_coverage,
          }));
        }
      } catch {
        /* ignore */
      }
    }, 6000);
    return () => clearInterval(id);
  }, []);

  const status = dashboard.github_actions?.running
    ? "running"
    : (pub.remaining || 0) > 0
      ? "running"
      : dashboard.status || "idle";

  const mission =
    dashboard.current_mission ||
    activity.current_thought ||
    "Standing by for the next learning session";

  const publishedToday =
    (pub.published || 0) > 0
      ? pub.published
      : kpis.knowledge_added_today;

  const nextAction =
    !pub.auto_publish && kpis.pending_review > 0
      ? {
          label: `Review ${kpis.pending_review} waiting candidate${kpis.pending_review === 1 ? "" : "s"}`,
          href: "/review",
          tone: "amber" as const,
        }
      : (pub.remaining || 0) > 0
        ? {
            label: `Publishing ${pub.remaining} knowledge rows…`,
            href: null,
            tone: "green" as const,
          }
        : status === "running"
          ? {
              label: "Learning in progress — watch the journal",
              href: null,
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
        "Expand Industry Library — acquire verified industry knowledge from trusted sources",
        true
      );
      setMsg(
        res.ok
          ? res.message || "Learning started"
          : res.reason || res.message || "Failed"
      );
      // Kick progressive publish for any pending
      await fetch("/api/publish-queue", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "enqueue" }),
      });
      await refreshPublish();
    } finally {
      setBusy(false);
    }
  }

  async function onDrain() {
    setPublishing(true);
    setMsg(null);
    try {
      const res = await fetch("/api/publish-queue", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "start" }),
      });
      const data = await res.json();
      setMsg(
        data.ok
          ? "Publish queue drained"
          : data.error || "Publish failed"
      );
      await refreshPublish();
    } finally {
      setPublishing(false);
    }
  }

  const eta =
    pub.eta_seconds != null
      ? pub.eta_seconds < 60
        ? `${pub.eta_seconds}s`
        : `${Math.floor(pub.eta_seconds / 60)}m ${pub.eta_seconds % 60}s`
      : "—";

  const feed = pub.feed || [];
  const journal = (pub.journal_tail || []).slice().reverse().slice(0, 12);

  return (
    <div className="mx-auto max-w-6xl space-y-8">
      <header className="space-y-3">
        <div className="flex flex-wrap items-center gap-2">
          <p className="text-xs font-medium uppercase tracking-[0.18em] text-[var(--text-faint)]">
            IDA Executive Learning
          </p>
          <ModeBadge
            mode={pub.mode || kpis.mode || "development"}
            auto={Boolean(pub.auto_publish ?? kpis.auto_publish)}
          />
        </div>
        <h1 className="text-3xl font-semibold tracking-tight text-[var(--text)] sm:text-4xl">
          What is IDA learning now?
        </h1>
        <p className="max-w-2xl text-base leading-relaxed text-[var(--text-muted)]">
          {loading
            ? "Loading learning status…"
            : activity.current_task || mission}
        </p>
        <div className="flex flex-wrap items-center gap-2 pt-1">
          <StatusPill status={status} />
          <span className="text-sm text-[var(--text-faint)]">
            {(pub.remaining || 0) > 0
              ? `Publishing · ${pub.current_knowledge || "knowledge"}`
              : "Ready to learn"}
          </span>
        </div>
      </header>

      {/* Primary cards — real knowledge growth */}
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          label="Knowledge growth today"
          value={`+${kpis.knowledge_added_today}`}
          hint={kpis.growth_message}
          tone="green"
        />
        <MetricCard
          label="Industries learned"
          value={String(kpis.industries_learned ?? kpis.total_industries ?? 0)}
          hint={
            kpis.industry_names?.length
              ? kpis.industry_names.join(" · ")
              : "Industry Library"
          }
          tone="blue"
        />
        <MetricCard
          label="Coverage progress"
          value={`${kpis.coverage_progress_pct ?? kpis.knowledge_coverage}%`}
          hint={kpis.coverage_message}
          tone="green"
        />
        <MetricCard
          label="Learning quality"
          value={String(kpis.knowledge_quality_score)}
          hint={
            kpis.average_confidence != null
              ? `Avg confidence ${Math.round(kpis.average_confidence * 100)}%`
              : "Quality score from coverage + confidence"
          }
          tone="blue"
        />
      </div>

      <div className="grid gap-4 lg:grid-cols-3">
        <Card className="lg:col-span-2">
          <CardBody className="space-y-4 p-6">
            <div>
              <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                Current mission
              </p>
              <p className="mt-2 text-lg font-medium text-[var(--text)]">
                {kpis.current_mission ||
                  dashboard.current_mission ||
                  "Expand Industry Library"}
              </p>
            </div>
            <div className="grid gap-3 sm:grid-cols-2">
              <div>
                <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                  Latest knowledge
                </p>
                <p className="mt-2 text-base text-[var(--text-muted)]">
                  {kpis.latest_industry ||
                    pub.current_knowledge ||
                    activity.current_task ||
                    "—"}
                </p>
              </div>
              <div>
                <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                  Current source / document
                </p>
                <p className="mt-2 text-sm text-[var(--text-muted)]">
                  {kpis.current_source || activity.current_source || "—"}
                </p>
                <p className="text-xs text-[var(--text-faint)]">
                  {kpis.current_document || activity.current_document || "—"}
                </p>
              </div>
            </div>
            <div className="grid grid-cols-2 gap-3 pt-1 sm:grid-cols-4">
              <Mini
                label="Field coverage"
                value={`${kpis.field_coverage_pct ?? "—"}%`}
              />
              <Mini
                label="Verified sources"
                value={String(kpis.verified_sources ?? kpis.sources_count ?? "—")}
              />
              <Mini
                label="Freshness"
                value={`${kpis.knowledge_freshness_pct ?? "—"}%`}
              />
              <Mini
                label="Dataset version"
                value={kpis.dataset_version || "—"}
              />
            </div>
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
              <Mini
                label="Duplicate rate"
                value={`${Math.round((kpis.duplicate_rate ?? 0) * 100)}%`}
              />
              <Mini
                label="Rows updated"
                value={String(kpis.knowledge_updated_today)}
              />
              <Mini
                label="Last session"
                value={
                  kpis.last_successful_session
                    ? String(kpis.last_successful_session).slice(0, 18)
                    : "—"
                }
              />
            </div>
            {(kpis.coverage_progress_pct != null || kpis.knowledge_coverage) && (
              <div className="space-y-2 pt-1">
                <div className="flex justify-between text-xs text-[var(--text-faint)]">
                  <span>Industry catalog progress</span>
                  <span>
                    {kpis.coverage_progress_pct ?? kpis.knowledge_coverage}%
                  </span>
                </div>
                <Progress
                  value={Number(
                    kpis.coverage_progress_pct ?? kpis.knowledge_coverage ?? 0
                  )}
                />
              </div>
            )}
          </CardBody>
        </Card>

        <Card>
          <CardBody className="flex h-full flex-col justify-between gap-4 p-6">
            <div>
              <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                What should I do next?
              </p>
              <p
                className={cn(
                  "mt-3 text-lg font-medium leading-snug",
                  nextAction.tone === "amber" && "text-amber-600 dark:text-amber-200",
                  nextAction.tone === "green" && "text-emerald-600 dark:text-emerald-300",
                  nextAction.tone === "blue" && "text-blue-600 dark:text-sky-300"
                )}
              >
                {nextAction.label}
              </p>
            </div>
            <div className="flex flex-col gap-2">
              {nextAction.href ? (
                <Link href={nextAction.href}>
                  <Button className="w-full" variant="warning">
                    Open Review
                  </Button>
                </Link>
              ) : (
                <Button className="w-full" disabled={busy} onClick={onStart}>
                  Start Learning
                </Button>
              )}
              {(pub.remaining || 0) > 0 ? (
                <Button
                  variant="success"
                  className="w-full"
                  disabled={publishing}
                  onClick={onDrain}
                >
                  {publishing ? "Publishing…" : "Publish queue now"}
                </Button>
              ) : (
                <Link href="/knowledge">
                  <Button variant="secondary" className="w-full">
                    Browse Knowledge
                  </Button>
                </Link>
              )}
              {msg ? (
                <p className="text-xs text-[var(--text-faint)]">{msg}</p>
              ) : null}
            </div>
          </CardBody>
        </Card>
      </div>

      {/* Progressive publishing widget + knowledge queue */}
      <div className="grid gap-4 lg:grid-cols-2">
        <Card>
          <CardHeader
            title="Publishing progress"
            description="Backend-paced progressive publish"
          />
          <CardBody className="space-y-4">
            <div className="flex items-end justify-between gap-3">
              <div>
                <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                  Published
                </p>
                <p className="mt-1 text-3xl font-semibold text-[var(--text)]">
                  {pub.published ?? 0}
                  <span className="text-lg text-[var(--text-faint)]">
                    {" "}
                    / {pub.total ?? 0}
                  </span>
                </p>
              </div>
              <div className="text-right text-sm text-[var(--text-muted)]">
                <div>Queue remaining · {pub.remaining ?? 0}</div>
                <div>
                  Speed · {pub.speed ?? 1} row/sec
                </div>
                <div>ETA · {eta}</div>
              </div>
            </div>
            <Progress
              value={
                pub.total
                  ? Math.round(
                      ((pub.published || 0) / Math.max(pub.total, 1)) * 100
                    )
                  : 0
              }
            />
            <p className="text-xs text-[var(--text-faint)]">
              Current · {pub.current_knowledge || "—"} ·{" "}
              {pub.current_dataset || "—"}
            </p>
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Knowledge queue"
            description="Visibly shrinks as knowledge is published"
          />
          <CardBody className="max-h-56 space-y-2 overflow-y-auto scrollbar-thin">
            {!pub.queue?.length ? (
              <Empty hint="Publish queue is empty. Start learning to generate knowledge." />
            ) : (
              pub.queue.map((q, i) => (
                <div
                  key={q.candidate_id}
                  className="flex items-center justify-between rounded-xl bg-[var(--panel-2)] px-3 py-2 text-sm"
                >
                  <div className="min-w-0">
                    <p className="truncate font-medium text-[var(--text)]">
                      {i === 0 ? "Next · " : ""}
                      {q.name}
                    </p>
                    <p className="text-xs text-[var(--text-faint)]">
                      {q.dataset}
                    </p>
                  </div>
                  <span className="text-xs text-blue-600 dark:text-sky-300">
                    {Math.round(q.confidence * 100)}%
                  </span>
                </div>
              ))
            )}
          </CardBody>
        </Card>
      </div>

      {/* Knowledge feed + journal */}
      <div className="grid gap-4 lg:grid-cols-2">
        <Card>
          <CardHeader
            title="Knowledge feed"
            description="Newest published knowledge first"
          />
          <CardBody className="max-h-72 space-y-2 overflow-y-auto scrollbar-thin">
            {!feed.length ? (
              <Empty hint="No knowledge published yet. Start a learning mission." />
            ) : (
              feed.map((f, i) => (
                <div
                  key={`${f.published_at}-${i}`}
                  className="border-b border-[var(--border)] py-2 last:border-0"
                >
                  <div className="flex items-center justify-between gap-2">
                    <span className="text-xs font-medium text-blue-600 dark:text-sky-300">
                      {f.knowledge_type}
                    </span>
                    <span className="text-[11px] text-[var(--text-faint)]">
                      {String(f.published_at || "").slice(11, 19)}
                    </span>
                  </div>
                  <p className="mt-0.5 text-sm font-medium text-[var(--text)]">
                    {f.name}
                  </p>
                  <p className="text-xs text-[var(--text-faint)]">
                    {f.dataset} · {f.source} ·{" "}
                    {Math.round((f.confidence || 0) * 100)}%
                  </p>
                </div>
              ))
            )}
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Learning journal"
            description="Human-readable learning actions"
          />
          <CardBody className="max-h-72 space-y-1.5 overflow-y-auto font-mono text-[11px] scrollbar-thin">
            {!journal.length ? (
              <Empty hint="Journal is quiet. Learning activity will appear here." />
            ) : (
              journal.map((ev, i) => (
                <div key={i} className="flex gap-2 text-[var(--text-muted)]">
                  <span className="w-14 shrink-0 text-[var(--text-faint)]">
                    {String(ev.ts || "").slice(11, 19)}
                  </span>
                  <span className="w-32 shrink-0 font-medium text-emerald-600 dark:text-emerald-300">
                    {humanVerb(String(ev.verb || ""), String(ev.stage || ""))}
                  </span>
                  <span className="truncate">{String(ev.detail || "")}</span>
                </div>
              ))
            )}
          </CardBody>
        </Card>
      </div>
    </div>
  );
}

function humanVerb(verb: string, stage: string): string {
  const map: Record<string, string> = {
    Publishing: "Publishing",
    "Knowledge Added": "Knowledge Added",
    "Learning Completed": "Learning Completed",
    Searching: "Searching",
    Reading: "Reading",
    Understanding: "Understanding",
    Extracting: "Extracting",
    Validating: "Validating",
    Connector: "Searching",
    Pipeline: "Extracting",
    Validator: "Validating",
  };
  if (map[verb]) return map[verb];
  if (stage === "publish") return "Publishing";
  return verb || "Learning";
}

function ModeBadge({ mode, auto }: { mode: string; auto: boolean }) {
  return (
    <span className="rounded-full bg-[var(--panel-2)] px-2.5 py-0.5 text-[11px] font-medium text-[var(--text-muted)]">
      {mode === "production" ? "Production" : "Development"}
      {auto ? " · Auto publish" : " · Review required"}
    </span>
  );
}

function StatusPill({ status }: { status: string }) {
  const running = status === "running" || status === "queued";
  const failed = status === "failed" || status === "error";
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-xs font-medium",
        running && "bg-emerald-500/15 text-emerald-700 dark:text-emerald-300",
        failed && "bg-red-500/15 text-red-700 dark:text-red-300",
        !running && !failed && "bg-blue-500/15 text-blue-700 dark:text-sky-300"
      )}
    >
      <span
        className={cn(
          "h-1.5 w-1.5 rounded-full",
          running && "animate-pulse bg-emerald-500",
          failed && "bg-red-500",
          !running && !failed && "bg-blue-500"
        )}
      />
      {running ? "Running" : failed ? "Attention" : "Ready"}
    </span>
  );
}

function Mini({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl bg-[var(--panel-2)] px-3 py-2">
      <div className="text-[10px] uppercase tracking-wider text-[var(--text-faint)]">
        {label}
      </div>
      <div className="mt-0.5 text-sm font-medium text-[var(--text)]">{value}</div>
    </div>
  );
}

function Empty({ hint }: { hint: string }) {
  return <EmptyState hint={hint} />;
}
