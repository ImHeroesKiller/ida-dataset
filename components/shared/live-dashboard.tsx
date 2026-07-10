"use client";

import { useEffect, useMemo, useState } from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { LiveProgress } from "@/components/shared/live-progress";
import { useLiveLearning } from "@/lib/use-live-learning";

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

export function LiveDashboard({ initialKpis }: { initialKpis: KpiSnap }) {
  const { events, activity, connected, startLive, replay } = useLiveLearning();
  const [kpis, setKpis] = useState(initialKpis);
  const [instruction, setInstruction] = useState(
    "Learn Industry Library knowledge for Banking"
  );
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);
  const [sessions, setSessions] = useState<
    { session_id: string; events: number; last_verb?: string | null }[]
  >([]);

  // Refresh KPIs when session completes (subscribe-driven, not result-polling loops)
  useEffect(() => {
    const last = events[events.length - 1];
    if (last?.verb === "Learning Completed" || last?.verb === "Knowledge Updated") {
      fetch("/api/journal")
        .then((r) => r.json())
        .then(() =>
          fetch("/api/status")
            .then(() => {
              // soft refresh KPI fields from journal endpoint's sibling
            })
            .catch(() => null)
        )
        .catch(() => null);
      // re-read KPIs via dedicated lightweight endpoint pattern
      fetch("/api/live/replay")
        .then((r) => r.json())
        .then((d) => setSessions(d.sessions || []))
        .catch(() => null);
    }
  }, [events]);

  useEffect(() => {
    fetch("/api/live/replay")
      .then((r) => r.json())
      .then((d) => setSessions(d.sessions || []))
      .catch(() => null);
  }, []);

  // Periodically refresh KPI snapshot only when live (low frequency)
  useEffect(() => {
    if (activity.status !== "running" && activity.status !== "progress") return;
    const id = setInterval(() => {
      // knowledge KPIs from server render path via journal kpis
      fetch("/api/journal")
        .then((r) => r.json())
        .then((d) => {
          if (d.kpis) {
            setKpis((prev) => ({
              ...prev,
              knowledge_added_today: d.kpis.added_today ?? prev.knowledge_added_today,
              pending_review: d.kpis.pending_review ?? prev.pending_review,
              knowledge_coverage: d.kpis.coverage ?? prev.knowledge_coverage,
              first_knowledge: d.kpis.first_knowledge ?? prev.first_knowledge,
            }));
          }
        })
        .catch(() => null);
    }, 3000);
    return () => clearInterval(id);
  }, [activity.status]);

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
      const res = await startLive(instruction);
      if (!res.ok) setMsg(res.error || "Failed to start");
      else setMsg(`Live session started (pid ${res.pid ?? "—"})`);
    } catch (e) {
      setMsg(e instanceof Error ? e.message : "Failed");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="space-y-4">
      <div className="flex flex-col gap-3 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <p className="text-xs text-zinc-500">LIVE AI LEARNING DASHBOARD</p>
          <p className="mt-1 max-w-2xl text-sm text-zinc-200">
            Watch IDA learn in realtime. Architecture is frozen — this only
            activates the existing pipeline and makes every stage observable.
          </p>
          <div className="mt-2 flex flex-wrap gap-1.5">
            <Badge className={connected ? "text-emerald-300" : ""}>
              stream {connected ? "connected" : "offline"}
            </Badge>
            <Badge>coverage {kpis.knowledge_coverage}%</Badge>
            <Badge>added today {kpis.knowledge_added_today}</Badge>
            <Badge>review {kpis.pending_review}</Badge>
          </div>
        </div>
        <div className="flex w-full max-w-xl flex-col gap-2">
          <Input
            value={instruction}
            onChange={(e) => setInstruction(e.target.value)}
            placeholder="Learn SAP ERP / Industry Banking / …"
          />
          <div className="flex flex-wrap gap-2">
            <Button size="sm" disabled={busy} onClick={onStart}>
              Start live learning
            </Button>
            <Button
              size="sm"
              variant="secondary"
              disabled={!sessions[0]}
              onClick={() => sessions[0] && replay(sessions[0].session_id, 280)}
            >
              Replay last session
            </Button>
          </div>
          {msg ? <p className="text-[11px] text-zinc-400">{msg}</p> : null}
        </div>
      </div>

      <Card>
        <CardHeader title="Learning activity" description="Live process observation" />
        <CardBody>
          <LiveProgress activity={activity} events={events} />
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
            <div className="text-[10px] uppercase text-zinc-500">
              Updated today
            </div>
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
            <div className="text-[10px] uppercase text-zinc-500">
              Waiting review
            </div>
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
            description="Newest learning signals first"
          />
          <CardBody className="max-h-72 space-y-1 overflow-y-auto text-xs scrollbar-thin">
            {feed.length === 0 ? (
              <p className="text-zinc-500">
                Start a live mission to see knowledge appear in realtime.
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
            title="Learning timeline"
            description="Stages animate as events arrive"
          />
          <CardBody className="max-h-72 space-y-1 overflow-y-auto font-mono text-[11px] scrollbar-thin">
            {events.length === 0 ? (
              <p className="font-sans text-xs text-zinc-500">
                Timeline idle — waiting for live events via SSE.
              </p>
            ) : (
              events.slice(-30).map((e, i) => (
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
          title="Replay sessions"
          description="Exact event stream as it happened"
        />
        <CardBody className="flex flex-wrap gap-2 text-xs">
          {sessions.length === 0 ? (
            <p className="text-zinc-500">No recorded sessions yet</p>
          ) : (
            sessions.slice(0, 8).map((s) => (
              <Button
                key={s.session_id}
                size="sm"
                variant="outline"
                onClick={() => replay(s.session_id, 250)}
              >
                {s.session_id} ({s.events})
              </Button>
            ))
          )}
        </CardBody>
      </Card>
    </div>
  );
}
