import Link from "next/link";
import { Card, CardBody } from "@/components/ui/card";
import { cn } from "@/lib/utils";

export type MetricTone = "green" | "blue" | "amber" | "neutral";

const tones: Record<MetricTone, string> = {
  green: "text-emerald-600 dark:text-emerald-300",
  blue: "text-blue-600 dark:text-sky-300",
  amber: "text-amber-600 dark:text-amber-200",
  neutral: "text-[var(--text)]",
};

/** Single metric card — design-system source of truth for KPI tiles. */
export function MetricCard({
  label,
  value,
  hint,
  tone = "neutral",
  href,
}: {
  label: string;
  value: string;
  hint?: string;
  tone?: MetricTone;
  href?: string;
}) {
  const inner = (
    <Card className="transition-transform duration-150 hover:-translate-y-0.5">
      <CardBody className="p-5">
        <p className="text-xs uppercase tracking-wider text-[var(--text-faint)]">
          {label}
        </p>
        <p
          className={cn(
            "mt-2 text-3xl font-semibold tracking-tight",
            tones[tone]
          )}
        >
          {value}
        </p>
        {hint ? (
          <p className="mt-2 text-xs text-[var(--text-faint)]">{hint}</p>
        ) : null}
      </CardBody>
    </Card>
  );
  if (href) return <Link href={href}>{inner}</Link>;
  return inner;
}
