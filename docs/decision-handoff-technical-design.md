# SpecSense v0.6.0 — Decision Handoff Technical Design

**Status:** Approved design; instruction-level implementation packaged in v0.6.0; live Copilot acceptance pending  
**Implementation:** Eight preset wrappers updated; core scripts/templates unchanged  
**Inputs:** `decision-handoff-requirements.md`, SpecSense v0.5.4, standard Spec Kit command definitions

## 1. Integration principle

Extend the existing eight command wrappers with a small, consistent **Decision Handoff contract**. Preserve `{CORE_TEMPLATE}` composition, the native `spec-template`, `plan-template`, `tasks-template`, feature selection via `.specify/feature.json`, standard setup scripts, and hooks. Do **not** create a feature-level decision registry, custom template, helper runtime, or additional command.

Rules apply to the *interactive prompt layer*. They cannot provide transactional guarantees if a model ignores instructions; safety-critical guarantees need explicit verification in tests.

## 2. Minimum entry format (proposed)

In a writable artifact, add this section only when there are approved decisions assigned to later stages:

```markdown
## Pending Handoffs

- **DH-001 → speckit.plan / research.md** — Decision: Respect `Retry-After` for HTTP 429. Approved during `speckit.specify`.
```

- IDs are stable within the current feature; do not recycle an ID within an unfinished transfer.
- The decision must be precise enough to carry forward without re-questioning the user; optional one-line rationale when needed.
- This is a temporary section in an existing file, **not a modification to the core template**.
- Keep ordinary requirements and technical constraints in their canonical sections. Do not copy them into `Pending Handoffs` solely to create a duplicate.
- Target can be a command and its existing standard artifact. Never invent a destination file.
- Remove an empty section after successful cleanup.

## 3. Shared lifecycle

### Preflight (read-only)

1. Use native Spec Kit active-feature resolution. Read relevant artifacts (e.g., `spec.md`, its Clarifications, `plan.md`, `research.md`, `tasks.md`, constitution) and all existing pending sections permitted by the current command.
2. Build an *in-memory* list of `approved / resolved / conflicting / pending-for-later` items; do not write a new register.
3. Before asking a question, check whether the exact decision is already approved, including semantically equivalent wording. Cite its current artifact/section internally during discovery.
4. For contradictions or changed constraints, show **what changed** before reopening the decision. Do not use discovery as a reason to re-confirm a decided issue.
5. If prerequisites/scripts/hooks may write, defer them until the command's ordinary final write gate; do not accidentally mutate during preflight.

### Interactive discovery

6. Keep the existing one-focused-question and approval behavior. Capture only *explicitly approved* decisions; distinguish suggestions, defaults and unresolved options.
7. Map decisions to a canonical current-stage destination if possible. Assign a future stage only when the canonical destination genuinely belongs later.
8. Do not add a new handoff-approval question; include a compact handoff preview in the existing final approval summary.

### Final approved write

9. Execute the native Spec Kit stage's authorized write process and hooks at its normal point.
10. Write approved current-stage decisions to standard sections. Place genuinely future-stage decisions into `## Pending Handoffs` of an eligible current artifact.
11. Re-read the output and verify that each new approved decision is present and semantically intact. Do not claim a complete handoff if missing.

### Target-stage transfer

12. Include incoming decisions in research/design/task generation without reasking the same questions.
13. After native output is saved, verify the target contains the exact substance of the transferred decisions, including any constraints and qualifiers.
14. Only after that, clean the corresponding temporary source entry **when the current command is authorized to do so**. For `speckit.plan`, the user has approved a bounded exception allowing removal of *verified, plan-targeted* `Pending Handoffs` entries from the active feature's `spec.md` as part of the already approved plan write (see §5). Other commands retain their native write boundaries; otherwise report pending cleanup and preserve the source.
15. For partial failures, preserve every unverified source item and do not silently mark success.

## 4. Command compatibility matrix

| Command | Read pending | Native writable artifact(s) | Proposed handoff role | Constraint |
| --- | --- | --- | --- | --- |
| `specify` | Existing feature context, when applicable | `spec.md` | Create approved future-stage entries; verify persistence at final approval | Keep product requirements WHAT/WHY; temporary technical entries are explicitly out-of-band |
| `clarify` | `spec.md` | Existing `spec.md` and canonical clarification content | Reuse resolved decisions; preserve/add entries for a later stage with final approval | No unapproved incremental writes |
| `plan` | `spec.md`, etc. | `plan.md`, `research.md`, related native planning outputs; **bounded cleanup of verified `plan`-targeted entries in active `spec.md`** | Import decisions targeted at plan; avoid repeated architecture questions | Explicit approved exception only; never modify permanent requirements, other pending entries, or other features |
| `tasks` | `spec.md`, plan/research | `tasks.md` | Derive tasks from existing approved decisions | Preserve core task IDs/phase/story structure |
| `constitution` | Existing constitution and applicable feature context | `.specify/memory/constitution.md` only | Read constraints and protect principles; avoid putting feature-specific handoffs in governance | Do not modify other files |
| `checklist` | Existing artifacts | Custom requirement checklist files (append restrictions) | Use approved decisions to avoid redundant quality questions | Cannot erase prior checklist entries for cleanup |
| `analyze` | Existing artifacts | **None** | Detect pending/conflicting items; recommend next writable command | Strictly read-only; no promise that a new conversational decision was persisted |
| `converge` | Existing artifacts | Append convergence phase to `tasks.md` only | Consume approved decisions as evidence and create approved remediation tasks | Append-only; no cleanup of other sections or files |

**Interpretation of “universal”:** universal *visibility and reuse*, with transfer/persistence only through write-capable native boundaries. This is the smallest safe interpretation of R2 + R7.

## 5. Approved decision — bounded `plan` source cleanup (Option A)

**Decision:** Option A was explicitly approved on 2026-11-03. This resolves the earlier Option A/Option B design gate; it **does not authorize implementation yet**.

The regular Spec Kit `plan` command primarily reads `spec.md` and generates planning artifacts (`plan.md`, `research.md`, etc.). SpecSense may extend its **approved final write** with one narrowly bounded cross-artifact cleanup operation: remove a `Pending Handoffs` entry from the **active feature's `spec.md`** after its meaning has been successfully written to and verified in the appropriate native planning artifact.

This is a **documented exception to the default write scope of `plan`**, not a change to Spec Kit core scripts, templates, commands, or resolution logic. It does not expand any read-only or append-only command's permissions; `analyze`, `converge`, and other restricted commands remain under their existing boundaries.

### 5.1 Preconditions (all required)

1. Resolve the active feature and its `spec.md` using the existing Spec Kit context, never a guessed path.
2. The source contains a uniquely identified, explicitly approved `Pending Handoffs` entry whose target is `speckit.plan` and an existing standard planning output. Entries for other targets are not eligible.
3. The user's **existing final plan approval** covers the planning output and the disclosed cleanup of matching verified pending entries. Do not ask for a second approval solely to transfer the same decision.
4. Write the intended decision to the canonical native destination (`research.md`, or `plan.md` when genuinely appropriate) using the standard plan workflow.
5. Re-read the destination and verify the decision's meaning, qualifiers, constraints, and target entry ID mapping. A similar topic or vague paraphrase is not sufficient.
6. Re-read `spec.md` immediately before cleanup. If the pending entry changed, disappeared, became ambiguous, or the file changed materially since review, do not delete; surface a conflict and ask only about the changed matter when necessary.

### 5.2 Constrained cleanup procedure

1. Select **only** the verified source entries targeted at `speckit.plan`; match by stable handoff ID and decision content.
2. Apply the smallest possible edit to the `## Pending Handoffs` section of the active feature's `spec.md`: remove exactly those entries; preserve other entries verbatim.
3. Remove the heading only if no pending entries remain. Preserve all permanent requirements, constraints, Clarifications, metadata, and unrelated document text.
4. Re-read source and destination after the edit: verify the destination still contains the decision, selected entries are gone, and all unrelated source content remains intact.
5. Report completed transfer/cleanup within the normal stage completion summary, without an extra approval or additional independent workflow step.

**Failure handling:** If destination verification fails, **do not touch the source**. If source cleanup fails, keep the verified destination and leave the original pending entry; report the incomplete cleanup without claiming full success. On retry, detect the existing destination (idempotence), verify it, and attempt deletion of the matching pending entry only—never duplicate or overwrite the decision. If the preconditions cannot be established safely, preserve the source and explain why.

**Scope boundary:** This approved exception authorizes cleanup in `plan` only for qualifying entries in the active `spec.md`. Universal Decision Handoff means all stages *read and reuse* approved decisions; it does **not** authorize cross-artifact deletion by `clarify`, `tasks`, `constitution`, `checklist`, `converge`, or `analyze` beyond each command's native permissions. Later transfers needing a different cleanup owner require a separately reviewed design, not silent extrapolation of this exception.

**Practical limitation:** The preset consists of agent instructions (`wrap`), not a transactional file-operation engine. These checks are required instructions and manual acceptance criteria, not a claim of atomic writes or guaranteed enforcement across all Copilot models.

## 6. Other design risks and mitigations

1. **Spec validation and HOW/WHY separation.** `specify` discourages implementation detail inside `spec.md`; test that a temporary pending section can coexist with the standard validation without turning into permanent scope or quality-check failure. Never change the standard template solely to hide this.
2. **Checklists and append-only files.** Do not put pending entries in documents that later cannot be cleaned. A command with constrained writes can only reuse decisions or recommend another permitted workflow for new decisions outside its scope.
3. **Unpersisted approvals in read-only commands.** If a user resolves something during `analyze`, label it as unpersisted and recommend a write-capable follow-up; do not promise the next chat will remember it.
4. **Stale source/target.** Re-read before write; if a document changed after approval, compare meaningful deltas and seek renewed consent only for material changes.
5. **Duplicate transfer / idempotence.** On retry, recognize a decision already present in the target; verify rather than adding an extra copy. Cleanup only its matching temporary entry.
6. **No hidden automatic transitions.** Do not invoke `clarify`, `plan`, `tasks`, or implementation automatically, preserving existing approval gates.
7. **Model-only enforcement.** Instructions can lower error rate, but cannot provide strong transactional guarantees. Test with a real Copilot agent and report limitations without claiming deterministic success.

## 7. Minimal implementation steps (implemented as instructions)

1. Add a compact shared handoff rules block to the wrappers or shared source text injected at packaging; maintain eight `wrap` contributions in `preset.yml`.
2. Update `specify` and `clarify` to account for approved future-stage decisions at final write.
3. Update `plan` to consume incoming decisions, refrain from re-questioning, verify destination research/design output, and perform the narrowly approved Option A cleanup with the §5 safeguards.
4. Update `tasks`, `constitution`, `checklist`, `analyze`, `converge` for read/reuse and their respective boundary protections.
5. Add regression tests and audit that the core templates/scripts/hooks remain unchanged.
6. Add this design and the approved requirements under `docs/` in the next release ZIP; update README and changelog.

## 8. Design approval and remaining implementation gate

- **Resolved:** Source cleanup Option A approved on 2026-11-03 for `speckit.plan`, narrowly scoped as specified in §5.
- **Implementation authorized:** the user explicitly requested implementation and packaging on 2026-11-03. The release contains instruction-level changes, not a deterministic file-operation engine.
- **Implementation verification:** static checks should pass; behavioral tests for destination-before-source order, cross-feature protection, idempotent retry, and unrelated content preservation remain necessary in Copilot.
- **Release artifact:** include the unchanged approved requirements summary and this updated design under `docs/` in the future v0.6.0 package, as already requested.

