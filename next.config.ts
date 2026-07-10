import type { NextConfig } from "next";
import path from "path";
import { fileURLToPath } from "url";
import { execSync } from "child_process";

const configDir = path.dirname(fileURLToPath(import.meta.url));

/**
 * Single-package Next.js app at the repository root.
 * Uses the default distDir (`.next`). Do not set a custom distDir.
 * Knowledge assets (domains/, metadata/, automation/, …) are siblings of app/.
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
  // Default distDir is `.next` — leave unset. Vercel Output Directory must match.
  outputFileTracingRoot: configDir,
  outputFileTracingIncludes: {
    "/*": knowledgeGlobs,
    "/**": knowledgeGlobs,
    "/api/*": knowledgeGlobs,
    "/api/**/*": knowledgeGlobs,
  },
  generateBuildId: async () => resolveBuildId(),
  basePath: "",
  assetPrefix: undefined,
  trailingSlash: false,
  serverExternalPackages: [],
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
        source: "/((?!_next/static|_next/image|favicon.ico).*)",
        headers: [
          {
            key: "Cache-Control",
            value: "private, no-cache, no-store, max-age=0, must-revalidate",
          },
        ],
      },
      {
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
