"""Bound static registration inventory; no Ruby execution and no semantic verdicts."""
import json
import pathlib
import re

ROOT = pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = pathlib.Path(__file__).resolve().parent
BASE = 'reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects/'
FILES = ['004_AI_MoveEffects_MoveAttributes.rb', '005_AI_MoveEffects_MultiHit.rb', '006_AI_MoveEffects_Healing.rb']
pattern = re.compile(r'Battle::AI::Handlers::(\w+)\.(add|copy)\((.*?)\n', re.S)
units = []
for filename in FILES:
    path = BASE + filename
    content = (ROOT / path).read_text(encoding='utf-8-sig')
    for m in pattern.finditer(content):
        start = content.count('\n', 0, m.start()) + 1
        suffix = content[m.start():]
        end_off = suffix.find('\n)')
        if m.group(2) == 'copy':
            end_off = suffix.find(')')
            block = suffix[:end_off+1]
        else:
            block = suffix[:end_off+2]
        end = start + block.count('\n')
        identities = re.findall(r'"([^"]+)"', block if m.group(2) == 'copy' else m.group(3))
        units.append(dict(id=f'{filename[:3]}:{start}', path=path, start=start, end=end,
                          family=m.group(1), operation=m.group(2), identities=identities,
                          coverage_status='inventory_only'))
(OUT/'structural-inventory.json').write_text(json.dumps(units, ensure_ascii=False, indent=2)+'\n')
for file in FILES:
    group = [u for u in units if u['path'].endswith(file)]
    print(file, len(group), 'registration statements')
    for u in group:
        print(u['id'], u['family'], u['operation'], ','.join(u['identities']))
