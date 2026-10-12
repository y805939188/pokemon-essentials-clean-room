"""Read-only textual data check; this does not execute reference behavior."""
import json
import re
from pathlib import Path

R = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B = Path(__file__).resolve().parents[5] / 'deliverables/final-specification-set'
MOVE = R / 'Data/Scripts/011_Battle/003_Move'

groups = [
    ('UseLastMoveUsed', '仿效'),
    ('UseMoveTargetIsAboutToUse', '抢先'),
    ('UseRandomMove', '挥指'),
    ('UseRandomMoveFromUserParty', '借助'),
    ('UseRandomUserMoveIfAsleep', '梦话'),
    ('ReplaceMoveThisBattleWithTargetLastMoveUsed', '模仿'),
    ('ReplaceMoveWithTargetLastMoveUsed', '写生'),
    ('TargetUsesItsLastUsedMoveAgain', '号令'),
    ('DisableTargetUsingDifferentMove', '安可'),
]

def read_source(path, identity):
    text = path.read_text()
    block = re.search(r'^class Battle::Move::' + identity + r'\s.*?(?=^class |\Z)', text, re.M | re.S).group()
    init = block.split('  def initialize', 1)[1].split('\n  def ', 1)[0]
    branch = '常'
    records = {}
    for line in init.splitlines():
        line = line.split('#', 1)[0]
        generation = re.search(r'MECHANICS_GENERATION\s*>=\s*(\d+)', line)
        if generation:
            branch = '≥' + generation.group(1)
        value = re.match(r'\s*"([A-Za-z0-9_]+)"', line)
        if value:
            assert value.group(1) not in records, (identity, 'duplicate', value.group(1))
            records[value.group(1)] = branch
    assert records, identity
    return records

def read_table(path, column_name):
    section = path.read_text().split('## 1.', 1)[1].split('\n## 2.', 1)[0]
    headers = None
    records = {}
    for line in section.splitlines():
        if not line.startswith('|'):
            continue
        cells = [s.strip() for s in line.strip('|').split('|')]
        if headers is None:
            headers = cells
            col = headers.index(column_name)
            continue
        if cells[col] in ('常', '≥6', '≥7'):
            assert cells[0] not in records
            records[cells[0]] = cells[col]
    return records

checks = []
for index, (identity, label) in enumerate(groups):
    if index < 7:
        source = MOVE / '012_MoveEffects_ChangeMoveEffect.rb'
        spec = B / 'combat-requirements/wp47-a-attributes-targeting-calling-data.md'
    else:
        source = MOVE / '013_MoveEffects_SwitchingActing.rb'
        spec = B / 'combat-requirements/wp47-b-control-items-coverage-data.md'
    actual, documented = read_source(source, identity), read_table(spec, label)
    missing = sorted(set(actual) - set(documented))
    extra = sorted(set(documented) - set(actual))
    different = sorted(k for k in actual.keys() & documented.keys() if actual[k] != documented[k])
    checks.append({
        'label': label,
        'source_path': str(source.relative_to(R)),
        'source_symbol': identity,
        'spec_path': str(spec.relative_to(B)),
        'constant_count': sum(v == '常' for v in actual.values()),
        'generation_addition_count': sum(v != '常' for v in actual.values()),
        'missing_from_spec': missing,
        'extra_in_spec': extra,
        'generation_mismatch': different,
        'matches': actual == documented,
    })
result = {'evidence_level': 'TOOL_VALIDATION', 'behavior_execution': False,
          'checks': checks, 'all_match': all(c['matches'] for c in checks)}
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(0 if result['all_match'] else 1)
