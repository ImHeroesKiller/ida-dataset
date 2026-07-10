import { Shell } from "@/components/layout/shell";
import { LearningClient } from "@/components/shared/learning-client";
import { getLearningDashboard } from "@/lib/learning";

export const dynamic = "force-dynamic";

export default function LearningPage() {
  const dash = getLearningDashboard();
  return (
    <Shell title="Learning Brain">
      <LearningClient initial={dash as Record<string, unknown>} />
    </Shell>
  );
}
