import { NextResponse } from "next/server";
import { getProgress } from "@/lib/orchestration";

export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json({ progress: getProgress() });
}
