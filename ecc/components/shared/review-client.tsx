"use client";

import { useMemo, useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { useInspector } from "@/components/layout/inspector-context";
import { cn } from "@/lib/utils";

type Candidate = {
  candidate_id: string;
  entity_id: string;
  target_dataset: string;
  canonical_name: string;
  confidence: number;
  source_id: string;
  validation_status: string;
  reviewer?: string | null;
};

type LocalState = "pending" | "approved" | "rejected" | "merged";

export function ReviewClient({
  pending,
  approved,
  rejected,
  waiting,
}: {
  pending: Candidate[];
  approved: Candidate[];
  rejected: Candidate[];
  waiting: boolean;
}) {
  const { inspect } = useInspector();
  const [tab, setTab] = useState<"pending" | "approved" | "rejected">("pending");
  const [local, setLocal] = useState<Record<string, LocalState>>({});
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [msg, setMsg] = useState<string | null>(null);

  const source = tab === "pending" ? pending : tab === "approved" ? approved : rejected;

  const rows = useMemo(() => {
    return source.map((c) => ({
      ...c,
      localState: local[c.candidate_id] ?? tab,
    }));
  }, [source, local, tab]);

  function toggle(id: string) {
    setSelected((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  }

  function decide(ids: string[], state: LocalState) {
    setLocal((prev) => {
      const next = { ...prev };
      for (const id of ids) next[id] = state;
      return next;
    });
    setSelected(new Set());
    setMsg(
      `${state} marked for ${ids.length} candidate(s). Persist via KAS review CLI/API — ECC does not publish.`
    );
  }

  return (
    <Card>
      <CardHeader
        title="Queue"
        description="Approve / Reject / Merge / Bulk — never publish here"
        action={
          <div className="flex gap-1">
            {(["pending", "approved", "rejected"] as const).map((t) => (
              <Button
                key={t}
                size="sm"
                variant={tab === t ? "default" : "ghost"}
                onClick={() => setTab(t)}
              >
                {t}
              </Button>
            ))}
          </div>
        }
      />
      <CardBody className="space-y-3">
        {waiting ? (
          <p className="text-xs text-zinc-500">Waiting for first execution</p>
        ) : null}

        <div className="flex flex-wrap gap-2">
          <Button
            size="sm"
            variant="secondary"
            disabled={selected.size === 0}
            onClick={() => decide([...selected], "approved")}
          >
            Bulk Approve
          </Button>
          <Button
            size="sm"
            variant="danger"
            disabled={selected.size === 0}
            onClick={() => decide([...selected], "rejected")}
          >
            Bulk Reject
          </Button>
          {msg ? <span className="text-[11px] text-zinc-400">{msg}</span> : null}
        </div>

        <div className="overflow-x-auto">
          <table className="w-full min-w-[860px] text-left text-xs">
            <thead className="border-b border-zinc-800 text-[10px] uppercase tracking-wide text-zinc-500">
              <tr>
                <th className="px-2 py-2"></th>
                <th className="px-2 py-2">Candidate</th>
                <th className="px-2 py-2">Dataset</th>
                <th className="px-2 py-2">Entity</th>
                <th className="px-2 py-2">Confidence</th>
                <th className="px-2 py-2">Source</th>
                <th className="px-2 py-2">Status</th>
                <th className="px-2 py-2">Actions</th>
              </tr>
            </thead>
            <tbody>
              {rows.length === 0 ? (
                <tr>
                  <td colSpan={8} className="px-2 py-4 text-zinc-500">
                    Empty queue
                  </td>
                </tr>
              ) : (
                rows.map((c) => (
                  <tr
                    key={c.candidate_id}
                    className="border-b border-zinc-900/80 hover:bg-zinc-900/40"
                  >
                    <td className="px-2 py-2">
                      <input
                        type="checkbox"
                        checked={selected.has(c.candidate_id)}
                        onChange={() => toggle(c.candidate_id)}
                      />
                    </td>
                    <td className="px-2 py-2">
                      <button
                        className="font-mono text-[11px] text-zinc-200 hover:underline"
                        onClick={() =>
                          inspect({
                            kind: "review-candidate",
                            title: c.candidate_id,
                            subtitle: c.canonical_name,
                            meta: {
                              Dataset: c.target_dataset,
                              Entity: c.entity_id,
                              Confidence: String(c.confidence),
                              Source: c.source_id,
                              Status: c.localState,
                            },
                          })
                        }
                      >
                        {c.candidate_id}
                      </button>
                    </td>
                    <td className="px-2 py-2 text-zinc-400">{c.target_dataset}</td>
                    <td className="px-2 py-2 text-zinc-300">{c.entity_id}</td>
                    <td className="px-2 py-2 text-zinc-300">{c.confidence}</td>
                    <td className="px-2 py-2 text-zinc-500">{c.source_id}</td>
                    <td className="px-2 py-2">
                      <span
                        className={cn(
                          "text-[11px]",
                          c.localState === "approved" && "text-emerald-400",
                          c.localState === "rejected" && "text-red-400",
                          c.localState === "merged" && "text-sky-400",
                          c.localState === "pending" && "text-amber-300"
                        )}
                      >
                        {c.localState}
                      </span>
                    </td>
                    <td className="px-2 py-2">
                      <div className="flex flex-wrap gap-1">
                        <Button
                          size="sm"
                          variant="outline"
                          onClick={() => decide([c.candidate_id], "approved")}
                        >
                          Approve
                        </Button>
                        <Button
                          size="sm"
                          variant="ghost"
                          onClick={() => decide([c.candidate_id], "rejected")}
                        >
                          Reject
                        </Button>
                        <Button
                          size="sm"
                          variant="secondary"
                          onClick={() => decide([c.candidate_id], "merged")}
                        >
                          Merge
                        </Button>
                      </div>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </CardBody>
    </Card>
  );
}
