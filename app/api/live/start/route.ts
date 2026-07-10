import { NextRequest } from "next/server";
import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import { startLiveRuntime, writeFailureLog } from "@/lib/runtime-manager";
import { getRepoRoot } from "@/lib/paths";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * POST /api/live/start
 *
 * Always returns valid JSON (never empty / HTML).
 *
 * Success envelope:
 *   { success: true, status, session_id, data: { pid, stream, ... } }
 *
 * Failure envelope (including HTTP 503 root causes):
 *   { success: false, status: "failed", component, reason, error_code,
 *     correlation_id, session_id, recovery_suggestion, failure }
 *
 * Documented 503 components:
 *   host.vercel | host.ecc_disable_python | host.python_missing
 *   | host.python_import | runtime.spawn | runtime.process | runtime.manager
 */
export async function POST(req: NextRequest) {
  return withApiJson("api.live.start", async () => {
    let body: { instruction?: string; pace?: number } = {};
    try {
      const text = await req.text();
      if (text && text.trim()) {
        body = JSON.parse(text) as { instruction?: string; pace?: number };
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
        recovery_suggestion: "Send Content-Type application/json with a valid object.",
      });
    }

    const result = await startLiveRuntime({
      instruction: body.instruction,
      pace: body.pace,
    });

    if (!result.ok) {
      // Persist structured log for every failed start (including 503)
      try {
        if (result.failure) {
          writeFailureLog(result.failure, getRepoRoot());
        }
      } catch {
        /* never fail the response */
      }

      const http = result.status_code || 503;
      return jsonFailure({
        component: result.failure?.component || "runtime.start",
        reason: result.message || result.failure?.message || "Runtime start failed",
        error_code:
          result.failure?.exception ||
          (http === 409 ? "ALREADY_RUNNING" : "RUNTIME_START_FAILED"),
        correlation_id: result.correlation_id,
        session_id: result.session_id ?? result.status?.session_id ?? null,
        recovery_suggestion:
          result.recovery_suggestion || result.failure?.recovery_suggestion,
        stack_trace: result.failure?.stack_trace,
        exception: result.failure?.exception,
        recovery_action: result.failure?.recovery_action,
        status: "failed",
        httpStatus: http,
        data: {
          pid: result.pid ?? null,
          instruction: result.instruction ?? null,
          host_capabilities: result.status?.host_capabilities ?? null,
          runtime_status: result.status ?? null,
          failure_meta: result.failure?.meta ?? null,
        },
      });
    }

    return jsonSuccess({
      status: result.status?.status || "running",
      session_id: result.session_id ?? result.status?.session_id ?? null,
      correlation_id: result.correlation_id,
      message: result.message,
      data: {
        pid: result.pid ?? null,
        instruction: result.instruction,
        stream: result.stream || "/api/live",
        correlation_id: result.correlation_id,
        runtime: result.status ?? null,
      },
    });
  });
}
