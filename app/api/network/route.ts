import { NextRequest, NextResponse } from "next/server";
import {
  getNetworkDashboard,
  runNetworkCli,
  runSearchCli,
} from "@/lib/network";

export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json(getNetworkDashboard());
}

export async function POST(req: NextRequest) {
  const body = (await req.json().catch(() => ({}))) as {
    action?: string;
    query?: string;
    limit?: number;
  };
  const action = body.action || "dashboard";

  if (action === "dashboard") {
    return NextResponse.json(getNetworkDashboard());
  }
  if (action === "health") {
    const r = runNetworkCli(["health"]);
    return NextResponse.json(
      { ok: r.ok, result: r.data, stderr: r.stderr },
      { status: r.ok ? 200 : 503 }
    );
  }
  if (action === "search") {
    if (!body.query?.trim()) {
      return NextResponse.json({ error: "query required" }, { status: 400 });
    }
    const r = runSearchCli(body.query, body.limit ?? 5);
    return NextResponse.json(
      { ok: r.ok, result: r.data, stderr: r.stderr },
      { status: r.ok ? 200 : 503 }
    );
  }
  if (action === "connect") {
    const r = runNetworkCli(["connect"]);
    return NextResponse.json(
      { ok: r.ok, result: r.data, stderr: r.stderr },
      { status: r.ok ? 200 : 503 }
    );
  }
  return NextResponse.json({ error: "unknown action" }, { status: 400 });
}
