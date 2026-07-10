import { NextRequest, NextResponse } from "next/server";
import {
  approveAndPublish,
  getReviewDashboard,
  loadFullCandidate,
  rejectCandidate,
} from "@/lib/review-actions";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

/**
 * GET /api/review
 * GET /api/review?candidate_id=CAND-...
 *
 * POST /api/review
 *   { action: "approve" | "reject", candidate_id, reason?, publish?, reviewer? }
 *   { action: "bulk_approve" | "bulk_reject", candidate_ids: string[] }
 */
export async function GET(req: NextRequest) {
  try {
    const candidateId = req.nextUrl.searchParams.get("candidate_id");
    if (candidateId) {
      const c = loadFullCandidate(candidateId);
      if (!c) {
        return NextResponse.json(
          { ok: false, error: "not_found", candidate_id: candidateId },
          { status: 404 }
        );
      }
      return NextResponse.json({
        ok: true,
        candidate: c,
      });
    }
    return NextResponse.json({ ok: true, ...getReviewDashboard() });
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    return NextResponse.json(
      { ok: false, error: err.message },
      { status: 500 }
    );
  }
}

export async function POST(req: NextRequest) {
  try {
    const body = (await req.json().catch(() => ({}))) as {
      action?: string;
      candidate_id?: string;
      candidate_ids?: string[];
      reason?: string;
      publish?: boolean;
      reviewer?: string;
    };

    const action = body.action || "";
    const reviewer = body.reviewer || "executive-reviewer";

    if (action === "approve" && body.candidate_id) {
      const result = approveAndPublish(body.candidate_id, {
        reviewer,
        publish: body.publish !== false,
      });
      return NextResponse.json(
        { ok: result.ok, result, queues: getReviewDashboard() },
        { status: result.ok ? 200 : result.error_code === "NOT_FOUND" ? 404 : 400 }
      );
    }

    if (action === "reject" && body.candidate_id) {
      const result = rejectCandidate(body.candidate_id, {
        reviewer,
        reason: body.reason,
      });
      return NextResponse.json(
        { ok: result.ok, result, queues: getReviewDashboard() },
        { status: result.ok ? 200 : result.error_code === "NOT_FOUND" ? 404 : 400 }
      );
    }

    if (
      (action === "bulk_approve" || action === "bulk_reject") &&
      Array.isArray(body.candidate_ids)
    ) {
      const results = body.candidate_ids.map((id) =>
        action === "bulk_approve"
          ? approveAndPublish(id, { reviewer, publish: body.publish !== false })
          : rejectCandidate(id, { reviewer, reason: body.reason })
      );
      const ok = results.every((r) => r.ok);
      return NextResponse.json({
        ok,
        results,
        queues: getReviewDashboard(),
      });
    }

    return NextResponse.json(
      {
        ok: false,
        error: "unknown_action",
        hint: "Use approve | reject | bulk_approve | bulk_reject",
      },
      { status: 400 }
    );
  } catch (e) {
    const err = e instanceof Error ? e : new Error(String(e));
    return NextResponse.json(
      {
        ok: false,
        error: err.message,
        error_code:
          /EROFS|read-only|EACCES/i.test(err.message)
            ? "READ_ONLY_FS"
            : "REVIEW_FAILED",
        recovery:
          "Review writes queue files under automation/queue/. On Vercel this filesystem is read-only — run review locally or via a writable host.",
      },
      { status: 503 }
    );
  }
}
