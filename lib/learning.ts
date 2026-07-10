/**
 * Server-side bridge to Continuous Learning Scheduler state.
 * Prefer spawning Python CLI for authoritative orchestration;
 * fall back to reading state files for dashboard rendering.
 */

import fs from "fs";
import path from "path";
import { spawnSync } from "child_process";
import { getRepoRoot, repoPath } from "./paths";

const WAITING = "Waiting for first execution";

function readJson(filePath: string): unknown {
  try {
    if (!fs.existsSync(filePath)) return null;
    return JSON.parse(fs.readFileSync(filePath, "utf8"));
  } catch {
    return null;
  }
}

function listJsonDir(dir: string): Record<string, unknown>[] {
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".json"))
    .sort()
    .map((f) => {
      const data = readJson(path.join(dir, f));
      return data && typeof data === "object"
        ? (data as Record<string, unknown>)
        : { file: f };
    });
}

export function runSchedulerCli(
  args: string[]
): { ok: boolean; data: unknown; stderr: string } {
  const root = getRepoRoot();
  // Skip Python on Vercel runtime
  if (process.env.VERCEL || process.env.ECC_DISABLE_PYTHON === "1") {
    return {
      ok: false,
      data: null,
      stderr: "Scheduler CLI unavailable on this runtime",
    };
  }
  const result = spawnSync(
    "python3",
    ["-m", "automation.scheduler", ...args],
    {
      cwd: root,
      encoding: "utf8",
      env: { ...process.env, PYTHONUNBUFFERED: "1" },
      maxBuffer: 4 * 1024 * 1024,
    }
  );
  const stdout = (result.stdout || "").trim();
  let data: unknown = null;
  try {
    data = stdout ? JSON.parse(stdout) : null;
  } catch {
    data = { raw: stdout };
  }
  return {
    ok: result.status === 0,
    data,
    stderr: (result.stderr || "").trim(),
  };
}

export function getLearningDashboard() {
  // Prefer live CLI dashboard for accuracy when Python is available
  const live = runSchedulerCli(["dashboard"]);
  if (live.ok && live.data && typeof live.data === "object") {
    return live.data as Record<string, unknown>;
  }

  // File-based fallback (Vercel / no Python)
  const metrics = readJson(
    repoPath("automation/scheduler/state/metrics.json")
  ) as Record<string, unknown> | null;
  const queue = readJson(
    repoPath("automation/scheduler/state/learning_queue.json")
  ) as Record<string, unknown> | null;
  const state = readJson(
    repoPath("automation/scheduler/state/scheduler_state.json")
  ) as Record<string, unknown> | null;
  const missions = listJsonDir(repoPath("automation/missions/missions"));
  const allocation =
    (state?.allocation as Record<string, unknown> | undefined) ||
    (metrics?.allocation as Record<string, unknown> | undefined) ||
    null;

  const running = missions.find((m) => m.status === "Running");
  const queued = missions.find((m) => m.status === "Queued");

  return {
    updated_at: new Date().toISOString(),
    brain_health: metrics?.brain_health ?? "waiting",
    knowledge_growth: metrics?.knowledge_growth ?? {
      datasets_populated: 0,
      datasets_total: 0,
      coverage_pct: 0,
    },
    learning_allocation: allocation,
    current_mission: running || queued || null,
    current_task: null,
    mission_queue: missions.filter((m) =>
      ["Draft", "Queued", "Running", "Waiting Review", "Paused"].includes(
        String(m.status || "")
      )
    ),
    continuous_learning_queue: (
      (queue?.tasks as Record<string, unknown>[]) || []
    ).filter((t) => t.kind === "continuous"),
    learning_timeline: (metrics?.learning_history as unknown[]) || [],
    knowledge_feed: (metrics?.learning_history as unknown[]) || [],
    brain_activity: {
      ticks: metrics?.ticks ?? 0,
      tasks_dispatched: metrics?.tasks_dispatched ?? 0,
      continuous_cycles: metrics?.continuous_cycles ?? 0,
      directed_cycles: metrics?.directed_cycles ?? 0,
      missions_completed: metrics?.missions_completed ?? 0,
    },
    learning_history: (metrics?.learning_history as unknown[]) || [],
    queue: queue || { total: 0, tasks: [] },
    placeholders: {
      reasoning_coverage: WAITING,
      decision_coverage: WAITING,
    },
    architecture: {
      entry: "ContinuousLearningScheduler",
      flow: [
        "Scheduler",
        "PriorityEngine",
        "Planner",
        "Policy",
        "Pipeline",
        "Review",
        "Publisher",
        "Telemetry",
      ],
    },
    source: live.ok ? "cli" : "files",
    waiting_message:
      missions.length === 0 && !queue
        ? WAITING
        : null,
  };
}

export function listMissions() {
  return listJsonDir(repoPath("automation/missions/missions")).sort((a, b) =>
    String(b.updated_at || b.created_at || "").localeCompare(
      String(a.updated_at || a.created_at || "")
    )
  );
}

/** Infer primary dataset class from natural language mission text. */
export function inferDatasetFromText(text: string): string {
  const t = text.toLowerCase();
  if (t.includes("persona") || t.includes("buyer")) return "buyer_persona_library";
  if (t.includes("decision maker")) return "decision_maker_library";
  if (t.includes("regulat")) return "regulation_library";
  if (t.includes("pain")) return "pain_point_library";
  if (t.includes("solution")) return "solution_library";
  if (t.includes("framework")) return "framework_library";
  if (t.includes("case stud")) return "case_study_library";
  if (t.includes("compan")) return "company_profile";
  if (t.includes("service")) return "service_library";
  if (t.includes("product")) return "product_catalog";
  if (t.includes("competitor")) return "competitor_library";
  if (t.includes("opportunit")) return "opportunity_analysis";
  if (t.includes("industry") || t.includes("industries")) return "industry_library";
  return "industry_library";
}

/**
 * Create a mission record on disk (no Python required) and return it.
 * Used when dispatching via GitHub Actions on Vercel/production.
 */
export function createMissionRecord(text: string, opts?: {
  requester?: string;
  priority?: string;
  status?: string;
}): Record<string, unknown> {
  const now = new Date().toISOString().replace(/\.\d{3}Z$/, "Z");
  const stamp = now.slice(0, 10).replace(/-/g, "");
  const rand = Math.random().toString(16).slice(2, 8).toUpperCase();
  const mission_id = `MIS-${stamp}-${rand}`;
  const contract_id = `CTR-${stamp}-${rand}`;
  const title =
    text.length > 90 ? `${text.slice(0, 87).trim()}…` : text.trim();
  const dataset = inferDatasetFromText(text);
  const mission: Record<string, unknown> = {
    mission_id,
    title,
    description: text.trim(),
    priority: opts?.priority || "P1",
    requester: opts?.requester || "factory-ui",
    created_at: now,
    due_date: null,
    status: opts?.status || "Queued",
    knowledge_targets: [dataset],
    allowed_sources: [],
    policies: {},
    estimated_effort: 1.0,
    resource_allocation: 30.0,
    progress: 0,
    confidence: 0,
    result: null,
    executive_summary: null,
    related_datasets: [dataset],
    updated_at: now,
    natural_language_request: text.trim(),
    contract_id,
    current_stage: "queued",
    current_dataset: dataset,
    documents_processed: 0,
    entities_learned: 0,
    knowledge_added: 0,
    eta: null,
    dispatch_channel: "github_actions",
  };

  // Best-effort persist (may be read-only on some serverless runtimes)
  try {
    const dir = repoPath("automation/missions/missions");
    fs.mkdirSync(dir, { recursive: true });
    const file = path.join(dir, `${mission_id}.json`);
    fs.writeFileSync(file, JSON.stringify(mission, null, 2) + "\n", "utf8");

    const cdir = repoPath("automation/missions/contracts");
    fs.mkdirSync(cdir, { recursive: true });
    const contract = {
      contract_id,
      mission_id,
      objective: title,
      knowledge_scope: [dataset],
      priority: mission.priority,
      resource_allocation: 30,
      created_at: now,
      updated_at: now,
      status: "active",
    };
    fs.writeFileSync(
      path.join(cdir, `${contract_id}.json`),
      JSON.stringify(contract, null, 2) + "\n",
      "utf8"
    );
  } catch {
    mission.persisted = false;
  }

  return mission;
}

/** Parse learning report metadata for human-readable cards (no raw-only filenames). */
export function enrichLearningReports(
  reports: { name: string; relativePath: string; mtime: string; size: number }[]
) {
  return reports.map((r) => {
    const lower = r.name.toLowerCase();
    let batch = "—";
    let mission = r.name.replace(/\.(md|json)$/i, "");
    let rowsAdded: number | null = null;
    let coverage: string | null = null;
    let confidence: number | null = null;

    const batchM = r.name.match(/batch0*(\d+)/i);
    if (batchM) batch = `Batch-${batchM[1].padStart(3, "0")}`;
    if (lower.includes("service")) mission = "Service Dataset";
    else if (lower.includes("product")) mission = "Product Dataset";
    else if (lower.includes("company")) mission = "Company Dataset";
    else if (lower.includes("pain")) mission = "Pain Point Dataset";
    else if (lower.includes("solution")) mission = "Solution Dataset";
    else if (lower.includes("framework")) mission = "Framework Dataset";
    else if (lower.includes("case")) mission = "Case Study Dataset";
    else if (lower.includes("industry") || lower.includes("epic2a"))
      mission = "Industry Dataset";
    else if (lower.includes("readiness")) mission = "Readiness / Quality";
    else if (lower.includes("session")) mission = "Learning Session";

    // Best-effort parse from markdown/json content
    try {
      const abs = path.join(getRepoRoot(), r.relativePath);
      if (fs.existsSync(abs) && r.size < 500_000) {
        const text = fs.readFileSync(abs, "utf8");
        const rowsM = text.match(/Rows Added[^\d]*(\d+)/i) || text.match(/"rows_added"\s*:\s*(\d+)/);
        if (rowsM) rowsAdded = Number(rowsM[1]);
        const covM =
          text.match(/Coverage After[^\n]*?(\d+(?:\.\d+)?\s*%)/i) ||
          text.match(/"coverage_after_pct"\s*:\s*([0-9.]+)/);
        if (covM) coverage = covM[1].includes("%") ? covM[1] : `${covM[1]}%`;
        const confM =
          text.match(/Average Confidence[^\d]*([0-9.]+)/i) ||
          text.match(/"average_confidence"\s*:\s*([0-9.]+)/);
        if (confM) confidence = Number(confM[1]);
      }
    } catch {
      /* ignore */
    }

    return {
      ...r,
      batch,
      mission,
      rows_added: rowsAdded,
      coverage_increase: coverage,
      confidence,
      generated: r.mtime,
    };
  });
}

export function listContracts() {
  return listJsonDir(repoPath("automation/missions/contracts"));
}

export function listLearningReports() {
  const dir = repoPath("reports/learning");
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => f !== ".gitkeep")
    .map((name) => {
      const abs = path.join(dir, name);
      const st = fs.statSync(abs);
      return {
        name,
        relativePath: path
          .relative(getRepoRoot(), abs)
          .replace(/\\/g, "/"),
        mtime: st.mtime.toISOString(),
        size: st.size,
      };
    })
    .sort((a, b) => b.mtime.localeCompare(a.mtime));
}
