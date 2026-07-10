import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import { getSessionsDashboard } from "@/lib/sessions";
import {
  getActionsLearningStatus,
  isGithubConfigured,
  resolveRepository,
} from "@/lib/github-actions";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/runtime/debug — GitHub Actions learning model diagnostics.
 */
export async function GET() {
  return withApiJson("api.runtime.debug", async () => {
    try {
      const dash = getSessionsDashboard();
      const actions = await getActionsLearningStatus();

      return jsonSuccess({
        status: actions.running ? "running" : dash.status,
        session_id: dash.current_session?.session_id ?? null,
        data: {
          execution_model: "github_actions",
          local_runtime: "removed",
          python_spawn: false,
          sse_runtime: false,
          github_configured: isGithubConfigured(),
          repository: resolveRepository(),
          github_actions: actions,
          sessions_dashboard: {
            status: dash.status,
            session_count: dash.sessions?.length ?? 0,
            next_scheduled_run: dash.next_scheduled_run,
            history: dash.history,
          },
          active_session: dash.current_session,
          note:
            "Learning executes entirely on GitHub Actions. Dashboard monitors sessions and dispatches workflows.",
        },
      });
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component: "api.runtime.debug",
        reason: err.message,
        error_code: "DEBUG_FAILED",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 500,
      });
    }
  });
}
