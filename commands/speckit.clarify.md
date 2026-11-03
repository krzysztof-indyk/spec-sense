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
