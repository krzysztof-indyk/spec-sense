{CORE_TEMPLATE}

---

## SDDW interactive policy — `speckit.specify` (overrides interaction only)

This policy is an **intentional refinement of the instructions above**. Treat it as the
controlling rule where the original command encourages inferring missing requirements,
running scripts immediately, or writing draft artifacts before explicit approval.
Preserve the original Spec Kit's scripts, extension hooks, naming, branch creation,
feature metadata, constitution checks, validation, templates, and final outputs.

### Mode

- The default is **interactive**, with no silent assumptions about product behavior.
- Use `--auto` only if the user explicitly includes that flag in the command invocation.
  It permits autonomous decisions **only** for noncritical, well-supported details;
  warn about assumptions. For a vague request (roughly <20 words), revert to interactive.
  Treat `--auto` as an interaction flag, not a feature requirement or a parameter to
  feed to feature-creation scripts.
- A user's explicit request to skip a specific question is not permission to invent
  a product requirement. Record it as deferred or open where the core format permits.

### Hard gate: do not mutate the project during discovery (interactive)

Before the user's **final approval**, ONLY read the repository and talk with the user.
Do not create a branch, change tracked files, create feature metadata, run creation/
setup commands, invoke write-capable hooks, or generate `spec.md` or a checklist.
Read-only inspection of existing files and conventions is allowed. Run the original
`before_specify` hook checks and all other standard creation steps **after** approval,
exactly as required by the core instructions. If a prerequisite needs a write to
inspect, explain that and obtain consent first. Do not claim a hook ran if it did not.

### Phase 1 — Discover (one question per reply)

- Start with the problem and desired outcome, not a solution or technology.
- Learn the actual actor/user, current painful behavior, expected observable success,
  must-have scenarios, excluded scope and meaningful constraints.
- Ask **exactly one** focused question per message, then STOP and wait for an answer.
  Adapt each follow-up to the answer; do not mechanically walk a questionnaire.
- If a reply is vague (e.g., "fast", "simple", "users"), gently probe for a concrete
  example, metric or decision. Do not ask again about information already provided.
- For genuine choices, offer 2–3 concrete options, with a short recommendation and
  trade-off if grounded in the repository or context. Otherwise ask an open question.
- In Copilot, use available interactive question UI if supported; otherwise use chat.
  Do not assume Claude Code's `AskUserQuestion` API exists.
- Do not reveal or paste a full specification template in the conversation.

### Phase 2 — Research & Propose

- Inspect the relevant existing code/docs and distinguish **observed facts**, **user-
  confirmed requirements**, and **proposals**. Never misrepresent an idea as a fact.
- Validate the intended behavior and scope in conversational, manageable sections:
  purpose; key user journeys; functional requirements and non-goals; acceptance
  behavior and relevant failure cases; meaningful constraints.
- Present **one unresolved decision/section at a time** and ask for acceptance or
  adjustment before continuing. Do not fabricate alternatives for straightforward
  choices and do not ask the user to approve boilerplate.
- Keep this phase technology-agnostic when possible: detailed architecture belongs
  in `speckit.plan`. Raise feasibility conflicts explicitly instead of guessing.

### Phase 3 — Confirm & Generate

- Summarize agreed goal, core behavior, boundaries, success/acceptance checks and any
  remaining open items in **at most 8 concise bullets**.
- Ask one explicit final question: "Generate the standard Spec Kit specification now?"
  STOP and wait for approval. A partial section approval is not final approval.
- On a 'no' or revision, continue discussion; do not write anything.
- On a 'yes', **resume the original complete `speckit.specify` execution flow**:
  prerequisites/hooks, branch/metadata creation, standard `spec-template.md`,
  requirement coverage, relevant checks and any standard output and handoffs.
  Use only user-confirmed requirements as product decisions; unresolved items must
  be explicitly identified instead of filled by informed defaults.
- Preserve the **standard artifact depth and formatting**. Concision applies to
  conversation, NOT to truncating the standard spec template.

### Communication

Keep messages short: one relevant context sentence or brief trade-off, followed by
one question. Avoid status narration, gratuitous matrices and multi-question dumps.

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

### Decision Handoff — `specify` responsibilities

- In discovery, if the user explicitly **approves** a technical choice or a
  later-stage task/deployment decision, preserve it as an agreed input; do not
  push the user to reapprove it in `plan` merely because it concerns HOW.
- At the final approved normal `spec.md` write, include a concise pending
  entry for each genuinely later-stage decision (usually targeted at
  `speckit.plan / research.md` or `plan.md`), while keeping business
  requirements and durable constraints in their canonical spec sections.
  Never erase or convert a product requirement into a temporary handoff.
- Re-read the generated spec; check that all approved decisions are either in
  canonical sections or `## Pending Handoffs` with an unambiguous target.
  Do not claim completion otherwise. Respect native quality checks; if a
  checker objects to the temporary technical content, explain the conflict
  rather than disabling validation or silently dropping an approved choice.
