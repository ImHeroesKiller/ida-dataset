"use client";

import { useMemo, useState } from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { LiveProgress } from "@/components/shared/live-progress";
import { useLearningSessions } from "@/lib/use-learning-sessions";

type KpiSnap = {
  knowledge_coverage: number;
  knowledge_added_today: number;
  knowledge_updated_today: number;
  knowledge_rejected: number;
  pending_review: number;
  growing_datasets: { name: string; domain: string; rows: number; path: string }[];
  knowledge_gaps: { name: string; domain: string; path: string }[];
  first_knowledge?: {
    learned?: boolean;
    industry_name?: unknown;
    [key: string]: unknown;
  };
};

function statusClass(status: string): string {
  switch (status) {
    case "running":
    case "queued":
      return "text-sky-300";
    case "completed":
    case "success":
      return "text-emerald-300";
    case "failed":
    case "error":
      return "text-red-400";
    default:
      return "text-zinc-400";
  }
}

function fmtDuration(sec: number | null | undefined): string {
  if (sec == null || Number.isNaN(sec)) return "—";
  if (sec < 60) return `${Math.round(sec)}s`;
  const m = Math.floor(sec / 60);
  const s = Math.round(sec % 60);
  return `${m}m ${s}s`;
}

function fmtTime(iso?: string | null): string {
  if (!iso) return "—";
  try {
    return new Date(iso).toLocaleString();
  } catch {
    return iso;
  }
}

export function LiveDashboard({ initialKpis }: { initialKpis: KpiSnap }) {
  const {
    dashboard,
    events,
    activity,
    startLearning,
    replay,
    selectSession,
    error,
    loading,
  } = useLearningSessions(5000);

  const [kpis] = useState(initialKpis);
  const [instruction, setInstruction] = useState(
    "Learn Industry Library knowledge for Banking"
  );
  const [dryRun, setDryRun] = useState(true);
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);
  const [replaying, setReplaying] = useState(false);

  const status = dashboard.github_actions?.running
    ? "running"
    : dashboard.status || "idle";

  const sessions = dashboard.sessions || [];
  const history = dashboard.history;
  const ga = dashboard.github_actions;

  const feed = useMemo(() => {
    return events
      .filter(
        (e) =>
          e.verb === "Knowledge Updated" ||
          e.verb === "Pipeline" ||
          e.verb === "Publishing" ||
          (e.current_entity && e.status === "progress")
      )
      .slice(-20)
      .reverse();
  }, [events]);

  async function onStart() {
    setBusy(true);
    setMsg(null);
    try {
      const res = await startLearning(instruction, dryRun);
      if (!res.ok) {
        setMsg(res.reason || res.message || "Dispatch failed");
      } else {
        setMsg(
          `GitHub Actions workflow dispatched${
            res.repository ? ` · ${res.repository}` : ""
          } · learning.yml`
        );
      }
    } catch (e) {
      setMsg(e instanceof Error ? e.message : "Failed");
    } finally {
      setBusy(false);
    }
  }

  async function onReplay(sessionId: string) {
    setReplaying(true);
    setMsg(`Replaying ${sessionId}…`);
    try {
      await replay(sessionId, 250);
      setMsg(`Replay finished · ${sessionId}`);
    } finally {
      setReplaying(false);
    }
  }

  const hToday = history?.today;
  const hWeek = history?.this_week;
  const hMonth = history?.this_month;
  const hTotal = history?.total;

  return (
    <div className="space-y-4">
      <div className="flex flex-col gap-3 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <p className="text-xs text-zinc-500">LEARNING SESSIONS · GITHUB ACTIONS</p>
          <p className="mt-1 max-w-2xl text-sm text-zinc-200">
            Learning runs entirely on GitHub Actions. This dashboard monitors
            completed and running sessions — no local Python runtime.
          </p>
          <div className="mt-2 flex flex-wrap gap-1.5">
            <Badge className={statusClass(status)}>status {status}</Badge>
            <Badge>
              next run {fmtTime(dashboard.next_scheduled_run)}
            </Badge>
            <Badge>
              last ok{" "}
              {fmtTime(dashboard.last_successful_run?.end_time || dashboard.last_successful_run?.start_time)}
            </Badge>
            <Badge className={ga?.configured ? "text-emerald-300" : "text-amber-300"}>
              gha {ga?.configured ? "connected" : "token missing"}
            </Badge>
            <Badge>coverage {kpis.knowledge_coverage}%</Badge>
            <Badge>added today {kpis.knowledge_added_today}</Badge>
          </div>
        </div>
        <div className="flex w-full max-w-xl flex-col gap-2">
          <Input
            value={instruction}
            onChange={(e) => setInstruction(e.target.value)}
            placeholder="Mission / learning instruction"
          />
          <div className="flex flex-wrap items-center gap-2">
            <Button size="sm" disabled={busy || status === "running"} onClick={onStart}>
              Start Learning
            </Button>
            <Button
              size="sm"
              variant="secondary"
              disabled={!sessions[0] || replaying}
              onClick={() => sessions[0] && onReplay(sessions[0].session_id)}
            >
              Replay last session
            </Button>
            <label className="flex items-center gap-1 text-[11px] text-zinc-500">
              <input
                type="checkbox"
                checked={dryRun}
                onChange={(e) => setDryRun(e.target.checked)}
                className="accent-zinc-400"
              />
              Dry run
            </label>
          </div>
          {msg ? <p className="text-[11px] text-zinc-400">{msg}</p> : null}
          {error ? <p className="text-[11px] text-red-400">{error}</p> : null}
          {loading ? (
            <p className="text-[11px] text-zinc-600">Loading sessions…</p>
          ) : null}
        </div>
      </div>

      {/* Current status panel */}
      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">Current status</div>
            <div className={`text-2xl font-semibold capitalize ${statusClass(status)}`}>
              {status}
            </div>
            <div className="mt-1 text-[11px] text-zinc-500">
              {ga?.current_run?.html_url ? (
                <a
                  href={ga.current_run.html_url}
                  target="_blank"
                  rel="noreferrer"
                  className="text-sky-400 hover:underline"
                >
                  Open workflow run
                </a>
              ) : (
                "GitHub Actions execution model"
              )}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">Current mission</div>
            <div className="line-clamp-2 text-sm font-medium text-zinc-100">
              {dashboard.current_mission || "—"}
            </div>
            <div className="mt-1 text-[11px] text-zinc-500">
              duration {fmtDuration(dashboard.session_duration)}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">Knowledge (session)</div>
            <div className="flex gap-3 text-lg font-semibold">
              <span className="text-emerald-400">+{dashboard.knowledge_added ?? 0}</span>
              <span className="text-sky-400">~{dashboard.knowledge_updated ?? 0}</span>
              <span className="text-red-400">×{dashboard.knowledge_rejected ?? 0}</span>
            </div>
            <div className="mt-1 text-[11px] text-zinc-500">
              added · updated · rejected
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">Next scheduled run</div>
            <div className="text-sm font-medium text-zinc-100">
              {fmtTime(dashboard.next_scheduled_run)}
            </div>
            <div className="mt-1 text-[11px] text-zinc-500">
              Hourly + daily (06:00 UTC) via learning.yml
            </div>
          </CardBody>
        </Card>
      </div>

      <Card>
        <CardHeader
          title="Learning activity"
          description="Real session events — no fake streaming"
        />
        <CardBody>
          <LiveProgress activity={activity} events={events} />
        </CardBody>
      </Card>

      {/* Learning history */}
      <Card>
        <CardHeader
          title="Learning history"
          description="Today · This week · This month · Totals"
        />
        <CardBody>
          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
            {(
              [
                ["Today", hToday],
                ["This week", hWeek],
                ["This month", hMonth],
                ["Total", hTotal],
              ] as const
            ).map(([label, bucket]) => (
              <div
                key={label}
                className="rounded border border-zinc-800 bg-zinc-950/50 p-3"
              >
                <div className="text-[10px] uppercase text-zinc-500">{label}</div>
                <div className="mt-1 text-xl font-semibold text-zinc-100">
                  {bucket?.sessions ?? 0}{" "}
                  <span className="text-sm font-normal text-zinc-500">sessions</span>
                </div>
                <div className="mt-2 space-y-0.5 text-[11px] text-zinc-400">
                  <div>
                    success rate{" "}
                    <span className="text-emerald-300">
                      {bucket?.success_rate ?? 0}%
                    </span>
                  </div>
                  <div>
                    knowledge +{bucket?.knowledge_added ?? 0} / avg{" "}
                    {bucket?.avg_knowledge_added ?? 0}
                  </div>
                  <div>
                    avg duration {fmtDuration(bucket?.avg_duration_seconds)}
                  </div>
                </div>
              </div>
            ))}
          </div>
          {history?.knowledge_growth ? (
            <p className="mt-3 text-[11px] text-zinc-500">
              Knowledge growth (all sessions): +
              {history.knowledge_growth.added} added · ~
              {history.knowledge_growth.updated} updated · ×
              {history.knowledge_growth.rejected} rejected
            </p>
          ) : null}
        </CardBody>
      </Card>

      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">
              Knowledge added today
            </div>
            <div className="text-2xl font-semibold text-emerald-400">
              {kpis.knowledge_added_today}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">Updated today</div>
            <div className="text-2xl font-semibold text-sky-400">
              {kpis.knowledge_updated_today}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">Rejected</div>
            <div className="text-2xl font-semibold text-red-400">
              {kpis.knowledge_rejected}
            </div>
          </CardBody>
        </Card>
        <Card>
          <CardBody>
            <div className="text-[10px] uppercase text-zinc-500">Waiting review</div>
            <div className="text-2xl font-semibold text-amber-300">
              {kpis.pending_review}
            </div>
          </CardBody>
        </Card>
      </div>

      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader
            title="Knowledge feed"
            description="From the selected / current session"
          />
          <CardBody className="max-h-72 space-y-1 overflow-y-auto text-xs scrollbar-thin">
            {feed.length === 0 ? (
              <p className="text-zinc-500">
                No knowledge events yet. Start a learning session or replay a
                completed one.
              </p>
            ) : (
              feed.map((e, i) => (
                <div
                  key={`${e.seq}-${i}`}
                  className="border-b border-zinc-900 py-1.5 text-zinc-300"
                >
                  <span className="text-emerald-400">
                    {e.current_entity || e.verb}
                  </span>
                  {e.dataset ? (
                    <span className="text-zinc-600"> · {e.dataset}</span>
                  ) : null}
                  <div className="text-[11px] text-zinc-500">{e.detail}</div>
                </div>
              ))
            )}
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Session timeline"
            description="Real timestamps from stored session files"
          />
          <CardBody className="max-h-72 space-y-1 overflow-y-auto font-mono text-[11px] scrollbar-thin">
            {events.length === 0 ? (
              <p className="font-sans text-xs text-zinc-500">
                Timeline empty — select a session or wait for the next GHA run.
              </p>
            ) : (
              events.slice(-40).map((e, i) => (
                <div key={`${e.seq}-t-${i}`} className="text-zinc-400">
                  <span className="text-zinc-600">
                    {String(e.ts || "").slice(11, 19)}
                  </span>{" "}
                  <span className="text-sky-400">{e.stage}</span>{" "}
                  <span className="text-zinc-200">{e.verb}</span>
                </div>
              ))
            )}
          </CardBody>
        </Card>
      </div>

      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader title="Growing datasets" />
          <CardBody className="space-y-1 text-xs">
            {kpis.growing_datasets.map((d) => (
              <div
                key={d.path}
                className="flex justify-between border-b border-zinc-900 py-1.5 text-zinc-300"
              >
                <span>{d.name}</span>
                <span className="text-zinc-500">{d.rows} rows</span>
              </div>
            ))}
          </CardBody>
        </Card>
        <Card>
          <CardHeader title="Knowledge gaps" />
          <CardBody className="max-h-56 space-y-1 overflow-y-auto text-xs scrollbar-thin">
            {kpis.knowledge_gaps.map((d) => (
              <div
                key={d.path}
                className="flex justify-between border-b border-zinc-900 py-1.5 text-zinc-400"
              >
                <span>{d.name}</span>
                <span className="text-zinc-600">{d.domain}</span>
              </div>
            ))}
          </CardBody>
        </Card>
      </div>

      <Card>
        <CardHeader
          title="Learning sessions"
          description="Stored under automation/sessions/ · replay preserves order & timestamps"
        />
        <CardBody className="space-y-2">
          {sessions.length === 0 ? (
            <p className="text-xs text-zinc-500">
              No sessions yet. Dispatch learning.yml or wait for the hourly
              schedule.
            </p>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs text-zinc-300">
                <thead className="text-[10px] uppercase text-zinc-500">
                  <tr>
                    <th className="pb-2 pr-3">Session</th>
                    <th className="pb-2 pr-3">Status</th>
                    <th className="pb-2 pr-3">Mission</th>
                    <th className="pb-2 pr-3">+ / ~ / ×</th>
                    <th className="pb-2 pr-3">Duration</th>
                    <th className="pb-2">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {sessions.slice(0, 15).map((s) => (
                    <tr key={s.session_id} className="border-t border-zinc-900">
                      <td className="py-2 pr-3 font-mono text-[10px] text-zinc-400">
                        {s.session_id}
                      </td>
                      <td className={`py-2 pr-3 ${statusClass(String(s.status))}`}>
                        {s.status}
                      </td>
                      <td className="max-w-[14rem] truncate py-2 pr-3">
                        {s.mission || "—"}
                      </td>
                      <td className="py-2 pr-3 font-mono text-[10px]">
                        {s.knowledge_added ?? 0}/{s.knowledge_updated ?? 0}/
                        {s.knowledge_rejected ?? 0}
                      </td>
                      <td className="py-2 pr-3">
                        {fmtDuration(s.duration_seconds)}
                      </td>
                      <td className="py-2">
                        <div className="flex gap-1">
                          <Button
                            size="sm"
                            variant="outline"
                            onClick={() => selectSession(s.session_id)}
                          >
                            View
                          </Button>
                          <Button
                            size="sm"
                            variant="secondary"
                            disabled={replaying}
                            onClick={() => onReplay(s.session_id)}
                          >
                            Replay
                          </Button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </CardBody>
      </Card>
    </div>
  );
}
