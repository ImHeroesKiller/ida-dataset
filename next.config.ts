import type { NextConfig } from "next";
import path from "path";
import { fileURLToPath } from "url";
import { execSync } from "child_process";

const configDir = path.dirname(fileURLToPath(import.meta.url));

/**
 * ECC lives at the repository root so Vercel auto-detects Next.js.
 * Knowledge assets (domains/, metadata/, automation/, …) are siblings.
 *
 * distDir is the default `.next` so the Vercel Next.js builder can
 * collect and upload static chunks without a custom Output Directory.
 * (Previous monorepo leftover `ecc/.next` + vercel outputDirectory caused
 * intermittent ChunkLoadError / asset 404 after rolling deploys.)
 */
const knowledgeGlobs = [
  "./VERSION",
  "./domains/**/*",
  "./relationships/**/*",
  "./metadata/**/*",
  "./automation/config/**/*",
  "./automation/queue/**/*",
  "./automation/queue/publish/**/*",
  "./automation/review/**/*",
  "./automation/ci/**/*",
  "./automation/sessions/**/*",
  "./automation/learning/state/**/*",
  "./automation/scheduler/state/**/*",
  "./automation/missions/**/*",
  "./automation/README.md",
  "./reports/**/*",
  "./config/**/*",
  "./docs/**/*",
];

function resolveBuildId(): string {
  // Prefer Vercel git SHA so each deploy has a stable, unique asset namespace.
  const vercelSha = process.env.VERCEL_GIT_COMMIT_SHA;
  if (vercelSha && vercelSha.length >= 7) return vercelSha.slice(0, 12);

  const ciSha = process.env.GITHUB_SHA || process.env.GIT_COMMIT;
  if (ciSha && ciSha.length >= 7) return ciSha.slice(0, 12);

  try {
    return execSync("git rev-parse --short=12 HEAD", {
      cwd: configDir,
      stdio: ["ignore", "pipe", "ignore"],
    })
      .toString()
      .trim();
  } catch {
    return `local-${Date.now().toString(36)}`;
  }
}

const nextConfig: NextConfig = {
  // Default distDir (`.next`) — do not set Output Directory on Vercel.
  // outputFileTracingRoot keeps knowledge assets next to the app on serverless.
  outputFileTracingRoot: configDir,
  outputFileTracingIncludes: {
    "/*": knowledgeGlobs,
    "/**": knowledgeGlobs,
    "/api/*": knowledgeGlobs,
    "/api/**/*": knowledgeGlobs,
  },
  // Unique build id → unique hashed chunk URLs per deploy (cache bust).
  generateBuildId: async () => resolveBuildId(),
  // Explicit defaults — no basePath / assetPrefix / trailingSlash surprises.
  basePath: "",
  assetPrefix: undefined,
  trailingSlash: false,
  serverExternalPackages: [],
  /**
   * HTML / document routes must never be served stale after a new deploy.
   * Hashed `/_next/static/*` assets already get immutable long-cache from
   * the Vercel Next.js builder; this only hardens document + API surfaces.
   */
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          {
            key: "X-Content-Type-Options",
            value: "nosniff",
          },
        ],
      },
      {
        // Never cache App Router HTML / RSC payloads across deploys.
        source: "/((?!_next/static|_next/image|favicon.ico).*)",
        headers: [
          {
            key: "Cache-Control",
            value: "private, no-cache, no-store, max-age=0, must-revalidate",
          },
        ],
      },
      {
        // Belt-and-suspenders for static chunks (Vercel already immutable).
        source: "/_next/static/:path*",
        headers: [
          {
            key: "Cache-Control",
            value: "public, max-age=31536000, immutable",
          },
        ],
      },
    ];
  },
};

export default nextConfig;
