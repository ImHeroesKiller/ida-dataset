import { cn } from "@/lib/utils";

type Variant = "default" | "secondary" | "ghost" | "danger" | "outline";

const variants: Record<Variant, string> = {
  default:
    "bg-zinc-100 text-zinc-900 hover:bg-white disabled:bg-zinc-700 disabled:text-zinc-400",
  secondary:
    "bg-zinc-900 text-zinc-100 border border-zinc-700 hover:bg-zinc-800",
  ghost: "bg-transparent text-zinc-300 hover:bg-zinc-900 hover:text-zinc-100",
  danger:
    "bg-red-500/15 text-red-300 border border-red-500/30 hover:bg-red-500/25",
  outline:
    "bg-transparent border border-zinc-700 text-zinc-200 hover:bg-zinc-900",
};

export function Button({
  className,
  variant = "default",
  size = "md",
  ...props
}: React.ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: Variant;
  size?: "sm" | "md";
}) {
  return (
    <button
      className={cn(
        "inline-flex items-center justify-center gap-1.5 rounded-xl font-medium transition-colors disabled:cursor-not-allowed disabled:opacity-50",
        size === "sm" ? "h-8 px-3 text-xs" : "h-10 px-4 text-sm",
        variants[variant],
        className
      )}
      {...props}
    />
  );
}
