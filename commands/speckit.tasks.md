{CORE_TEMPLATE}

---

## SDDW interactive policy — `speckit.tasks` (overrides interaction and write timing)

This policy **extends the standard Spec Kit task-generation command**. Preserve its
feature setup, input documents, hook handling, dependency ordering, checklist syntax,
parallel flags, user-story labels, phases, independent test criteria, validation,
and completion report. Use the **original standard `tasks.md` template and format**.
Do not generate separate task files or change task structure to SDDW's format.

### Read-only discovery gate (interactive default)

- Until all groups are approved **and the user explicitly authorizes generation**,
  perform read-only inspection and conversational drafting only. Do not run
  `setup-tasks` or other write-capable scripts, write/overwrite `tasks.md`, alter
  project files, run write-capable extension hooks, or begin implementation.
- Read the approved `spec.md`, `plan.md`, applicable constitution, and available
  research, contracts, data model, quickstart and repository conventions. Check
  hook declarations, and surface prerequisite/mandatory hook blockers. Execute
  mandatory pre- and post-hooks at their normal applicable stage **after** final
  approval, never silently omit them or claim they ran during discovery.
- If essential user-story behavior or implementation design is missing, identify
  the specific blocker and recommend `speckit.clarify` or `speckit.plan`. Do not
  silently fill missing business or architectural decisions with assumptions.
- `--auto` does **not** bypass the chosen approval model: every applicable
  phase/user-story group and the final file write still require explicit
  user approval. When explicitly supplied, `--auto` may streamline read-only
  research or obvious task derivation, but never silently settle critical
  scope, security or architecture decisions. Do not pass it to setup scripts
  as a feature requirement.

### Discover task boundaries

1. Base the grouping on standard phases: **Setup → Foundational → each user story
   in specification priority order → Polish / cross-cutting**. Do not regroup by
   technical component. Skip empty/inapplicable phase content only when the
   standard task-generation rules permit it.
2. Identify real work and dependencies from approved artifacts. Do not invent
   extra features, unrequested test suites or new architectural components.
   Respect the core rule: test tasks are included only when requested by the spec
   or TDD was explicitly requested.
3. Ask **exactly one focused question per reply**, then stop and await the answer.
   Use a relevant follow-up for an ambiguous answer; never ask for information
   already confirmed in artifacts or conversation. Offer 2–3 options with concise
   trade-offs only when a material choice actually exists.

### Phase / user-story approval loop

1. Propose **one complete phase or user-story group at a time**, in the standard
   order. Show a compact preview of its actionable tasks (including file paths,
   important dependencies, story goal, independent test condition and tests if
   applicable). Use provisional task IDs if useful; final numbering is assigned
   on generation, after all groups are approved.
2. End each preview with **one approval question**: approve this group, change it,
   or discuss a specific concern? STOP. Do not advance until it is approved.
3. If the user requests changes, revise **that group** and present it for approval
   again. Keep accepted groups in session as confirmed; do not reopen them without
   a new dependency, contradiction, or a user-requested change. If a later change
   materially affects an accepted group, show the delta and reapprove only affected
   group(s).
4. Avoid unnecessary per-task approvals. Phase / user-story groups are the unit
   of approval. If one group is large, preview it in manageable chunks, but ask
   for **one decision on the whole group** once the user can inspect it.
5. For the final Polish / cross-cutting phase, avoid padding with speculative or
   duplicate tasks; include only work traceable to the approved design and spec.

### Final confirm & generate

- After **every applicable group** is approved, give a short final summary:
  approved phases/stories, rough task counts, execution dependencies and risks.
  Ask ONE explicit final question: **"Generate the standard Spec Kit tasks.md now?"**
  STOP. Group approvals are not permission to write files.
- If a prior `tasks.md` exists, show that it will be replaced or updated and seek
  explicit informed approval (including this in the final approval question).
- On approval, resume the **full normal Spec Kit command**: run required hooks,
  setup script, resolve the standard template, generate **one** standard `tasks.md`,
  assign globally sequential T IDs, preserve the required `[P]` and `[US#]`
  markers, paths and dependency/parallel/MVP sections, validate, then run
  post-hooks and report completion. Render **only the approved task groups** and
  mechanically necessary tasks the base format mandates; do not introduce new
  consequential decisions during generation. If a new blocker is discovered,
  pause and ask instead of silently revising an approved group.
- On rejection, resume conversation without writing. Do not auto-run analyze or
  implement; only offer the standard handoffs.

### Communication

Prefer one short contextual statement plus **one question**. Use the full standard
file format on disk; conversational previews should be concise, not vague.

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

### Decision Handoff — `tasks` responsibilities

- Prior to Discovery/group approvals, inspect canonical spec/plan/research
  decisions and any `## Pending Handoffs` in them. Do not re-ask a design or
  requirement choice already approved in `specify`, `clarify` or `plan`.
- Carry decisions targeted at `speckit.tasks` into the normal approved
  phase/user-story work breakdown and standard `tasks.md` at its **existing
  final write gate**. Verify resulting tasks reflect approved meaning; avoid
  reintroducing an already satisfied task or inventing new architecture.
- Native `tasks` cannot delete pending entries in `spec.md`/`plan.md`.
  Preserve such sources and disclose **cleanup pending** where applicable;
  do not claim verified removal, bypass the source permissions, or add a
  second approval just to reuse the decision.
