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

## SpecSense v0.6.0 — Decision Handoff (shared safety contract)

This extends the **existing** Spec Kit command and the interactive policy above;
it is not a new command, storage system or replacement for native scripts,
templates, hooks, approval gates or artifact formats.

- **Read before asking:** use standard Spec Kit active-feature resolution and
  permitted read-only prerequisites to inspect relevant `spec.md` (including
  Clarifications), `research.md`, `plan.md`, `tasks.md`, constitution and any
  existing `## Pending Handoffs`. An absent section is normal for older
  features; **do not backfill** historical decisions. Use only current-feature
  artifacts, never a guessed path or remembered chat as the sole authority.
- **Ask only what is still open:** an explicit approved decision, even if
  phrased differently, is already answered. Do not reconfirm it merely because
  a new command or discovery phase began. Only ask about a missing material
  detail, genuine contradiction or newly discovered risk; show the earlier
  decision and the specific new information first. One focused question if
  clarification is necessary; no mandatory question if nothing is missing.
- **Approved versus proposed:** don't promote exploratory options, implicit
  defaults, unaccepted recommendations or conversation-only risk discussions
  into binding decisions. An approved requirement stays in its native section;
  store only an approved *future-stage* decision temporarily, and only in a
  document this command can normally write under its existing final approval.
- **Temporary format:** when needed, use a single `## Pending Handoffs` section
  in the current native artifact. One stable feature-unique ID per entry, e.g.
  `- **DH-001 → speckit.plan / research.md** — Decision: Respect Retry-After on
  HTTP 429, with an explicit cap. Approved during speckit.specify.` Preserve
  the exact decision, qualifiers and target existing Spec Kit artifact. Do not
  create a new decision file or change any core template. Do not add an empty
  section. Avoid duplicate entries if the target already contains the decision.
- **Persistence gate:** collect approvals in chat during Discovery. At the
  command's existing **final approved write** only, persist approved
  current-stage decisions canonically and eligible future-stage decisions as
  pending entries; then re-read and verify coverage before reporting success.
  Never run write-capable tools early. Preview incoming/outgoing handoffs in
  the existing approval summary; do not demand another approval for a decision
  already accepted. Existing `--auto` does not cancel safety/write gates.
- **Transfer rule:** consume incoming decisions when the target command runs,
  verify the *full meaning and qualifiers* in the native target after its
  authorized write, and only then clean a source entry **if that command is
  specifically allowed to edit that source**. On incomplete writes, missing
  qualifiers, changed source or uncertain feature identity, preserve the
  pending entry and report the incomplete handoff. Never delete permanent
  product requirements or constraints. Do not silently retry or duplicate.
- **Hard boundaries:** `speckit.analyze` is read-only; `speckit.converge`
  remains append-only; `speckit.constitution` changes only its constitution;
  custom checklist files remain append-only. The **only** approved bounded
  cross-artifact cleanup exception is in `speckit.plan`, defined below. Other
  commands may reuse pending decisions but cannot delete earlier-stage entries
  by inventing new permissions. If cleanup is outside the command's scope,
  preserve the source and identify the outstanding cleanup without claiming
  a fully completed transfer.

### Decision Handoff — `plan` responsibilities and approved bounded cleanup

1. In read-only preflight, resolve the **active feature** via standard Spec Kit
   mechanisms. Read `spec.md` including approved `## Pending Handoffs`, and
   existing `research.md`/`plan.md` if present. Treat entries targeting
   `speckit.plan` as inputs to design, not unanswered questions. Include a
   concise list of decisions being carried into the **existing** final plan
   approval preview. Do not change `spec.md` during preflight.
2. At the **approved native planning write**, record each applicable decision
   with all qualifiers in the standard `research.md` (or `plan.md` if
   canonically appropriate). Keep normal design reasoning and constitution
   checks; if a real conflict appears, cite it and ask only about that delta.
3. **Verify before cleanup:** re-read the destination, ensure the exact meaning,
   constraints and caveats of each entry are present; topic overlap alone is
   insufficient. If absent or ambiguous, preserve the source and report failure.
   On retry, reuse and verify existing matching target content; never duplicate
   it. Re-read active feature identity and original `spec.md` immediately before
   cleanup; if either changed materially, abort deletion and report the conflict.
4. **Approved narrowly scoped exception (Option A):** as part of the already
   approved plan write, and **only after successful destination verification**,
   remove exactly the verified `speckit.plan`-targeted `DH-...` entries from the
   active feature's `spec.md` `## Pending Handoffs`, matched by both stable ID
   and unchanged original content. Preserve every other entry, canonical
   requirement, constraint, Clarifications section and all unrelated text.
   Remove the temporary heading only when empty. Never edit another feature's
   spec or a non-pending paragraph; never delete an entry targeting `tasks`.
5. Re-read both files after cleanup. If removal fails, keep the valid target
   and the source entry, report **partial transfer / cleanup pending**, and
   do not claim full completion. On retry, verify target and try only the
   matching cleanup. No separate approval for unchanged approved decisions;
   this exception is included in the normal plan write consent. Do not grant
   this cleanup authority to any other command.
