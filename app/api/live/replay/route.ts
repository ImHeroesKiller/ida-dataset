import { NextRequest } from "next/server";
import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import {
  listLegacySessions,
  listSessions,
  loadLegacySessionEvents,
  loadSession,
} from "@/lib/sessions";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/live/replay[?session_id=]
 * Replay from stored session files (GHA sessions + legacy jsonl).
 */
export async function GET(req: NextRequest) {
  return withApiJson("api.live.replay", async () => {
    try {
      const sessionId = req.nextUrl.searchParams.get("session_id");

      if (!sessionId) {
        const sessions = [
          ...listSessions({ limit: 100 }),
          ...listLegacySessions(),
        ];
        return jsonSuccess({
          status: "ok",
          data: {
            sessions: sessions.map((s) => ({
              session_id: s.session_id,
              events: s.events ?? 0,
              started: s.start_time,
              ended: s.end_time,
              last_verb: s.summary,
              status: s.status,
              mission: s.mission,
              knowledge_added: s.knowledge_added,
            })),
          },
        });
      }

      const session = loadSession(sessionId);
      if (session) {
        return jsonSuccess({
          status: "ok",
          session_id: sessionId,
          data: {
            session_id: sessionId,
            events: session.events || [],
            session,
          },
        });
      }

      const legacy = loadLegacySessionEvents(sessionId);
      if (legacy.length) {
        return jsonSuccess({
          status: "ok",
          session_id: sessionId,
          data: {
            session_id: sessionId,
            events: legacy,
          },
        });
      }

      return jsonFailure({
        component: "api.live.replay",
        reason: `session not found: ${sessionId}`,
        error_code: "SESSION_NOT_FOUND",
        session_id: sessionId,
        httpStatus: 404,
      });
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component: "api.live.replay",
        reason: err.message,
        error_code: "REPLAY_FAILED",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 500,
      });
    }
  });
}
