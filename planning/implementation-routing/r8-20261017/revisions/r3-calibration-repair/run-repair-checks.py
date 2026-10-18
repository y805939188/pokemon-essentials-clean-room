#!/usr/bin/env python3
"""Capture real bounded follow-up I/O after the unchanged ten-command suite."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
INV = HERE.parents[1]
ROOT = INV.parents[2]


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def hashes():
    paths = ['routing-manifest.json', 'routing.py', 'revisions/r3/source-refinement-patch.json',
             'revisions/r3/feature-source-deltas.json', 'revisions/r3/source-file-reassessment.json',
             'revisions/r3/build-author-evidence.py', 'revisions/r3/facet-inheritance.json',
             'revisions/r3/feature-resolution.json', 'revisions/r3-calibration-repair/correction-record.json',
             'revisions/r3-calibration-repair/check-repair.py', 'revisions/r3-calibration-repair/run-repair-checks.py']
    return {p: hashlib.sha256((INV / p).read_bytes()).hexdigest() for p in paths}


def main():
    suite_path = INV / 'revisions/r3/tools/actual-command-io.json'
    suite = json.loads(suite_path.read_bytes())
    assert len(suite['commands']) == 10 and suite['all_commands_exit_zero'] and suite['all_input_hashes_stable']
    assert suite['initial_input_sha256']['routing-manifest.json'] == hashes()['routing-manifest.json']
    record = {'schema_version': 'routing-r3-bounded-repair-command-io.v1',
              'role': 'AUTHOR_STATIC_IO_ONLY_NOT_INDEPENDENT_REVIEW', 'started_utc': stamp(),
              'working_directory': str(ROOT), 'python': sys.executable,
              'preparation_observation': {'initial_python': 'python3',
                  'observed_first_validate_failure': "ModuleNotFoundError: No module named 'jsonschema'",
                  'original_observation': 'Tool execution before the retained suite; no exact start/end timestamp asserted for that preliminary invocation.',
                  'resolved_by': 'Isolated /tmp/r3-repair-venv with jsonschema4.26.0; no project/system dependency edit.'},
              'unchanged_ten_command_suite': {'path': str(suite_path.relative_to(INV)),
                  'sha256': hashlib.sha256(suite_path.read_bytes()).hexdigest(),
                  'started_utc': suite['started_utc'], 'completed_utc': suite['completed_utc'],
                  'commands': suite['commands'], 'all_commands_exit_zero': True, 'all17_input_hashes_stable': True},
              'initial_input_sha256': hashes(), 'commands': []}
    commands = [[sys.executable, str(HERE / 'check-repair.py')],
                [sys.executable, str(INV / 'revisions/r3/tools/final-calibration-proof.py'),
                 '--output', str(INV / 'revisions/r3/tools/final-calibration-proof.json')]]
    for argv in commands:
        item = {'argv': argv, 'started_utc': stamp(), 'input_sha256_before': hashes()}
        start = time.monotonic()
        result = subprocess.run(argv, cwd=ROOT, text=True, capture_output=True)
        item.update(ended_utc=stamp(), elapsed_seconds=round(time.monotonic()-start, 3),
                    exit_code=result.returncode, stdout=result.stdout, stderr=result.stderr,
                    input_sha256_after=hashes())
        record['commands'].append(item)
        record['completed_utc'] = stamp()
        record['all_commands_exit_zero'] = len(record['commands']) == 2 and all(c['exit_code'] == 0 for c in record['commands'])
        record['all_input_hashes_stable'] = all(c['input_sha256_before'] == c['input_sha256_after'] == record['initial_input_sha256'] for c in record['commands'])
        (HERE / 'command-io.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
        print(json.dumps({'command': Path(argv[1]).name, 'exit_code': result.returncode,
                          'elapsed_seconds': item['elapsed_seconds']}, ensure_ascii=False), flush=True)
        if result.returncode or not record['all_input_hashes_stable']:
            print(result.stdout)
            print(result.stderr, file=sys.stderr)
            return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
