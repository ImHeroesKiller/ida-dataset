import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { buildPlannerView } from "@/lib/repo-data";
import { PlannerClient } from "@/components/shared/planner-client";
import { RunActions } from "@/components/shared/run-actions";

export const dynamic = "force-dynamic";

export default function PlannerPage() {
  const data = buildPlannerView();

  return (
    <Shell title="Knowledge Planner">
      <div className="mb-4 space-y-2">
        <p className="text-sm text-zinc-300">{data.architectureNote}</p>
        <p className="text-xs text-zinc-500">
          Planner proposes only. Approve/reject plans here; execution still
          respects Policy → Pipeline → Review → Publisher.
        </p>
        <div className="flex flex-wrap gap-1.5">
          <Badge>Total {data.summary.total}</Badge>
          <Badge>Populated {data.summary.populated}</Badge>
          <Badge>Placeholder {data.summary.placeholders}</Badge>
        </div>
        <RunActions />
      </div>

      <Card>
        <CardHeader
          title="Suggested Plans"
          description="Derived from live dataset inventory — not synthetic targets"
        />
        <CardBody className="p-0">
          {data.waiting ? (
            <p className="p-4 text-xs text-zinc-500">{data.message}</p>
          ) : (
            <PlannerClient plans={data.datasets} />
          )}
        </CardBody>
      </Card>
    </Shell>
  );
}
