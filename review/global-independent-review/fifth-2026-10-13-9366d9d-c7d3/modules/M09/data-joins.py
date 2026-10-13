"""Read-only identifier and ordered-record joins; no reference code execution.
The report is an audit aid, not a semantic-review verdict or behavior model.
"""
from pathlib import Path
from collections import Counter
import re,json
R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
def sections(path):
    out=[]; row=None
    for line,s in enumerate(path.read_text(encoding='utf-8-sig').splitlines(),1):
        s=s.strip()
        if s.startswith('['):
            row={'key':s[1:-1],'line':line};out.append(row)
        elif row is not None and '=' in s and not s.startswith('#'):
            k,v=s.split('=',1);k=k.strip();v=v.strip()
            row[k]=row[k]+' | '+v if k=='Evolution' and k in row else v
    return out
ids={kind:{r['key']:r for r in sections(R/'PBS'/name)} for kind,name in [('species','pokemon.txt'),('moves','moves.txt'),('items','items.txt'),('types','trainer_types.txt')]}
nature=(R/'Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb').read_text()
natures=set(re.findall(r':id\s*=>\s*:(\w+)',nature))
pairs=[('battle_tower_trainers.txt','battle_tower_pokemon.txt'),('cup_pika_trainers.txt','cup_pika_pkmn.txt'),('cup_poke_trainers.txt','cup_poke_pkmn.txt'),('cup_little_trainers.txt','cup_little_pkmn.txt'),('cup_fancy_trainers_single.txt','cup_fancy_pkmn_single.txt'),('cup_fancy_trainers.txt','cup_fancy_pkmn.txt')]
usedspecies=set();usedtypes=set()
for tf,pf in pairs:
    templates=[];invalid=[];evcounts=Counter();evids=set();returns=[]
    for ln,s in enumerate((R/'PBS'/pf).read_text(encoding='utf-8-sig').splitlines(),1):
        if not s.strip() or s.lstrip().startswith('#'):continue
        f=[v.strip() for v in s.split(';')];i=len(templates);templates.append(f)
        if len(f)!=5:invalid.append([i,ln,'field_count',len(f)]);continue
        sp,it,na,ev,mv=f;usedspecies.add(sp)
        for kind,val in [('species',sp),('items',it)]:
            if val and val not in ids[kind]:invalid.append([i,ln,kind,val])
        if na not in natures:invalid.append([i,ln,'nature',na])
        moves=[m.strip() for m in mv.split(',') if m.strip()]
        for m in moves:
            if m not in ids['moves']:invalid.append([i,ln,'move',m])
        if 'RETURN' in moves:returns.append(i)
        evlist=ev.split(',') if ev else [];evcounts[len(evlist)]+=1;evids.update(evlist)
    trainers=sections(R/'PBS'/tf);badrefs=[];dups=[];lengths=Counter()
    for i,t in enumerate(trainers):
        usedtypes.add(t['Type']);ns=[int(n.strip()) for n in t['PokemonNos'].split(',')];lengths[len(ns)]+=1
        if t['Type'] not in ids['types']:badrefs.append([i,'type',t['Type']])
        for n in ns:
            if n<0 or n>=len(templates):badrefs.append([i,'index',n])
        repeat={k:v for k,v in Counter(ns).items() if v>1}
        if repeat:dups.append([i,repeat])
    print(json.dumps({'templates':pf,'records':len(templates),'identifier_errors':invalid,'ev_entry_counts':dict(evcounts),'ev_ids':sorted(evids),'return_indexes':returns,'trainers':tf,'trainer_records':len(trainers),'bad_references':badrefs,'roster_length_distribution':dict(sorted(lengths.items())),'duplicate_roster_indexes':dups},ensure_ascii=False))
print('USED TRAINER TYPE DATA (SkillLevel default follows BaseMoney, whose default is 30)')
for k in sorted(usedtypes):
    t=ids['types'].get(k,{});print(k,t.get('line'), 'BaseMoney='+t.get('BaseMoney','<default>'),'SkillLevel='+t.get('SkillLevel','<default>'),'Flags='+t.get('Flags','<none>'))
print('USED SPECIES RESTRICTION INPUTS (no rule executed)')
for k in sorted(usedspecies):
    s=ids['species'].get(k,{})
    print(k,s.get('line'),';'.join(f'{x}={s.get(x,"<absent>")}' for x in ['BaseStats','Abilities','Height','Weight','Evolution']))
