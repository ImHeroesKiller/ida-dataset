/**
 * Learning-first KPIs for the IDA Learning Dashboard.
 * Prioritizes knowledge metrics over framework/internal module stats.
 */

import fs from "fs";
import path from "path";
import { getRepoRoot, repoPath } from "./paths";
import { listDatasets, getReviewQueues } from "./repo-data";
import { parseCsv } from "./csv";

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

function parseConfidence(blob: string): number | null {
  const m = blob.match(/confidence=([0-9.]+)/i);
  if (!m) return null;
  const n = Number(m[1]);
  return Number.isFinite(n) ? n : null;
}

/** Industry Library metrics from the live CSV + knowledge cycle report. */
export function getIndustryLibraryMetrics() {
  const csvPath = repoPath("domains/business_development/industry_library.csv");
  const cycle = readJson(repoPath("reports/learning/knowledge_v1_industry_cycle.json"));
  let rows: Record<string, string>[] = [];
  let headers: string[] = [];
  if (fs.existsSync(csvPath)) {
    const text = fs.readFileSync(csvPath, "utf8");
    const parsed = parseCsv(text);
    headers = parsed.headers;
    rows = parsed.rows;
  }

  const confidences: number[] = [];
  let verified = 0;
  let fresh = 0;
  const today = new Date();
  const industries = rows.map((r) => {
    const filled = headers.filter((h) => String(r[h] || "").trim()).length;
    const coverage = headers.length ? filled / headers.length : 0;
    const ds = String(r["Data Sources"] || "");
    const notes = String(r["Notes"] || "");
    const conf = parseConfidence(`${notes} ${ds}`);
    if (conf != null) confidences.push(conf);
    const low = ds.toLowerCase();
    if (
      !low.includes("example.invalid") &&
      !low.includes("example.com") &&
      (ds.includes("SRC-") ||
        low.includes("bps.go.id") ||
        low.includes("worldbank") ||
        low.includes("oecd.org") ||
        low.includes("ojk.go.id"))
    ) {
      verified += 1;
    }
    const lu = String(r["Last Updated"] || "").slice(0, 10);
    if (/^\d{4}-\d{2}-\d{2}$/.test(lu)) {
      const d = new Date(lu + "T00:00:00Z");
      const days = (today.getTime() - d.getTime()) / 86400000;
      if (days <= 90) fresh += 1;
    }
    return {
      id: r["Industry ID"] || "",
      name: r["Industry Name"] || "",
      category: r["Industry Category"] || "",
      coverage,
      last_updated: lu,
      confidence: conf,
    };
  });

  const n = industries.length;
  const fieldCoverage =
    n > 0
      ? Math.round(
          (industries.reduce((s, i) => s + i.coverage, 0) / n) * 1000
        ) / 10
      : 0;
  const avgConf =
    confidences.length > 0
      ? Math.round(
          (confidences.reduce((a, b) => a + b, 0) / confidences.length) * 1000
        ) / 1000
      : null;

  // Phase-1 catalog target (EPIC-2A); stretch 100 tracked in reports
  const targetIndustries = 50;
  const coverageProgress = Math.min(
    100,
    Math.round((n / targetIndustries) * 1000) / 10
  );

  return {
    total_industries: n,
    field_coverage_pct: fieldCoverage,
    coverage_progress_pct: coverageProgress,
    target_industries: targetIndustries,
    rows_added: Number(cycle?.rows_added ?? 0),
    rows_updated: Number(cycle?.rows_updated ?? 0),
    duplicate_rate: Number(cycle?.duplicate_rate ?? 0),
    average_confidence: avgConf,
    verified_sources: verified,
    knowledge_freshness_pct:
      n > 0 ? Math.round((fresh / n) * 1000) / 10 : 0,
    industries,
    latest: industries.slice().reverse()[0] || null,
    dataset_version: "knowledge-v1.0",
    mission_id: String(cycle?.mission_id || "MIS-20260710-EXPAND-IND"),
    mission_title: String(
      cycle?.mission_title || "Expand Industry Library"
    ),
  };
}

export function getKnowledgeKpis() {
  const root = getRepoRoot();
  const datasets = listDatasets();
  const review = getReviewQueues();
  const daily = readJson(
    repoPath(
      `automation/learning/state/daily_${new Date().toISOString().slice(0, 10)}.json`
    )
  );
  const current = readJson(
    repoPath("automation/learning/state/current_snapshot.json")
  );
  const firstCycle = readJson(
    repoPath("reports/learning/first_knowledge_cycle.json")
  );
  const knowledgeCycle = readJson(
    repoPath("reports/learning/knowledge_v1_industry_cycle.json")
  );
  const industry = getIndustryLibraryMetrics();
  const activity = readJson(
    repoPath("automation/learning/state/live_activity.json")
  );

  // yesterday: latest snapshot not today
  const stateDir = repoPath("automation/learning/state");
  let yesterday: Record<string, unknown> | null = null;
  if (fs.existsSync(stateDir)) {
    const snaps = fs
      .readdirSync(stateDir)
      .filter((f) => f.startsWith("snapshot_") && f.endsWith(".json"))
      .sort()
      .reverse();
    const today = new Date().toISOString().slice(0, 10);
    for (const f of snaps) {
      if (f.includes(today)) continue;
      yesterday = readJson(path.join(stateDir, f));
      if (yesterday) break;
    }
  }

  const populated = datasets.filter((d) => !d.isPlaceholder).length;
  const gaps = datasets.filter((d) => d.isPlaceholder);
  const growing = datasets
    .filter((d) => d.rowCount > 0)
    .sort((a, b) => b.rowCount - a.rowCount);

  const rowsTotal =
    (current?.rows_total as number | undefined) ??
    datasets.reduce((s, d) => s + d.rowCount, 0);
  const priorRows = (yesterday?.rows_total as number | undefined) ?? rowsTotal;
  const deltaRows = rowsTotal - priorRows;
  const coverage =
    industry.coverage_progress_pct ||
    (current?.coverage_pct as number | undefined) ||
    (datasets.length
      ? Math.round((populated / datasets.length) * 1000) / 10
      : 0);

  const journal = listJsonl(
    repoPath("automation/learning/state/learning_journal.jsonl"),
    100
  );
  const docsIncoming = fs.existsSync(repoPath("automation/documents/incoming"))
    ? fs
        .readdirSync(repoPath("automation/documents/incoming"))
        .filter((f) => f.endsWith(".json")).length
    : 0;

  const recentlyLearned = industry.industries
    .slice()
    .reverse()
    .slice(0, 8)
    .map((d) => ({
      dataset: "industry_library",
      domain: "business_development",
      rows: 1,
      path: "domains/business_development/industry_library.csv",
      name: d.name,
      id: d.id,
    }));

  const addedToday = Number(
    daily?.knowledge_added ??
      (knowledgeCycle
        ? Number(knowledgeCycle.rows_added || 0) +
          Number(knowledgeCycle.rows_updated || 0)
        : firstCycle?.published
          ? 1
          : 0)
  );

  const qualityScore = Math.min(
    100,
    Math.round(
      industry.field_coverage_pct * 0.35 +
        Math.min(industry.total_industries, 20) * 2.5 +
        (industry.average_confidence || 0) * 30 +
        (industry.verified_sources > 0 ? 15 : 0) +
        (review.counts.pending === 0 ? 5 : 0)
    )
  );

  // Count active trusted sources from registry
  let sourcesCount = 0;
  try {
    const reg = repoPath("metadata/source_registry.csv");
    if (fs.existsSync(reg)) {
      const { rows } = parseCsv(fs.readFileSync(reg, "utf8"));
      sourcesCount = rows.filter(
        (r) =>
          String(r.Status || r.status || "").toLowerCase() === "active" &&
          String(r.Allowed || r.allowed || "").toLowerCase() === "true"
      ).length;
    }
  } catch {
    sourcesCount = 0;
  }

  const lastSessionDir = repoPath("automation/sessions");
  let lastSession: string | null = null;
  try {
    const idx = readJson(path.join(lastSessionDir, "index.json"));
    const sessions = (idx?.sessions as Array<Record<string, unknown>>) || [];
    if (sessions.length) {
      lastSession = String(
        sessions[0].session_id || sessions[0].id || ""
      );
    }
  } catch {
    lastSession = null;
  }

  return {
    philosophy: {
      focus: "Knowledge Growth",
      architecture: "Frozen — plug into existing systems only",
      principle: "Increase IDA Knowledge. Measure everything.",
    },
    knowledge_coverage: coverage,
    knowledge_growth_today: {
      delta_rows: deltaRows || addedToday,
      smarter_than_yesterday: deltaRows > 0 || addedToday > 0,
      message:
        addedToday > 0
          ? `+${addedToday} industry knowledge rows acquired/updated today`
          : deltaRows > 0
            ? `+${deltaRows} knowledge rows vs prior snapshot`
            : yesterday
              ? "No new rows since prior snapshot"
              : "Baseline snapshot established",
    },
    knowledge_added_today: addedToday,
    knowledge_updated_today: Number(
      daily?.knowledge_updated ?? knowledgeCycle?.rows_updated ?? 0
    ),
    knowledge_rejected: Number(daily?.knowledge_rejected ?? 0),
    pending_review: review.counts.pending,
    continuous_learning_status: "always_on",
    knowledge_confidence:
      industry.average_confidence ??
      (firstCycle?.published ? 0.86 : null),
    average_confidence: industry.average_confidence,
    dataset_coverage: {
      total: datasets.length,
      populated,
      gaps: gaps.length,
      rows_total: rowsTotal,
    },
    industry_library: industry,
    domain_coverage: Object.entries(
      datasets.reduce<Record<string, { total: number; populated: number }>>(
        (acc, d) => {
          acc[d.domain] = acc[d.domain] || { total: 0, populated: 0 };
          acc[d.domain].total += 1;
          if (!d.isPlaceholder) acc[d.domain].populated += 1;
          return acc;
        },
        {}
      )
    ).map(([domain, v]) => ({
      domain,
      total: v.total,
      populated: v.populated,
      coverage_pct: v.total ? Math.round((v.populated / v.total) * 100) : 0,
    })),
    growing_datasets: growing.map((d) => ({
      name: d.name,
      domain: d.domain,
      rows: d.rowCount,
      path: d.relativePath,
    })),
    knowledge_gaps: gaps.map((d) => ({
      name: d.name,
      domain: d.domain,
      path: d.relativePath,
    })),
    documents_processing: docsIncoming,
    recently_learned: recentlyLearned,
    learning_journal: journal,
    knowledge_quality_score: qualityScore,
    sources_count: sourcesCount,
    dataset_version: industry.dataset_version,
    last_successful_session: lastSession,
    current_source: String(
      (activity as Record<string, unknown> | null)?.current_source ||
        "SRC-000004 World Bank"
    ),
    current_document: String(
      (activity as Record<string, unknown> | null)?.current_document ||
        "DOC-WB-IEP-2025-06"
    ),
    current_mission: industry.mission_title,
    first_knowledge: firstCycle
      ? {
          learned: Boolean(firstCycle.published),
          industry_id: firstCycle.industry_id,
          industry_name: firstCycle.industry_name,
          mission_id: firstCycle.mission_id,
          dataset: firstCycle.dataset,
        }
      : { learned: industry.total_industries > 0 },
    answers: {
      how_much_knowledge: `${industry.total_industries} industries · ${industry.field_coverage_pct}% field coverage · ${industry.verified_sources} verified · ${coverage}% catalog progress`,
      learning_now:
        String((activity as Record<string, unknown> | null)?.current_task || "") ||
        (docsIncoming > 0
          ? `${docsIncoming} document(s) in queue`
          : industry.total_industries > 0
            ? `Continuous · Expand Industry Library (${industry.total_industries} industries)`
            : "Waiting for first learning cycle"),
      smarter_than_yesterday:
        addedToday > 0
          ? `Yes (+${addedToday} industry knowledge actions today)`
          : deltaRows > 0
            ? `Yes (+${deltaRows} rows)`
            : yesterday
              ? "No measurable growth yet today"
              : "Baseline set — compare from tomorrow",
      growing: [
        "industry_library",
        ...growing.map((d) => d.name).slice(0, 4),
      ],
      gaps: gaps.map((d) => d.name).slice(0, 8),
      pending_review: review.counts.pending,
      documents: docsIncoming,
    },
  };
}
