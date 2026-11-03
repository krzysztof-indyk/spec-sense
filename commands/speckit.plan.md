{CORE_TEMPLATE}

---

## SDDW interactive policy — `speckit.plan` (overrides decision/write timing)

This is **standard Spec Kit planning**, not Lean planning. Retain the full core
planning workflow (constitution, hooks, setup scripts, `plan-template.md`, research,
design, data model, contracts, quickstart, agent-context updates, validations and
handoffs). Only introduce an interactive design/approval gate BEFORE write-capable
planning operations. If base instructions would immediately run setup scripts or
make unsupported architecture decisions, follow this interactive gate first.

### Mode / read-only preflight

- Default to interactive. `--auto` is allowed only when explicitly included by the
  user; in that mode follow normal Spec Kit with disclosed assumptions, but **stop
  for unresolved critical architecture, security, data migration or compatibility
  decisions** instead of silently choosing.
- Interactive mode: until final plan-generation approval, **read only**. Inspect the
  approved `spec.md`, constitution, existing repository conventions, dependencies,
  interfaces, tests, deployments and known constraints. Do not run `setup-plan`
  or another script that writes files, create design artifacts, modify agent
  context, run write-capable hooks, or change any source file yet.
- If the spec lacks essential product semantics, do not guess or cross the boundary
  into product design: recommend `speckit.clarify` and identify the precise blocker.
- If a mandatory extension hook or constitution constraint blocks planning, surface
  it. Do not silently bypass it in order to ask fewer questions.

### Discover technical constraints

- Reuse explicitly selected tech stack and project architecture; do not re-ask.
- Identify only material technical decisions: integration boundaries, data/storage,
  API/contracts, error handling/reliability, security/access, rollout/migration,
  observability and testing, as actually relevant to this feature.
- Ground proposals in **actual repository observations** and distinguish confirmed
  facts, constraints, suggested choices, and open questions.
- Ask **exactly one question per reply** and wait. Follow-ups must respond to what
  the user just said; avoid predetermined questionnaires.

### Research & Propose (approve decisions one by one)

- For each meaningful unresolved choice, propose 2–3 viable options if alternatives
  exist. Rank/recommend briefly, with one key trade-off each and evidence from the
  codebase. Do not invent unnecessary alternatives or layers of abstraction.
- Present ONE design decision or coherent topic, request acceptance/amendment, then
  move on. Treat accepted choices as frozen unless new evidence creates a conflict.
- Ask only to the depth the change warrants; do not force the user through boilerplate
  sections already determined by existing code or the constitution.
- Summarize any remaining risks, unknowns and testing/rollout choices.

### Confirm & Generate

- Show a concise architecture decision summary: chosen approach, integration points,
  significant trade-offs, testing/rollback and any outstanding blockers.
- Ask one explicit final question: "Generate the standard Spec Kit technical plan now?"
  STOP. Section approvals are **not** final file-write approval.
- If approved, resume the **entire normal base planning flow**: required extension
  hooks, setup script, standard plan template, research/design artifacts as needed,
  constitution gates, agent-context updates and final handoffs.
- Only document technical decisions supported by code or user confirmation. Do not
  silently substitute the base command's defaults for user-rejected choices.
- If existing plan/design files will be overwritten, explicitly identify this and
  request approval to replace them before writing.
- Do not trigger `speckit.tasks` or `implement` automatically.

### Communication

Short, conversational and technical: a brief finding/recommendation and ONE question.
No large unrequested architecture report in chat. Use normal comprehensive Spec Kit
outputs on disk after approval.

---

## Decision Handoff — v0.6.0

- Use native active-feature resolution; never guess paths. Read relevant artifacts
  and pending sections before asking. Classify decisions in memory: approved,
  open, conflicting, later-stage or out-of-scope. Track source references.
- Reuse approved decisions, including semantically equivalent wording. Do not
  treat suggestions or defaults as approval. Reopen only missing details,
  material contradictions or new risks; explain what changed.
- Keep discovery read-only, including scripts/hooks. Preserve existing gates
  and `--auto` limits. Require no additional handoff approval for unchanged
  decisions; preview transfers in the existing final write summary.
- Apply forward-only adoption: read historical artifacts, but do not migrate
  old decisions. Add no registry, runtime, command or core template/script change.
  Never auto-invoke another stage. Reading a source grants no write permission.
- Re-read saved output; verify meaning, constraints and qualifiers. Account for
  every new approved decision. Report persisted, pending or unpersisted status;
  never claim complete persistence when missing or lose the only durable copy.

### Transfer — approved Option A

1. Retain resolved active-feature identity and source content. Select only
   approved entries targeting `speckit.plan` and native planning outputs.
   Reject ambiguous entries or duplicate IDs as cleanup candidates.
2. Preview destinations and exact cleanup IDs in existing final plan approval.
   Require that approval to cover cleanup; do not reapprove unchanged decisions.
   Rejection means no writes. Recheck feature/source/target before writing;
   stop affected work on material changes and explain the discrepancy.
3. Save the full decision canonically in native planning output, normally
   `research.md` or appropriate `plan.md`. Map source IDs to destination sections
   in memory. Preserve qualifiers; run the standard workflow and hooks.
4. RE-READ DESTINATION BEFORE SOURCE DELETION. Verify complete meaning, not
   similar topics. On write/verification failure, keep the source and report
   incomplete transfer. Only individually verified entries qualify for cleanup.
5. Immediately before cleanup, re-resolve the feature and re-read `spec.md`.
   Abort deletion if the feature switched, entries changed/disappeared, IDs
   became ambiguous or source changed materially. Explain the conflict; ask
   only about changed matters when necessary.
6. Match by stable ID AND decision content. Remove only verified, approved,
   plan-targeted entries from active `spec.md`. Preserve all other entries,
   requirements, constraints, Clarifications and metadata byte-for-byte.
   Remove the heading only if no pending content remains. Edit no other source.
7. Re-read source AND destination. Verify decisions remain at the destination,
   only selected entries disappeared and unrelated content is intact. On failure,
   keep verified output and original pending entries; report incomplete cleanup.
   Reinspect interrupted/uncertain writes; never assume success.
8. Retry idempotently: verify existing destination decisions, then attempt only
   eligible cleanup. Do not duplicate/overwrite decisions. Preserve the source
   whenever a precondition is uncertain.

### New decisions

- At final approved writing, save current decisions canonically. Put genuinely
  later-stage decisions in one `## Pending Handoffs` section of `plan.md` with
  stable feature ID, approved meaning/provenance and native command/artifact
  target. Check existing IDs; never recycle an unfinished ID. Verify persistence.
- Keep pending entries out of tasks/checklists. Allow later stages to read
  `plan.md`; grant no later-stage cross-artifact cleanup permission. Retain entries
  and report pending cleanup. Do not extend the active-spec-to-plan exception.
