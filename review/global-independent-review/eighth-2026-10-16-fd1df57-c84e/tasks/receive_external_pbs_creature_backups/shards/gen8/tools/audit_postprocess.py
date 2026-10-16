# Independently written static audit derivation, not execution of reference compiler.
import pathlib,json,sys,hashlib
b=pathlib.Path('/workspace/pokemon-essentials-clean-room/review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/receive_external_pbs_creature_backups');d=json.loads((b/'delegation/remaining-v1/gen8/readset.complete.json').read_text());rs={r['frozen']['id']:r for r in d['owned_records']};raws={p['id']:(pathlib.Path('/workspace/pokemon-essentials')/p['path']).read_bytes() for p in d['owned_primary_files']}
def fields(r):
 a,z=r['frozen']['byte_offsets_half_open'];v=raws[r['frozen']['identity_id']][a:z];assert hashlib.sha256(v).hexdigest()==r['source_unit_sha256'];out={}
 for line in v.decode().splitlines():
  if '=' in line and not line.startswith('#'):
   k,v=line.split('=',1);out.setdefault(k.strip(),[]).append(v.strip())
 return out
empty={'Name':'Unnamed','FormName':None,'MegaStone':None,'MegaMove':None,'UnmegaForm':0,'MegaMessage':0,'Types':['NORMAL'],'BaseStats':[1,1,1,1,1,1],'GenderRatio':'Female50Percent','GrowthRate':'Medium','BaseExp':100,'EVs':{'all_main_stats':0},'CatchRate':255,'Happiness':70,'Abilities':[],'HiddenAbilities':[],'Moves':[],'TutorMoves':[],'EggMoves':[],'EggGroups':['Undiscovered'],'HatchSteps':1,'Incense':None,'Offspring':[],'Height':0.1,'Weight':0.1,'Color':'Red','Shape':'Head','Habitat':'None','Category':'???','Pokedex':'???','Generation':0,'Flags':[],'WildItemCommon':[],'WildItemUncommon':[],'WildItemRare':[]}

import re,collections,copy

# Static audit derivation; no reference evaluator, compiler or serialized load.
evosrc=(pathlib.Path('/workspace/pokemon-essentials')/'Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb').read_text()
params={}
for block in evosrc.split('GameData::Evolution.register({')[1:]:
 m=re.search(r':id\s*=>\s*:(\w+)',block);p=re.search(r':parameter\s*=>\s*([^,\n]+)',block);params[m[1]]=p[1].strip() if p else None
def evo(f):
 out=[]
 for k in ['Evolutions','Evolution']:
  for v in f.get(k,[]):
   a=v.split(',');a += [None]*(3-len(a));t,m,p=a;pt=params[m];p=None if pt is None else int(p) if pt=='Integer' else p
   out.append([t,m,p,False])
 return out
objs=[];bases={};groups=collections.defaultdict(list)
for r in d['owned_records']:
 if r['frozen']['identity_id']!='P14':continue
 f=fields(r);sp=r['frozen']['section'];o={'id':r['frozen']['id'],'section':sp,'species':sp,'form':0,'fields':f,'evo':evo(f)};objs.append(o);bases[sp]=o
 groups[tuple(k for k,fc,pol,anc in r['complete_target_forward_object']['omitted'])].append(o['id'])
pre={}
for o in objs:
 for e in o['evo']:pre.setdefault(e[0],[o['species'],e[1],e[2],True])
for o in objs:
 if o['species'] in pre:o['evo'].append(copy.copy(pre[o['species']]))
for r in d['owned_records']:
 if r['frozen']['identity_id']!='P15':continue
 f=fields(r);sp,form=r['frozen']['section'].split(',');base=bases[sp];es=evo(f)
 if not es:es=copy.deepcopy(base['evo'])
 objs.append({'id':r['frozen']['id'],'section':r['frozen']['section'],'species':sp,'form':int(form),'fields':f,'evo':es})
pre={};formpre={}
for o in objs:
 for e in o['evo']:
  if e[3]:continue
  pre.setdefault(e[0],[o['species'],e[1],e[2],True])
  if o['form']>0:formpre.setdefault((e[0],o['form']),[o['species'],e[1],e[2],True])
added=[]
for o in objs:
 f=o['fields'];flags=f.get('Flags',bases[o['species']]['fields'].get('Flags',[]));flags=','.join(flags).split(',');defaults=[int(m[1]) for flag in flags if (m:=re.fullmatch('DefaultForm_(\\d+)',flag,re.I))];baseform=defaults[0] if defaults else o['form'];p=formpre.get((o['species'],baseform),pre.get(o['species']))
 if p:
  o['evo']=[e for e in o['evo'] if not e[3]]+[copy.copy(p)]
  pb=bases[p[0]]
  if not any(not e[3] and e[0]==o['species'] for e in pb['evo']):pb['evo'].append([o['species'],'None',None,False]);added.append((pb['id'],o['species']))
res={o['id']:{'forward': [e for e in o['evo'] if not e[3]],'prevolution':[e for e in o['evo'] if e[3]],'section':o['section']} for o in objs}
pathlib.Path('/tmp/gen8-postprocess.json').write_text(json.dumps(res,ensure_ascii=False,separators=(',',':')))
print('BASE_DEFAULT_GROUPS (complete omitted key lists; concrete values=already read Species ctor):')
for keys,ids in groups.items():print(len(ids),','.join(keys),'IDs_in_order='+','.join(str(int(x[-4:])) for x in ids))
print('FORM_FINAL_EVOLUTIONS every form; compact identical empty groups:')
for o in objs:
 if o['form'] and (res[o['id']]['forward'] or res[o['id']]['prevolution']):print(o['id'],o['section'],json.dumps({k:v for k,v in res[o['id']].items() if k!='section'},separators=(',',':')))
emptyforms=[o['id'] for o in objs if o['form'] and not res[o['id']]['forward'] and not res[o['id']]['prevolution']]
print('ALL_OTHER_FORMS_EXACT_EMPTY_FORWARD_AND_PREVO',','.join(emptyforms));print('ADDED_BASE_NONE_LINKS',added)
print('PARAM_METADATA_FOR_ALL_AUTHORED_METHODS', {m:params[m] for m in sorted({e[1] for o in objs for e in o['evo']})})
