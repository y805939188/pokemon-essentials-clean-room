"""Read-only input presenter. Writes only R6-F ledger/transcript, never certifies semantics."""
import argparse, datetime, hashlib, json, pathlib, subprocess

ROOT = pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-F'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
p = argparse.ArgumentParser()
p.add_argument('path')
p.add_argument('start', type=int)
p.add_argument('end', type=int)
p.add_argument('--reader', default='R6-F')
a = p.parse_args()
path = (ROOT / a.path).resolve()
assert path.is_relative_to(ROOT)
if path.is_relative_to(ROOT / 'reference/pokemon-essentials'):
    repo = ROOT / 'reference/pokemon-essentials'
    commit = REF
elif path.is_relative_to(ROOT / 'deliverables/final-specification-set') or path == ROOT / 'AGENTS.md':
    repo = ROOT
    commit = MAIN
else:
    raise ValueError('Input outside frozen permitted source/formal/instruction sets')
rel = path.relative_to(repo).as_posix()
raw = subprocess.check_output(['git', '-C', str(repo), 'show', f'{commit}:{rel}'])
assert path.read_bytes() == raw, 'Worktree differs from frozen input'
blob = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', f'{commit}:{rel}'], text=True).strip()
lines = raw.decode('utf-8-sig').splitlines()
assert 1 <= a.start <= a.end <= len(lines)
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
entry = {'reader': a.reader, 'path': a.path, 'commit': commit, 'git_blob': blob,
         'sha256': hashlib.sha256(raw).hexdigest(), 'start_line': a.start, 'end_line': a.end,
         'total_lines': len(lines), 'phase': 'PRESENTED_FOR_READING_NOT_SEMANTIC_PASS', 'time': stamp}
body = json.dumps(entry, ensure_ascii=False) + '\n' + '\n'.join(f'{i}: {lines[i-1]}' for i in range(a.start, a.end+1)) + '\n'
target = OUT / 'reads' / a.reader
target.mkdir(parents=True, exist_ok=True)
name = hashlib.sha256(a.path.encode()).hexdigest()[:12] + f'-{a.start}-{a.end}.txt'
(target / name).write_text(body)
with (OUT / f'reading-ledger{("-"+a.reader) if a.reader != "R6-F" else ""}.jsonl').open('a') as f:
    f.write(json.dumps(entry, ensure_ascii=False) + '\n')
print(body, end='')
