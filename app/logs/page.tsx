import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { getFactoryKpis } from "@/lib/factory-kpis";
import { formatWib } from "@/lib/time-wib";

export const dynamic = "force-dynamic";

export default function LogsPage() {
  const kpis = getFactoryKpis();
  const events = kpis.recent_activity;

  return (
    <Shell title="Logs">
      <div className="mx-auto max-w-5xl space-y-6">
        <header>
          <h1 className="text-2xl font-semibold text-[var(--text)]">
            Factory Logs
          </h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            Learning journal and pipeline activity for dataset generation.
          </p>
        </header>

        <Card>
          <CardHeader
            title="Activity stream"
            description={`${events.length} recent events`}
          />
          <CardBody className="max-h-[32rem] space-y-1.5 overflow-y-auto font-mono text-[11px] scrollbar-thin">
            {!events.length ? (
              <p className="text-sm text-[var(--text-faint)]">No log events.</p>
            ) : (
              events.map((ev, i) => (
                <div
                  key={i}
                  className="flex gap-2 border-b border-[var(--border)] py-1.5 text-[var(--text-muted)] last:border-0"
                >
                  <span className="w-44 shrink-0 text-[var(--text-faint)]">
                    {formatWib(ev.ts)}
                  </span>
                  <span className="w-32 shrink-0 font-medium text-emerald-600 dark:text-emerald-300">
                    {ev.verb}
                  </span>
                  <span className="min-w-0 break-words">{ev.detail}</span>
                </div>
              ))
            )}
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}
