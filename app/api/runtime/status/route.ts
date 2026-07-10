import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import { getSessionsDashboard } from "@/lib/sessions";
import { getActionsLearningStatus } from "@/lib/github-actions";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/runtime/status
 *
 * Compatibility endpoint: now reports GitHub Actions learning status,
 * not a local Python process.
 */
export async function GET() {
  return withApiJson("api.runtime.status", async () => {
    try {
      const dash = getSessionsDashboard();
      const actions = await getActionsLearningStatus();
      const status = actions.running || actions.queued ? "running" : dash.status;
      const current = dash.current_session || dash.last_successful_run;

      return jsonSuccess({
        status,
        session_id: current?.session_id ?? null,
        data: {
          status,
          session_id: current?.session_id ?? null,
          correlation_id: null,
          started_at: current?.start_time ?? null,
          stopped_at: current?.end_time ?? null,
          current_stage: status === "running" ? "github_actions" : "idle",
          current_task: dash.current_mission || current?.mission || null,
          documents_processed: 0,
          knowledge_candidates: Number(dash.knowledge_added || 0),
          uptime_seconds: Number(dash.session_duration || 0),
          pid: null,
          instruction: dash.current_mission,
          last_error: dash.last_failed_run
            ? {
                message: dash.last_failed_run.summary,
                session_id: dash.last_failed_run.session_id,
              }
            : null,
          health: {
            runtime: "disabled",
            scheduler: "healthy",
            connector: "healthy",
            queue: "healthy",
            sse: "disabled",
            publisher: "healthy",
            github_actions: actions.configured ? "healthy" : "warning",
          },
          overall_health: actions.configured ? "healthy" : "warning",
          health_details: {
            note: "Local runtime removed. Learning executes via GitHub Actions.",
            github_actions: actions,
          },
          host_capabilities: {
            can_spawn_runtime: false,
            vercel: Boolean(process.env.VERCEL),
            execution_model: "github_actions",
            github_configured: actions.configured,
          },
          execution_model: "github_actions",
          next_scheduled_run: dash.next_scheduled_run,
          knowledge_added: dash.knowledge_added,
          knowledge_updated: dash.knowledge_updated,
          knowledge_rejected: dash.knowledge_rejected,
          updated_at: new Date().toISOString(),
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
      });
    }
  });
}
