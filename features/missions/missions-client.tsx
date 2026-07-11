"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Progress } from "@/components/ui/progress";
import { useInspector } from "@/components/layout/inspector-context";
import { useLearning } from "@/hooks/learning-provider";
import { cn } from "@/lib/utils";
import { formatWib } from "@/lib/time-wib";
import { safeFetchJson } from "@/lib/safe-fetch";

type Row = Record<string, unknown>;

type ReportCard = {
  name: string;
  relativePath: string;
  mtime: string;
  size: number;
  batch?: string;
  mission?: string;
  rows_added?: number | null;
  coverage_increase?: string | null;
  confidence?: number | null;
  generated?: string;
};

type Toast = { id: string; text: string; tone: "ok" | "err" | "warn" };

type SessionSummary = {
  session_id: string;
  mission?: string;
  status?: string;
  start_time?: string | null;
  end_time?: string | null;
  duration_seconds?: number | null;
  knowledge_added?: number;
  knowledge_updated?: number;
  knowledge_rejected?: number;
  summary?: string;
  trigger?: string;
  events?: number;
  knowledge_delta?: Record<string, unknown> | null;
  production_trace?: Record<string, unknown> | null;
  publish_summary?: Record<string, unknown> | null;
};

function mapStatus(
  raw: string
): "queued" | "running" | "completed" | "failed" | "cancelled" | "superseded" {
  const s = raw.toLowerCase();
  if (s.includes("supersed")) return "superseded";
  if (s.includes("cancel")) return "cancelled";
  if (s.includes("fail") || s.includes("error")) return "failed";
  if (s.includes("run") || s.includes("progress") || s.includes("active"))
    return "running";
  if (s.includes("complete") || s.includes("done") || s.includes("success"))
    return "completed";
  if (s.includes("queue") || s.includes("pending") || s.includes("draft"))
    return "queued";
  return "queued";
}

const statusStyle: Record<string, string> = {
  queued: "bg-[var(--badge-warning-bg)] text-[var(--badge-warning-fg)]",
  running: "bg-[var(--badge-running-bg)] text-[var(--badge-running-fg)]",
  completed: "bg-[var(--badge-completed-bg)] text-[var(--badge-completed-fg)]",
  failed: "bg-[var(--badge-error-bg)] text-[var(--badge-error-fg)]",
  cancelled: "bg-[var(--badge-idle-bg)] text-[var(--badge-idle-fg)]",
  superseded: "bg-[var(--badge-publishing-bg)] text-[var(--badge-publishing-fg)]",
};

const SUGGESTED_MISSIONS = [
  "Produce Buyer Persona Dataset for banking and manufacturing",
  "Produce Decision Maker patterns for enterprise Indonesia",
  "Produce Competitor Dataset for manufacturing Indonesia",
  "Produce Regulation Dataset — employment and banking",
  "Produce Risk Dataset — operational and regulatory risk",
  "Produce Trend Dataset — digital economy Indonesia",
  "Produce Industry Dataset — expand industry_library",
  "Market intelligence signals for Indonesian SMEs",
];

const PIPELINE = [
  "Searching",
  "Collecting",
  "Extracting",
  "Validating",
  "Publishing",
  "Completed",
] as const;

function stageFromEvents(
  events: Array<{ verb?: string; stage?: string; detail?: string }>
): string {
  if (!events.length) return "Searching";
  const last = events[events.length - 1];
  const blob = `${last.verb || ""} ${last.stage || ""} ${last.detail || ""}`.toLowerCase();
  if (/complete|finished|done/.test(blob)) return "Completed";
  if (/publish|append|knowledge/.test(blob)) return "Publishing";
  if (/validat|review|policy/.test(blob)) return "Validating";
  if (/extract|pipeline|entity|understand/.test(blob)) return "Extracting";
  if (/download|document|reading|queue|collect/.test(blob)) return "Collecting";
  return "Searching";
}

function friendlyError(input: unknown): string {
  const raw =
    typeof input === "string"
      ? input
      : input instanceof Error
        ? input.message
        : String(input ?? "");
  if (!raw.trim()) return "Unable to dispatch the mission. Please try again.";
  if (/unexpected token|json\.parse|syntaxerror|invalid json|unexpected end of json/i.test(raw)) {
    return "Something went wrong while processing the response. Please try again.";
  }
  if (/scheduler cli unavailable|python/i.test(raw)) {
    return "Mission will be dispatched through GitHub Actions.";
  }
  return raw;
}

async function readJsonSafe(res: Response): Promise<Record<string, unknown>> {
  const text = await res.text();
  if (!text.trim()) return {};
  try {
    return JSON.parse(text) as Record<string, unknown>;
  } catch {
    return {
      ok: false,
      error: "Something went wrong while processing the response. Please try again.",
      _raw_non_json: true,
    };
  }
}

export function MissionsClient({
  missions: initialMissions,
  contracts: _contracts,
  reports: initialReports,
}: {
  missions: Row[];
  contracts: Row[];
  reports: ReportCard[];
}) {
  const { inspect } = useInspector();
  const { dashboard, events, activity, loadSessionEvents } = useLearning();
  const [missions, setMissions] = useState(initialMissions);
  const [reports, setReports] = useState(initialReports);
  const [sessions, setSessions] = useState<SessionSummary[]>([]);
  const [selectedSession, setSelectedSession] = useState<SessionSummary | null>(null);
  const [text, setText] = useState("");
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);
  const [msgTone, setMsgTone] = useState<"ok" | "err">("ok");
  const [toasts, setToasts] = useState<Toast[]>([]);
  const lastToastKey = useRef("");
  const submitting = useRef(false);

  const pushToast = useCallback((text: string, tone: Toast["tone"] = "ok") => {
    const key = `${tone}:${text}`;
    if (lastToastKey.current === key) return;
    lastToastKey.current = key;
    const id = `${Date.now()}-${Math.random().toString(36).slice(2, 6)}`;
    setToasts((t) => [...t.slice(-3), { id, text, tone }]);
    setTimeout(() => {
      setToasts((t) => t.filter((x) => x.id !== id));
      if (lastToastKey.current === key) lastToastKey.current = "";
    }, 4000);
  }, []);

  const refresh = useCallback(async () => {
    const result = await safeFetchJson<Record<string, unknown>>("/api/missions");
    if (!result.parsed || !result.data) return;
    const data = result.data;
    if (Array.isArray(data.missions)) setMissions(data.missions as Row[]);
    if (Array.isArray(data.reports)) setReports(data.reports as ReportCard[]);
    if (Array.isArray(data.sessions)) setSessions(data.sessions as SessionSummary[]);
  }, []);

  useEffect(() => {
    void refresh();
    const id = setInterval(() => void refresh(), 8000);
    return () => clearInterval(id);
  }, [refresh]);

  // Merge session history from learning dashboard when available
  useEffect(() => {
    if (dashboard.sessions?.length) {
      setSessions((prev) => {
        if (prev.length) return prev;
        return dashboard.sessions as SessionSummary[];
      });
    }
  }, [dashboard.sessions]);

  const active = useMemo(() => {
    return missions.filter((m) => {
      const st = mapStatus(String(m.status || ""));
      return st === "queued" || st === "running";
    });
  }, [missions]);

  const history = useMemo(() => {
    const fromMissions = missions.filter((m) => {
      const st = mapStatus(String(m.status || ""));
      return st === "completed" || st === "failed" || st === "cancelled" || st === "superseded";
    });
    return { missions: fromMissions, sessions };
  }, [missions, sessions]);

  const running =
    dashboard.github_actions?.running ||
    active.some((m) => mapStatus(String(m.status)) === "running") ||
    activity.status === "running";

  const currentStage = useMemo(() => {
    if (events.length) return stageFromEvents(events);
    if (running) return "Searching";
    return "—";
  }, [events, running]);

  const progressPct = useMemo(() => {
    if (!running) {
      const a = active[0];
      return Number(a?.progress || 0);
    }
    const idx = PIPELINE.indexOf(currentStage as (typeof PIPELINE)[number]);
    if (idx < 0) return 15;
    return Math.round(((idx + 1) / PIPELINE.length) * 100);
  }, [running, currentStage, active]);

  async function createMission() {
    if (submitting.current || busy) return;
    const instruction = text.trim();
    if (!instruction) {
      setMsg("Please enter a mission instruction.");
      setMsgTone("err");
      return;
    }
    if (instruction.length < 8) {
      setMsg("Please describe the mission in a bit more detail.");
      setMsgTone("err");
      return;
    }

    submitting.current = true;
    setBusy(true);
    setMsg(null);
    try {
      const res = await fetch("/api/missions", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "mission", text: instruction }),
      });
      const data = await readJsonSafe(res);

      if (!res.ok || data.ok === false) {
        const err = friendlyError(
          data.error || data.reason || data.message || "Dispatch failed"
        );
        setMsg(err);
        setMsgTone("err");
        pushToast(err, "err");
        // Still refresh if mission was saved
        if (Array.isArray(data.missions)) setMissions(data.missions as Row[]);
        return;
      }

      setText("");
      const mission = (data.mission || {}) as Row;
      const mid = String(mission.mission_id || "mission");
      const message =
        String(data.message || "") ||
        "Mission queued for autonomous production.";
      // Never show scheduler CLI / JSON parse details
      const clean = friendlyError(message)
        .replace(/scheduler cli.*/i, "Mission queued for autonomous production.")
        .replace(/python.*/i, "Mission will be dispatched through GitHub Actions.");
      setMsg(clean);
      setMsgTone("ok");
      pushToast(
        data.queued !== false
          ? `Mission queued · ${mid}`
          : `Mission started · ${mid}`,
        "ok"
      );
      if (Array.isArray(data.missions)) setMissions(data.missions as Row[]);
      else await refresh();
    } catch (e) {
      const err = friendlyError(e);
      setMsg(err);
      setMsgTone("err");
      pushToast(err, "err");
    } finally {
      busy && setBusy(false);
      setBusy(false);
      submitting.current = false;
    }
  }

  // Notify when GHA run starts/completes (deduped)
  useEffect(() => {
    if (dashboard.github_actions?.running) {
      pushToast("Mission started", "ok");
    }
  }, [dashboard.github_actions?.running, pushToast]);

  return (
    <div className="relative space-y-6">
      {/* Toasts */}
      <div className="pointer-events-none fixed right-4 top-16 z-50 flex w-80 flex-col gap-2">
        {toasts.map((t) => (
          <div
            key={t.id}
            className={cn(
              "pointer-events-auto rounded-xl border px-3 py-2 text-sm shadow-lg",
              t.tone === "ok" &&
                "border-emerald-500/30 bg-emerald-500/10 text-emerald-800 dark:text-emerald-200",
              t.tone === "err" &&
                "border-red-500/30 bg-red-500/10 text-red-800 dark:text-red-200",
              t.tone === "warn" &&
                "border-amber-500/30 bg-amber-500/10 text-amber-900 dark:text-amber-200"
            )}
          >
            {t.text}
          </div>
        ))}
      </div>

      <header className="space-y-2">
        <h1 className="text-page-title">Missions</h1>
        <p className="max-w-2xl text-body text-[var(--text-secondary)]">
          Tell the factory what dataset to grow next. Missions queue into
          autonomous production and never stop continuous learning.
        </p>
      </header>

      {/* Create */}
      <Card>
        <CardHeader
          title="Dispatch mission"
          description="Describe the production goal in plain language"
        />
        <CardBody className="space-y-4">
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
                e.preventDefault();
                void createMission();
              }
            }}
            disabled={busy}
            rows={4}
            placeholder="e.g. Produce buyer personas for banking and manufacturing Indonesia — expand coverage with trusted sources only"
            className="w-full resize-y rounded-[var(--radius-lg)] border border-[var(--border)] bg-[var(--panel)] px-4 py-3 text-body text-[var(--text)] outline-none placeholder:text-[var(--text-muted)] focus:border-[var(--blue)] focus:ring-2 focus:ring-[var(--blue)]/20 disabled:opacity-50"
            aria-label="Mission instruction"
          />
          <div className="flex flex-wrap gap-2">
            {SUGGESTED_MISSIONS.map((s) => (
              <button
                key={s}
                type="button"
                onClick={() => setText(s)}
                className="rounded-full border border-[var(--border)] bg-[var(--panel-2)] px-3 py-1.5 text-caption font-semibold text-[var(--text-secondary)] transition-colors hover:border-[var(--blue)] hover:text-[var(--text)]"
              >
                {s.split("—")[0].replace("Produce ", "").trim().slice(0, 28)}
              </button>
            ))}
          </div>
          <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
            <p className="text-caption text-[var(--text-muted)]">
              ⌘/Ctrl + Enter to dispatch
            </p>
            <Button
              size="lg"
              disabled={busy || !text.trim()}
              onClick={() => void createMission()}
              loading={busy}
            >
              {busy ? "Dispatching…" : "Dispatch mission"}
            </Button>
          </div>
        </CardBody>
        {msg ? (
          <p
            className={cn(
              "px-6 pb-5 text-small font-medium",
              msgTone === "ok"
                ? "text-[var(--green)]"
                : "text-[var(--red)]"
            )}
          >
            {msg}
          </p>
        ) : null}
      </Card>

      {/* Live progress when active */}
      {(running || active.length > 0) && (
        <Card>
          <CardHeader
            title="Mission progress"
            description="Stages follow real production events only"
          />
          <CardBody className="space-y-4 p-6">
            <div className="flex flex-wrap gap-2">
              {PIPELINE.map((s) => (
                <span
                  key={s}
                  className={cn(
                    "rounded-full px-2.5 py-1 text-[11px] font-medium",
                    currentStage === s
                      ? "bg-emerald-500/15 text-emerald-700 dark:text-emerald-300"
                      : "bg-[var(--panel-2)] text-[var(--text-faint)]"
                  )}
                >
                  {s}
                </span>
              ))}
            </div>
            <Progress value={progressPct} />
            <p className="text-xs text-[var(--text-faint)]">
              {running
                ? activity.current_task || activity.current_thought || "Production running…"
                : "Queued — waiting for the autonomous worker"}
            </p>
          </CardBody>
        </Card>
      )}

      {/* Active missions */}
      <Card>
        <CardHeader
          title="Active missions"
          description={`${active.length} active · ${missions.length} total`}
        />
        <CardBody className="overflow-x-auto p-0">
          <table className="w-full min-w-[880px] text-left text-xs">
            <thead className="border-b border-[var(--border)] text-[10px] uppercase tracking-wide text-[var(--text-faint)]">
              <tr>
                <th className="px-4 py-3">Mission</th>
                <th className="px-4 py-3">Dataset</th>
                <th className="px-4 py-3">Priority</th>
                <th className="px-4 py-3">Status</th>
                <th className="px-4 py-3">Progress</th>
                <th className="px-4 py-3">Created</th>
                <th className="px-4 py-3">Last update</th>
              </tr>
            </thead>
            <tbody>
              {missions.length === 0 ? (
                <tr>
                  <td
                    colSpan={7}
                    className="px-4 py-8 text-center text-[var(--text-faint)]"
                  >
                    No missions yet. Dispatch one to start production.
                  </td>
                </tr>
              ) : (
                missions.map((m) => {
                  const st = mapStatus(String(m.status || ""));
                  const dataset = String(
                    (Array.isArray(m.related_datasets) &&
                      (m.related_datasets as string[])[0]) ||
                      (Array.isArray(m.knowledge_targets) &&
                        (m.knowledge_targets as string[])[0]) ||
                      m.current_dataset ||
                      "—"
                  );
                  return (
                    <tr
                      key={String(m.mission_id)}
                      className="border-b border-[var(--border)]/70 hover:bg-[var(--panel-2)]"
                    >
                      <td className="px-4 py-3">
                        <button
                          type="button"
                          className="text-left font-medium text-[var(--text)] hover:underline"
                          onClick={() =>
                            inspect({
                              kind: "mission",
                              title: String(m.title),
                              subtitle: String(m.mission_id),
                              meta: {
                                Priority: String(m.priority || "—"),
                                Status: String(m.status || "—"),
                                Dataset: dataset,
                                Progress: `${m.progress ?? 0}%`,
                              },
                              body: String(
                                m.description ||
                                  m.natural_language_request ||
                                  ""
                              ),
                            })
                          }
                        >
                          {String(m.title)}
                        </button>
                        <div className="font-mono text-[10px] text-[var(--text-faint)]">
                          {String(m.mission_id)}
                        </div>
                      </td>
                      <td className="px-4 py-3 text-[var(--text-muted)]">
                        {dataset}
                      </td>
                      <td className="px-4 py-3">
                        <span className="rounded-md bg-[var(--panel-2)] px-1.5 py-0.5 text-[10px] font-semibold">
                          {String(m.priority || "P1")}
                        </span>
                      </td>
                      <td className="px-4 py-3">
                        <span
                          className={cn(
                            "inline-flex rounded-full px-2 py-0.5 text-[10px] font-semibold uppercase",
                            statusStyle[st]
                          )}
                        >
                          {st}
                        </span>
                      </td>
                      <td className="px-4 py-3 text-[var(--text-muted)]">
                        {Number(m.progress || 0)}%
                      </td>
                      <td className="px-4 py-3 text-[var(--text-faint)]">
                        {formatWib(String(m.created_at || ""))}
                      </td>
                      <td className="px-4 py-3 text-[var(--text-faint)]">
                        {formatWib(String(m.updated_at || m.created_at || ""))}
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </CardBody>
      </Card>

      <div className="grid gap-4 lg:grid-cols-2">
        {/* History */}
        <Card>
          <CardHeader
            title="Mission history"
            description="Completed sessions and past missions"
          />
          <CardBody className="max-h-80 space-y-2 overflow-y-auto p-4 scrollbar-thin">
            {history.sessions.length === 0 && history.missions.length === 0 ? (
              <div className="rounded-xl bg-[var(--panel-2)] px-4 py-8 text-center text-sm text-[var(--text-faint)]">
                No completed missions yet.
                <br />
                History appears after production sessions finish.
              </div>
            ) : (
              <>
                {history.sessions.slice(0, 12).map((s) => (
                  <button
                    key={s.session_id}
                    type="button"
                    onClick={() => {
                      setSelectedSession(s);
                      void loadSessionEvents(s.session_id);
                    }}
                    className={cn(
                      "w-full rounded-xl border bg-[var(--panel-2)] px-3 py-2.5 text-left hover:border-emerald-500/30",
                      selectedSession?.session_id === s.session_id
                        ? "border-emerald-500/40"
                        : "border-[var(--border)]"
                    )}
                  >
                    <div className="flex items-center justify-between gap-2">
                      <span className="truncate text-xs font-medium text-[var(--text)]">
                        {s.mission || s.session_id}
                      </span>
                      <span className="shrink-0 text-[10px] text-emerald-600 dark:text-emerald-300">
                        +{Number(s.knowledge_added || 0)} published
                      </span>
                    </div>
                    <div className="mt-1 flex flex-wrap gap-x-3 text-[10px] text-[var(--text-faint)]">
                      <span>{formatWib(s.end_time || s.start_time)}</span>
                      <span>
                        {s.duration_seconds != null
                          ? `${Math.round(Number(s.duration_seconds))}s`
                          : "—"}
                      </span>
                      <span>rej {Number(s.knowledge_rejected || 0)}</span>
                      <span>{s.status || "completed"}</span>
                    </div>
                  </button>
                ))}
                {history.missions.slice(0, 8).map((m) => (
                  <div
                    key={String(m.mission_id)}
                    className="rounded-xl border border-[var(--border)]/60 px-3 py-2 text-xs"
                  >
                    <div className="font-medium text-[var(--text)]">
                      {String(m.title)}
                    </div>
                    <div className="mt-0.5 text-[10px] text-[var(--text-faint)]">
                      {String(m.status)} · {formatWib(String(m.updated_at || ""))}
                      {m.knowledge_added != null
                        ? ` · +${m.knowledge_added} knowledge`
                        : ""}
                    </div>
                  </div>
                ))}
              </>
            )}
          </CardBody>
        </Card>

        {/* Reports */}
        <Card>
          <CardHeader
            title="Learning reports"
            description="Production batch and quality reports"
          />
          <CardBody className="max-h-80 space-y-2 overflow-y-auto p-4 scrollbar-thin">
            {reports.length === 0 ? (
              <div className="rounded-xl bg-[var(--panel-2)] px-4 py-8 text-center text-sm text-[var(--text-faint)]">
                No reports generated yet.
              </div>
            ) : (
              reports
                .filter((r) => r.name.endsWith(".md") || r.name.endsWith(".json"))
                .slice(0, 24)
                .map((r) => (
                  <a
                    key={r.relativePath}
                    href={`https://github.com/${process.env.NEXT_PUBLIC_GITHUB_REPOSITORY || "ImHeroesKiller/ida-dataset"}/blob/main/${r.relativePath}`}
                    target="_blank"
                    rel="noreferrer"
                    className="block rounded-xl border border-[var(--border)] bg-[var(--panel-2)] px-3 py-2.5 hover:border-emerald-500/30"
                  >
                    <div className="flex items-center justify-between gap-2">
                      <span className="text-xs font-medium text-[var(--text)]">
                        {r.batch && r.batch !== "—"
                          ? `${r.batch} · ${r.mission || "Report"}`
                          : r.mission || r.name.replace(/\.(md|json)$/i, "")}
                      </span>
                      {r.rows_added != null ? (
                        <span className="text-[10px] text-emerald-600 dark:text-emerald-300">
                          +{r.rows_added} rows
                        </span>
                      ) : null}
                    </div>
                    <div className="mt-1 flex flex-wrap gap-x-3 text-[10px] text-[var(--text-faint)]">
                      <span>{formatWib(r.generated || r.mtime)}</span>
                      {r.coverage_increase ? (
                        <span>Coverage {r.coverage_increase}</span>
                      ) : null}
                      {r.confidence != null ? (
                        <span>
                          Conf{" "}
                          {r.confidence <= 1
                            ? `${Math.round(r.confidence * 100)}%`
                            : r.confidence}
                        </span>
                      ) : null}
                    </div>
                  </a>
                ))
            )}
          </CardBody>
        </Card>
      </div>

      {/* Mission production detail — real session telemetry only */}
      {selectedSession ? (
        <Card>
          <CardHeader
            title="Mission production detail"
            description={`${selectedSession.session_id} · real acquisition telemetry`}
          />
          <CardBody className="grid gap-4 p-6 sm:grid-cols-2 lg:grid-cols-4">
            {(() => {
              const d = selectedSession.knowledge_delta || {};
              const ps = selectedSession.publish_summary || {};
              const pt = selectedSession.production_trace || {};
              const connectors = (d.connectors ||
                pt.connectors ||
                []) as Array<Record<string, unknown>>;
              const stages = (pt.stages || []) as Array<Record<string, unknown>>;
              return (
                <>
                  <StatMini
                    label="Duration"
                    value={
                      selectedSession.duration_seconds != null
                        ? `${Math.round(Number(selectedSession.duration_seconds))}s`
                        : "—"
                    }
                  />
                  <StatMini
                    label="Documents"
                    value={`${Number(d.documents_downloaded || 0)} / ${Number(d.documents_discovered || 0)}`}
                  />
                  <StatMini
                    label="Candidates"
                    value={`${Number(d.candidates_extracted || 0)} ext · ${Number(d.candidates_validated || 0)} ok · ${Number(d.candidates_rejected || d.rejected || 0)} rej`}
                  />
                  <StatMini
                    label="Published rows"
                    value={`+${Number(selectedSession.knowledge_added || ps.rows_published || 0)}`}
                  />
                  <div className="sm:col-span-2 lg:col-span-4">
                    <p className="mb-2 text-[10px] font-semibold uppercase tracking-wider text-[var(--text-faint)]">
                      Connectors used
                    </p>
                    {connectors.length === 0 ? (
                      <p className="text-xs text-[var(--text-faint)]">
                        No connector telemetry on this session record.
                      </p>
                    ) : (
                      <div className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
                        {connectors.map((c, i) => (
                          <div
                            key={String(c.connector_id || i)}
                            className="rounded-lg border border-[var(--border)] bg-[var(--panel-2)] px-3 py-2 text-xs"
                          >
                            <div className="font-medium text-[var(--text)]">
                              {String(c.name || c.connector_id)}
                            </div>
                            <div className="text-[10px] text-[var(--text-faint)]">
                              {c.http_status != null
                                ? `HTTP ${c.http_status}`
                                : String(c.status || "")}
                              {" · "}
                              {Number(c.documents_discovered || 0)} found
                              {" · "}
                              {Number(c.documents_downloaded || 0)} down
                            </div>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                  {stages.length > 0 ? (
                    <div className="sm:col-span-2 lg:col-span-4">
                      <p className="mb-2 text-[10px] font-semibold uppercase tracking-wider text-[var(--text-faint)]">
                        Mission timeline
                      </p>
                      <div className="overflow-x-auto">
                        <table className="w-full min-w-[640px] text-left text-xs">
                          <thead className="text-[10px] uppercase text-[var(--text-faint)]">
                            <tr>
                              <th className="pb-1 pr-2">Stage</th>
                              <th className="pb-1 pr-2">Status</th>
                              <th className="pb-1 pr-2">ms</th>
                              <th className="pb-1 pr-2">Docs</th>
                              <th className="pb-1">Rows</th>
                            </tr>
                          </thead>
                          <tbody>
                            {stages.map((st) => (
                              <tr
                                key={String(st.name)}
                                className="border-t border-[var(--border)] text-[var(--text-muted)]"
                              >
                                <td className="py-1.5 pr-2 font-medium text-[var(--text)]">
                                  {String(st.name)}
                                </td>
                                <td className="py-1.5 pr-2">{String(st.status)}</td>
                                <td className="py-1.5 pr-2">{Number(st.duration_ms || 0)}</td>
                                <td className="py-1.5 pr-2">{Number(st.documents || 0)}</td>
                                <td className="py-1.5">{Number(st.rows || 0)}</td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  ) : null}
                  <div className="sm:col-span-2 lg:col-span-4 text-[11px] text-[var(--text-muted)]">
                    Publish balance · extracted={String(ps.extracted ?? d.candidates_extracted ?? "—")} ·
                    validated={String(ps.validated ?? d.candidates_validated ?? "—")} · rejected=
                    {String(ps.rejected ?? d.candidates_rejected ?? "—")} · published=
                    {String(ps.rows_published ?? selectedSession.knowledge_added ?? "—")} ·
                    duplicate={String(ps.duplicate ?? d.publish_duplicate ?? "—")}
                  </div>
                </>
              );
            })()}
          </CardBody>
        </Card>
      ) : null}
    </div>
  );
}

function StatMini({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl border border-[var(--border)] bg-[var(--panel-2)] px-3 py-2">
      <div className="text-[10px] uppercase tracking-wider text-[var(--text-faint)]">
        {label}
      </div>
      <div className="mt-0.5 text-sm font-semibold text-[var(--text)]">{value}</div>
    </div>
  );
}
