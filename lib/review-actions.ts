/**
 * Human review actions: approve → publish, reject → archive.
 * Operates on automation/queue/{pending,approved,rejected}.
 */

import fs from "fs";
import path from "path";
import { getRepoRoot, PATHS, repoPath } from "@/lib/paths";
import { getReviewQueues, type CandidateSummary } from "@/lib/repo-data";

export type FullCandidate = {
  candidate_id: string;
  entity_type?: string;
  entity_id: string;
  target_dataset: string;
  canonical_name: string;
  payload: Record<string, unknown>;
  provenance: {
    source_id?: string;
    source_url?: string;
    retrieved_at?: string;
    confidence?: number;
    extraction_version?: string;
    validation_status?: string;
    reviewer?: string | null;
    published_at?: string | null;
  };
  rejection_reasons?: string[];
  metadata?: Record<string, unknown>;
  links?: Record<string, unknown>;
  created_at?: string;
  updated_at?: string;
  path?: string;
  queue?: "pending" | "approved" | "rejected";
};

function nowIso(): string {
  return new Date().toISOString().replace(/\.\d{3}Z$/, "Z");
}

function queueDirs() {
  return {
    pending: PATHS.queuePending(),
    approved: PATHS.queueApproved(),
    rejected: PATHS.queueRejected(),
  };
}

function findCandidateFile(
  candidateId: string
): { queue: "pending" | "approved" | "rejected"; path: string } | null {
  const dirs = queueDirs();
  for (const queue of ["pending", "approved", "rejected"] as const) {
    const p = path.join(dirs[queue], `${candidateId}.json`);
    if (fs.existsSync(p)) return { queue, path: p };
  }
  return null;
}

export function loadFullCandidate(candidateId: string): FullCandidate | null {
  const found = findCandidateFile(candidateId);
  if (!found) return null;
  try {
    const raw = JSON.parse(fs.readFileSync(found.path, "utf8")) as FullCandidate;
    return { ...raw, path: found.path, queue: found.queue };
  } catch {
    return null;
  }
}

export function listFullQueue(
  queue: "pending" | "approved" | "rejected"
): FullCandidate[] {
  const dir = queueDirs()[queue];
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".json") && f !== ".gitkeep")
    .sort()
    .map((f) => {
      try {
        const full = path.join(dir, f);
        const raw = JSON.parse(fs.readFileSync(full, "utf8")) as FullCandidate;
        return { ...raw, path: full, queue };
      } catch {
        return null;
      }
    })
    .filter(Boolean) as FullCandidate[];
}

function writeJson(file: string, data: unknown): void {
  const dir = path.dirname(file);
  fs.mkdirSync(dir, { recursive: true });
  const tmp = `${file}.tmp.${process.pid}`;
  fs.writeFileSync(tmp, JSON.stringify(data, null, 2) + "\n", "utf8");
  fs.renameSync(tmp, file);
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
  if (!fs.existsSync(domains)) return null;
  // shallow search
  const stack = [domains];
  while (stack.length) {
    const d = stack.pop()!;
    for (const name of fs.readdirSync(d)) {
      const full = path.join(d, name);
      const st = fs.statSync(full);
      if (st.isDirectory()) stack.push(full);
      else if (name === `${targetDataset}.csv`) return full;
    }
  }
  return preferred; // may not exist yet
}

function entityAlreadyInCsv(
  csvPath: string,
  entityId: string,
  idHeaderCandidates: string[]
): boolean {
  if (!fs.existsSync(csvPath)) return false;
  const text = fs.readFileSync(csvPath, "utf8");
  const lines = text.split(/\r?\n/).filter(Boolean);
  if (lines.length < 2) return false;
  const headers = lines[0].split(",").map((h) => h.replace(/^\uFEFF/, "").trim());
  let idIdx = -1;
  for (const cand of idHeaderCandidates) {
    idIdx = headers.findIndex((h) => h.toLowerCase() === cand.toLowerCase());
    if (idIdx >= 0) break;
  }
  if (idIdx < 0) {
    // fallback: any cell equals entity id
    return lines.slice(1).some((line) => line.includes(entityId));
  }
  for (const line of lines.slice(1)) {
    // naive CSV split sufficient for ID check
    const cols = line.split(",");
    if ((cols[idIdx] || "").replace(/^"|"$/g, "") === entityId) return true;
  }
  return false;
}

function csvEscape(value: string): string {
  if (/[",\n\r]/.test(value)) return `"${value.replace(/"/g, '""')}"`;
  return value;
}

function appendPayloadToCsv(
  csvPath: string,
  payload: Record<string, unknown>
): { ok: boolean; message: string; appended: boolean } {
  try {
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
      fs.writeFileSync(
        csvPath,
        headers.map(csvEscape).join(",") + "\n",
        "utf8"
      );
    }
    const row = headers
      .map((h) => csvEscape(String(payload[h] ?? "")))
      .join(",");
    fs.appendFileSync(csvPath, row + "\n", "utf8");
    return { ok: true, message: `Appended to ${path.basename(csvPath)}`, appended: true };
  } catch (e) {
    const err = e as NodeJS.ErrnoException;
    return {
      ok: false,
      message: err.message || "CSV append failed",
      appended: false,
    };
  }
}

export type ReviewActionResult = {
  ok: boolean;
  action: string;
  candidate_id: string;
  message: string;
  error_code?: string;
  published?: boolean;
  dataset?: string | null;
  queue?: string;
};

/**
 * Approve a pending candidate and publish append-only into the target dataset.
 */
export function approveAndPublish(
  candidateId: string,
  opts: { reviewer?: string; publish?: boolean } = {}
): ReviewActionResult {
  const found = findCandidateFile(candidateId);
  if (!found) {
    return {
      ok: false,
      action: "approve",
      candidate_id: candidateId,
      message: "Candidate not found",
      error_code: "NOT_FOUND",
    };
  }
  if (found.queue !== "pending") {
    return {
      ok: false,
      action: "approve",
      candidate_id: candidateId,
      message: `Candidate is in ${found.queue}, not pending`,
      error_code: "WRONG_QUEUE",
      queue: found.queue,
    };
  }

  try {
    const raw = JSON.parse(fs.readFileSync(found.path, "utf8")) as FullCandidate;
    const reviewer = opts.reviewer || "executive-reviewer";
    const publish = opts.publish !== false;
    const ts = nowIso();

    raw.provenance = {
      ...(raw.provenance || {}),
      validation_status: "approved",
      reviewer,
      published_at: publish ? ts : null,
    };
    raw.updated_at = ts;

    let published = false;
    let publishMsg = "Approved — publish skipped";
    const dataset = raw.target_dataset || "";

    if (publish && dataset) {
      const csvPath = resolveDatasetCsv(dataset);
      if (csvPath) {
        const idHints = [
          "Industry ID",
          "Entity ID",
          "ID",
          "Pain Point ID",
          "Solution ID",
          "Competitor ID",
          "Case Study ID",
          "Framework ID",
        ];
        const already = entityAlreadyInCsv(
          csvPath,
          raw.entity_id,
          idHints
        );
        if (already) {
          publishMsg = `Approved — ${raw.entity_id} already in ${dataset} (confirmed)`;
          published = false;
        } else {
          const res = appendPayloadToCsv(
            csvPath,
            (raw.payload || {}) as Record<string, unknown>
          );
          if (!res.ok) {
            return {
              ok: false,
              action: "approve",
              candidate_id: candidateId,
              message: `Approved state failed to publish: ${res.message}`,
              error_code: "PUBLISH_FAILED",
            };
          }
          published = res.appended;
          publishMsg = res.message;
          // daily counter best-effort
          try {
            const day = ts.slice(0, 10);
            const dailyPath = repoPath(
              `automation/learning/state/daily_${day}.json`
            );
            let daily: Record<string, number> = {};
            if (fs.existsSync(dailyPath)) {
              daily = JSON.parse(fs.readFileSync(dailyPath, "utf8"));
            }
            daily.knowledge_added = Number(daily.knowledge_added || 0) + 1;
            writeJson(dailyPath, daily);
          } catch {
            /* ignore */
          }
        }
      } else {
        publishMsg = "Approved — dataset CSV not found";
      }
    }

    const destDir = queueDirs().approved;
    fs.mkdirSync(destDir, { recursive: true });
    const dest = path.join(destDir, `${candidateId}.json`);
    writeJson(dest, raw);
    fs.unlinkSync(found.path);

    return {
      ok: true,
      action: "approve",
      candidate_id: candidateId,
      message: publishMsg,
      published,
      dataset: dataset || null,
      queue: "approved",
    };
  } catch (e) {
    const err = e as NodeJS.ErrnoException;
    return {
      ok: false,
      action: "approve",
      candidate_id: candidateId,
      message: err.message || "Approve failed",
      error_code:
        err.code === "EROFS" || err.code === "EACCES"
          ? "READ_ONLY_FS"
          : "APPROVE_FAILED",
    };
  }
}

/**
 * Reject a pending candidate and archive to rejected queue.
 */
export function rejectCandidate(
  candidateId: string,
  opts: { reviewer?: string; reason?: string } = {}
): ReviewActionResult {
  const found = findCandidateFile(candidateId);
  if (!found) {
    return {
      ok: false,
      action: "reject",
      candidate_id: candidateId,
      message: "Candidate not found",
      error_code: "NOT_FOUND",
    };
  }
  if (found.queue !== "pending") {
    return {
      ok: false,
      action: "reject",
      candidate_id: candidateId,
      message: `Candidate is in ${found.queue}, not pending`,
      error_code: "WRONG_QUEUE",
      queue: found.queue,
    };
  }

  try {
    const raw = JSON.parse(fs.readFileSync(found.path, "utf8")) as FullCandidate;
    const ts = nowIso();
    raw.provenance = {
      ...(raw.provenance || {}),
      validation_status: "rejected",
      reviewer: opts.reviewer || "executive-reviewer",
    };
    raw.rejection_reasons = [
      ...(raw.rejection_reasons || []),
      opts.reason || "Rejected by human reviewer",
    ];
    raw.updated_at = ts;

    const destDir = queueDirs().rejected;
    fs.mkdirSync(destDir, { recursive: true });
    const dest = path.join(destDir, `${candidateId}.json`);
    writeJson(dest, raw);
    fs.unlinkSync(found.path);

    try {
      const day = ts.slice(0, 10);
      const dailyPath = repoPath(`automation/learning/state/daily_${day}.json`);
      let daily: Record<string, number> = {};
      if (fs.existsSync(dailyPath)) {
        daily = JSON.parse(fs.readFileSync(dailyPath, "utf8"));
      }
      daily.knowledge_rejected = Number(daily.knowledge_rejected || 0) + 1;
      writeJson(dailyPath, daily);
    } catch {
      /* ignore */
    }

    return {
      ok: true,
      action: "reject",
      candidate_id: candidateId,
      message: "Rejected and archived",
      queue: "rejected",
    };
  } catch (e) {
    const err = e as NodeJS.ErrnoException;
    return {
      ok: false,
      action: "reject",
      candidate_id: candidateId,
      message: err.message || "Reject failed",
      error_code:
        err.code === "EROFS" || err.code === "EACCES"
          ? "READ_ONLY_FS"
          : "REJECT_FAILED",
    };
  }
}

export function getReviewDashboard() {
  const queues = getReviewQueues();
  const pendingFull = listFullQueue("pending");
  return {
    ...queues,
    pending_full: pendingFull,
    updated_at: nowIso(),
  };
}

export type { CandidateSummary };
