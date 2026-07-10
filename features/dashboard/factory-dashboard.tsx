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
        "Expand Industry Library — factory learn cycle",
        true
      );
      setMsg(res.ok ? res.message || "Mission dispatched" : res.reason || "Failed");
      await refresh();
    } finally {
      setBusy(false);
    }
  }

  const journal = (kpis.recent_activity || []).slice(0, 14);

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

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          label="Rows added today"
          value={`+${kpis.rows_added_today}`}
          hint={`Week +${kpis.rows_added_week} · Month +${kpis.rows_added_month}`}
          tone="green"
        />
        <MetricCard
          label="Dataset coverage"
          value={`${kpis.dataset_coverage}%`}
          hint={`${kpis.populated_datasets}/${kpis.total_datasets} datasets · ${kpis.total_rows} rows`}
          tone="blue"
        />
        <MetricCard
          label="Dataset quality"
          value={String(kpis.dataset_quality)}
          hint={
            kpis.average_confidence != null
              ? `Avg confidence ${Math.round(kpis.average_confidence * 100)}%`
              : "Quality score"
          }
          tone="green"
        />
        <MetricCard
          label="Export status"
          value={String(kpis.exports_generated)}
          hint={kpis.export_status}
          tone="blue"
          href="/exports"
        />
      </div>

      <div className="grid gap-4 lg:grid-cols-3">
        <Card className="lg:col-span-2">
          <CardBody className="space-y-4 p-6">
            <div className="grid gap-4 sm:grid-cols-2">
              <div>
                <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                  Current mission
                </p>
                <p className="mt-2 text-lg font-medium text-[var(--text)]">
                  {kpis.current_mission}
                </p>
              </div>
              <div>
                <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
                  Current activity
                </p>
                <p className="mt-2 text-base text-[var(--text-muted)]">
                  {kpis.current_activity}
                </p>
              </div>
            </div>
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
              <Mini label="Schema completeness" value={`${kpis.schema_completeness}%`} />
              <Mini label="Source freshness" value={`${kpis.source_freshness}%`} />
              <Mini
                label="Duplicate rate"
                value={`${Math.round(kpis.duplicate_rate * 100)}%`}
              />
              <Mini
                label="Mission success"
                value={`${kpis.mission_success_rate}%`}
              />
            </div>
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
              <Mini label="Verified sources" value={String(kpis.verified_sources)} />
              <Mini label="Active sources" value={String(kpis.active_sources)} />
              <Mini label="Industries" value={String(kpis.total_industries)} />
              <Mini label="Dataset version" value={kpis.dataset_version} />
            </div>
            <div>
              <div className="mb-2 flex justify-between text-xs text-[var(--text-faint)]">
                <span>Coverage progress</span>
                <span>{kpis.dataset_coverage}%</span>
              </div>
              <Progress value={kpis.dataset_coverage} />
            </div>
            <p className="text-xs text-[var(--text-faint)]">
              Source · {kpis.current_source} · Document · {kpis.current_document}
              {kpis.latest_industry ? ` · Latest · ${kpis.latest_industry}` : ""}
            </p>
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
              <p className="mt-1 text-sm text-[var(--text-muted)]">
                Pipeline: Mission → Collect → Extract → Validate → Publish → Export
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
              <Link href="/exports">
                <Button variant="secondary" className="w-full">
                  View exports
                </Button>
              </Link>
              {msg ? (
                <p className="text-xs text-[var(--text-faint)]">{msg}</p>
              ) : null}
            </div>
          </CardBody>
        </Card>
      </div>

      <div className="grid gap-4 lg:grid-cols-2">
        <Card>
          <CardHeader
            title="Latest activity"
            description="Factory pipeline events"
          />
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
          <CardHeader title="Factory KPIs" description="Official production metrics" />
          <CardBody className="grid grid-cols-2 gap-3 p-6">
            <Mini label="Rows this week" value={`+${kpis.rows_added_week}`} />
            <Mini label="Rows this month" value={`+${kpis.rows_added_month}`} />
            <Mini label="Datasets updated" value={String(kpis.datasets_updated)} />
            <Mini label="Pending quality" value={String(kpis.pending_quality)} />
            <Mini label="Exports generated" value={String(kpis.exports_generated)} />
            <Mini
              label="Last session"
              value={kpis.last_session ? kpis.last_session.slice(0, 16) : "—"}
            />
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
