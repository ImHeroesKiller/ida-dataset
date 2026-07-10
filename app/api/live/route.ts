import { NextRequest } from "next/server";
import {
  jsonFailure,
  jsonSuccess,
  withApiJson,
} from "@/lib/api-contract";
import { getSessionsDashboard, loadSession } from "@/lib/sessions";
import { getActionsLearningStatus } from "@/lib/github-actions";
import { getKnowledgeKpis } from "@/lib/knowledge-kpis";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/live
 *
 * Formerly server-side SSE tailing a local Python journal.
 * Now returns a JSON snapshot of learning sessions + GitHub Actions status.
 * Clients poll this (or /api/sessions) — no long-lived SSE runtime.
 */
export async function GET(req: NextRequest) {
  // Keep EventSource clients from hanging: if Accept prefers event-stream,
  // return a short-lived SSE that pushes one snapshot then closes.
  const accept = req.headers.get("accept") || "";
  if (accept.includes("text/event-stream")) {
    const dash = getSessionsDashboard();
    const actions = await getActionsLearningStatus();
    const status = actions.running || actions.queued ? "running" : dash.status;
    const sessionId = dash.current_session?.session_id;
    const session = sessionId ? loadSession(sessionId) : null;
    const kpis = getKnowledgeKpis();

    const enc = new TextEncoder();
    const snapshot = {
      status,
      activity: {
        status,
        session_id: sessionId,
        progress: status === "running" ? 10 : session?.status === "completed" ? 100 : 0,
        current_thought:
          session?.summary ||
          (status === "running"
            ? "GitHub Actions learning session running"
            : "Idle — Continuous Learning via GitHub Actions"),
        current_task: session?.mission || dash.current_mission,
        execution_model: "github_actions",
        updated_at: new Date().toISOString(),
      },
      kpis,
      github_actions: actions,
      sessions: dash.sessions?.slice(0, 10),
    };

    const stream = new ReadableStream({
      start(controller) {
        controller.enqueue(
          enc.encode(
            `event: hello\ndata: ${JSON.stringify({
              ts: new Date().toISOString(),
              message: "Learning session monitor (no local runtime)",
              execution_model: "github_actions",
            })}\n\n`
          )
        );
        controller.enqueue(
          enc.encode(
            `event: activity\ndata: ${JSON.stringify(snapshot.activity)}\n\n`
          )
        );
        controller.enqueue(
          enc.encode(`event: kpis\ndata: ${JSON.stringify(kpis)}\n\n`)
        );
        if (session?.events?.length) {
          // Send last few real session events (not fake stream)
          for (const ev of session.events.slice(-30)) {
            controller.enqueue(
              enc.encode(`event: journal\ndata: ${JSON.stringify(ev)}\n\n`)
            );
          }
        }
        controller.enqueue(
          enc.encode(
            `event: snapshot\ndata: ${JSON.stringify(snapshot)}\n\n`
          )
        );
        // Close — clients should poll /api/sessions; no long-lived connection
        controller.close();
      },
    });

    return new Response(stream, {
      headers: {
        "Content-Type": "text/event-stream; charset=utf-8",
        "Cache-Control": "no-cache, no-transform",
        Connection: "close",
      },
    });
  }

  return withApiJson("api.live", async () => {
    try {
      const dash = getSessionsDashboard();
      const actions = await getActionsLearningStatus();
      const status = actions.running || actions.queued ? "running" : dash.status;
      return jsonSuccess({
        status,
        session_id: dash.current_session?.session_id ?? null,
        data: {
          ...dash,
          status,
          github_actions: actions,
          execution_model: "github_actions",
          kpis: getKnowledgeKpis(),
        },
      });
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      return jsonFailure({
        component: "api.live",
        reason: err.message,
        error_code: "LIVE_SNAPSHOT_FAILED",
        exception: err.name,
        stack_trace: err.stack,
        httpStatus: 500,
      });
    }
  });
}
