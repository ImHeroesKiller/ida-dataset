import { Shell } from "@/components/layout/shell";
import { ExecutiveDashboard } from "@/features/dashboard/executive-dashboard";
import { getKnowledgeKpis } from "@/lib/knowledge-kpis";
import { getLearningMode } from "@/lib/learning-mode";
import { getReviewQueues } from "@/lib/repo-data";

export const dynamic = "force-dynamic";

export default function DashboardPage() {
  const kpis = getKnowledgeKpis();
  const review = getReviewQueues();
  const mode = getLearningMode();
  const industry = kpis.industry_library;
  const avgConf =
    kpis.average_confidence ??
    (review.pending.length
      ? review.pending.reduce((a, c) => a + Number(c.confidence || 0), 0) /
        review.pending.length
      : null);

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
          growing_count: industry.total_industries,
          gaps_count: kpis.knowledge_gaps.length,
          coverage_message: kpis.answers.how_much_knowledge,
          growth_message: kpis.knowledge_growth_today.message,
          sources_count: kpis.sources_count,
          mode: mode.mode,
          auto_publish: mode.auto_publish,
          total_industries: industry.total_industries,
          industries_learned: industry.total_industries,
          field_coverage_pct: industry.field_coverage_pct,
          coverage_progress_pct: industry.coverage_progress_pct,
          verified_sources: industry.verified_sources,
          knowledge_freshness_pct: industry.knowledge_freshness_pct,
          duplicate_rate: industry.duplicate_rate,
          dataset_version: kpis.dataset_version,
          last_successful_session: kpis.last_successful_session,
          current_source: kpis.current_source,
          current_document: kpis.current_document,
          current_mission: kpis.current_mission,
          latest_industry: industry.latest
            ? `${industry.latest.id} ${industry.latest.name}`
            : null,
          industry_names: industry.industries.map((i) => i.name),
        }}
      />
    </Shell>
  );
}
