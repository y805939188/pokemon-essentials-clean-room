"""Recover complete matching PBS records and compare finite bundled alternatives."""
from pathlib import Path
import re, json, hashlib
R=Path('/workspace/pokemon-essentials')
def records(p):
    lines=p.read_text(encoding='utf-8-sig').splitlines()
    starts=[i for i,l in enumerate(lines) if re.fullmatch(r'\[[^\]]+\]',l)]
    return [(lines[a][1:-1],a+1,(starts[i+1] if i+1<len(starts) else len(lines)),lines[a:(starts[i+1] if i+1<len(starts) else len(lines))]) for i,a in enumerate(starts)]
effects=set()
for f in ['008_MoveEffects_MoveAttributes.rb','012_MoveEffects_ChangeMoveEffect.rb']:
    effects.update(re.findall(r'^class Battle::Move::(\w+)',(R/'Data/Scripts/011_Battle/003_Move'/f).read_text(),re.M))
effects.update(['UserSwapBaseAtkDef','UserTargetSwapBaseSpeed','UserTargetAverageBaseAtkSpAtk','UserTargetAverageBaseDefSpDef','SetUserTypesBasedOnEnvironment','SetUserTypesToResistLastAttack','SetUserTypesToTargetTypes','SetUserTypesToUserMoveType','SetTargetTypesToPsychic','SetTargetTypesToWater','AddGhostTypeToTarget','AddGrassTypeToTarget','UserLosesFireType','HigherPriorityInGrassyTerrain'])
prior={}
for p in sorted((R/'PBS').rglob('*.txt')):
    if p.name not in ['moves.txt','items.txt','types.txt','moves_shadow_pkmn.txt','items_shadow_pkmn.txt','types_shadow_pkmn.txt']: continue
    for name,a,b,lines in records(p):
        text='\n'.join(lines)
        if p.name.startswith('moves'):
            hit=any(re.fullmatch(r'FunctionCode\s*=\s*'+re.escape(effect),l) for l in lines for effect in effects)
        elif p.name.startswith('items'): hit='NaturalGift_' in text
        else: hit=True
        if not hit: continue
        # Current/backup exact bytes still have their identity and selection,
        # while distinct variants are displayed in full to read.
        digest=hashlib.sha256(text.encode()).hexdigest()
        here=f'{p.relative_to(R)}:{a}-{b} [{name}]'
        if digest in prior:
            print(f'IDENTICAL_RECORD {here} = {prior[digest]} sha256={digest}')
        else:
            print(f'RECORD {here} sha256={digest}')
            print(text)
            prior[digest]=here
