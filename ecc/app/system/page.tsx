import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { getGitStatus, getVersion, listDatasets } from "@/lib/repo-data";
import { getRepoRoot } from "@/lib/paths";
import { FLOW_HINT } from "@/lib/nav";
import { RunActions } from "@/components/shared/run-actions";

export const dynamic = "force-dynamic";

export default function SystemPage() {
  const git = getGitStatus();
  const datasets = listDatasets();

  return (
    <Shell title="System">
      <div className="mb-4">
        <p className="text-sm text-zinc-300">
          Operational health of the ECC orchestration layer.
        </p>
      </div>

      <div className="mb-3 flex flex-wrap gap-2">
        {FLOW_HINT.map((step, i) => (
          <div key={step} className="flex items-center gap-2 text-xs">
            <Badge>{step}</Badge>
            {i < FLOW_HINT.length - 1 ? (
              <span className="text-zinc-600">→</span>
            ) : null}
          </div>
        ))}
      </div>

      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader title="Runtime" description="Process context" />
          <CardBody className="space-y-1 text-xs text-zinc-400">
            <div>
              Repo: <span className="font-mono text-zinc-200">{getRepoRoot()}</span>
            </div>
            <div>
              VERSION: <Badge>{getVersion()}</Badge>
            </div>
            <div>Node: {process.version}</div>
            <div>Datasets indexed: {datasets.length}</div>
            <div>
              Architecture: ECC orchestrates existing automation modules only
            </div>
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Git" description="Repository state" />
          <CardBody className="space-y-1 text-xs text-zinc-400">
            {git.available ? (
              <>
                <div>
                  Branch: <span className="text-zinc-200">{git.branch}</span>
                </div>
                <div>
                  Commit:{" "}
                  <span className="font-mono text-zinc-200">{git.commit}</span>
                </div>
                <div>Dirty: {String(git.dirty)}</div>
                <pre className="mt-2 overflow-x-auto rounded border border-zinc-900 bg-zinc-950 p-2 font-mono text-[11px]">
                  {(git.recentCommits ?? []).join("\n") || "—"}
                </pre>
              </>
            ) : (
              <p className="text-zinc-500">Waiting for first execution</p>
            )}
          </CardBody>
        </Card>
      </div>

      <div className="mt-3">
        <Card>
          <CardHeader
            title="Safe orchestration actions"
            description="No crawler · publish dry-run only"
          />
          <CardBody>
            <RunActions />
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}
