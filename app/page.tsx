import { Shell } from "@/components/layout/shell";
import { LiveDashboard } from "@/components/shared/live-dashboard";
import { getKnowledgeKpis } from "@/lib/knowledge-kpis";

export const dynamic = "force-dynamic";

export default function DashboardPage() {
  const kpis = getKnowledgeKpis();
  return (
    <Shell title="IDA Learning Dashboard">
      <LiveDashboard
        initialKpis={{
          knowledge_coverage: kpis.knowledge_coverage,
          knowledge_added_today: kpis.knowledge_added_today,
          knowledge_updated_today: kpis.knowledge_updated_today,
          knowledge_rejected: kpis.knowledge_rejected,
          pending_review: kpis.pending_review,
          growing_datasets: kpis.growing_datasets,
          knowledge_gaps: kpis.knowledge_gaps,
          first_knowledge: kpis.first_knowledge,
        }}
      />
    </Shell>
  );
}
