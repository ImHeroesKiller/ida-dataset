import { Shell } from "@/components/layout/shell";
import { getReviewQueues } from "@/lib/repo-data";
import { ReviewClient } from "@/components/shared/review-client";

export const dynamic = "force-dynamic";

export default function ReviewPage() {
  const queues = getReviewQueues();
  return (
    <Shell title="Review Queue">
      <div className="mb-3 space-y-1">
        <p className="text-sm text-zinc-300">
          Human decisions only. No direct publishing from this view.
        </p>
        <p className="text-xs text-zinc-500">
          Pending {queues.counts.pending} · Approved {queues.counts.approved} ·
          Rejected {queues.counts.rejected}
        </p>
      </div>
      <ReviewClient
        pending={queues.pending}
        approved={queues.approved}
        rejected={queues.rejected}
        waiting={queues.waiting}
      />
    </Shell>
  );
}
