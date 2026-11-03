#!/usr/bin/env python3
"""Offline verification for SpecSense v0.5.4.

Usage:
    python3 verify_package.py --previous /path/to/specsense-v0.5.3.zip
    python3 verify_package.py --archive /path/to/spec-sense-v0.5.4.zip

Structural/integrity checks only. Does not emulate Copilot or execute Spec Kit.
"""
import argparse
import hashlib
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
BASE = ("specify", "clarify", "plan", "tasks", "constitution")
NEW = ("converge", "analyze", "checklist")
ALL = BASE + NEW


def check() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--previous", type=Path, help="Previous v0.5.3 ZIP")
    parser.add_argument("--archive", type=Path, help="New v0.5.4 ZIP")
    args = parser.parse_args()

    yaml_text = (ROOT / "preset.yml").read_text(encoding="utf-8")
    try:
        import yaml
    except ImportError:
        raise SystemExit("PyYAML is required for this validator: pip install PyYAML")
    m = yaml.safe_load(yaml_text)
    assert m["schema_version"] == "1.0"
    assert m["preset"]["id"] == "spec-sense"
    assert m["preset"]["version"] == "0.5.4"
    assert m["preset"]["license"] == "MIT"
    assert m["preset"]["name"].startswith("SpecSense")
    assert ROOT.name == "spec-sense"
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
        content = (ROOT / f"commands/speckit.{name}.md").read_text().lower()
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
                new = (ROOT / rel).read_bytes()
                assert old == new, f"Regression: {name} differs from v0.4.0"
                digest = hashlib.sha256(new).hexdigest()[:16]
                print(f"UNCHANGED v0.5.3 -> v0.5.4: {name} sha256={digest}")

    if args.archive:
        expected_paths = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file()}
        with ZipFile(args.archive) as archive:
            assert archive.testzip() is None
            members = [i.filename for i in archive.infolist() if not i.is_dir()]
            assert len(members) == len(set(members))
            paths = {Path(n).relative_to("spec-sense").as_posix() for n in members}
            assert paths == expected_paths, f"Archive files differ: {paths ^ expected_paths}"
            for name in members:
                local = ROOT / Path(name).relative_to("spec-sense")
                assert archive.read(name) == local.read_bytes(), name
        print(f"OK: ZIP structure + {len(members)} content hashes + CRC checks")

    print("PASS: v0.5.4 manifest, eight wrapped commands, new policies, naming and regression checks")


if __name__ == "__main__":
    check()
