# Changelog

## Unreleased

### Changed

- **refactor(runtime):** migrate continuous learning to GitHub Actions sessions
  - Learning executes via `.github/workflows/learning.yml` (hourly, daily, manual, mission, dry-run)
  - Sessions stored at `automation/sessions/YYYY-MM-DD/SESSION-*.json`
  - Dashboard is a Vercel-safe monitor; Start Learning uses workflow_dispatch
  - Console is Learning Session Journal (real session logs + replay)
  - No long-lived Python runtime or server-side SSE learning stream required
