"use client";

import { useCallback, useEffect, useRef, useState } from "react";

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
};

/**
 * Subscribe to live learning SSE stream (no completed-result polling).
 */
export function useLiveLearning() {
  const [events, setEvents] = useState<LiveJournalEvent[]>([]);
  const [activity, setActivity] = useState<LiveActivity>({
    status: "idle",
    current_thought: "Connecting to learning stream…",
  });
  const [connected, setConnected] = useState(false);
  const [kpis, setKpis] = useState<Record<string, unknown> | null>(null);
  const esRef = useRef<EventSource | null>(null);

  useEffect(() => {
    const es = new EventSource("/api/live");
    esRef.current = es;

    es.addEventListener("hello", () => setConnected(true));
    es.addEventListener("ping", () => setConnected(true));
    es.addEventListener("journal", (ev) => {
      try {
        const data = JSON.parse((ev as MessageEvent).data) as LiveJournalEvent;
        setEvents((prev) => [...prev.slice(-300), data]);
      } catch {
        /* ignore */
      }
    });
    es.addEventListener("activity", (ev) => {
      try {
        setActivity(JSON.parse((ev as MessageEvent).data) as LiveActivity);
      } catch {
        /* ignore */
      }
    });
    es.addEventListener("kpis", (ev) => {
      try {
        setKpis(JSON.parse((ev as MessageEvent).data));
      } catch {
        /* ignore */
      }
    });
    es.onerror = () => setConnected(false);

    return () => {
      es.close();
      esRef.current = null;
    };
  }, []);

  const startLive = useCallback(async (instruction?: string) => {
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
    return res.json();
  }, []);

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

  return { events, activity, connected, kpis, startLive, replay, setEvents };
}
