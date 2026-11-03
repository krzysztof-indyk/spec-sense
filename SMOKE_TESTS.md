# Smoke tests — SpecSense v0.6.0 + GitHub Copilot

Run these existing-policy regressions together with T01–T27 in
`docs/decision-handoff-test-plan.md`. Results are tracked separately in
`docs/validation-results.md`; a scenario listed here is not evidence it passed.

**Manual acceptance scenarios**, not executed by the offline package validator.
Test in a disposable initialized Spec Kit project; inspect git status and
artifact bytes before and after the approval gates. If the project has extension
hooks, test without them first, then separately test safe and unsafe hooks.

## Registration and regression (1–8)

1. `specify preset list` reports `spec-sense` v0.6.0. Lean is not required.
   Verify the unpacked directory and ZIP root are `spec-sense/` while the
   manifest `preset.name` and documentation use the public name **SpecSense**.
   If a legacy preset is still installed, remove it before adding `spec-sense`.
2. All eight `specify preset resolve speckit.<name>` commands resolve this preset.
3. Verify the effective Copilot skills/agent instructions include **core command**
   plus SDDW wrapper; no raw `{CORE_TEMPLATE}` remains.
4. Compare the original policy portions of all eight wrappers against the
   v0.5.4 ZIP using `verify_package.py --previous`. Only the added handoff block
   is excluded; line endings are normalized. Exercise the policies below to
   detect behavioral regressions that text comparison cannot establish.
5. Run `speckit.specify` with a vague feature idea: one question at a time,
   no write before final approval; standard spec generated afterward.
6. Run `speckit.clarify`: one question at a time, approved batch before update.
7. Run `speckit.plan`: propose/approve material technical choices, then generate
   normal `plan.md` and core outputs after final approval.
8. Run `speckit.tasks` and `speckit.constitution`: group-level and principle-level
   approval gates continue working; default standard templates remain intact.

## Converge: grouped, evidence-based, append-only (9–19)

9. With complete spec/plan/tasks and implemented feature, introduce an actual
   missing FR and a partial US acceptance condition. `converge` shows concise
   severity summary and one group of findings, including source refs and
   concrete code evidence. **No write yet**.
10. Approve group A. Agent now proposes the next group; it never assumes that
    accepting A authorizes other groups or a final file write.
11. Reject one false positive. Agent reevaluates evidence and excludes it from
    append. If actual evidence remains, report it as disputed, not "fixed".
12. Defer a proposed remediation needing a new architectural choice. Agent
    recommends `speckit.plan` and does not invent a design or auto-edit plan.
13. After every group is decided, reject final append: `tasks.md` is byte-for-
    byte unchanged and code is unchanged. Approve final append in a new test:
    exactly one new Convergence phase, sequential new `T###`, valid source refs
    and correct gap-type markers; all earlier task lines remain identical.
14. Run twice without new code changes: no duplicate convergence tasks are
    added for the same already-open finding.
15. Create a clean implementation satisfying everything: get **Converged**,
    no questions about adding empty work, no changed files.
16. Change a relevant source file after group approval but before final consent:
    a material discrepancy triggers re-evaluation and renewed approval for
    affected groups before append.
17. Violate a ratified constitution MUST: CRITICAL finding, proposed task first;
    choosing "risk accepted" does not mark it compliant or waive constitution.
18. Run without tasks or without prior implementation: prerequisite gate blocks
    appending rather than creating work on unapproved assumptions.
19. Use `--auto`: still requires group reviews and separate final consent.

## Analyze: full coverage, selective decisions, read-only (20–29)

20. Create CRITICAL/HIGH contradiction + cosmetic LOW issue. Analyze the whole
    spec/plan/tasks, present a short triage, ask **one question** on the material
    issue, and leave the minor finding in the **final full report**.
21. Present 2 materially distinct issues: agent asks about one, stops, then
    asks about the next only after your answer.
22. Identify an important MEDIUM issue affecting acceptance behavior: the
    agent treats it as material even though severity is not HIGH.
23. Mark an issue `risk accepted` and another `deferred`: both appear as
    review status in the final report; no underlying files are changed.
24. Violate constitution MUST: label CRITICAL, not waivable; direct separate
    correction of spec/plan/tasks instead of weakening constitution implicitly.
25. Run on a clean set of artifacts: full concise report, no artificial review
    questions or invented issues. Check coverage metrics.
26. Ask for a code/spec fix during the review: analyze does **not** implement
    or rewrite artifacts; suggests separate approved command.
27. Verify git status, file byte hashes, no new report/decision files, no
    checkbox changes, and no auto-invoked repair workflow.
28. Ask to stop mid-review: partial decisions and unresolved findings are
    transparently reported, with no writes.
29. Put a potentially write-capable mandatory `before_analyze` hook in config:
    agent stops or requests explicit separate authorization, never silently
    executes it while claiming a read-only run.

## Checklist: discovery, category approval, native format (30–41)

30. Ask `speckit.checklist` without focus area on a feature with API + security
    rules. Agent reads source, asks **one focused scope question** and stops.
31. If scope already explicit (`Focus on password reset permission rules`),
    skip redundant scoping questions.
32. Preview API requirement-quality questions under one category, request
    **category-level approval** only (no per-question approval).
33. Reject security category and revise reliability category. Agent excludes
    rejected questions and seeks renewed approval only for revised category.
34. With a large category, allow chunked previews of the exact questions
    while still asking for a single category-level approval after review.
35. Reject final file write: no `checklists/` created/modified. Approve later:
    generate valid native checklist file(s) with `CHK###`, appropriate quality
    dimension markers and all new boxes unchecked (`[ ]`).
36. Run in a repo with existing `checklists/api.md`: only append fresh,
    approved, non-duplicated `CHK###` items. Existing text and `[x]` marks
    remain untouched; continuation IDs are correct.
37. Keep `checklists/requirements.md` from core specify/clarify: custom
    checklist generation does not rewrite its internal evaluation state.
38. Request an implementation test ("verify response returns 200"): agent
    reframes to requirements-quality check ("is response behavior specified?")
    and does not pretend to run tests.
39. Approve no categories: no empty checklist file or directory is written.
40. New risk discovered between category approvals and final write: agent
    surfaces change and re-approves affected category rather than silently
    enlarging the checklist.
41. Use `--auto`: still asks for each category and final file-write consent.

## Hooks, packaging and rollback (42–46)

42. Validate manifest YAML, exactly eight `wrap` commands, no template/script
    overrides, and only one `{CORE_TEMPLATE}` per wrapper.
43. For converge/checklist, confirm mandatory hooks are not silently skipped:
    a hook with side effects requires separate authorization to run during
    the discovery gate or is delayed until the final authorized workflow,
    with any blockers stated explicitly.
44. Run offline `verify_package.py --previous /path/spec-sense-v0.5.4.zip`
    and inspect `PRESERVED` policy results for all eight commands. Run
    `python3 -m unittest -v test_package.py` and verify the candidate ZIP with
    `verify_package.py --archive /path/spec-sense-v0.6.0.zip`.
45. Remove v0.6.0 and reinstall v0.5.4; previous commands work as before;
    artifacts already generated with user approval are not removed.
46. Inspect resulting `tasks.md`, checklists and analysis report for missing
    required native metadata, false assertions of execution, and unexpected
    file modifications.
