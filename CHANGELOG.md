# Changelog

## 0.6.0 — Decision Handoff (candidate; behavioral release gate pending)

- Reuse approved decisions across all eight standard wrapped commands.
- Place concise handoff instructions after the existing interactive policy.
- Save genuinely future-stage decisions in one temporary `Pending Handoffs`
  section of an eligible native artifact at its existing final approval gate.
- Add the approved plan-only bounded cleanup exception: verify native planning
  output before removing matching plan-targeted entries from active `spec.md`.
- Preserve source decisions on failed or ambiguous transfer; require idempotent
  retries, feature identity checks and preservation of unrelated source content.
- Keep read-only, append-only, governance and native approval boundaries.
- Adopt forward-only: no historical decision migration or new registry/runtime.
- Add static contract checks, baseline policy comparison, negative package tests,
  and reproducible ZIP generation using an explicit distributable-file allowlist.

This is prompt-layer behavior, not transactional enforcement. See
`docs/validation-results.md` for evidence and outstanding Copilot acceptance tests.

## 0.5.4 — Naming consistency

- Rename preset ID and archive/source root to `spec-sense`; retain SpecSense
  as the display name and all eight v0.5.3 wrappers unchanged.
