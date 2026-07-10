"use client";

import { useCallback, useEffect, useState } from "react";
import {
  safeFetchJson,
  type RawHttpDiagnostic,
  type SafeJsonResult,
} from "@/lib/safe-fetch";

export type SessionEvent = {
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

export type SessionSummary = {
  session_id: string;
  start_time?: string | null;
  end_time?: string | null;
  duration_seconds?: number | null;
  status?: string;
  mission?: string;
  knowledge_added?: number;
  knowledge_updated?: number;
  knowledge_rejected?: number;
  summary?: string;
  trigger?: string;
  dry_run?: boolean;
  events?: number;
  github?: Record<string, unknown>;
};

export type PeriodStats = {
  sessions: number;
  success: number;
  failed: number;
  success_rate: number;
  knowledge_added: number;
  knowledge_updated: number;
  knowledge_rejected: number;
  avg_duration_seconds: number;
  avg_knowledge_added: number;
};

export type LearningDashboardState = {
  status: string;
  current_status?: string;
  next_scheduled_run?: string;
  last_successful_run?: SessionSummary | null;
  last_failed_run?: SessionSummary | null;
  current_session?: SessionSummary | null;
  current_mission?: string | null;
  knowledge_added?: number;
  knowledge_updated?: number;
  knowledge_rejected?: number;
  session_duration?: number | null;
  history?: {
    today: PeriodStats;
    this_week: PeriodStats;
    this_month: PeriodStats;
    total: PeriodStats;
    knowledge_growth: {
      added: number;
      updated: number;
      rejected: number;
    };
  };
  sessions?: SessionSummary[];
  legacy_sessions?: SessionSummary[];
  github_actions?: {
    configured?: boolean;
    running?: boolean;
    queued?: boolean;
    status?: string;
    current_run?: {
      id?: number;
      html_url?: string;
      status?: string;
      conclusion?: string | null;
      created_at?: string;
    } | null;
    recent_runs?: unknown[];
    next_scheduled_hint?: string;
    repository?: string | null;
    error?: string | null;
  };
  execution_model?: string;
};

export type StartLearningResult = {
  ok: boolean;
  success?: boolean;
  message?: string;
  reason?: string;
  error_code?: string;
  recovery_suggestion?: string;
  workflow?: string;
  repository?: string;
  inputs?: Record<string, string>;
  raw_response?: RawHttpDiagnostic | null;
};

function failureFrom(
  result: SafeJsonResult<Record<string, unknown>>,
  fallback: string
): StartLearningResult {
  const d = result.data || {};
  const reason =
    (typeof d.reason === "string" && d.reason) ||
    (typeof d.message === "string" && d.message) ||
    (typeof d.error === "string" && d.error) ||
    result.reason ||
    fallback;
  return {
    ok: false,
    success: false,
    message: reason,
    reason,
    error_code: (d.error_code as string) || "DISPATCH_FAILED",
    recovery_suggestion: d.recovery_suggestion as string | undefined,
    raw_response: result.raw,
  };
}

/**
 * Poll learning sessions from disk + GitHub Actions status.
 * Prefer useLearning() from LearningProvider (single shared poll).
 * No SSE, no local Python runtime.
 */
export function useLearningMonitor(pollMs = 5000) {
  const [dashboard, setDashboard] = useState<LearningDashboardState>({
    status: "idle",
  });
  const [events, setEvents] = useState<SessionEvent[]>([]);
  const [activeSessionId, setActiveSessionId] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [lastRaw, setLastRaw] = useState<RawHttpDiagnostic | null>(null);

  const refresh = useCallback(async () => {
    const result = await safeFetchJson<Record<string, unknown>>(
      "/api/sessions"
    );
    if (!result.parsed || !result.data) {
      setLastRaw(result.raw);
      setError(result.reason || "Failed to load sessions");
      setLoading(false);
      return;
    }
    const payload = result.data;
    const data =
      (payload.data as LearningDashboardState | undefined) ||
      (payload as unknown as LearningDashboardState);
    setDashboard(data);
    setError(null);
    setLoading(false);

    // Prefer running / current session events for journal
    const curId =
      data.current_session?.session_id ||
      data.last_successful_run?.session_id ||
      null;
    if (curId && curId !== activeSessionId) {
      // only auto-switch when not replaying a user-selected session
      if (!activeSessionId || data.github_actions?.running) {
        setActiveSessionId(curId);
      }
    }
  }, [activeSessionId]);

  const loadSessionEvents = useCallback(async (sessionId: string) => {
    const result = await safeFetchJson<Record<string, unknown>>(
      `/api/sessions?session_id=${encodeURIComponent(sessionId)}`
    );
    if (!result.parsed || !result.data) {
      setLastRaw(result.raw);
      return [];
    }
    const payload = result.data;
    const data =
      (payload.data as Record<string, unknown> | undefined) || payload;
    const session = (data.session as Record<string, unknown>) || data;
    const list = (session.events || data.events || []) as SessionEvent[];
    setEvents(list);
    setActiveSessionId(sessionId);
    return list;
  }, []);

  useEffect(() => {
    void refresh();
    const id = setInterval(() => void refresh(), pollMs);
    return () => clearInterval(id);
  }, [refresh, pollMs]);

  // Load events when active session changes
  useEffect(() => {
    if (!activeSessionId) return;
    void loadSessionEvents(activeSessionId);
  }, [activeSessionId, loadSessionEvents]);

  const startLearning = useCallback(
    async (mission?: string, dryRun = true): Promise<StartLearningResult> => {
      setError(null);
      const result = await safeFetchJson<Record<string, unknown>>(
        "/api/run",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            action: "learn",
            mission,
            dry_run: dryRun,
            environment: "production",
          }),
        }
      );
      setLastRaw(result.raw);
      if (!result.parsed || result.success === false || !result.http_ok) {
        const fail = failureFrom(result, "Failed to dispatch learning workflow");
        setError(fail.reason || fail.message || null);
        return fail;
      }
      const payload = result.data || {};
      const data =
        (payload.data as Record<string, unknown> | undefined) || {};
      // Force refresh so "running" appears from Actions API
      await refresh();
      return {
        ok: true,
        success: true,
        message:
          (payload.message as string) ||
          "Learning workflow dispatched to GitHub Actions",
        workflow: (data.workflow as string) || "learn.yml",
        repository: data.repository as string | undefined,
        inputs: data.inputs as Record<string, string> | undefined,
      };
    },
    [refresh]
  );

  /**
   * Replay a completed session from stored events — preserves timestamps/order.
   * No fake streaming of a live process; client-side paced playback only.
   */
  const replay = useCallback(
    async (sessionId: string, paceMs = 280) => {
      const list = await loadSessionEvents(sessionId);
      if (!list.length) return { events: [] as SessionEvent[] };
      setEvents([]);
      for (const ev of list) {
        setEvents((prev) => [...prev, ev]);
        await new Promise((r) => setTimeout(r, paceMs));
      }
      return { events: list };
    },
    [loadSessionEvents]
  );

  const selectSession = useCallback(
    (sessionId: string) => {
      setActiveSessionId(sessionId);
      void loadSessionEvents(sessionId);
    },
    [loadSessionEvents]
  );

  const activity = (() => {
    const last = events[events.length - 1];
    const ga = dashboard.github_actions;
    const running =
      ga?.running ||
      dashboard.status === "running" ||
      dashboard.current_status === "running";
    return {
      status: running
        ? "running"
        : dashboard.status === "failed"
          ? "error"
          : last?.status === "completed"
            ? "idle"
            : dashboard.status || "idle",
      session_id: activeSessionId || dashboard.current_session?.session_id,
      mission_id: last?.mission_id,
      progress: last?.progress ?? (running ? 5 : 0),
      current_thought:
        last?.detail ||
        dashboard.current_mission ||
        (running
          ? "GitHub Actions learning session in progress…"
          : "Idle — waiting for next scheduled or manual learning session"),
      current_task: last?.current_task || last?.detail,
      current_entity: last?.current_entity,
      current_document: last?.current_document,
      current_source: last?.current_source,
      current_dataset: last?.dataset,
      current_relationship: last?.current_relationship,
      current_confidence: last?.confidence,
      updated_at: last?.ts || dashboard.current_session?.end_time,
    };
  })();

  return {
    dashboard,
    events,
    activity,
    activeSessionId,
    loading,
    error,
    lastRaw,
    refresh,
    startLearning,
    replay,
    selectSession,
    loadSessionEvents,
    setEvents,
  };
}

export type UseLearningMonitorResult = ReturnType<typeof useLearningMonitor>;

/** @deprecated Use useLearningMonitor or useLearning() */
export const useLearningSessions = useLearningMonitor;
