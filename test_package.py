"""Offline regression tests for packaging and prompt contracts, not Copilot behavior."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile

import verify_package as package


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "spec-sense"
        for rel in package.RELEASE_FILES:
            target = self.root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((package.ROOT / rel).read_bytes())
        self.scope = patch.object(package, "ROOT", self.root)
        self.scope.start()
        self.addCleanup(self.scope.stop)

    def check(self):
        with patch("sys.argv", ["verify_package.py"]), contextlib.redirect_stdout(io.StringIO()):
            package.check()

    def change(self, rel, old, new):
        target = self.root / rel
        content = target.read_text(encoding="utf-8")
        self.assertIn(old, content)
        target.write_text(content.replace(old, new, 1), encoding="utf-8")

    def build(self, name="release.zip"):
        path = Path(self.temp.name) / name
        with contextlib.redirect_stdout(io.StringIO()):
            package.build_archive(path)
        return path

    def test_valid_source(self):
        self.check()

    def test_reject_handoff_before_original_policy(self):
        target = self.root / "commands/speckit.plan.md"
        content = target.read_text(encoding="utf-8")
        policy, block = content.split(package.HANDOFF_MARKER)
        prefix = "{CORE_TEMPLATE}\n"
        target.write_text(prefix + package.HANDOFF_MARKER + block + policy[len(prefix):], encoding="utf-8")
        with self.assertRaisesRegex(AssertionError, "handoff must follow"):
            self.check()

    def test_reject_changed_command_strategy(self):
        self.change("preset.yml", 'strategy: "wrap"', 'strategy: "replace"')
        with self.assertRaises(AssertionError):
            self.check()

    def test_reject_duplicate_command(self):
        self.change("preset.yml", 'name: "speckit.clarify"', 'name: "speckit.specify"')
        with self.assertRaises(AssertionError):
            self.check()

    def test_reject_duplicate_core(self):
        self.change("commands/speckit.plan.md", "{CORE_TEMPLATE}", "{CORE_TEMPLATE}\n{CORE_TEMPLATE}")
        with self.assertRaises(AssertionError):
            self.check()

    def test_reject_missing_plan_guard(self):
        self.change("commands/speckit.plan.md", "stable ID AND decision content", "topic")
        with self.assertRaises(AssertionError):
            self.check()

    def test_reject_reversed_verification_order(self):
        target = self.root / "commands/speckit.plan.md"
        content = target.read_text(encoding="utf-8")
        content = content.replace("RE-READ DESTINATION BEFORE SOURCE DELETION", "TEMP_MARKER")
        content = content.replace("Immediately before cleanup", "RE-READ DESTINATION BEFORE SOURCE DELETION")
        content = content.replace("TEMP_MARKER", "Immediately before cleanup")
        target.write_text(content, encoding="utf-8")
        with self.assertRaisesRegex(AssertionError, "unsafe transfer"):
            self.check()

    def test_reject_missing_read_only_guard(self):
        self.change("commands/speckit.analyze.md", "no file writes of any kind", "writes allowed")
        with self.assertRaises(AssertionError):
            self.check()

    def test_archive_excludes_local_files_and_is_reproducible(self):
        for rel in (".git/config", "artifacts/old.zip", "__pycache__/test.pyc", "private.txt"):
            target = self.root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("not distributable", encoding="utf-8")
        first = self.build("first.zip")
        second = self.build("second.zip")
        self.assertEqual(first.read_bytes(), second.read_bytes())
        self.assertTrue(first.with_suffix(".zip.sha256").is_file())

    def test_reject_unsafe_or_extra_archive_paths(self):
        for member in ("spec-sense/.git/config", "spec-sense/../outside", "/absolute", "other-root/README.md"):
            with self.subTest(member=member):
                path = self.build()
                with ZipFile(path, "a") as archive:
                    archive.writestr(member, "unexpected")
                with self.assertRaises(AssertionError):
                    package.verify_archive(path)

    def test_reject_archive_content_mismatch(self):
        path = self.build()
        self.change("README.md", "SpecSense", "Altered")
        with self.assertRaises(AssertionError):
            package.verify_archive(path)

    def test_reject_missing_required_doc(self):
        (self.root / "docs/decision-handoff-requirements.md").unlink()
        with self.assertRaises(AssertionError):
            self.check()


if __name__ == "__main__":
    unittest.main()
