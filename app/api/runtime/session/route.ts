import { NextRequest } from "next/server";
import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import {
  listSessions,
  loadLegacySessionEvents,
  loadSession,
} from "@/lib/sessions";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/runtime/session[?session_id=]
 * Session summaries from automation/sessions/ (GHA model).
 */
export async function GET(req: NextRequest) {
  return withApiJson("api.runtime.session", async () => {
    try {
      const sessionId = req.nextUrl.searchParams.get("session_id");
      if (!sessionId) {
        const sessions = listSessions({ limit: 20 });
        const current = sessions[0] || null;
        return jsonSuccess({
          status: current?.status || "idle",
          session_id: current?.session_id ?? null,
          data: {
            session_id: current?.session_id ?? null,
            status: current?.status || "idle",
            sessions,
            execution_model: "github_actions",
          },
        });
      }

      const session = loadSession(sessionId);
      if (session) {
        return jsonSuccess({
          status: String(session.status || "ok"),
          session_id: sessionId,
          data: session,
        });
      }

      const legacy = loadLegacySessionEvents(sessionId);
      if (legacy.length) {
        return jsonSuccess({
          status: "completed",
          session_id: sessionId,
          data: {
            session_id: sessionId,
            events: legacy.length,
            status: "completed",
            legacy: true,
          },
        });
      }

      return jsonFailure({
        component: "api.runtime.session",
        reason: `Session not found: ${sessionId}`,
        error_code: "SESSION_NOT_FOUND",
        session_id: sessionId,
        httpStatus: 404,
      });
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component: "api.runtime.session",
        reason: err.message,
        error_code: "SESSION_READ_FAILED",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 500,
      });
    }
  });
}
