/** Server bridge to IDA Knowledge Network (connectors). */

import fs from "fs";
import path from "path";
import { spawnSync } from "child_process";
import { getRepoRoot, repoPath } from "./paths";

function readJson(p: string): unknown {
  try {
    if (!fs.existsSync(p)) return null;
    return JSON.parse(fs.readFileSync(p, "utf8"));
  } catch {
    return null;
  }
}

function listDocs(dir: string): Record<string, unknown>[] {
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".json"))
    .sort()
    .map((f) => {
      const data = readJson(path.join(dir, f));
      return (data && typeof data === "object" ? data : { file: f }) as Record<
        string,
        unknown
      >;
    });
}

export function runNetworkCli(args: string[]) {
  const root = getRepoRoot();
  if (process.env.VERCEL || process.env.ECC_DISABLE_PYTHON === "1") {
    return { ok: false, data: null as unknown, stderr: "CLI unavailable" };
  }
  const result = spawnSync("python3", ["-m", "automation.connectors", ...args], {
    cwd: root,
    encoding: "utf8",
    maxBuffer: 4 * 1024 * 1024,
  });
  let data: unknown = null;
  try {
    data = result.stdout ? JSON.parse(result.stdout) : null;
  } catch {
    data = { raw: result.stdout };
  }
  return {
    ok: result.status === 0,
    data,
    stderr: (result.stderr || "").trim(),
  };
}

export function runSearchCli(query: string, limit = 5) {
  const root = getRepoRoot();
  if (process.env.VERCEL || process.env.ECC_DISABLE_PYTHON === "1") {
    return { ok: false, data: null as unknown, stderr: "CLI unavailable" };
  }
  const result = spawnSync(
    "python3",
    ["-m", "automation.search", query, "--limit", String(limit)],
    { cwd: root, encoding: "utf8", maxBuffer: 4 * 1024 * 1024 }
  );
  let data: unknown = null;
  try {
    data = result.stdout ? JSON.parse(result.stdout) : null;
  } catch {
    data = { raw: result.stdout };
  }
  return {
    ok: result.status === 0,
    data,
    stderr: (result.stderr || "").trim(),
  };
}

export function getNetworkDashboard() {
  const live = runNetworkCli(["dashboard"]);
  if (live.ok && live.data && typeof live.data === "object") {
    return live.data as Record<string, unknown>;
  }

  // File fallback
  const metrics = readJson(
    repoPath("automation/connectors/cache/metrics.json")
  ) as Record<string, unknown> | null;
  const eventsPath = repoPath("automation/connectors/cache/events.jsonl");
  let events: unknown[] = [];
  if (fs.existsSync(eventsPath)) {
    events = fs
      .readFileSync(eventsPath, "utf8")
      .split("\n")
      .filter(Boolean)
      .slice(-50)
      .map((l) => {
        try {
          return JSON.parse(l);
        } catch {
          return { detail: l };
        }
      });
  }

  const queue = {
    incoming: listDocs(repoPath("automation/documents/incoming")).length,
    processing: listDocs(repoPath("automation/documents/processing")).length,
    processed: listDocs(repoPath("automation/documents/processed")).length,
    failed: listDocs(repoPath("automation/documents/failed")).length,
  };

  return {
    updated_at: new Date().toISOString(),
    enabled: true,
    connectors: [],
    queue: {
      counts: queue,
      queue_length: Object.values(queue).reduce((a, b) => a + b, 0),
      incoming: listDocs(repoPath("automation/documents/incoming")).slice(0, 20),
    },
    metrics: metrics || { totals: {} },
    events,
    source: live.ok ? "cli" : "files",
    waiting_message:
      events.length === 0 ? "Waiting for first execution" : null,
  };
}

export function listQueuedDocuments() {
  return {
    incoming: listDocs(repoPath("automation/documents/incoming")),
    processing: listDocs(repoPath("automation/documents/processing")),
    processed: listDocs(repoPath("automation/documents/processed")),
    failed: listDocs(repoPath("automation/documents/failed")),
  };
}

export function listSourcesCsv() {
  const p = repoPath("metadata/source_registry.csv");
  if (!fs.existsSync(p)) return [];
  const text = fs.readFileSync(p, "utf8");
  const lines = text.replace(/^\uFEFF/, "").split(/\n/).filter(Boolean);
  if (lines.length < 2) return [];
  const headers = lines[0].split(",");
  return lines.slice(1).map((line) => {
    const cols = line.split(",");
    const row: Record<string, string> = {};
    headers.forEach((h, i) => {
      row[h.trim()] = (cols[i] || "").trim();
    });
    return row;
  });
}
