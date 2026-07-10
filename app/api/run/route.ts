import { NextRequest, NextResponse } from "next/server";
import {
  dispatchLearningWorkflow,
  isGithubConfigured,
} from "@/lib/github-actions";

export const dynamic = "force-dynamic";
export const runtime = "nodejs";

const ALLOWED = new Set(["learn", "validate", "quality", "publish", "export"]);

/**
 * Factory job dispatch — dataset production only.
 * Prefer GitHub Actions; no local crawler spawn.
 */
export async function POST(req: NextRequest) {
  const body = (await req.json().catch(() => ({}))) as {
    action?: string;
    mission?: string;
    environment?: string;
    dry_run?: boolean;
  };
  const action = body.action || "learn";
  if (!ALLOWED.has(action)) {
    return NextResponse.json(
      {
        ok: false,
        error: "Invalid action",
        allowed: Array.from(ALLOWED),
        note: "Factory jobs only: learn | validate | quality | publish | export",
      },
      { status: 400 }
    );
  }

  if (action === "learn") {
    if (!isGithubConfigured()) {
      return NextResponse.json(
        {
          ok: false,
          error_code: "GITHUB_NOT_CONFIGURED",
          message:
            "Set IDA_GITHUB_TOKEN to dispatch the learn workflow on GitHub Actions.",
        },
        { status: 422 }
      );
    }
    const result = await dispatchLearningWorkflow({
      mission:
        body.mission ||
        "Expand Industry Library — factory learn cycle",
      environment: body.environment || "production",
      dry_run: body.dry_run !== false,
      trigger: "manual",
      commit_session: true,
    });
    return NextResponse.json(
      {
        action,
        factory: "IDA Dataset Factory",
        ...result,
      },
      { status: result.ok ? 200 : 422 }
    );
  }

  return NextResponse.json({
    ok: true,
    action,
    message: `Job '${action}' should be run via GitHub Actions workflow (${action}.yml).`,
    factory: "IDA Dataset Factory",
  });
}
