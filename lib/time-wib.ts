/**
 * Asia/Jakarta (WIB, UTC+7) display formatting for the factory UI.
 * Internal storage remains UTC ISO; only presentation converts to WIB.
 */

const WIB = "Asia/Jakarta";

function asDate(input: string | number | Date | null | undefined): Date | null {
  if (input == null || input === "" || input === "—") return null;
  if (input instanceof Date) {
    return Number.isNaN(input.getTime()) ? null : input;
  }
  const d = new Date(input);
  return Number.isNaN(d.getTime()) ? null : d;
}

/** Full format: 11 Jul 2026 08:15:32 WIB */
export function formatWib(
  input: string | number | Date | null | undefined,
  opts?: { dateOnly?: boolean; timeOnly?: boolean }
): string {
  const d = asDate(input);
  if (!d) return "—";

  if (opts?.dateOnly) {
    return new Intl.DateTimeFormat("en-GB", {
      timeZone: WIB,
      day: "2-digit",
      month: "short",
      year: "numeric",
    }).format(d);
  }

  if (opts?.timeOnly) {
    const t = new Intl.DateTimeFormat("en-GB", {
      timeZone: WIB,
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
      hour12: false,
    }).format(d);
    return `${t} WIB`;
  }

  const datePart = new Intl.DateTimeFormat("en-GB", {
    timeZone: WIB,
    day: "2-digit",
    month: "short",
    year: "numeric",
  }).format(d);
  const timePart = new Intl.DateTimeFormat("en-GB", {
    timeZone: WIB,
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false,
  }).format(d);
  return `${datePart} ${timePart} WIB`;
}

/** Compact clock for dense journals: 08:15:32 WIB */
export function formatWibTime(
  input: string | number | Date | null | undefined
): string {
  return formatWib(input, { timeOnly: true });
}

/** Date only: 11 Jul 2026 */
export function formatWibDate(
  input: string | number | Date | null | undefined
): string {
  return formatWib(input, { dateOnly: true });
}
