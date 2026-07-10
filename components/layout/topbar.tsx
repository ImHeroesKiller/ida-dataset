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
    <header className="flex h-[var(--topbar-h)] items-center gap-4 border-b border-zinc-800/50 bg-[#0a0a0c]/90 px-6 backdrop-blur sm:px-8">
      <div className="min-w-0 shrink-0">
        <div className="text-sm font-medium text-zinc-100">
          {title ?? "Dashboard"}
        </div>
      </div>

      <div className="relative mx-auto w-full max-w-md">
        <Search className="pointer-events-none absolute top-1/2 left-3 h-3.5 w-3.5 -translate-y-1/2 text-zinc-600" />
        <Input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          onFocus={() => q && setOpen(true)}
          placeholder="Search knowledge…"
          className="rounded-xl border-zinc-800/80 bg-zinc-950/60 pl-9"
        />

        {open && (hits.length > 0 || loading) ? (
          <div className="absolute top-[calc(100%+8px)] right-0 left-0 z-50 overflow-hidden rounded-xl border border-zinc-800 bg-zinc-950 shadow-2xl">
            <div className="max-h-72 overflow-y-auto scrollbar-thin">
              {loading && hits.length === 0 ? (
                <div className="px-3 py-2 text-xs text-zinc-500">Searching…</div>
              ) : null}
              {hits.map((hit) => (
                <button
                  key={`${hit.type}-${hit.id}`}
                  className={cn(
                    "flex w-full items-start gap-2 border-b border-zinc-900 px-3 py-2.5 text-left hover:bg-zinc-900"
                  )}
                  onClick={() => {
                    setOpen(false);
                    setQ("");
                    // Map internal routes to executive surfaces
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
                  <span className="mt-0.5 rounded-md bg-zinc-900 px-1.5 py-0.5 text-[10px] uppercase tracking-wide text-zinc-500">
                    {hit.type}
                  </span>
                  <span className="min-w-0">
                    <span className="block truncate text-xs text-zinc-100">
                      {hit.title}
                    </span>
                    {hit.subtitle ? (
                      <span className="block truncate text-[11px] text-zinc-500">
                        {hit.subtitle}
                      </span>
                    ) : null}
                  </span>
                </button>
              ))}
            </div>
          </div>
        ) : null}
      </div>
    </header>
  );
}
