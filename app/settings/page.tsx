import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { getRepoRoot } from "@/lib/paths";
import { getVersion, getPolicies } from "@/lib/repo-data";
import { listPlugins } from "@/lib/plugins";

export const dynamic = "force-dynamic";

export default function SettingsPage() {
  const plugins = listPlugins();
  const policies = getPolicies();
  const features = ((policies.data as { features?: Record<string, unknown> } | null)
    ?.features ?? {}) as Record<string, unknown>;

  return (
    <Shell title="Settings">
      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader title="Environment" description="External config only" />
          <CardBody className="space-y-2 text-xs text-zinc-400">
            <div>
              Repo root:{" "}
              <span className="font-mono text-zinc-200">{getRepoRoot()}</span>
            </div>
            <div>
              Dataset VERSION:{" "}
              <Badge>{getVersion()}</Badge>
            </div>
            <div>
              IDA_ENVIRONMENT default: <Badge>development</Badge>
            </div>
            <p className="text-zinc-500">
              Profiles live in config/environments/*.yaml — never hardcode
              production rules in the UI.
            </p>
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Feature flags (from Policy Engine)"
            description="Read-only mirror of policies.yaml"
          />
          <CardBody className="space-y-1 text-xs">
            {Object.keys(features).length === 0 ? (
              <p className="text-zinc-500">Waiting for first execution</p>
            ) : (
              Object.entries(features).map(([k, v]) => (
                <div
                  key={k}
                  className="flex justify-between border-b border-zinc-900 py-1"
                >
                  <span className="text-zinc-400">{k}</span>
                  <span className="text-zinc-200">{String(v)}</span>
                </div>
              ))
            )}
          </CardBody>
        </Card>

        <Card className="lg:col-span-2">
          <CardHeader
            title="Plugins"
            description="Future modules register without redesign — still respect control flow"
          />
          <CardBody>
            <div className="grid gap-2 md:grid-cols-2 xl:grid-cols-3">
              {plugins.map((p) => (
                <div
                  key={p.id}
                  className="rounded-md border border-zinc-800 bg-zinc-950/60 p-3"
                >
                  <div className="flex items-center justify-between gap-2">
                    <div className="text-xs font-medium text-zinc-100">
                      {p.name}
                    </div>
                    <Badge>{p.status}</Badge>
                  </div>
                  <p className="mt-1 text-[11px] text-zinc-500">
                    {p.description}
                  </p>
                  <p className="mt-2 text-[10px] text-zinc-600">
                    respectsControlFlow=true · slots: {p.slots.join(", ")}
                  </p>
                </div>
              ))}
            </div>
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}
