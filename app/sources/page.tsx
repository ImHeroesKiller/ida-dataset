import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { getSourceHealthDashboard } from "@/lib/source-health";
import { cn } from "@/lib/utils";

export const dynamic = "force-dynamic";

function fmtTs(v: string | null): string {
  if (!v) return "—";
  return v.replace("T", " ").replace("Z", " UTC").slice(0, 19);
}

function pct(n: number): string {
  return `${Math.round(n * 1000) / 10}%`;
}

function HealthBadge({ status }: { status: string }) {
  const tone =
    status === "healthy"
      ? "bg-emerald-500/15 text-emerald-700 dark:text-emerald-300"
      : status === "degraded"
        ? "bg-amber-500/15 text-amber-700 dark:text-amber-300"
        : status === "down"
          ? "bg-red-500/15 text-red-700 dark:text-red-300"
          : status === "inactive"
            ? "bg-[var(--panel-2)] text-[var(--text-faint)]"
            : "bg-[var(--panel-2)] text-[var(--text-muted)]";
  return (
    <span
      className={cn(
        "inline-flex rounded-full px-2 py-0.5 text-[11px] font-medium capitalize",
        tone
      )}
    >
      {status || "unknown"}
    </span>
  );
}

export default function SourcesPage() {
  const dash = getSourceHealthDashboard();
  const sources = dash.sources.filter(
    (s) => s.allowed || s.status === "active" || s.rows_produced > 0
  );

  return (
    <Shell title="Sources">
      <div className="mx-auto max-w-6xl space-y-6">
        <header>
          <h1 className="text-2xl font-semibold text-[var(--text)]">
            Trusted Sources
          </h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            Operational view of factory production sources.{" "}
            {dash.totals.active} active · {dash.totals.healthy} healthy ·{" "}
            {dash.totals.rows_produced} rows attributed
            {dash.updated_at ? ` · metrics ${fmtTs(dash.updated_at)}` : ""}
          </p>
        </header>

        <Card>
          <CardHeader
            title="Source production monitor"
            description="Health · Coverage · Produced rows · Last sync · Status · Mission usage"
          />
          <CardBody className="overflow-x-auto">
            <table className="w-full min-w-[1100px] text-left text-sm">
              <thead className="text-[10px] uppercase tracking-wider text-[var(--text-faint)]">
                <tr>
                  <th className="pb-2 pr-3">Name</th>
                  <th className="pb-2 pr-3">Category</th>
                  <th className="pb-2 pr-3">Trust</th>
                  <th className="pb-2 pr-3">Coverage</th>
                  <th className="pb-2 pr-3">Health</th>
                  <th className="pb-2 pr-3">Last sync</th>
                  <th className="pb-2 pr-3">Last attempt</th>
                  <th className="pb-2 pr-3">Rows</th>
                  <th className="pb-2 pr-3">Docs</th>
                  <th className="pb-2 pr-3">Success</th>
                  <th className="pb-2 pr-3">Fails</th>
                  <th className="pb-2 pr-3">Avg ms</th>
                  <th className="pb-2 pr-3">Status</th>
                  <th className="pb-2">Missions</th>
                </tr>
              </thead>
              <tbody>
                {sources.map((s) => (
                  <tr
                    key={s.source_id}
                    className="border-t border-[var(--border)] text-[var(--text-muted)]"
                  >
                    <td className="py-2.5 pr-3">
                      <div className="font-medium text-[var(--text)]">
                        {s.name}
                      </div>
                      <div className="font-mono text-[10px] text-[var(--text-faint)]">
                        {s.source_id}
                      </div>
                    </td>
                    <td className="py-2.5 pr-3 text-xs">{s.category}</td>
                    <td className="py-2.5 pr-3">
                      {s.trust_score.toFixed(2)}
                    </td>
                    <td className="py-2.5 pr-3">{pct(s.coverage)}</td>
                    <td className="py-2.5 pr-3">
                      <HealthBadge status={s.health_status} />
                    </td>
                    <td className="py-2.5 pr-3 text-xs whitespace-nowrap">
                      {fmtTs(s.last_successful_sync)}
                    </td>
                    <td className="py-2.5 pr-3 text-xs whitespace-nowrap">
                      {fmtTs(s.last_attempt)}
                    </td>
                    <td className="py-2.5 pr-3 font-medium text-[var(--text)]">
                      {s.rows_produced}
                    </td>
                    <td className="py-2.5 pr-3">{s.documents_processed}</td>
                    <td className="py-2.5 pr-3">{pct(s.success_rate)}</td>
                    <td className="py-2.5 pr-3">{s.failure_count}</td>
                    <td className="py-2.5 pr-3">
                      {s.average_processing_time_ms
                        ? Math.round(s.average_processing_time_ms)
                        : "—"}
                    </td>
                    <td className="py-2.5 pr-3 text-xs capitalize">
                      {s.status}
                      {!s.allowed ? " / blocked" : ""}
                    </td>
                    <td className="py-2.5">{s.mission_usage}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}
