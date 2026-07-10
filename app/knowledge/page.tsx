import { Shell } from "@/components/layout/shell";
import { KnowledgeClient } from "@/components/shared/knowledge-client";
import { getKnowledgeOverview } from "@/lib/knowledge-catalog";

export const dynamic = "force-dynamic";

export default function KnowledgePage() {
  const categories = getKnowledgeOverview();
  return (
    <Shell title="Knowledge">
      <KnowledgeClient categories={categories} />
    </Shell>
  );
}
