{CORE_TEMPLATE}

---

## SDDW interactive policy — `speckit.converge` (group-by-group approval)

This policy adds an **approval gate before the core command's append step**;
all other standard Spec Kit convergence behavior still applies. Preserve its
prerequisites (tasks generation AND implementation already run), evidence and
severity classification, intent inventory, hook contract, task syntax,
no-code-changes rule, and **append-only** invariant. The only permitted
artifact modification is appending one new `## Phase N: Convergence` section
to the existing `tasks.md`. Never edit or reorder earlier tasks, `spec.md`,
`plan.md`, or application code.

### 1. Assess without writing

- Default to interactive. Read the required existing artifacts and in-scope
  code before proposing action. Treat `spec.md`, `plan.md`, and `tasks.md` as
  the sources of feature intent and the ratified constitution as binding.
  Do not derive new product requirements from preference or speculation.
- Before all finding groups AND the final append are approved, do **not**
  modify `tasks.md` or other files, run a write-capable setup script, execute
  a write-capable extension hook, or implement fixes. Read-only checks and
  read-only prerequisites are permitted. Inspect `.specify/extensions.yml`;
  if a mandatory hook might write, explain its effects and obtain separate
  authorization before running it, or stop with an explicit blocker. Never
  silently ignore mandatory hooks or claim they were run.
- Follow the standard convergence inventory: assess actual current behavior
  (not checkbox completion claims or Git history), map every finding to a
  concrete artifact obligation, code evidence, gap type, and severity.
  Distinguish `missing`, `partial`, `contradicts`, and `unrequested`.
- Do not issue an action item without specific remaining, buildable work.
  A low-confidence suspicion is a question or an investigation finding,
  not proof that implementation is missing. Consolidate duplicate findings.
- If genuinely **no gaps** remain, report the normal `Converged` outcome,
  leave `tasks.md` byte-for-byte unchanged, and do not ask for a needless
  approval or append an empty phase.

### 2. Present and approve one findings group at a time

1. Show a **compact overall severity summary** (counts by severity/type and
   requirements checked), then identify a useful grouping based on severity
   and/or related requirements. Avoid a category with no real findings.
2. Present exactly **one group** per conversational turn. For each finding,
   include its stable ID, severity, type, requirement/acceptance/constitution
   source reference, supporting code location/evidence, and the *proposed*
   append-only remediation task. Keep proposals traceable and practical.
   For multiple similar findings, use concise bullets rather than a wall
   of repeated prose.
3. End with **one question**: approve this group for append, revise its
   tasks, reject a finding with explanation, or defer the group? STOP and
   await the user's response; do not present another group meanwhile.
4. Ask adaptive follow-ups **one at a time** only for material ambiguity.
   Offer 2–3 alternatives and brief trade-offs where a real decision exists.
   Do not invent an architecture choice or change a requirement to close a
   gap. If fixing it requires a product/design decision, defer and recommend
   the appropriate `speckit.clarify`/`speckit.plan` step.
5. Track groups approved, rejected and deferred **in session, not in files**.
   A rejection does not prove the gap is absent: retain it as an unresolved
   or disputed finding in the report. Constitutional MUST violations cannot
   be waived via this command; explain that they remain blocking even if
   the user declines to append a proposed task.
6. Reopen an approved group only when new evidence materially changes it;
   show the exact delta for renewed approval, rather than restarting the
   review. `--auto` never bypasses group or final write approvals.

### 3. Final confirmation and append

- After every group is decided, show counts of approved actionable findings,
  rejected/deferred issues and unresolved critical gaps. Provide a concise
  preview of the **exact new tasks**, with expected next phase and task IDs.
  Say clearly that existing task content will not be rewritten.
- Ask one explicit final question: **"Append only the approved convergence
  tasks to the existing `tasks.md` now?"** STOP. Group approvals are NOT
  write permission. If there are no approved actionable tasks, do not write;
  report unresolved findings and exit.
- On rejection: no writes. On approval: ensure the artifacts/code are still
  current. If the basis changed, refresh the affected findings and seek
  renewed approval of changed groups. Then execute the **core command's
  normal permitted append path**, including required hooks at their
  authorized stage, sequential unique `T###` IDs, next phase number,
  source refs, gap-type markers, CRITICAL-first ordering, and validation.
- Never append a task already satisfied by the code or already represented by
  an existing open convergence task. Never silently include a rejected,
  deferred or newly discovered finding in the append.
- Report how many tasks were appended, what remains disputed/deferred, and
  the core handoff (`speckit.implement` then `speckit.converge` again).

### Communication

Use **one focused question per reply**, not a multi-question checklist.
Minimize chatter, not rigor. Preserve the full standard convergence format.

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

### Decision Handoff — `converge` responsibilities

- During read-only evidence gathering, read canonical decisions and any
  current-feature Pending Handoffs. An approved design decision can guide
  gap analysis but is not evidence that the code already implements it.
- Reuse agreed decisions when presenting remediation; do not ask for the same
  design choice again unless new implementation evidence shows a specific
  contradiction. The existing group and final append approvals still apply.
- Write only newly approved remediation tasks via the **native append-only**
  convergence phase of `tasks.md`; never create/update/erase `spec.md`,
  `research.md`, `plan.md`, or pending entries, and never treat append as source
  cleanup. When cleanup cannot be performed here, disclose it without claiming
  a completed handoff.
