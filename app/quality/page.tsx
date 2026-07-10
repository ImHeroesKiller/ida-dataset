import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { getFactoryKpis } from "@/lib/factory-kpis";
import { getReviewQueues } from "@/lib/repo-data";

export const dynamic = "force-dynamic";

export default function QualityPage() {
  const kpis = getFactoryKpis();
  const review = getReviewQueues();

  return (
    <Shell title="Quality">
      <div className="mx-auto max-w-5xl space-y-6">
        <header>
          <h1 className="text-2xl font-semibold text-[var(--text)]">
            Dataset Quality
          </h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            Confidence, completeness, freshness, duplicates, and validation gates.
          </p>
        </header>

        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          <Stat label="Quality score" value={String(kpis.dataset_quality)} />
          <Stat
            label="Average confidence"
            value={
              kpis.average_confidence != null
                ? `${Math.round(kpis.average_confidence * 100)}%`
                : "—"
            }
          />
          <Stat
            label="Schema completeness"
            value={`${kpis.schema_completeness}%`}
          />
          <Stat
            label="Source freshness"
            value={`${kpis.source_freshness}%`}
          />
          <Stat
            label="Duplicate rate"
            value={`${Math.round(kpis.duplicate_rate * 100)}%`}
          />
          <Stat label="Pending review" value={String(review.counts.pending)} />
        </div>

        <Card>
          <CardHeader
            title="Quality policy"
            description="Every published row must carry provenance"
          />
          <CardBody className="space-y-2 text-sm text-[var(--text-muted)]">
            <p>Required on every row: Source · Retrieved Date · Confidence · Version</p>
            <p>Checks: Freshness · Schema completeness · Duplicate detection · Validation result</p>
            <p>Policy: append-only datasets — never rewrite history without version bump.</p>
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Review queues" description="Human quality gate" />
          <CardBody className="grid grid-cols-3 gap-3 text-center">
            <Stat label="Pending" value={String(review.counts.pending)} />
            <Stat label="Approved" value={String(review.counts.approved)} />
            <Stat label="Rejected" value={String(review.counts.rejected)} />
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-2xl border border-[var(--border)] bg-[var(--panel)] px-4 py-4">
      <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
        {label}
      </p>
      <p className="mt-2 text-2xl font-semibold text-[var(--text)]">{value}</p>
    </div>
  );
}
