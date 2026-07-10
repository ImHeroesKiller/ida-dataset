import { NextRequest } from "next/server";
import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import {
  dispatchLearningWorkflow,
  isGithubConfigured,
} from "@/lib/github-actions";
import {
  isLocalLearningAllowed,
  runLocalLearningSession,
} from "@/lib/local-learning";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";
export const maxDuration = 180;

/**
 * POST /api/live/start
 *
 * Preferred: GitHub Actions workflow_dispatch on learning.yml
 * Fallback (local only): one-shot python automation/ci/learning_session.py
 * Never spawns a long-lived runtime. Safe on Vercel with IDA_GITHUB_TOKEN.
 */
export async function POST(req: NextRequest) {
  return withApiJson("api.live.start", async () => {
    let body: {
      instruction?: string;
      mission?: string;
      dry_run?: boolean;
      environment?: string;
      trigger?: string;
      pace?: number;
      prefer_local?: boolean;
    } = {};
    try {
      const text = await req.text();
      if (text && text.trim()) {
        body = JSON.parse(text) as typeof body;
      }
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component: "api.live.start",
        reason: `Invalid JSON request body: ${err.message}`,
        error_code: "INVALID_REQUEST_BODY",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 400,
        recovery_suggestion:
          "Send Content-Type application/json with a valid object.",
      });
    }

    const mission =
      body.mission?.trim() ||
      body.instruction?.trim() ||
      "Learn Industry Library knowledge — continuous learning session";
    const dryRun = body.dry_run !== false;
    const environment =
      body.environment ||
      (process.env.VERCEL ? "production" : "development");
    const trigger = body.trigger || "manual";

    const preferLocal =
      body.prefer_local === true ||
      process.env.IDA_PREFER_LOCAL_LEARNING === "1";

    // --- Preferred path: GitHub Actions ---
    if (isGithubConfigured() && !preferLocal) {
      const result = await dispatchLearningWorkflow({
        mission,
        environment,
        dry_run: dryRun,
        trigger,
        commit_session: true,
      });

      if (result.ok) {
        return jsonSuccess({
          status: "queued",
          message: result.message,
          data: {
            workflow: result.workflow,
            repository: result.repository,
            inputs: result.inputs,
            execution_model: "github_actions",
            stream: null,
            note: "Learning runs on GitHub Actions. Dashboard polls /api/sessions for status.",
          },
        });
      }

      if (!isLocalLearningAllowed()) {
        const http =
          result.status_code >= 400 && result.status_code < 600
            ? result.status_code
            : 422;
        return jsonFailure({
          component: "github.actions",
          reason: result.message,
          error_code: result.error_code || "WORKFLOW_DISPATCH_FAILED",
          recovery_suggestion: result.recovery_suggestion,
          // Never mask config failures as opaque 503
          httpStatus: http === 503 ? 422 : http,
          status: "failed",
          data: {
            workflow: result.workflow,
            repository: result.repository,
            inputs: result.inputs ?? null,
            execution_model: "github_actions",
          },
        });
      }
      // fall through to local when GHA fails on a capable host
    }

    // --- Local one-shot (dev / no GITHUB token) ---
    if (isLocalLearningAllowed()) {
      const local = runLocalLearningSession({
        mission,
        dry_run: dryRun,
        environment,
        trigger,
      });

      if (!local.ok) {
        return jsonFailure({
          component: "local.learning_session",
          reason: local.message,
          error_code: local.error_code || "LOCAL_SESSION_FAILED",
          recovery_suggestion: local.recovery_suggestion,
          session_id: local.session_id ?? null,
          httpStatus:
            local.status_code >= 400 && local.status_code < 600
              ? local.status_code
              : 500,
          status: "failed",
          data: {
            execution_model: "local_oneshot",
            session: local.data ?? null,
            stderr: local.stderr ?? null,
          },
        });
      }

      return jsonSuccess({
        status: local.status || "completed",
        session_id: local.session_id ?? null,
        message: local.message,
        data: {
          ...(local.data || {}),
          execution_model: "local_oneshot",
          workflow: null,
          stream: null,
          note: "Ran automation/ci/learning_session.py once (same entrypoint as GHA).",
        },
      });
    }

    // --- Vercel without token ---
    return jsonFailure({
      component: "github.actions",
      reason:
        "GitHub Actions is not configured. Set IDA_GITHUB_TOKEN (actions:write) and GITHUB_REPOSITORY on this host.",
      error_code: "GITHUB_NOT_CONFIGURED",
      recovery_suggestion:
        "Vercel → Project → Settings → Environment Variables: IDA_GITHUB_TOKEN=ghp_… (PAT with actions:write), GITHUB_REPOSITORY=owner/repo. Redeploy, then Start Learning again.",
      httpStatus: 422,
      status: "failed",
      data: {
        execution_model: "github_actions",
        vercel: Boolean(process.env.VERCEL),
        github_configured: false,
      },
    });
  });
}
