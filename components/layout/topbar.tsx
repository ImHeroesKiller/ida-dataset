"use client";

import { useEffect, useState } from "react";
import { Search } from "lucide-react";
import { Input } from "@/components/ui/input";
import { useRouter } from "next/navigation";
import { cn } from "@/lib/utils";

type SearchHit = {
  type: string;
  id: string;
  title: string;
  subtitle?: string;
  href: string;
};

export function Topbar({ title }: { title?: string }) {
  const router = useRouter();
  const [q, setQ] = useState("");
  const [open, setOpen] = useState(false);
  const [hits, setHits] = useState<SearchHit[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!q.trim()) {
      setHits([]);
      return;
    }
    const t = setTimeout(async () => {
      setLoading(true);
      try {
        const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`);
        const data = await res.json();
        setHits(data.results ?? []);
        setOpen(true);
      } finally {
        setLoading(false);
      }
    }, 180);
    return () => clearTimeout(t);
  }, [q]);

  return (
    <header className="flex h-[var(--topbar-h)] items-center gap-4 border-b border-[var(--border)] bg-[var(--bg)]/90 px-6 backdrop-blur sm:px-8">
      <div className="min-w-0 shrink-0">
        <div className="text-sm font-medium text-[var(--text)]">
          {title ?? "Dashboard"}
        </div>
      </div>

      <div className="relative mx-auto w-full max-w-md">
        <Search className="pointer-events-none absolute top-1/2 left-3 h-3.5 w-3.5 -translate-y-1/2 text-[var(--text-faint)]" />
        <Input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          onFocus={() => q && setOpen(true)}
          placeholder="Search knowledge…"
          className="rounded-xl border-[var(--border)] bg-[var(--panel)] pl-9 text-[var(--text)] placeholder:text-[var(--text-faint)]"
        />

        {open && (hits.length > 0 || loading) ? (
          <div className="absolute top-[calc(100%+8px)] right-0 left-0 z-50 overflow-hidden rounded-xl border border-[var(--border)] bg-[var(--panel)] shadow-[var(--shadow)]">
            <div className="max-h-72 overflow-y-auto scrollbar-thin">
              {loading && hits.length === 0 ? (
                <div className="px-3 py-2 text-xs text-[var(--text-faint)]">
                  Searching…
                </div>
              ) : null}
              {hits.map((hit) => (
                <button
                  key={`${hit.type}-${hit.id}`}
                  className={cn(
                    "flex w-full items-start gap-2 border-b border-[var(--border)] px-3 py-2.5 text-left hover:bg-[var(--panel-2)]"
                  )}
                  onClick={() => {
                    setOpen(false);
                    setQ("");
                    let href = hit.href;
                    if (
                      href.startsWith("/datasets") ||
                      href.startsWith("/ontology") ||
                      href.startsWith("/sources")
                    ) {
                      href = "/knowledge";
                    }
                    if (href.startsWith("/planner") || href.startsWith("/queue")) {
                      href = "/missions";
                    }
                    if (href.startsWith("/publisher")) {
                      href = "/review";
                    }
                    router.push(href);
                  }}
                >
                  <span className="mt-0.5 rounded-md bg-[var(--panel-2)] px-1.5 py-0.5 text-[10px] uppercase tracking-wide text-[var(--text-faint)]">
                    {hit.type}
                  </span>
                  <span className="min-w-0">
                    <span className="block truncate text-xs text-[var(--text)]">
                      {hit.title}
                    </span>
                    {hit.subtitle ? (
                      <span className="block truncate text-[11px] text-[var(--text-faint)]">
                        {hit.subtitle}
                      </span>
                    ) : null}
                  </span>
                </button>
              ))}
              {!loading && hits.length === 0 ? (
                <div className="px-3 py-2 text-xs text-[var(--text-faint)]">
                  No matches
                </div>
              ) : null}
            </div>
          </div>
        ) : null}
      </div>
    </header>
  );
}
