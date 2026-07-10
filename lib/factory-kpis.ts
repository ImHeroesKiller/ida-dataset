/**
 * Official Factory KPIs for IDA Dataset Factory v2.0.
 * Monitors dataset generation — not AI/engineering vanity metrics.
 */

import fs from "fs";
import path from "path";
import { repoPath } from "./paths";
import { listDatasets, getReviewQueues } from "./repo-data";
import { parseCsv } from "./csv";
import { getIndustryLibraryMetrics } from "./knowledge-kpis";

function readJson(p: string): Record<string, unknown> | null {
  try {
    if (!fs.existsSync(p)) return null;
    return JSON.parse(fs.readFileSync(p, "utf8"));
  } catch {
    return null;
  }
}

function listJsonl(p: string, limit = 80): Record<string, unknown>[] {
  if (!fs.existsSync(p)) return [];
  const lines = fs.readFileSync(p, "utf8").split("\n").filter(Boolean);
  const out: Record<string, unknown>[] = [];
  for (const line of lines.slice(-limit)) {
    try {
      out.push(JSON.parse(line));
    } catch {
      /* skip */
    }
  }
  return out;
}

function dayKey(d = new Date()): string {
  return d.toISOString().slice(0, 10);
}

function loadDaily(day: string): Record<string, number> {
  const j = readJson(repoPath(`automation/learning/state/daily_${day}.json`));
  if (!j) return { knowledge_added: 0, knowledge_updated: 0, knowledge_rejected: 0 };
  return {
    knowledge_added: Number(j.knowledge_added || 0),
    knowledge_updated: Number(j.knowledge_updated || 0),
    knowledge_rejected: Number(j.knowledge_rejected || 0),
  };
}

function sumDays(n: number): number {
  let total = 0;
  const now = new Date();
  for (let i = 0; i < n; i++) {
    const d = new Date(now);
    d.setUTCDate(d.getUTCDate() - i);
    total += loadDaily(dayKey(d)).knowledge_added + loadDaily(dayKey(d)).knowledge_updated;
  }
  return total;
}

function countExports(): number {
  const roots = [
    repoPath("exports"),
    repoPath("exports/jsonl"),
    repoPath("exports/parquet"),
    repoPath("exports/embeddings"),
    repoPath("reports/export"),
  ];
  let n = 0;
  for (const r of roots) {
    if (!fs.existsSync(r)) continue;
    for (const name of fs.readdirSync(r)) {
      if (name.startsWith(".")) continue;
      const full = path.join(r, name);
      try {
        if (fs.statSync(full).isFile()) n += 1;
      } catch {
        /* skip */
      }
    }
  }
  return n;
}

function countActiveSources(): number {
  try {
    const reg = repoPath("metadata/source_registry.csv");
    if (!fs.existsSync(reg)) return 0;
    const { rows } = parseCsv(fs.readFileSync(reg, "utf8"));
    return rows.filter(
      (r) =>
        String(r.Status || "").toLowerCase() === "active" &&
        String(r.Allowed || "").toLowerCase() === "true"
    ).length;
  } catch {
    return 0;
  }
}

function missionStats(): { total: number; success: number; rate: number } {
  const dir = repoPath("automation/missions/missions");
  if (!fs.existsSync(dir)) return { total: 0, success: 0, rate: 0 };
  let total = 0;
  let success = 0;
  for (const f of fs.readdirSync(dir)) {
    if (!f.endsWith(".json")) continue;
    total += 1;
    try {
      const m = JSON.parse(fs.readFileSync(path.join(dir, f), "utf8"));
      const st = String(m.status || "").toLowerCase();
      if (st === "completed" || st === "active" || Number(m.progress) >= 100) {
        success += 1;
      }
    } catch {
      /* skip */
    }
  }
  return {
    total,
    success,
    rate: total ? Math.round((success / total) * 1000) / 10 : 0,
  };
}

export type FactoryKpis = {
  factory_status: "idle" | "running" | "error";
  current_mission: string;
  current_activity: string;
  current_source: string;
  current_document: string;
  rows_added_today: number;
  rows_added_week: number;
  rows_added_month: number;
  datasets_updated: number;
  dataset_coverage: number;
  dataset_quality: number;
  average_confidence: number | null;
  duplicate_rate: number;
  schema_completeness: number;
  source_freshness: number;
  verified_sources: number;
  active_sources: number;
  mission_success_rate: number;
  exports_generated: number;
  export_status: string;
  pending_quality: number;
  total_datasets: number;
  populated_datasets: number;
  total_rows: number;
  total_industries: number;
  latest_industry: string | null;
  dataset_version: string;
  last_session: string | null;
  journal: Record<string, unknown>[];
  recent_activity: Array<{ ts: string; verb: string; detail: string }>;
  pipeline: string[];
};

export function getFactoryKpis(): FactoryKpis {
  const datasets = listDatasets();
  const review = getReviewQueues();
  const industry = getIndustryLibraryMetrics();
  const activity = readJson(repoPath("automation/learning/state/live_activity.json")) || {};
  const cycle = readJson(repoPath("reports/learning/knowledge_v1_industry_cycle.json"));
  const journal = listJsonl(
    repoPath("automation/learning/state/learning_journal.jsonl"),
    60
  );
  const feed = listJsonl(
    repoPath("automation/learning/state/knowledge_feed.jsonl"),
    30
  );

  const today = loadDaily(dayKey());
  const rowsToday =
    today.knowledge_added +
    today.knowledge_updated ||
    Number(cycle?.rows_added || 0) + Number(cycle?.rows_updated || 0);
  const rowsWeek = sumDays(7) || rowsToday;
  const rowsMonth = sumDays(30) || rowsWeek;

  const populated = datasets.filter((d) => !d.isPlaceholder).length;
  const totalRows = datasets.reduce((s, d) => s + d.rowCount, 0);
  const coverage =
    industry.coverage_progress_pct ||
    (datasets.length
      ? Math.round((populated / datasets.length) * 1000) / 10
      : 0);

  const quality = Math.min(
    100,
    Math.round(
      (industry.field_coverage_pct || 0) * 0.35 +
        (industry.average_confidence || 0) * 30 +
        (industry.verified_sources > 0 ? 20 : 0) +
        (review.counts.pending === 0 ? 10 : 0) +
        Math.min(industry.total_industries, 10) * 1.5
    )
  );

  const missions = missionStats();
  const exportsN = countExports();
  const statusRaw = String(activity.status || "idle").toLowerCase();
  const factory_status: FactoryKpis["factory_status"] =
    statusRaw === "running" || statusRaw === "error"
      ? (statusRaw as "running" | "error")
      : "idle";

  let lastSession: string | null = null;
  try {
    const idx = readJson(repoPath("automation/sessions/index.json"));
    const sessions = (idx?.sessions as Array<Record<string, unknown>>) || [];
    if (sessions[0]) {
      lastSession = String(sessions[0].session_id || sessions[0].id || "");
    }
  } catch {
    lastSession = null;
  }

  const recent = [...journal]
    .reverse()
    .slice(0, 20)
    .map((ev) => ({
      ts: String(ev.ts || ""),
      verb: String(ev.verb || ""),
      detail: String(ev.detail || ""),
    }));

  const latestFromFeed = feed.length
    ? String(feed[feed.length - 1]?.name || "")
    : null;

  return {
    factory_status,
    current_mission: String(
      activity.mission_id ||
        industry.mission_title ||
        "Expand Industry Library"
    ),
    current_activity: String(
      activity.current_task ||
        activity.current_thought ||
        "Factory idle — ready for next mission"
    ),
    current_source: String(activity.current_source || "—"),
    current_document: String(activity.current_document || "—"),
    rows_added_today: rowsToday,
    rows_added_week: rowsWeek,
    rows_added_month: rowsMonth,
    datasets_updated: populated,
    dataset_coverage: coverage,
    dataset_quality: quality,
    average_confidence: industry.average_confidence,
    duplicate_rate: Number(industry.duplicate_rate || 0),
    schema_completeness: industry.field_coverage_pct,
    source_freshness: industry.knowledge_freshness_pct,
    verified_sources: industry.verified_sources,
    active_sources: countActiveSources(),
    mission_success_rate: missions.rate,
    exports_generated: exportsN,
    export_status:
      exportsN > 0 ? `${exportsN} artifact(s) available` : "No exports yet — run export job",
    pending_quality: review.counts.pending,
    total_datasets: datasets.length,
    populated_datasets: populated,
    total_rows: totalRows,
    total_industries: industry.total_industries,
    latest_industry: industry.latest
      ? `${industry.latest.id} ${industry.latest.name}`
      : latestFromFeed,
    dataset_version: industry.dataset_version || "knowledge-v1.0",
    last_session: lastSession || String(activity.session_id || "") || null,
    journal,
    recent_activity: recent,
    pipeline: [
      "Mission",
      "Source Discovery",
      "Document Collection",
      "Extraction",
      "Normalization",
      "Validation",
      "Schema Mapping",
      "Append Dataset",
      "Quality Validation",
      "Export",
      "Dashboard Update",
    ],
  };
}
