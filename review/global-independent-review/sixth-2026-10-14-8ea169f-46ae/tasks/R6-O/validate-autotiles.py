from pathlib import Path
import json
import re
import datetime
out = Path('review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-O')
inv = json.loads((out / 'inventory.json').read_text())
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
lines = Path(inv['sources'][36]['path']).read_text().splitlines()
values = [int(x) for x in re.findall(r'\d+', '\n'.join(lines[21:37]))]
mismatches = []
subsets = set()
for mask in range(256):
    n, e, s, w = [bool(mask & bit) for bit in [1, 4, 16, 64]]
    ne, se, sw, nw = [int(bool(mask & bit)) for bit in [2, 8, 32, 128]]
    cardinal = (n, e, s, w)
    subsets.add(cardinal)
    if sum(cardinal) == 0:
        value = 46
    elif sum(cardinal) == 1:
        value = [44, 43, 42, 45][cardinal.index(True)]
    elif cardinal == (True, False, True, False):
        value = 32
    elif cardinal == (False, True, False, True):
        value = 33
    elif cardinal == (True, True, False, False):
        value = 41 - ne
    elif cardinal == (False, True, True, False):
        value = 35 - se
    elif cardinal == (False, False, True, True):
        value = 37 - sw
    elif cardinal == (True, False, False, True):
        value = 39 - nw
    elif cardinal == (True, True, True, False):
        value = 19 - ne - 2 * se
    elif cardinal == (True, True, False, True):
        value = 31 - 2 * ne - nw
    elif cardinal == (True, False, True, True):
        value = 27 - sw - 2 * nw
    elif cardinal == (False, True, True, True):
        value = 23 - se - 2 * sw
    else:
        value = 15 - nw - 2 * ne - 4 * se - 8 * sw
    if value != values[mask]:
        mismatches.append({'mask': mask, 'formula': value, 'literal': values[mask]})
result = {
    'id': 'O-LIT-AUTOTILE256',
    'start_utc': start,
    'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'argv': ['python3', str(out / 'validate-autotiles.py')],
    'exit': 0,
    'stdout': f'256 of {len(values)} equal; mismatches={len(mismatches)}',
    'stderr': '',
    'grade': ['TOOL_VALIDATION', 'INDEPENDENT_FINITE_ARITHMETIC'],
    'source': inv['sources'][36]['path'],
    'source_lines': [21, 38],
    'formal': inv['formal'][6]['path'],
    'formal_lines': [245, 262],
    'cases': 256,
    'cardinal_subsets': len(subsets),
    'matched': len(values) == 256 and not mismatches,
    'mismatches': mismatches,
    'reference_execution': 0,
    'gameplay_model_execution': 0,
    'host': 0,
    'limitation': 'Finite independently entered formal arithmetic compared to literal array; no source function, generator, renderer, map or pixel execution.'
}
(out / 'finite-autotile256.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
with (out / 'command-log.jsonl').open('a') as log:
    log.write(json.dumps({'at': start, 'command': result['argv'], 'result': result, 'earlier_failure': 'Inline version SyntaxError and245 before execution; no result or file writes from that attempt.'}, ensure_ascii=False) + '\n')
rows = [json.loads(x) for x in (out / 'reverse-matrix.jsonl').read_text().splitlines()]
for row in rows:
    if row['formal'] == result['formal'] and 245 <= row['lines'][0] <= 262:
        row['finite_validation'] = 'finite-autotile256.json all256 independent arithmetic, no reference/host'
(out / 'reverse-matrix.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows))
print(result['stdout'])
