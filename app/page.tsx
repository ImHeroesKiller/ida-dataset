import { Shell } from "@/components/layout/shell";
import { StatusCard } from "@/components/dashboard/status-card";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { buildDashboardSnapshot } from "@/lib/repo-data";
import { getLearningDashboard } from "@/lib/learning";
import { RunActions } from "@/components/shared/run-actions";
import Link from "next/link";

export const dynamic = "force-dynamic";

export default function DashboardPage() {
  const snap = buildDashboardSnapshot();
  const learning = getLearningDashboard() as Record<string, unknown>;
  const growth = (learning.knowledge_growth || {}) as Record<string, number>;
  const alloc = (learning.learning_allocation || {}) as Record<string, number | string>;
  const mission = learning.current_mission as Record<string, unknown> | null;
  const activity = (learning.brain_activity || {}) as Record<string, number>;
  const feed = (learning.knowledge_feed || learning.learning_timeline || []) as Record<
    string,
    unknown
  >[];

  return (
    <Shell title="Learning Dashboard">
      <div className="mb-4 flex flex-col gap-3 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <p className="text-xs text-zinc-500">
            AI Learning Dashboard — not an admin console
          </p>
          <p className="mt-1 max-w-2xl text-sm text-zinc-300">
            Continuous Learning never stops. Directed Learning missions coexist
            under the Scheduler. Planner never starts directly.
          </p>
          <div className="mt-2 flex flex-wrap gap-1.5">
            <Badge>VERSION {snap.version}</Badge>
            <Badge>brain: {String(learning.brain_health || "waiting")}</Badge>
            <Badge>
              growth {growth.coverage_pct ?? snap.datasetSummary.coveragePct}%
            </Badge>
            <Badge>
              alloc C{String(alloc.continuous ?? "—")}/D
              {String(alloc.directed ?? "—")}
            </Badge>
          </div>
        </div>
        <div className="space-y-2">
          <RunActions />
          <div className="flex gap-2">
            <Link
              href="/learning"
              className="rounded-md border border-zinc-700 px-2 py-1 text-xs text-zinc-300 hover:bg-zinc-900"
            >
              Open Learning Brain
            </Link>
            <Link
              href="/missions"
              className="rounded-md border border-zinc-700 px-2 py-1 text-xs text-zinc-300 hover:bg-zinc-900"
            >
              Missions
            </Link>
          </div>
        </div>
      </div>

      <div className="mb-4 grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
        <Card>
          <CardBody className="space-y-1">
            <div className="text-[10px] uppercase tracking-wide text-zinc-500">
              Brain Health
            </div>
            <div className="text-lg font-semibold text-zinc-100">
              {String(learning.brain_health || "waiting")}
            </div>
            <div className="text-[11px] text-zinc-500">
              ticks {activity.ticks ?? 0} · dispatched {activity.tasks_dispatched ?? 0}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody className="space-y-1">
            <div className="text-[10px] uppercase tracking-wide text-zinc-500">
              Knowledge Growth
            </div>
            <div className="text-lg font-semibold text-zinc-100">
              {growth.coverage_pct ?? snap.datasetSummary.coveragePct}%
            </div>
            <div className="text-[11px] text-zinc-500">
              {growth.datasets_populated ?? snap.datasetSummary.populated}/
              {growth.datasets_total ?? snap.datasetSummary.total} datasets
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody className="space-y-1">
            <div className="text-[10px] uppercase tracking-wide text-zinc-500">
              Learning Allocation
            </div>
            <div className="text-lg font-semibold text-zinc-100">
              C {String(alloc.continuous ?? "—")}% · D {String(alloc.directed ?? "—")}%
            </div>
            <div className="text-[11px] text-zinc-500">
              profile {String(alloc.profile || "—")}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody className="space-y-1">
            <div className="text-[10px] uppercase tracking-wide text-zinc-500">
              Current Mission
            </div>
            <div className="truncate text-lg font-semibold text-zinc-100">
              {mission ? String(mission.title) : "Waiting for first execution"}
            </div>
            <div className="text-[11px] text-zinc-500">
              {mission
                ? `${mission.priority} · ${mission.status} · ${mission.progress}%`
                : "No directed mission"}
            </div>
          </CardBody>
        </Card>
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
            title="Knowledge Feed / Brain Activity"
            description="Scheduler telemetry stream"
          />
          <CardBody className="max-h-56 space-y-1 overflow-y-auto font-mono text-[11px] scrollbar-thin">
            {feed.length === 0 ? (
              <p className="font-sans text-xs text-zinc-500">
                {snap.waitingMessage}
              </p>
            ) : (
              [...feed].reverse().slice(0, 25).map((e, i) => (
                <div key={i} className="text-zinc-400">
                  <span className="text-zinc-600">
                    {String(e.ts || "").slice(11, 19)}
                  </span>{" "}
                  <span className="text-sky-400">{String(e.stream)}</span>{" "}
                  {String(e.event)} — {String(e.detail)}
                </div>
              ))
            )}
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Latest Reports"
            description="reports/ artifacts"
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
      </div>
    </Shell>
  );
}
