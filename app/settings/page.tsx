import { Shell } from "@/components/layout/shell";
import { Card, CardBody } from "@/components/ui/card";
import { getVersion } from "@/lib/repo-data";

export const dynamic = "force-dynamic";

export default function SettingsPage() {
  return (
    <Shell title="Settings">
      <div className="mx-auto max-w-3xl space-y-8">
        <header>
          <h1 className="text-3xl font-semibold tracking-tight text-zinc-50">
            Settings
          </h1>
          <p className="mt-2 text-base text-zinc-400">
            Lightweight environment overview for executives.
          </p>
        </header>

        <div className="grid gap-4">
          <Card className="border-zinc-800/50 bg-zinc-950/40">
            <CardBody className="space-y-3 p-6">
              <p className="text-xs uppercase tracking-wider text-zinc-500">
                Platform
              </p>
              <p className="text-lg font-medium text-zinc-100">
                IDA Knowledge · v{getVersion()}
              </p>
              <p className="text-sm leading-relaxed text-zinc-400">
                Learning runs on GitHub Actions. This dashboard monitors sessions,
                knowledge growth, and human review. Architecture modules
                (planner, policy, connectors, pipeline) stay internal.
              </p>
            </CardBody>
          </Card>

          <Card className="border-zinc-800/50 bg-zinc-950/40">
            <CardBody className="space-y-3 p-6">
              <p className="text-xs uppercase tracking-wider text-zinc-500">
                How to learn
              </p>
              <ol className="list-decimal space-y-2 pl-5 text-sm text-zinc-300">
                <li>Start learning from the Dashboard (or wait for schedule).</li>
                <li>Review waiting candidates and approve to publish.</li>
                <li>Browse Knowledge to see what IDA has learned.</li>
                <li>Check Reports for growth over time.</li>
              </ol>
            </CardBody>
          </Card>

          <Card className="border-zinc-800/50 bg-zinc-950/40">
            <CardBody className="space-y-2 p-6 text-sm text-zinc-400">
              <p className="text-xs uppercase tracking-wider text-zinc-500">
                Vercel / Start Learning
              </p>
              <p>
                Set <code className="text-zinc-200">IDA_GITHUB_TOKEN</code> and{" "}
                <code className="text-zinc-200">GITHUB_REPOSITORY</code> so the
                dashboard can dispatch learning workflows.
              </p>
            </CardBody>
          </Card>
        </div>
      </div>
    </Shell>
  );
}
