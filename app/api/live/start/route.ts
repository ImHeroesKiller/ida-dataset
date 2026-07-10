import { NextRequest, NextResponse } from "next/server";
import { spawn } from "child_process";
import { getRepoRoot } from "@/lib/paths";

export const dynamic = "force-dynamic";

/**
 * Start a live learning session (background process).
 * Streams events via existing journal → /api/live SSE.
 */
export async function POST(req: NextRequest) {
  if (process.env.VERCEL || process.env.ECC_DISABLE_PYTHON === "1") {
    return NextResponse.json(
      {
        ok: false,
        error:
          "Live Python runtime unavailable on this host. Run locally: python -m automation.learning.live_runtime",
      },
      { status: 503 }
    );
  }

  const body = (await req.json().catch(() => ({}))) as {
    instruction?: string;
    pace?: number;
  };
  const instruction =
    body.instruction?.trim() ||
    "Learn Industry Library knowledge — live session";
  const pace = body.pace ?? 0.7;
  const root = getRepoRoot();

  const child = spawn(
    "python3",
    [
      "-m",
      "automation.learning.live_runtime",
      "--instruction",
      instruction,
      "--pace",
      String(pace),
    ],
    {
      cwd: root,
      env: { ...process.env, PYTHONUNBUFFERED: "1" },
      detached: true,
      stdio: "ignore",
    }
  );
  child.unref();

  return NextResponse.json({
    ok: true,
    message: "Live learning session started",
    pid: child.pid,
    instruction,
    stream: "/api/live",
  });
}
