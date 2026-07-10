import { NextRequest } from "next/server";
import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import {
  getSessionsDashboard,
  loadLegacySessionEvents,
  loadSession,
} from "@/lib/sessions";
import { getActionsLearningStatus } from "@/lib/github-actions";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/sessions
 * GET /api/sessions?session_id=SESSION-...
 *
 * Reads committed session files + GitHub Actions run status.
 * No local Python runtime. Safe on Vercel.
 */
export async function GET(req: NextRequest) {
  return withApiJson("api.sessions", async () => {
    try {
      const sessionId = req.nextUrl.searchParams.get("session_id");

      if (sessionId) {
        let session = loadSession(sessionId);
        let events = session?.events || [];
        if (!session) {
          // Legacy SES-*.jsonl fallback
          events = loadLegacySessionEvents(sessionId);
          if (!events.length) {
            return jsonFailure({
              component: "api.sessions",
              reason: `Session not found: ${sessionId}`,
              error_code: "SESSION_NOT_FOUND",
              session_id: sessionId,
              httpStatus: 404,
            });
          }
          session = {
            session_id: sessionId,
            status: "completed",
            events,
            logs: events.map(
              (e) => `[${e.ts || ""}] ${e.verb}: ${e.detail}`
            ),
            summary: "Legacy session",
            trigger: "legacy",
          };
        }
        return jsonSuccess({
          status: String(session.status || "ok"),
          session_id: sessionId,
          data: {
            session,
            events: session.events || events,
            logs: session.logs || [],
          },
        });
      }

      const dash = getSessionsDashboard();
      const actions = await getActionsLearningStatus();

      // Merge Actions running state into dashboard status
      let status = dash.status;
      if (actions.running) status = "running";
      else if (actions.queued) status = "running";

      return jsonSuccess({
        status,
        session_id: dash.current_session?.session_id ?? null,
        data: {
          ...dash,
          status,
          current_status: status,
          next_scheduled_run:
            actions.next_scheduled_hint || dash.next_scheduled_run,
          github_actions: actions,
        },
      });
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component: "api.sessions",
        reason: err.message,
        error_code: "SESSIONS_READ_FAILED",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 500,
      });
    }
  });
}
