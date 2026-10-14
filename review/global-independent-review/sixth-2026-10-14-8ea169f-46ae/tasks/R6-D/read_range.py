"""Read only fixed audit inputs; persist presented ranges, never infer semantics."""
import argparse
import datetime
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-D'
EXPECTED = [('HEAD', '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'),
            ('HEAD^{tree}', '6ab3429170d2762607fbc2237014c3a160449fa1'),
            ('HEAD:deliverables/final-specification-set', '1046fbb657882e84b3dfc6d017943a9edf7782e5')]

def verify():
    for rev, wanted in EXPECTED:
        assert subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', rev], text=True).strip() == wanted
    ref = ROOT / 'reference/pokemon-essentials'
    assert subprocess.check_output(['git', '-C', str(ref), 'rev-parse', 'HEAD'], text=True).strip() == '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
    assert subprocess.check_output(['git', '-C', str(ref), 'rev-parse', 'HEAD^{tree}'], text=True).strip() == '7589c800b61ba13a13040ed0d686979b80a84fd0'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('start', type=int)
    parser.add_argument('end', type=int)
    args = parser.parse_args()
    verify()
    path = (ROOT / args.path).resolve()
    assert path.is_relative_to(ROOT)
    raw = path.read_bytes()
    lines = raw.decode('utf-8-sig').splitlines()
    if args.end == 0:
        args.end = len(lines)
    assert 1 <= args.start <= args.end <= len(lines)
    text = '\n'.join(f'{i}: {lines[i-1]}' for i in range(args.start, args.end+1))
    row = dict(timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(), path=str(path.relative_to(ROOT)),
               sha256=hashlib.sha256(raw).hexdigest(), start_line=args.start, end_line=args.end,
               total_lines=len(lines), stage='text_presented_pending_semantic_review', method='static_text_range')
    with (OUT / 'reading-ledger.jsonl').open('a') as stream:
        stream.write(json.dumps(row, ensure_ascii=False)+'\n')
    with (OUT / 'command-log.jsonl').open('a') as stream:
        stream.write(json.dumps(dict(operation='read_range', input=row, exit=0))+'\n')
    print(str(path.relative_to(ROOT)))
    print(text)
