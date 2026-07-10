/** Shared empty-state copy for executive tables and lists. */
export function EmptyState({
  title = "Nothing here yet",
  hint,
}: {
  title?: string;
  hint?: string;
}) {
  return (
    <div className="px-5 py-10 text-center">
      <p className="text-sm font-medium text-[var(--text-muted)]">{title}</p>
      {hint ? (
        <p className="mt-1 text-sm text-[var(--text-faint)]">{hint}</p>
      ) : null}
    </div>
  );
}
