import { NextRequest } from "next/server";
import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import { dispatchLearningWorkflow } from "@/lib/github-actions";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * POST /api/live/start
 *
 * Triggers GitHub Actions workflow_dispatch on learning.yml.
 * Does NOT spawn local Python. Safe on Vercel.
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

    const result = await dispatchLearningWorkflow({
      mission,
      environment: body.environment || "production",
      // Default dry_run true for safety from dashboard; caller can set false
      dry_run: body.dry_run !== false,
      trigger: body.trigger || "manual",
      commit_session: true,
    });

    if (!result.ok) {
      return jsonFailure({
        component: "github.actions",
        reason: result.message,
        error_code: result.error_code || "WORKFLOW_DISPATCH_FAILED",
        recovery_suggestion: result.recovery_suggestion,
        httpStatus: result.status_code === 404 ? 404 : 503,
        status: "failed",
        data: {
          workflow: result.workflow,
          repository: result.repository,
          inputs: result.inputs ?? null,
          execution_model: "github_actions",
        },
      });
    }

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
  });
}
