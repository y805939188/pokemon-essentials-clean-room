"""Read-only whitelist and exact long-source-line candidate audit of every new commit.
Never executes, imports, compiles, deserializes or simulates reference material.
No network or filesystem writes. A zero candidate count is not semantic proof.
"""
import argparse
import json
from pathlib import Path
import subprocess


def git(root, *args):
    return subprocess.check_output(['git', '--no-optional-locks', '-C', root, *args])


def main():
    parser = argparse.ArgumentParser()
    for name in ('root', 'reference', 'base', 'head', 'allowed-prefix'):
        parser.add_argument('--' + name, required=True)
    args = parser.parse_args()
    source_lines = set()
    for path in git(args.reference, 'ls-files', '-z').decode().split(chr(0)):
        if not path.endswith('.rb'):
            continue
        for line in (Path(args.reference) / path).read_text().splitlines():
            value = line.strip()
            if len(value) >= 80 and not value.startswith('#'):
                source_lines.add(value)
    commits = git(args.root, 'rev-list', '--reverse', args.base + '..' + args.head).decode().splitlines()
    violations, candidates, nontext, paths = [], [], [], set()
    versions = 0
    for commit in commits:
        changed = git(args.root, 'diff-tree', '--no-commit-id', '--name-only', '-r', '-z', commit).decode().split(chr(0))
        for path in changed:
            if not path:
                continue
            paths.add(path)
            if not path.startswith(args.allowed_prefix):
                violations.append(dict(commit=commit, path=path))
            exists = subprocess.run(['git', '--no-optional-locks', '-C', args.root, 'cat-file', '-e', commit + ':' + path], capture_output=True).returncode == 0
            if not exists:
                continue
            raw = git(args.root, 'show', commit + ':' + path)
            versions += 1
            try:
                text = raw.decode()
            except UnicodeDecodeError:
                nontext.append(dict(commit=commit, path=path))
                continue
            for number, line in enumerate(text.splitlines(), 1):
                if line.strip() in source_lines:
                    candidates.append(dict(commit=commit, path=path, line=number))
    print(json.dumps(dict(base=args.base, head=args.head,
        actual_head=git(args.root, 'rev-parse', 'HEAD').decode().strip(),
        push_remote=git(args.root, 'remote', 'get-url', '--push', 'origin').decode().strip(),
        commits=commits, changed_path_count=len(paths), file_versions_checked=versions,
        whitelist_violations=violations, exact_long_source_line_candidates=candidates,
        non_utf8_files=nontext, working_status=git(args.root, 'status', '--porcelain=v1', '--untracked-files=all').decode().splitlines(),
        limitations=['Mechanical publication safety navigation only; manual content review required.',
                    'No reference reading coverage inferred from copy-candidate scan.']), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
