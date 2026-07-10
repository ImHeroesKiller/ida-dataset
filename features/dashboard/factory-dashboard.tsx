"use client";

import Link from "next/link";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import { useLearning } from "@/hooks/learning-provider";
import { cn } from "@/lib/utils";
import type { FactoryKpis } from "@/lib/factory-kpis";
import type { ExecutiveFactoryView, PipelineStageId } from "@/lib/executive-factory";
import { formatWib, formatWibTime } from "@/lib/time-wib";

type Toast = { id: string; text: string; tone: "ok" | "warn" | "err" };

function useCountUp(value: number, duration = 450) {
  const [display, setDisplay] = useState(value);
  const prev = useRef(value);
  useEffect(() => {
    if (prev.current === value) return;
    const from = prev.current;
    const to = value;
    prev.current = value;
    const start = performance.now();
    let raf = 0;
    const tick = (t: number) => {
      const p = Math.min(1, (t - start) / duration);
      const eased = 1 - Math.pow(1 - p, 3);
      setDisplay(Math.round(from + (to - from) * eased));
      if (p < 1) raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [value, duration]);
  return display;
}

function LiveNumber({
  value,
  prefix = "",
  suffix = "",
  className,
}: {
  value: number;
  prefix?: string;
  suffix?: string;
  className?: string;
}) {
  const n = useCountUp(value);
  return (
    <span className={className}>
      {prefix}
      {n}
      {suffix}
    </span>
  );
}

function mapEventStage(verb?: string, stage?: string, task?: string): PipelineStageId {
  const blob = `${verb || ""} ${stage || ""} ${task || ""}`.toLowerCase();
  if (/complete|finished|done/.test(blob)) return "completed";
  if (/export|packag/.test(blob)) return "export";
  if (/quality|qa\b/.test(blob)) return "quality";
  if (/publish|append|knowledge added|knowledge updated/.test(blob)) return "append";
  if (/validat|review|policy|confidence/.test(blob)) return "validation";
  if (/normaliz/.test(blob)) return "normalization";
  if (/extract|pipeline|entity|understanding/.test(blob)) return "extraction";
  if (/download|document|reading|queue/.test(blob)) return "collection";
  if (/search|connector|planner|gap|discovery|scheduler/.test(blob)) return "discovery";
  return "mission";
}

function statusTone(s: string) {
  if (s === "RUNNING") return "text-emerald-600 dark:text-emerald-300 bg-emerald-500/15";
  if (s === "ERROR") return "text-red-600 dark:text-red-300 bg-red-500/15";
  if (s === "WAITING") return "text-amber-700 dark:text-amber-300 bg-amber-500/15";
  if (s === "ONLINE") return "text-sky-700 dark:text-sky-300 bg-sky-500/15";
  return "text-[var(--text-muted)] bg-[var(--panel-2)]";
}

function sessionStatusBucket(st: string): "queued" | "running" | "completed" | "failed" | "skipped" {
  const s = st.toLowerCase();
  if (s.includes("fail") || s.includes("error")) return "failed";
  if (s.includes("run") || s.includes("progress")) return "running";
  if (s.includes("skip") || s.includes("cancel")) return "skipped";
  if (s.includes("queue") || s.includes("pending")) return "queued";
  return "completed";
}

export function FactoryDashboard({ kpis: initialKpis }: { kpis: FactoryKpis }) {
  const {
    dashboard,
    activity,
    events,
    startLearning,
    loading,
    selectSession,
    replay,
  } = useLearning();
  const [kpis, setKpis] = useState(initialKpis);
  const [exec, setExec] = useState<ExecutiveFactoryView | null>(null);
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);
  const [toasts, setToasts] = useState<Toast[]>([]);
  const [replayIdx, setReplayIdx] = useState(-1);
  const [replayPlaying, setReplayPlaying] = useState(false);
  const [pulse, setPulse] = useState(false);
  const prevSnap = useRef<{
    rows: number;
    mission: string;
    status: string;
    lastEvent: string;
  } | null>(null);

  const pushToast = useCallback((text: string, tone: Toast["tone"] = "ok") => {
    const id = `${Date.now()}-${Math.random().toString(36).slice(2, 7)}`;
    setToasts((t) => [...t.slice(-4), { id, text, tone }]);
    setTimeout(() => {
      setToasts((t) => t.filter((x) => x.id !== id));
    }, 4200);
  }, []);

  const refresh = useCallback(async () => {
    try {
      const res = await fetch("/api/factory/status", { cache: "no-store" });
      if (!res.ok) return;
      const data = await res.json();
      if (data.ok && data.kpis) setKpis(data.kpis as FactoryKpis);
      if (data.ok && data.executive) setExec(data.executive as ExecutiveFactoryView);
    } catch {
      /* ignore */
    }
  }, []);

  useEffect(() => {
    void refresh();
    // Match existing architecture poll cadence (not faster than LearningProvider 5s)
    const id = setInterval(() => void refresh(), 5000);
    return () => clearInterval(id);
  }, [refresh]);

  const gaRunning = Boolean(dashboard.github_actions?.running);
  const status: string = useMemo(() => {
    if (exec?.status) {
      if (gaRunning && exec.status !== "ERROR") return "RUNNING";
      return exec.status;
    }
    if (gaRunning || kpis.factory_status === "running") return "RUNNING";
    if (kpis.factory_status === "error") return "ERROR";
    if (String(activity.status || "").includes("wait")) return "WAITING";
    return "IDLE";
  }, [exec, gaRunning, kpis.factory_status, activity.status]);

  // Real-event toasts + heartbeat pulse
  useEffect(() => {
    const rows = exec?.counters.rows_today ?? kpis.rows_added_today;
    const mission = exec?.current_mission || kpis.current_mission;
    const lastEvent = exec?.heartbeat.last_event || "";
    const prev = prevSnap.current;
    if (!prev) {
      prevSnap.current = { rows, mission, status, lastEvent };
      return;
    }
    if (rows > prev.rows) {
      pushToast(`Rows published · today ${rows} (+${rows - prev.rows})`, "ok");
      setPulse(true);
    }
    if (mission !== prev.mission && status === "RUNNING") {
      pushToast(`Mission started · ${mission}`, "ok");
      setPulse(true);
    }
    if (prev.status === "RUNNING" && status !== "RUNNING" && status !== "ERROR") {
      pushToast("Mission completed", "ok");
      setPulse(true);
    }
    if (status === "ERROR" && prev.status !== "ERROR") {
      pushToast("Workflow failed", "err");
      setPulse(true);
    }
    if (lastEvent && lastEvent !== prev.lastEvent) {
      setPulse(true);
      setTimeout(() => setPulse(false), 900);
    }
    prevSnap.current = { rows, mission, status, lastEvent };
  }, [exec, kpis, status, pushToast]);

  // Live stage from real session events when available
  const liveStage: PipelineStageId = useMemo(() => {
    if (events.length) {
      const last = events[events.length - 1];
      return mapEventStage(last.verb, last.stage, last.current_task || undefined);
    }
    return exec?.current_stage || "mission";
  }, [events, exec?.current_stage]);

  // Replay uses recorded session events only (via useLearning.replay)
  const replayEvents = useMemo(() => {
    if (!events.length) return [];
    return events.filter((e) => e.verb || e.detail);
  }, [events]);

  useEffect(() => {
    if (!replayPlaying) return;
    setReplayIdx(Math.max(0, events.length - 1));
  }, [events, replayPlaying]);

  async function onStart() {
    setBusy(true);
    setMsg(null);
    try {
      // Empty mission → server / Actions dynamic selector
      const res = await startLearning(undefined, true);
      setMsg(res.ok ? res.message || "Mission dispatched" : res.reason || "Failed");
      if (res.ok) pushToast("Mission started", "ok");
      else pushToast(res.reason || "Dispatch failed", "err");
      await refresh();
    } finally {
      setBusy(false);
    }
  }

  async function onReplayLatest() {
    const sid =
      dashboard.last_successful_run?.session_id ||
      dashboard.sessions?.[0]?.session_id ||
      exec?.heartbeat.last_session;
    if (!sid || sid === "—") {
      pushToast("No completed session to replay", "warn");
      return;
    }
    setReplayPlaying(true);
    setReplayIdx(0);
    await replay(sid, 420);
    setReplayPlaying(false);
    pushToast("Replay finished (recorded events)", "ok");
  }

  const counters = exec?.counters || {
    rows_today: kpis.rows_added_today,
    rows_rejected_today: 0,
    documents_processed_today: 0,
    sessions_today: dashboard.history?.today?.sessions || 0,
    rows_week: kpis.rows_added_week,
    rows_month: kpis.rows_added_month,
    average_confidence: kpis.average_confidence,
    freshness: kpis.freshness,
    duplicate_rate: kpis.duplicate_rate,
  };

  const coverage = exec?.coverage || [];
  const feed = exec?.knowledge_feed || [];
  const timeline = exec?.timeline || (dashboard.sessions || []).slice(0, 16).map((s) => ({
    session_id: s.session_id,
    mission: s.mission || "—",
    status: s.status || "unknown",
    start_time: s.start_time || "",
    end_time: s.end_time || "",
    knowledge_added: s.knowledge_added || 0,
    knowledge_rejected: s.knowledge_rejected || 0,
    trigger: s.trigger || "",
    events: s.events || 0,
  }));
  const stages = exec?.pipeline_stages || [];
  const hb = exec?.heartbeat;

  const elapsedLabel = (() => {
    const sec = exec?.elapsed_seconds;
    if (sec == null) return "—";
    if (sec < 60) return `${sec}s`;
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m}m ${s}s`;
  })();

  return (
    <div className="relative mx-auto max-w-7xl space-y-6 pb-4">
      {/* Toasts — real events only */}
      <div className="pointer-events-none fixed right-4 top-16 z-50 flex w-80 flex-col gap-2">
        {toasts.map((t) => (
          <div
            key={t.id}
            className={cn(
              "pointer-events-auto rounded-xl border px-3 py-2 text-sm shadow-lg backdrop-blur",
              t.tone === "ok" &&
                "border-emerald-500/30 bg-emerald-500/10 text-emerald-800 dark:text-emerald-200",
              t.tone === "warn" &&
                "border-amber-500/30 bg-amber-500/10 text-amber-900 dark:text-amber-200",
              t.tone === "err" &&
                "border-red-500/30 bg-red-500/10 text-red-800 dark:text-red-200"
            )}
          >
            {t.text}
          </div>
        ))}
      </div>

      {/* Header + Heartbeat */}
      <header className="flex flex-wrap items-start justify-between gap-4">
        <div className="space-y-2">
          <p className="text-xs font-medium uppercase tracking-[0.18em] text-[var(--text-faint)]">
            IDA Dataset Factory · Executive
          </p>
          <h1 className="text-3xl font-semibold tracking-tight text-[var(--text)]">
            Living Knowledge Factory
          </h1>
          <p className="max-w-2xl text-sm text-[var(--text-muted)]">
            {loading
              ? "Loading factory status…"
              : exec?.heartbeat.last_event ||
                kpis.current_activity ||
                activity.current_task ||
                "Ready"}
          </p>
        </div>
        <div
          className={cn(
            "flex min-w-[220px] flex-col gap-1 rounded-2xl border border-[var(--border)] bg-[var(--panel)] px-4 py-3",
            pulse && "ring-2 ring-emerald-400/50"
          )}
        >
          <div className="flex items-center gap-2 text-sm font-semibold">
            <span
              className={cn(
                "inline-block h-2.5 w-2.5 rounded-full",
                status === "RUNNING" || pulse
                  ? "animate-pulse bg-emerald-500"
                  : status === "ERROR"
                    ? "bg-red-500"
                    : "bg-zinc-400"
              )}
            />
            {status === "ERROR" ? "ERROR" : hb?.online ? "ONLINE" : "OFFLINE"}
          </div>
          <p className="text-[11px] text-[var(--text-faint)]">
            Health {hb?.factory_health ?? kpis.dataset_readiness}
            {hb?.production_readiness != null
              ? ` · Readiness ${hb.production_readiness}`
              : ""}
          </p>
          <p className="truncate text-[11px] text-[var(--text-muted)]">
            Last · {hb?.last_session || "—"}
          </p>
        </div>
      </header>

      {/* PANEL 1 — Factory Status */}
      <Card>
        <CardHeader
          title="Factory status"
          description="Live runtime · sessions · scheduled production"
          action={
            <Button size="sm" disabled={busy || status === "RUNNING"} onClick={onStart}>
              {busy ? "Starting…" : "Start factory learn"}
            </Button>
          }
        />
        <CardBody className="grid gap-3 p-6 sm:grid-cols-2 lg:grid-cols-4">
          <Stat
            label="Factory status"
            value={status}
            className={statusTone(status)}
          />
          <Stat label="Current mission" value={String(exec?.current_mission || kpis.current_mission).slice(0, 42)} />
          <Stat label="Current dataset" value={exec?.current_dataset || "—"} />
          <Stat label="Current stage" value={exec?.current_stage_label || liveStage} />
          <Stat label="Current source" value={exec?.current_source || activity.current_source || "—"} />
          <Stat
            label="Current workflow"
            value={
              gaRunning
                ? "Learn (GitHub Actions)"
                : exec?.current_workflow || "github_actions"
            }
          />
          <Stat label="Current batch" value={exec?.current_batch || "—"} />
          <Stat label="Elapsed" value={elapsedLabel} />
          <Stat
            label="Estimated completion"
            value={exec?.estimated_completion || kpis.capacity?.estimated_completion || "—"}
          />
          <Stat
            label="Next scheduled"
            value={formatWib(
              exec?.next_scheduled_run || dashboard.next_scheduled_run || null
            )}
          />
          <div className="sm:col-span-2">
            <Stat
              label="Next mission (selector)"
              value={String(exec?.next_scheduled_mission || "—").slice(0, 80)}
            />
          </div>
        </CardBody>
        {msg ? (
          <p className="px-6 pb-4 text-xs text-[var(--text-faint)]">{msg}</p>
        ) : null}
      </Card>

      {/* PANEL 2 — Live counters */}
      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <CounterCard label="Rows today" value={counters.rows_today} prefix="+" tone="green" />
        <CounterCard label="Rows rejected today" value={counters.rows_rejected_today} tone="neutral" />
        <CounterCard label="Sessions today" value={counters.sessions_today} tone="blue" />
        <CounterCard label="Docs/sessions today" value={counters.documents_processed_today} tone="blue" />
        <CounterCard label="Rows this week" value={counters.rows_week} prefix="+" tone="green" />
        <CounterCard label="Rows this month" value={counters.rows_month} prefix="+" tone="green" />
        <MetricSimple
          label="Avg confidence"
          value={
            counters.average_confidence != null
              ? `${Math.round(counters.average_confidence * 100)}%`
              : "—"
          }
        />
        <MetricSimple
          label="Freshness / Dup"
          value={`${counters.freshness}% · ${Math.round((counters.duplicate_rate || 0) * 1000) / 10}%`}
        />
      </div>

      {/* PANEL 3 — Dataset coverage */}
      <Card>
        <CardHeader
          title="Dataset coverage"
          description="Product targets · readiness (real row counts)"
        />
        <CardBody className="grid gap-3 p-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          {coverage.map((d) => (
            <Link
              key={d.key}
              href={d.href}
              className="rounded-xl border border-[var(--border)] bg-[var(--panel-2)] p-3 transition hover:border-emerald-500/40"
            >
              <div className="flex items-center justify-between gap-2">
                <p className="text-sm font-medium text-[var(--text)]">{d.label}</p>
                <span className="text-xs text-emerald-600 dark:text-emerald-300">
                  R{d.readiness}
                </span>
              </div>
              <p className="mt-1 font-mono text-xs text-[var(--text-muted)]">
                {d.current} / {d.target}
              </p>
              <div className="mt-2">
                <Progress value={d.coverage_pct} />
              </div>
              <p className="mt-1 text-[11px] text-[var(--text-faint)]">{d.coverage_pct}%</p>
            </Link>
          ))}
          {!coverage.length ? (
            <p className="text-sm text-[var(--text-faint)]">Loading coverage…</p>
          ) : null}
        </CardBody>
      </Card>

      <div className="grid gap-4 lg:grid-cols-2">
        {/* PANEL 4 — Pipeline */}
        <Card>
          <CardHeader title="Factory pipeline" description="Active stage from session events" />
          <CardBody className="space-y-1.5 p-6">
            {(stages.length
              ? stages
              : [
                  { id: "mission", label: "Mission" },
                  { id: "discovery", label: "Discovery" },
                  { id: "collection", label: "Collection" },
                  { id: "extraction", label: "Extraction" },
                  { id: "normalization", label: "Normalization" },
                  { id: "validation", label: "Validation" },
                  { id: "append", label: "Append" },
                  { id: "quality", label: "Quality" },
                  { id: "export", label: "Export" },
                  { id: "completed", label: "Completed" },
                ]
            ).map((s, i, arr) => {
              const active = s.id === liveStage;
              return (
                <div key={s.id}>
                  <div
                    className={cn(
                      "flex items-center gap-2 rounded-lg px-3 py-2 text-sm",
                      active
                        ? "bg-emerald-500/15 font-semibold text-emerald-700 dark:text-emerald-300"
                        : "text-[var(--text-muted)]"
                    )}
                  >
                    <span
                      className={cn(
                        "h-2 w-2 rounded-full",
                        active ? "bg-emerald-500" : "bg-zinc-500/40"
                      )}
                    />
                    {s.label}
                  </div>
                  {i < arr.length - 1 ? (
                    <div className="ml-4 h-2 w-px bg-[var(--border)]" />
                  ) : null}
                </div>
              );
            })}
          </CardBody>
        </Card>

        {/* PANEL 5 — Knowledge feed */}
        <Card>
          <CardHeader title="Live knowledge feed" description="Verified session deltas (newest first)" />
          <CardBody className="max-h-96 space-y-2 overflow-y-auto p-6 scrollbar-thin">
            {feed.length === 0 ? (
              <p className="text-sm text-[var(--text-faint)]">
                No knowledge deltas in recent sessions yet.
              </p>
            ) : (
              feed.map((f) => (
                <Link
                  key={f.id}
                  href={f.href}
                  className="flex items-center justify-between gap-2 rounded-xl bg-[var(--panel-2)] px-3 py-2 text-sm hover:bg-emerald-500/10"
                >
                  <span className="font-medium text-emerald-700 dark:text-emerald-300">
                    {f.label}
                  </span>
                  <span className="truncate font-mono text-[10px] text-[var(--text-faint)]">
                    {formatWib(f.ts)}
                  </span>
                </Link>
              ))
            )}
          </CardBody>
        </Card>
      </div>

      {/* PANEL 6 detail already in header heartbeat; expand */}
      <Card>
        <CardHeader title="Factory heartbeat" description="Pulses only on real production events" />
        <CardBody className="grid gap-3 p-6 sm:grid-cols-2 lg:grid-cols-4">
          <Mini label="Last event" value={hb?.last_event || "—"} />
          <Mini label="Last event time" value={formatWib(hb?.last_event_ts)} />
          <Mini label="Last session" value={hb?.last_session || "—"} />
          <Mini label="Last workflow" value={hb?.last_workflow || "—"} />
          <Mini label="Last commit hint" value={hb?.last_commit || "—"} />
          <Mini label="Rows today" value={String(hb?.rows_today ?? counters.rows_today)} />
          <Mini label="Factory health" value={String(hb?.factory_health ?? kpis.dataset_readiness)} />
          <Mini
            label="Production readiness"
            value={
              hb?.production_readiness != null ? String(hb.production_readiness) : "—"
            }
          />
          {hb?.idle_message ? (
            <p className="sm:col-span-2 lg:col-span-4 text-xs text-[var(--text-faint)]">
              {hb.idle_message}
            </p>
          ) : null}
        </CardBody>
      </Card>

      {/* PANEL 7 — Mission timeline */}
      <Card>
        <CardHeader title="Mission timeline" description="One card per production session" />
        <CardBody className="grid gap-2 p-6 sm:grid-cols-2 lg:grid-cols-3">
          {timeline.map((s) => {
            const bucket = sessionStatusBucket(s.status);
            return (
              <button
                key={s.session_id}
                type="button"
                onClick={() => selectSession(s.session_id)}
                className="rounded-xl border border-[var(--border)] bg-[var(--panel-2)] p-3 text-left hover:border-emerald-500/40"
              >
                <div className="flex items-center justify-between gap-2">
                  <span
                    className={cn(
                      "rounded-full px-2 py-0.5 text-[10px] font-semibold uppercase",
                      bucket === "completed" && "bg-emerald-500/15 text-emerald-700 dark:text-emerald-300",
                      bucket === "running" && "bg-sky-500/15 text-sky-700 dark:text-sky-300",
                      bucket === "failed" && "bg-red-500/15 text-red-700 dark:text-red-300",
                      bucket === "queued" && "bg-amber-500/15 text-amber-800 dark:text-amber-300",
                      bucket === "skipped" && "bg-zinc-500/15 text-zinc-600"
                    )}
                  >
                    {bucket}
                  </span>
                  <span className="font-mono text-[10px] text-[var(--text-faint)]">
                    +{s.knowledge_added}
                  </span>
                </div>
                <p className="mt-2 line-clamp-2 text-xs font-medium text-[var(--text)]">
                  {s.mission}
                </p>
                <p className="mt-1 font-mono text-[10px] text-[var(--text-faint)]">
                  {s.session_id}
                </p>
              </button>
            );
          })}
          {!timeline.length ? (
            <p className="text-sm text-[var(--text-faint)]">No sessions recorded yet.</p>
          ) : null}
        </CardBody>
      </Card>

      {/* PANEL 8 — Production replay */}
      <Card>
        <CardHeader
          title="Production replay"
          description="Replays recorded session events only — never simulated"
          action={
            <Button
              size="sm"
              variant="secondary"
              onClick={() => void onReplayLatest()}
              disabled={replayPlaying}
            >
              {replayPlaying ? "Replaying…" : "Replay latest session"}
            </Button>
          }
        />
        <CardBody className="max-h-72 space-y-1 overflow-y-auto p-6 font-mono text-[11px] scrollbar-thin">
          {!replayEvents.length ? (
            <p className="font-sans text-sm text-[var(--text-faint)]">
              Select a session from the timeline or start replay to load real events.
            </p>
          ) : (
            replayEvents.map((ev, i) => (
              <div
                key={i}
                className={cn(
                  "flex gap-2 border-b border-[var(--border)]/50 py-1 text-[var(--text-muted)]",
                  replayPlaying && i === replayIdx && "bg-emerald-500/10 text-[var(--text)]",
                  replayPlaying && i > replayIdx && "opacity-30"
                )}
              >
                <span className="w-24 shrink-0 text-[var(--text-faint)]">
                  {formatWibTime(ev.ts)}
                </span>
                <span className="w-28 shrink-0 font-medium text-emerald-600 dark:text-emerald-300">
                  {ev.verb}
                </span>
                <span className="min-w-0 truncate">{ev.detail}</span>
              </div>
            ))
          )}
        </CardBody>
      </Card>
    </div>
  );
}

function Stat({
  label,
  value,
  className,
}: {
  label: string;
  value: string;
  className?: string;
}) {
  return (
    <div className={cn("rounded-xl bg-[var(--panel-2)] px-3 py-2", className)}>
      <p className="text-[10px] uppercase tracking-wider text-[var(--text-faint)]">
        {label}
      </p>
      <p className="mt-0.5 truncate text-sm font-semibold text-[var(--text)]">{value}</p>
    </div>
  );
}

function Mini({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl bg-[var(--panel-2)] px-3 py-2">
      <p className="text-[10px] uppercase tracking-wider text-[var(--text-faint)]">
        {label}
      </p>
      <p className="mt-0.5 truncate text-xs font-medium text-[var(--text)]" title={value}>
        {value}
      </p>
    </div>
  );
}

function CounterCard({
  label,
  value,
  prefix = "",
  tone = "neutral",
}: {
  label: string;
  value: number;
  prefix?: string;
  tone?: "green" | "blue" | "neutral";
}) {
  return (
    <div className="rounded-2xl border border-[var(--border)] bg-[var(--panel)] px-4 py-4">
      <p className="text-[10px] uppercase tracking-wider text-[var(--text-faint)]">
        {label}
      </p>
      <p
        className={cn(
          "mt-1 text-2xl font-semibold tabular-nums",
          tone === "green" && "text-emerald-600 dark:text-emerald-300",
          tone === "blue" && "text-sky-600 dark:text-sky-300",
          tone === "neutral" && "text-[var(--text)]"
        )}
      >
        <LiveNumber value={value} prefix={prefix} />
      </p>
    </div>
  );
}

function MetricSimple({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-2xl border border-[var(--border)] bg-[var(--panel)] px-4 py-4">
      <p className="text-[10px] uppercase tracking-wider text-[var(--text-faint)]">
        {label}
      </p>
      <p className="mt-1 text-2xl font-semibold text-[var(--text)]">{value}</p>
    </div>
  );
}
