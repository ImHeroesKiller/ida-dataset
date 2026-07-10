import { NextResponse } from "next/server";
import { listQueuedDocuments } from "@/lib/network";

export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json(listQueuedDocuments());
}
