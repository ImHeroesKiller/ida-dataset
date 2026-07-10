/**
 * Progressive publish queue — backend paced publishing.
 * Delay lives here (or Python CI), never simulated only in the UI.
 */

import fs from "fs";
import path from "path";
import { getRepoRoot, PATHS, repoPath } from "@/lib/paths";
import { getLearningMode } from "@/lib/learning-mode";
import type { FullCandidate } from "@/lib/review-actions";

function nowIso(): string {
  return new Date().toISOString().replace(/\.\d{3}Z$/, "Z");
}

/** True on Vercel / any read-only serverless FS — never write state files. */
function isReadOnlyFs(): boolean {
  return Boolean(process.env.VERCEL) || process.env.IDA_READ_ONLY_FS === "1";
}

function writeJson(file: string, data: unknown): void {
  if (isReadOnlyFs()) return;
  try {
    fs.mkdirSync(path.dirname(file), { recursive: true });
    const tmp = `${file}.tmp.${process.pid}`;
    fs.writeFileSync(tmp, JSON.stringify(data, null, 2) + "\n", "utf8");
    fs.renameSync(tmp, file);
  } catch (e) {
    const err = e as NodeJS.ErrnoException;
    if (err?.code === "EROFS" || err?.code === "EACCES") return;
    throw e;
  }
}

function appendJsonl(file: string, row: unknown): void {
  if (isReadOnlyFs()) return;
  try {
    fs.mkdirSync(path.dirname(file), { recursive: true });
    fs.appendFileSync(file, JSON.stringify(row) + "\n", "utf8");
  } catch (e) {
    const err = e as NodeJS.ErrnoException;
    if (err?.code === "EROFS" || err?.code === "EACCES") return;
    throw e;
  }
}

export function publishQueueDir(): string {
  return repoPath("automation/queue/publish");
}

export function publishStatePath(): string {
  return repoPath("automation/learning/state/publish_state.json");
}

export function knowledgeFeedPath(): string {
  return repoPath("automation/learning/state/knowledge_feed.jsonl");
}

export type PublishState = {
  status: "idle" | "publishing" | "paused" | "completed";
  total: number;
  published: number;
  remaining: number;
  speed: number;
  unit: string;
  eta_seconds: number | null;
  current_dataset: string | null;
  current_knowledge: string | null;
  next_knowledge: string | null;
  last_published_at: string | null;
  started_at: string | null;
  updated_at: string;
  mode: string;
  auto_publish: boolean;
};

export type FeedItem = {
  ts: string;
  knowledge_type: string;
  name: string;
  dataset: string;
  source: string;
  confidence: number;
  candidate_id?: string;
  published_at: string;
};

export type PublishStateView = PublishState & {
  queue: Array<{
    candidate_id: string;
    name: string;
    dataset: string;
    confidence: number;
  }>;
  feed: FeedItem[];
  journal_tail: Array<Record<string, unknown>>;
};

function emptyState(): PublishState {
  const mode = getLearningMode();
  return {
    status: "idle",
    total: 0,
    published: 0,
    remaining: 0,
    speed: mode.publish_rate || 1,
    unit: mode.publish_rate_unit || "rows_per_second",
    eta_seconds: null,
    current_dataset: null,
    current_knowledge: null,
    next_knowledge: null,
    last_published_at: null,
    started_at: null,
    updated_at: nowIso(),
    mode: mode.mode,
    auto_publish: mode.auto_publish,
  };
}

export function readPublishState(): PublishState {
  const p = publishStatePath();
  try {
    if (fs.existsSync(p)) {
      return { ...emptyState(), ...JSON.parse(fs.readFileSync(p, "utf8")) };
    }
  } catch {
    /* ignore */
  }
  return emptyState();
}

function listPublishFiles(): string[] {
  const dir = publishQueueDir();
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".json") && f !== ".gitkeep")
    .sort();
}

function loadCandidateFromFile(file: string): FullCandidate | null {
  try {
    return JSON.parse(fs.readFileSync(file, "utf8")) as FullCandidate;
  } catch {
    return null;
  }
}

function knowledgeType(c: FullCandidate): string {
  const ds = (c.target_dataset || c.entity_type || "Knowledge").replace(
    /_library$/,
    ""
  );
  return ds
    .split("_")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(" ");
}

function resolveDatasetCsv(targetDataset: string): string | null {
  const root = getRepoRoot();
  const preferred = path.join(
    root,
    "domains",
    "business_development",
    `${targetDataset}.csv`
  );
  if (fs.existsSync(preferred)) return preferred;
  const domains = path.join(root, "domains");
  if (!fs.existsSync(domains)) return preferred;
  const stack = [domains];
  while (stack.length) {
    const d = stack.pop()!;
    for (const name of fs.readdirSync(d)) {
      const full = path.join(d, name);
      if (fs.statSync(full).isDirectory()) stack.push(full);
      else if (name === `${targetDataset}.csv`) return full;
    }
  }
  return preferred;
}

function entityAlreadyInCsv(csvPath: string, entityId: string): boolean {
  if (!fs.existsSync(csvPath) || !entityId) return false;
  const text = fs.readFileSync(csvPath, "utf8");
  return text.split(/\r?\n/).some((line) => line.includes(entityId));
}

function csvEscape(value: string): string {
  if (/[",\n\r]/.test(value)) return `"${value.replace(/"/g, '""')}"`;
  return value;
}

function appendPayloadToCsv(
  csvPath: string,
  payload: Record<string, unknown>
): boolean {
  fs.mkdirSync(path.dirname(csvPath), { recursive: true });
  let headers: string[] = [];
  if (fs.existsSync(csvPath)) {
    const first = fs.readFileSync(csvPath, "utf8").split(/\r?\n/)[0] || "";
    headers = first
      .split(",")
      .map((h) => h.replace(/^\uFEFF/, "").trim())
      .filter(Boolean);
  }
  if (!headers.length) {
    headers = Object.keys(payload);
    fs.writeFileSync(csvPath, headers.map(csvEscape).join(",") + "\n", "utf8");
  }
  const row = headers.map((h) => csvEscape(String(payload[h] ?? ""))).join(",");
  fs.appendFileSync(csvPath, row + "\n", "utf8");
  return true;
}

function emitJournal(verb: string, detail: string, meta?: Record<string, unknown>) {
  const journal = repoPath("automation/learning/state/learning_journal.jsonl");
  appendJsonl(journal, {
    seq: Date.now(),
    ts: nowIso(),
    verb,
    detail,
    stage: "publish",
    status: "progress",
    ...meta,
  });
}

function emitFeed(item: FeedItem) {
  appendJsonl(knowledgeFeedPath(), item);
}

function bumpDaily(field: string, n = 1) {
  try {
    const day = nowIso().slice(0, 10);
    const p = repoPath(`automation/learning/state/daily_${day}.json`);
    let daily: Record<string, number> = {};
    if (fs.existsSync(p)) daily = JSON.parse(fs.readFileSync(p, "utf8"));
    daily[field] = Number(daily[field] || 0) + n;
    writeJson(p, daily);
  } catch {
    /* ignore */
  }
}

function recomputeState(patch: Partial<PublishState> = {}): PublishState {
  const files = listPublishFiles();
  const prev = readPublishState();
  const mode = getLearningMode();
  const remaining = files.length;
  const next = files[0]
    ? loadCandidateFromFile(path.join(publishQueueDir(), files[0]))
    : null;
  const speed = mode.publish_rate || 1;
  const eta =
    remaining === 0 || speed <= 0
      ? 0
      : Math.ceil(remaining / speed);

  const state: PublishState = {
    ...prev,
    ...patch,
    remaining,
    speed,
    unit: mode.publish_rate_unit,
    eta_seconds: eta,
    next_knowledge: next
      ? String(next.canonical_name || next.entity_id)
      : null,
    current_dataset: next?.target_dataset || prev.current_dataset,
    updated_at: nowIso(),
    mode: mode.mode,
    auto_publish: mode.auto_publish,
    status:
      patch.status ||
      (remaining > 0
        ? prev.status === "publishing"
          ? "publishing"
          : "idle"
        : prev.published > 0
          ? "completed"
          : "idle"),
  };
  // total = published + remaining (session batch)
  if (state.total < state.published + remaining) {
    state.total = state.published + remaining;
  }
  writeJson(publishStatePath(), state);
  return state;
}

/**
 * Move pending candidate into progressive publish queue (review bypass path).
 */
export function enqueueToPublishQueue(
  candidateId: string,
  opts: { from?: "pending" | "approved" } = {}
): { ok: boolean; message: string } {
  const from = opts.from || "pending";
  const srcDir =
    from === "approved" ? PATHS.queueApproved() : PATHS.queuePending();
  const src = path.join(srcDir, `${candidateId}.json`);
  if (!fs.existsSync(src)) {
    return { ok: false, message: `Not found in ${from}: ${candidateId}` };
  }
  try {
    const raw = JSON.parse(fs.readFileSync(src, "utf8")) as FullCandidate;
    raw.provenance = {
      ...(raw.provenance || {}),
      validation_status: "approved",
      reviewer: raw.provenance?.reviewer || "auto-development",
    };
    const destDir = publishQueueDir();
    fs.mkdirSync(destDir, { recursive: true });
    writeJson(path.join(destDir, `${candidateId}.json`), raw);
    fs.unlinkSync(src);
    recomputeState({ status: "idle" });
    return { ok: true, message: `Enqueued ${candidateId}` };
  } catch (e) {
    const err = e as Error;
    return { ok: false, message: err.message };
  }
}

/** Development: move all pending → publish queue. */
export function autoEnqueuePending(): { moved: number; ids: string[] } {
  const dir = PATHS.queuePending();
  if (!fs.existsSync(dir)) return { moved: 0, ids: [] };
  const ids: string[] = [];
  for (const f of fs.readdirSync(dir).filter((x) => x.endsWith(".json"))) {
    const id = f.replace(/\.json$/, "");
    const r = enqueueToPublishQueue(id, { from: "pending" });
    if (r.ok) ids.push(id);
  }
  const state = recomputeState({
    total: readPublishState().published + ids.length,
    started_at: readPublishState().started_at || nowIso(),
  });
  void state;
  return { moved: ids.length, ids };
}

/**
 * Publish exactly one knowledge row from the publish queue (backend unit of work).
 */
export function publishOne(): {
  ok: boolean;
  done: boolean;
  published?: FeedItem;
  message: string;
  state: PublishState;
} {
  const files = listPublishFiles();
  if (!files.length) {
    const state = recomputeState({
      status: "completed",
      current_knowledge: null,
      next_knowledge: null,
    });
    return { ok: true, done: true, message: "Queue empty", state };
  }

  const file = path.join(publishQueueDir(), files[0]);
  const raw = loadCandidateFromFile(file);
  if (!raw) {
    try {
      fs.unlinkSync(file);
    } catch {
      /* ignore */
    }
    return {
      ok: false,
      done: false,
      message: "Corrupt candidate removed",
      state: recomputeState(),
    };
  }

  const ts = nowIso();
  const name = String(raw.canonical_name || raw.entity_id || "Knowledge");
  const dataset = raw.target_dataset || "unknown";
  const conf = Number(raw.provenance?.confidence ?? 0.9);
  const source = String(
    raw.provenance?.source_id || raw.provenance?.source_url || "source"
  );

  recomputeState({
    status: "publishing",
    current_knowledge: name,
    current_dataset: dataset,
    started_at: readPublishState().started_at || ts,
  });

  let appended = false;
  const csvPath = resolveDatasetCsv(dataset);
  if (csvPath) {
    if (!entityAlreadyInCsv(csvPath, raw.entity_id)) {
      appendPayloadToCsv(csvPath, (raw.payload || {}) as Record<string, unknown>);
      appended = true;
      bumpDaily("knowledge_added", 1);
    } else {
      bumpDaily("knowledge_updated", 1);
    }
  }

  raw.provenance = {
    ...(raw.provenance || {}),
    validation_status: "approved",
    published_at: ts,
    reviewer: raw.provenance?.reviewer || "progressive-publisher",
  };
  raw.updated_at = ts;

  // Archive to approved
  const approvedDir = PATHS.queueApproved();
  fs.mkdirSync(approvedDir, { recursive: true });
  writeJson(path.join(approvedDir, `${raw.candidate_id}.json`), raw);
  fs.unlinkSync(file);

  const feedItem: FeedItem = {
    ts,
    knowledge_type: knowledgeType(raw),
    name,
    dataset,
    source,
    confidence: conf,
    candidate_id: raw.candidate_id,
    published_at: ts,
  };
  emitFeed(feedItem);
  emitJournal("Publishing", `Published · ${feedItem.knowledge_type} · ${name}`, {
    dataset,
    current_entity: name,
    confidence: conf,
    progress: null,
  });
  emitJournal(
    "Knowledge Added",
    `${feedItem.knowledge_type}: ${name}`,
    { dataset, current_entity: name, confidence: conf }
  );

  const prev = readPublishState();
  const state = recomputeState({
    published: Number(prev.published || 0) + 1,
    last_published_at: ts,
    current_knowledge: name,
    status: listPublishFiles().length ? "publishing" : "completed",
  });

  return {
    ok: true,
    done: listPublishFiles().length === 0,
    published: feedItem,
    message: appended
      ? `Published ${name} → ${dataset}`
      : `Confirmed ${name} in ${dataset}`,
    state,
  };
}

/**
 * Drain queue with backend delay (interval_ms). Blocks the calling process.
 */
export async function runProgressiveDrain(
  opts: { max?: number } = {}
): Promise<PublishState> {
  const mode = getLearningMode();
  const interval = mode.interval_ms;
  let n = 0;
  const max = opts.max ?? 10_000;

  recomputeState({
    status: "publishing",
    started_at: readPublishState().started_at || nowIso(),
    total:
      readPublishState().published + listPublishFiles().length ||
      listPublishFiles().length,
  });

  while (n < max) {
    const r = publishOne();
    n += 1;
    if (r.done) break;
    if (interval > 0) {
      await new Promise((res) => setTimeout(res, interval));
    }
  }

  emitJournal("Learning Completed", "Publish queue drained", {
    status: "completed",
  });
  return recomputeState({ status: "completed" });
}

export function readKnowledgeFeed(limit = 40): FeedItem[] {
  const p = knowledgeFeedPath();
  if (!fs.existsSync(p)) return [];
  const lines = fs.readFileSync(p, "utf8").split("\n").filter(Boolean);
  const out: FeedItem[] = [];
  for (const line of lines.slice(-limit).reverse()) {
    try {
      out.push(JSON.parse(line) as FeedItem);
    } catch {
      /* skip */
    }
  }
  return out;
}

export function readJournalTail(limit = 50): Array<Record<string, unknown>> {
  const p = repoPath("automation/learning/state/learning_journal.jsonl");
  if (!fs.existsSync(p)) return [];
  const lines = fs.readFileSync(p, "utf8").split("\n").filter(Boolean);
  const out: Array<Record<string, unknown>> = [];
  for (const line of lines.slice(-limit)) {
    try {
      out.push(JSON.parse(line));
    } catch {
      /* skip */
    }
  }
  return out;
}

/**
 * If auto-publish is on and enough backend time has elapsed since last row,
 * publish exactly one item. Rate limit lives here — not in the UI.
 */
export function maybeAutoPublishTick(): PublishState {
  const mode = getLearningMode();
  if (!mode.auto_publish) return recomputeState();
  if (mode.review_bypassed) autoEnqueuePending();

  const files = listPublishFiles();
  if (!files.length) return recomputeState({ status: "completed" });

  const prev = readPublishState();
  const interval = mode.interval_ms;
  if (interval > 0 && prev.last_published_at) {
    const last = Date.parse(prev.last_published_at);
    if (!Number.isNaN(last) && Date.now() - last < interval) {
      return recomputeState({ status: "publishing" });
    }
  }
  publishOne();
  return readPublishState();
}

export function getPublishDashboard(): PublishStateView {
  const mode = getLearningMode();
  // Never mutate FS on GET when the host is read-only (Vercel serverless).
  // Local dev: auto-move pending into publish queue + rate-limited tick.
  if (!isReadOnlyFs()) {
    try {
      if (mode.auto_publish) {
        maybeAutoPublishTick();
      } else {
        recomputeState();
      }
    } catch (e) {
      const err = e as NodeJS.ErrnoException;
      if (err?.code !== "EROFS" && err?.code !== "EACCES") throw e;
    }
  }

  // In-memory dashboard view (safe on read-only FS).
  const prev = readPublishState();
  const files = listPublishFiles();
  const remaining = files.length;
  const next = files[0]
    ? loadCandidateFromFile(path.join(publishQueueDir(), files[0]))
    : null;
  const speed = mode.publish_rate || 1;
  const state: PublishState = {
    ...prev,
    remaining,
    speed,
    unit: mode.publish_rate_unit,
    eta_seconds:
      remaining === 0 || speed <= 0 ? 0 : Math.ceil(remaining / speed),
    next_knowledge: next
      ? String(next.canonical_name || next.entity_id)
      : null,
    current_dataset: next?.target_dataset || prev.current_dataset,
    updated_at: nowIso(),
    mode: mode.mode,
    auto_publish: mode.auto_publish,
    total: Math.max(prev.total, prev.published + remaining),
    status:
      remaining > 0
        ? prev.status === "publishing"
          ? "publishing"
          : "idle"
        : prev.published > 0
          ? "completed"
          : "idle",
  };

  const queue = files.map((f) => {
    const c = loadCandidateFromFile(path.join(publishQueueDir(), f));
    return {
      candidate_id: c?.candidate_id || f.replace(/\.json$/, ""),
      name: String(c?.canonical_name || c?.entity_id || "—"),
      dataset: c?.target_dataset || "—",
      confidence: Number(c?.provenance?.confidence ?? 0),
    };
  });
  return {
    ...state,
    queue,
    feed: readKnowledgeFeed(30),
    journal_tail: readJournalTail(40),
  };
}
