"use client";

import { useCallback, useEffect, useState } from "react";
import { subscribeLiveLearning } from "@/lib/live-sse-bus";
import {
  safeFetchJson,
  type RawHttpDiagnostic,
  type SafeJsonResult,
} from "@/lib/safe-fetch";

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
  reason?: string;
  error_code?: string;
  stack_trace?: string;
  correlation_id?: string;
  session_id?: string | null;
  recovery_action?: string;
  recovery_suggestion?: string;
  recoverable?: boolean;
  /** When JSON parse failed — raw transport diagnostics */
  raw_response?: RawHttpDiagnostic | null;
};

export type StartLiveResult = {
  ok: boolean;
  success?: boolean;
  message?: string;
  reason?: string;
  pid?: number;
  correlation_id?: string;
  session_id?: string | null;
  error?: string;
  error_code?: string;
  component?: string;
  failure?: RuntimeClientFailure;
  recovery_suggestion?: string;
  status?: string | Record<string, unknown>;
  data?: Record<string, unknown>;
  stack_trace?: string | null;
  raw_response?: RawHttpDiagnostic | null;
};

function failureFromEnvelope(
  result: SafeJsonResult<Record<string, unknown>>,
  fallbackComponent: string
): RuntimeClientFailure {
  const d = result.data || {};
  const nested = (d.failure as RuntimeClientFailure | undefined) || null;
  const reason =
    (typeof d.reason === "string" && d.reason) ||
    (typeof d.message === "string" && d.message) ||
    (typeof d.error === "string" && d.error) ||
    result.reason ||
    `HTTP ${result.http_status}`;

  if (!result.parsed) {
    return {
      timestamp: new Date().toISOString(),
      component: fallbackComponent,
      exception: "InvalidJsonResponse",
      message: reason,
      reason,
      error_code: "INVALID_JSON_RESPONSE",
      recovery_suggestion:
        "The server returned a non-JSON or empty body. Inspect Raw response below and /api/runtime/debug.",
      raw_response: result.raw,
    };
  }

  return {
    timestamp: nested?.timestamp || new Date().toISOString(),
    component:
      (d.component as string) ||
      nested?.component ||
      fallbackComponent,
    exception:
      nested?.exception ||
      (d.error_code as string) ||
      "StartFailed",
    message: reason,
    reason,
    error_code:
      (d.error_code as string) ||
      nested?.error_code ||
      nested?.exception ||
      "FAILED",
    stack_trace:
      (d.stack_trace as string) ||
      nested?.stack_trace ||
      undefined,
    correlation_id:
      (d.correlation_id as string) ||
      nested?.correlation_id,
    session_id:
      (d.session_id as string | null) ??
      nested?.session_id ??
      null,
    recovery_action: nested?.recovery_action,
    recovery_suggestion:
      (d.recovery_suggestion as string) ||
      nested?.recovery_suggestion ||
      "Inspect /api/runtime/status and /api/runtime/debug.",
    raw_response: null,
  };
}

/**
 * Subscribe to live learning via the shared SSE bus (single EventSource).
 * Start failures are returned with structured failure + recovery — never silent retry.
 * Never assumes JSON — uses defensive parsing.
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
  const [lastRawResponse, setLastRawResponse] =
    useState<RawHttpDiagnostic | null>(null);

  useEffect(() => {
    const unsub = subscribeLiveLearning({
      onJournal: (data) => {
        setEvents((prev) => [...prev.slice(-300), data]);
        if (data.status === "error") {
          setRuntimeError({
            message: data.detail,
            reason: data.detail,
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
              reason: data.current_thought || "Runtime error",
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

  // Poll runtime status lightly — defensive JSON
  useEffect(() => {
    let cancelled = false;
    const tick = async () => {
      const result = await safeFetchJson<Record<string, unknown>>(
        "/api/runtime/status"
      );
      if (cancelled) return;
      if (!result.parsed) {
        // Do not crash UI — surface only if we have no better error
        setLastRawResponse(result.raw);
        return;
      }
      const payload = result.data || {};
      const data =
        (payload.data as Record<string, unknown> | undefined) || payload;
      const st = String(data.status || payload.status || "idle");
      setRuntimeStatus(st);
      if (data.last_error) {
        setRuntimeError(data.last_error as RuntimeClientFailure);
      } else if (st === "running") {
        setRuntimeError(null);
      }
    };
    void tick();
    const id = setInterval(() => void tick(), 4000);
    return () => {
      cancelled = true;
      clearInterval(id);
    };
  }, []);

  const startLive = useCallback(
    async (instruction?: string): Promise<StartLiveResult> => {
      setRuntimeError(null);
      setLastRawResponse(null);
      const result = await safeFetchJson<Record<string, unknown>>(
        "/api/live/start",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            instruction:
              instruction ||
              "Learn Industry Library knowledge — live observable session",
            pace: 0.65,
          }),
        }
      );

      setLastRawResponse(result.raw);

      if (!result.parsed || result.success === false || !result.http_ok) {
        const failure = failureFromEnvelope(result, "api.live.start");
        setRuntimeError(failure);
        setRuntimeStatus("failed");
        return {
          ok: false,
          success: false,
          message: failure.message,
          reason: failure.reason,
          correlation_id: failure.correlation_id,
          session_id: failure.session_id,
          error: failure.message,
          error_code: failure.error_code,
          component: failure.component,
          failure,
          recovery_suggestion: failure.recovery_suggestion,
          stack_trace: failure.stack_trace,
          raw_response: result.raw,
        };
      }

      const payload = result.data || {};
      const data =
        (payload.data as Record<string, unknown> | undefined) || {};
      const pid = (data.pid as number | undefined) ?? undefined;
      const correlation_id =
        (payload.correlation_id as string) ||
        (data.correlation_id as string) ||
        undefined;
      const session_id =
        (payload.session_id as string | null) ??
        (data.session_id as string | null) ??
        null;

      setRuntimeStatus(String(payload.status || "starting"));
      return {
        ok: true,
        success: true,
        message:
          (payload.message as string) || "Live learning session started",
        pid,
        correlation_id,
        session_id,
        status: String(payload.status || "running"),
        data,
      };
    },
    []
  );

  const clearRuntimeError = useCallback(() => {
    setRuntimeError(null);
    setLastRawResponse(null);
  }, []);

  const replay = useCallback(async (sessionId: string, paceMs = 350) => {
    const result = await safeFetchJson<Record<string, unknown>>(
      `/api/live/replay?session_id=${encodeURIComponent(sessionId)}`
    );
    if (!result.parsed || !result.data) {
      setLastRawResponse(result.raw);
      setRuntimeError(failureFromEnvelope(result, "api.live.replay"));
      return result;
    }
    const payload = result.data;
    const data =
      (payload.data as Record<string, unknown> | undefined) || payload;
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
    lastRawResponse,
  };
}
