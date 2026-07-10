/**
 * Shared client-side SSE subscription bus.
 *
 * Problem: LiveDashboard + BottomConsole each called useLiveLearning(),
 * creating two EventSource connections (and more under React Strict Mode).
 * That accumulated server abort listeners / intervals and triggered
 * MaxListenersExceededWarning on reconnects.
 *
 * Fix: one EventSource per browser tab, ref-counted. Never raise max listeners.
 */

export type BusJournalEvent = {
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

export type BusActivity = {
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
  last_error?: unknown;
};

type JournalHandler = (ev: BusJournalEvent) => void;
type ActivityHandler = (ev: BusActivity) => void;
type KpiHandler = (ev: Record<string, unknown>) => void;
type ConnHandler = (connected: boolean) => void;

type Subscription = {
  onJournal?: JournalHandler;
  onActivity?: ActivityHandler;
  onKpis?: KpiHandler;
  onConnection?: ConnHandler;
};

type InternalSub = Subscription & { id: number };

let es: EventSource | null = null;
let refCount = 0;
let nextId = 1;
const subs = new Map<number, InternalSub>();
let connected = false;

function notifyConnection(value: boolean) {
  connected = value;
  for (const s of subs.values()) {
    s.onConnection?.(value);
  }
}

function ensureSource() {
  if (es) return;
  es = new EventSource("/api/live");

  es.addEventListener("hello", () => notifyConnection(true));
  es.addEventListener("ping", () => notifyConnection(true));

  es.addEventListener("journal", (ev) => {
    try {
      const data = JSON.parse((ev as MessageEvent).data) as BusJournalEvent;
      for (const s of subs.values()) s.onJournal?.(data);
    } catch {
      /* ignore bad payload */
    }
  });

  es.addEventListener("activity", (ev) => {
    try {
      const data = JSON.parse((ev as MessageEvent).data) as BusActivity;
      for (const s of subs.values()) s.onActivity?.(data);
    } catch {
      /* ignore */
    }
  });

  es.addEventListener("kpis", (ev) => {
    try {
      const data = JSON.parse(
        (ev as MessageEvent).data
      ) as Record<string, unknown>;
      for (const s of subs.values()) s.onKpis?.(data);
    } catch {
      /* ignore */
    }
  });

  es.onerror = () => {
    notifyConnection(false);
    // EventSource auto-reconnects; we do not open a second connection.
  };
}

function teardownIfIdle() {
  if (refCount > 0) return;
  if (es) {
    es.close();
    es = null;
  }
  connected = false;
}

/**
 * Subscribe to the shared live learning stream.
 * Returns unsubscribe — must be called on unmount (releases ref-count).
 */
export function subscribeLiveLearning(handlers: Subscription): () => void {
  const id = nextId++;
  const sub: InternalSub = { id, ...handlers };
  subs.set(id, sub);
  refCount += 1;
  ensureSource();
  handlers.onConnection?.(connected);

  return () => {
    subs.delete(id);
    refCount = Math.max(0, refCount - 1);
    teardownIfIdle();
  };
}

/** Test/diagnostic helpers */
export function __sseBusStats() {
  return {
    refCount,
    subscriberCount: subs.size,
    hasSource: Boolean(es),
    connected,
  };
}

export function __sseBusResetForTests() {
  for (const id of [...subs.keys()]) subs.delete(id);
  refCount = 0;
  if (es) {
    es.close();
    es = null;
  }
  connected = false;
  nextId = 1;
}
