"use client";

import { useCallback, useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardBody, CardHeader } from "@/components/ui/card";
import { cn } from "@/lib/utils";
import { X } from "lucide-react";

type CandidateRow = {
  candidate_id: string;
  entity_id: string;
  target_dataset: string;
  canonical_name: string;
  confidence: number;
  source_id: string;
  validation_status: string;
  reviewer?: string | null;
  path?: string;
};

type FullCandidate = CandidateRow & {
  payload?: Record<string, unknown>;
  provenance?: {
    source_id?: string;
    source_url?: string;
    confidence?: number;
    validation_status?: string;
    reviewer?: string | null;
    retrieved_at?: string;
  };
  metadata?: Record<string, unknown>;
  rejection_reasons?: string[];
  queue?: string;
};

type Queues = {
  pending: CandidateRow[];
  approved: CandidateRow[];
  rejected: CandidateRow[];
  counts: { pending: number; approved: number; rejected: number };
  waiting?: boolean;
};

export function ReviewClient({ initial }: { initial: Queues }) {
  const [queues, setQueues] = useState<Queues>(initial);
  const [tab, setTab] = useState<"pending" | "approved" | "rejected">("pending");
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [detail, setDetail] = useState<FullCandidate | null>(null);
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const refresh = useCallback(async () => {
    try {
      const res = await fetch("/api/review", { cache: "no-store" });
      const data = await res.json();
      if (data.ok !== false) {
        setQueues({
          pending: data.pending || [],
          approved: data.approved || [],
          rejected: data.rejected || [],
          counts: data.counts || { pending: 0, approved: 0, rejected: 0 },
          waiting: data.waiting,
        });
      }
    } catch {
      /* keep last good state */
    }
  }, []);

  // Auto-refresh pending queue — no manual refresh required
  useEffect(() => {
    void refresh();
    const id = setInterval(() => void refresh(), 4000);
    return () => clearInterval(id);
  }, [refresh]);

  useEffect(() => {
    if (!selectedId) {
      setDetail(null);
      return;
    }
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch(
          `/api/review?candidate_id=${encodeURIComponent(selectedId)}`,
          { cache: "no-store" }
        );
        const data = await res.json();
        if (!cancelled && data.candidate) setDetail(data.candidate);
      } catch {
        if (!cancelled) setDetail(null);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [selectedId]);

  // Auto-open first pending when list appears and nothing selected
  useEffect(() => {
    if (tab === "pending" && !selectedId && queues.pending[0]) {
      setSelectedId(queues.pending[0].candidate_id);
    }
  }, [queues.pending, selectedId, tab]);

  const rows =
    tab === "pending"
      ? queues.pending
      : tab === "approved"
        ? queues.approved
        : queues.rejected;

  async function act(action: "approve" | "reject", candidateId: string) {
    setBusy(true);
    setMsg(null);
    setError(null);
    try {
      const res = await fetch("/api/review", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          action,
          candidate_id: candidateId,
          publish: true,
        }),
      });
      const data = await res.json();
      if (!res.ok || data.ok === false) {
        setError(
          data.result?.message ||
            data.error ||
            data.recovery ||
            `Failed to ${action}`
        );
      } else {
        setMsg(data.result?.message || `${action} ok`);
        if (data.queues) {
          setQueues({
            pending: data.queues.pending || [],
            approved: data.queues.approved || [],
            rejected: data.queues.rejected || [],
            counts: data.queues.counts || {
              pending: 0,
              approved: 0,
              rejected: 0,
            },
          });
        } else {
          await refresh();
        }
        // Advance to next pending
        const next = (data.queues?.pending || []).find(
          (c: CandidateRow) => c.candidate_id !== candidateId
        );
        setSelectedId(next?.candidate_id || null);
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Request failed");
    } finally {
      setBusy(false);
    }
  }

  const conf = Number(
    detail?.provenance?.confidence ?? detail?.confidence ?? 0
  );

  return (
    <div className="relative space-y-4">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight text-[var(--text)]">
            Review
          </h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            Approve knowledge to publish · Reject to archive
          </p>
        </div>
        <div className="flex flex-wrap gap-2 text-sm">
          <span className="rounded-full bg-amber-500/15 px-3 py-1 text-amber-200">
            {queues.counts.pending} waiting
          </span>
          <span className="rounded-full bg-emerald-500/15 px-3 py-1 text-emerald-300">
            {queues.counts.approved} approved
          </span>
          <span className="rounded-full bg-zinc-800 px-3 py-1 text-zinc-400">
            {queues.counts.rejected} rejected
          </span>
        </div>
      </div>

      {msg ? (
        <p className="text-sm text-emerald-400">{msg}</p>
      ) : null}
      {error ? (
        <p className="text-sm text-red-400">{error}</p>
      ) : null}

      <Card className="border-zinc-800/60 bg-zinc-950/40">
        <CardHeader
          title="Knowledge candidates"
          description="Select a row to open the review panel"
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
        <CardBody className="p-0">
          {rows.length === 0 ? (
            <p className="px-5 py-10 text-center text-sm text-[var(--text-faint)]">
              {tab === "pending"
                ? "No candidates waiting. Start a learning mission to generate knowledge."
                : `No ${tab} candidates.`}
            </p>
          ) : (
            <ul className="divide-y divide-zinc-900/80">
              {rows.map((c) => (
                <li key={c.candidate_id}>
                  <button
                    type="button"
                    onClick={() => setSelectedId(c.candidate_id)}
                    className={cn(
                      "flex w-full items-center justify-between gap-4 px-5 py-4 text-left transition-colors hover:bg-zinc-900/50",
                      selectedId === c.candidate_id && "bg-sky-500/10"
                    )}
                  >
                    <div className="min-w-0">
                      <div className="truncate text-base font-medium text-zinc-100">
                        {c.canonical_name || c.entity_id}
                      </div>
                      <div className="mt-0.5 truncate text-xs text-zinc-500">
                        {c.target_dataset} · {c.source_id || "source"} ·{" "}
                        {c.candidate_id}
                      </div>
                    </div>
                    <div className="shrink-0 text-right">
                      <div className="text-sm font-medium text-sky-300">
                        {Math.round(Number(c.confidence || 0) * 100)}%
                      </div>
                      <div className="text-[11px] text-zinc-500">confidence</div>
                    </div>
                  </button>
                </li>
              ))}
            </ul>
          )}
        </CardBody>
      </Card>

      {/* Slide-over review panel */}
      {selectedId && detail ? (
        <div className="fixed inset-0 z-50 flex justify-end">
          <button
            type="button"
            aria-label="Close"
            className="absolute inset-0 bg-black/50 backdrop-blur-[2px]"
            onClick={() => setSelectedId(null)}
          />
          <aside className="relative flex h-full w-full max-w-lg flex-col border-l border-zinc-800 bg-[#0c0c0f] shadow-2xl animate-in">
            <div className="flex items-start justify-between gap-3 border-b border-zinc-800/80 px-6 py-5">
              <div className="min-w-0">
                <p className="text-xs uppercase tracking-wider text-zinc-500">
                  Review candidate
                </p>
                <h2 className="mt-1 text-xl font-semibold text-zinc-50">
                  {detail.canonical_name || detail.entity_id}
                </h2>
                <p className="mt-1 font-mono text-[11px] text-zinc-600">
                  {detail.candidate_id}
                </p>
              </div>
              <button
                type="button"
                onClick={() => setSelectedId(null)}
                className="rounded-lg p-2 text-zinc-500 hover:bg-zinc-900 hover:text-zinc-200"
              >
                <X className="h-4 w-4" />
              </button>
            </div>

            <div className="flex-1 space-y-5 overflow-y-auto px-6 py-5 scrollbar-thin">
              <section className="grid grid-cols-2 gap-3">
                <Metric label="Confidence" value={`${Math.round(conf * 100)}%`} accent="sky" />
                <Metric
                  label="Dataset"
                  value={detail.target_dataset || "—"}
                  accent="emerald"
                />
                <Metric
                  label="Source"
                  value={detail.provenance?.source_id || detail.source_id || "—"}
                />
                <Metric label="Entity" value={detail.entity_id || "—"} />
              </section>

              <section>
                <h3 className="text-xs font-medium uppercase tracking-wider text-zinc-500">
                  Evidence
                </h3>
                <p className="mt-2 break-all text-sm text-zinc-300">
                  {detail.provenance?.source_url || "No source URL"}
                </p>
                <p className="mt-1 text-xs text-zinc-500">
                  Retrieved {detail.provenance?.retrieved_at || "—"}
                </p>
              </section>

              <section>
                <h3 className="text-xs font-medium uppercase tracking-wider text-zinc-500">
                  Suggested dataset
                </h3>
                <p className="mt-2 text-sm text-zinc-200">
                  {detail.target_dataset}
                </p>
              </section>

              <section>
                <h3 className="text-xs font-medium uppercase tracking-wider text-zinc-500">
                  Publish preview
                </h3>
                <div className="mt-2 max-h-56 overflow-y-auto rounded-xl border border-zinc-800/80 bg-zinc-950/80 p-3 font-mono text-[11px] text-zinc-400 scrollbar-thin">
                  <pre className="whitespace-pre-wrap">
                    {JSON.stringify(detail.payload || {}, null, 2)}
                  </pre>
                </div>
              </section>

              {detail.metadata ? (
                <section>
                  <h3 className="text-xs font-medium uppercase tracking-wider text-zinc-500">
                    Mission context
                  </h3>
                  <p className="mt-2 text-xs text-zinc-400">
                    Mission {String(detail.metadata.mission_id || "—")} · Session{" "}
                    {String(detail.metadata.session_id || "—")}
                  </p>
                </section>
              ) : null}
            </div>

            {detail.queue === "pending" || tab === "pending" ? (
              <div className="flex gap-3 border-t border-zinc-800/80 px-6 py-4">
                <Button
                  className="flex-1"
                  disabled={busy}
                  onClick={() => act("approve", detail.candidate_id)}
                >
                  Approve & Publish
                </Button>
                <Button
                  className="flex-1"
                  variant="danger"
                  disabled={busy}
                  onClick={() => act("reject", detail.candidate_id)}
                >
                  Reject
                </Button>
              </div>
            ) : (
              <div className="border-t border-zinc-800/80 px-6 py-4 text-sm text-zinc-500">
                Status: {detail.provenance?.validation_status || detail.queue}
              </div>
            )}
          </aside>
        </div>
      ) : null}
    </div>
  );
}

function Metric({
  label,
  value,
  accent,
}: {
  label: string;
  value: string;
  accent?: "sky" | "emerald";
}) {
  return (
    <div className="rounded-xl border border-zinc-800/60 bg-zinc-950/60 px-3 py-3">
      <div className="text-[10px] uppercase tracking-wider text-zinc-500">
        {label}
      </div>
      <div
        className={cn(
          "mt-1 truncate text-sm font-medium",
          accent === "sky" && "text-sky-300",
          accent === "emerald" && "text-emerald-300",
          !accent && "text-zinc-100"
        )}
      >
        {value}
      </div>
    </div>
  );
}
