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

## Decision Handoff — v0.6.0

- Use native active-feature resolution; never guess paths. Read relevant artifacts
  and pending sections before asking. Classify decisions in memory: approved,
  open, conflicting, later-stage or out-of-scope. Track source references.
- Reuse approved decisions, including semantically equivalent wording. Do not
  treat suggestions or defaults as approval. Reopen only missing details,
  material contradictions or new risks; explain what changed.
- Keep discovery read-only, including scripts/hooks. Preserve existing gates
  and `--auto` limits. Require no additional handoff approval for unchanged
  decisions; preview transfers in the existing final write summary.
- Apply forward-only adoption: read historical artifacts, but do not migrate
  old decisions. Add no registry, runtime, command or core template/script change.
  Never auto-invoke another stage. Reading a source grants no write permission.
- Re-read saved output; verify meaning, constraints and qualifiers. Account for
  every new approved decision. Report persisted, pending or unpersisted status;
  never claim complete persistence when missing or lose the only durable copy.

### Read-only boundary

- Report pending/conflicting decisions with source references; no file writes of any kind.
  Never add, transfer or erase entries. Preserve the full report and constitution authority.
- Label new decisions conversation-only and unpersisted. Do not promise later-chat
  recall. Recommend a separate writable command without invoking it.
