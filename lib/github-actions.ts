/**
 * GitHub Actions integration for continuous learning.
 *
 * Manual "Start Learning" → workflow_dispatch on learn.yml
 * Dashboard status → list workflow runs (running / queued / completed)
 *
 * Env:
 *   GITHUB_TOKEN | GH_PAT | IDA_GITHUB_TOKEN — fine-grained or classic PAT
 *     with actions:write (dispatch) + actions:read (status) + contents:read
 *   GITHUB_REPOSITORY | VERCEL_GIT_REPO_OWNER + VERCEL_GIT_REPO_SLUG
 */

export type WorkflowRun = {
  id: number;
  name: string;
  status: string; // queued | in_progress | completed
  conclusion: string | null;
  html_url: string;
  created_at: string;
  updated_at: string;
  event: string;
  display_title?: string;
  head_branch?: string;
  path?: string;
};

export type DispatchResult = {
  ok: boolean;
  status_code: number;
  message: string;
  workflow: string;
  repository: string;
  inputs?: Record<string, string>;
  error_code?: string;
  recovery_suggestion?: string;
};

export type ActionsStatus = {
  configured: boolean;
  repository: string | null;
  running: boolean;
  queued: boolean;
  status: "idle" | "running" | "queued" | "completed" | "failed" | "unknown";
  current_run: WorkflowRun | null;
  recent_runs: WorkflowRun[];
  next_scheduled_hint: string;
  error?: string | null;
};

function token(): string | null {
  return (
    process.env.IDA_GITHUB_TOKEN ||
    process.env.GH_PAT ||
    process.env.GITHUB_TOKEN ||
    null
  );
}

export function resolveRepository(): string | null {
  if (process.env.GITHUB_REPOSITORY) return process.env.GITHUB_REPOSITORY;
  if (process.env.IDA_GITHUB_REPOSITORY) return process.env.IDA_GITHUB_REPOSITORY;
  const owner =
    process.env.VERCEL_GIT_REPO_OWNER || process.env.GITHUB_REPOSITORY_OWNER;
  const slug =
    process.env.VERCEL_GIT_REPO_SLUG || process.env.GITHUB_REPOSITORY_NAME;
  if (owner && slug) return `${owner}/${slug}`;
  return null;
}

function apiBase(): string {
  return (process.env.GITHUB_API_URL || "https://api.github.com").replace(
    /\/$/,
    ""
  );
}

async function ghFetch(
  path: string,
  init: RequestInit = {}
): Promise<{ ok: boolean; status: number; json: unknown; text: string }> {
  const t = token();
  const repo = resolveRepository();
  if (!t || !repo) {
    return {
      ok: false,
      status: 0,
      json: null,
      text: !t
        ? "Missing GITHUB_TOKEN / IDA_GITHUB_TOKEN / GH_PAT"
        : "Missing GITHUB_REPOSITORY",
    };
  }
  const url = path.startsWith("http")
    ? path
    : `${apiBase()}/repos/${repo}${path.startsWith("/") ? path : `/${path}`}`;
  try {
    const res = await fetch(url, {
      ...init,
      headers: {
        Accept: "application/vnd.github+json",
        Authorization: `Bearer ${t}`,
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "ida-dataset-ecc",
        ...(init.headers || {}),
      },
      cache: "no-store",
    });
    const text = await res.text();
    let json: unknown = null;
    try {
      json = text ? JSON.parse(text) : null;
    } catch {
      json = null;
    }
    return { ok: res.ok, status: res.status, json, text };
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    return { ok: false, status: 0, json: null, text: err.message };
  }
}

export function isGithubConfigured(): boolean {
  return Boolean(token() && resolveRepository());
}

/**
 * Trigger learn.yml via workflow_dispatch.
 * No local Python execution.
 */
export async function dispatchLearningWorkflow(opts: {
  mission?: string;
  environment?: string;
  dry_run?: boolean;
  trigger?: string;
  ref?: string;
  commit_session?: boolean;
}): Promise<DispatchResult> {
  const repo = resolveRepository();
  if (!token() || !repo) {
    return {
      ok: false,
      status_code: 422,
      message:
        "GitHub Actions dispatch is not configured. Set IDA_GITHUB_TOKEN (actions:write) and GITHUB_REPOSITORY (or VERCEL_GIT_REPO_*).",
      workflow: "learn.yml",
      repository: repo || "unknown",
      error_code: "GITHUB_NOT_CONFIGURED",
      recovery_suggestion:
        "Add repository secrets/env: IDA_GITHUB_TOKEN (PAT with actions:write), GITHUB_REPOSITORY=owner/repo. On Vercel set the same env vars. Locally, Start Learning falls back to a one-shot learning_session.py run.",
    };
  }

  const inputs: Record<string, string> = {
    environment: opts.environment || "production",
    dry_run: opts.dry_run === false ? "false" : "true",
    mission:
      opts.mission?.trim() ||
      "Learn Industry Library knowledge — continuous learning session",
    trigger: opts.trigger || "manual",
    commit_session: opts.commit_session === false ? "false" : "true",
  };

  const ref =
    opts.ref ||
    process.env.VERCEL_GIT_COMMIT_REF ||
    process.env.GITHUB_REF_NAME ||
    "main";

  const res = await ghFetch(`/actions/workflows/learn.yml/dispatches`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ref, inputs }),
  });

  if (res.status === 204 || res.ok) {
    return {
      ok: true,
      status_code: res.status || 204,
      message: "Learning workflow dispatched to GitHub Actions",
      workflow: "learn.yml",
      repository: repo,
      inputs,
    };
  }

  // Fallback: try workflow file name without path issues
  if (res.status === 404) {
    const res2 = await ghFetch(`/actions/workflows/learn.yml/dispatches`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ref, inputs }),
    });
    if (res2.status === 204 || res2.ok) {
      return {
        ok: true,
        status_code: 204,
        message: "Learning workflow dispatched to GitHub Actions",
        workflow: "learn.yml",
        repository: repo,
        inputs,
      };
    }
  }

  return {
    ok: false,
    status_code: res.status || 500,
    message:
      (res.json as { message?: string } | null)?.message ||
      res.text ||
      "Workflow dispatch failed",
    workflow: "learn.yml",
    repository: repo,
    inputs,
    error_code: "WORKFLOW_DISPATCH_FAILED",
    recovery_suggestion:
      "Verify the PAT can dispatch workflows on this repo and that .github/workflows/learn.yml exists on the target branch.",
  };
}

export async function listLearningRuns(limit = 10): Promise<{
  ok: boolean;
  runs: WorkflowRun[];
  error?: string;
}> {
  if (!isGithubConfigured()) {
    return { ok: false, runs: [], error: "GitHub not configured" };
  }
  const res = await ghFetch(
    `/actions/workflows/learn.yml/runs?per_page=${Math.min(30, limit)}`
  );
  if (!res.ok) {
    return {
      ok: false,
      runs: [],
      error:
        (res.json as { message?: string } | null)?.message ||
        res.text ||
        `HTTP ${res.status}`,
    };
  }
  const payload = res.json as { workflow_runs?: WorkflowRun[] };
  const runs = (payload.workflow_runs || []).map((r) => ({
    id: r.id,
    name: r.name,
    status: r.status,
    conclusion: r.conclusion,
    html_url: r.html_url,
    created_at: r.created_at,
    updated_at: r.updated_at,
    event: r.event,
    display_title: r.display_title,
    head_branch: r.head_branch,
    path: r.path,
  }));
  return { ok: true, runs };
}

export async function getActionsLearningStatus(): Promise<ActionsStatus> {
  const repo = resolveRepository();
  // Align with learn.yml continuous cadence (every 15 minutes)
  const next = (() => {
    const d = new Date();
    d.setUTCSeconds(0, 0);
    const mins = d.getUTCMinutes();
    const nextSlot = Math.floor(mins / 15) * 15 + 15;
    if (nextSlot >= 60) {
      d.setUTCHours(d.getUTCHours() + 1);
      d.setUTCMinutes(0, 0, 0);
    } else {
      d.setUTCMinutes(nextSlot, 0, 0);
    }
    return d.toISOString().replace(/\.\d{3}Z$/, "Z");
  })();

  if (!isGithubConfigured()) {
    return {
      configured: false,
      repository: repo,
      running: false,
      queued: false,
      status: "idle",
      current_run: null,
      recent_runs: [],
      next_scheduled_hint: next,
      error: "GitHub token/repository not configured — status from local sessions only",
    };
  }

  const listed = await listLearningRuns(15);
  if (!listed.ok) {
    return {
      configured: true,
      repository: repo,
      running: false,
      queued: false,
      status: "unknown",
      current_run: null,
      recent_runs: [],
      next_scheduled_hint: next,
      error: listed.error,
    };
  }

  const runs = listed.runs;
  const inProgress = runs.find((r) => r.status === "in_progress") || null;
  const queued = runs.find((r) => r.status === "queued" || r.status === "waiting") || null;
  const latest = runs[0] || null;

  let status: ActionsStatus["status"] = "idle";
  if (inProgress) status = "running";
  else if (queued) status = "queued";
  else if (latest?.conclusion === "failure" || latest?.conclusion === "cancelled")
    status = "failed";
  else if (latest?.conclusion === "success") status = "completed";

  return {
    configured: true,
    repository: repo,
    running: Boolean(inProgress),
    queued: Boolean(queued),
    status,
    current_run: inProgress || queued || latest,
    recent_runs: runs,
    next_scheduled_hint: next,
    error: null,
  };
}
