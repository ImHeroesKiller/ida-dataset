"use client";

import Link from "next/link";
import {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
  type ReactNode,
} from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { useLearning } from "@/hooks/learning-provider";
import { cn } from "@/lib/utils";
import type { FactoryKpis } from "@/lib/factory-kpis";
import type { ExecutiveFactoryView, PipelineStageId } from "@/lib/executive-factory";
import { formatWib } from "@/lib/time-wib";

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
      {n.toLocaleString()}
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

/** Operator-facing stage labels (wireframe language). */
function stageLabel(stage: string | PipelineStageId | undefined): string {
  const s = String(stage || "").toLowerCase();
  if (!s || s === "—" || s === "mission") return "Ready";
  if (s.includes("extract")) return "Extracting Knowledge";
  if (s.includes("discover") || s.includes("search")) return "Discovering Sources";
  if (s.includes("collect") || s.includes("download") || s.includes("reading"))
    return "Collecting Documents";
  if (s.includes("normal")) return "Normalizing";
  if (s.includes("valid")) return "Validating";
  if (s.includes("append") || s.includes("publish")) return "Publishing Knowledge";
  if (s.includes("quality")) return "Quality Check";
  if (s.includes("export")) return "Exporting";
  if (s.includes("complete")) return "Completed";
  return String(stage).replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
}

function formatCountdown(targetIso: string | null | undefined, nowMs: number): string {
  if (!targetIso) return "—";
  const t = new Date(targetIso).getTime();
  if (!Number.isFinite(t)) return "—";
  const diff = Math.max(0, Math.floor((t - nowMs) / 1000));
  if (diff < 60) return `${diff}s`;
  const m = Math.floor(diff / 60);
  if (m < 60) return `${m} min`;
  const h = Math.floor(m / 60);
  const rm = m % 60;
  return rm ? `${h}h ${rm}m` : `${h}h`;
}

function missionShort(raw: string): string {
  const s = (raw || "").trim();
  if (!s) return "—";
  // Prefer human title after em dash / colon
  const cut = s.split(/\s+[—–-]\s+|:\s+/).pop() || s;
  return cut.length > 48 ? `${cut.slice(0, 46)}…` : cut;
}

export function FactoryDashboard({ kpis: initialKpis }: { kpis: FactoryKpis }) {
  const { dashboard, activity, events, startLearning, loading } = useLearning();
  const [kpis, setKpis] = useState(initialKpis);
  const [exec, setExec] = useState<ExecutiveFactoryView | null>(null);
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);
  const [toasts, setToasts] = useState<Toast[]>([]);
  const [pulse, setPulse] = useState(false);
  const [nowMs, setNowMs] = useState(() => Date.now());
  const [hfStatus, setHfStatus] = useState<"Synced" | "Running" | "Idle" | "Unknown">(
    "Unknown"
  );
  const prevSnap = useRef<{ rows: number; mission: string; status: string } | null>(
    null
  );

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
      if (data.ok && data.sync) {
        const hf = String(data.sync.huggingface || "").toLowerCase();
        if (hf.includes("sync") || hf === "ok" || hf === "pass") setHfStatus("Synced");
        else if (hf.includes("run")) setHfStatus("Running");
        else if (hf.includes("idle") || hf.includes("skip")) setHfStatus("Idle");
        else setHfStatus("Unknown");
      }
    } catch {
      /* ignore */
    }
  }, []);

  useEffect(() => {
    void refresh();
    const id = setInterval(() => void refresh(), 30_000);
    return () => clearInterval(id);
  }, [refresh]);

  useEffect(() => {
    const id = setInterval(() => setNowMs(Date.now()), 1000);
    return () => clearInterval(id);
  }, []);

  const gaRunning = Boolean(dashboard.github_actions?.running);
  const gaQueued = Boolean(dashboard.github_actions?.queued);
  const gaFailed = dashboard.github_actions?.status === "failed";

  const learningStatus: "Running" | "Waiting" | "Error" | "Idle" = useMemo(() => {
    if (exec?.status === "ERROR" || kpis.factory_status === "error" || gaFailed)
      return "Error";
    if (gaRunning || kpis.factory_status === "running" || exec?.status === "RUNNING")
      return "Running";
    if (gaQueued) return "Waiting";
    return "Idle";
  }, [exec?.status, kpis.factory_status, gaRunning, gaQueued, gaFailed]);

  const liveStage: PipelineStageId = useMemo(() => {
    if (events.length) {
      const last = events[events.length - 1];
      return mapEventStage(last.verb, last.stage, last.current_task || undefined);
    }
    return exec?.current_stage || "mission";
  }, [events, exec?.current_stage]);

  const currentStageLabel = stageLabel(
    productionStageLabel(exec, activity, liveStage)
  );

  const mission = missionShort(
    String(exec?.current_mission || dashboard.current_mission || kpis.current_mission || "—")
  );

  const counters = exec?.counters;
  const production = exec?.production;
  const rowsToday = counters?.rows_today ?? kpis.rows_added_today ?? 0;
  const knowledgeAdded =
    Number(dashboard.history?.today?.knowledge_added ?? dashboard.knowledge_added ?? 0) ||
    Number(dashboard.history?.knowledge_growth?.added ?? 0) ||
    rowsToday;
  const datasetCount = kpis.datasets?.length || exec?.coverage?.length || 0;
  const queueDepth =
    (production?.documents_queued ?? counters?.documents_queued ?? 0) +
    (production?.candidates_queued ?? counters?.candidates_queued ?? 0) +
    (production?.publish_queue ?? counters?.publish_queue_size ?? 0);

  const nextProductionIso =
    exec?.next_scheduled_run ||
    dashboard.next_scheduled_run ||
    dashboard.github_actions?.next_scheduled_hint ||
    null;
  const nextRunLabel = formatCountdown(nextProductionIso, nowMs);

  // Real-event toasts
  useEffect(() => {
    const prev = prevSnap.current;
    if (!prev) {
      prevSnap.current = { rows: rowsToday, mission, status: learningStatus };
      return;
    }
    if (rowsToday > prev.rows) {
      pushToast(`Rows today ${rowsToday.toLocaleString()} (+${rowsToday - prev.rows})`, "ok");
      setPulse(true);
      setTimeout(() => setPulse(false), 900);
    }
    if (mission !== prev.mission && learningStatus === "Running") {
      pushToast(`Mission · ${mission}`, "ok");
    }
    if (prev.status === "Running" && learningStatus === "Idle") {
      pushToast("Learning completed", "ok");
    }
    if (learningStatus === "Error" && prev.status !== "Error") {
      pushToast("Learning failed", "err");
    }
    prevSnap.current = { rows: rowsToday, mission, status: learningStatus };
  }, [rowsToday, mission, learningStatus, pushToast]);

  async function onStart() {
    setBusy(true);
    setMsg(null);
    try {
      const res = await startLearning(undefined, true);
      setMsg(res.ok ? res.message || "Learning started" : res.reason || "Failed");
      if (res.ok) pushToast("Learning started", "ok");
      else pushToast(res.reason || "Unable to start", "err");
      await refresh();
    } finally {
      setBusy(false);
    }
  }

  // Knowledge growth series — last 14 sessions (real knowledge_added)
  const growthSeries = useMemo(() => {
    const sessions = (dashboard.sessions || []).slice(0, 14).reverse();
    if (!sessions.length && exec?.timeline?.length) {
      return exec.timeline
        .slice(0, 14)
        .reverse()
        .map((s) => ({
          label: (s.session_id || "").slice(-6) || "·",
          value: Number(s.knowledge_added || 0),
        }));
    }
    return sessions.map((s) => ({
      label: (s.session_id || "").replace(/^SESSION-/, "").slice(-8) || "·",
      value: Number(s.knowledge_added || 0),
    }));
  }, [dashboard.sessions, exec?.timeline]);

  // Dataset distribution — real coverage rows
  const distribution = useMemo(() => {
    if (exec?.coverage?.length) {
      return exec.coverage
        .map((d) => ({
          label: d.label,
          value: Number(d.current || 0),
          href: d.href || "/exports",
        }))
        .sort((a, b) => b.value - a.value);
    }
    return (kpis.datasets || [])
      .map((d) => ({
        label: d.name.replace(/_library$|_profile$|_catalog$|_analysis$/, ""),
        value: Number(d.current_rows || 0),
        href: "/exports",
      }))
      .sort((a, b) => b.value - a.value);
  }, [exec?.coverage, kpis.datasets]);

  const githubLabel = gaRunning
    ? "Running"
    : gaQueued
      ? "Waiting"
      : gaFailed
        ? "Error"
        : "Synced";

  const exportStatus =
    liveStage === "export" || /export/i.test(currentStageLabel)
      ? "Exporting"
      : learningStatus === "Running" && /publish/i.test(currentStageLabel)
        ? "Publishing"
        : kpis.exports_generated > 0
          ? "Synced"
          : "Idle";

  return (
    <div className="op-page relative pb-4">
      {/* Toasts */}
      <div className="pointer-events-none fixed right-3 top-12 z-50 flex w-72 flex-col gap-1.5">
        {toasts.map((t) => (
          <div
            key={t.id}
            className={cn(
              "pointer-events-auto rounded-[var(--radius-md)] border px-2.5 py-1.5 text-xs shadow-md backdrop-blur",
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

      {/* Title */}
      <header className="op-page-header">
        <div>
          <p className="text-[10px] font-semibold uppercase tracking-[0.12em] text-[var(--text-muted)]">
            IDA Dataset Factory
          </p>
          <h1 className="text-page-title">Dashboard</h1>
          <p>
            {loading
              ? "Loading…"
              : exec?.heartbeat?.last_event ||
                kpis.current_activity ||
                activity.current_task ||
                "Continuous knowledge manufacturing"}
          </p>
        </div>
        <Button
          size="sm"
          disabled={busy || learningStatus === "Running"}
          onClick={() => void onStart()}
        >
          {busy ? "Starting…" : "Start Learning"}
        </Button>
      </header>

      {/* Top status strip — wireframe metrics only */}
      <Card className={cn(pulse && "ring-1 ring-[var(--green)]/40")}>
        <CardBody className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
          <Metric
            label="Learning"
            value={learningStatus}
            leading={
              <span
                className={cn(
                  "inline-block h-2 w-2 rounded-full",
                  learningStatus === "Running" && "animate-pulse bg-[var(--green)]",
                  learningStatus === "Waiting" && "animate-pulse bg-amber-500",
                  learningStatus === "Error" && "bg-[var(--red)]",
                  learningStatus === "Idle" && "bg-[var(--text-muted)]"
                )}
              />
            }
            tone={
              learningStatus === "Running"
                ? "run"
                : learningStatus === "Error"
                  ? "err"
                  : learningStatus === "Waiting"
                    ? "warn"
                    : "idle"
            }
            kpi
          />
          <Metric label="Mission" value={mission} />
          <Metric label="Current Stage" value={currentStageLabel} />
          <Metric
            label="Rows Today"
            valueNode={<LiveNumber value={rowsToday} className="tabular-nums" />}
            kpi
          />
          <Metric
            label="Datasets"
            valueNode={<LiveNumber value={datasetCount} className="tabular-nums" />}
            kpi
          />
          <Metric
            label="Knowledge Added"
            valueNode={
              <LiveNumber
                value={knowledgeAdded}
                prefix="+"
                className="tabular-nums text-emerald-600 dark:text-emerald-300"
              />
            }
            kpi
          />
          <Metric
            label="Queue"
            valueNode={<LiveNumber value={queueDepth} className="tabular-nums" />}
            kpi
          />
          <Metric
            label="Next Run"
            value={nextRunLabel}
            hint={nextProductionIso ? formatWib(nextProductionIso) : undefined}
          />
        </CardBody>
        {msg ? (
          <p className="border-t border-[var(--border)] px-3 py-1.5 text-[11px] text-[var(--text-muted)]">
            {msg}
          </p>
        ) : null}
      </Card>

      {/* Graphs */}
      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader
            title="Knowledge Growth"
            description="Per recent learning session"
          />
          <CardBody>
            <BarChart
              series={growthSeries}
              empty="No session growth yet."
              color="emerald"
            />
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Dataset Distribution"
            description="Rows across datasets"
          />
          <CardBody>
            <HBarChart
              series={distribution}
              empty="No dataset rows yet."
            />
          </CardBody>
        </Card>
      </div>

      {/* Sync strip */}
      <div className="grid gap-2 sm:grid-cols-3">
        <SyncCard
          title="GitHub"
          status={githubLabel}
          detail={
            dashboard.github_actions?.repository ||
            (dashboard.github_actions?.configured ? "Actions learn.yml" : "Local / not configured")
          }
          href={dashboard.github_actions?.current_run?.html_url}
        />
        <SyncCard
          title="Hugging Face"
          status={hfStatus === "Unknown" ? (kpis.exports_generated > 0 ? "Synced" : "Idle") : hfStatus}
          detail="Dataset publish channel"
          href="https://huggingface.co/datasets/ariew/ida-dataset"
        />
        <SyncCard
          title="Export"
          status={exportStatus}
          detail={`${kpis.exports_generated} artifacts`}
          href="/exports"
        />
      </div>

      {/* Console lives in shell bottom bar — pointer for operators */}
      <p className="text-center text-caption text-[var(--text-muted)]">
        Live console · acquisition · GitHub · Hugging Face · export — bottom panel
      </p>
    </div>
  );
}

function productionStageLabel(
  exec: ExecutiveFactoryView | null,
  activity: { current_task?: string | null },
  liveStage: PipelineStageId
): string {
  return (
    exec?.production?.current_stage ||
    exec?.current_stage_label ||
    activity.current_task ||
    liveStage
  );
}

function Metric({
  label,
  value,
  valueNode,
  leading,
  tone,
  hint,
  kpi,
}: {
  label: string;
  value?: string;
  valueNode?: ReactNode;
  leading?: ReactNode;
  tone?: "run" | "err" | "warn" | "idle";
  hint?: string;
  kpi?: boolean;
}) {
  return (
    <div className="min-w-0">
      <p className="text-[10px] font-semibold uppercase tracking-wide text-[var(--text-muted)]">
        {label}
      </p>
      <div
        className={cn(
          "mt-0.5 flex items-center gap-1.5 font-semibold tracking-tight text-[var(--text)]",
          kpi ? "text-kpi" : "text-sm",
          tone === "run" && "text-emerald-600 dark:text-emerald-300",
          tone === "err" && "text-red-600 dark:text-red-300",
          tone === "warn" && "text-amber-700 dark:text-amber-300"
        )}
        title={hint}
      >
        {leading}
        <span className="min-w-0 truncate">{valueNode ?? value ?? "—"}</span>
      </div>
    </div>
  );
}

function SyncCard({
  title,
  status,
  detail,
  href,
}: {
  title: string;
  status: string;
  detail: string;
  href?: string | null;
}) {
  const ok = /sync|ok|pass|idle|healthy/i.test(status) && !/fail|error|offline/i.test(status);
  const run = /run|wait|export|publish/i.test(status);
  const bad = /fail|error|offline/i.test(status);
  const body = (
    <div className="rounded-[var(--radius-lg)] border border-[var(--border)] bg-[var(--panel)] px-3 py-2.5 shadow-[var(--shadow)] transition hover:border-[var(--border-strong)]">
      <div className="flex items-center justify-between gap-2">
        <p className="text-xs font-semibold text-[var(--text)]">{title}</p>
        <span
          className={cn(
            "inline-flex items-center gap-1 text-xs font-semibold",
            ok && "text-emerald-600 dark:text-emerald-300",
            run && "text-sky-600 dark:text-sky-300",
            bad && "text-red-600 dark:text-red-300",
            !ok && !run && !bad && "text-[var(--text-secondary)]"
          )}
        >
          {ok ? "✔" : run ? "●" : bad ? "✕" : "·"} {status}
        </span>
      </div>
      <p className="mt-0.5 truncate text-[10px] text-[var(--text-muted)]">{detail}</p>
    </div>
  );
  if (href) {
    return (
      <Link href={href} target={href.startsWith("http") ? "_blank" : undefined} rel="noreferrer">
        {body}
      </Link>
    );
  }
  return body;
}

function BarChart({
  series,
  empty,
  color = "emerald",
}: {
  series: Array<{ label: string; value: number }>;
  empty: string;
  color?: "emerald" | "sky";
}) {
  if (!series.length) {
    return <p className="py-8 text-center text-xs text-[var(--text-muted)]">{empty}</p>;
  }
  const max = Math.max(1, ...series.map((s) => s.value));
  return (
    <div className="flex h-36 items-end gap-1 sm:gap-1.5">
      {series.map((s, i) => {
        const h = Math.max(4, Math.round((s.value / max) * 100));
        return (
          <div key={`${s.label}-${i}`} className="flex min-w-0 flex-1 flex-col items-center gap-0.5">
            <span className="text-[9px] tabular-nums text-[var(--text-muted)]">
              {s.value > 0 ? s.value : ""}
            </span>
            <div
              className={cn(
                "w-full max-w-[24px] rounded-t transition-all",
                color === "emerald" && "bg-emerald-500/80 dark:bg-emerald-400/70",
                color === "sky" && "bg-sky-500/80 dark:bg-sky-400/70",
                s.value === 0 && "bg-[var(--panel-2)]"
              )}
              style={{ height: `${h}%` }}
              title={`${s.label}: ${s.value}`}
            />
            <span className="w-full truncate text-center text-[8px] text-[var(--text-faint)]">
              {s.label.slice(-4)}
            </span>
          </div>
        );
      })}
    </div>
  );
}

function HBarChart({
  series,
  empty,
}: {
  series: Array<{ label: string; value: number; href?: string }>;
  empty: string;
}) {
  if (!series.length) {
    return <p className="py-8 text-center text-xs text-[var(--text-muted)]">{empty}</p>;
  }
  const max = Math.max(1, ...series.map((s) => s.value));
  const top = series.slice(0, 12);
  return (
    <div className="max-h-44 space-y-1.5 overflow-y-auto scrollbar-thin">
      {top.map((s) => {
        const pct = Math.round((s.value / max) * 100);
        const row = (
          <div className="grid grid-cols-[6.5rem_1fr_2.75rem] items-center gap-1.5 text-xs">
            <span className="truncate text-[var(--text-secondary)]" title={s.label}>
              {s.label}
            </span>
            <div className="h-1.5 overflow-hidden rounded-full bg-[var(--panel-2)]">
              <div
                className="h-full rounded-full bg-sky-500/80 dark:bg-sky-400/70"
                style={{ width: `${pct}%` }}
              />
            </div>
            <span className="text-right tabular-nums font-medium text-[var(--text)]">
              {s.value.toLocaleString()}
            </span>
          </div>
        );
        return s.href ? (
          <Link key={s.label} href={s.href} className="block hover:opacity-90">
            {row}
          </Link>
        ) : (
          <div key={s.label}>{row}</div>
        );
      })}
    </div>
  );
}
