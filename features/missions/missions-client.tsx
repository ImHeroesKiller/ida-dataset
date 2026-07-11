"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import { useLearning } from "@/hooks/learning-provider";
import { cn } from "@/lib/utils";
import { formatWib } from "@/lib/time-wib";
import { safeFetchJson } from "@/lib/safe-fetch";

type Row = Record<string, unknown>;

type Toast = { id: string; text: string; tone: "ok" | "err" | "warn" };

type SessionSummary = {
  session_id: string;
  mission?: string;
  status?: string;
  start_time?: string | null;
  end_time?: string | null;
  duration_seconds?: number | null;
  knowledge_added?: number;
  knowledge_rejected?: number;
};

function mapStatus(
  raw: string
): "Waiting" | "Running" | "Completed" | "Error" | "Paused" {
  const s = raw.toLowerCase();
  if (s.includes("cancel") || s.includes("pause")) return "Paused";
  if (s.includes("fail") || s.includes("error")) return "Error";
  if (s.includes("run") || s.includes("progress") || s.includes("active"))
    return "Running";
  if (s.includes("complete") || s.includes("done") || s.includes("success"))
    return "Completed";
  if (s.includes("queue") || s.includes("pending") || s.includes("draft"))
    return "Waiting";
  return "Waiting";
}

const statusStyle: Record<string, string> = {
  Waiting: "bg-[var(--badge-warning-bg)] text-[var(--badge-warning-fg)]",
  Running: "bg-[var(--badge-running-bg)] text-[var(--badge-running-fg)]",
  Completed: "bg-[var(--badge-completed-bg)] text-[var(--badge-completed-fg)]",
  Error: "bg-[var(--badge-error-bg)] text-[var(--badge-error-fg)]",
  Paused: "bg-[var(--badge-idle-bg)] text-[var(--badge-idle-fg)]",
};

const STAGES = [
  "Discovering",
  "Collecting",
  "Extracting",
  "Validating",
  "Publishing",
  "Completed",
] as const;

function stageFromEvents(
  events: Array<{ verb?: string; stage?: string; detail?: string }>
): string {
  if (!events.length) return "Discovering";
  const last = events[events.length - 1];
  const blob = `${last.verb || ""} ${last.stage || ""} ${last.detail || ""}`.toLowerCase();
  if (/complete|finished|done/.test(blob)) return "Completed";
  if (/publish|append|knowledge/.test(blob)) return "Publishing";
  if (/validat|review|policy/.test(blob)) return "Validating";
  if (/extract|pipeline|entity|understand/.test(blob)) return "Extracting";
  if (/download|document|reading|queue|collect/.test(blob)) return "Collecting";
  return "Discovering";
}

function friendlyError(input: unknown): string {
  const raw =
    typeof input === "string"
      ? input
      : input instanceof Error
        ? input.message
        : String(input ?? "");
  if (!raw.trim()) return "Unable to start the mission. Please try again.";
  if (/unexpected token|json\.parse|syntaxerror|invalid json/i.test(raw)) {
    return "Something went wrong. Please try again.";
  }
  return raw;
}

async function readJsonSafe(res: Response): Promise<Record<string, unknown>> {
  const text = await res.text();
  if (!text.trim()) return {};
  try {
    return JSON.parse(text) as Record<string, unknown>;
  } catch {
    return { ok: false, error: "Something went wrong. Please try again." };
  }
}

function missionTitle(m: Row): string {
  return String(m.title || m.natural_language_request || m.mission_id || "Mission");
}

export function MissionsClient({
  missions: initialMissions,
}: {
  missions: Row[];
  contracts?: Row[];
  reports?: unknown[];
}) {
  const { dashboard, events, activity, startLearning } = useLearning();
  const [missions, setMissions] = useState(initialMissions);
  const [sessions, setSessions] = useState<SessionSummary[]>([]);
  const [text, setText] = useState("");
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);
  const [msgTone, setMsgTone] = useState<"ok" | "err">("ok");
  const [toasts, setToasts] = useState<Toast[]>([]);
  const [paused, setPaused] = useState(false);
  const lastToastKey = useRef("");
  const submitting = useRef(false);
  const lastInstruction = useRef("");

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
    if (Array.isArray(data.sessions)) setSessions(data.sessions as SessionSummary[]);
  }, []);

  useEffect(() => {
    void refresh();
    const id = setInterval(() => void refresh(), 8000);
    return () => clearInterval(id);
  }, [refresh]);

  useEffect(() => {
    if (dashboard.sessions?.length) {
      setSessions((prev) =>
        prev.length ? prev : (dashboard.sessions as SessionSummary[])
      );
    }
  }, [dashboard.sessions]);

  const queue = useMemo(() => {
    return missions.filter((m) => {
      const st = mapStatus(String(m.status || ""));
      return st === "Waiting" || st === "Running" || st === "Paused";
    });
  }, [missions]);

  const history = useMemo(() => {
    const fromMissions = missions.filter((m) => {
      const st = mapStatus(String(m.status || ""));
      return st === "Completed" || st === "Error";
    });
    return { missions: fromMissions, sessions };
  }, [missions, sessions]);

  const running =
    !paused &&
    (dashboard.github_actions?.running ||
      queue.some((m) => mapStatus(String(m.status)) === "Running") ||
      activity.status === "running");

  const currentMission = useMemo(() => {
    const active = queue.find((m) => mapStatus(String(m.status)) === "Running");
    if (active) return missionTitle(active);
    if (queue[0]) return missionTitle(queue[0]);
    return String(
      dashboard.current_mission || activity.current_task || "No active mission"
    );
  }, [queue, dashboard.current_mission, activity.current_task]);

  const statusLabel: "Running" | "Waiting" | "Paused" | "Idle" | "Error" = paused
    ? "Paused"
    : dashboard.github_actions?.status === "failed" || activity.status === "error"
      ? "Error"
      : running
        ? "Running"
        : dashboard.github_actions?.queued
          ? "Waiting"
          : "Idle";

  const currentStage = useMemo(() => {
    if (paused) return "Paused";
    if (events.length) return stageFromEvents(events);
    if (running) return "Discovering";
    return "—";
  }, [events, running, paused]);

  const progressPct = useMemo(() => {
    if (paused) return 0;
    if (!running) {
      const a = queue[0];
      return Number(a?.progress || 0);
    }
    const idx = STAGES.indexOf(currentStage as (typeof STAGES)[number]);
    if (idx < 0) return 15;
    return Math.round(((idx + 1) / STAGES.length) * 100);
  }, [running, currentStage, queue, paused]);

  async function dispatchInstruction(instruction: string) {
    if (submitting.current || busy) return;
    if (!instruction.trim() || instruction.trim().length < 8) {
      setMsg("Describe the mission in a few words.");
      setMsgTone("err");
      return;
    }
    submitting.current = true;
    setBusy(true);
    setMsg(null);
    setPaused(false);
    lastInstruction.current = instruction.trim();
    try {
      const res = await fetch("/api/missions", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "mission", text: instruction.trim() }),
      });
      const data = await readJsonSafe(res);
      if (!res.ok || data.ok === false) {
        const err = friendlyError(
          data.error || data.reason || data.message || "Failed"
        );
        setMsg(err);
        setMsgTone("err");
        pushToast(err, "err");
        return;
      }
      setText("");
      setMsg("Mission queued.");
      setMsgTone("ok");
      pushToast("Mission started", "ok");
      if (Array.isArray(data.missions)) setMissions(data.missions as Row[]);
      else await refresh();
    } catch (e) {
      const err = friendlyError(e);
      setMsg(err);
      setMsgTone("err");
      pushToast(err, "err");
    } finally {
      setBusy(false);
      submitting.current = false;
    }
  }

  async function onStart() {
    if (text.trim()) {
      await dispatchInstruction(text);
      return;
    }
    setBusy(true);
    try {
      const res = await startLearning(undefined, true);
      setPaused(false);
      if (res.ok) {
        setMsg("Learning started.");
        setMsgTone("ok");
        pushToast("Learning started", "ok");
      } else {
        setMsg(res.reason || "Unable to start.");
        setMsgTone("err");
        pushToast(res.reason || "Unable to start", "err");
      }
    } finally {
      setBusy(false);
    }
  }

  function onPause() {
    setPaused(true);
    pushToast("Paused (operator)", "warn");
    setMsg("Paused — resume when ready.");
    setMsgTone("ok");
  }

  function onResume() {
    setPaused(false);
    pushToast("Resumed", "ok");
    setMsg("Resumed.");
    setMsgTone("ok");
  }

  async function onRetry() {
    const instr =
      lastInstruction.current ||
      text.trim() ||
      String(queue[0]?.natural_language_request || queue[0]?.title || "");
    if (instr) await dispatchInstruction(instr);
    else {
      setMsg("Nothing to retry — enter a mission first.");
      setMsgTone("err");
    }
  }

  function onStop() {
    setPaused(true);
    pushToast("Stop requested — current cycle will finish", "warn");
    setMsg("Stop requested. The current cycle will finish safely.");
    setMsgTone("ok");
  }

  return (
    <div className="op-page relative">
      <div className="pointer-events-none fixed right-3 top-12 z-50 flex w-72 flex-col gap-1.5">
        {toasts.map((t) => (
          <div
            key={t.id}
            className={cn(
              "pointer-events-auto rounded-[var(--radius-md)] border px-2.5 py-1.5 text-xs shadow-md",
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

      <header className="op-page-header">
        <div>
          <h1 className="text-page-title">Mission</h1>
          <p>Queue the next dataset the factory should grow.</p>
        </div>
      </header>

      {/* Current mission */}
      <Card>
        <CardHeader title="Current Mission" />
        <CardBody className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
          <Field label="Mission" value={currentMission} />
          <Field
            label="Status"
            value={statusLabel}
            tone={
              statusLabel === "Running"
                ? "run"
                : statusLabel === "Error"
                  ? "err"
                  : statusLabel === "Paused" || statusLabel === "Waiting"
                    ? "warn"
                    : undefined
            }
          />
          <Field label="Current Stage" value={currentStage} />
          <div>
            <p className="text-[10px] font-semibold uppercase tracking-wide text-[var(--text-muted)]">
              Progress
            </p>
            <div className="mt-1.5">
              <Progress value={progressPct} />
            </div>
            <p className="mt-1 text-[11px] tabular-nums text-[var(--text-muted)]">
              {progressPct}%
            </p>
          </div>
        </CardBody>
      </Card>

      {/* Controls + create */}
      <Card>
        <CardHeader title="Controls" description="Start · Pause · Resume · Retry · Stop" />
        <CardBody className="space-y-3">
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
                e.preventDefault();
                void onStart();
              }
            }}
            disabled={busy}
            rows={2}
            placeholder="Mission instruction (optional for Start)"
            className="w-full resize-y rounded-[var(--radius-md)] border border-[var(--border)] bg-[var(--panel)] px-2.5 py-2 text-xs text-[var(--text)] outline-none placeholder:text-[var(--text-muted)] focus:border-[var(--blue)] focus:ring-1 focus:ring-[var(--blue)]/25 disabled:opacity-50"
            aria-label="Mission instruction"
          />
          <div className="flex flex-wrap gap-1.5">
            <Button size="sm" disabled={busy} loading={busy} onClick={() => void onStart()}>
              Start
            </Button>
            <Button
              size="sm"
              variant="secondary"
              disabled={!running || paused}
              onClick={onPause}
            >
              Pause
            </Button>
            <Button
              size="sm"
              variant="secondary"
              disabled={!paused}
              onClick={onResume}
            >
              Resume
            </Button>
            <Button
              size="sm"
              variant="secondary"
              disabled={busy}
              onClick={() => void onRetry()}
            >
              Retry
            </Button>
            <Button
              size="sm"
              variant="danger"
              disabled={!running && !paused}
              onClick={onStop}
            >
              Stop
            </Button>
          </div>
          {msg ? (
            <p
              className={cn(
                "text-xs font-medium",
                msgTone === "ok" ? "text-[var(--green)]" : "text-[var(--red)]"
              )}
            >
              {msg}
            </p>
          ) : null}
        </CardBody>
      </Card>

      {/* Queue */}
      <Card>
        <CardHeader title="Mission Queue" description={`${queue.length} waiting or running`} />
        <CardBody className="overflow-x-auto p-0">
          <table className="ds-table min-w-[560px]">
            <thead>
              <tr>
                <th>Mission</th>
                <th>Status</th>
                <th>Progress</th>
                <th>Updated</th>
              </tr>
            </thead>
            <tbody>
              {queue.length === 0 ? (
                <tr>
                  <td colSpan={4} className="text-center text-[var(--text-muted)]">
                    Queue empty — start a mission to begin.
                  </td>
                </tr>
              ) : (
                queue.map((m) => {
                  const st = mapStatus(String(m.status || ""));
                  return (
                    <tr key={String(m.mission_id)}>
                      <td>
                        <div className="font-medium text-[var(--text)]">
                          {missionTitle(m)}
                        </div>
                      </td>
                      <td>
                        <span
                          className={cn(
                            "inline-flex rounded-full px-2 py-0.5 text-[10px] font-semibold",
                            statusStyle[st]
                          )}
                        >
                          {st}
                        </span>
                      </td>
                      <td className="tabular-nums">{Number(m.progress || 0)}%</td>
                      <td className="text-[var(--text-muted)]">
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

      {/* History */}
      <Card>
        <CardHeader title="Mission History" />
        <CardBody className="max-h-64 space-y-1.5 overflow-y-auto scrollbar-thin">
          {history.sessions.length === 0 && history.missions.length === 0 ? (
            <p className="py-6 text-center text-xs text-[var(--text-muted)]">
              No completed missions yet.
            </p>
          ) : (
            <>
              {history.sessions.slice(0, 16).map((s) => (
                <div
                  key={s.session_id}
                  className="flex items-center justify-between gap-2 rounded-[var(--radius-md)] border border-[var(--border)] bg-[var(--panel-2)] px-2.5 py-1.5"
                >
                  <div className="min-w-0">
                    <p className="truncate text-xs font-medium text-[var(--text)]">
                      {s.mission || s.session_id}
                    </p>
                    <p className="text-[10px] text-[var(--text-muted)]">
                      {formatWib(s.end_time || s.start_time)} ·{" "}
                      {mapStatus(String(s.status || "completed"))}
                    </p>
                  </div>
                  <span className="shrink-0 text-[11px] font-semibold tabular-nums text-emerald-600 dark:text-emerald-300">
                    +{Number(s.knowledge_added || 0)}
                  </span>
                </div>
              ))}
              {history.missions.slice(0, 8).map((m) => (
                <div
                  key={String(m.mission_id)}
                  className="flex items-center justify-between gap-2 rounded-[var(--radius-md)] border border-[var(--border)] bg-[var(--panel-2)] px-2.5 py-1.5"
                >
                  <div className="min-w-0">
                    <p className="truncate text-xs font-medium text-[var(--text)]">
                      {missionTitle(m)}
                    </p>
                    <p className="text-[10px] text-[var(--text-muted)]">
                      {mapStatus(String(m.status || ""))}
                    </p>
                  </div>
                </div>
              ))}
            </>
          )}
        </CardBody>
      </Card>
    </div>
  );
}

function Field({
  label,
  value,
  tone,
}: {
  label: string;
  value: string;
  tone?: "run" | "err" | "warn";
}) {
  return (
    <div className="min-w-0">
      <p className="text-[10px] font-semibold uppercase tracking-wide text-[var(--text-muted)]">
        {label}
      </p>
      <p
        className={cn(
          "mt-0.5 truncate text-sm font-semibold text-[var(--text)]",
          tone === "run" && "text-emerald-600 dark:text-emerald-300",
          tone === "err" && "text-red-600 dark:text-red-300",
          tone === "warn" && "text-amber-700 dark:text-amber-300"
        )}
        title={value}
      >
        {value}
      </p>
    </div>
  );
}
