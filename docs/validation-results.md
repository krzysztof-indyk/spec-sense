# v0.6.0 validation record

Date: 2026-11-03. Status: candidate package; NOT release-approved.

## Automated evidence

- PASS: 12 automated unit/regression tests (`python -B -m unittest -v
  test_package.py`), including invalid manifest strategy/names, duplicate core
  placeholders, missing guards, reversed transfer instructions, missing docs,
  unexpected ZIP paths, modified ZIP contents and reproducible packaging.
  The ordering regression rejects handoff instructions before the original policy.
  All eight wrappers now end with concise Decision Handoff instructions.
- PASS: `verify_package.py --previous artifacts/spec-sense-v0.5.4-baseline.zip`:
  all eight wrappers, manifest, simulated core composition and handoff contract
  checks. All eight original policy bodies match the v0.5.4 baseline after
  line-ending normalization; only the appended Decision Handoff block is excluded.
- Baseline: local Git HEAD `571fe3cbd1b5655924bd732e4258811d4c0531dd`, exported
  with `git archive` under `spec-sense/`; its manifest reports v0.5.4. This is a
  local baseline export, not an independently downloaded release archive.
- PASS: `git diff --check` (no whitespace errors).
- Environment: Windows, bundled Python 3.12, PyYAML 6.0.3 installed only under
  ignored `artifacts/python-deps`. Unit tests passed outside the sandbox after
  its temporary-directory permissions prevented the first run from executing.

Reproduce offline validation from the repository root with Python and PyYAML:

```text
python -B -m unittest -v test_package.py
python -B verify_package.py --previous artifacts/spec-sense-v0.5.4-baseline.zip
python -B verify_package.py --build-archive artifacts/spec-sense-v0.6.0.zip
python -B verify_package.py --archive artifacts/spec-sense-v0.6.0.zip
```

The package contains exactly the 20 distributable files in `RELEASE_FILES`,
including the three unchanged approved input documents. The builder verifies
paths, bytes and CRCs and emits a SHA-256 sidecar. Local dependencies, baseline
ZIPs, `.git` and caches are excluded. The validator checks prompt structure and
packaging; it cannot establish that Copilot obeys the prompts or that native
Spec Kit integration succeeds.

## Required observed behavior — pending

No real Spec Kit + Copilot acceptance scenarios have been executed in this
environment. The repository does not contain an initialized disposable Spec Kit
project, and `specify` is not available on PATH. Do not mark T01–T27 passed.

Before calling v0.6.0 complete, run the release-gate subset from
`decision-handoff-test-plan.md`: T01–T10, T12–T13, T17–T18, T20–T21, T23–T27
in a clean Spec Kit + Copilot test repository. Run the existing smoke scenarios
as regressions, particularly all original approval gates and output formats.

For each scenario, record the Spec Kit version, Copilot agent/model, inputs,
decisions, observed result and before/after artifact diffs. For failure tests,
capture destination/source state and the agent's completion report. Verify all
eight preset resolutions and native script/template resolution. Static string
checks and simulated core composition do not substitute for this evidence.

The approved requirements, design and test plan are retained unchanged. Their
approval/history labels describe the design baseline; this record tracks the
implementation's validation state separately.
