"""Full reference-presence joins; no compiler, gameplay or compatibility model."""
import json
import pathlib
import re
from read_range import ROOT, OUT, verify

verify()
REF=ROOT/'reference/pokemon-essentials'
inputs=[json.loads(p.read_text()) for p in sorted(OUT.glob('structure-*.json'))]
data_atoms=[]
for d in inputs:
    if d['family']=='facility_pokemon':
        for row in d['unsectioned']:
            a=row['atoms']
            data_atoms.append(dict(path=d['path'],line=row['line'],domain='species',identity=a[0]))
            if a[1]:data_atoms.append(dict(path=d['path'],line=row['line'],domain='items',identity=a[1]))
            for m in a[4].split(',')[:4]:
                if m.strip():data_atoms.append(dict(path=d['path'],line=row['line'],domain='moves',identity=m.strip()))
    elif d['family']=='trainers':
        for r in d['records']:
            for field in r['fields']:
                dom={'Pokemon':'species','Items':'items','Item':'items','Ball':'items','Moves':'moves'}.get(field['key'])
                if dom:
                    vs=field['value'].split(',')
                    if field['key']=='Pokemon':vs=vs[:1]
                    for v in vs:data_atoms.append(dict(path=d['path'],line=field['line'],domain=dom,identity=v.strip()))
    elif d['family']=='metadata':
        for r in d['records']:
            for field in r['fields']:
                if field['key']=='StartItemStorage':
                    for v in field['value'].split(','):data_atoms.append(dict(path=d['path'],line=field['line'],domain='items',identity=v.strip()))
    elif d['family']=='regional_dexes':
        for r in d['records']:
            for row in r['rows']:
                for v in row['value'].split(','):data_atoms.append(dict(path=d['path'],line=row['line'],domain='species',identity=v.strip()))

profiles=[]
for prefix in ['PBS','PBS/Gen 5 backup','PBS/Gen 6 backup','PBS/Gen 7 backup','PBS/Gen 8 backup']:
    catalogs={}
    for domain,filename in [('species','pokemon.txt'),('items','items.txt'),('moves','moves.txt')]:
        catalogs[domain]=set(re.findall(r'^\[([^]]+)\]',(REF/prefix/filename).read_text(encoding='utf-8-sig'),re.M))
    for key in re.findall(r'^\[([^]]+)\]',(REF/prefix/'pokemon_forms.txt').read_text(encoding='utf-8-sig'),re.M):
        species,form=key.split(',');catalogs['species'].add(species.strip()+'_'+str(int(form.strip())))
    unresolved=[a for a in data_atoms if a['identity'] not in catalogs[a['domain']]]
    profiles.append(dict(profile=prefix,atoms_checked=len(data_atoms),unresolved_count=len(unresolved),unresolved=unresolved,
        interpretation='Presence only. Backups are not activated or compiled, existing runtime tables not changed; mechanics/configuration, legacy aliases and full compatibility remain unproved.'))
(OUT/'cross-profile-special-references.json').write_text(json.dumps(profiles,ensure_ascii=False,indent=2)+'\n')
with (OUT/'command-log.jsonl').open('a') as f:
    f.write(json.dumps(dict(operation='cross_profile_references.py',input_reference='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
        output='cross-profile-special-references.json',atoms=len(data_atoms),profiles=5,source_execution=0,exit=0))+'\n')
for p in profiles:print(p['profile'],p['atoms_checked'],p['unresolved_count'],p['unresolved'])
