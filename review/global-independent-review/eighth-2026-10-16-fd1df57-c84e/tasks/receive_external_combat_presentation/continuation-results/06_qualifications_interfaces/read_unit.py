"""Inert, bounded reading and identity records. Does not execute reviewed material."""
from pathlib import Path
import sys, json, hashlib, subprocess, datetime

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / '.git').exists())
ROOT = REPO / 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
CONTRACT = ROOT / 'tasks/receive_external_combat_presentation/continuation/06_qualifications_interfaces/readset.complete.json'

def identity(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()}

def main():
    path = Path(sys.argv[1])
    if not path.is_absolute():
        path = Path.cwd() / path
    raw = path.read_bytes()
    lines = raw.decode('utf-8').splitlines(keepends=True)
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end = int(sys.argv[3]) if len(sys.argv) > 3 else len(lines)
    assert 1 <= start <= end <= len(lines), (start, end, len(lines))
    output = ''.join(f'{i}: {lines[i-1]}' for i in range(start, end+1))
    event = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'path': str(path), **identity(raw), 'total_lines': len(lines),
             'shown_lines': [start, end], 'output_sha256': hashlib.sha256(output.encode()).hexdigest(),
             'credit': 'PRESENTED_ONLY; reviewer must separately record semantic reception',
             'reviewed_code_executed': False}
    with (HERE / 'presentation-events.jsonl').open('a') as f:
        f.write(json.dumps(event, ensure_ascii=False) + '\n')
    print(json.dumps(event, ensure_ascii=False))
    print(output, end='')

if __name__ == '__main__':
    main()
