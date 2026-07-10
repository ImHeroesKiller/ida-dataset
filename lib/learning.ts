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
  return listJsonDir(repoPath("automation/missions/missions"));
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
