# SpecSense v0.6.0 — Decision Handoff Test Plan

**Status:** Updated for approved Option A (2026-11-03); no tests run against Copilot yet  
**Baseline:** SpecSense v0.5.4

## Static / package checks

- [ ] Exactly eight command contributions still exist in `preset.yml` with `strategy: wrap` and the unchanged native `speckit.*` names.
- [ ] Each wrapper contains a single valid `{CORE_TEMPLATE}` placeholder; no core source/template/script is copied or altered.
- [ ] `specify preset resolve` points all eight commands to the intended preset after install.
- [ ] Core scripts and templates resolve through normal Spec Kit priority rules.
- [ ] README explains the limitations of model-based enforcement and the approved **plan-only bounded cleanup exception**.
- [ ] `docs/decision-handoff-requirements.md`, `docs/decision-handoff-technical-design.md`, and this test plan are included in the release ZIP.

## Agent behavior / manual acceptance scenarios

| ID | Scenario | Expected behavior |
| --- | --- | --- |
| T01 | `specify` asks about a technical decision destined for `plan`; user approves it. | At final spec write, one pending entry appears, with destination and exact approved meaning. |
| T02 | User only discusses an architecture suggestion without approving. | No pending entry; downstream must not treat a proposal as ratified. |
| T03 | `clarify` follows T01. | Reads and preserves the pending entry; does not repeat the approved question. |
| T04 | `plan` follows T01 and final write is approved. | `research.md` or appropriate native design artifact contains the full decision; only **after verifying it**, `plan` removes the matching pending entry from active `spec.md`, without another approval. |
| T05 | Target write fails or semantic verification fails. | Original pending entry survives; no false completion report. |
| T06 | Transfer completes but `spec.md` cleanup fails. | Destination survives, original remains; reports incomplete cleanup (not a fully completed handoff) and never loses meaning. |
| T07 | Retry `plan` after T06. | Detects existing destination decision; does not duplicate; verifies it and removes only the matching pending source entry when preconditions still hold. |
| T08 | A material new contradiction appears. | Explain old decision and new evidence; ask to resolve only changed matter. |
| T09 | Approved product requirement and technical handoff coexist in `spec.md`. | Permanent requirement, Clarifications, and unrelated text remain byte-for-byte intact as practical; only the verified pending entry is removed. |
| T10 | A feature created before v0.6.0 has no pending section. | No migration or rewriting; native artifact consumption still works. |
| T11 | Multiple handoffs target different stages. | Transfer only currently applicable entries; preserve all others. |
| T12 | `analyze` reviews pending items. | Read-only report; does not add, transfer, or erase entries. |
| T13 | `converge` reviews pending items. | Only its standard append-only convergence tasks may be written after approval; no source cleanup. |
| T14 | `checklist` reads a pending decision. | Does not redundantly question the approved requirement; does not rewrite existing checklist content. |
| T15 | `constitution` encounters a feature technical decision. | Does not move it into governance or mutate feature artifacts. |
| T16 | User rejects the stage's final write. | No new pending entries or target artifact modifications. |
| T17 | A single chat spans `specify`, `clarify`, `plan`, `tasks`. | No repeated question for an approved decision; result independent of long chat context where artifacts suffice. |
| T18 | New Copilot chat starts at `plan`. | Same approved decision is found in durable artifacts without needing the prior conversation. |
| T19 | Core setup/hook mutates unexpectedly during discovery. | Agent avoids or blocks premature write and reports the constraint. |
| T20 | Temp section causes native spec quality checker to flag HOW details. | Conflict detected and surfaced; do not silently bypass the checker. |
| T21 | Existing selected `spec.md` changes before transfer. | Re-check source/target; ask only if change materially affects the approved decision. |
| T22 | `--auto` is used. | Existing critical approval gates remain effective; no unauthorized transfer or cleanup. |
| T23 | Two pending entries exist, one targeted at `plan`, the other at `tasks`. | `plan` transfers and removes only its verified entry; leaves the `tasks` entry unchanged and keeps the section heading. |
| T24 | The source entry changes between plan approval and cleanup (or active feature switches). | Abort source deletion; never mutate a different feature or remove an ambiguous/modified entry. |
| T25 | Destination contains a matching topic but omits an approved qualifier (e.g., retry cap). | Semantic verification fails; preserve source entry and report missing detail. |
| T26 | Verify permission boundaries for all commands. | `analyze` never writes; `converge` remains append-only; `plan` is the only command granted the explicit bounded cross-artifact cleanup exception. |
| T27 | All `Pending Handoffs` entries in `spec.md` were successfully transferred and verified by `plan`. | Cleanup removes the now-empty heading, leaving all canonical sections unchanged. |

## Outcome metrics

- Repeated questions about already approved decisions: **0** in T01/T03/T04/T17/T18.
- Lost approved decisions after interrupted writes: **0** in T05/T06.
- Unauthorized writes from `analyze` and `converge`: **0**.
- Existing v0.5.4 approval and output formatting regressions: **0** in smoke tests.

## Release gate

Do not call v0.6.0 complete until static checks pass and at least T01–T10, T12–T13, T17–T18, T20–T21, **T23–T27** pass in a clean Spec Kit + Copilot test repository. Option A is approved in the design but still requires observed behavior tests before release.
