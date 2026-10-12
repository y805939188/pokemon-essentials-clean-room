"""Read-only literal/table comparison for the M11 review; no game execution."""
import ast
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
REF = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
FORMAL = ROOT / 'deliverables/final-specification-set'
MINI = REF / 'Data/Scripts/017_Minigames'
started = datetime.now(timezone.utc).isoformat()
errors = []

def literal(path, key):
    text = path.read_text(encoding='utf-8-sig')
    text = re.sub(r'#[^\n]*', '', text)
    text = text[text.index(key):]
    start = text.index('[')
    level = 0
    for end in range(start, len(text)):
        level += (text[end] == '[') - (text[end] == ']')
        if level == 0:
            part = text[start:end + 1]
            part = re.sub(r':([A-Z][A-Z0-9_]*)', r'"\1"', part)
            return ast.literal_eval(part)
    raise ValueError(key)

def rows(path):
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if line.startswith('|'):
            yield n, [v.strip().strip('`') for v in line.strip('|').split('|')]

def check(name, actual, expected):
    if actual != expected:
        errors.append({'check': name, 'result': 'MISMATCH'})

reels = literal(MINI / '003_Minigame_SlotMachine.rb', 'ICONS_SETS')
symbols = ['樱桃', '小磁怪', '大舌贝', '皮卡丘', '可达鸭', '红 7', '蓝 7', '重玩']
reel_rows = list(rows(FORMAL / 'user-interface/wp69-slot-reels.md'))
position_rows = [(n, v) for n, v in reel_rows if v[0].isdigit()]
check('slot ordered row count', len(position_rows), 22)
for n, values in position_rows:
    index = int(values[0])
    check(f'slot line {n}', values[1:], [symbols[r[index]] for r in reels])
for n, values in reel_rows:
    if values[0] in symbols:
        index = symbols.index(values[0])
        check(f'slot frequencies line {n}', list(map(int, values[1:])), [r.count(index) for r in reels])

vf = literal(MINI / '004_Minigame_VoltorbFlip.rb', 'TILE_DISTRIBUTIONS')
vf_rows = [(n, list(map(int, v))) for n, v in rows(FORMAL / 'pokemon-rules/wp69-voltorb-layouts.md') if v[0].isdigit()]
check('voltorb ordered row count', len(vf_rows), 75)
expected_keys = [(level + 1, i + 1) for level, group in enumerate(vf) for i in range(len(group))]
check('voltorb row order', [(v[0], v[1]) for _, v in vf_rows], expected_keys)
for n, v in vf_rows:
    level, idx, zero, two, three, one, f, g, product = v
    check(f'voltorb parameters line {n}', [zero, two, three, f, g], vf[level - 1][idx - 1])
    check(f'voltorb remainder line {n}', one, 25 - zero - two - three)
    check(f'voltorb product line {n}', product, 2 ** two * 3 ** three)

mining = literal(MINI / '006_Minigame_Mining.rb', 'ITEMS =')
iron = literal(MINI / '006_Minigame_Mining.rb', 'IRON =')
mining_rows = [(n, v) for n, v in rows(FORMAL / 'user-interface/wp70-mining-data.md') if v[0].isdigit()]
item_rows = [(n, v) for n, v in mining_rows if len(v) == 6]
iron_rows = [(n, v) for n, v in mining_rows if len(v) == 4]
check('mining row count', len(item_rows), 61)
check('iron row count', len(iron_rows), 13)

def shape(pattern, width):
    return '/'.join(''.join('#' if x else '.' for x in pattern[i:i + width]) for i in range(0, len(pattern), width))

for n, v in item_rows:
    idx, identity, weight, size, occupied, mask = v
    source = mining[int(idx) - 1]
    name, probability, _, _, width, height, pattern = source
    check(f'mining line {n}', [identity, int(weight), size, int(occupied), mask], [name, probability, f'{width}×{height}', sum(pattern), shape(pattern, width)])
    check(f'mining mask length line {n}', len(pattern), width * height)
for n, v in iron_rows:
    idx, size, occupied, mask = v
    _, _, width, height, pattern = iron[int(idx) - 1]
    check(f'iron line {n}', [size, int(occupied), mask], [f'{width}×{height}', sum(pattern), shape(pattern, width)])
    check(f'iron mask length line {n}', len(pattern), width * height)
items = {}
current = None
for line in (REF / 'PBS/items.txt').read_text(encoding='utf-8-sig').splitlines():
    match = re.fullmatch(r'\[([^]]+)\]', line)
    if match:
        current = match[1]
        items[current] = {}
    elif current and '=' in line:
        key, value = line.split('=', 1)
        items[current][key.strip()] = value.strip()
identities = set(v[0] for v in mining)
for identity in identities:
    expected_pocket = '2' if identity in ('REVIVE', 'MAXREVIVE') else '1'
    check(f'item pocket {identity}', items.get(identity, {}).get('Pocket'), expected_pocket)

result = {
    'evidence_level': 'TOOL_VALIDATION',
    'execution_kind': 'literal_data_and_table_comparison_only',
    'started_at': started,
    'finished_at': datetime.now(timezone.utc).isoformat(),
    'python_version': sys.version,
    'command': ['python3', str(Path(__file__).resolve())],
    'counts': {'slot_positions': len(position_rows) * 3, 'voltorb_rows': len(vf_rows), 'mining_rows': len(item_rows), 'iron_rows': len(iron_rows), 'mining_identities': len(identities), 'mining_weight_total': sum(v[1] for v in mining)},
    'voltorb_max_fixed_product': max(v[-1] for _, v in vf_rows),
    'errors': errors,
    'exit_code': 1 if errors else 0,
    'side_effects': ['M11/data-validation.json only'],
    'behavior_execution': 'NOT_EXECUTED',
}
(OUT / 'data-validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'counts': result['counts'], 'errors': errors, 'behavior_execution': 'NOT_EXECUTED'}, ensure_ascii=False))
sys.exit(result['exit_code'])
