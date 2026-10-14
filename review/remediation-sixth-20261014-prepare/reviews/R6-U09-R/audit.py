import argparse
import datetime as dt
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
CWD = pathlib.Path('/workspace/pokemon-essentials-clean-room')

def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}

def run(argv, output):
    start = utc()
    p = subprocess.run(argv, cwd=CWD, capture_output=True)
    record = {'argv': argv, 'cwd': str(CWD), 'utc_start': start, 'utc_end': utc(),
              'exit': p.returncode, 'stdout': p.stdout.decode('utf-8', 'replace'),
              'stderr': p.stderr.decode('utf-8', 'replace'),
              'evidence_level': 'TOOL_VALIDATION', 'reference_execution': False}
    (ROOT / output).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(record, ensure_ascii=False))
    return p

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='action', required=True)
    r = sub.add_parser('read')
    r.add_argument('path')
    r.add_argument('start', type=int)
    r.add_argument('end', type=int)
    r.add_argument('--repo')
    r.add_argument('--ref')
    c = sub.add_parser('command')
    c.add_argument('output')
    c.add_argument('argv', nargs=argparse.REMAINDER)
    a = p.parse_args()
    if a.action == 'command':
        result = run(a.argv, a.output)
        sys.exit(result.returncode)
    start = utc()
    argv = (['git', '-C', a.repo, 'show', a.ref + ':' + a.path] if a.repo else None)
    if argv:
        result = subprocess.run(argv, cwd=CWD, capture_output=True, check=True)
        data = result.stdout
    else:
        data = (CWD / a.path).read_bytes()
    lines = data.decode('utf-8').splitlines(keepends=True)
    end = min(a.end, len(lines))
    selected = ''.join(lines[a.start - 1:end])
    record = {'argv': sys.argv, 'cwd': str(CWD), 'utc_start': start, 'utc_end': utc(),
              'path': a.path, 'repo': a.repo, 'ref': a.ref, **identity(data),
              'lines': len(lines), 'range': [a.start, end], 'full_read': a.start == 1 and end == len(lines),
              'rendered_bytes': len(selected.encode()), 'exit': 0,
              'stdout_capture': 'full requested range rendered to platform tool output',
              'stderr': '', 'evidence_level': 'READING', 'reference_execution': False}
    with (ROOT / 'reading-ledger.jsonl').open('a') as f:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')
    print(json.dumps({k: record[k] for k in ['path', 'ref', 'lines', 'range']}, ensure_ascii=False))
    print(selected, end='')
