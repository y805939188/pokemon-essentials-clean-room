"""Static inventory only; never imports/executes reference or grades semantics.
Reads the two fixed AI directories and frozen formal block inventory; writes
this task's structural-denominator.json. Annotations are produced separately.
"""
import json, re, hashlib
from pathlib import Path
W=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
O=Path(__file__).resolve().parent
R=W/'reference/pokemon-essentials/Data/Scripts/011_Battle'
files=[]
for folder in ['005_AI','006_AI MoveEffects']:
    for p in sorted((R/folder).glob('*.rb')):
        raw=p.read_bytes(); lines=raw.decode('utf-8-sig').splitlines()
        starts=[]
        for i,line in enumerate(lines,1):
            if re.search(r'^\s*def\s|^Battle::AI::Handlers::\w+\.(?:add|copy|addIf)\(',line):
                starts.append({'start':i,'unit':line.strip(),'kind':'lexical_unit_start'})
        for n,u in enumerate(starts):
            u['envelope_end']=(starts[n+1]['start']-1 if n+1<len(starts) else len(lines))
        files.append({'path':str(p.relative_to(W)),'lines':len(lines),'sha256':hashlib.sha256(raw).hexdigest(),'units':starts,'status':'INVENTORY_ONLY'})
formal=json.loads((O.parent.parent/'inventory/formal-block-denominator.json').read_text())
blocks=[x for x in formal if re.search(r'/(?:wp51-|wp52-[abc]-)|/test-catalog/combat-requirements-wp49-51-52.md$',x['path'])]
(O/'structural-denominator.json').write_text(json.dumps({'source_files':files,'formal_blocks':blocks,'status':'INVENTORY_ONLY_NOT_SEMANTIC_PASS'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(files),'source_lines':sum(x['lines'] for x in files),'lexical_units':sum(len(x['units']) for x in files),'formal_blocks':len(blocks)}))
