/**
 * Learning-first KPIs for the IDA Learning Dashboard.
 * Prioritizes knowledge metrics over framework/internal module stats.
 */

import fs from "fs";
import path from "path";
import { getRepoRoot, repoPath } from "./paths";
import { listDatasets, getReviewQueues } from "./repo-data";

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
    (current?.coverage_pct as number | undefined) ??
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

  // recently learned = non-placeholder rows summary
  const recentlyLearned = growing.slice(0, 8).map((d) => ({
    dataset: d.name,
    domain: d.domain,
    rows: d.rowCount,
    path: d.relativePath,
  }));

  const qualityScore = Math.min(
    100,
    Math.round(
      coverage * 0.5 +
        Math.min(rowsTotal, 50) * 0.8 +
        (firstCycle?.published ? 20 : 0) +
        (review.counts.pending === 0 ? 5 : 0)
    )
  );

  return {
    philosophy: {
      focus: "Knowledge Growth",
      architecture: "Frozen — plug into existing systems only",
      principle: "Increase IDA Knowledge. Measure everything.",
    },
    knowledge_coverage: coverage,
    knowledge_growth_today: {
      delta_rows: deltaRows,
      smarter_than_yesterday: deltaRows > 0,
      message:
        deltaRows > 0
          ? `+${deltaRows} knowledge rows vs prior snapshot`
          : yesterday
            ? "No new rows since prior snapshot"
            : "Baseline snapshot established",
    },
    knowledge_added_today: Number(daily?.knowledge_added ?? (firstCycle?.published ? 1 : 0)),
    knowledge_updated_today: Number(daily?.knowledge_updated ?? 0),
    knowledge_rejected: Number(daily?.knowledge_rejected ?? 0),
    pending_review: review.counts.pending,
    continuous_learning_status: "always_on",
    knowledge_confidence: firstCycle?.published ? 0.86 : null,
    dataset_coverage: {
      total: datasets.length,
      populated,
      gaps: gaps.length,
      rows_total: rowsTotal,
    },
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
    first_knowledge: firstCycle
      ? {
          learned: Boolean(firstCycle.published),
          industry_id: firstCycle.industry_id,
          industry_name: firstCycle.industry_name,
          mission_id: firstCycle.mission_id,
          dataset: firstCycle.dataset,
        }
      : { learned: false },
    answers: {
      how_much_knowledge: `${populated}/${datasets.length} datasets · ${rowsTotal} rows · ${coverage}% coverage`,
      learning_now:
        docsIncoming > 0
          ? `${docsIncoming} document(s) in queue`
          : firstCycle?.published
            ? "Continuous learning active — scanning gaps"
            : "Waiting for first learning cycle",
      smarter_than_yesterday:
        deltaRows > 0
          ? `Yes (+${deltaRows} rows)`
          : yesterday
            ? "No measurable growth yet today"
            : "Baseline set — compare from tomorrow",
      growing: growing.map((d) => d.name).slice(0, 5),
      gaps: gaps.map((d) => d.name).slice(0, 8),
      pending_review: review.counts.pending,
      documents: docsIncoming,
    },
  };
}
