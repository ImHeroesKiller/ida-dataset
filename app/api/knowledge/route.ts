import { NextRequest, NextResponse } from "next/server";
import {
  getCategoryDetail,
  getKnowledgeOverview,
} from "@/lib/knowledge-catalog";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  const category = req.nextUrl.searchParams.get("category");
  if (category) {
    const detail = getCategoryDetail(category);
    if (!detail) {
      return NextResponse.json({ ok: false, error: "not_found" }, { status: 404 });
    }
    return NextResponse.json({ ok: true, ...detail });
  }
  return NextResponse.json({
    ok: true,
    categories: getKnowledgeOverview(),
  });
}
