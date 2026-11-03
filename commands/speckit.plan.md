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
