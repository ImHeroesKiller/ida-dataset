/**
 * Local one-shot learning session (development only).
 *
 * Same entrypoint as GitHub Actions: automation/ci/learning_session.py
 * Not a long-lived runtime — process exits when the session ends.
 * Never used on Vercel/serverless.
 */

import { spawnSync } from "child_process";
import { getRepoRoot } from "@/lib/paths";

export type LocalSessionResult = {
  ok: boolean;
  status_code: number;
  message: string;
  session_id?: string | null;
  status?: string;
  data?: Record<string, unknown> | null;
  error_code?: string;
  recovery_suggestion?: string;
  stderr?: string;
};

export function isLocalLearningAllowed(): boolean {
  if (process.env.VERCEL || process.env.VERCEL_ENV) return false;
  if (process.env.AWS_LAMBDA_FUNCTION_NAME) return false;
  if (process.env.ECC_DISABLE_LOCAL_LEARNING === "1") return false;
  return true;
}

export function runLocalLearningSession(opts: {
  mission?: string;
  dry_run?: boolean;
  environment?: string;
  trigger?: string;
}): LocalSessionResult {
  if (!isLocalLearningAllowed()) {
    return {
      ok: false,
      status_code: 422,
      message:
        "Local learning is disabled on this host (serverless / Vercel). Configure IDA_GITHUB_TOKEN to dispatch learn.yml.",
      error_code: "LOCAL_LEARNING_DISABLED",
      recovery_suggestion:
        "Set IDA_GITHUB_TOKEN (actions:write) and GITHUB_REPOSITORY on Vercel, then retry Start Learning.",
    };
  }

  const root = getRepoRoot();
  const mission =
    opts.mission?.trim() ||
    "Learn Industry Library knowledge — continuous learning session";
  const dryRun = opts.dry_run !== false;
  const environment = opts.environment || "development";
  const trigger = opts.trigger || "manual";

  const args = [
    "automation/ci/learning_session.py",
    "--environment",
    environment,
    dryRun ? "--dry-run" : "--no-dry-run",
    "--instruction",
    mission,
    "--mission",
    mission,
    "--trigger",
    trigger,
    "--pace",
    "0.08",
  ];

  try {
    const result = spawnSync("python3", args, {
      cwd: root,
      encoding: "utf8",
      env: { ...process.env, PYTHONUNBUFFERED: "1" },
      maxBuffer: 8 * 1024 * 1024,
      timeout: 180_000,
    });

    const stdout = (result.stdout || "").trim();
    const stderr = (result.stderr || "").trim();
    let parsed: Record<string, unknown> | null = null;
    for (const line of stdout.split("\n").reverse()) {
      const t = line.trim();
      if (!t.startsWith("{")) continue;
      try {
        parsed = JSON.parse(t) as Record<string, unknown>;
        break;
      } catch {
        /* keep scanning */
      }
    }

    if (result.error) {
      const err = result.error as NodeJS.ErrnoException;
      return {
        ok: false,
        status_code: 500,
        message: err.message || "Failed to spawn python3",
        error_code:
          err.code === "ENOENT" ? "PYTHON_MISSING" : "LOCAL_SPAWN_FAILED",
        recovery_suggestion:
          "Install Python 3 and ensure `python3 automation/ci/learning_session.py --help` works from the repo root.",
        stderr,
      };
    }

    if (result.status !== 0 || !parsed?.ok) {
      return {
        ok: false,
        status_code: 500,
        message:
          (parsed?.summary as string) ||
          (parsed?.status as string) ||
          stderr.slice(0, 500) ||
          `Local learning session exited with code ${result.status}`,
        session_id: (parsed?.session_id as string) || null,
        status: (parsed?.status as string) || "failed",
        data: parsed,
        error_code: "LOCAL_SESSION_FAILED",
        recovery_suggestion:
          "Inspect automation/sessions/ for the failed session JSON and fix the underlying learning error.",
        stderr: stderr.slice(0, 2000),
      };
    }

    // Development progressive auto-publish after session (backend-paced)
    try {
      spawnSync("python3", ["automation/ci/progressive_publish.py"], {
        cwd: root,
        encoding: "utf8",
        env: { ...process.env, PYTHONUNBUFFERED: "1" },
        timeout: 300_000,
      });
    } catch {
      /* non-fatal */
    }

    return {
      ok: true,
      status_code: 200,
      message: `Local learning session completed (${parsed.session_id})`,
      session_id: (parsed.session_id as string) || null,
      status: (parsed.status as string) || "completed",
      data: {
        ...parsed,
        execution_model: "local_oneshot",
        note: "Same learning_session.py entrypoint as GitHub Actions (not a long-lived runtime).",
      },
    };
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    return {
      ok: false,
      status_code: 500,
      message: err.message,
      error_code: "LOCAL_SESSION_EXCEPTION",
      recovery_suggestion: "See server logs for the stack trace.",
    };
  }
}
