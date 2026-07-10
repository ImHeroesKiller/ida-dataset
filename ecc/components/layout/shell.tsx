"use client";

import { Sidebar } from "@/components/layout/sidebar";
import { Topbar } from "@/components/layout/topbar";
import { InspectorPanel } from "@/components/layout/inspector";
import { InspectorProvider } from "@/components/layout/inspector-context";
import { BottomConsole } from "@/components/console/bottom-console";
import { ProgressBar } from "@/components/shared/progress-bar";

export function Shell({
  title,
  children,
}: {
  title?: string;
  children: React.ReactNode;
}) {
  return (
    <InspectorProvider>
      <div className="flex h-screen w-screen overflow-hidden bg-[var(--bg)] text-zinc-100">
        <Sidebar />
        <div className="flex min-w-0 flex-1 flex-col">
          <div className="flex min-h-0 flex-1">
            <div className="flex min-w-0 flex-1 flex-col">
              <Topbar title={title} />
              <ProgressBar />
              <main className="min-h-0 flex-1 overflow-y-auto p-4 scrollbar-thin">
                {children}
              </main>
            </div>
            <InspectorPanel />
          </div>
          <BottomConsole />
        </div>
      </div>
    </InspectorProvider>
  );
}
