import pathlib,json,sys,hashlib
b=pathlib.Path('/workspace/pokemon-essentials-clean-room/review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/receive_external_pbs_creature_backups');d=json.loads((b/'delegation/remaining-v1/gen8/readset.complete.json').read_text());rs={r['frozen']['id']:r for r in d['owned_records']};raws={p['id']:(pathlib.Path('/workspace/pokemon-essentials')/p['path']).read_bytes() for p in d['owned_primary_files']}
def fields(r):
 a,z=r['frozen']['byte_offsets_half_open'];v=raws[r['frozen']['identity_id']][a:z];assert hashlib.sha256(v).hexdigest()==r['source_unit_sha256'];out={}
 for line in v.decode().splitlines():
  if '=' in line and not line.startswith('#'):
   k,v=line.split('=',1);out.setdefault(k.strip(),[]).append(v.strip())
 return out
empty={'Name':'Unnamed','FormName':None,'MegaStone':None,'MegaMove':None,'UnmegaForm':0,'MegaMessage':0,'Types':['NORMAL'],'BaseStats':[1,1,1,1,1,1],'GenderRatio':'Female50Percent','GrowthRate':'Medium','BaseExp':100,'EVs':{'all_main_stats':0},'CatchRate':255,'Happiness':70,'Abilities':[],'HiddenAbilities':[],'Moves':[],'TutorMoves':[],'EggMoves':[],'EggGroups':['Undiscovered'],'HatchSteps':1,'Incense':None,'Offspring':[],'Height':0.1,'Weight':0.1,'Color':'Red','Shape':'Head','Habitat':'None','Category':'???','Pokedex':'???','Generation':0,'Flags':[],'WildItemCommon':[],'WildItemUncommon':[],'WildItemRare':[]}

import re,collections
R=pathlib.Path('/workspace/pokemon-essentials'); enums={}
for k,fn in [('Item','items.txt'),('Move','moves.txt'),('Ability','abilities.txt'),('Type','types.txt')]:
 enums[k]={m[1] for line in (R/'PBS/Gen 8 backup'/fn).read_text(encoding='utf-8-sig').splitlines() if (m:=re.match(r'^\[([^\]]+)\]',line))}
enums['Species']={r['frozen']['section'] for r in d['owned_records'] if r['frozen']['identity_id']=='P14'}
for k,fn in [('GenderRatio','002_GenderRatio.rb'),('GrowthRate','005_GrowthRate.rb'),('Stat','008_Stat.rb'),('EggGroup','003_EggGroup.rb'),('BodyColor','004_BodyColor.rb'),('BodyShape','005_BodyShape.rb'),('Habitat','006_Habitat.rb')]:
 # Locate actual numbered catalog, never invent path identity.
 hits=list((R/'Data/Scripts/010_Data/001_Hardcoded data').glob('*_'+k+'.rb'))
 if not hits: continue
 enums[k]=set(re.findall(r':id\s*=>\s*:(\w+)',hits[0].read_text()))
field_enum={'Types':'Type','GenderRatio':'GenderRatio','GrowthRate':'GrowthRate','Abilities':'Ability','HiddenAbilities':'Ability','TutorMoves':'Move','EggMoves':'Move','EggGroups':'EggGroup','Incense':'Item','Offspring':'Species','Color':'BodyColor','Shape':'BodyShape','Habitat':'Habitat','WildItemCommon':'Item','WildItemUncommon':'Item','WildItemRare':'Item','MegaStone':'Item','MegaMove':'Move'}
errors=[];refs=collections.Counter();dupes=[];rawfield=0
for rid,r in rs.items():
 f=fields(r);rawfield+=sum(map(len,f.values()))
 for k,ek in field_enum.items():
  if ek not in enums:continue
  for v in f.get(k,[]):
   for token in v.split(','):
    refs[ek]+=1
    if token.strip() not in enums[ek]:errors.append([rid,k,token])
 for k in ['Moves','EVs']:
  for v in f.get(k,[]):
   a=v.split(',');assert len(a)%2==0
   if k=='Moves': assert all(re.fullmatch(r'\d+',x) for x in a[::2]);toks=a[1::2];ek='Move'
   else: assert all(re.fullmatch(r'[1-9]\d*',x) for x in a[1::2]);toks=a[::2];ek='Stat'
   for t in toks:
    refs[ek]+=1
    if t not in enums[ek]:errors.append([rid,k,t])
 for k in ['BaseStats']:
  if k in f:assert len(f[k][0].split(','))==6 and all(re.fullmatch(r'[1-9]\d*',x) for x in f[k][0].split(','))
 for k in ['CatchRate','Happiness','PokedexForm','UnmegaForm','MegaMessage','Generation']:
  for v in f.get(k,[]):assert re.fullmatch(r'\d+',v),(rid,k,v)
 for k in ['TutorMoves','EggMoves','Abilities','HiddenAbilities','Offspring']:
  for v in f.get(k,[]):
   a=v.split(',');reps=[x for x,c in collections.Counter(a).items() if c>1]
   if reps:dupes.append([rid,k,reps])
print(json.dumps({'mechanical_only_no_reading_or_business_credit':True,'records':len(rs),'all_actual_raw_fields':rawfield,'checked_enum_occurrences':refs,'enum_or_grammar_errors':errors,'preserved_list_repeats':dupes},ensure_ascii=False,indent=2))
