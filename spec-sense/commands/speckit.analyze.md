{CORE_TEMPLATE}

---

## SDDW interactive policy — `speckit.analyze` (material issues, one by one)

This is a **conversation-layer extension** to the standard Spec Kit
cross-artifact analysis. Preserve all original checks, prerequisites,
severity heuristics, traceability, metrics, constitution authority and
standard report contents. `speckit.analyze` remains **strictly read-only**:
no edits to `spec.md`, `plan.md`, `tasks.md`, constitution, application
source, or any other file, including notes, reports or decision ledgers.

### 1. Complete the baseline analysis first

- Inspect the current `spec.md`, `plan.md`, `tasks.md`, ratified constitution
  and relevant supporting context through the normal core read-only path.
  Apply the full standard detection passes, coverage calculation and
  finding-severity rules. Keep stable finding IDs and precise file/section
  references (line numbers when known). Do not shrink the actual analysis
  to only issues expected to need conversation.
- Read `.specify/extensions.yml` and respect hook reporting. Execute only
  hooks and prerequisite operations **known to be read-only**. If a mandatory
  hook may write or its side effects are unknown, explain the conflict and
  stop or request an explicitly separate, user-controlled hook execution;
  never silently run it as part of a supposedly read-only analysis, never
  claim it executed, and never fabricate a complete result while blocked.
- Classify findings into (a) material decisions — CRITICAL or HIGH, plus
  MEDIUM findings whose resolution materially changes scope, safety,
  architecture, or acceptance behavior — and (b) minor/unambiguous findings.
  Do not use severity alone to hide important decisions. Constitution MUST
  violations remain CRITICAL and are not optionally waivable in this command.
- If no material decision is outstanding, deliver the normal complete report
  directly without forcing an interaction. Include lower-severity issues
  in that report, with recommendations and coverage statistics.

### 2. Review material decisions interactively

1. Present a short triage overview (number of material findings by severity,
   and number of minor ones) so the user knows the scope. If an issue is a
   deterministic noncompliance with ratified rules, identify that fact.
2. Present **one material finding per reply**, prioritized CRITICAL then HIGH
   then consequential MEDIUM. Show the affected artifact references, conflict
   or ambiguity and evidence, impact, and 1 recommended path. Where multiple
   viable paths exist, give 2–3 concise options with trade-offs.
3. End with **one focused decision question**, then STOP. User may confirm
   a remediation direction, correct the analysis, defer the issue, or
   explicitly accept a permissible risk. Never treat silence as acceptance.
   Ask one adaptive follow-up at a time when necessary.
4. An explicit "risk accepted" is a record of the user's review **for this
   conversational report only**; it is not a waiver of constitution MUST
   principles or an alteration of the feature artifacts. If the user
   challenges an evidence-backed finding, reconsider it and explain any
   revised classification with source references.
5. Keep decisions **in the conversation**. No local decision log, markdown
   edit, marker update, remediation execution or silent calls to editing
   commands. Do not repeat already settled questions unless source facts
   changed materially. `--auto` does not skip material decision review.

### 3. Finish with the complete report (still read-only)

- After review, produce the **full standard Spec Kit analysis report**:
  finding table, coverage mapping, constitution alignment, unmapped tasks,
  metrics, concise next actions. Include minor issues even if they received
  no interactive review. Label material findings as `remediation agreed`,
  `risk accepted`, `deferred`, `disputed` or `unresolved` as applicable.
  Agreement does not mean a correction was performed.
- Recommend the appropriate **separate command** (`speckit.clarify`,
  `speckit.specify`, `speckit.plan`, or `speckit.tasks`) for corrections.
  Explicit authorization for those workflows must be obtained there.
  This command must never invoke them or change files itself.
- If the user stops the review early, provide a partial-decision summary,
  retain unreviewed material findings as unresolved, and keep read-only.

### Communication

Avoid huge unprioritized dumps before the interactive review; show the
high-signal finding and **one question per reply**. The final report remains
complete (subject to the base command's finding limit), not truncated to
only the questions asked.

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

### Decision Handoff — `analyze` responsibilities

- During the native read-only scan, inspect canonical approved decisions and
  any `## Pending Handoffs` in relevant active-feature artifacts. Do not
  classify a resolved approved decision as an unanswered question solely
  because it is stored in a temporary section.
- Flag genuine conflicts, missing target coverage, or stale/ambiguous handoffs
  with evidence. When asking about a material issue, cite the prior decision
  and the newly conflicting fact instead of repeating the old question.
- This command remains **strictly read-only**: no handoff entries, reports,
  transfer marks, generated ledger or cleanup may be written. If a decision
  arises during analysis, label it **conversation-only / not persisted**, and
  recommend the corresponding standard writable command. Never promise that
  subsequent stages will see it unless it is persisted there.
