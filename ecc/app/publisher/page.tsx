import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { getReviewQueues, getGitStatus, getPolicies } from "@/lib/repo-data";
import { PublisherClient } from "@/components/shared/publisher-client";

export const dynamic = "force-dynamic";

export default function PublisherPage() {
  const review = getReviewQueues();
  const git = getGitStatus();
  const policies = getPolicies();
  const features = ((policies.data as { features?: Record<string, boolean> } | null)
    ?.features ?? {}) as Record<string, boolean>;
  const reviewRequired = Boolean(
    (policies.data as { review_required?: boolean } | null)?.review_required ?? true
  );

  const datasetsAffected = Array.from(
    new Set(review.approved.map((c) => c.target_dataset).filter(Boolean))
  );

  return (
    <Shell title="Publisher">
      <div className="mb-3 space-y-2">
        <p className="text-sm text-zinc-300">
          Append-only publish after Review. Never invoked without Planner →
          Policy → Review path.
        </p>
        <div className="flex flex-wrap gap-1.5">
          <Badge>approved={review.counts.approved}</Badge>
          <Badge>review_required={String(reviewRequired)}</Badge>
          <Badge>
            publishing_enabled={String(Boolean(features.publishing_enabled))}
          </Badge>
          <Badge>
            git={git.available ? `${git.branch}@${git.commit}` : "n/a"}
          </Badge>
        </div>
      </div>

      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader
            title="Pending Publish"
            description="Approved candidates only"
          />
          <CardBody className="space-y-1 text-xs">
            {review.approved.length === 0 ? (
              <p className="text-zinc-500">Waiting for first execution</p>
            ) : (
              review.approved.map((c) => (
                <div
                  key={c.candidate_id}
                  className="flex justify-between border-b border-zinc-900 py-1.5 text-zinc-300"
                >
                  <span className="font-mono text-[11px]">{c.candidate_id}</span>
                  <span className="text-zinc-500">{c.target_dataset}</span>
                </div>
              ))
            )}
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Datasets affected" description="From approved queue" />
          <CardBody className="space-y-1 text-xs text-zinc-300">
            {datasetsAffected.length === 0 ? (
              <p className="text-zinc-500">None</p>
            ) : (
              datasetsAffected.map((d) => <div key={d}>{d}</div>)
            )}
          </CardBody>
        </Card>
      </div>

      <div className="mt-3">
        <Card>
          <CardHeader
            title="Git Diff Summary"
            description="Working tree status (append-only publish creates diffs later)"
          />
          <CardBody>
            <pre className="overflow-x-auto rounded-md border border-zinc-900 bg-zinc-950 p-3 font-mono text-[11px] text-zinc-400">
              {git.statusLines.length
                ? git.statusLines.join("\n")
                : git.available
                  ? "(clean working tree)"
                  : "Waiting for first execution"}
            </pre>
          </CardBody>
        </Card>
      </div>

      <div className="mt-3">
        <PublisherClient
          approvedCount={review.counts.approved}
          publishingEnabled={Boolean(features.publishing_enabled)}
          reviewRequired={reviewRequired}
        />
      </div>
    </Shell>
  );
}
