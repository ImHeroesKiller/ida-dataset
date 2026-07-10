import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import {
  computeHealthBundle,
  readRuntimeStatus,
} from "@/lib/runtime-manager";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/runtime/status — always valid JSON.
 */
export async function GET() {
  return withApiJson("api.runtime.status", async () => {
    try {
      const status = readRuntimeStatus();
      const health = computeHealthBundle();
      return jsonSuccess({
        status: String(status.status || "idle"),
        session_id: status.session_id,
        correlation_id: status.correlation_id,
        data: {
          status: status.status,
          session_id: status.session_id,
          correlation_id: status.correlation_id,
          started_at: status.started_at,
          stopped_at: status.stopped_at,
          current_stage: status.current_stage,
          current_task: status.current_task,
          documents_processed: status.documents_processed,
          knowledge_candidates: status.knowledge_candidates,
          uptime_seconds: status.uptime_seconds,
          pid: status.pid,
          instruction: status.instruction,
          last_error: status.last_error,
          health: health.components,
          overall_health: health.overall,
          health_details: health.details,
          host_capabilities: status.host_capabilities,
          updated_at: status.updated_at,
        },
      });
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component: "api.runtime.status",
        reason: err.message,
        error_code: "STATUS_READ_FAILED",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 500,
        recovery_suggestion: "Check automation/runtime/state permissions.",
      });
    }
  });
}
