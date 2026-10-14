"""Read fixed Git payloads in bounded, contiguous full-text segments; no source execution."""
from pathlib import Path
import datetime, hashlib, json, subprocess, sys

REPO = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
PREP = REPO / 'review/remediation-sixth-20261014-prepare'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def read(commit, path):
    data = git('show', f'{commit}:{path}')
    entry = git('ls-tree', commit, '--', path).decode().strip()
    return data, entry

def emit(kind, path, start, end):
    commit = REF if kind == 'source' else MAIN if kind == 'formal' else '469a268b92daed7b4d28d7fd0da75520cbb7228f'
    data, entry = read(commit, path)
    lines = data.decode('utf-8').splitlines(keepends=True)
    end = min(end, len(lines))
    payload = ''.join(lines[start - 1:end])
    row = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'cwd': str(REPO), 'argv': sys.argv, 'kind': kind, 'commit': commit,
           'path': path, 'git_entry': entry, 'bytes': len(data),
           'sha256': hashlib.sha256(data).hexdigest(), 'lines': len(lines),
           'start_line': start, 'end_line': end, 'returned_bytes': len(payload.encode()),
           'stdout_content_sha256': hashlib.sha256(payload.encode()).hexdigest(),
           'git_read_exit': 0, 'stderr': '', 'status': 'CONTENT_RETURNED_FOR_AUTHOR_READING'}
    with (OUT / 'reading-ledger.jsonl').open('a') as f:
        f.write(json.dumps(row, ensure_ascii=False) + '\n')
    print(json.dumps(row, ensure_ascii=False))
    print(payload, end='')

if __name__ == '__main__':
    emit(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
