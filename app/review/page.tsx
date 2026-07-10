import { Shell } from "@/components/layout/shell";
import { getReviewQueues } from "@/lib/repo-data";
import { ReviewClient } from "@/components/shared/review-client";

export const dynamic = "force-dynamic";

export default function ReviewPage() {
  const queues = getReviewQueues();
  return (
    <Shell title="Review">
      <ReviewClient
        initial={{
          pending: queues.pending,
          approved: queues.approved,
          rejected: queues.rejected,
          counts: queues.counts,
          waiting: queues.waiting,
        }}
      />
    </Shell>
  );
}
