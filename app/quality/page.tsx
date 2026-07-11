import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { RoleBadge } from "@/components/ui/badge";
import { getFactoryKpis } from "@/lib/factory-kpis";
import { getReviewQueues } from "@/lib/repo-data";

export const dynamic = "force-dynamic";

export default function QualityPage() {
  const kpis = getFactoryKpis();
  const review = getReviewQueues();
  const confPct =
    kpis.average_confidence != null
      ? Math.round(kpis.average_confidence * 100)
      : null;
  const schema =
    kpis.datasets?.find((d) => d.name === "industry_library")
      ?.schema_completeness ?? 0;
  const dupPct = Math.round((kpis.duplicate_rate || 0) * 1000) / 10;

  return (
    <Shell title="Quality">
      <div className="mx-auto max-w-5xl space-y-8">
        <header>
          <h1 className="text-page-title">Dataset quality</h1>
          <p className="mt-2 text-body text-[var(--text-secondary)]">
            Confidence, completeness, freshness, duplicates, and validation
            gates for published knowledge.
          </p>
        </header>

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          <Metric
            label="Dataset readiness"
            value={String(kpis.dataset_readiness)}
            progress={kpis.dataset_readiness}
          />
          <Metric
            label="Average confidence"
            value={confPct != null ? `${confPct}%` : "—"}
            progress={confPct ?? 0}
          />
          <Metric
            label="Schema completeness"
            value={`${schema}%`}
            progress={schema}
          />
          <Metric
            label="Freshness"
            value={`${kpis.freshness}%`}
            progress={kpis.freshness}
          />
          <Metric
            label="Duplicate rate"
            value={`${dupPct}%`}
            progress={Math.min(100, dupPct * 5)}
            inverse
          />
          <Metric
            label="Pending review"
            value={String(review.counts.pending)}
          />
        </div>

        <Card>
          <CardHeader
            title="Quality policy"
            description="Every published row must carry provenance"
          />
          <CardBody className="space-y-3 text-small text-[var(--text-secondary)]">
            <p>
              Required on every row:{" "}
              <span className="font-semibold text-[var(--text)]">
                Source · Retrieved Date · Confidence · Version
              </span>
            </p>
            <p>
              Checks: Freshness · Schema completeness · Duplicate detection ·
              Validation result
            </p>
            <p>
              Policy: append-only datasets — never rewrite history without
              version bump.
            </p>
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Review queues" description="Human quality gate" />
          <CardBody className="grid grid-cols-3 gap-4">
            <QueueStat
              label="Pending"
              value={review.counts.pending}
              role="warning"
            />
            <QueueStat
              label="Approved"
              value={review.counts.approved}
              role="completed"
            />
            <QueueStat
              label="Rejected"
              value={review.counts.rejected}
              role="error"
            />
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}

function Metric({
  label,
  value,
  progress,
  inverse,
}: {
  label: string;
  value: string;
  progress?: number;
  inverse?: boolean;
}) {
  return (
    <div className="rounded-[var(--radius-xl)] border border-[var(--border)] bg-[var(--panel)] p-6 shadow-[var(--shadow)]">
      <p className="text-caption font-semibold uppercase tracking-wide text-[var(--text-muted)]">
        {label}
      </p>
      <p className="mt-2 text-section-title tabular-nums">{value}</p>
      {progress != null ? (
        <div className="mt-4">
          <Progress value={inverse ? Math.max(0, 100 - progress) : progress} />
        </div>
      ) : null}
    </div>
  );
}

function QueueStat({
  label,
  value,
  role,
}: {
  label: string;
  value: number;
  role: "warning" | "completed" | "error";
}) {
  return (
    <div className="rounded-[var(--radius-lg)] border border-[var(--border)] bg-[var(--panel-2)] p-4 text-center">
      <div className="flex justify-center">
        <RoleBadge role={role}>{label}</RoleBadge>
      </div>
      <p className="mt-3 text-section-title tabular-nums">{value}</p>
    </div>
  );
}
