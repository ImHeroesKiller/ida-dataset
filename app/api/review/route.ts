import { NextResponse } from "next/server";
import { getReviewQueues } from "@/lib/repo-data";

export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json(getReviewQueues());
}
