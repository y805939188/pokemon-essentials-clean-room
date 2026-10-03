"""Read-only audit of this review's Git boundaries and reported reading coverage.

Reads reference text for a mechanical copy-candidate scan only; never imports,
executes, deserializes, compiles, or simulates reference behavior. It prints JSON
and does not write files. Reading-log aggregation is evidence navigation, not a
claim of semantic completeness.
"""
import argparse
import collections
import csv
import json
from pathlib import Path
import re
import subprocess

BASE = 'e1e01bb18d824931e54f182dd61af5a9f908ba85'
REFERENCE = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REMOTE = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
RUN = '2026-10-03-fd82a639'
PREFIX = f'review/global-independent-review/{RUN}/'


def git(root, *args):
    return subprocess.check_output(['git', '--no-optional-locks', '-C', str(root), *args])


def git_paths(root, *args):
    return git(root, *args).decode().rstrip('\0').split('\0')


def reading_records(run_root):
    records = []
    logs = list((run_root / 'agents').glob('*/*/reading-log.tsv'))
    logs += list((run_root / 'agents').glob('*/*/comparison-reading-log.tsv'))
    logs += list((run_root / 'agents').glob('*/*/peer-reading-log.tsv'))
    logs += [run_root / 'agents/D/reading-log.tsv', run_root / 'root/peer-reading-log.tsv',
             run_root / 'root/reading-supplement.tsv', run_root / 'root-reading-log.tsv']
    for log in sorted(set(path for path in logs if path.exists())):
        with log.open() as stream:
            for index, row in enumerate(csv.DictReader(stream, delimiter='\t'), 2):
                def first(*keys, default=''):
                    return next((row[key] for key in keys if row.get(key)), default)
                repository = first('repository', 'origin', 'material', 'kind', 'source',
                                   default='project' if log.name == 'root-reading-log.tsv' or log.parent.name == 'D' else '')
                identity = first('commit', 'fixed_commit', 'fixed_identity')
                if identity == REFERENCE:
                    repository = 'reference'
                elif repository == 'source':
                    repository = 'reference'
                path = first('relative_path', 'path', 'path_or_url', 'path_or_search',
                             'path_or_message', 'path_from_run_or_repository')
                mode = first('mode', 'reading_mode', 'method', 'read_extent', 'reading', 'extent')
                if log.parent.name == 'D':
                    path = 'deliverables/final-specification-set/' + path
                ranges = first('read_ranges', 'ranges_1_based', 'read_scope', 'ranges', 'range',
                               'lines_read', 'lines', 'actual_ranges', 'range_or_ids', 'selection', 'range_or_selector')
                if not ranges and row.get('start') and row.get('end'):
                    ranges = row['start'] + '-' + row['end']
                    mode = mode or 'explicit-bounded-static-read'
                if row.get('actual_ranges') and not mode:
                    mode = 'explicit-bounded-static-read'
                if repository not in ('project', 'reference'):
                    continue
                records.append(dict(repository=repository, path=path, mode=mode,
                                    ranges=ranges, scope=first('scope', 'purpose', 'purpose_and_limit',
                                                             'scope_and_limit', 'use_and_limit', 'note', 'limit'),
                                    log=str(log.relative_to(run_root)), log_line=index))
    return records


def ranges_for(record, count):
    mode = record['mode'].lower()
    if any(word in mode for word in ('search', 'identity', 'discover', 'inventory', 'parse', 'structure', 'count', 'mechanical')):
        return []
    value = record['ranges'].replace('–', '-').replace('—', '-').replace(',', ';')
    if value.strip().lower() in ('all', 'all lines', '1-eof') and 'full' in mode:
        return [(1, count)]
    ranges = []
    for part in value.split(';'):
        match = re.fullmatch(r'\s*(\d+)\s*-\s*(\d+|EOF)\s*', part)
        if match:
            start = int(match[1])
            end = count if match[2] == 'EOF' else int(match[2])
            if 1 <= start <= end <= count:
                ranges.append((start, end))
        elif re.fullmatch(r'\s*\d+\s*', part):
            number = int(part)
            if 1 <= number <= count:
                ranges.append((number, number))
    return ranges


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', required=True)
    parser.add_argument('--reference', required=True)
    args = parser.parse_args()
    root = Path(args.root)
    ref = Path(args.reference)
    run_root = root / PREFIX
    remote = git(root, 'remote', 'get-url', '--push', 'origin').decode().strip()
    commits = git(root, 'rev-list', '--reverse', BASE + '..HEAD').decode().splitlines()
    outside = []
    for commit in commits:
        for path in git_paths(root, 'diff-tree', '--no-commit-id', '--name-only', '-r', '-z', commit):
            if path and not path.startswith(PREFIX):
                outside.append(dict(commit=commit, path=path))
    tracked = set(git_paths(root, 'ls-tree', '-r', '--name-only', '-z', BASE))
    reference_paths = set(git_paths(ref, 'ls-files', '-z'))
    mapping = json.loads((root / 'review/wp80-delivery-readiness-review-2026-10-03/input-output-map.json').read_text())
    missing_inputs = [entry['input'] for entry in mapping if entry['input'] not in tracked]
    missing_outputs = [path for entry in mapping for path in entry['destinations'] if path not in tracked]
    with (run_root / 'wp-review-matrix.tsv').open() as stream:
        wps = list(csv.DictReader(stream, delimiter='\t'))
    expected = {f'WP{x:02}' for x in range(1, 81)}
    for family, children in ((47, 'AB'), (52, 'ABC'), (66, 'ABC'), (67, 'AB'), (73, 'AB')):
        expected.remove(f'WP{family:02}')
        expected.update(f'WP{family:02}-{child}' for child in children)
    actual = [row['wp'] for row in wps]
    records = reading_records(run_root)
    by_path = collections.defaultdict(list)
    for record in records:
        if record['repository'] == 'reference' and record['path'] in reference_paths:
            by_path[record['path']].append(record)
    coverage = []
    for path in sorted(reference_paths):
        file = ref / path
        evidence = by_path[path]
        count = None
        covered = set()
        try:
            is_text = file.suffix.lower() in ('.rb', '.txt', '.md', '.json', '.html', '.yml', '.url') or file.name in ('LICENSE', '.gitignore')
            if not is_text:
                coverage.append(dict(path=path, reported_semantic_lines=0, total_text_lines=None, evidence=evidence, meaning='Binary identity only; not opened or deserialized.'))
                continue
            count = len(file.read_text().splitlines())
            for record in evidence:
                for start, end in ranges_for(record, count):
                    covered.update(range(start, end + 1))
        except (UnicodeError, OSError):
            pass
        coverage.append(dict(path=path, reported_semantic_lines=len(covered),
                             total_text_lines=count, evidence=evidence,
                             meaning='Reported reading only; consult scope and equivalence judgments.'))
    # Candidate scan: exact long reference source lines, not a legal or semantic test.
    source_lines = set()
    for path in reference_paths:
        if path.endswith('.rb'):
            for line in (ref / path).read_text().splitlines():
                value = line.strip()
                if len(value) >= 80 and not value.startswith('#'):
                    source_lines.add(value)
    copy_candidates = []
    checked_versions = 0
    for commit in commits:
        changed = git_paths(root, 'diff-tree', '--no-commit-id', '--name-only', '-r', '-z', commit)
        for path in changed:
            if not path or Path(path).suffix not in ('.md', '.json', '.tsv', '.py'):
                continue
            try:
                data = git(root, 'show', commit + ':' + path).decode()
            except subprocess.CalledProcessError:
                continue  # Deleted paths are still checked by the commit whitelist above.
            checked_versions += 1
            for number, line in enumerate(data.splitlines(), 1):
                if line.strip() in source_lines:
                    copy_candidates.append(dict(commit=commit, path=path, line=number))
    print(json.dumps(dict(run_id=RUN, project_base=BASE,
        project_head=git(root, 'rev-parse', 'HEAD').decode().strip(), remote=remote,
        remote_matches_authorization=remote == REMOTE, new_commit_count=len(commits),
        commit_whitelist_violations=outside,
        working_status=git(root, 'status', '--porcelain=v1', '--untracked-files=all').decode().splitlines(),
        reference_head=git(ref, 'rev-parse', 'HEAD').decode().strip(),
        reference_head_matches=git(ref, 'rev-parse', 'HEAD').decode().strip() == REFERENCE,
        reference_status=git(ref, 'status', '--porcelain=v1', '--untracked-files=all').decode().splitlines(),
        reference_ignored=git_paths(ref, 'ls-files', '--others', '--ignored', '--exclude-standard', '-z'),
        missing_primary_inputs=missing_inputs, missing_sanitized_outputs=missing_outputs,
        wp_rows=len(actual), wp_unique=len(set(actual)), wp_set_matches=set(actual) == expected,
        wp_owner_counts=dict(collections.Counter(row['primary_agent'] for row in wps)),
        wp_status_counts=dict(collections.Counter(row['status'] for row in wps)),
        reference_tracked_count=len(reference_paths), reading_records=len(records),
        committed_file_versions_scanned=checked_versions,
        source_reading_navigation=coverage, exact_long_source_line_candidates=copy_candidates,
        limitations=['Mechanical aggregation does not prove substantive reading or behavioral coverage.',
                    'Unparseable or nonnumeric ranges remain in original logs and are not guessed.',
                    'Reference source corpus was mechanically scanned for copy candidates only; not counted as semantic reading.']),
        ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
