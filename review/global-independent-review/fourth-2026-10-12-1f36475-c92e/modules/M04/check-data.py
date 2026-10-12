"""Read-only textual contract audit; does not execute reference behavior."""
from pathlib import Path
import re, json
R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B=Path('deliverables/final-specification-set')
def pbs(path):
    entries={}; current=None
    for n,line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(),1):
        line=line.strip()
        if line.startswith('[') and line.endswith(']'):
            current=line[1:-1]; assert current not in entries
            entries[current]={'_line':n}
        elif current and '=' in line and not line.startswith('#'):
            k,v=line.split('=',1); entries[current][k.strip()]=v.strip()
    return entries
def rows(path):
    return [[v.strip() for v in line.strip().strip('|').split('|')] for line in path.read_text().splitlines() if line.startswith('|')]
forms=pbs(R/'PBS/pokemon_forms.txt')
mega={k:v for k,v in forms.items() if 'MegaStone' in v or 'MegaMove' in v}
actual={}
for row in rows(B/'pokemon-rules/wp22-transformation-data.md'):
    if len(row)==4 and row[0].isupper() and row[1].isdigit():
        key=f'{row[0]},{row[1]}'
        actual[key]=(row[2].split()[-1],row[3].replace('／',','))
expected={k:(v.get('MegaStone',v.get('MegaMove')),v['BaseStats']) for k,v in mega.items()}
assert actual==expected, {'mega_missing':sorted(expected.keys()-actual.keys()),'different':[k for k in expected.keys()&actual.keys() if expected[k]!=actual[k]]}
assert len(actual)==48
items=pbs(R/'PBS/items.txt')
assert {k for k,v in items.items() if 'MegaStone' in v.get('Flags','').split(',')}=={v['MegaStone'] for v in mega.values() if 'MegaStone' in v}
assert {k for k,v in items.items() if 'MegaRing' in v.get('Flags','').split(',')}=={'MEGARING'}
sh=pbs(R/'PBS/Shadow Pokémon backup/shadow_pokemon.txt')
shrows={row[0]:(row[1],row[2].replace('／',',')) for row in rows(B/'pokemon-rules/wp23-shadow-data-and-vectors.md') if len(row)==3 and row[0].isupper() and row[1].isdigit()}
assert shrows=={k:(v.get('GaugeSize','4000'),v.get('Moves','')) for k,v in sh.items()}
assert len(shrows)==131
shadow_text=(R/'Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb').read_text()
source_natures={name:tuple(map(int,re.findall(r'\d+',numbers))) for name,numbers in re.findall(r':([A-Z]+)\s*=>\s*\[([^\]]+)\]',shadow_text)}
spec_natures={row[0]:tuple(map(int,row[1:])) for row in rows(B/'pokemon-rules/wp23-shadow-data-and-vectors.md') if len(row)==5 and row[0].isupper() and all(x.isdigit() for x in row[1:])}
assert len(source_natures)==25 and spec_natures==source_natures
form_text=(R/'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb').read_text()
source_shapes={}
for k,block in re.findall(r'spot([1-4]) = \[(.*?)\n  \]',form_text,re.S):
    source_shapes['S'+k]=[set(i for i,v in enumerate(re.findall(r'[01]',line)) if v=='1') for line in re.findall(r'\[([^\]]+)\]',block)]
def interval(s):
    nums=list(map(int,s.split('…')))
    return range(nums[0],nums[-1]+1)
spec_shapes={}
for row in rows(B/'pokemon-rules/wp21-dynamic-forms-and-display.md'):
    if len(row)==2 and row[0] in source_shapes:
        ys={}
        for part in row[1].split('；'):
            y,x=part.split('→')
            for yy in interval(y):ys[yy]=set(interval(x))
        spec_shapes[row[0]]=[ys[i] for i in range(len(ys))]
assert spec_shapes==source_shapes
print(json.dumps({'evidence_level':'TOOL_VALIDATION','behavior_execution':False,'checks':{'mega_targets':len(actual),'mega_stones':47,'mega_ring':'MEGARING','shadow_species':len(shrows),'heart_nature_rows':len(source_natures),'spinda_shapes':{k:{'rows':len(v),'marked_points':sum(map(len,v))} for k,v in source_shapes.items()}},'result':'MATCH','source_data_anchors':{'mega':{k:v['_line'] for k,v in mega.items()},'shadow_selected':{k:sh[k]['_line'] for k in ['GROWLITHE','SNORUNT','LUGIA']}}},ensure_ascii=False,indent=2))
