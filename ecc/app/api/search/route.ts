import { NextRequest, NextResponse } from "next/server";
import { globalSearch } from "@/lib/repo-data";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  const q = req.nextUrl.searchParams.get("q") ?? "";
  return NextResponse.json(globalSearch(q));
}
