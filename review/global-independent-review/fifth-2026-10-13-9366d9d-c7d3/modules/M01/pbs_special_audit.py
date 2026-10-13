"""Audit-only ordered records/primitive identifier relations for special PBS.
No reference/compiler/model execution. Raw prose is hashed. Findings require
manual source/contract comparison, not automated admission of these outputs.
"""
import re,hashlib
from collections import Counter,defaultdict
import review_state as s
D=s.read('pbs-data-inspection.json');files=D['files'];ROOT=s.REF

def h(v):return hashlib.sha256(v.encode()).hexdigest()
def records(path):return s.read('pbs-records-'+path[4:].replace('/','--').replace(' ','_')+'.json')
def idset(path):return {r['record_key'] for r in records(path)['records']}
ids={'species':idset('PBS/pokemon.txt'),'items':idset('PBS/items.txt'),'moves':idset('PBS/moves.txt'),'trainer_types':idset('PBS/trainer_types.txt')}
for r in records('PBS/pokemon_forms.txt')['records']:
 k=[v.strip() for v in r['record_key'].split(',')];ids['species'].add(k[0]+'_'+str(int(k[1])))
ids['natures']=set(re.findall(r':id\s*=>\s*:(\w+)',(ROOT/'Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb').read_text()))
ids['encounter_types']=set(re.findall(r':id\s*=>\s*:(\w+)',(ROOT/'Data/Scripts/010_Data/001_Hardcoded data/013_EncounterType.rb').read_text()))
pools={};exceptions=[];out=[]
evkeys={'HP':'HP','ATK':'ATTACK','DEF':'DEFENSE','SA':'SPECIAL_ATTACK','SPATK':'SPECIAL_ATTACK','SD':'SPECIAL_DEFENSE','SPDEF':'SPECIAL_DEFENSE','SPD':'SPEED'}
for f in files:
 if f['family']!='facility_pokemon':continue
 d=records(f['path']);rows=[]
 for ix,r in enumerate(d['unsectioned_rows']):
  t=r['data_value'].split(';');row={'pool_index':ix,'line':r['line'],'raw_sha256':r['sha256'],'separator_field_count':len(t),'consumer_semantic_status':'not_reviewed'}
  if len(t)<5:exceptions.append(dict(path=f['path'],**row));rows.append(row);continue
  atoms=[x.strip() for x in t[:3]]
  row['references']={dom:{'identity':value,'defined':value in ids[dom]} for dom,value in zip(['species','items','natures'],atoms)}
  ev=t[3].split(',');mapped=[evkeys.get(v.upper()) for v in ev];row['effort_items']=[v for v in mapped if v];row['ignored_effort_tokens']=[v for v in ev if v.upper() not in evkeys]
  row['duplicate_effort_items']={k:v for k,v in Counter(row['effort_items']).items() if v>1}
  move_tokens=t[4].split(',');row['moves_supplied']=move_tokens;row['moves_in_first_four']=[v for v in move_tokens[:4] if v in ids['moves']];row['ignored_move_atoms']=[v for v in move_tokens[:4] if v not in ids['moves']]
  row['additional_semicolon_fields']=len(t)-5;row['additional_move_atoms']=max(len(move_tokens)-4,0)
  if not all(x['defined'] or (k=='items' and not x['identity']) for k,x in row['references'].items()) or row['ignored_effort_tokens'] or any(row['ignored_move_atoms']) or row['duplicate_effort_items'] or not row['moves_in_first_four'] or row['additional_semicolon_fields'] or row['additional_move_atoms']:exceptions.append(dict(path=f['path'],**row))
  rows.append(row)
 pools[f['path']]=rows
 name='pbs-special-'+f['path'][4:].replace('/','--').replace(' ','_')+'.json';s.write(name,{'schema_version':'gr5.review.v1','path':f['path'],'version':s.R,'git_blob':f['git_blob'],'records':rows,'boundary':'All five ordered fields resolved as inert data; source/consumer semantic decision separate.'});out.append({'path':f['path'],'records':len(rows),'family':f['family']})
# Preserve physical headers separately from ordinal identities used by consumers.
for f in files:
 if f['family']!='facility_trainers':continue
 d=records(f['path']);text=(ROOT/f['path']).read_text(encoding='utf-8-sig').splitlines();rows=[]
 poolname=f['path'].replace('battle_tower_trainers','battle_tower_pokemon').replace('_trainers','_pkmn');pool=pools[poolname]
 for ix,r in enumerate(d['records']):
  vals={v['key']:text[v['line']-1].split('=',1)[1].strip() for v in r['properties']};nums=[int(v) for v in vals.get('PokemonNos','').split(',') if v]
  row={'ordinal':ix,'header_text':r['record_key'],'lines':r['lines'],'type_identity':vals.get('Type'),'type_defined':vals.get('Type') in ids['trainer_types'],'candidate_indices':nums,'candidate_index_min':min(nums) if nums else None,'candidate_index_max':max(nums) if nums else None,'candidate_duplicates':{k:v for k,v in Counter(nums).items() if v>1},'all_candidate_indices_in_paired_pool':all(0<=n<len(pool) for n in nums),'paired_pool':poolname,'text_properties':[{ 'field':k,'sha256':h(v),'contains_quote':'"' in v,'starts_plain_quote':v.startswith('"'),'ends_plain_quote':v.endswith('"')} for k,v in vals.items() if k not in ['Type','PokemonNos']],'missing_fields':list(set(['Type','Name','PokemonNos','BeginSpeech','EndSpeechWin','EndSpeechLose'])-set(vals)),'consumer_semantic_status':'not_reviewed'}
  if not row['type_defined'] or not row['all_candidate_indices_in_paired_pool'] or row['candidate_duplicates'] or row['missing_fields']:exceptions.append(dict(path=f['path'],**row))
  rows.append(row)
 s.write('pbs-special-'+f['path'][4:]+'.json',{'schema_version':'gr5.review.v1','path':f['path'],'version':s.R,'git_blob':f['git_blob'],'records':rows,'boundary':'Header text is not assumed consumed as a numeric trainer ID. Candidate references checked against paired existing data only.'});out.append({'path':f['path'],'records':len(rows),'family':f['family']})
for f in files:
 if f['family']!='encounters':continue
 d=records(f['path']);profile=f['path'].split('/')[1] if '/Gen ' in f['path'] else None
 species=idset('PBS/'+(profile+'/' if profile else '')+'pokemon.txt')
 for r in records('PBS/'+(profile+'/' if profile else '')+'pokemon_forms.txt')['records']:
  k=[v.strip() for v in r['record_key'].split(',')];species.add(k[0]+'_'+str(int(k[1])))
 rows=[]
 for r in d['records']:
  sec={'header':r['record_key'],'lines':r['lines'],'methods':[],'consumer_semantic_status':'not_reviewed'};cur=None
  for line in r['raw_rows']:
   atoms=[x.strip() for x in line['data_value'].split(',')]
   if atoms[0] in ids['encounter_types']:
    cur={'identity':atoms[0],'line':line['line'],'explicit_chance':int(atoms[1]) if len(atoms)>1 else None,'slots':[]};sec['methods'].append(cur)
   else:
    slot={'line':line['line'],'weight':int(atoms[0]),'species':atoms[1],'minimum':int(atoms[2]),'maximum':int(atoms[3]) if len(atoms)>3 else int(atoms[2]),'maximum_omitted':len(atoms)<4,'species_defined':atoms[1] in species}
    if not cur or not slot['species_defined'] or slot['weight']<=0 or not 1<=slot['minimum']<=slot['maximum']<=100:exceptions.append(dict(path=f['path'],header=r['record_key'],**slot))
    if cur:cur['slots'].append(slot)
  for m in sec['methods']:
   c=Counter((v['species'],v['minimum'],v['maximum']) for v in m['slots']);m['same_species_and_level_tuple_duplicates']=[{'tuple':list(k),'count':v} for k,v in c.items() if v>1];m['weight_sum']=sum(v['weight'] for v in m['slots'])
  rows.append(sec)
 s.write('pbs-special-'+f['path'][4:].replace('/','--').replace(' ','_')+'.json',{'schema_version':'gr5.review.v1','path':f['path'],'version':s.R,'git_blob':f['git_blob'],'records':rows,'boundary':'All slots/weights/levels and identity references read by data parser. Chance/slot selection behavior compared separately, not executed.'});out.append({'path':f['path'],'records':len(rows),'family':f['family']})
# Remaining singleton special files retain ordered primitive relation data.
for fam in ['regional_dexes','map_connections','battle_facility_lists']:
 f=next(f for f in files if f['family']==fam);d=records(f['path']);rows=[]
 if fam=='regional_dexes':
  for rec in d['records']:
   mem=[x.strip() for rr in rec['raw_rows'] for x in rr['data_value'].split(',')]
   rows.append({'region':int(rec['record_key']),'lines':rec['lines'],'ordered_members':mem,'all_members_exist':all(x in ids['species'] for x in mem),'duplicates':{k:v for k,v in Counter(mem).items() if v>1},'consumer_semantic_status':'not_reviewed'})
 elif fam=='map_connections':
  maps={int(x) for x in idset('PBS/map_metadata.txt')}
  for rr in d['unsectioned_rows']:
   a=[x.strip() for x in rr['data_value'].split(',')];rows.append({'line':rr['line'],'from_map':int(a[0]),'from_edge':a[1],'from_coordinate':int(a[2]),'to_map':int(a[3]),'to_edge':a[4],'to_coordinate':int(a[5]),'both_metadata_exist':int(a[0]) in maps and int(a[3]) in maps,'consumer_semantic_status':'not_reviewed'})
 else:
  text=(ROOT/f['path']).read_text(encoding='utf-8-sig').splitlines()
  for rec in d['records']:
   v={p['key']:text[p['line']-1].split('=',1)[1].strip() for p in rec['properties']};rows.append({'section_name':rec['record_key'],'lines':rec['lines'],'references':v,'trainer_file_exists':(ROOT/'PBS'/v['Trainers']).is_file(),'pokemon_file_exists':(ROOT/'PBS'/v['Pokemon']).is_file(),'consumer_semantic_status':'not_reviewed'})
 s.write('pbs-special-'+f['path'][4:]+'.json',{'schema_version':'gr5.review.v1','path':f['path'],'version':s.R,'git_blob':f['git_blob'],'records':rows,'boundary':'Data-only complete ordered relation audit; consumer semantics separately reviewed.'});out.append({'path':f['path'],'records':len(rows),'family':fam})
s.write('pbs-special-audit.json',{'schema_version':'gr5.review.v1','files':out,'exceptions':exceptions,'boundary':'Automatic field relations are review inputs, not completed semantic coverage.'})
print('SPECIAL FILES',len(out),'EXCEPTIONS',len(exceptions))
for e in exceptions:print(e)
for path,rs in pools.items():print(path,len(rs),'empty_item',sum(not r['references']['items']['identity'] for r in rs),'move_holes',sum(bool(r['ignored_move_atoms']) for r in rs))
