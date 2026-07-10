import { NextResponse } from "next/server";
import { getKnowledgeKpis } from "@/lib/knowledge-kpis";

export const dynamic = "force-dynamic";

export async function GET() {
  const k = getKnowledgeKpis();
  return NextResponse.json({
    journal: k.learning_journal,
    kpis: {
      coverage: k.knowledge_coverage,
      added_today: k.knowledge_added_today,
      pending_review: k.pending_review,
      first_knowledge: k.first_knowledge,
    },
  });
}
