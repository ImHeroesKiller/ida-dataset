/**
 * Trusted source health & production metrics (EPIC-1).
 * Reads registry + automation/learning/state/source_health.json
 */

import fs from "fs";
import { repoPath } from "./paths";
import { parseCsv } from "./csv";

export type SourceHealthRow = {
  source_id: string;
  name: string;
  category: string;
  trust_score: number;
  coverage: number;
  health_status: string;
  last_successful_sync: string | null;
  last_attempt: string | null;
  rows_produced: number;
  documents_processed: number;
  success_rate: number;
  failure_count: number;
  average_processing_time_ms: number;
  mission_usage: number;
  status: string;
  allowed: boolean;
  base_url: string;
  attempts: number;
  successes: number;
};

function readJson(p: string): Record<string, unknown> | null {
  try {
    if (!fs.existsSync(p)) return null;
    return JSON.parse(fs.readFileSync(p, "utf8"));
  } catch {
    return null;
  }
}

function emptyRow(id: string, name = "", category = ""): SourceHealthRow {
  return {
    source_id: id,
    name,
    category,
    trust_score: 0,
    coverage: 0,
    health_status: "unknown",
    last_successful_sync: null,
    last_attempt: null,
    rows_produced: 0,
    documents_processed: 0,
    success_rate: 0,
    failure_count: 0,
    average_processing_time_ms: 0,
    mission_usage: 0,
    status: "unknown",
    allowed: false,
    base_url: "",
    attempts: 0,
    successes: 0,
  };
}

/** Merge registry + health state for Sources operational view. */
export function getSourceHealthDashboard(): {
  updated_at: string | null;
  sources: SourceHealthRow[];
  totals: {
    registered: number;
    active: number;
    healthy: number;
    rows_produced: number;
    documents_processed: number;
  };
} {
  const regPath = repoPath("metadata/source_registry.csv");
  const healthPath = repoPath("automation/learning/state/source_health.json");

  let registry: Record<string, string>[] = [];
  if (fs.existsSync(regPath)) {
    registry = parseCsv(fs.readFileSync(regPath, "utf8")).rows;
  }

  const state = readJson(healthPath) || {};
  const metrics = (state.sources || {}) as Record<string, Record<string, unknown>>;

  // Lightweight attribution from industry library if metrics empty
  const industryPath = repoPath(
    "domains/business_development/industry_library.csv"
  );
  const producedBySource: Record<string, number> = {};
  if (fs.existsSync(industryPath)) {
    const { rows } = parseCsv(fs.readFileSync(industryPath, "utf8"));
    for (const row of rows) {
      const blob = `${row["Data Sources"] || ""} ${row.Notes || ""}`;
      const ids = blob.match(/SRC-\d{6}/g) || [];
      const names: string[] = [];
      const low = blob.toLowerCase();
      if (low.includes("bps")) names.push("SRC-000001");
      if (low.includes("world bank")) names.push("SRC-000004");
      if (low.includes("oecd")) names.push("SRC-000005");
      if (low.includes("ojk")) names.push("SRC-000010");
      if (low.includes("kemenperin") || low.includes("perindustrian"))
        names.push("SRC-000007");
      const all = [...new Set([...ids, ...names])];
      if (!all.length) continue;
      const share = 1 / all.length;
      for (const sid of all) {
        producedBySource[sid] = (producedBySource[sid] || 0) + share;
      }
    }
  }

  // Mission usage from missions dir
  const missionUsage: Record<string, number> = {};
  const missionsDir = repoPath("automation/missions/missions");
  if (fs.existsSync(missionsDir)) {
    for (const f of fs.readdirSync(missionsDir)) {
      if (!f.endsWith(".json")) continue;
      try {
        const m = JSON.parse(
          fs.readFileSync(`${missionsDir}/${f}`, "utf8")
        ) as { allowed_sources?: string[] };
        for (const sid of m.allowed_sources || []) {
          missionUsage[sid] = (missionUsage[sid] || 0) + 1;
        }
      } catch {
        /* skip */
      }
    }
  }

  const industryTotal = Math.max(
    1,
    Object.values(producedBySource).reduce((a, b) => a + b, 0) || 1
  );

  const sources: SourceHealthRow[] = registry.map((r) => {
    const id = r["Source ID"] || "";
    const m = metrics[id] || {};
    const allowed = String(r.Allowed || "").toLowerCase() === "true";
    const status = String(r.Status || m.status || "unknown").toLowerCase();
    const rowsProduced = Math.max(
      Number(m.rows_produced || 0),
      Math.round(producedBySource[id] || 0)
    );
    const attempts = Number(m.attempts || 0);
    const successes = Number(m.successes || 0);
    let health = String(m.health_status || "unknown");
    if (!allowed || status !== "active") health = "inactive";
    else if (health === "unknown" && rowsProduced > 0) health = "healthy";

    return {
      source_id: id,
      name: String(m.name || r["Source Name"] || id),
      category: String(m.category || r.Category || ""),
      trust_score: Number(m.trust_score ?? r["Trust Score"] ?? 0),
      coverage:
        Number(m.coverage || 0) ||
        (producedBySource[id]
          ? Math.round((producedBySource[id] / industryTotal) * 1000) / 1000
          : 0),
      health_status: health,
      last_successful_sync: (m.last_successful_sync as string) || null,
      last_attempt: (m.last_attempt as string) || null,
      rows_produced: rowsProduced,
      documents_processed: Number(m.documents_processed || 0),
      success_rate:
        Number(m.success_rate || 0) ||
        (attempts ? successes / attempts : rowsProduced > 0 ? 1 : 0),
      failure_count: Number(m.failure_count || 0),
      average_processing_time_ms: Number(m.average_processing_time_ms || 0),
      mission_usage: Math.max(
        Number(m.mission_usage || 0),
        missionUsage[id] || 0
      ),
      status,
      allowed,
      base_url: String(m.base_url || r["Base URL"] || ""),
      attempts,
      successes,
    };
  });

  const active = sources.filter((s) => s.allowed && s.status === "active");
  return {
    updated_at: (state.updated_at as string) || null,
    sources,
    totals: {
      registered: sources.length,
      active: active.length,
      healthy: sources.filter((s) => s.health_status === "healthy").length,
      rows_produced: sources.reduce((a, s) => a + s.rows_produced, 0),
      documents_processed: sources.reduce(
        (a, s) => a + s.documents_processed,
        0
      ),
    },
  };
}
