import { Shell } from "@/components/layout/shell";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { getKnowledgeKpis } from "@/lib/knowledge-kpis";
import { getLearningDashboard } from "@/lib/learning";
import Link from "next/link";

export const dynamic = "force-dynamic";

export default function DashboardPage() {
  const k = getKnowledgeKpis();
  const learning = getLearningDashboard() as Record<string, unknown>;
  const mission = learning.current_mission as Record<string, unknown> | null;
  const journal = k.learning_journal;

  return (
    <Shell title="IDA Learning Dashboard">
      <div className="mb-4">
        <p className="text-xs text-zinc-500">{k.philosophy.focus}</p>
        <p className="mt-1 max-w-3xl text-sm text-zinc-200">
          {k.philosophy.principle} Architecture is frozen. Every change should
          increase knowledge, coverage, quality, relationships, and confidence.
        </p>
        <div className="mt-2 flex flex-wrap gap-1.5">
          <Badge>
            first knowledge:{" "}
            {k.first_knowledge.learned
              ? String(k.first_knowledge.industry_name)
              : "not yet"}
          </Badge>
          <Badge>quality {k.knowledge_quality_score}</Badge>
          <Badge>continuous: always on</Badge>
        </div>
      </div>

      {/* Core questions */}
      <div className="mb-4 grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
        <Card>
          <CardBody className="space-y-1">
            <div className="text-[10px] uppercase tracking-wide text-zinc-500">
              How much knowledge?
            </div>
            <div className="text-lg font-semibold text-zinc-50">
              {k.knowledge_coverage}%
            </div>
            <div className="text-[11px] text-zinc-500">
              {k.answers.how_much_knowledge}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody className="space-y-1">
            <div className="text-[10px] uppercase tracking-wide text-zinc-500">
              Learning right now?
            </div>
            <div className="text-lg font-semibold text-zinc-50">
              {String(mission?.title || "Continuous gaps")}
            </div>
            <div className="text-[11px] text-zinc-500">
              {k.answers.learning_now}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody className="space-y-1">
            <div className="text-[10px] uppercase tracking-wide text-zinc-500">
              Smarter than yesterday?
            </div>
            <div className="text-lg font-semibold text-zinc-50">
              {k.knowledge_growth_today.smarter_than_yesterday ? "Yes" : "Baseline"}
            </div>
            <div className="text-[11px] text-zinc-500">
              {k.answers.smarter_than_yesterday}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody className="space-y-1">
            <div className="text-[10px] uppercase tracking-wide text-zinc-500">
              Knowledge quality
            </div>
            <div className="text-lg font-semibold text-zinc-50">
              {k.knowledge_quality_score}
            </div>
            <div className="text-[11px] text-zinc-500">
              confidence {k.knowledge_confidence ?? "—"}
            </div>
          </CardBody>
        </Card>
      </div>

      <div className="mb-4 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">Added today</div>
            <div className="text-2xl font-semibold text-emerald-400">
              {k.knowledge_added_today}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">Updated today</div>
            <div className="text-2xl font-semibold text-sky-400">
              {k.knowledge_updated_today}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">Rejected</div>
            <div className="text-2xl font-semibold text-red-400">
              {k.knowledge_rejected}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">Pending review</div>
            <div className="text-2xl font-semibold text-amber-300">
              {k.pending_review}
            </div>
          </CardBody>
        </Card>
      </div>

      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader
            title="Growing datasets"
            description="Which datasets are growing?"
          />
          <CardBody className="space-y-1 text-xs">
            {k.growing_datasets.length === 0 ? (
              <p className="text-zinc-500">Waiting for first execution</p>
            ) : (
              k.growing_datasets.map((d) => (
                <div
                  key={d.path}
                  className="flex justify-between border-b border-zinc-900 py-1.5 text-zinc-300"
                >
                  <span>{d.name}</span>
                  <span className="text-zinc-500">
                    {d.domain} · {d.rows} rows
                  </span>
                </div>
              ))
            )}
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Knowledge gaps"
            description="Still empty / header-only"
          />
          <CardBody className="max-h-64 space-y-1 overflow-y-auto text-xs scrollbar-thin">
            {k.knowledge_gaps.length === 0 ? (
              <p className="text-zinc-500">No gaps</p>
            ) : (
              k.knowledge_gaps.map((d) => (
                <div
                  key={d.path}
                  className="flex justify-between border-b border-zinc-900 py-1.5 text-zinc-400"
                >
                  <span>{d.name}</span>
                  <span className="text-zinc-600">{d.domain}</span>
                </div>
              ))
            )}
          </CardBody>
        </Card>
      </div>

      <div className="mt-3 grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader
            title="Current mission"
            description="Directed learning (never stops continuous)"
          />
          <CardBody className="text-xs text-zinc-400">
            {!mission ? (
              <p className="text-zinc-500">No active directed mission</p>
            ) : (
              <div className="space-y-1">
                <div className="text-sm text-zinc-100">{String(mission.title)}</div>
                <div>
                  {String(mission.priority)} · {String(mission.status)} ·{" "}
                  {String(mission.progress)}%
                </div>
                <div>Stage: {String(mission.current_stage || "—")}</div>
                <div>Dataset: {String(mission.current_dataset || "—")}</div>
              </div>
            )}
            <div className="mt-3 flex gap-2">
              <Link href="/missions" className="text-sky-400 hover:underline">
                Missions
              </Link>
              <Link href="/learning" className="text-sky-400 hover:underline">
                Learning Brain
              </Link>
              <Link href="/documents" className="text-sky-400 hover:underline">
                Documents ({k.documents_processing})
              </Link>
              <Link href="/review" className="text-sky-400 hover:underline">
                Review ({k.pending_review})
              </Link>
            </div>
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Learning journal"
            description="Realtime learning verbs — not system noise"
          />
          <CardBody className="max-h-64 space-y-1 overflow-y-auto font-mono text-[11px] scrollbar-thin">
            {journal.length === 0 ? (
              <p className="font-sans text-xs text-zinc-500">
                Waiting for first execution
              </p>
            ) : (
              [...journal].reverse().slice(0, 40).map((e, i) => (
                <div key={i} className="text-zinc-400">
                  <span className="text-zinc-600">
                    {String(e.ts || "").slice(11, 19)}
                  </span>{" "}
                  <span className="text-emerald-400">{String(e.verb)}</span> —{" "}
                  {String(e.detail)}
                </div>
              ))
            )}
          </CardBody>
        </Card>
      </div>

      <div className="mt-3 grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader title="Recently learned knowledge" />
          <CardBody className="space-y-1 text-xs">
            {k.recently_learned.length === 0 ? (
              <p className="text-zinc-500">Waiting for first execution</p>
            ) : (
              k.recently_learned.map((r) => (
                <div
                  key={r.path}
                  className="flex justify-between border-b border-zinc-900 py-1.5 text-zinc-300"
                >
                  <span>{r.dataset}</span>
                  <span className="text-zinc-500">{r.rows} rows</span>
                </div>
              ))
            )}
          </CardBody>
        </Card>
        <Card>
          <CardHeader title="Domain coverage" />
          <CardBody className="space-y-1 text-xs">
            {k.domain_coverage.map((d) => (
              <div
                key={d.domain}
                className="flex justify-between border-b border-zinc-900 py-1.5 text-zinc-300"
              >
                <span>{d.domain}</span>
                <span className="text-zinc-500">
                  {d.populated}/{d.total} · {d.coverage_pct}%
                </span>
              </div>
            ))}
          </CardBody>
        </Card>
      </div>
    </Shell>
  );
}
