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
