import { NextResponse } from "next/server";
import { getNetworkDashboard, runNetworkCli } from "@/lib/network";

export const dynamic = "force-dynamic";

export async function GET() {
  const live = runNetworkCli(["list"]);
  if (live.ok) {
    return NextResponse.json({ connectors: live.data });
  }
  const dash = getNetworkDashboard();
  return NextResponse.json({
    connectors: dash.connectors || [],
    source: "fallback",
  });
}
