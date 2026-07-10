"use client";

import { useCallback, useEffect, useState } from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { StatusBadge } from "@/components/ui/badge";
import type { ModuleStatus } from "@/lib/status";

type Dash = Record<string, unknown>;

function healthToStatus(h: string): ModuleStatus {
  if (h === "healthy" || h === "idle") return "healthy";
  if (h === "degraded" || h === "rate_limited") return "waiting";
  if (h === "error") return "error";
  if (h === "disabled") return "disabled";
  return "waiting";
}

export function NetworkClient({ initial }: { initial: Dash }) {
  const [dash, setDash] = useState(initial);
  const [query, setQuery] = useState("");
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);
  const [lastSearch, setLastSearch] = useState<Record<string, unknown> | null>(
    null
  );

  const refresh = useCallback(async () => {
    try {
      const res = await fetch("/api/network", { cache: "no-store" });
      setDash(await res.json());
    } catch {
      /* ignore */
    }
  }, []);

  useEffect(() => {
    const id = setInterval(refresh, 5000);
    return () => clearInterval(id);
  }, [refresh]);

  async function post(action: string, body: Record<string, unknown> = {}) {
    setBusy(true);
    setMsg(null);
    try {
      const res = await fetch("/api/network", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action, ...body }),
      });
      const data = await res.json();
      if (!res.ok) setMsg(data.stderr || data.error || "failed");
      else {
        setMsg(`${action} ok`);
        if (action === "search") setLastSearch(data.result || data);
        await refresh();
      }
    } catch (e) {
      setMsg(e instanceof Error ? e.message : "failed");
    } finally {
      setBusy(false);
    }
  }

  const connectors = (dash.connectors || []) as Record<string, unknown>[];
  const queue = (dash.queue || {}) as Record<string, unknown>;
  const counts = (queue.counts || {}) as Record<string, number>;
  const metrics = (dash.metrics || {}) as Record<string, unknown>;
  const totals = (metrics.totals || {}) as Record<string, number>;
  const events = (dash.events || []) as Record<string, unknown>[];

  return (
    <div className="space-y-4">
      <div className="flex flex-col gap-2 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <p className="text-sm text-zinc-300">
            Controlled Knowledge Network — connectors acquire documents only.
          </p>
          <p className="mt-1 text-xs text-zinc-500">
            Scheduler → Planner → Policy → Connector Manager → Document Queue →
            Pipeline → Review → Publisher
          </p>
          <div className="mt-2 flex flex-wrap gap-1.5">
            <Badge>connectors {connectors.length}</Badge>
            <Badge>queue {Number(queue.queue_length || 0)}</Badge>
            <Badge>searches {totals.searches ?? 0}</Badge>
            <Badge>downloads {totals.downloads ?? 0}</Badge>
          </div>
        </div>
        <div className="flex flex-wrap gap-2">
          <Button size="sm" disabled={busy} onClick={() => post("health")}>
            Health check
          </Button>
          <Button
            size="sm"
            variant="secondary"
            disabled={busy}
            onClick={() => post("connect")}
          >
            Connect
          </Button>
          <Button size="sm" variant="outline" disabled={busy} onClick={refresh}>
            Refresh
          </Button>
        </div>
      </div>

      <Card>
        <CardHeader
          title="Planner search request"
          description="Dry-run document acquisition via Search Orchestrator"
        />
        <CardBody className="flex flex-col gap-2 sm:flex-row">
          <Input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Indonesian manufacturing industry"
          />
          <Button
            size="sm"
            disabled={busy || !query.trim()}
            onClick={() => post("search", { query, limit: 5 })}
          >
            Search + queue
          </Button>
        </CardBody>
        {msg ? <div className="px-4 pb-3 text-[11px] text-zinc-400">{msg}</div> : null}
      </Card>

      <div className="grid gap-3 lg:grid-cols-3">
        <Card className="lg:col-span-2">
          <CardHeader title="Connectors" description="Registry + live health" />
          <CardBody className="overflow-x-auto p-0">
            <table className="w-full min-w-[720px] text-left text-xs">
              <thead className="border-b border-zinc-800 text-[10px] uppercase text-zinc-500">
                <tr>
                  <th className="px-3 py-2">Name</th>
                  <th className="px-3 py-2">Type</th>
                  <th className="px-3 py-2">Trust</th>
                  <th className="px-3 py-2">Health</th>
                  <th className="px-3 py-2">Rate left</th>
                  <th className="px-3 py-2">Enabled</th>
                </tr>
              </thead>
              <tbody>
                {connectors.length === 0 ? (
                  <tr>
                    <td colSpan={6} className="px-3 py-4 text-zinc-500">
                      Waiting for first execution
                    </td>
                  </tr>
                ) : (
                  connectors.map((c) => {
                    const h = (c.health || {}) as Record<string, unknown>;
                    return (
                      <tr
                        key={String(c.connector_id)}
                        className="border-b border-zinc-900"
                      >
                        <td className="px-3 py-2 text-zinc-100">
                          {String(c.name)}
                          <div className="font-mono text-[10px] text-zinc-500">
                            {String(c.connector_id)}
                          </div>
                        </td>
                        <td className="px-3 py-2 text-zinc-400">
                          {String(c.type)}
                        </td>
                        <td className="px-3 py-2 text-zinc-300">
                          {String(c.trust_score)}
                        </td>
                        <td className="px-3 py-2">
                          <StatusBadge
                            status={healthToStatus(String(h.health || "unknown"))}
                          />
                        </td>
                        <td className="px-3 py-2 text-zinc-400">
                          {String(c.rate_remaining ?? "—")}
                        </td>
                        <td className="px-3 py-2 text-zinc-400">
                          {String(c.enabled)}
                        </td>
                      </tr>
                    );
                  })
                )}
              </tbody>
            </table>
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Document Queue" description="No direct dataset writes" />
          <CardBody className="space-y-2 text-xs text-zinc-400">
            <div>Incoming: {counts.incoming ?? 0}</div>
            <div>Processing: {counts.processing ?? 0}</div>
            <div>Processed: {counts.processed ?? 0}</div>
            <div>Failed: {counts.failed ?? 0}</div>
            <div className="pt-2 text-zinc-200">
              Length: {Number(queue.queue_length || 0)}
            </div>
          </CardBody>
        </Card>
      </div>

      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader title="Connector Logs" description="Live event stream" />
          <CardBody className="max-h-64 space-y-1 overflow-y-auto font-mono text-[11px] scrollbar-thin">
            {events.length === 0 ? (
              <p className="font-sans text-xs text-zinc-500">
                Waiting for first execution
              </p>
            ) : (
              [...events].reverse().map((e, i) => (
                <div key={i} className="text-zinc-400">
                  <span className="text-zinc-600">
                    {String(e.ts || "").slice(11, 19)}
                  </span>{" "}
                  <span className="text-sky-400">{String(e.connector_id)}</span>{" "}
                  <span className="text-zinc-200">{String(e.event)}</span> —{" "}
                  {String(e.detail)}
                </div>
              ))
            )}
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Last search" description="Merged dry-run results" />
          <CardBody className="max-h-64 overflow-y-auto text-xs scrollbar-thin">
            {!lastSearch ? (
              <p className="text-zinc-500">Waiting for first execution</p>
            ) : (
              <pre className="whitespace-pre-wrap font-mono text-[11px] text-zinc-400">
                {JSON.stringify(lastSearch, null, 2).slice(0, 4000)}
              </pre>
            )}
          </CardBody>
        </Card>
      </div>
    </div>
  );
}
