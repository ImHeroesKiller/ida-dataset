import fs from "fs";
import path from "path";
import { execSync } from "child_process";
import { listCsvFiles, readCsvFile, type CsvTable } from "./csv";
import { PATHS, getRepoRoot, repoPath } from "./paths";
import { loadSimpleYaml } from "./simple-yaml";
import type { ModuleStatus } from "./status";
import { statusFromCounts } from "./status";

const WAITING = "Waiting for first execution";

export type DatasetInfo = {
  id: string;
  name: string;
  domain: string;
  relativePath: string;
  absolutePath: string;
  rowCount: number;
  columnCount: number;
  isPlaceholder: boolean;
  headers: string[];
};

export type CandidateSummary = {
  candidate_id: string;
  entity_id: string;
  target_dataset: string;
  canonical_name: string;
  confidence: number;
  source_id: string;
  validation_status: string;
  reviewer?: string | null;
  path: string;
};

function safeRead(filePath: string): string | null {
  try {
    if (!fs.existsSync(filePath)) return null;
    return fs.readFileSync(filePath, "utf8");
  } catch {
    return null;
  }
}

function listJsonCandidates(dir: string): CandidateSummary[] {
  if (!fs.existsSync(dir)) return [];
  const files = fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".json") && f !== ".gitkeep")
    .sort();
  const out: CandidateSummary[] = [];
  for (const file of files) {
    const full = path.join(dir, file);
    try {
      const raw = JSON.parse(fs.readFileSync(full, "utf8"));
      out.push({
        candidate_id: raw.candidate_id ?? file.replace(/\.json$/, ""),
        entity_id: raw.entity_id ?? "",
        target_dataset: raw.target_dataset ?? "",
        canonical_name: raw.canonical_name ?? "",
        confidence: Number(raw.provenance?.confidence ?? 0),
        source_id: raw.provenance?.source_id ?? "",
        validation_status: raw.provenance?.validation_status ?? "pending",
        reviewer: raw.provenance?.reviewer ?? null,
        path: full,
      });
    } catch {
      // skip invalid
    }
  }
  return out;
}

export function getVersion(): string {
  return (safeRead(PATHS.version()) ?? "unknown").trim();
}

export function listDatasets(): DatasetInfo[] {
  const root = getRepoRoot();
  const domainRoot = PATHS.domains();
  const files = listCsvFiles(domainRoot, true);
  return files.map((abs) => {
    const rel = path.relative(root, abs).replace(/\\/g, "/");
    const parts = rel.split("/");
    const domain = parts[1] ?? "unknown";
    const name = path.basename(abs, ".csv");
    const table = readCsvFile(abs);
    return {
      id: rel,
      name,
      domain,
      relativePath: rel,
      absolutePath: abs,
      rowCount: table.rowCount,
      columnCount: table.headers.length,
      isPlaceholder: table.rowCount === 0,
      headers: table.headers,
    };
  });
}

export function readDataset(relativeOrAbs: string, limit = 100): CsvTable & {
  relativePath: string;
  previewRows: Record<string, string>[];
} {
  const root = getRepoRoot();
  const abs = path.isAbsolute(relativeOrAbs)
    ? relativeOrAbs
    : path.join(root, relativeOrAbs);
  const table = readCsvFile(abs);
  return {
    ...table,
    relativePath: path.relative(root, abs).replace(/\\/g, "/"),
    previewRows: table.rows.slice(0, limit),
  };
}

export function getOntologyBundle() {
  const dir = PATHS.ontology();
  const files = [
    "entities.csv",
    "entity_types.csv",
    "entity_properties.csv",
    "entity_synonyms.csv",
    "entity_aliases.csv",
    "relationships.csv",
    "relationship_types.csv",
    "relationship_rules.csv",
    "categories.csv",
    "domains.csv",
  ];
  const tables: Record<string, CsvTable> = {};
  for (const f of files) {
    tables[f] = readCsvFile(path.join(dir, f));
  }
  let version: Record<string, unknown> | null = null;
  const versionPath = path.join(dir, "ontology_version.json");
  const raw = safeRead(versionPath);
  if (raw) {
    try {
      version = JSON.parse(raw);
    } catch {
      version = null;
    }
  }
  return { tables, version, waiting: !version };
}

export function getPolicies() {
  const raw = safeRead(PATHS.policies());
  if (!raw) {
    return { exists: false, data: null as Record<string, unknown> | null, waiting: true };
  }
  try {
    const data = loadSimpleYaml(raw) as Record<string, unknown>;
    return { exists: true, data, waiting: false };
  } catch (err) {
    return {
      exists: true,
      data: null,
      waiting: false,
      error: err instanceof Error ? err.message : "Failed to parse policies",
    };
  }
}

export function getSources() {
  const raw = safeRead(PATHS.sources());
  if (!raw) return { exists: false, data: null as Record<string, unknown> | null };
  try {
    return { exists: true, data: loadSimpleYaml(raw) as Record<string, unknown> };
  } catch {
    return { exists: false, data: null };
  }
}

export function getReviewQueues() {
  const pending = listJsonCandidates(PATHS.queuePending());
  const approved = listJsonCandidates(PATHS.queueApproved());
  const rejected = listJsonCandidates(PATHS.queueRejected());
  return {
    pending,
    approved,
    rejected,
    counts: {
      pending: pending.length,
      approved: approved.length,
      rejected: rejected.length,
    },
    waiting: pending.length + approved.length + rejected.length === 0,
  };
}

export function listReports() {
  const root = PATHS.reports();
  const kinds = ["validation", "planner", "review", "publish"] as const;
  const items: {
    kind: string;
    name: string;
    relativePath: string;
    absolutePath: string;
    mtime: string | null;
    size: number;
  }[] = [];

  for (const kind of kinds) {
    const dir = path.join(root, kind);
    if (!fs.existsSync(dir)) continue;
    for (const name of fs.readdirSync(dir)) {
      if (name === ".gitkeep") continue;
      const abs = path.join(dir, name);
      if (!fs.statSync(abs).isFile()) continue;
      const st = fs.statSync(abs);
      items.push({
        kind,
        name,
        relativePath: path.relative(getRepoRoot(), abs).replace(/\\/g, "/"),
        absolutePath: abs,
        mtime: st.mtime.toISOString(),
        size: st.size,
      });
    }
  }
  items.sort((a, b) => (b.mtime ?? "").localeCompare(a.mtime ?? ""));
  return {
    items,
    waiting: items.length === 0,
    message: items.length === 0 ? WAITING : null,
  };
}

export function readReport(relativePath: string): {
  content: string | null;
  error?: string;
  relativePath: string;
} {
  const abs = repoPath(relativePath);
  const root = getRepoRoot();
  if (!abs.startsWith(root) || !abs.includes(`${path.sep}reports${path.sep}`)) {
    return { content: null, error: "Invalid report path", relativePath };
  }
  const content = safeRead(abs);
  if (content === null) return { content: null, error: "Not found", relativePath };
  return { content, relativePath };
}

export function getGitStatus() {
  const root = getRepoRoot();
  try {
    const branch = execSync("git rev-parse --abbrev-ref HEAD", {
      cwd: root,
      encoding: "utf8",
    }).trim();
    const short = execSync("git rev-parse --short HEAD", {
      cwd: root,
      encoding: "utf8",
    }).trim();
    const status = execSync("git status --porcelain", {
      cwd: root,
      encoding: "utf8",
    }).trim();
    const log = execSync("git log -5 --oneline", {
      cwd: root,
      encoding: "utf8",
    }).trim();
    return {
      available: true,
      branch,
      commit: short,
      dirty: status.length > 0,
      statusLines: status ? status.split("\n") : [],
      recentCommits: log ? log.split("\n") : [],
    };
  } catch {
    return {
      available: false,
      branch: null,
      commit: null,
      dirty: false,
      statusLines: [] as string[],
      recentCommits: [] as string[],
      message: WAITING,
    };
  }
}

export function buildPlannerView() {
  const datasets = listDatasets();
  const threshold = 5;
  const plans = datasets.map((d) => {
    const coverage =
      d.rowCount <= 0 ? 0 : Math.min(100, Math.round((d.rowCount / threshold) * 100));
    const gap = Math.max(0, threshold - d.rowCount);
    const priority =
      d.isPlaceholder ? 0.9 : d.rowCount < threshold ? 0.6 : 0.2;
    return {
      dataset: d.name,
      domain: d.domain,
      path: d.relativePath,
      rows: d.rowCount,
      targetRows: threshold,
      coverage,
      gap,
      priority: Number(priority.toFixed(2)),
      isPlaceholder: d.isPlaceholder,
      suggestedAction: d.isPlaceholder
        ? "Populate via KAS review queue (human-approved)"
        : gap > 0
          ? "Expand coverage under Planner + Policy"
          : "Maintain and validate",
    };
  });
  plans.sort((a, b) => b.priority - a.priority);
  return {
    datasets: plans,
    summary: {
      total: datasets.length,
      placeholders: datasets.filter((d) => d.isPlaceholder).length,
      populated: datasets.filter((d) => !d.isPlaceholder).length,
    },
    waiting: datasets.length === 0,
    message: datasets.length === 0 ? WAITING : null,
    architectureNote:
      "Planner proposes. Policy governs. Human decides. Pipeline executes. Publisher publishes.",
  };
}

export function buildDashboardSnapshot() {
  const datasets = listDatasets();
  const ontology = getOntologyBundle();
  const policies = getPolicies();
  const review = getReviewQueues();
  const reports = listReports();
  const git = getGitStatus();
  const version = getVersion();

  const populated = datasets.filter((d) => !d.isPlaceholder).length;
  const coveragePct =
    datasets.length === 0 ? 0 : Math.round((populated / datasets.length) * 100);

  const policyFeatures = (policies.data?.features ?? {}) as Record<string, boolean>;
  const publishingEnabled = Boolean(policyFeatures.publishing_enabled);
  const reviewRequired = Boolean(policies.data?.review_required ?? true);

  const modules: {
    key: string;
    label: string;
    status: ModuleStatus;
    detail: string;
  }[] = [
    {
      key: "coverage",
      label: "Knowledge Coverage",
      status: statusFromCounts({ hasData: populated > 0 }),
      detail:
        datasets.length === 0
          ? WAITING
          : `${populated}/${datasets.length} datasets populated (${coveragePct}%)`,
    },
    {
      key: "health",
      label: "Dataset Health",
      status: statusFromCounts({
        hasData: datasets.length > 0,
        error: datasets.some((d) => d.columnCount === 0),
      }),
      detail:
        datasets.length === 0
          ? WAITING
          : `${datasets.filter((d) => d.isPlaceholder).length} placeholder, ${populated} with rows`,
    },
    {
      key: "reviews",
      label: "Pending Reviews",
      status: review.waiting
        ? "waiting"
        : statusFromCounts({ hasData: true }),
      detail: review.waiting
        ? WAITING
        : `${review.counts.pending} pending · ${review.counts.approved} approved · ${review.counts.rejected} rejected`,
    },
    {
      key: "planner",
      label: "Today's Plans",
      status: statusFromCounts({ hasData: datasets.length > 0 }),
      detail:
        datasets.length === 0
          ? WAITING
          : `${datasets.filter((d) => d.isPlaceholder || d.rowCount < 5).length} gap-focused plan items`,
    },
    {
      key: "validation",
      label: "Validation Status",
      status: statusFromCounts({
        hasData: reports.items.some((r) => r.kind === "validation"),
      }),
      detail: reports.items.some((r) => r.kind === "validation")
        ? `Latest: ${reports.items.find((r) => r.kind === "validation")?.name}`
        : WAITING,
    },
    {
      key: "publisher",
      label: "Publisher Status",
      status: publishingEnabled
        ? statusFromCounts({ hasData: review.counts.approved > 0 })
        : "disabled",
      detail: publishingEnabled
        ? review.counts.approved > 0
          ? `${review.counts.approved} approved candidates ready`
          : WAITING
        : "Publishing disabled by policy",
    },
    {
      key: "policy",
      label: "Policy Status",
      status: policies.exists ? "healthy" : "waiting",
      detail: policies.exists
        ? `review_required=${reviewRequired} · crawl=${Boolean(policyFeatures.crawling_enabled)} · extract=${Boolean(policyFeatures.extraction_enabled)} · publish=${publishingEnabled}`
        : WAITING,
    },
    {
      key: "ontology",
      label: "Ontology Status",
      status: ontology.version ? "healthy" : "waiting",
      detail: ontology.version
        ? `v${String((ontology.version as { version?: string }).version ?? "?")} · ${ontology.tables["entities.csv"]?.rowCount ?? 0} entities`
        : WAITING,
    },
    {
      key: "repo",
      label: "Repository Status",
      status: "healthy",
      detail: `VERSION ${version} · root ready`,
    },
    {
      key: "git",
      label: "Git Status",
      status: git.available ? (git.dirty ? "waiting" : "healthy") : "waiting",
      detail: git.available
        ? `${git.branch}@${git.commit}${git.dirty ? " (dirty)" : " (clean)"}`
        : WAITING,
    },
  ];

  // Fix pending reviews status when waiting
  const reviewsMod = modules.find((m) => m.key === "reviews");
  if (reviewsMod && review.waiting) reviewsMod.status = "waiting";

  return {
    philosophy: {
      statement: "Planner proposes. Policy governs. Human decides. Pipeline executes. Publisher publishes.",
      control: "Human Controlled — not autonomous",
    },
    version,
    modules,
    latestReports: reports.items.slice(0, 8),
    latestRuns: git.recentCommits,
    reviewCounts: review.counts,
    datasetSummary: {
      total: datasets.length,
      populated,
      placeholders: datasets.length - populated,
      coveragePct,
    },
    waitingMessage: WAITING,
  };
}

export function globalSearch(query: string) {
  const q = query.trim().toLowerCase();
  if (!q) return { query, results: [] as { type: string; id: string; title: string; subtitle?: string; href: string }[] };

  const results: { type: string; id: string; title: string; subtitle?: string; href: string }[] = [];

  for (const d of listDatasets()) {
    if (d.name.toLowerCase().includes(q) || d.domain.toLowerCase().includes(q)) {
      results.push({
        type: "dataset",
        id: d.id,
        title: d.name,
        subtitle: d.domain,
        href: `/datasets?file=${encodeURIComponent(d.relativePath)}`,
      });
    }
  }

  const ont = getOntologyBundle();
  for (const row of ont.tables["entities.csv"]?.rows ?? []) {
    const name = row["Entity Name"] ?? "";
    const id = row["Entity ID"] ?? "";
    if (name.toLowerCase().includes(q) || id.toLowerCase().includes(q)) {
      results.push({
        type: "entity",
        id,
        title: name,
        subtitle: row["Entity Type"],
        href: `/ontology?entity=${encodeURIComponent(id)}`,
      });
    }
  }
  for (const row of ont.tables["relationships.csv"]?.rows ?? []) {
    const label = `${row["Source Entity"]} ${row["Relationship"]} ${row["Target Entity"]}`;
    if (label.toLowerCase().includes(q)) {
      results.push({
        type: "relationship",
        id: row["Relationship ID"] ?? label,
        title: label,
        href: `/ontology?rel=${encodeURIComponent(row["Relationship ID"] ?? "")}`,
      });
    }
  }

  const policies = getPolicies();
  if (policies.data) {
    const blob = JSON.stringify(policies.data).toLowerCase();
    if (blob.includes(q) || "policy".includes(q) || "policies".includes(q)) {
      results.push({
        type: "policy",
        id: "policies",
        title: "Knowledge Policies",
        subtitle: "automation/config/policies.yaml",
        href: "/policies",
      });
    }
  }

  for (const r of listReports().items) {
    if (r.name.toLowerCase().includes(q) || r.kind.toLowerCase().includes(q)) {
      results.push({
        type: "report",
        id: r.relativePath,
        title: r.name,
        subtitle: r.kind,
        href: `/reports?file=${encodeURIComponent(r.relativePath)}`,
      });
    }
  }

  const planner = buildPlannerView();
  for (const p of planner.datasets) {
    if (p.dataset.toLowerCase().includes(q) || p.suggestedAction.toLowerCase().includes(q)) {
      results.push({
        type: "plan",
        id: p.path,
        title: `Plan: ${p.dataset}`,
        subtitle: `priority ${p.priority}`,
        href: "/planner",
      });
    }
  }

  return { query, results: results.slice(0, 40) };
}
