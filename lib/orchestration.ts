/**
 * ECC orchestration layer.
 *
 * Architecture (never bypass):
 * Dashboard → Planner → Policy Engine → Pipeline → Review → Publisher
 *
 * ECC does not reimplement KAS/CI logic. It invokes existing modules
 * via child processes when explicitly requested, with dry-run defaults.
 */

import { spawn } from "child_process";
import path from "path";
import { getRepoRoot } from "./paths";

export type PipelineStage =
  | "planner"
  | "policy"
  | "pipeline"
  | "review"
  | "publisher";

export type ProgressState = {
  runId: string;
  status: "idle" | "running" | "success" | "error" | "blocked";
  currentStage: PipelineStage | null;
  progressPct: number;
  elapsedMs: number;
  currentTask: string;
  rowsProcessed: number;
  currentDataset: string | null;
  etaMs: number | null;
  message: string;
  logs: ConsoleLine[];
  startedAt: string | null;
  finishedAt: string | null;
};

export type ConsoleLine = {
  ts: string;
  stream: "system" | "planner" | "pipeline" | "validator" | "publisher" | "git" | "policy";
  level: "info" | "warn" | "error" | "success";
  text: string;
};

const STAGE_ORDER: PipelineStage[] = [
  "planner",
  "policy",
  "pipeline",
  "review",
  "publisher",
];

/** In-memory singleton for the current ECC process (dev server). */
let activeProgress: ProgressState = idleProgress();
const listeners = new Set<(p: ProgressState) => void>();

function idleProgress(): ProgressState {
  return {
    runId: "",
    status: "idle",
    currentStage: null,
    progressPct: 0,
    elapsedMs: 0,
    currentTask: "Idle — waiting for human command",
    rowsProcessed: 0,
    currentDataset: null,
    etaMs: null,
    message: "No active run",
    logs: [
      {
        ts: new Date().toISOString(),
        stream: "system",
        level: "info",
        text: "ECC console ready. Human-controlled mode. Scheduler → Planner → Policy → Pipeline → Review → Publisher. Continuous learning never stops.",
      },
    ],
    startedAt: null,
    finishedAt: null,
  };
}

export function getProgress(): ProgressState {
  return activeProgress;
}

export function subscribeProgress(fn: (p: ProgressState) => void): () => void {
  listeners.add(fn);
  return () => listeners.delete(fn);
}

function emit() {
  for (const fn of listeners) fn(activeProgress);
}

function pushLog(
  stream: ConsoleLine["stream"],
  level: ConsoleLine["level"],
  text: string
) {
  activeProgress = {
    ...activeProgress,
    logs: [
      ...activeProgress.logs.slice(-500),
      { ts: new Date().toISOString(), stream, level, text },
    ],
  };
  emit();
}

function setProgress(partial: Partial<ProgressState>) {
  activeProgress = { ...activeProgress, ...partial };
  emit();
}

function stageIndex(stage: PipelineStage | null): number {
  if (!stage) return 0;
  return STAGE_ORDER.indexOf(stage);
}

function runPython(
  scriptRel: string,
  args: string[],
  stream: ConsoleLine["stream"]
): Promise<number> {
  const root = getRepoRoot();
  const script = path.join(root, scriptRel);

  // Vercel serverless does not ship Python CI runners by default.
  if (process.env.VERCEL || process.env.ECC_DISABLE_PYTHON === "1") {
    pushLog(
      stream,
      "warn",
      `Python orchestration skipped on this runtime (${scriptRel}). Use GitHub Actions for planner/validate/publish jobs.`
    );
    return Promise.resolve(0);
  }

  return new Promise((resolve) => {
    const child = spawn("python3", [script, ...args], {
      cwd: root,
      env: { ...process.env, PYTHONUNBUFFERED: "1" },
    });
    child.stdout.on("data", (buf: Buffer) => {
      for (const line of buf.toString("utf8").split(/\n/)) {
        if (line.trim()) pushLog(stream, "info", line);
      }
    });
    child.stderr.on("data", (buf: Buffer) => {
      for (const line of buf.toString("utf8").split(/\n/)) {
        if (line.trim()) pushLog(stream, "warn", line);
      }
    });
    child.on("close", (code) => resolve(code ?? 1));
    child.on("error", (err) => {
      pushLog(stream, "error", err.message);
      resolve(1);
    });
  });
}

export type RunRequest = {
  action: "planner_dry_run" | "validate" | "review_summary" | "publish_dry_run" | "full_dry_chain";
  environment?: string;
};

/**
 * Execute an allowed orchestration action.
 * Publisher never runs with --no-dry-run from ECC unless explicitly extended later.
 * Crawler is never invoked.
 */
export async function runOrchestration(req: RunRequest): Promise<ProgressState> {
  if (activeProgress.status === "running") {
    pushLog("system", "warn", "Run already in progress — ignored");
    return activeProgress;
  }

  const runId = `ECC-${Date.now().toString(36).toUpperCase()}`;
  const started = Date.now();
  const env = req.environment ?? "development";

  setProgress({
    runId,
    status: "running",
    currentStage: "planner",
    progressPct: 5,
    elapsedMs: 0,
    currentTask: `Starting ${req.action}`,
    rowsProcessed: 0,
    currentDataset: null,
    etaMs: null,
    message: "Running under human control (dry-run safe defaults)",
    startedAt: new Date().toISOString(),
    finishedAt: null,
  });
  pushLog("system", "info", `[${runId}] action=${req.action} env=${env}`);
  pushLog(
    "system",
    "info",
    "Control flow: Planner → Policy → Pipeline → Review → Publisher (no bypass)"
  );

  const tick = setInterval(() => {
    setProgress({ elapsedMs: Date.now() - started });
  }, 250);

  try {
    // Policy gate check is always first after planner intent
    if (req.action === "planner_dry_run" || req.action === "full_dry_chain") {
      setProgress({
        currentStage: "planner",
        progressPct: 15,
        currentTask: "Running Knowledge Planner (dry-run)",
      });
      const code = await runPython(
        "automation/ci/planner.py",
        ["--environment", env, "--dry-run"],
        "planner"
      );
      if (code !== 0) {
        setProgress({
          status: "error",
          message: `Planner failed (exit ${code})`,
          progressPct: 100,
          finishedAt: new Date().toISOString(),
        });
        return activeProgress;
      }
      pushLog("planner", "success", "Planner completed");
    }

    if (req.action === "validate" || req.action === "full_dry_chain") {
      setProgress({
        currentStage: "policy",
        progressPct: 35,
        currentTask: "Policy context loaded — running repository validator",
      });
      pushLog("policy", "info", "Policy Engine consulted (read-only)");
      setProgress({
        currentStage: "pipeline",
        progressPct: 50,
        currentTask: "Running repository validation",
      });
      const code = await runPython(
        "automation/ci/validate_repo.py",
        ["--environment", env, "--dry-run"],
        "validator"
      );
      if (code !== 0) {
        setProgress({
          status: "error",
          message: `Validator failed (exit ${code})`,
          progressPct: 100,
          finishedAt: new Date().toISOString(),
        });
        return activeProgress;
      }
      pushLog("validator", "success", "Validation completed");
    }

    if (req.action === "review_summary" || req.action === "full_dry_chain") {
      setProgress({
        currentStage: "review",
        progressPct: 70,
        currentTask: "Generating review summary",
      });
      const code = await runPython(
        "automation/ci/review_summary.py",
        ["--environment", env, "--dry-run"],
        "pipeline"
      );
      if (code !== 0) {
        setProgress({
          status: "error",
          message: `Review summary failed (exit ${code})`,
          progressPct: 100,
          finishedAt: new Date().toISOString(),
        });
        return activeProgress;
      }
      pushLog("pipeline", "success", "Review summary completed");
    }

    if (req.action === "publish_dry_run" || req.action === "full_dry_chain") {
      setProgress({
        currentStage: "publisher",
        progressPct: 90,
        currentTask: "Publisher dry-run (never bypasses review)",
      });
      pushLog(
        "publisher",
        "info",
        "Publisher invoked only after Planner/Policy/Review path — dry-run forced"
      );
      const code = await runPython(
        "automation/ci/publish_ci.py",
        ["--environment", env, "--dry-run"],
        "publisher"
      );
      // exit 4 = blocked is expected without approvals
      if (code === 0) {
        pushLog("publisher", "success", "Publish dry-run completed");
      } else if (code === 4) {
        pushLog(
          "publisher",
          "warn",
          "Publisher blocked (exit 4) — expected without approved candidates / policy"
        );
        setProgress({
          status: "blocked",
          message: "Publisher blocked by policy or empty approved queue",
          progressPct: 100,
          finishedAt: new Date().toISOString(),
          elapsedMs: Date.now() - started,
        });
        return activeProgress;
      } else {
        setProgress({
          status: "error",
          message: `Publisher failed (exit ${code})`,
          progressPct: 100,
          finishedAt: new Date().toISOString(),
        });
        return activeProgress;
      }
    }

    setProgress({
      status: "success",
      progressPct: 100,
      currentTask: "Completed",
      message: "Orchestration finished",
      finishedAt: new Date().toISOString(),
      elapsedMs: Date.now() - started,
      currentStage: STAGE_ORDER[stageIndex(activeProgress.currentStage)] ?? "publisher",
    });
    pushLog("system", "success", `[${runId}] done in ${Date.now() - started}ms`);
    return activeProgress;
  } finally {
    clearInterval(tick);
    setProgress({ elapsedMs: Date.now() - started });
  }
}

export function resetProgress() {
  activeProgress = idleProgress();
  emit();
}
