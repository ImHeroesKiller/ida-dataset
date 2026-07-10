import { Shell } from "@/components/layout/shell";
import { StatusCard } from "@/components/dashboard/status-card";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { buildDashboardSnapshot } from "@/lib/repo-data";
import { RunActions } from "@/components/shared/run-actions";

export const dynamic = "force-dynamic";

export default function DashboardPage() {
  const snap = buildDashboardSnapshot();

  return (
    <Shell title="Dashboard">
      <div className="mb-4 flex flex-col gap-3 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <p className="text-xs text-zinc-500">{snap.philosophy.control}</p>
          <p className="mt-1 max-w-2xl text-sm text-zinc-300">
            {snap.philosophy.statement}
          </p>
          <div className="mt-2 flex flex-wrap gap-1.5">
            <Badge>VERSION {snap.version}</Badge>
            <Badge>
              Coverage {snap.datasetSummary.coveragePct}% ·{" "}
              {snap.datasetSummary.populated}/{snap.datasetSummary.total}
            </Badge>
          </div>
        </div>
        <RunActions />
      </div>

      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-5">
        {snap.modules.map((m) => (
          <StatusCard
            key={m.key}
            label={m.label}
            status={m.status}
            detail={m.detail}
          />
        ))}
      </div>

      <div className="mt-4 grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader
            title="Latest Reports"
            description="Artifacts under reports/ — no fabricated metrics"
          />
          <CardBody className="space-y-1.5">
            {snap.latestReports.length === 0 ? (
              <p className="text-xs text-zinc-500">{snap.waitingMessage}</p>
            ) : (
              snap.latestReports.map((r) => (
                <a
                  key={r.relativePath}
                  href={`/reports?file=${encodeURIComponent(r.relativePath)}`}
                  className="flex items-center justify-between rounded-md border border-transparent px-2 py-1.5 text-xs hover:border-zinc-800 hover:bg-zinc-900/60"
                >
                  <span className="truncate text-zinc-200">{r.name}</span>
                  <span className="ml-2 shrink-0 text-[10px] text-zinc-500">
                    {r.kind}
                  </span>
                </a>
              ))
            )}
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Latest Runs / Git"
            description="Recent commits from the knowledge repository"
          />
          <CardBody className="space-y-1.5 font-mono text-[11px]">
            {snap.latestRuns.length === 0 ? (
              <p className="font-sans text-xs text-zinc-500">
                {snap.waitingMessage}
              </p>
            ) : (
              snap.latestRuns.map((line) => (
                <div key={line} className="truncate text-zinc-400">
                  {line}
                </div>
              ))
            )}
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}
