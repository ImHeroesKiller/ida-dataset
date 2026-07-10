"use client";

import { useEffect, useMemo, useState } from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { LiveProgress } from "@/components/shared/live-progress";
import {
  useLiveLearning,
  type RuntimeClientFailure,
} from "@/lib/use-live-learning";
import { safeFetchJson } from "@/lib/safe-fetch";

type KpiSnap = {
  knowledge_coverage: number;
  knowledge_added_today: number;
  knowledge_updated_today: number;
  knowledge_rejected: number;
  pending_review: number;
  growing_datasets: { name: string; domain: string; rows: number; path: string }[];
  knowledge_gaps: { name: string; domain: string; path: string }[];
  first_knowledge?: {
    learned?: boolean;
    industry_name?: unknown;
    [key: string]: unknown;
  };
};

type HealthMap = Record<string, string>;

function healthClass(level: string): string {
  switch (level) {
    case "healthy":
      return "text-emerald-300";
    case "warning":
      return "text-amber-300";
    case "failed":
      return "text-red-400";
    case "disabled":
      return "text-zinc-500";
    default:
      return "text-zinc-400";
  }
}

export function LiveDashboard({ initialKpis }: { initialKpis: KpiSnap }) {
  const {
    events,
    activity,
    connected,
    startLive,
    replay,
    runtimeError,
    runtimeStatus,
    clearRuntimeError,
    lastRawResponse,
  } = useLiveLearning();
  const [kpis, setKpis] = useState(initialKpis);
  const [instruction, setInstruction] = useState(
    "Learn Industry Library knowledge for Banking"
  );
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);
  const [sessions, setSessions] = useState<
    { session_id: string; events: number; last_verb?: string | null }[]
  >([]);
  const [health, setHealth] = useState<HealthMap>({});
  const [overallHealth, setOverallHealth] = useState<string>("healthy");
  const [statusSnap, setStatusSnap] = useState<Record<string, unknown> | null>(
    null
  );
  const [showLogs, setShowLogs] = useState(false);
  const [logEntries, setLogEntries] = useState<Record<string, unknown>[]>([]);
  const [copyOk, setCopyOk] = useState(false);

  useEffect(() => {
    const last = events[events.length - 1];
    if (last?.verb === "Learning Completed" || last?.verb === "Knowledge Updated") {
      void safeFetchJson<Record<string, unknown>>("/api/live/replay").then((r) => {
        if (!r.parsed || !r.data) return;
        const data = (r.data.data as Record<string, unknown>) || r.data;
        setSessions((data.sessions as typeof sessions) || []);
      });
    }
  }, [events]);

  useEffect(() => {
    void safeFetchJson<Record<string, unknown>>("/api/live/replay").then((r) => {
      if (!r.parsed || !r.data) return;
      const data = (r.data.data as Record<string, unknown>) || r.data;
      setSessions((data.sessions as typeof sessions) || []);
    });
  }, []);

  // Runtime status + health (does not restart learning)
  useEffect(() => {
    let cancelled = false;
    const load = async () => {
      const r = await safeFetchJson<Record<string, unknown>>("/api/runtime/status");
      if (cancelled || !r.parsed || !r.data) return;
      const data = (r.data.data as Record<string, unknown>) || r.data;
      setStatusSnap(data);
      setHealth((data.health as HealthMap) || {});
      setOverallHealth(String(data.overall_health || "healthy"));
    };
    void load();
    const id = setInterval(() => void load(), 5000);
    return () => {
      cancelled = true;
      clearInterval(id);
    };
  }, []);

  useEffect(() => {
    if (activity.status !== "running" && activity.status !== "progress") return;
    const id = setInterval(() => {
      void safeFetchJson<Record<string, unknown>>("/api/journal").then((r) => {
        if (!r.parsed || !r.data) return;
        const d = r.data;
        const k = (d.kpis as Record<string, unknown> | undefined) || undefined;
        if (k) {
          setKpis((prev) => ({
            ...prev,
            knowledge_added_today:
              (k.added_today as number) ?? prev.knowledge_added_today,
            pending_review: (k.pending_review as number) ?? prev.pending_review,
            knowledge_coverage: (k.coverage as number) ?? prev.knowledge_coverage,
            first_knowledge:
              (k.first_knowledge as KpiSnap["first_knowledge"]) ??
              prev.first_knowledge,
          }));
        }
      });
    }, 3000);
    return () => clearInterval(id);
  }, [activity.status]);

  const feed = useMemo(() => {
    return events
      .filter(
        (e) =>
          e.verb === "Knowledge Updated" ||
          e.verb === "Pipeline" ||
          e.verb === "Publishing" ||
          (e.current_entity && e.status === "progress")
      )
      .slice(-20)
      .reverse();
  }, [events]);

  const failed =
    runtimeStatus === "failed" ||
    activity.status === "error" ||
    Boolean(runtimeError);

  async function onStart() {
    setBusy(true);
    setMsg(null);
    clearRuntimeError();
    setShowLogs(false);
    try {
      const res = await startLive(instruction);
      if (!res.ok) {
        // Do NOT auto-retry — surface the real failure
        setMsg(null);
      } else {
        setMsg(
          `Live session started (pid ${res.pid ?? "—"} · ${res.correlation_id ?? ""})`
        );
      }
    } catch (e) {
      setMsg(e instanceof Error ? e.message : "Failed");
    } finally {
      setBusy(false);
    }
  }

  async function onViewLogs() {
    setShowLogs(true);
    const cid =
      runtimeError?.correlation_id ||
      (statusSnap?.correlation_id as string | undefined);
    const q = new URLSearchParams({ channel: "errors", limit: "40" });
    if (cid) q.set("correlation_id", cid);
    const r = await safeFetchJson<Record<string, unknown>>(
      `/api/runtime/logs?${q.toString()}`
    );
    if (!r.parsed || !r.data) {
      setLogEntries([
        {
          parse_error: r.reason,
          raw: r.raw,
        },
      ]);
      return;
    }
    const data = (r.data.data as Record<string, unknown>) || r.data;
    setLogEntries((data.entries as Record<string, unknown>[]) || []);
  }

  async function onCopyDiagnostic() {
    const payload = {
      captured_at: new Date().toISOString(),
      runtime_status: runtimeStatus,
      activity_status: activity.status,
      failure: runtimeError,
      status: statusSnap,
      health,
      overall_health: overallHealth,
      last_raw_response: lastRawResponse || runtimeError?.raw_response || null,
      recent_events: events.slice(-15),
    };
    try {
      await navigator.clipboard.writeText(JSON.stringify(payload, null, 2));
      setCopyOk(true);
      setTimeout(() => setCopyOk(false), 2000);
    } catch {
      setMsg("Could not copy diagnostic to clipboard");
    }
  }

  const failure: RuntimeClientFailure | null =
    runtimeError ||
    (statusSnap?.last_error as RuntimeClientFailure | undefined) ||
    null;

  const rawDiag = lastRawResponse || failure?.raw_response || null;
  const showStack =
    Boolean(failure?.stack_trace) &&
    (process.env.NODE_ENV === "development" || Boolean(failure?.stack_trace));

  return (
    <div className="space-y-4">
      <div className="flex flex-col gap-3 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <p className="text-xs text-zinc-500">LIVE AI LEARNING DASHBOARD</p>
          <p className="mt-1 max-w-2xl text-sm text-zinc-200">
            Watch IDA learn in realtime. Architecture is frozen — this only
            activates the existing pipeline and makes every stage observable.
          </p>
          <div className="mt-2 flex flex-wrap gap-1.5">
            <Badge className={connected ? "text-emerald-300" : ""}>
              stream {connected ? "connected" : "offline"}
            </Badge>
            <Badge
              className={
                runtimeStatus === "running"
                  ? "text-sky-300"
                  : runtimeStatus === "failed"
                    ? "text-red-400"
                    : ""
              }
            >
              runtime {runtimeStatus || "idle"}
            </Badge>
            <Badge className={healthClass(overallHealth)}>
              health {overallHealth}
            </Badge>
            <Badge>coverage {kpis.knowledge_coverage}%</Badge>
            <Badge>added today {kpis.knowledge_added_today}</Badge>
            <Badge>review {kpis.pending_review}</Badge>
          </div>
        </div>
        <div className="flex w-full max-w-xl flex-col gap-2">
          <Input
            value={instruction}
            onChange={(e) => setInstruction(e.target.value)}
            placeholder="Learn SAP ERP / Industry Banking / …"
          />
          <div className="flex flex-wrap gap-2">
            <Button size="sm" disabled={busy} onClick={onStart}>
              Start live learning
            </Button>
            <Button
              size="sm"
              variant="secondary"
              disabled={!sessions[0]}
              onClick={() => sessions[0] && replay(sessions[0].session_id, 280)}
            >
              Replay last session
            </Button>
          </div>
          {msg ? <p className="text-[11px] text-zinc-400">{msg}</p> : null}
        </div>
      </div>

      {failed && failure ? (
        <Card>
          <CardHeader
            title="Runtime Failed"
            description="Exact failure — not a generic 503. No silent retry."
          />
          <CardBody className="space-y-3 text-sm">
            <div className="rounded-md border border-red-900/60 bg-red-950/40 p-3">
              <p className="text-xs uppercase tracking-wide text-red-400">
                Exact reason
              </p>
              <p className="mt-1 text-red-100">
                {failure.reason ||
                  failure.message ||
                  failure.exception ||
                  "Unknown failure"}
              </p>
              <div className="mt-2 grid gap-1 font-mono text-[11px] text-zinc-400 sm:grid-cols-2">
                <div>component: {failure.component || "—"}</div>
                <div>error_code: {failure.error_code || failure.exception || "—"}</div>
                <div>exception: {failure.exception || "—"}</div>
                <div>correlation: {failure.correlation_id || "—"}</div>
                <div>
                  session: {failure.session_id || activity.session_id || "—"}
                </div>
                <div>action: {failure.recovery_action || "—"}</div>
                <div>time: {failure.timestamp || "—"}</div>
                <div>
                  http:{" "}
                  {rawDiag?.http_status != null ? rawDiag.http_status : "—"}
                </div>
              </div>
            </div>
            <div>
              <p className="text-xs uppercase tracking-wide text-amber-300">
                Suggested recovery
              </p>
              <p className="mt-1 text-zinc-300">
                {failure.recovery_suggestion ||
                  "Inspect /api/runtime/debug and runtime logs, fix the root cause, then Retry."}
              </p>
            </div>
            {showStack && failure.stack_trace ? (
              <div>
                <p className="text-xs uppercase tracking-wide text-zinc-500">
                  Stack trace (development)
                </p>
                <pre className="mt-1 max-h-40 overflow-y-auto whitespace-pre-wrap rounded border border-zinc-800 bg-black/50 p-2 font-mono text-[10px] text-zinc-400 scrollbar-thin">
                  {failure.stack_trace}
                </pre>
              </div>
            ) : null}
            {rawDiag &&
            (!failure.error_code ||
              failure.error_code === "INVALID_JSON_RESPONSE" ||
              rawDiag.parse_error) ? (
              <div>
                <p className="text-xs uppercase tracking-wide text-orange-300">
                  Raw response (invalid / empty JSON)
                </p>
                <div className="mt-1 space-y-1 rounded border border-orange-900/50 bg-orange-950/20 p-2 font-mono text-[10px] text-zinc-300">
                  <div>HTTP status: {rawDiag.http_status} {rawDiag.status_text}</div>
                  <div>URL: {rawDiag.url || "—"}</div>
                  <div>Content-Type: {rawDiag.content_type || "—"}</div>
                  <div>Parse error: {rawDiag.parse_error || "—"}</div>
                  <div className="text-zinc-500">Headers:</div>
                  <pre className="max-h-24 overflow-y-auto whitespace-pre-wrap text-zinc-500 scrollbar-thin">
                    {JSON.stringify(rawDiag.headers, null, 2)}
                  </pre>
                  <div className="text-zinc-500">Body:</div>
                  <pre className="max-h-32 overflow-y-auto whitespace-pre-wrap text-zinc-400 scrollbar-thin">
                    {rawDiag.body === ""
                      ? "(empty body)"
                      : rawDiag.body.slice(0, 4000)}
                  </pre>
                </div>
              </div>
            ) : null}
            <div className="flex flex-wrap gap-2">
              <Button size="sm" disabled={busy} onClick={onStart}>
                Retry
              </Button>
              <Button size="sm" variant="secondary" onClick={onViewLogs}>
                View Logs
              </Button>
              <Button size="sm" variant="outline" onClick={onCopyDiagnostic}>
                {copyOk ? "Copied" : "Copy Diagnostic"}
              </Button>
              <Button
                size="sm"
                variant="outline"
                onClick={() =>
                  void safeFetchJson("/api/runtime/debug").then((r) => {
                    setShowLogs(true);
                    setLogEntries([
                      {
                        debug: r.parsed ? r.data : null,
                        raw: r.raw,
                        reason: r.reason,
                      },
                    ]);
                  })
                }
              >
                Runtime Debug
              </Button>
            </div>
            {showLogs ? (
              <div className="max-h-48 overflow-y-auto rounded border border-zinc-800 bg-black/40 p-2 font-mono text-[10px] text-zinc-400 scrollbar-thin">
                {logEntries.length === 0 ? (
                  <p>No error log entries for this correlation yet.</p>
                ) : (
                  logEntries.map((e, i) => (
                    <pre
                      key={i}
                      className="mb-2 whitespace-pre-wrap border-b border-zinc-900 pb-2"
                    >
                      {JSON.stringify(e, null, 2)}
                    </pre>
                  ))
                )}
              </div>
            ) : null}
          </CardBody>
        </Card>
      ) : null}

      <Card>
        <CardHeader
          title="Runtime health"
          description="True component status — Healthy · Warning · Failed · Disabled"
        />
        <CardBody>
          <div className="grid gap-2 sm:grid-cols-3 lg:grid-cols-6">
            {(
              [
                "runtime",
                "scheduler",
                "connector",
                "queue",
                "sse",
                "publisher",
              ] as const
            ).map((key) => (
              <div
                key={key}
                className="rounded border border-zinc-800 bg-zinc-950/50 px-2 py-2"
              >
                <div className="text-[10px] uppercase text-zinc-500">{key}</div>
                <div className={`text-sm font-medium ${healthClass(health[key] || "healthy")}`}>
                  {health[key] || "healthy"}
                </div>
              </div>
            ))}
          </div>
          {statusSnap ? (
            <div className="mt-3 grid gap-1 font-mono text-[11px] text-zinc-500 sm:grid-cols-2">
              <div>session: {String(statusSnap.session_id || "—")}</div>
              <div>stage: {String(statusSnap.current_stage || "—")}</div>
              <div>task: {String(statusSnap.current_task || "—")}</div>
              <div>uptime: {String(statusSnap.uptime_seconds ?? 0)}s</div>
              <div>docs: {String(statusSnap.documents_processed ?? 0)}</div>
              <div>
                candidates: {String(statusSnap.knowledge_candidates ?? 0)}
              </div>
            </div>
          ) : null}
        </CardBody>
      </Card>

      <Card>
        <CardHeader title="Learning activity" description="Live process observation" />
        <CardBody>
          <LiveProgress activity={activity} events={events} />
        </CardBody>
      </Card>

      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">
              Knowledge added today
            </div>
            <div className="text-2xl font-semibold text-emerald-400">
              {kpis.knowledge_added_today}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">
              Updated today
            </div>
            <div className="text-2xl font-semibold text-sky-400">
              {kpis.knowledge_updated_today}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">Rejected</div>
            <div className="text-2xl font-semibold text-red-400">
              {kpis.knowledge_rejected}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">
              Waiting review
            </div>
            <div className="text-2xl font-semibold text-amber-300">
              {kpis.pending_review}
            </div>
          </CardBody>
        </Card>
      </div>

      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader
            title="Knowledge feed"
            description="Newest learning signals first"
          />
          <CardBody className="max-h-72 space-y-1 overflow-y-auto text-xs scrollbar-thin">
            {feed.length === 0 ? (
              <p className="text-zinc-500">
                Start a live mission to see knowledge appear in realtime.
              </p>
            ) : (
              feed.map((e, i) => (
                <div
                  key={`${e.seq}-${i}`}
                  className="border-b border-zinc-900 py-1.5 text-zinc-300"
                >
                  <span className="text-emerald-400">
                    {e.current_entity || e.verb}
                  </span>
                  {e.dataset ? (
                    <span className="text-zinc-600"> · {e.dataset}</span>
                  ) : null}
                  <div className="text-[11px] text-zinc-500">{e.detail}</div>
                </div>
              ))
            )}
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Learning timeline"
            description="Stages animate as events arrive"
          />
          <CardBody className="max-h-72 space-y-1 overflow-y-auto font-mono text-[11px] scrollbar-thin">
            {events.length === 0 ? (
              <p className="font-sans text-xs text-zinc-500">
                Timeline idle — waiting for live events via SSE.
              </p>
            ) : (
              events.slice(-30).map((e, i) => (
                <div key={`${e.seq}-t-${i}`} className="text-zinc-400">
                  <span className="text-zinc-600">
                    {String(e.ts || "").slice(11, 19)}
                  </span>{" "}
                  <span className="text-sky-400">{e.stage}</span>{" "}
                  <span className="text-zinc-200">{e.verb}</span>
                </div>
              ))
            )}
          </CardBody>
        </Card>
      </div>

      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader title="Growing datasets" />
          <CardBody className="space-y-1 text-xs">
            {kpis.growing_datasets.map((d) => (
              <div
                key={d.path}
                className="flex justify-between border-b border-zinc-900 py-1.5 text-zinc-300"
              >
                <span>{d.name}</span>
                <span className="text-zinc-500">{d.rows} rows</span>
              </div>
            ))}
          </CardBody>
        </Card>
        <Card>
          <CardHeader title="Knowledge gaps" />
          <CardBody className="max-h-56 space-y-1 overflow-y-auto text-xs scrollbar-thin">
            {kpis.knowledge_gaps.map((d) => (
              <div
                key={d.path}
                className="flex justify-between border-b border-zinc-900 py-1.5 text-zinc-400"
              >
                <span>{d.name}</span>
                <span className="text-zinc-600">{d.domain}</span>
              </div>
            ))}
          </CardBody>
        </Card>
      </div>

      <Card>
        <CardHeader
          title="Replay sessions"
          description="Exact event stream as it happened"
        />
        <CardBody className="flex flex-wrap gap-2 text-xs">
          {sessions.length === 0 ? (
            <p className="text-zinc-500">No recorded sessions yet</p>
          ) : (
            sessions.slice(0, 8).map((s) => (
              <Button
                key={s.session_id}
                size="sm"
                variant="outline"
                onClick={() => replay(s.session_id, 250)}
              >
                {s.session_id} ({s.events})
              </Button>
            ))
          )}
        </CardBody>
      </Card>
    </div>
  );
}
