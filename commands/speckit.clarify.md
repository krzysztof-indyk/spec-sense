{CORE_TEMPLATE}

---

## SDDW interactive policy — `speckit.clarify` (overrides question/write timing)

Keep all **standard Spec Kit** prerequisites, spec format, checklist consistency,
extension-hook semantics, validation, and final handoffs. Where the core command
says "up to five questions" or "write each answer immediately", this policy
intentionally takes precedence **in interactive mode**.

### Mode and read-only gate

- Interactive by default. Respect an explicit `--auto` for low-risk clarifications,
  but never silently redefine user-facing behavior, security, data retention,
  permissions, or other materially consequential requirements. When critical gaps
  remain, ask even if `--auto` was supplied.
- Before final approval, read the spec/repo and prepare a proposed change set
  **in conversation only**. Do not mutate `spec.md`, requirements checklists,
  feature metadata or code. Do not run write-capable hooks. Perform the base command's
  hook and integration operations at their proper stage after final approval.
  Do not pretend skipped hooks executed.

### Discover and clarify

1. Read the existing spec and supporting context using the normal Spec Kit methods.
   Reuse already confirmed answers; do not repeat the same questions.
2. Identify genuine specification ambiguity or contradictions. Prioritize by impact
   and uncertainty: product semantics, actors, boundaries, failures, permissions,
   success criteria, then less consequential details.
3. Ask **exactly one question per reply**, wait for the answer and adapt the next
   question. Probe vague answers; do not mechanically ask every category.
4. For a decision with useful alternatives, offer 2–3 options with short trade-offs
   and an evidence-based recommendation. Allow free-form answers.
5. Continue until important ambiguities are resolved, explicitly deferred by the
   user, or the user asks to stop. There is **no fixed five-question cap** in this
   interaction layer. Do not keep asking once sufficiently clear.
6. Distinguish confirmed answers from proposals and deferred/open points.
   If no material ambiguity exists, say so and leave files unchanged.

### Confirm and apply

- Show a **compact proposed change summary**: requirements or sections affected,
  exact intended meaning, and any deferred items. Ask one explicit question:
  "Apply these clarifications to the existing standard `spec.md`?" Stop and wait.
- On approval, perform the core command's normal prerequisites/hooks and **batch
  integration** of all approved clarifications, using its standard `## Clarifications`
  entries and the appropriate canonical sections. Preserve existing content and
  identifiers. Update built-in requirements checklist evaluation state if applicable;
  do not alter unrelated custom checklists or planning/implementation files.
- Treat already-answered questions as resolved: do **not** restart the core loop and
  re-ask them after approval. Execute the **write/validation/handoff parts** of the
  base process with the collected approved answers.
- On rejection, iterate in chat; do not write anything.

### Communication

Prefer one specific question, not a long report. No automatic broadening of scope,
no speculative requirements, and no wall of clarification tables.

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

### Decision Handoff — `clarify` responsibilities

- On entering the command, inspect `spec.md` **including `## Pending
  Handoffs`** before generating clarification questions. Pending decisions
  for `plan` or another later stage are already approved; preserve them, do
  not rediscover them, and do not mistake them for a missing product decision.
- Apply approved clarifications in the existing final **batch** write, keeping
  canonical `## Clarifications` and requirements. Add future-stage entries
  only if approved in this clarification session and truly relevant; use
  distinct stable IDs. Preserve unrelated pending entries verbatim.
- Do not clean `plan`-targeted entries just because you read them. If new
  evidence conflicts with an entry, show the old wording and new evidence,
  ask only for the changed decision and update it only after normal approval.
