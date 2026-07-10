"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { NAV_ITEMS } from "@/lib/nav";
import { cn } from "@/lib/utils";

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="flex h-full w-[var(--sidebar-w)] shrink-0 flex-col border-r border-zinc-800/50 bg-[#0a0a0c]">
      <div className="flex h-[var(--topbar-h)] items-center gap-3 px-5">
        <div className="flex h-8 w-8 items-center justify-center rounded-xl bg-zinc-100 text-[11px] font-bold tracking-wide text-zinc-900">
          IDA
        </div>
        <div className="min-w-0">
          <div className="truncate text-sm font-semibold tracking-tight text-zinc-50">
            IDA Learning
          </div>
          <div className="truncate text-[11px] text-zinc-500">
            Executive AI
          </div>
        </div>
      </div>

      <nav className="flex-1 space-y-1 px-3 py-4">
        {NAV_ITEMS.map((item) => {
          const active =
            item.href === "/"
              ? pathname === "/"
              : pathname === item.href || pathname.startsWith(`${item.href}/`);
          const Icon = item.icon;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={cn(
                "flex items-center gap-3 rounded-xl px-3 py-2.5 text-sm transition-colors",
                active
                  ? "bg-zinc-100 font-medium text-zinc-900"
                  : "text-zinc-400 hover:bg-zinc-900/80 hover:text-zinc-100"
              )}
            >
              <Icon className="h-4 w-4 shrink-0 opacity-80" />
              <span className="truncate">{item.label}</span>
            </Link>
          );
        })}
      </nav>

      <div className="px-4 pb-5">
        <p className="text-[11px] leading-relaxed text-zinc-600">
          Learn · Review · Grow knowledge
        </p>
      </div>
    </aside>
  );
}
