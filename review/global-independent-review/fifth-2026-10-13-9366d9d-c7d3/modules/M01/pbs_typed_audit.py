"""Audit-only literal PBS checking. Does not import/execute Ruby or a behavioral model.
Field grammars are declarative tokens extracted from already-inspected schemas;
only primitive text, arity, numeric-domain and identifier relations are checked.
Semantic decisions are made separately; these results never mark review complete.
"""
import re,json,hashlib
from collections import defaultdict,Counter
from pathlib import Path
import review_state as s

def digest(v): return hashlib.sha256(v.encode()).hexdigest()
def lex(p):
 out=[];cur=None
 for n,line in enumerate(p.read_text(encoding='utf-8-sig').splitlines(),1):
  if not line.strip() or line.lstrip().startswith('#'):continue
  h=re.match(r'^\s*\[(.*)\]\s*(?:#.*)?$',line)
  if h:cur={'key':h[1],'line':n,'fields':[],'rows':[]};out.append(cur);continue
  m=re.match(r'^\s*(\w+)\s*=\s*(.*)$',line)
  if m and cur:cur['fields'].append({'key':m[1],'value':m[2],'line':n})
  elif cur:cur['rows'].append({'value':line.strip(),'line':n})
 return out
raw={str(p.relative_to(s.REF)):lex(p) for p in (s.REF/'PBS').rglob('*.txt')}
family_to_file={'town_map':'002_TownMap','types':'003_Type','abilities':'004_Ability','moves':'005_Move','items':'006_Item','berry_plants':'007_BerryPlant','pokemon':'008_Species','pokemon_forms':'008_Species','pokemon_metrics':'010_SpeciesMetrics','shadow_pokemon':'011_ShadowPokemon','ribbons':'012_Ribbon','trainer_types':'014_TrainerType','trainers':'015_Trainer','metadata':'016_Metadata','player_metadata':'017_PlayerMetadata','map_metadata':'018_MapMetadata','dungeon_tilesets':'019_DungeonTileset','dungeon_parameters':'020_DungeonParameters','phone':'021_PhoneMessage'}
# Safe text-only inventory. No eval/exec, Ruby interpreter, deserialization or file writes outside OUT.
schemas={};schema_lines={};schema_refs={}
for fam,fn in family_to_file.items():
 src=s.REF/'Data/Scripts/010_Data/002_PBS data'/ (fn+'.rb');entries={};anchors={};refs={}
 for n,l in enumerate(src.read_text().splitlines(),1):
  m=re.search(r'(?:"(\w+)"\s*=>|ret\["(\w+)"\]\s*=)\s*\[:\w+,\s*"([^"]+)"(.*)',l)
  if not m:continue
  key=m[1] or m[2];fmt=m[3];tail=m[4]
  entries[key]=fmt;anchors[key]=n;refs[key]=re.findall(r':([A-Z]\w*)',tail)
 if fam=='pokemon':
  entries['SectionName']='m';refs['SectionName']=[];anchors['SectionName']=57
  entries['Offspring']='*s';refs['Offspring']=[]
  entries['Evolutions']='*ses';refs['Evolutions']=['Evolution'];entries['Evolution']='^seS';refs['Evolution']=['Evolution']
  for k in ['PokedexForm','MegaStone','MegaMove','UnmegaForm','MegaMessage']:entries.pop(k,None)
 if fam=='pokemon_forms':
  entries['SectionName']='ev';refs['SectionName']=['Species'];anchors['SectionName']=55
  entries['Offspring']='*e';refs['Offspring']=['Species'];entries['Evolutions']='*ees';refs['Evolutions']=['Species','Evolution'];entries['Evolution']='^eeS';refs['Evolution']=['Species','Evolution']
  for k in ['Name','GenderRatio','GrowthRate','Incense']:entries.pop(k,None)
 schemas[fam]=entries;schema_lines[fam]=anchors;schema_refs[fam]=refs
# Finite identity collections from literal registrations, not class loading.
fixed={}
for p in (s.REF/'Data/Scripts/010_Data/001_Hardcoded data').glob('*.rb'):
 fixed[p.stem.split('_',1)[1]]=set(re.findall(r':id\s*=>\s*:(\w+)',p.read_text()))
fixed['Target']=fixed.get('Target',set());fixed['Weather']=fixed.get('Weather',set())
profiles={}
for profile in ['current','Gen 5 backup','Gen 6 backup','Gen 7 backup','Gen 8 backup']:
 prefix='PBS/' if profile=='current' else 'PBS/'+profile+'/'
 ids={}
 for dom,fam in [('Type','types'),('Ability','abilities'),('Move','moves'),('Item','items'),('Species','pokemon')]:
  ids[dom]={r['key'] for r in raw[prefix+fam+'.txt']}
 # Species compound identities are registered by forms as well as base records.
 for r in raw[prefix+'pokemon_forms.txt']:
  t=[x.strip() for x in r['key'].split(',')];ids['Species'].add(t[0]+'_'+str(int(t[1])))
 for dom,fam in [('TrainerType','trainer_types'),('Ribbon','ribbons')]:ids[dom]={r['key'] for r in raw['PBS/'+fam+'.txt']}
 ids.update(fixed);profiles[profile]=ids
# Shadow files, if explicitly installed into root, extend current identity sets.
shadow_ids={k:set(v) for k,v in profiles['current'].items()}
for dom,fam in [('Type','types'),('Move','moves'),('Item','items')]:
 for r in raw['PBS/Shadow Pokémon backup/'+fam+'_shadow_pkmn.txt']:shadow_ids[dom].add(r['key'])
profiles['Shadow Pokémon backup']=shadow_ids
inline={'Category':{'Physical','Special','Status'},'FieldUse':{'OnPokemon','Direct','TM','HM','TR'},'BattleUse':{'OnPokemon','OnMove','OnBattler','OnFoe','Direct'},'Gender':{'Male','male','M','m','0','Female','female','F','f','1','Unknown','unknown','Mixed','mixed','2'}}
# Actual files do not contain escaped CSV quotes/hash comments in the checked
# typed fields. Raw q payloads are never comma-split; anomalous s payloads are
# explicitly deferred instead of pretending Python CSV equals the reference.

def fields_for(fam,rec):
 d=dict(schemas.get(fam,{}));refs=dict(schema_refs.get(fam,{}))
 if fam=='metadata' and rec['key']!='0':return schemas['player_metadata'],schema_refs['player_metadata'],'player_metadata'
 return d,refs,fam

def atomcheck(val,code,ref,ids,key):
 optional=code.isupper();base=code.lower()
 if optional and not val:return {'kind':'absent_optional','ok':True}
 if base in 'uvix':
  match=bool(re.fullmatch(r'\d+' if base in 'uv' else r'-?\d+',val));ok=match and (base!='v' or int(val)>0)
  return {'kind':{'u':'nonnegative_integer','v':'positive_integer','i':'signed_integer','x':'signed_optional_integer'}.get(base),'ok':ok,'value':int(val) if match else None}
 if base=='f':return {'kind':'restricted_unsigned_decimal','ok':bool(re.fullmatch(r'[0-9]*\.[0-9]*|[0-9]+',val)),'text':val}
 if base=='b':return {'kind':'boolean','ok':val.lower() in ['true','false','yes','no','1','0'],'text':val}
 if base=='e':
  names=inline.get(key) if key in inline else ids.get(ref,set())
  return {'kind':'registered_reference' if ref else 'finite_enum','domain':ref or key,'ok':val in names,'identity':val}
 if base=='m':return {'kind':'symbol_identity','ok':bool(re.fullmatch(r'\w+',val)),'identity':val}
 if base in 'sq':return {'kind':'csv_text' if base=='s' else 'raw_text','ok':True,'sha256':digest(val),'length':len(val)}
 return {'kind':'unhandled_descriptor','ok':False,'descriptor':code}
allrows=[];exceptions=[];values=defaultdict(lambda:defaultdict(Counter));byfamily=defaultdict(Counter)
inspection=s.read('pbs-data-inspection.json')
for fi in inspection['files']:
 path=fi['path'];fam=fi['family'];parts=path.split('/');profile=parts[1] if len(parts)>2 else 'current';ids=profiles.get(profile,profiles['current'])
 if fam not in schemas:continue
 output=[]
 for rec in raw[path]:
  schema,refs,sfam=fields_for(fam,rec);checks=[]
  for p in [{'key':'SectionName','line':rec['line'],'value':rec['key']},*rec['fields']]:
   key,val=p['key'],p['value'];fmt=schema.get(key);check={'field':key,'line':p['line'],'payload_sha256':digest(val),'schema_family':sfam,'schema_line':schema_lines[sfam].get(key),'consumer_semantic_status':'not_reviewed'}
   if fmt is None:check.update(kind='unknown_property',ok=False);exceptions.append(dict(path=path,record=rec['key'],**check));checks.append(check);continue
   prefix=fmt[0] if fmt[0] in '*^' else '';body=fmt[1:] if prefix else fmt
   check['repeat_semantics']='repeat_field_occurrences' if prefix=='^' else 'repeat_groups_on_one_line' if prefix=='*' else 'single_group'
   if body=='q':tokens=[val]
   elif '"' in val or '#' in val:
    check.update(kind='special_csv_text_requires_individual_review',ok=False);exceptions.append(dict(path=path,record=rec['key'],**check));checks.append(check);continue
   else:tokens=[x.strip() for x in val.split(',')]
   # Match all provided atoms; missing required atoms explicitly recorded.
   if prefix=='*':expected=len(body)*((len(tokens)+len(body)-1)//len(body));codes=(body*((expected+len(body)-1)//len(body)))[:expected]
   else:codes=body
   toks=tokens+[None]*max(0,len(codes)-len(tokens));results=[]
   doms=iter(refs.get(key,[]));perpos=[next(doms,None) if c.lower()=='e' else None for c in body]
   for ix,code in enumerate(codes):
    v=toks[ix]
    if v is None:v=''
    results.append(atomcheck(v,code,perpos[ix%len(body)],ids,key))
   check['atoms']=results;check['ignored_tail_atom_count']=max(0,len(tokens)-len(codes));check['ok']=all(x['ok'] for x in results);check['kind']='typed_literal_validation'
   if not check['ok']:exceptions.append(dict(path=path,record=rec['key'],**check))
   byfamily[fam][key]+=1
   # Finite summaries are inspection prompts only, not semantic completion.
   if key not in ['Name','NamePlural','PortionName','PortionNamePlural','FormName','Description','Pokedex','Category','LoseText','StorageCreator','Intro','IntroMorning','IntroAfternoon','IntroEvening','Body','Body1','Body2','BattleRequest','BattleRemind','End','Moves','TutorMoves','EggMoves','Evolution','Evolutions','EVs','BaseStats','Point']:
    values[fam][key][val]+=1
   checks.append(check)
  output.append({'record_key':rec['key'],'header_line':rec['line'],'fields':checks,'semantic_status':'typed_literals_checked_consumer_contracts_pending'})
 name='pbs-typed-'+path[4:].replace('/','--').replace(' ','_')+'.json'
 s.write(name,{'schema_version':'gr5.review.v1','path':path,'version':s.R,'git_blob':fi['git_blob'],'profile':profile,'boundary':'literal data validity and identifier resolution only, no behavioral execution and no semantic-complete assertion','records':output})
 allrows.append({'path':path,'profile':profile,'record_count':len(output),'typed_fields':sum(len(x['fields']) for x in output),'status':'typed_validation_only'})
s.write('pbs-typed-audit.json',{'schema_version':'gr5.review.v1','module':'M01','source_baseline':s.R,'boundary':'No Ruby/reference/model execution; all per-field literal checks require reviewer interpretation and consumer mappings before completion. False results may be parser approximation limits.','files':allrows,'exceptions':exceptions,'value_sets':{f:{k:dict(v) for k,v in kv.items()} for f,kv in values.items()}})
print('Typed files',len(allrows),'exceptions',len(exceptions))
for x in exceptions[:30]:print(x['path'],x['record'],x['field'],x['line'],[(a.get('domain'),a.get('identity'),a.get('kind')) for a in x.get('atoms',[]) if not a['ok']])
