"use client";

import {
  createContext,
  useCallback,
  useContext,
  useMemo,
  useState,
} from "react";

export type InspectorSelection = {
  kind: string;
  title: string;
  subtitle?: string;
  meta?: Record<string, string>;
  body?: string;
};

type Ctx = {
  selection: InspectorSelection | null;
  inspect: (s: InspectorSelection) => void;
  clear: () => void;
};

const InspectorContext = createContext<Ctx | null>(null);

export function InspectorProvider({ children }: { children: React.ReactNode }) {
  const [selection, setSelection] = useState<InspectorSelection | null>(null);
  const inspect = useCallback((s: InspectorSelection) => setSelection(s), []);
  const clear = useCallback(() => setSelection(null), []);
  const value = useMemo(
    () => ({ selection, inspect, clear }),
    [selection, inspect, clear]
  );
  return (
    <InspectorContext.Provider value={value}>
      {children}
    </InspectorContext.Provider>
  );
}

export function useInspector() {
  const ctx = useContext(InspectorContext);
  if (!ctx) {
    throw new Error("useInspector must be used within InspectorProvider");
  }
  return ctx;
}
