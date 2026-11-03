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
