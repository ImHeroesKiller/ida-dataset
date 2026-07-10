/**
 * Factory KPIs — calibrated against product targets (not sprint milestones).
 * Observe-only: never mutates datasets.
 */

import fs from "fs";
import path from "path";
import { repoPath } from "./paths";
import { listDatasets, type DatasetInfo } from "./repo-data";
import { parseCsv } from "./csv";
import {
  loadProductTargets,
  productCoveragePct,
  productTargetFor,
} from "./product-targets";

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
    const day = loadDaily(dayKey(d));
    total += day.knowledge_added + day.knowledge_updated;
  }
  return total;
}

function countExports(): number {
  const roots = [
    repoPath("exports/jsonl"),
    repoPath("exports/parquet"),
    repoPath("exports/embeddings"),
    repoPath("exports/openai"),
    repoPath("exports/huggingface"),
    repoPath("reports/export"),
  ];
  let n = 0;
  for (const r of roots) {
    if (!fs.existsSync(r)) continue;
    for (const name of fs.readdirSync(r)) {
      if (name.startsWith(".")) continue;
      try {
        if (fs.statSync(path.join(r, name)).isFile()) n += 1;
      } catch {
        /* skip */
      }
    }
  }
  return n;
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
      if (
        st === "completed" ||
        st === "active" ||
        st === "superseded" ||
        Number(m.progress) >= 100
      ) {
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

function parseConfidence(blob: string): number | null {
  const m = blob.match(/confidence=([0-9.]+)/i);
  if (!m) return null;
  const n = Number(m[1]);
  return Number.isFinite(n) ? n : null;
}

function analyzeCsvFile(
  absolutePath: string,
  freshnessDays: number
): {
  schema_completeness: number;
  average_confidence: number | null;
  duplicate_rate: number;
  freshness: number;
} {
  if (!fs.existsSync(absolutePath)) {
    return {
      schema_completeness: 0,
      average_confidence: null,
      duplicate_rate: 0,
      freshness: 0,
    };
  }
  try {
    const { headers, rows } = parseCsv(fs.readFileSync(absolutePath, "utf8"));
    if (!rows.length) {
      return {
        schema_completeness: 0,
        average_confidence: null,
        duplicate_rate: 0,
        freshness: 0,
      };
    }
    let filled = 0;
    let cells = 0;
    const confidences: number[] = [];
    let fresh = 0;
    const today = Date.now();
    const ids: string[] = [];
    for (const r of rows) {
      for (const h of headers) {
        cells += 1;
        if (String(r[h] || "").trim()) filled += 1;
      }
      const conf = parseConfidence(
        `${r["Notes"] || ""} ${r["Data Sources"] || ""} ${r["Notes"] || ""}`
      );
      if (conf != null) confidences.push(conf);
      const lu = String(
        r["Last Updated"] || r["last_updated"] || r["Updated"] || ""
      ).slice(0, 10);
      if (/^\d{4}-\d{2}-\d{2}$/.test(lu)) {
        const age =
          (today - new Date(lu + "T00:00:00Z").getTime()) / 86400000;
        if (age <= freshnessDays) fresh += 1;
      }
      const id =
        r["Industry ID"] ||
        r["Company ID"] ||
        r["Product ID"] ||
        r["Pain ID"] ||
        r["Solution ID"] ||
        r["Competitor ID"] ||
        r["Opportunity ID"] ||
        r["Case ID"] ||
        r["Signal ID"] ||
        r["Framework ID"] ||
        Object.values(r)[0] ||
        "";
      if (id) ids.push(String(id).toLowerCase());
    }
    const uniq = new Set(ids);
    const dupRate =
      ids.length > 0
        ? Math.round(((ids.length - uniq.size) / ids.length) * 1000) / 1000
        : 0;
    return {
      schema_completeness:
        cells > 0 ? Math.round((filled / cells) * 1000) / 10 : 0,
      average_confidence:
        confidences.length > 0
          ? Math.round(
              (confidences.reduce((a, b) => a + b, 0) / confidences.length) *
                1000
            ) / 1000
          : null,
      duplicate_rate: dupRate,
      freshness:
        rows.length > 0
          ? Math.round((fresh / rows.length) * 1000) / 10
          : 0,
    };
  } catch {
    return {
      schema_completeness: 0,
      average_confidence: null,
      duplicate_rate: 0,
      freshness: 0,
    };
  }
}

/**
 * Readiness 0–100 from coverage, completeness, confidence, inverse dup, freshness.
 */
export function computeReadiness(parts: {
  coverage_pct: number;
  schema_completeness: number;
  average_confidence: number | null;
  duplicate_rate: number;
  freshness: number;
}): number {
  const conf =
    parts.average_confidence != null ? parts.average_confidence * 100 : 50;
  const dupPenalty = Math.min(100, parts.duplicate_rate * 100);
  const score =
    parts.coverage_pct * 0.25 +
    parts.schema_completeness * 0.25 +
    conf * 0.2 +
    (100 - dupPenalty) * 0.15 +
    parts.freshness * 0.15;
  return Math.max(0, Math.min(100, Math.round(score)));
}

export type DatasetReadiness = {
  name: string;
  domain: string;
  relativePath: string;
  current_rows: number;
  product_target: number;
  coverage_pct: number;
  coverage_label: string;
  schema_completeness: number;
  average_confidence: number | null;
  duplicate_rate: number;
  freshness: number;
  readiness: number;
  isPlaceholder: boolean;
};

export type FactoryCapacity = {
  average_rows_per_day: number;
  average_rows_per_session: number;
  estimated_completion: string;
  mission_throughput: number;
  lookback_days: number;
};

export type FactoryKpis = {
  factory_status: "idle" | "running" | "error";
  current_mission: string;
  current_activity: string;
  rows_added_today: number;
  rows_added_week: number;
  rows_added_month: number;
  /** Weighted product coverage across primary datasets (0–100). */
  dataset_coverage: number;
  /** Primary product coverage label e.g. "Industry 50 / 250 (20%)" */
  coverage_label: string;
  coverage_breakdown: Array<{
    name: string;
    current: number;
    target: number;
    pct: number;
  }>;
  dataset_readiness: number;
  average_confidence: number | null;
  duplicate_rate: number;
  freshness: number;
  mission_success_rate: number;
  exports_generated: number;
  capacity: FactoryCapacity;
  datasets: DatasetReadiness[];
  recent_activity: Array<{ ts: string; verb: string; detail: string }>;
  product_targets_version: string;
  /** Sprint milestones (informational — never product coverage denominator) */
  sprint_milestones: Record<string, number>;
  total_industries: number;
  industry_product_target: number;
};

function buildDatasetReadiness(
  datasets: DatasetInfo[],
  freshnessDays: number
): DatasetReadiness[] {
  return datasets.map((d) => {
    const target = productTargetFor(d.name);
    const analysis = analyzeCsvFile(d.absolutePath, freshnessDays);
    const cov = productCoveragePct(d.rowCount, target);
    const readiness = computeReadiness({
      coverage_pct: cov,
      schema_completeness: d.rowCount === 0 ? 0 : analysis.schema_completeness,
      average_confidence: analysis.average_confidence,
      duplicate_rate: analysis.duplicate_rate,
      freshness: d.rowCount === 0 ? 0 : analysis.freshness,
    });
    return {
      name: d.name,
      domain: d.domain,
      relativePath: d.relativePath,
      current_rows: d.rowCount,
      product_target: target,
      coverage_pct: cov,
      coverage_label: `${d.rowCount} / ${target}`,
      schema_completeness:
        d.rowCount === 0 ? 0 : analysis.schema_completeness,
      average_confidence: analysis.average_confidence,
      duplicate_rate: analysis.duplicate_rate,
      freshness: d.rowCount === 0 ? 0 : analysis.freshness,
      readiness: d.rowCount === 0 ? 0 : readiness,
      isPlaceholder: d.isPlaceholder,
    };
  });
}

function capacityMetrics(
  rowsMonth: number,
  lookbackDays: number
): FactoryCapacity {
  const avgDay =
    lookbackDays > 0
      ? Math.round((rowsMonth / Math.min(lookbackDays, 30)) * 10) / 10
      : 0;

  // sessions
  let sessionCount = 0;
  const sessionsDir = repoPath("automation/sessions");
  try {
    const idx = readJson(path.join(sessionsDir, "index.json"));
    const sessions = (idx?.sessions as unknown[]) || [];
    sessionCount = sessions.length;
    if (!sessionCount && fs.existsSync(sessionsDir)) {
      for (const d of fs.readdirSync(sessionsDir)) {
        const full = path.join(sessionsDir, d);
        if (fs.statSync(full).isDirectory()) {
          sessionCount += fs
            .readdirSync(full)
            .filter((f) => f.endsWith(".json")).length;
        }
      }
    }
  } catch {
    sessionCount = 0;
  }
  const avgSession =
    sessionCount > 0
      ? Math.round((rowsMonth / Math.max(sessionCount, 1)) * 10) / 10
      : rowsMonth > 0
        ? rowsMonth
        : 0;

  // Mission throughput: missions with progress/completed in window (count files)
  let missionFiles = 0;
  const mdir = repoPath("automation/missions/missions");
  if (fs.existsSync(mdir)) {
    missionFiles = fs.readdirSync(mdir).filter((f) => f.endsWith(".json")).length;
  }
  const throughput =
    lookbackDays > 0
      ? Math.round((missionFiles / Math.max(lookbackDays / 7, 1)) * 10) / 10
      : 0;

  // ETA for industry product target
  const industryRows =
    listDatasets().find((d) => d.name === "industry_library")?.rowCount || 0;
  const industryTarget = productTargetFor("industry_library");
  const remaining = Math.max(0, industryTarget - industryRows);
  let eta = "—";
  if (avgDay > 0 && remaining > 0) {
    const days = Math.ceil(remaining / avgDay);
    eta =
      days < 30
        ? `~${days} days to industry product target`
        : days < 365
          ? `~${Math.ceil(days / 30)} months to industry product target`
          : `~${Math.round((days / 365) * 10) / 10} years to industry product target`;
  } else if (remaining === 0) {
    eta = "Industry product target reached";
  } else {
    eta = "Insufficient throughput history for ETA";
  }

  return {
    average_rows_per_day: avgDay,
    average_rows_per_session: avgSession,
    estimated_completion: eta,
    mission_throughput: throughput,
    lookback_days: lookbackDays,
  };
}

export function getFactoryKpis(): FactoryKpis {
  const cfg = loadProductTargets();
  const datasets = listDatasets();
  const activity =
    readJson(repoPath("automation/learning/state/live_activity.json")) || {};
  const journal = listJsonl(
    repoPath("automation/learning/state/learning_journal.jsonl"),
    60
  );

  const today = loadDaily(dayKey());
  let rowsToday = today.knowledge_added + today.knowledge_updated;
  // Prefer explicit daily; fall back to expansion report if daily empty today
  if (!rowsToday) {
    const epic = readJson(
      repoPath("reports/learning/epic2a_industry_expansion.json")
    );
    if (epic?.retrieved_at && String(epic.retrieved_at).startsWith(dayKey())) {
      rowsToday = Number(epic.rows_added || 0);
    }
  }
  const rowsWeek = sumDays(7) || rowsToday;
  const rowsMonth = sumDays(30) || rowsWeek;

  const readinessList = buildDatasetReadiness(
    datasets,
    cfg.freshness_window_days
  );

  // Product coverage: weighted by target size among non-empty OR primary libraries
  const primary = readinessList.filter(
    (d) =>
      !d.name.includes("guidance") &&
      (d.current_rows > 0 ||
        [
          "industry_library",
          "company_profile",
          "product_catalog",
          "pain_point_library",
          "solution_library",
          "competitor_library",
          "case_study_library",
          "framework_library",
          "opportunity_analysis",
          "business_signal_library",
        ].includes(d.name))
  );
  let weighted = 0;
  let weightSum = 0;
  for (const d of primary) {
    const w = d.product_target;
    weighted += d.coverage_pct * w;
    weightSum += w;
  }
  const datasetCoverage =
    weightSum > 0 ? Math.round((weighted / weightSum) * 10) / 10 : 0;

  const industry = readinessList.find((d) => d.name === "industry_library");
  const coverageLabel = industry
    ? `Industry ${industry.current_rows} / ${industry.product_target} (${industry.coverage_pct}%)`
    : `${datasetCoverage}% product coverage`;

  const coverageBreakdown = readinessList
    .filter((d) => d.current_rows > 0 || d.name === "industry_library")
    .slice(0, 12)
    .map((d) => ({
      name: d.name,
      current: d.current_rows,
      target: d.product_target,
      pct: d.coverage_pct,
    }));

  // Aggregate readiness / confidence / dup / freshness across datasets with rows
  const withRows = readinessList.filter((d) => d.current_rows > 0);
  const datasetReadiness =
    withRows.length > 0
      ? Math.round(
          withRows.reduce((s, d) => s + d.readiness, 0) / withRows.length
        )
      : 0;
  const confs = withRows
    .map((d) => d.average_confidence)
    .filter((c): c is number => c != null);
  const avgConf =
    confs.length > 0
      ? Math.round((confs.reduce((a, b) => a + b, 0) / confs.length) * 1000) /
        1000
      : null;
  const dupRate =
    withRows.length > 0
      ? Math.round(
          (withRows.reduce((s, d) => s + d.duplicate_rate, 0) /
            withRows.length) *
            1000
        ) / 1000
      : 0;
  const freshness =
    withRows.length > 0
      ? Math.round(
          withRows.reduce((s, d) => s + d.freshness, 0) / withRows.length
        )
      : 0;

  const missions = missionStats();
  const exportsN = countExports();
  const statusRaw = String(activity.status || "idle").toLowerCase();
  const factory_status: FactoryKpis["factory_status"] =
    statusRaw === "running" || statusRaw === "error"
      ? (statusRaw as "running" | "error")
      : "idle";

  const recent = [...journal]
    .reverse()
    .slice(0, 20)
    .map((ev) => ({
      ts: String(ev.ts || ""),
      verb: String(ev.verb || ""),
      detail: String(ev.detail || ""),
    }));

  const capacity = capacityMetrics(
    rowsMonth,
    cfg.capacity.lookback_days
  );

  return {
    factory_status,
    current_mission: String(
      activity.mission_id ||
        activity.current_task ||
        "Produce Industry Dataset"
    ),
    current_activity: String(
      activity.current_task ||
        activity.current_thought ||
        "Factory idle — ready for next mission"
    ),
    rows_added_today: rowsToday,
    rows_added_week: rowsWeek,
    rows_added_month: rowsMonth,
    dataset_coverage: industry?.coverage_pct ?? datasetCoverage,
    coverage_label: coverageLabel,
    coverage_breakdown: coverageBreakdown,
    dataset_readiness: industry?.readiness ?? datasetReadiness,
    average_confidence: industry?.average_confidence ?? avgConf,
    duplicate_rate: industry?.duplicate_rate ?? dupRate,
    freshness: industry?.freshness ?? freshness,
    mission_success_rate: missions.rate,
    exports_generated: exportsN,
    capacity,
    datasets: readinessList,
    recent_activity: recent,
    product_targets_version: cfg.version,
    sprint_milestones: cfg.sprint_milestones,
    total_industries: industry?.current_rows ?? 0,
    industry_product_target: productTargetFor("industry_library"),
  };
}
