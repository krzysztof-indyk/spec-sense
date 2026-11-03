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

### Capture

- Keep decisions in chat until final write approval. Save current-stage decisions
  canonically. Use exactly one `## Pending Handoffs` section in active `spec.md`
  for genuinely later-stage decisions; preserve existing entries and requirements.
- Format: `- **DH-001 → speckit.plan / research.md** — Decision: Respect Retry-After for HTTP 429. Approved during speckit.specify.`
  Retain full meaning, qualifiers, approval provenance and a native destination.
  Check existing feature IDs; keep IDs stable and never reuse an unfinished ID.
  Resolve ambiguous identity/targets before writing; never invent destinations.
- Preview exact entries in final approval. Rejection means no writes. After the
  authorized native write, verify every new approved decision in canonical or
  pending text. Report incomplete persistence if missing; preserve unrelated text.
- Keep product WHAT/WHY separate from temporary technical entries. Run native
  checks; surface conflicts with the spec checker; do not bypass validation.

- Read and preserve later-stage entries; do not repeat approved questions.
  Include new pending decisions in final approval even on the no-change path.
  Do not clean sources merely because another artifact mentions the topic.
