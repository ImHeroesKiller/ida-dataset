import { NextRequest, NextResponse } from "next/server";
import { getLearningMode } from "@/lib/learning-mode";
import {
  autoEnqueuePending,
  getPublishDashboard,
  publishOne,
  runProgressiveDrain,
} from "@/lib/progressive-publish";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";
export const maxDuration = 300;

/**
 * GET  /api/publish-queue — status, queue, feed, journal tail
 * POST /api/publish-queue { action: "tick" | "start" | "enqueue" }
 *
 * tick  — publish exactly one row (backend)
 * start — drain queue with configured backend delay
 * enqueue — move pending → publish (dev auto)
 */
export async function GET() {
  try {
    const dash = getPublishDashboard();
    return NextResponse.json({
      ok: true,
      learning_mode: getLearningMode(),
      ...dash,
    });
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    return NextResponse.json({ ok: false, error: err.message }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const body = (await req.json().catch(() => ({}))) as {
      action?: string;
      max?: number;
    };
    const action = body.action || "tick";
    const mode = getLearningMode();

    if (action === "enqueue") {
      const r = autoEnqueuePending();
      return NextResponse.json({
        ok: true,
        ...r,
        learning_mode: mode,
        ...getPublishDashboard(),
      });
    }

    if (action === "tick") {
      if (mode.auto_publish) autoEnqueuePending();
      const r = publishOne();
      return NextResponse.json({
        ok: r.ok,
        result: r,
        learning_mode: mode,
        ...getPublishDashboard(),
      });
    }

    if (action === "start") {
      if (!mode.auto_publish && mode.mode === "production") {
        return NextResponse.json(
          {
            ok: false,
            error: "Auto publish disabled in production mode",
            learning_mode: mode,
          },
          { status: 403 }
        );
      }
      autoEnqueuePending();
      // Backend-paced drain (sleep between rows)
      const state = await runProgressiveDrain({ max: body.max ?? 500 });
      return NextResponse.json({
        ok: true,
        drained: true,
        state,
        learning_mode: mode,
        ...getPublishDashboard(),
      });
    }

    return NextResponse.json(
      { ok: false, error: "unknown_action", hint: "tick | start | enqueue" },
      { status: 400 }
    );
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    const readOnly = /EROFS|read-only|EACCES/i.test(err.message);
    return NextResponse.json(
      {
        ok: false,
        error: err.message,
        error_code: readOnly ? "READ_ONLY_FS" : "PUBLISH_FAILED",
      },
      { status: readOnly ? 503 : 500 }
    );
  }
}
