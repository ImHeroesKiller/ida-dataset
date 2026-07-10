import { NextRequest, NextResponse } from "next/server";
import {
  getLearningDashboard,
  runSchedulerCli,
} from "@/lib/learning";

export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json(getLearningDashboard());
}

export async function POST(req: NextRequest) {
  const body = (await req.json().catch(() => ({}))) as {
    action?: string;
    text?: string;
    mission_id?: string;
    priority?: string;
    dry_run?: boolean;
  };

  const action = body.action || "dashboard";

  if (action === "dashboard") {
    return NextResponse.json(getLearningDashboard());
  }

  if (action === "tick") {
    const args = ["tick"];
    if (body.dry_run === false) args.push("--no-dry-run");
    else args.push("--dry-run");
    const result = runSchedulerCli(args);
    return NextResponse.json(
      { ok: result.ok, result: result.data, stderr: result.stderr },
      { status: result.ok ? 200 : 503 }
    );
  }

  if (action === "mission") {
    if (!body.text?.trim()) {
      return NextResponse.json({ error: "text required" }, { status: 400 });
    }
    const args = ["mission", body.text];
    if (body.priority) args.push("--priority", body.priority);
    const result = runSchedulerCli(args);
    return NextResponse.json(
      { ok: result.ok, result: result.data, stderr: result.stderr },
      { status: result.ok ? 200 : 503 }
    );
  }

  if (action === "complete" && body.mission_id) {
    const result = runSchedulerCli(["complete", body.mission_id]);
    return NextResponse.json(
      { ok: result.ok, result: result.data, stderr: result.stderr },
      { status: result.ok ? 200 : 503 }
    );
  }

  return NextResponse.json({ error: "unknown action" }, { status: 400 });
}
