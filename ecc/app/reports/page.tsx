import { Shell } from "@/components/layout/shell";
import { listReports } from "@/lib/repo-data";
import { ReportsClient } from "@/components/shared/reports-client";

export const dynamic = "force-dynamic";

export default function ReportsPage() {
  const reports = listReports();
  return (
    <Shell title="Reports">
      <div className="mb-3">
        <p className="text-sm text-zinc-300">
          Validation · Planner · Review · Publish · Run history artifacts
        </p>
      </div>
      <ReportsClient
        items={reports.items}
        waiting={reports.waiting}
        message={reports.message}
      />
    </Shell>
  );
}
