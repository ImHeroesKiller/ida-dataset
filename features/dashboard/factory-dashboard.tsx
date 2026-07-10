"use client";

import Link from "next/link";
import { useCallback, useEffect, useState } from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { MetricCard } from "@/components/ui/metric-card";
import { Progress } from "@/components/ui/progress";
import { useLearning } from "@/hooks/learning-provider";
import { cn } from "@/lib/utils";
import type { FactoryKpis } from "@/lib/factory-kpis";

export function FactoryDashboard({ kpis: initial }: { kpis: FactoryKpis }) {
  const { dashboard, activity, startLearning, loading } = useLearning();
  const [kpis, setKpis] = useState(initial);
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);

  const refresh = useCallback(async () => {
    try {
      const res = await fetch("/api/factory/status", { cache: "no-store" });
      if (!res.ok) return;
      const data = await res.json();
      if (data.ok && data.kpis) setKpis(data.kpis as FactoryKpis);
    } catch {
      /* ignore */
    }
  }, []);

  useEffect(() => {
    const id = setInterval(() => void refresh(), 8000);
    return () => clearInterval(id);
  }, [refresh]);

  const running =
    dashboard.github_actions?.running || kpis.factory_status === "running";

  async function onStart() {
    setBusy(true);
    setMsg(null);
    try {
      const res = await startLearning(
        "Produce Industry Dataset — factory learn cycle",
        true
      );
      setMsg(
        res.ok ? res.message || "Mission dispatched" : res.reason || "Failed"
      );
      await refresh();
    } finally {
      setBusy(false);
    }
  }

  const journal = (kpis.recent_activity || []).slice(0, 14);
  const industry = kpis.datasets?.find((d) => d.name === "industry_library");

  return (
    <div className="mx-auto max-w-6xl space-y-8">
      <header className="space-y-3">
        <p className="text-xs font-medium uppercase tracking-[0.18em] text-[var(--text-faint)]">
          IDA Dataset Factory
        </p>
        <h1 className="text-3xl font-semibold tracking-tight text-[var(--text)] sm:text-4xl">
          Automatic Knowledge Factory
        </h1>
        <p className="max-w-2xl text-base leading-relaxed text-[var(--text-muted)]">
          {loading
            ? "Loading factory status…"
            : kpis.current_activity || activity.current_task || "Ready"}
        </p>
        <div className="flex flex-wrap items-center gap-2 pt-1">
          <StatusPill running={running} status={kpis.factory_status} />
          <span className="text-sm text-[var(--text-faint)]">
            Mission · {kpis.current_mission}
          </span>
        </div>
      </header>

      {/* Official Factory KPIs only */}
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          label="Factory status"
          value={running ? "Running" : kpis.factory_status === "error" ? "Error" : "Idle"}
          hint={kpis.current_activity}
          tone={running ? "green" : "neutral"}
        />
        <MetricCard
          label="Rows added today"
          value={`+${kpis.rows_added_today}`}
          hint={`Week +${kpis.rows_added_week} · Month +${kpis.rows_added_month}`}
          tone="green"
        />
        <MetricCard
          label="Dataset coverage"
          value={`${kpis.dataset_coverage}%`}
          hint={kpis.coverage_label}
          tone="blue"
        />
        <MetricCard
          label="Dataset readiness"
          value={String(kpis.dataset_readiness)}
          hint="0–100 composite readiness score"
          tone="green"
        />
      </div>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          label="Average confidence"
          value={
            kpis.average_confidence != null
              ? `${Math.round(kpis.average_confidence * 100)}%`
              : "—"
          }
          hint="Product knowledge confidence"
          tone="blue"
        />
        <MetricCard
          label="Duplicate rate"
          value={`${Math.round((kpis.duplicate_rate || 0) * 1000) / 10}%`}
          hint="Lower is better"
          tone="neutral"
        />
        <MetricCard
          label="Freshness"
          value={`${kpis.freshness}%`}
          hint="Rows within product freshness window"
          tone="blue"
        />
        <MetricCard
          label="Mission success rate"
          value={`${kpis.mission_success_rate}%`}
          hint="Completed / active missions"
          tone="green"
        />
      </div>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <MetricCard
          label="Exports generated"
          value={String(kpis.exports_generated)}
          hint="Training package artifacts"
          tone="blue"
          href="/exports"
        />
        <MetricCard
          label="Current mission"
          value={String(kpis.current_mission).slice(0, 28)}
          hint={kpis.current_activity}
          tone="neutral"
        />
        <MetricCard
          label="Rows this period"
          value={`W+${kpis.rows_added_week} · M+${kpis.rows_added_month}`}
          hint="Week / month production"
          tone="green"
        />
      </div>

      <div className="grid gap-4 lg:grid-cols-3">
        <Card className="lg:col-span-2">
          <CardBody className="space-y-4 p-6">
            <div>
              <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                Product coverage (not sprint target)
              </p>
              <p className="mt-2 text-lg font-medium text-[var(--text)]">
                {kpis.coverage_label}
              </p>
              <p className="mt-1 text-xs text-[var(--text-faint)]">
                Sprint milestones are informational only (e.g. phase1=
                {kpis.sprint_milestones?.industry_phase1 ?? 50}). Product target
                for industry = {kpis.industry_product_target}.
              </p>
            </div>
            <div>
              <div className="mb-2 flex justify-between text-xs text-[var(--text-faint)]">
                <span>Industry product coverage</span>
                <span>{kpis.dataset_coverage}%</span>
              </div>
              <Progress value={kpis.dataset_coverage} />
            </div>
            {industry ? (
              <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
                <Mini label="Industry rows" value={String(industry.current_rows)} />
                <Mini label="Product target" value={String(industry.product_target)} />
                <Mini label="Readiness" value={String(industry.readiness)} />
                <Mini
                  label="Completeness"
                  value={`${industry.schema_completeness}%`}
                />
              </div>
            ) : null}
            <div className="space-y-2">
              <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                Coverage by dataset
              </p>
              <div className="max-h-40 space-y-1.5 overflow-y-auto text-sm scrollbar-thin">
                {(kpis.coverage_breakdown || []).map((d) => (
                  <div
                    key={d.name}
                    className="flex items-center justify-between gap-2 text-[var(--text-muted)]"
                  >
                    <span className="truncate font-medium text-[var(--text)]">
                      {d.name}
                    </span>
                    <span className="shrink-0 font-mono text-xs">
                      {d.current} / {d.target} · {d.pct}%
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </CardBody>
        </Card>

        <Card>
          <CardBody className="flex h-full flex-col justify-between gap-4 p-6">
            <div>
              <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                Factory control
              </p>
              <p className="mt-3 text-lg font-medium text-[var(--text)]">
                {running ? "Learn job running" : "Dispatch a learn mission"}
              </p>
            </div>
            <div className="flex flex-col gap-2">
              <Button className="w-full" disabled={busy || running} onClick={onStart}>
                {busy ? "Starting…" : "Start factory learn"}
              </Button>
              <Link href="/datasets">
                <Button variant="secondary" className="w-full">
                  Browse datasets
                </Button>
              </Link>
              {msg ? (
                <p className="text-xs text-[var(--text-faint)]">{msg}</p>
              ) : null}
            </div>
          </CardBody>
        </Card>
      </div>

      {/* Capacity — informational only */}
      <Card>
        <CardHeader
          title="Factory capacity"
          description="Informational throughput estimates — not product targets"
        />
        <CardBody className="grid grid-cols-2 gap-3 p-6 sm:grid-cols-4">
          <Mini
            label="Avg rows / day"
            value={String(kpis.capacity?.average_rows_per_day ?? 0)}
          />
          <Mini
            label="Avg rows / session"
            value={String(kpis.capacity?.average_rows_per_session ?? 0)}
          />
          <Mini
            label="Mission throughput"
            value={String(kpis.capacity?.mission_throughput ?? 0)}
          />
          <Mini
            label="Estimated completion"
            value={kpis.capacity?.estimated_completion || "—"}
          />
        </CardBody>
      </Card>

      <div className="grid gap-4 lg:grid-cols-2">
        <Card>
          <CardHeader title="Latest activity" description="Factory pipeline events" />
          <CardBody className="max-h-72 space-y-1.5 overflow-y-auto font-mono text-[11px] scrollbar-thin">
            {!journal.length ? (
              <p className="text-sm text-[var(--text-faint)]">No activity yet.</p>
            ) : (
              journal.map((ev, i) => (
                <div key={i} className="flex gap-2 text-[var(--text-muted)]">
                  <span className="w-14 shrink-0 text-[var(--text-faint)]">
                    {String(ev.ts || "").slice(11, 19)}
                  </span>
                  <span className="w-28 shrink-0 font-medium text-emerald-600 dark:text-emerald-300">
                    {ev.verb}
                  </span>
                  <span className="truncate">{ev.detail}</span>
                </div>
              ))
            )}
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Dataset readiness"
            description="Per-dataset score beside product coverage"
          />
          <CardBody className="max-h-72 space-y-2 overflow-y-auto scrollbar-thin">
            {(kpis.datasets || [])
              .filter((d) => d.current_rows > 0 || d.name === "industry_library")
              .map((d) => (
                <div
                  key={d.relativePath}
                  className="flex items-center justify-between gap-2 rounded-xl bg-[var(--panel-2)] px-3 py-2 text-sm"
                >
                  <div className="min-w-0">
                    <p className="truncate font-medium text-[var(--text)]">
                      {d.name}
                    </p>
                    <p className="text-xs text-[var(--text-faint)]">
                      {d.coverage_label} · {d.coverage_pct}%
                    </p>
                  </div>
                  <span className="shrink-0 text-sm font-semibold text-emerald-600 dark:text-emerald-300">
                    {d.readiness}
                  </span>
                </div>
              ))}
          </CardBody>
        </Card>
      </div>
    </div>
  );
}

function StatusPill({
  running,
  status,
}: {
  running: boolean;
  status: string;
}) {
  return (
    <span
      className={cn(
        "inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium",
        running
          ? "bg-emerald-500/15 text-emerald-700 dark:text-emerald-300"
          : status === "error"
            ? "bg-red-500/15 text-red-700 dark:text-red-300"
            : "bg-[var(--panel-2)] text-[var(--text-muted)]"
      )}
    >
      {running ? "Running" : status === "error" ? "Error" : "Idle"}
    </span>
  );
}

function Mini({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl bg-[var(--panel-2)] px-3 py-2">
      <p className="text-[10px] uppercase tracking-wider text-[var(--text-faint)]">
        {label}
      </p>
      <p className="mt-0.5 truncate text-sm font-medium text-[var(--text)]">
        {value}
      </p>
    </div>
  );
}
