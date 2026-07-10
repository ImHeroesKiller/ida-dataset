import { NextRequest } from "next/server";
import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import { listSessions, loadSession } from "@/lib/sessions";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/runtime/logs
 * Returns real session logs from stored session files (not local runtime channels).
 */
export async function GET(req: NextRequest) {
  return withApiJson("api.runtime.logs", async () => {
    try {
      const sp = req.nextUrl.searchParams;
      const session_id = sp.get("session_id");
      const limit = Math.min(500, Math.max(1, Number(sp.get("limit") || 100)));

      if (session_id) {
        const session = loadSession(session_id);
        if (!session) {
          return jsonFailure({
            component: "api.runtime.logs",
            reason: `Session not found: ${session_id}`,
            error_code: "SESSION_NOT_FOUND",
            session_id,
            httpStatus: 404,
          });
        }
        const entries = (session.logs || []).slice(-limit).map((line, i) => ({
          channel: "learning",
          message: line,
          session_id,
          seq: i,
        }));
        // Also expose events as structured log rows
        for (const ev of (session.events || []).slice(-limit)) {
          entries.push({
            channel: "learning",
            message: `${ev.verb}: ${ev.detail}`,
            session_id,
            seq: ev.seq ?? 0,
            ...ev,
          } as Record<string, unknown> as {
            channel: string;
            message: string;
            session_id: string;
            seq: number;
          });
        }
        return jsonSuccess({
          status: "ok",
          session_id,
          data: {
            channel: "session",
            count: entries.length,
            entries: entries.slice(0, limit),
            errors: session.errors || [],
          },
        });
      }

      // Aggregate recent session errors / summaries
      const sessions = listSessions({ limit: 20 });
      const entries: Record<string, unknown>[] = [];
      for (const s of sessions) {
        entries.push({
          channel: "learning",
          session_id: s.session_id,
          status: s.status,
          message: s.summary,
          timestamp: s.end_time || s.start_time,
          knowledge_added: s.knowledge_added,
        });
        if (entries.length >= limit) break;
      }

      return jsonSuccess({
        status: "ok",
        data: {
          channel: "sessions",
          count: entries.length,
          entries,
        },
      });
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component: "api.runtime.logs",
        reason: err.message,
        error_code: "LOGS_READ_FAILED",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 500,
      });
    }
  });
}
