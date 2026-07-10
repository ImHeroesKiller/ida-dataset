/**
 * Learning session storage reader.
 *
 * Sessions live at automation/sessions/YYYY-MM-DD/SESSION-*.json
 * Written exclusively by GitHub Actions learning jobs (or local CI CLI).
 * Dashboard is a realtime monitor of completed + running sessions — no local runtime.
 */

import fs from "fs";
import path from "path";
import { getRepoRoot, repoPath } from "./paths";

export type LearningSession = {
  session_id: string;
  start_time?: string | null;
  end_time?: string | null;
  duration_seconds?: number | null;
  knowledge_added?: number;
  knowledge_updated?: number;
  knowledge_rejected?: number;
  mission?: string;
  instruction?: string;
  mission_id?: string | null;
  status?: string;
  errors?: unknown[];
  summary?: string;
  trigger?: string;
  dry_run?: boolean;
  environment?: string;
  planner_output?: unknown;
  connector_output?: unknown;
  knowledge_delta?: Record<string, unknown> | null;
  publish_summary?: Record<string, unknown> | null;
  telemetry?: Record<string, unknown>;
  logs?: string[];
  events?: SessionEvent[];
  github?: Record<string, unknown>;
  path?: string;
  execution_model?: string;
};

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
  meta?: Record<string, unknown>;
};

export type SessionSummary = {
  session_id: string;
  path?: string;
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
  knowledge_delta?: Record<string, unknown> | null;
};

export type HistoryStats = {
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

function readJson(file: string): Record<string, unknown> | null {
  try {
    if (!fs.existsSync(file)) return null;
    return JSON.parse(fs.readFileSync(file, "utf8")) as Record<string, unknown>;
  } catch {
    return null;
  }
}

export function sessionsRoot(root = getRepoRoot()): string {
  return path.join(root, "automation", "sessions");
}

/** Next hourly boundary (UTC) — approximate for schedule cron "0 * * * *". */
export function nextScheduledRunIso(from = new Date()): string {
  const d = new Date(from);
  d.setUTCMinutes(0, 0, 0);
  d.setUTCHours(d.getUTCHours() + 1);
  return d.toISOString().replace(/\.\d{3}Z$/, "Z");
}

export function loadSession(
  sessionId: string,
  root = getRepoRoot()
): LearningSession | null {
  const base = sessionsRoot(root);
  if (!fs.existsSync(base)) return null;

  // Fast path: derive day from SESSION-YYYYMMDD-...
  const m = /^SESSION-(\d{8})-/i.exec(sessionId);
  if (m) {
    const raw = m[1];
    const day = `${raw.slice(0, 4)}-${raw.slice(4, 6)}-${raw.slice(6, 8)}`;
    const file = path.join(base, day, `${sessionId}.json`);
    const data = readJson(file);
    if (data) return data as LearningSession;
  }

  // Fallback search
  const stack = [base];
  while (stack.length) {
    const dir = stack.pop()!;
    let entries: fs.Dirent[];
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      continue;
    }
    for (const ent of entries) {
      const full = path.join(dir, ent.name);
      if (ent.isDirectory()) stack.push(full);
      else if (ent.name === `${sessionId}.json`) {
        const data = readJson(full);
        if (data) return { ...(data as LearningSession), path: full };
      }
    }
  }
  return null;
}

export function listSessions(opts: {
  limit?: number;
  root?: string;
} = {}): SessionSummary[] {
  const root = opts.root || getRepoRoot();
  const base = sessionsRoot(root);
  const limit = opts.limit ?? 100;
  if (!fs.existsSync(base)) return [];

  const files: string[] = [];
  const stack = [base];
  while (stack.length) {
    const dir = stack.pop()!;
    let entries: fs.Dirent[];
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      continue;
    }
    for (const ent of entries) {
      const full = path.join(dir, ent.name);
      if (ent.isDirectory()) stack.push(full);
      else if (
        ent.isFile() &&
        ent.name.startsWith("SESSION-") &&
        ent.name.endsWith(".json")
      ) {
        files.push(full);
      }
    }
  }

  const out: SessionSummary[] = [];
  for (const file of files) {
    const data = readJson(file);
    if (!data) continue;
    out.push({
      session_id: String(data.session_id || path.basename(file, ".json")),
      path: path.relative(root, file),
      start_time: (data.start_time as string) ?? null,
      end_time: (data.end_time as string) ?? null,
      duration_seconds: (data.duration_seconds as number) ?? null,
      status: data.status as string | undefined,
      mission: data.mission as string | undefined,
      knowledge_added: Number(data.knowledge_added || 0),
      knowledge_updated: Number(data.knowledge_updated || 0),
      knowledge_rejected: Number(data.knowledge_rejected || 0),
      summary: data.summary as string | undefined,
      trigger: data.trigger as string | undefined,
      dry_run: Boolean(data.dry_run),
      events: Array.isArray(data.events) ? data.events.length : 0,
      github: (data.github as Record<string, unknown>) || {},
      knowledge_delta: (data.knowledge_delta as Record<string, unknown>) || null,
    });
  }

  out.sort((a, b) =>
    String(b.start_time || "").localeCompare(String(a.start_time || ""))
  );
  return out.slice(0, limit);
}

function periodStats(items: SessionSummary[]): PeriodStats {
  const total = items.length;
  const success = items.filter((s) =>
    ["completed", "success"].includes(String(s.status))
  ).length;
  const failed = items.filter((s) =>
    ["failed", "error"].includes(String(s.status))
  ).length;
  const durations = items
    .map((s) => s.duration_seconds)
    .filter((d): d is number => d != null && !Number.isNaN(d));
  const added = items.map((s) => Number(s.knowledge_added || 0));
  return {
    sessions: total,
    success,
    failed,
    success_rate: total ? Math.round((success / total) * 1000) / 10 : 0,
    knowledge_added: added.reduce((a, b) => a + b, 0),
    knowledge_updated: items.reduce(
      (a, s) => a + Number(s.knowledge_updated || 0),
      0
    ),
    knowledge_rejected: items.reduce(
      (a, s) => a + Number(s.knowledge_rejected || 0),
      0
    ),
    avg_duration_seconds: durations.length
      ? Math.round(
          (durations.reduce((a, b) => a + b, 0) / durations.length) * 100
        ) / 100
      : 0,
    avg_knowledge_added: added.length
      ? Math.round((added.reduce((a, b) => a + b, 0) / added.length) * 100) /
        100
      : 0,
  };
}

export function computeHistory(sessions: SessionSummary[]): HistoryStats {
  const now = Date.now();
  const dayMs = 86400000;
  const startOfToday = new Date();
  startOfToday.setUTCHours(0, 0, 0, 0);
  const todayMs = startOfToday.getTime();

  const parse = (s: SessionSummary) => {
    if (!s.start_time) return null;
    const t = Date.parse(s.start_time);
    return Number.isNaN(t) ? null : t;
  };

  const today = sessions.filter((s) => {
    const t = parse(s);
    return t != null && t >= todayMs;
  });
  const week = sessions.filter((s) => {
    const t = parse(s);
    return t != null && now - t < 7 * dayMs;
  });
  const month = sessions.filter((s) => {
    const t = parse(s);
    return t != null && now - t < 30 * dayMs;
  });

  const total = periodStats(sessions);
  return {
    today: periodStats(today),
    this_week: periodStats(week),
    this_month: periodStats(month),
    total,
    knowledge_growth: {
      added: total.knowledge_added,
      updated: total.knowledge_updated,
      rejected: total.knowledge_rejected,
    },
  };
}

/**
 * Derive dashboard status from local session files.
 * Running is refined by GitHub Actions API in github-actions.ts.
 */
export function deriveLocalStatus(sessions: SessionSummary[]): {
  status: "idle" | "running" | "completed" | "failed";
  current_session: SessionSummary | null;
  last_successful: SessionSummary | null;
  last_failed: SessionSummary | null;
} {
  const running = sessions.find((s) => s.status === "running") || null;
  const lastSuccessful =
    sessions.find((s) =>
      ["completed", "success"].includes(String(s.status))
    ) || null;
  const lastFailed =
    sessions.find((s) => ["failed", "error"].includes(String(s.status))) ||
    null;
  const latest = sessions[0] || null;

  if (running) {
    return {
      status: "running",
      current_session: running,
      last_successful: lastSuccessful,
      last_failed: lastFailed,
    };
  }
  if (latest && ["failed", "error"].includes(String(latest.status))) {
    return {
      status: "failed",
      current_session: latest,
      last_successful: lastSuccessful,
      last_failed: lastFailed,
    };
  }
  if (latest && ["completed", "success"].includes(String(latest.status))) {
    return {
      status: "completed",
      current_session: latest,
      last_successful: lastSuccessful,
      last_failed: lastFailed,
    };
  }
  return {
    status: "idle",
    current_session: null,
    last_successful: lastSuccessful,
    last_failed: lastFailed,
  };
}

/** Also surface legacy SES-*.jsonl sessions for replay compatibility. */
export function listLegacySessions(root = getRepoRoot()): SessionSummary[] {
  const dir = path.join(root, "automation/learning/state/sessions");
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".jsonl"))
    .map((f) => {
      const full = path.join(dir, f);
      const lines = fs.readFileSync(full, "utf8").split("\n").filter(Boolean);
      let first: Record<string, unknown> | null = null;
      let last: Record<string, unknown> | null = null;
      try {
        first = JSON.parse(lines[0] || "{}");
        last = JSON.parse(lines[lines.length - 1] || "{}");
      } catch {
        /* ignore */
      }
      return {
        session_id: f.replace(/\.jsonl$/, ""),
        path: path.relative(root, full),
        start_time: (first?.ts as string) ?? null,
        end_time: (last?.ts as string) ?? null,
        status:
          last?.status === "completed"
            ? "completed"
            : last?.status === "error"
              ? "failed"
              : "completed",
        mission: (last?.detail as string) || undefined,
        knowledge_added: 0,
        knowledge_updated: 0,
        knowledge_rejected: 0,
        events: lines.length,
        summary: "Legacy live-runtime session (pre-GHA)",
        trigger: "legacy",
      } satisfies SessionSummary;
    })
    .sort((a, b) =>
      String(b.start_time || "").localeCompare(String(a.start_time || ""))
    );
}

export function loadLegacySessionEvents(
  sessionId: string,
  root = getRepoRoot()
): SessionEvent[] {
  const file = path.join(
    root,
    "automation/learning/state/sessions",
    `${sessionId}.jsonl`
  );
  if (!fs.existsSync(file)) return [];
  return fs
    .readFileSync(file, "utf8")
    .split("\n")
    .filter(Boolean)
    .map((line) => {
      try {
        return JSON.parse(line) as SessionEvent;
      } catch {
        return null;
      }
    })
    .filter(Boolean) as SessionEvent[];
}

export function getSessionsDashboard() {
  const sessions = listSessions({ limit: 200 });
  const legacy = listLegacySessions();
  const local = deriveLocalStatus(sessions);
  const history = computeHistory(sessions);
  const current = local.current_session
    ? loadSession(local.current_session.session_id)
    : null;

  // Prefer knowledge counters from latest completed session + daily KPIs
  const latestDone = local.last_successful;
  return {
    execution_model: "github_actions",
    status: local.status,
    current_status: local.status,
    next_scheduled_run: nextScheduledRunIso(),
    last_successful_run: latestDone,
    last_failed_run: local.last_failed,
    current_session: local.current_session,
    current_mission:
      current?.mission ||
      local.current_session?.mission ||
      latestDone?.mission ||
      null,
    knowledge_added:
      current?.knowledge_added ?? latestDone?.knowledge_added ?? 0,
    knowledge_updated:
      current?.knowledge_updated ?? latestDone?.knowledge_updated ?? 0,
    knowledge_rejected:
      current?.knowledge_rejected ?? latestDone?.knowledge_rejected ?? 0,
    session_duration:
      current?.duration_seconds ?? latestDone?.duration_seconds ?? null,
    history,
    sessions,
    legacy_sessions: legacy.slice(0, 20),
    index: readJson(repoPath("automation/sessions/index.json")),
  };
}
