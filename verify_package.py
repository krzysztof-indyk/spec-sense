#!/usr/bin/env python3
"""Static SpecSense v0.6.0 package and additive handoff-contract validator.

No Copilot execution or transactional behavior is simulated by this script.
Usage: python verify_package.py --previous old-v0.5.4.zip --archive new-v0.6.0.zip
"""
import argparse
from pathlib import Path
from zipfile import ZipFile
import yaml

ROOT = Path(__file__).resolve().parent
COMMANDS = ('specify', 'clarify', 'plan', 'tasks', 'constitution',
            'converge', 'analyze', 'checklist')
DOCS = ('decision-handoff-requirements.md',
        'decision-handoff-technical-design.md',
        'decision-handoff-test-plan.md')


def read_previous(archive: Path, path: str) -> bytes:
    with ZipFile(archive) as z:
        return z.read('spec-sense/' + path)


def check(previous=None, archive=None):
    assert ROOT.name == 'spec-sense'
    manifest = yaml.safe_load((ROOT / 'preset.yml').read_text(encoding='utf-8'))
    assert manifest['schema_version'] == '1.0'
    p = manifest['preset']
    assert p['id'] == 'spec-sense' and p['version'] == '0.6.0'
    assert p['name'].startswith('SpecSense') and p['license'] == 'MIT'
    assert set(manifest['provides']) == {'templates'}
    entries = manifest['provides']['templates']
    assert len(entries) == len(COMMANDS)
    assert {entry['name'] for entry in entries} == {f'speckit.{x}' for x in COMMANDS}
    assert 'lean' not in str(manifest.get('requires', {})).lower()

    for x in COMMANDS:
        path = f'commands/speckit.{x}.md'
        e = next(v for v in entries if v['name'] == f'speckit.{x}')
        assert e['type'] == 'command' and e['file'] == path
        assert e['strategy'] == 'wrap' and e['replaces'] == f'speckit.{x}'
        contents = (ROOT / path).read_text(encoding='utf-8')
        assert contents.startswith('{CORE_TEMPLATE}\n')
        assert contents.count('{CORE_TEMPLATE}') == 1
        assert contents.count('## SpecSense v0.6.0 — Decision Handoff') == 1
        assert '## Pending Handoffs' in contents
        assert 'Read before asking' in contents
        assert 'explicit approved decision' in contents or 'explicit approved' in contents
        assert 'final approved write' in contents
        assert 'do not backfill' in contents
        assert 'verify' in contents.lower()
        native = '---\ndescription: core command\n---\n## Original core logic\n'
        expanded = contents.replace('{CORE_TEMPLATE}', native)
        assert expanded.startswith(native) and expanded.count('## Original core logic') == 1
        if previous:
            old = read_previous(previous, path)
            updated = (ROOT / path).read_bytes()
            assert updated.startswith(old.rstrip() + b'\n\n---\n\n'), f'{x} old policy edited unexpectedly'
        print('PASS: wrapped core + handoff contract', x)

    role_phrases = {
        'specify': ('final approved normal', 'technical choice', 'checker'),
        'clarify': ('existing final', 'preserve unrelated', 'pending entries'),
        'plan': ('approved narrowly scoped exception', 'verify before cleanup',
                 're-read both', 'active feature', 'qualifiers', 'retry'),
        'tasks': ('cleanup pending', 'cannot delete', 'standard'),
        'constitution': ('only `.specify/memory/constitution.md`', 'feature-specific'),
        'analyze': ('strictly read-only', 'conversation-only', 'not persisted'),
        'converge': ('append-only', 'never treat append as source'),
        'checklist': ('append-only', 'quality of requirements'),
    }
    for x, terms in role_phrases.items():
        txt = (ROOT / f'commands/speckit.{x}.md').read_text().lower()
        for term in terms:
            assert term.lower() in txt, f'{x} missing {term!r}'
    print('PASS: per-command permission / reuse checks')

    for d in DOCS:
        f = ROOT / 'docs' / d
        assert f.is_file() and f.stat().st_size > 1500
    if previous:
        # Named docs, README and the validator are intentionally updated; license and notices not.
        for unchanged in ('LICENSE', 'THIRD_PARTY_NOTICES.md'):
            assert (ROOT / unchanged).read_bytes() == read_previous(previous, unchanged)
    readme = (ROOT / 'README.md').read_text()
    for term in ('SpecSense v0.6.0', 'Pending Handoffs', 'plan-targeted',
                 'decision-handoff-technical-design.md', 'spec-sense',
                 'https://github.com/sermakarevich/sddw',
                 'https://github.com/github/spec-kit'):
        assert term in readme, term
    assert 'MIT License' in (ROOT / 'LICENSE').read_text()
    print('PASS: documentation and MIT attribution')

    if archive:
        expected = {q.relative_to(ROOT).as_posix() for q in ROOT.rglob('*') if q.is_file()}
        with ZipFile(archive) as z:
            assert z.testzip() is None, 'Archive CRC failed'
            files = [m.filename for m in z.infolist() if not m.is_dir()]
            assert len(files) == len(set(files)), 'Duplicate ZIP members'
            actual = {Path(n).relative_to('spec-sense').as_posix() for n in files}
            assert actual == expected, f'ZIP contents differ: {actual ^ expected}'
            for name in files:
                f = ROOT / Path(name).relative_to('spec-sense')
                assert z.read(name) == f.read_bytes(), name
        print('PASS: archive integrity, paths, exact bytes:', len(files), 'files')
    print('PASS: SpecSense v0.6.0 STATIC validation (agent E2E not run)')


if __name__ == '__main__':
    a = argparse.ArgumentParser()
    a.add_argument('--previous', type=Path)
    a.add_argument('--archive', type=Path)
    args = a.parse_args()
    check(args.previous, args.archive)
