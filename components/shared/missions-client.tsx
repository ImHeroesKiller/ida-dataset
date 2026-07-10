"use client";

import { useState } from "react";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { useInspector } from "@/components/layout/inspector-context";

type Row = Record<string, unknown>;

export function MissionsClient({
  missions: initialMissions,
  contracts,
  reports,
}: {
  missions: Row[];
  contracts: Row[];
  reports: { name: string; relativePath: string; mtime: string; size: number }[];
}) {
  const { inspect } = useInspector();
  const [missions, setMissions] = useState(initialMissions);
  const [text, setText] = useState("");
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);

  async function createMission() {
    if (!text.trim()) return;
    setBusy(true);
    setMsg(null);
    try {
      const res = await fetch("/api/learning", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "mission", text }),
      });
      const data = await res.json();
      if (!res.ok) {
        setMsg(data.stderr || data.error || "Failed");
      } else {
        setMsg(`Created ${data.result?.mission?.mission_id || "mission"}`);
        setText("");
        const list = await fetch("/api/missions").then((r) => r.json());
        setMissions(list.missions || []);
      }
    } catch (e) {
      setMsg(e instanceof Error ? e.message : "Failed");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="space-y-4">
      <p className="text-sm text-zinc-300">
        Directed Learning missions become Learning Contracts. They never disable
        Continuous Learning.
      </p>

      <Card>
        <CardHeader title="New mission" description="Natural language instruction" />
        <CardBody className="flex flex-col gap-2 sm:flex-row">
          <Input
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder='Study all Indonesian mining companies.'
          />
          <Button size="sm" disabled={busy} onClick={createMission}>
            Dispatch
          </Button>
        </CardBody>
        {msg ? (
          <div className="px-4 pb-3 text-[11px] text-zinc-400">{msg}</div>
        ) : null}
      </Card>

      <Card>
        <CardHeader title="Active missions" description={`${missions.length} total`} />
        <CardBody className="overflow-x-auto p-0">
          <table className="w-full min-w-[720px] text-left text-xs">
            <thead className="border-b border-zinc-800 text-[10px] uppercase text-zinc-500">
              <tr>
                <th className="px-3 py-2">Mission</th>
                <th className="px-3 py-2">Priority</th>
                <th className="px-3 py-2">Status</th>
                <th className="px-3 py-2">Progress</th>
                <th className="px-3 py-2">Contract</th>
              </tr>
            </thead>
            <tbody>
              {missions.length === 0 ? (
                <tr>
                  <td colSpan={5} className="px-3 py-4 text-zinc-500">
                    Waiting for first execution
                  </td>
                </tr>
              ) : (
                missions.map((m) => (
                  <tr
                    key={String(m.mission_id)}
                    className="border-b border-zinc-900 hover:bg-zinc-900/40"
                  >
                    <td className="px-3 py-2">
                      <button
                        className="text-left font-medium text-zinc-100 hover:underline"
                        onClick={() =>
                          inspect({
                            kind: "mission",
                            title: String(m.title),
                            subtitle: String(m.mission_id),
                            meta: {
                              Priority: String(m.priority),
                              Status: String(m.status),
                              Requester: String(m.requester),
                              Progress: `${m.progress}%`,
                            },
                            body: String(m.description || m.natural_language_request || ""),
                          })
                        }
                      >
                        {String(m.title)}
                      </button>
                      <div className="text-[10px] text-zinc-500">
                        {String(m.mission_id)}
                      </div>
                    </td>
                    <td className="px-3 py-2">
                      <Badge>{String(m.priority)}</Badge>
                    </td>
                    <td className="px-3 py-2 text-zinc-300">{String(m.status)}</td>
                    <td className="px-3 py-2 text-zinc-300">{String(m.progress)}%</td>
                    <td className="px-3 py-2 font-mono text-[10px] text-zinc-500">
                      {String(m.contract_id || "—")}
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </CardBody>
      </Card>

      <div className="grid gap-3 lg:grid-cols-2">
        <Card>
          <CardHeader title="Learning Contracts" description="Permanent history" />
          <CardBody className="max-h-64 space-y-1 overflow-y-auto text-xs scrollbar-thin">
            {contracts.length === 0 ? (
              <p className="text-zinc-500">Waiting for first execution</p>
            ) : (
              contracts.map((c) => (
                <div
                  key={String(c.contract_id)}
                  className="border-b border-zinc-900 py-1.5 text-zinc-300"
                >
                  <div className="font-mono text-[11px] text-zinc-100">
                    {String(c.contract_id)}
                  </div>
                  <div className="text-zinc-500">
                    {String(c.mission_id)} · {String(c.priority)} · alloc{" "}
                    {String(c.resource_allocation)}%
                  </div>
                </div>
              ))
            )}
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Learning reports" description="reports/learning" />
          <CardBody className="max-h-64 space-y-1 overflow-y-auto text-xs scrollbar-thin">
            {reports.length === 0 ? (
              <p className="text-zinc-500">Waiting for first execution</p>
            ) : (
              reports.map((r) => (
                <a
                  key={r.relativePath}
                  href={`/reports?file=${encodeURIComponent(r.relativePath)}`}
                  className="block border-b border-zinc-900 py-1.5 text-zinc-300 hover:text-zinc-100"
                >
                  {r.name}
                </a>
              ))
            )}
          </CardBody>
        </Card>
      </div>
    </div>
  );
}
