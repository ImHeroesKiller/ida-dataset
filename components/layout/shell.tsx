"use client";

import { Sidebar } from "@/components/layout/sidebar";
import { Topbar } from "@/components/layout/topbar";
import { BottomConsole } from "@/components/console/bottom-console";
import { InspectorProvider } from "@/components/layout/inspector-context";

/**
 * Application shell — chrome only (sidebar, topbar, main, console).
 * Operator UI v1.0 frozen density.
 */
export function Shell({
  title,
  children,
}: {
  title?: string;
  children: React.ReactNode;
}) {
  return (
    <InspectorProvider>
      <div className="flex h-screen w-screen overflow-hidden bg-[var(--bg)] text-[var(--text)]">
        <Sidebar />
        <div className="flex min-w-0 flex-1 flex-col">
          <Topbar title={title} />
          <main className="min-h-0 flex-1 overflow-y-auto px-4 py-4 scrollbar-thin sm:px-5">
            {children}
          </main>
          <BottomConsole />
        </div>
      </div>
    </InspectorProvider>
  );
}
