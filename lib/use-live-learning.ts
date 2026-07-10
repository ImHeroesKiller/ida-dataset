"use client";

import { useCallback, useEffect, useState } from "react";
import { subscribeLiveLearning } from "@/lib/live-sse-bus";

export type LiveJournalEvent = {
  seq?: number;
  ts?: string;
  verb?: string;
  detail?: string;
  stage?: string;
  status?: string;
  dataset?: string;
  mission_id?: string;
  session_id?: string;
  progress?: number | null;
  current_task?: string | null;
  current_entity?: string | null;
  current_document?: string | null;
  current_source?: string | null;
  current_relationship?: string | null;
  confidence?: number | null;
  duration_ms?: number | null;
};

export type LiveActivity = {
  status?: string;
  session_id?: string;
  mission_id?: string;
  correlation_id?: string;
  progress?: number;
  current_thought?: string;
  current_task?: string;
  current_entity?: string;
  current_document?: string;
  current_source?: string;
  current_dataset?: string;
  current_relationship?: string;
  current_confidence?: number | null;
  last_learned?: string;
  updated_at?: string;
  last_error?: RuntimeClientFailure | null;
};

export type RuntimeClientFailure = {
  timestamp?: string;
  component?: string;
  exception?: string;
  message?: string;
  stack_trace?: string;
  correlation_id?: string;
  session_id?: string | null;
  recovery_action?: string;
  recovery_suggestion?: string;
  recoverable?: boolean;
};

export type StartLiveResult = {
  ok: boolean;
  message?: string;
  pid?: number;
  correlation_id?: string;
  session_id?: string | null;
  error?: string;
  failure?: RuntimeClientFailure;
  recovery_suggestion?: string;
  status?: Record<string, unknown>;
};

/**
 * Subscribe to live learning via the shared SSE bus (single EventSource).
 * Start failures are returned with structured failure + recovery — never silent retry.
 */
export function useLiveLearning() {
  const [events, setEvents] = useState<LiveJournalEvent[]>([]);
  const [activity, setActivity] = useState<LiveActivity>({
    status: "idle",
    current_thought: "Connecting to learning stream…",
  });
  const [connected, setConnected] = useState(false);
  const [kpis, setKpis] = useState<Record<string, unknown> | null>(null);
  const [runtimeError, setRuntimeError] = useState<RuntimeClientFailure | null>(
    null
  );
  const [runtimeStatus, setRuntimeStatus] = useState<string>("idle");

  useEffect(() => {
    const unsub = subscribeLiveLearning({
      onJournal: (data) => {
        setEvents((prev) => [...prev.slice(-300), data]);
        if (data.status === "error") {
          setRuntimeError({
            message: data.detail,
            component: data.stage || "learning",
            exception: data.verb || "LearningError",
            session_id: data.session_id,
            timestamp: data.ts,
            recovery_suggestion:
              "Open View Logs /api/runtime/logs for the full failure record.",
          });
          setRuntimeStatus("failed");
        }
      },
      onActivity: (data) => {
        const activityData: LiveActivity = {
          status: data.status,
          session_id: data.session_id,
          mission_id: data.mission_id,
          correlation_id: data.correlation_id,
          progress: data.progress,
          current_thought: data.current_thought,
          current_task: data.current_task,
          current_entity: data.current_entity,
          current_document: data.current_document,
          current_source: data.current_source,
          current_dataset: data.current_dataset,
          current_relationship: data.current_relationship,
          current_confidence: data.current_confidence,
          last_learned: data.last_learned,
          updated_at: data.updated_at,
          last_error: (data.last_error as RuntimeClientFailure | null) ?? null,
        };
        setActivity(activityData);
        if (data.status === "error" || data.last_error) {
          setRuntimeError(
            (data.last_error as RuntimeClientFailure) || {
              message: data.current_thought || "Runtime error",
              session_id: data.session_id,
              correlation_id: data.correlation_id,
            }
          );
          setRuntimeStatus("failed");
        } else if (data.status === "idle" || data.status === "running") {
          setRuntimeStatus(data.status);
          if (data.status === "running") setRuntimeError(null);
        }
      },
      onKpis: (data) => setKpis(data),
      onConnection: (c) => setConnected(c),
    });
    return unsub;
  }, []);

  // Poll runtime status lightly so dashboard shows true lifecycle / failures
  // even if SSE activity snapshot lags. Does not restart learning.
  useEffect(() => {
    let cancelled = false;
    const tick = () => {
      fetch("/api/runtime/status")
        .then((r) => r.json())
        .then((d) => {
          if (cancelled) return;
          if (d?.status) setRuntimeStatus(String(d.status));
          if (d?.last_error) {
            setRuntimeError(d.last_error as RuntimeClientFailure);
          } else if (d?.status === "running" || d?.status === "idle") {
            // clear sticky error only when healthy again
            if (d.status === "running") setRuntimeError(null);
          }
        })
        .catch(() => null);
    };
    tick();
    const id = setInterval(tick, 4000);
    return () => {
      cancelled = true;
      clearInterval(id);
    };
  }, []);

  const startLive = useCallback(
    async (instruction?: string): Promise<StartLiveResult> => {
      setRuntimeError(null);
      try {
        const res = await fetch("/api/live/start", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            instruction:
              instruction ||
              "Learn Industry Library knowledge — live observable session",
            pace: 0.65,
          }),
        });
        const data = (await res.json()) as StartLiveResult & {
          error?: string;
        };
        if (!res.ok || !data.ok) {
          const failure =
            data.failure ||
            ({
              timestamp: new Date().toISOString(),
              component: "api.live.start",
              exception: "StartFailed",
              message:
                data.message ||
                data.error ||
                `HTTP ${res.status} from /api/live/start`,
              correlation_id: data.correlation_id,
              recovery_action: "inspect_and_retry",
              recovery_suggestion:
                data.recovery_suggestion ||
                "Inspect /api/runtime/status and /api/runtime/logs.",
            } as RuntimeClientFailure);
          setRuntimeError(failure);
          setRuntimeStatus("failed");
          return {
            ok: false,
            message: failure.message,
            correlation_id: data.correlation_id || failure.correlation_id,
            failure,
            recovery_suggestion:
              data.recovery_suggestion || failure.recovery_suggestion,
            status: data.status,
          };
        }
        setRuntimeStatus("starting");
        return data;
      } catch (e) {
        const failure: RuntimeClientFailure = {
          timestamp: new Date().toISOString(),
          component: "api.live.start",
          exception: e instanceof Error ? e.name : "NetworkError",
          message: e instanceof Error ? e.message : String(e),
          recovery_action: "check_network",
          recovery_suggestion:
            "Could not reach /api/live/start. Confirm the Next.js server is running.",
        };
        setRuntimeError(failure);
        setRuntimeStatus("failed");
        return { ok: false, failure, message: failure.message };
      }
    },
    []
  );

  const clearRuntimeError = useCallback(() => setRuntimeError(null), []);

  const replay = useCallback(async (sessionId: string, paceMs = 350) => {
    const res = await fetch(
      `/api/live/replay?session_id=${encodeURIComponent(sessionId)}`
    );
    const data = await res.json();
    const list = (data.events || []) as LiveJournalEvent[];
    setEvents([]);
    for (const ev of list) {
      setEvents((prev) => [...prev, ev]);
      setActivity({
        status: ev.status === "completed" ? "running" : ev.status,
        session_id: ev.session_id,
        mission_id: ev.mission_id,
        progress: ev.progress ?? undefined,
        current_thought: ev.detail,
        current_task: ev.current_task || ev.detail,
        current_entity: ev.current_entity || undefined,
        current_document: ev.current_document || undefined,
        current_source: ev.current_source || undefined,
        current_dataset: ev.dataset,
        current_relationship: ev.current_relationship || undefined,
        current_confidence: ev.confidence,
      });
      await new Promise((r) => setTimeout(r, paceMs));
    }
    setActivity((a) => ({
      ...a,
      status: "idle",
      current_thought: "Replay finished",
    }));
    return data;
  }, []);

  return {
    events,
    activity,
    connected,
    kpis,
    startLive,
    replay,
    setEvents,
    runtimeError,
    runtimeStatus,
    clearRuntimeError,
  };
}
