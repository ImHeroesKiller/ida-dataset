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
    <header className="flex h-[var(--topbar-h)] items-center gap-4 border-b border-[var(--border)] bg-[var(--panel)]/95 px-6 backdrop-blur sm:px-8">
      <div className="min-w-0 shrink-0">
        <div className="text-small font-semibold text-[var(--text)]">
          {title ?? "Dashboard"}
        </div>
      </div>

      <div className="relative mx-auto w-full max-w-md">
        <Search
          className="pointer-events-none absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2 text-[var(--text-muted)]"
          aria-hidden
        />
        <Input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          onFocus={() => q && setOpen(true)}
          placeholder="Search knowledge…"
          className="pl-10"
          aria-label="Search knowledge"
        />

        {open && (hits.length > 0 || loading) ? (
          <div className="absolute top-[calc(100%+8px)] right-0 left-0 z-50 overflow-hidden rounded-[var(--radius-xl)] border border-[var(--border)] bg-[var(--panel)] shadow-[var(--shadow-md)]">
            <div className="max-h-72 overflow-y-auto scrollbar-thin">
              {loading && hits.length === 0 ? (
                <div className="px-4 py-3 text-small text-[var(--text-muted)]">
                  Searching…
                </div>
              ) : null}
              {hits.map((hit) => (
                <button
                  key={`${hit.type}-${hit.id}`}
                  type="button"
                  className={cn(
                    "flex w-full items-start gap-3 border-b border-[var(--border)] px-4 py-3 text-left hover:bg-[var(--panel-2)]"
                  )}
                  onClick={() => {
                    setOpen(false);
                    setQ("");
                    router.push(hit.href);
                  }}
                >
                  <span className="mt-0.5 rounded-md bg-[var(--panel-2)] px-2 py-0.5 text-caption font-semibold uppercase tracking-wide text-[var(--text-muted)]">
                    {hit.type}
                  </span>
                  <span className="min-w-0">
                    <span className="block truncate text-small font-medium text-[var(--text)]">
                      {hit.title}
                    </span>
                    {hit.subtitle ? (
                      <span className="block truncate text-caption text-[var(--text-muted)]">
                        {hit.subtitle}
                      </span>
                    ) : null}
                  </span>
                </button>
              ))}
              {!loading && hits.length === 0 ? (
                <div className="px-4 py-3 text-small text-[var(--text-muted)]">
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
