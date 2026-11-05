# SpecSense — Standard Spec Kit + GitHub Copilot

**Unofficial** Spec Kit preset inspired by [sermakarevich/sddw](https://github.com/sermakarevich/sddw).
It adapts **how Spec Kit collaborates with the user**; it does **not** replace Spec Kit's standard process, templates, scripts, or artifact formats. No Lean dependency.

## Less paperwork. More thinking.

**Asked Spec Kit to define your feature and got a wall of text instead?**

You describe an idea. The AI fills in the blanks, picks an architecture, produces
pages of confident-looking Markdown — and only *then* do you discover it solved
the wrong problem. You're reviewing assumptions you never agreed to, instead of
shaping the solution.

**SpecSense changes the conversation, not the framework.**

| Without SpecSense | With SpecSense |
| --- | --- |
| **Walls of text** before the problem is clear | **One focused question at a time** |
| **Silent assumptions** disguised as requirements | **Unknowns surfaced** and discussed |
| **Architecture decided for you** | **Options and trade-offs** you can choose from |
| **Documents generated before you're ready** | **Explicit approval** before important writes |
| **Endless boilerplate** to review | **Focused dialogue** on decisions that matter |

**Ask → Understand → Decide together → Generate.**

Keep standard Spec Kit artifacts, commands, and templates. Add the
SDDW-inspired discovery and approval checkpoints that put you back in control.
This is *not* a token-minimizing preset: it targets unnecessary back-and-forth,
premature output, and unapproved decisions while preserving Spec Kit's normal
artifact structure.

> **Your project. Your decisions. Spec Kit asks before it assumes.**

## Release notes

**v0.6.1 — fewer redundant prompts:** Existing native Copilot decisions stay;
do not add an optional second comment tab
alongside a valid decision question. Request missing change details only
after a user selects a change. No extra approvals or workflow stages.

**v0.6.0 — Decision Handoff:** All eight command wrappers now reuse previously
approved decisions from native Spec Kit artifacts before asking new questions.
Future-stage decisions approved during Discovery are persisted at the **final
approved stage write** in a temporary `## Pending Handoffs` section. No new
registry, workflow stage, or changes to core templates and scripts.

The **only** cross-artifact cleanup exception is `speckit.plan`: after fully
verifying an incoming plan-targeted decision in native `research.md`/`plan.md`,
it may remove precisely that unchanged pending entry from the active feature's
`spec.md`. Other commands retain their read-only/append-only/write scopes.

**v0.5.4 — naming consistency:** renamed the source/archive root and preset ID
from the historical unhyphenated identifier to **`spec-sense`**, while keeping
**SpecSense** as the display name. All eight command wrappers and their behavior
are unchanged from v0.5.3. This is an **ID migration**, not an in-place update:
remove the older preset before installing this release.

v0.5.3 updated introductory messaging to focus on Spec Kit rather than Copilot.
v0.5.2 added the README introduction; v0.5.1 added licensing and upstream
attribution. The wrappers are unchanged from v0.5.0, including the original
five carried over from v0.4.0.

## License and upstream attribution

SpecSense is released under the **MIT License**. See [LICENSE](LICENSE).

This project is an **unofficial, independent adaptation**, inspired by
[SDDW — Spec Driven Development Workflow](https://github.com/sermakarevich/sddw)
by **Sergii Makarevych**, and designed as an extension for
[GitHub Spec Kit](https://github.com/github/spec-kit) by **GitHub, Inc.**
Both upstream projects use the MIT License. SpecSense preserves their
attributions and MIT texts in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

SpecSense adapts SDDW's *interactive approach* (discover, ask one question at
a time, propose trade-offs, confirm decisions) to Spec Kit commands; it is
not a fork or an official integration. Its wrapper files use
`{CORE_TEMPLATE}` to insert Spec Kit's commands at install time, instead of
redistributing the core command templates. Neither upstream project
endorses or maintains SpecSense.

The MIT License permits use, modification and redistribution, including
commercial use, subject to retention of applicable copyright and license
notices. It does not grant trademark endorsement or ownership of upstream
code. If you bring in additional upstream source files, preserve their
copyright notices and review any applicable additional licenses.

## Scope and behavior

| Command | Interactive behavior | Native Spec Kit behavior preserved |
| --- | --- | --- |
| `speckit.specify` | One-at-a-time product discovery; section approvals; final write consent | Native spec artifacts, checks, hooks |
| `speckit.clarify` | Adaptive questions; approve batch clarification before writing | Native `spec.md` clarification structure |
| `speckit.plan` | Propose/approve material architecture choices before generation | Standard plan and design artifacts |
| `speckit.tasks` | Approve each Setup / Foundational / user-story / Polish group, then final file write | One standard `tasks.md`, normal IDs and phases |
| `speckit.constitution` | Review each principle separately and approve the constitution's final write | Original constitution template and scope guard |
| **`speckit.converge`** | **Inspect implementation, present evidence-backed gaps and proposed remediation tasks by group; approve each group and final append** | **Append-only `## Phase N: Convergence` in `tasks.md`; never modify code** |
| **`speckit.analyze`** | **Analyze fully; discuss only material issues, one at a time; include minor findings in final report** | **Strictly read-only cross-artifact analysis and coverage report** |
| **`speckit.checklist`** | **Discover review scope; preview/approve questions category-by-category; final write consent** | **Reviewer-owned requirements-quality checklist(s), native CHK IDs, append-only domain files** |

Other Spec Kit commands, including `implement`, and all artifact **templates** are unmodified.

## Decision Handoff — ask once, decide once

Example: while discussing `specify`, you explicitly approve a technical
choice (such as respecting `Retry-After` with a retry cap). The choice belongs
to `plan`, but must not be forgotten or asked again.

1. At the **approved final write**, `specify` adds to its existing `spec.md`:

   ```markdown
   ## Pending Handoffs

   - **DH-001 → speckit.plan / research.md** — Decision: Respect Retry-After for HTTP 429, with the agreed retry cap. Approved during speckit.specify.
   ```

2. `clarify` reads and preserves that entry; it does not ask again.
3. `plan` reuses the decision within the normal approval and writes its full
   meaning into `research.md` or an appropriate native planning artifact.
4. **Only after re-reading and verifying** the destination, `plan` can remove
   just the unchanged, plan-targeted entry from the active feature's `spec.md`.
   It keeps other pending entries and all permanent requirements intact.
5. If writing or verification fails, the source entry survives; a retry must
   not duplicate an existing valid destination. No extra human approval is
   required solely to carry forward an already approved decision.

Only **new decisions** are managed in this way; old feature files are not
backfilled. Decisions belonging to the current stage still go into canonical
Spec Kit sections. Pending handoffs do **not** extend permissions globally:
`analyze` remains read-only, `converge` remains append-only, and other stages
may consume decisions without permission to clean the original source.

The design and regression scenarios are part of this release:
[Requirements](docs/decision-handoff-requirements.md),
[Technical Design](docs/decision-handoff-technical-design.md),
[Test Plan](docs/decision-handoff-test-plan.md).

## Interactive workflow details

### `speckit.converge` — approve groups of gaps

1. Run only when a complete `tasks.md` exists and `speckit.implement` has run on it.
2. Inspect the present codebase versus spec/plan/tasks, using the ratified constitution as a constraint. Do not trust task checkboxes as evidence of implementation.
3. Report a compact severity summary and show **one group** of gaps with traceable evidence and **proposed new tasks** at a time. Group by severity or related requirement, whichever is clearer.
4. Ask approve/revise/reject/defer for each group. An unresolved constitution MUST violation cannot be waived by accepting the risk.
5. After all groups, request **separate final authorization** to append **only approved tasks**.
6. Use native convergence ID, phase, severity and source-reference rules. Do not edit existing task rows, previous convergence phases, spec, plan or application code. If no gap exists, **do not write**.

The command does not perform remediation. The handoff remains `speckit.implement` followed by `speckit.converge` again.

### `speckit.analyze` — interact only where decisions matter

1. Complete the normal full cross-artifact checks, coverage mapping, severity classification and constitution validation. **No file writes**.
2. Identify material findings (CRITICAL/HIGH and potentially consequential MEDIUM), show short triage information, and discuss **one** at a time with a recommendation and trade-offs when relevant.
3. Allow `remediation agreed`, `risk accepted` (only where permissible), `deferred`, `disputed` and `unresolved` decisions. They are **conversation-only**, never implicit file edits.
4. Produce the **full standard report**, including the smaller LOW/MEDIUM issues that were not discussed and the standard coverage metrics. Suggest the appropriate separate workflow to correct issues.
5. A constitution MUST conflict remains binding, regardless of a preference to ignore it.

**Hook safety:** if a mandatory extension hook could mutate data, the agent must stop or request separate explicit approval before triggering it; a read-only report never justifies hidden writes. The gate is prompt-level, not an OS sandbox.

### `speckit.checklist` — discover and approve categories

1. Inspect the feature spec and relevant context. Ask scope questions **one per reply** only while they materially change the checklist; avoid generic questionnaire dumps.
2. Propose scoped categories (e.g. API contract quality, permissions clarity, recovery behavior), then review the **actual proposed questions** for one category at a time.
3. Ask approve/revise/reject for that category; don't require per-item sign-off. If the category is long, review its exact questions in readable chunks and request one category-level approval.
4. After all category decisions, show destination domain file(s), number of items and append behavior. Ask for **separate final write approval**.
5. Generate standard `checklists/<domain>.md` artifacts. Never overwrite existing custom checklist text or mark newly generated items `[x]`. This is **requirements quality review**, not source-code testing.

The built-in `checklists/requirements.md` from specify/clarify has a distinct lifecycle; it is not a custom checklist to revise using this command.

## Install / upgrade

```bash
specify preset remove spec-sense
# New installation (or after uninstalling an older version):
specify preset add --from https://github.com/krzysztof-indyk/spec-sense/archive/refs/heads/main.zip --priority 5
specify preset list
```

## Why a `wrap` preset?

Each command file starts with `{CORE_TEMPLATE}` and adds a narrow interaction
policy below. With Spec Kit's `strategy: wrap`, the placeholder is replaced by
the original core command. This preserves native behavior and allows subsequent
core updates to be picked up instead of forking the command text.

A wrapper is still an **LLM instruction**, not deterministic process enforcement.
The new approval gates deliberately override when the core would write or ask
multiple questions. Hooks that can write require careful treatment. If the core
and an approval gate cannot both be satisfied safely, **stop and make the
conflict visible** rather than silently bypassing either.

## Requirements and validation

- An existing standard Spec Kit installation supporting presets and `wrap`
  (v0.3.0 worked with your setup). Manifest retains the earlier version range
  `speckit_version: ">=0.6.0"`; check actual CLI compatibility in your repo.
- An initialized project configured for GitHub Copilot.
- No Lean preset required; no template overrides shipped here.

Validate offline:

```bash
python3 /absolute/path/to/spec-sense/verify_package.py \
  --previous /absolute/path/to/spec-sense-v0.5.4.zip \
  --archive /absolute/path/to/spec-sense-v0.6.0.zip
```

`SMOKE_TESTS.md` includes earlier manual scenarios; the Decision Handoff
test plan adds 27 scenarios. Agent behavior cannot be proven statically. The offline validator parses YAML (when PyYAML is installed), checks
all wrapper files, checks preservation of original v0.5.4 wrapper content, validates per-command
Decision Handoff policy markers and simulates `{CORE_TEMPLATE}` composition. This is **not** an end-to-end Copilot test.

## References

- [Spec Kit preset reference](https://github.github.io/spec-kit/reference/presets.html)
- [Spec Kit command reference](https://github.github.io/spec-kit/reference/agentic-sdd.html)
- [Native converge command](https://github.com/github/spec-kit/blob/main/templates/commands/converge.md)
- [Native analyze command](https://github.com/github/spec-kit/blob/main/templates/commands/analyze.md)
- [Native checklist command](https://github.com/github/spec-kit/blob/main/templates/commands/checklist.md)
- [SDDW](https://github.com/sermakarevich/sddw)
