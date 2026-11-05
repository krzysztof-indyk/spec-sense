{CORE_TEMPLATE}

---

## SDDW interactive policy — `speckit.constitution` (principle-by-principle approval)

This policy **extends the standard Spec Kit constitution command**. Preserve its
constitution template resolution, governance model, version/date semantics,
Sync Impact Report, validation, hooks, final output and **scope guard**. Only
`.specify/memory/constitution.md` may be written by this command. Do not change
standard templates or feature artifacts as a side effect of constitution updates.

### Default: discover before writing

- Work interactively, starting with read-only inspection of README, repository
  structure, relevant existing documents and the current constitution. Distinguish
  **observed conventions**, **confirmed rules**, **suggested principles** and
  **open issues**. Existing code conventions are evidence, not automatically
  binding governance rules.
- Before final approval, do not write constitution or other files, invoke
  write-capable resolver/setup scripts, or run write-capable hooks. Inspect hook
  declarations and surface mandatory blockers; run required pre/post hooks at
  their normal stage when generation is authorized. Never claim skipped hooks ran.
- If no constitution exists, propose only the principles necessary to govern this
  project, not a speculative generic catalogue. Keep the **standard document
  structure** and governance section, without assuming an arbitrary number of
  principles.
- For an existing constitution, preserve all unmodified principles and prior
  ratification history. Never silently remove, weaken, rename, reorder or modify
  a principle; even a removal requires its own approval.
- Do not let `--auto`, pasted lists of principles, or a broad instruction such
  as "update everything" bypass **per-principle approval**. A proposed principle
  supplied verbatim by the user still needs explicit confirmation to ratify it.

### Discover and propose — one principle at a time

1. First understand the project's purpose, risk profile, constraints and quality
   expectations. Ask **exactly one focused question per reply**, use adaptive
   follow-ups, and do not repeat already confirmed answers.
2. Offer **one concrete, testable principle (or one proposed modification to an
   existing principle)** at a time. Include: a short name; enforceable normative
   wording; brief rationale grounded in the project; and the main consequence or
   trade-off. For amendments, show **old → proposed** wording and identify whether
   the change adds, modifies, renames or removes a principle.
3. Ask for explicit **approve / revise / reject** of **that single principle**.
   STOP and wait. Accept no other principle implicitly. If rejected, exclude it;
   if revised, present revised wording and seek its approval again.
4. Continue until all proposed additions, modifications and removals are decided.
   Do not invent more principles to fill a template. Confirm meaningful governance
   changes (amendment process, review policy) separately; apply ordinary standard
   placeholder/date handling only where supported or transparently deferred.
5. Retain the per-principle decision ledger **in conversation/context only**; do
   not write a temporary file. No change is effective until final file approval.

### Impact assessment and final consent

- Inspect existing `spec.md`, `plan.md`, `tasks.md`, and related artifacts **only
  if present and relevant**. For each approved change, identify concrete potential
  conflicts or necessary reviews, with paths/sections and why; distinguish verified
  conflicts from possible downstream impact. Do not manufacture problems if none
  are found.
- Summarize the exact proposed constitution changes, any rejections/deferrals,
  expected semantic version bump (MAJOR/MINOR/PATCH with rationale), and affected
  artifacts. If changing an existing file, flag the overwrite explicitly.
- Ask ONE final question: **"Write the approved constitution changes now?"**
  STOP. Principle approvals are not final write approval. On rejection, make no
  changes and continue discovery/revision if asked.
- On approval, run the original complete constitution workflow: required hooks,
  canonical constitution-template resolution, normal version/date handling,
  drafting, validation, Sync Impact Report comment, write **only** to
  `.specify/memory/constitution.md`, and post-hooks. Only incorporate individually
  approved principles and approved governance amendments. Do not auto-ratify
  unapproved suggestions discovered in the source template or repository.

### Controlled downstream changes (strict scope guard)

- Report the impact of the confirmed constitution amendment on existing
  `spec.md`, `plan.md`, `tasks.md` and other relevant artifacts, including suggested
  targeted updates. The **analysis and proposals** are part of this command;
  **editing those artifacts is not**.
- **Never modify downstream files in the constitution command**, even if a user
  authorizes the proposed changes. The standard core command explicitly prohibits
  writing files other than the constitution. Instead, ask whether to proceed with
  a **separate, explicit follow-up workflow** for the affected artifacts. Require
  the user's approval before starting that workflow and again before actual writes
  according to the relevant command's approval policy. Offer `speckit.clarify`,
  `speckit.plan` and/or `speckit.tasks` as appropriate; do not auto-invoke them.
- If a follow-up is declined, list it as an outstanding recommendation, not a
  performed update. If no relevant artifacts or conflicts exist, say so briefly.
- Feature work, code changes or refactors remain outside constitution's scope;
  retain the core's deferred-intent / Next Actions behavior.

### Communication

Be concise. One principle or one decision per turn, with **one question**. Do not
present a multi-question constitution checklist. Preserve the full standard
constitution file and governance conventions after approval.

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
  In native Copilot question UI, send only this decision item, not a second
  optional "Zmiana (jeśli potrzebna)" / comment / free-text prompt in another
  tab. If the chosen option requires details, ask about those details afterward.
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

### Decision Handoff — `constitution` responsibilities

- Read relevant approved project governance and applicable feature context
  before asking to ratify a principle; do not reopen settled choices without
  a material conflict. A feature-specific technical choice is **not** a
  constitutional principle and must never be moved into governance merely
  because it appears in a Pending Handoffs section.
- Only `.specify/memory/constitution.md` is writable, under the existing
  individual-principle and final approval gates. Never add feature-specific
  pending entries or modify feature artifacts from `constitution`. If a newly
  approved feature-specific detail needs durable recording, explain that an
  appropriate write-capable feature command is required; do not claim the
  decision was persisted here.
