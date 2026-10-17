#!/usr/bin/env python3
"""Run and retain exact author check I/O on one frozen R3 input set."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
INVENTORY = HERE.parents[2]
ROOT = INVENTORY.parents[2]


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def hashes(phase):
    paths = ['routing-manifest.json', 'section-coverage.json', 'routing-manifest.schema.json',
             'accepted-source-updates.json', 'routing.py',
             'revisions/r1/tools/validator-regressions.py',
             'revisions/r3/tools/navigation-check.py', 'revisions/r3/tools/preservation-check.py',
             'revisions/r3/tools/run-author-checks.py',
             'current-section-coverage.schema.json', 'revisions/r3/tools/current-coverage-check.py',
             'revisions/r3/tools/accepted-binding-regressions.py',
             'revisions/r3/tools/backfill-accepted-sources.py',
             'revisions/r3/tools/source-guard-regressions.py',
             'revisions/r3/source-refinement-patch.json']
    if phase == 'cumulative-source':
        paths += ['current-section-coverage.json', 'revisions/r3/tools/accepted-backfill-result.json']
    return {p: hashlib.sha256((INVENTORY / p).read_bytes()).hexdigest() for p in paths}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phase', required=True, choices=['r2-fixed-source', 'cumulative-source'])
    args = parser.parse_args()
    python = sys.executable
    routing = str(INVENTORY / 'routing.py')
    commands = [
        [python, routing, 'validate'],
        [python, str(INVENTORY / 'revisions/r1/tools/validator-regressions.py'), '--output', str(HERE / 'actual-results.json')],
        [python, routing, 'self-test'],
        [python, routing, 'render'],
        [python, routing, 'check-generated'],
        [python, str(HERE / 'navigation-check.py'), '--output', str(HERE / 'navigation-results.json')],
        [python, str(HERE / 'preservation-check.py'), '--output', str(HERE / 'preservation-results.json')],
    ]
    if args.phase == 'cumulative-source':
        commands += [
            [python, str(HERE / 'accepted-binding-regressions.py'), '--output', str(HERE / 'accepted-binding-results.json')],
            [python, str(HERE / 'current-coverage-check.py'), '--output', str(HERE / 'current-coverage-results.json')],
            [python, str(HERE / 'source-guard-regressions.py'), '--output', str(HERE / 'source-guard-results.json')],
        ]
    evidence = {'schema_version': 'routing-r3-author-command-io.v1',
                'scope': 'AUTHOR_TOOL_CHECKS_ONLY; no independent acceptance, prototype or game/reference execution',
                'stage': args.phase, 'started_utc': stamp(),
                'working_directory': str(ROOT), 'fixed_previous_candidate': 'a32873d2860b15d9f5e27727db8f131f4ec433b6',
                'initial_input_sha256': hashes(args.phase), 'commands': [],
                'not_executed_in_this_phase': [] if args.phase == 'cumulative-source' else [
                    'Full cumulative current-heading coverage check: source switch awaits U04 accepted input',
                    'Five actual extension/shared-receiver regression fixtures: await cumulative applied source; no PASS claimed']}
    evidence_path = HERE / 'actual-command-io.json'
    for argv in commands:
        item = {'argv': argv, 'started_utc': stamp(), 'input_sha256_before': hashes(args.phase)}
        start = time.monotonic()
        completed = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
        item.update(ended_utc=stamp(), elapsed_seconds=round(time.monotonic() - start, 3),
                    exit_code=completed.returncode, stdout=completed.stdout, stderr=completed.stderr,
                    input_sha256_after=hashes(args.phase))
        evidence['commands'].append(item)
        evidence['completed_utc'] = stamp()
        evidence['all_commands_exit_zero'] = len(evidence['commands']) == len(commands) and all(c['exit_code'] == 0 for c in evidence['commands'])
        evidence['all_input_hashes_stable'] = all(c['input_sha256_before'] == c['input_sha256_after'] == evidence['initial_input_sha256'] for c in evidence['commands'])
        evidence_path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n')
        print(json.dumps({'command': Path(argv[1]).name, 'arguments': argv[2:], 'exit_code': completed.returncode,
                          'elapsed_seconds': item['elapsed_seconds']}, ensure_ascii=False), flush=True)
        if completed.returncode != 0 or not evidence['all_input_hashes_stable']:
            print(completed.stdout, file=sys.stderr)
            print(completed.stderr, file=sys.stderr)
            return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
