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
