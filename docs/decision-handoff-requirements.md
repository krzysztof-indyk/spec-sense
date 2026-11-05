# SpecSense — Decision Handoff

**Status:** Discovery approved  
**Planned release:** v0.6.0  
**Baseline:** SpecSense v0.5.4, standard GitHub Spec Kit (no Lean)

## Problem

GitHub Copilot sometimes repeats effectively identical questions during later Spec Kit stages (`clarify`, `plan`, etc.) even after the user has approved the decision in an earlier stage (`specify`). One possible cause is that a decision made during interactive discovery is not saved to a durable artifact, especially when it is a technical decision discussed during `specify` but normally documented during `plan`.

## Objective

**Ask once. Decide once. Carry decisions forward.** Preserve consciously approved decisions between stages while keeping SpecSense an interaction-layer preset on the standard Spec Kit workflow.

## Requirements

| ID | Requirement |
| --- | --- |
| R1 | Preserve standard Spec Kit commands, templates, scripts, artifacts, and stage responsibilities. Do not add a separate decision registry or workflow. |
| R2 | Support Decision Handoff across stages, not solely `specify → plan`. A stage reuses existing approved decisions rather than rediscovering them. |
| R3 | Decisions agreed before their target stage are temporarily recorded in a single `## Pending Handoffs` section of the current writable Spec Kit artifact. Each entry includes the approved decision and target stage. No new feature-level files or core template changes. |
| R4 | During interactive discovery, collect decisions in conversation. Persist them only during the current stage's **final user-approved artifact write**. Do not report stage completion unless all new approved decisions are accounted for in a canonical section or `Pending Handoffs`. |
| R5 | Before asking, load relevant existing Spec Kit artifacts and distinguish decided, open, conflicting, and out-of-scope questions. Ask again only for material contradictions, genuinely missing details, or newly discovered risks; explain why. |
| R6 | At the target stage, copy the decision's meaning into the standard destination artifact, verify the destination, then remove the temporary entry. Retain the entry if transfer or verification fails. Never remove a permanent requirement or constraint from the source. |
| R7 | Reuse the stage's existing final approval; no additional approval merely to transfer an already approved decision. Preserve read-only and append-only command boundaries. |
| R8 | Forward-only adoption: do not migrate, reinterpret, or rewrite historical decisions that predate this feature. Normal reading of existing Spec Kit artifacts remains necessary. |

## Acceptance criteria

1. A technical decision explicitly approved in `specify` is accessible to `plan` without the same question being asked again.
2. `clarify` sees and preserves approved pending decisions destined for a later stage.
3. Decision transfer is verified in the destination before its pending source entry is removed.
4. Failed, partial, interrupted, or ambiguous transfers never cause loss of the only durable copy.
5. A stage never claims successful completion when newly approved decisions have been omitted from both its canonical artifact and its pending section.
6. No additional human approval is requested solely for an unchanged, already approved decision.
7. Standard Spec Kit templates and native command boundaries remain intact.
8. Historical projects and decisions are not retroactively migrated.

## Explicitly out of scope

- Automatic backfill of decisions from older projects.
- A new decisions database, ledger file, or SpecSense-specific workflow stage.
- Changing the Copilot interactive multiple-choice/comment UI (deferred pending screenshot).
- Auto-resolving conflicts between approved decisions and newly discovered facts.
- Changing core Spec Kit scripts or document templates.

## Important compatibility note

The exact mechanism for removing a temporary entry from a **previous stage's** file is an open technical-design decision. Core commands such as `analyze` are strictly read-only and `converge` is append-only, so universal *reading* must not imply universal *writing*. This requirement document records the desired behavior, not authorization to bypass core restrictions.
