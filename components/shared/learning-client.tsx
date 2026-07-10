"use client";

import { useCallback, useEffect, useState } from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge, StatusBadge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import type { ModuleStatus } from "@/lib/status";

type Dash = Record<string, unknown>;

function pctBar(label: string, value: number, color: string) {
  return (
    <div className="space-y-1">
      <div className="flex justify-between text-[11px] text-zinc-400">
        <span>{label}</span>
        <span className="text-zinc-200">{value}%</span>
      </div>
      <div className="h-1.5 overflow-hidden rounded-full bg-zinc-900">
        <div
          className={`h-full rounded-full ${color}`}
          style={{ width: `${Math.min(100, Math.max(0, value))}%` }}
        />
      </div>
    </div>
  );
}

function healthStatus(h: string): ModuleStatus {
  if (h === "healthy") return "healthy";
  if (h === "learning" || h === "nascent") return "running";
  if (h === "error") return "error";
  return "waiting";
}

export function LearningClient({ initial }: { initial: Dash }) {
  const [dash, setDash] = useState<Dash>(initial);
  const [text, setText] = useState("");
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);

  const refresh = useCallback(async () => {
    try {
      const res = await fetch("/api/learning", { cache: "no-store" });
      const data = await res.json();
      setDash(data);
    } catch {
      /* ignore */
    }
  }, []);

  useEffect(() => {
    const id = setInterval(refresh, 4000);
    return () => clearInterval(id);
  }, [refresh]);

  async function post(action: string, body: Record<string, unknown> = {}) {
    setBusy(true);
    setMsg(null);
    try {
      const res = await fetch("/api/learning", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action, ...body }),
      });
      const data = await res.json();
      if (!res.ok) {
        setMsg(data.stderr || data.error || "Request failed");
      } else {
        setMsg(`${action} ok`);
        await refresh();
      }
    } catch (e) {
      setMsg(e instanceof Error ? e.message : "Failed");
    } finally {
      setBusy(false);
    }
  }

  const growth = (dash.knowledge_growth || {}) as Record<string, number>;
  const alloc = (dash.learning_allocation || {}) as Record<string, number | string>;
  const mission = dash.current_mission as Record<string, unknown> | null;
  const activity = (dash.brain_activity || {}) as Record<string, number>;
  const timeline = (dash.learning_timeline || dash.knowledge_feed || []) as Record<
    string,
    unknown
  >[];
  const continuous = (dash.continuous_learning_queue || []) as Record<
    string,
    unknown
  >[];
  const missionQueue = (dash.mission_queue || []) as Record<string, unknown>[];
  const placeholders = (dash.placeholders || {}) as Record<string, string>;

  return (
    <div className="space-y-4">
      <div className="flex flex-col gap-3 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <p className="text-sm text-zinc-300">
            Continuous Learning never stops. Directed Learning coexists via the
            Scheduler.
          </p>
          <p className="mt-1 text-xs text-zinc-500">
            Scheduler → Priority → Planner → Policy → Pipeline → Review →
            Publisher → Telemetry
          </p>
          <div className="mt-2 flex flex-wrap gap-1.5">
            <StatusBadge status={healthStatus(String(dash.brain_health || "waiting"))} />
            <Badge>brain: {String(dash.brain_health || "waiting")}</Badge>
            <Badge>
              coverage {growth.coverage_pct ?? 0}% · {growth.datasets_populated ?? 0}/
              {growth.datasets_total ?? 0}
            </Badge>
          </div>
        </div>
        <div className="flex flex-wrap gap-2">
          <Button size="sm" disabled={busy} onClick={() => post("tick", { dry_run: true })}>
            Scheduler tick
          </Button>
          <Button size="sm" variant="secondary" disabled={busy} onClick={refresh}>
            Refresh
          </Button>
        </div>
      </div>

      <Card>
        <CardHeader
          title="Assign Directed Learning"
          description='Natural instruction → Learning Contract + Mission'
        />
        <CardBody className="space-y-2">
          <div className="flex flex-col gap-2 sm:flex-row">
            <Input
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder='e.g. "Learn everything about SAP ERP." or "Prepare for Telkom meeting."'
            />
            <Button
              size="sm"
              disabled={busy || !text.trim()}
              onClick={() => {
                post("mission", { text });
                setText("");
              }}
            >
              Create mission
            </Button>
          </div>
          {msg ? <p className="text-[11px] text-zinc-400">{msg}</p> : null}
        </CardBody>
      </Card>

      <div className="grid gap-3 lg:grid-cols-3">
        <Card>
          <CardHeader title="Brain Health" description="Learning vitality" />
          <CardBody className="space-y-2 text-xs text-zinc-400">
            <div className="text-2xl font-semibold text-zinc-100">
              {String(dash.brain_health || "waiting")}
            </div>
            <div>Ticks: {activity.ticks ?? 0}</div>
            <div>Tasks dispatched: {activity.tasks_dispatched ?? 0}</div>
            <div>Continuous cycles: {activity.continuous_cycles ?? 0}</div>
            <div>Directed cycles: {activity.directed_cycles ?? 0}</div>
            <div>Missions completed: {activity.missions_completed ?? 0}</div>
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Knowledge Growth" description="Dataset coverage" />
          <CardBody className="space-y-2 text-xs text-zinc-400">
            <div className="text-2xl font-semibold text-zinc-100">
              {growth.coverage_pct ?? 0}%
            </div>
            <div>
              Populated {growth.datasets_populated ?? 0} / {growth.datasets_total ?? 0}
            </div>
            {pctBar("Coverage", Number(growth.coverage_pct || 0), "bg-emerald-500")}
          </CardBody>
        </Card>

        <Card>
          <CardHeader
            title="Learning Allocation"
            description={String(alloc.profile || "—")}
          />
          <CardBody className="space-y-2">
            {pctBar("Continuous", Number(alloc.continuous || 0), "bg-sky-500")}
            {pctBar("Directed / Mission", Number(alloc.directed || 0), "bg-violet-500")}
            {pctBar("Maintenance", Number(alloc.maintenance || 0), "bg-zinc-500")}
            {pctBar("Ontology", Number(alloc.ontology || 0), "bg-amber-500")}
            {pctBar("Policy", Number(alloc.policy || 0), "bg-pink-500")}
          </CardBody>
        </Card>
      </div>

      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader title="Current Mission" description="Directed learning focus" />
          <CardBody className="space-y-2 text-xs">
            {!mission ? (
              <p className="text-zinc-500">Waiting for first execution</p>
            ) : (
              <>
                <div className="text-sm font-medium text-zinc-100">
                  {String(mission.title)}
                </div>
                <div className="flex flex-wrap gap-1.5">
                  <Badge>{String(mission.priority)}</Badge>
                  <Badge>{String(mission.status)}</Badge>
                  <Badge>{String(mission.progress)}%</Badge>
                </div>
                <div className="grid grid-cols-2 gap-2 text-zinc-400">
                  <div>ETA: {String(mission.eta || "—")}</div>
                  <div>Confidence: {String(mission.confidence ?? 0)}</div>
                  <div>Knowledge added: {String(mission.knowledge_added ?? 0)}</div>
                  <div>Documents: {String(mission.documents_processed ?? 0)}</div>
                  <div>Entities: {String(mission.entities_learned ?? 0)}</div>
                  <div>Stage: {String(mission.current_stage || "—")}</div>
                  <div className="col-span-2">
                    Dataset: {String(mission.current_dataset || "—")}
                  </div>
                </div>
                <div className="h-1.5 overflow-hidden rounded-full bg-zinc-900">
                  <div
                    className="h-full bg-violet-500"
                    style={{ width: `${Number(mission.progress || 0)}%` }}
                  />
                </div>
              </>
            )}
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Mission Queue" description="Directed learning backlog" />
          <CardBody className="max-h-64 space-y-1 overflow-y-auto scrollbar-thin text-xs">
            {missionQueue.length === 0 ? (
              <p className="text-zinc-500">Waiting for first execution</p>
            ) : (
              missionQueue.map((m) => (
                <div
                  key={String(m.mission_id)}
                  className="flex items-center justify-between border-b border-zinc-900 py-1.5"
                >
                  <span className="truncate text-zinc-200">{String(m.title)}</span>
                  <span className="ml-2 shrink-0 text-zinc-500">
                    {String(m.priority)} · {String(m.status)}
                  </span>
                </div>
              ))
            )}
          </CardBody>
        </Card>
      </div>

      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader
            title="Continuous Learning Queue"
            description="Always-on gap closing"
          />
          <CardBody className="max-h-64 space-y-1 overflow-y-auto scrollbar-thin text-xs">
            {continuous.length === 0 ? (
              <p className="text-zinc-500">Waiting for first execution</p>
            ) : (
              continuous.map((t) => (
                <div
                  key={String(t.task_id)}
                  className="flex justify-between border-b border-zinc-900 py-1.5"
                >
                  <span className="text-zinc-200">{String(t.title)}</span>
                  <span className="text-zinc-500">
                    {String(t.priority)} · {String(t.target_dataset)}
                  </span>
                </div>
              ))
            )}
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Learning Timeline / Knowledge Feed" description="Brain activity" />
          <CardBody className="max-h-64 space-y-1 overflow-y-auto font-mono text-[11px] scrollbar-thin">
            {timeline.length === 0 ? (
              <p className="font-sans text-xs text-zinc-500">
                Waiting for first execution
              </p>
            ) : (
              [...timeline].reverse().map((e, i) => (
                <div key={i} className="text-zinc-400">
                  <span className="text-zinc-600">
                    {String(e.ts || "").slice(11, 19)}
                  </span>{" "}
                  <span className="text-sky-400">{String(e.stream)}</span>{" "}
                  <span className="text-zinc-200">{String(e.event)}</span> —{" "}
                  {String(e.detail)}
                </div>
              ))
            )}
          </CardBody>
        </Card>
      </div>

      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardHeader title="Domain Coverage" />
          <CardBody className="text-xs text-zinc-400">
            Populated datasets proxy: {growth.coverage_pct ?? 0}%
          </CardBody>
        </Card>
        <Card>
          <CardHeader title="Knowledge Confidence" />
          <CardBody className="text-xs text-zinc-400">
            Mission confidence: {String(mission?.confidence ?? "—")}
          </CardBody>
        </Card>
        <Card>
          <CardHeader title="Reasoning Coverage" />
          <CardBody className="text-xs text-zinc-500">
            {placeholders.reasoning_coverage || "Waiting for first execution"}
          </CardBody>
        </Card>
        <Card>
          <CardHeader title="Decision Coverage" />
          <CardBody className="text-xs text-zinc-500">
            {placeholders.decision_coverage || "Waiting for first execution"}
          </CardBody>
        </Card>
      </div>
    </div>
  );
}
