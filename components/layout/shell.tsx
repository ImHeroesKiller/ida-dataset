"use client";

import { Sidebar } from "@/components/layout/sidebar";
import { Topbar } from "@/components/layout/topbar";
import { BottomConsole } from "@/components/console/bottom-console";

export function Shell({
  title,
  children,
}: {
  title?: string;
  children: React.ReactNode;
}) {
  return (
    <div className="flex h-screen w-screen overflow-hidden bg-[var(--bg)] text-zinc-100">
      <Sidebar />
      <div className="flex min-w-0 flex-1 flex-col">
        <Topbar title={title} />
        <main className="min-h-0 flex-1 overflow-y-auto px-6 py-6 scrollbar-thin sm:px-8">
          {children}
        </main>
        <BottomConsole />
      </div>
    </div>
  );
}
