#!/usr/bin/env python3
"""Offline verification and reproducible packaging for SpecSense v0.6.0.

Usage:
    python3 verify_package.py --previous /path/to/spec-sense-v0.5.4.zip
    python3 verify_package.py --build-archive /path/to/spec-sense-v0.6.0.zip
    python3 verify_package.py --archive /path/to/spec-sense-v0.6.0.zip

Structural/integrity checks only. Does not emulate Copilot or execute Spec Kit.
"""
import argparse
import hashlib
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent
BASE = ("specify", "clarify", "plan", "tasks", "constitution")
NEW = ("converge", "analyze", "checklist")
ALL = BASE + NEW
VERSION = "0.6.0"
HANDOFF_MARKER = "\n---\n\n## Decision Handoff — v0.6.0\n"
RELEASE_FILES = (
    "LICENSE", "THIRD_PARTY_NOTICES.md", "README.md", "CHANGELOG.md",
    "SMOKE_TESTS.md", "preset.yml", "verify_package.py", "test_package.py",
    "docs/decision-handoff-requirements.md",
    "docs/decision-handoff-technical-design.md",
    "docs/decision-handoff-test-plan.md", "docs/validation-results.md",
) + tuple(f"commands/speckit.{name}.md" for name in ALL)


def original_policy(contents: str) -> str:
    """Remove only the appended handoff block for baseline policy comparison."""
    return contents.split(HANDOFF_MARKER, 1)[0]


def verify_handoff(name: str, contents: str) -> None:
    assert contents.count(HANDOFF_MARKER) == 1, f"{name}: expected one final handoff block"
    policy, block = contents.split(HANDOFF_MARKER)
    assert "## SDDW interactive policy" in policy, f"{name}: handoff must follow the original policy"
    assert "## SDDW interactive policy" not in block, f"{name}: handoff must be last"
    normalized = " ".join(block.split())
    for phrase in (
        "native active-feature resolution",
        "semantically equivalent", "forward-only adoption", "read-only",
        "no additional handoff approval", "constraints and qualifiers",
        "only durable copy",
    ):
        assert phrase in normalized, f"{name}: missing handoff contract: {phrase}"
    required = {
        "specify": ("exactly one", "DH-001", "final", "every new approved", "do not bypass validation"),
        "clarify": ("DH-001", "Read and preserve", "no-change path", "do not bypass validation"),
        "plan": ("approved Option A", "duplicate IDs", "byte-for-byte", "feature switched",
                 "stable ID AND decision content", "Retry idempotently", "no pending content remains",
                 "report incomplete cleanup", "no later-stage cross-artifact cleanup"),
        "tasks": ("Do not create a pending", "report pending cleanup", "unpersisted"),
        "constitution": ("Never put feature-specific", "only writable file", "unpersisted"),
        "checklist": ("Never create pending entries", "append-only", "unpersisted"),
        "analyze": ("no file writes of any kind", "conversation-only and unpersisted"),
        "converge": ("Only append", "transfer entries, or clean", "unpersisted"),
    }
    # Normalize line wraps; these are prompt-presence checks, NOT agent execution.
    for phrase in required[name]:
        assert phrase in normalized, f"{name}: missing boundary: {phrase}"
    if name == "plan":
        steps = ("Save the full decision", "RE-READ DESTINATION BEFORE SOURCE DELETION",
                 "Immediately before cleanup", "Match by stable ID", "Re-read source AND destination",
                 "Retry idempotently")
        positions = [block.index(step) for step in steps]
        assert positions == sorted(positions), "plan: unsafe transfer instruction order"
    else:
        assert "approved Option A" not in block, f"{name}: unexpected cleanup exception"


def verify_archive(path: Path) -> None:
    expected = {f"spec-sense/{rel}" for rel in RELEASE_FILES}
    with ZipFile(path) as archive:
        assert archive.testzip() is None, "Corrupt archive"
        names = archive.namelist()
        assert len(names) == len(set(names)), "Duplicate archive member"
        files = {i.filename for i in archive.infolist() if not i.is_dir()}
        assert files == expected, f"Archive files differ: {files ^ expected}"
        allowed_dirs = {"spec-sense/", "spec-sense/commands/", "spec-sense/docs/"}
        assert set(names) - files <= allowed_dirs, "Unexpected archive directories"
        for rel in RELEASE_FILES:
            assert archive.read(f"spec-sense/{rel}") == (ROOT / rel).read_bytes(), rel
    print(f"OK: ZIP allowlist + {len(expected)} exact file contents + CRC checks")


def build_archive(path: Path) -> None:
    # Never package .git, local artifacts, caches or arbitrary untracked files.
    assert path.resolve() not in {(ROOT / rel).resolve() for rel in RELEASE_FILES}
    path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(path, "w", compression=ZIP_DEFLATED) as archive:
        for rel in sorted(RELEASE_FILES):
            info = ZipInfo(f"spec-sense/{rel}", date_time=(2026, 11, 3, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (ROOT / rel).read_bytes())
    verify_archive(path)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    path.with_suffix(path.suffix + ".sha256").write_text(
        f"{digest}  {path.name}\n", encoding="utf-8")
    print(f"Prepared candidate package: {path}; Copilot release gate remains separate")


def check() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--previous", type=Path, help="Baseline v0.5.4 ZIP (original policy regression)")
    parser.add_argument("--archive", type=Path, help="Verify a v0.6.0 ZIP")
    parser.add_argument("--build-archive", type=Path, help="Build and verify a candidate ZIP")
    args = parser.parse_args()

    yaml_text = (ROOT / "preset.yml").read_text(encoding="utf-8")
    try:
        import yaml
    except ImportError:
        raise SystemExit("PyYAML is required for this validator: pip install PyYAML")
    m = yaml.safe_load(yaml_text)
    assert m["schema_version"] == "1.0"
    assert m["preset"]["id"] == "spec-sense"
    assert m["preset"]["version"] == VERSION
    assert m["preset"]["license"] == "MIT"
    assert m["preset"]["name"].startswith("SpecSense")
    assert ROOT.name == "spec-sense"
    for rel in RELEASE_FILES:
        assert (ROOT / rel).is_file(), f"Missing release file: {rel}"
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    notice_text = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert license_text.startswith("MIT License\n")
    assert "SpecSense contributors" in license_text
    for owner in ("Sergii Makarevych", "GitHub, Inc."):
        assert owner in notice_text and owner in readme_text
    for url in ("https://github.com/sermakarevich/sddw", "https://github.com/github/spec-kit"):
        assert url in notice_text and url in readme_text
    assert "THIRD_PARTY_NOTICES.md" in readme_text
    assert "`spec-sense`" in readme_text
    assert "specify preset remove spec-sense" in readme_text
    assert "specify preset add --dev /absolute/path/to/spec-sense" in readme_text
    assert "lean" not in str(m.get("requires", {})).lower(), "Must not depend on Lean"
    assert "templates" in m["provides"]
    assert not (set(m["provides"]) - {"templates"}), "No scripts/settings overrides"
    entries = m["provides"]["templates"]
    assert len(entries) == 8, f"Expected 8 commands, found {len(entries)}"
    assert {e["name"] for e in entries} == {f"speckit.{name}" for name in ALL}
    assert len({e["name"] for e in entries}) == len(entries)

    for name in ALL:
        rel = f"commands/speckit.{name}.md"
        entry = next(e for e in entries if e["name"] == f"speckit.{name}")
        assert entry["type"] == "command"
        assert entry["file"] == rel
        assert entry["replaces"] == f"speckit.{name}"
        assert entry["strategy"] == "wrap"
        contents = (ROOT / rel).read_text(encoding="utf-8")
        assert contents.startswith("{CORE_TEMPLATE}\n"), name
        assert contents.count("{CORE_TEMPLATE}") == 1, name
        assert "SDDW interactive policy" in contents, name
        assert any(word in contents.lower() for word in ("approval", "approve", "decision")), name
        verify_handoff(name, contents)
        # Simulate native command composition with YAML metadata at the top.
        mock_core = "---\ndescription: native core\n---\n## Native instruction\n"
        composed = contents.replace("{CORE_TEMPLATE}", mock_core)
        assert composed.startswith("---\ndescription: native core\n---")
        assert composed.count("## Native instruction") == 1
        assert "{CORE_TEMPLATE}" not in composed
        print(f"OK: speckit.{name}: wrap + core composition")

    details = {
        "converge": ("APPEND-ONLY", "one group", "final", "no gaps", "constitution"),
        "analyze": ("read-only", "one material", "full standard", "minor", "constitution"),
        "checklist": ("requirements-quality", "one category", "unchecked", "append-only", "final"),
    }
    for name, phrases in details.items():
        content = (ROOT / f"commands/speckit.{name}.md").read_text(encoding="utf-8").lower()
        for phrase in phrases:
            assert phrase.lower() in content, f"{name} missing {phrase!r}"

    if args.previous:
        with ZipFile(args.previous) as prev:
            for name in ALL:
                rel = f"commands/speckit.{name}.md"
                prior_paths = prev.namelist()
                prior_roots = {n.split("/", 1)[0] for n in prior_paths if "/" in n}
                assert len(prior_roots) == 1, f"Unexpected prior ZIP roots: {prior_roots}"
                prior_root = next(iter(prior_roots))
                old = prev.read(prior_root + "/" + rel)
                assert yaml.safe_load(prev.read(prior_root + "/preset.yml"))["preset"]["version"] == "0.5.4"
                new = original_policy((ROOT / rel).read_text(encoding="utf-8"))
                baseline = old.decode("utf-8").replace("\r\n", "\n")
                assert baseline == new, f"Regression: original {name} policy differs from v0.5.4"
                print(f"PRESERVED v0.5.4 policy: {name} (line endings normalized)")

    if args.archive:
        verify_archive(args.archive)
    if args.build_archive:
        build_archive(args.build_archive)

    print("PASS: v0.6.0 static/package checks only; Copilot behavior NOT tested by this validator")


if __name__ == "__main__":
    check()
