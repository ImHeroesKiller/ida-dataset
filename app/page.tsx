import { Shell } from "@/components/layout/shell";
import { ExecutiveDashboard } from "@/features/dashboard/executive-dashboard";
import { getKnowledgeKpis } from "@/lib/knowledge-kpis";
import { getLearningMode } from "@/lib/learning-mode";
import { getReviewQueues } from "@/lib/repo-data";
import fs from "fs";
import { repoPath } from "@/lib/paths";

export const dynamic = "force-dynamic";

export default function DashboardPage() {
  const kpis = getKnowledgeKpis();
  const review = getReviewQueues();
  const mode = getLearningMode();
  const confidences = [
    ...review.pending,
    ...review.approved.slice(0, 20),
  ].map((c) => Number(c.confidence || 0));
  const avgConf =
    confidences.length > 0
      ? confidences.reduce((a, b) => a + b, 0) / confidences.length
      : null;

  let sources = 0;
  try {
    const p = repoPath("automation/config/sources.yaml");
    if (fs.existsSync(p)) {
      sources = (fs.readFileSync(p, "utf8").match(/id:\s*/g) || []).length;
    }
  } catch {
    sources = 0;
  }

  return (
    <Shell title="Dashboard">
      <ExecutiveDashboard
        kpis={{
          knowledge_coverage: kpis.knowledge_coverage,
          knowledge_added_today: kpis.knowledge_added_today,
          knowledge_updated_today: kpis.knowledge_updated_today,
          knowledge_rejected: kpis.knowledge_rejected,
          pending_review: kpis.pending_review,
          knowledge_quality_score: kpis.knowledge_quality_score,
          average_confidence: avgConf,
          growing_count: kpis.growing_datasets.length,
          gaps_count: kpis.knowledge_gaps.length,
          coverage_message: kpis.answers.how_much_knowledge,
          growth_message: kpis.knowledge_growth_today.message,
          sources_count: sources || undefined,
          mode: mode.mode,
          auto_publish: mode.auto_publish,
        }}
      />
    </Shell>
  );
}
