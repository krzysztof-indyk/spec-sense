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
