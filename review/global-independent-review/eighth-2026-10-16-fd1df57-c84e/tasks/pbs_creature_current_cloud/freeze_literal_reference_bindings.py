from pathlib import Path
import json,re,datetime,hashlib,collections
P=Path(__file__).resolve().parent;R=Path('/workspace/pokemon-essentials');U=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
maps=collections.defaultdict(dict);target_records=[]
def body(kind,id,pointer,reader,condition='Fixeddefaultloadedrecords andnooverride'):
 k=(kind,id,condition)
 if id not in maps[kind]:
  maps[kind][id]=len(target_records);target_records.append(dict(kind=kind,id=id,complete_read_body_pointer=pointer,actual_original_reader=reader,activation=condition,evidence='Actualcompletebodypreviouslyread/received; thismap isonlyexactlocatorandpostreadingbinding, not hash/parser/readsubstitute.'))
def own(kind,rs,root,condition='Fixeddefaultloadedrecords andnooverride'):
 for i,r in enumerate(rs):body(kind,r['id'],f'{root}/{i}','/root/pbs_creature_current_cloud',condition)
t=json.loads((P/'typed-record-facts.v1.json').read_text())
for i in range(1,6):
 n=f'pokemon-records-{i:02}.complete.v1.json';own('Species',json.loads((P/n).read_text())['records'],n+'#/records')
own('Item',json.loads((P/'item-dependency-records-229.complete.v2.json').read_text())['records'],'item-dependency-records-229.complete.v2.json#/records')
for i,r in enumerate(t['paths'][5]['records']):body('Species',r['id'].replace(',','_'),f'typed-record-facts.v1.json#/paths/5/records/{i}','/root/pbs_creature_current_cloud')
own('TrainerType',t['paths'][8]['records'],'typed-record-facts.v1.json#/paths/8/records')
for index,kind in [(1,'Move'),(3,'Type')]:own(kind,t['paths'][index]['records'],f'typed-record-facts.v1.json#/paths/{index}/records','ExplicitShadowbackupactivation+validdependencies; notdefaultdiscovery')
pb=json.loads((P/'provider-snapshots/pbs-battle-default-records.complete.v2.json').read_text())
for vi,v in enumerate(pb['complete_received_record_vectors']):
 kind='Ability' if 'PBS_abilities.txt.'in v['path'] else 'Move'
 for li,s in enumerate(v['text'].splitlines()[1:],2):body(kind,s.split('|')[1],f'provider-snapshots/pbs-battle-default-records.complete.v2.json#/complete_received_record_vectors/{vi}/text#line{li}','/root/pbs_battle')
types=pb['own_full_type_source']['text'].splitlines()
for li,s in enumerate(types,1):
 m=re.match(r'^\[([^]]+)\]',s)
 if m:body('Type',m.group(1),f'R:PBS/types.txt#line{li} completeownrawfile1–129 /provider-snapshots/pbs-battle-default-records.complete.v2.json#/own_full_type_source/text','/root/pbs_creature_current_cloud')
defs={'GrowthRate':'001_GrowthRate.rb','GenderRatio':'002_GenderRatio.rb','EggGroup':'003_EggGroup.rb','BodyShape':'004_BodyShape.rb','BodyColor':'005_BodyColor.rb','Habitat':'006_Habitat.rb','Evolution':'007_Evolution.rb','Stat':'008_Stat.rb','Nature':'009_Nature.rb','EncounterType':'013_EncounterType.rb','Target':'017_Target.rb'}
for kind,name in defs.items():
 path='Data/Scripts/010_Data/001_Hardcoded data/'+name;ls=(R/path).read_text().splitlines();starts=[i for i,s in enumerate(ls) if s.startswith('GameData::'+kind+'.register(')]
 for k,si in enumerate(starts):
  hi=starts[k+1] if k+1<len(starts) else len(ls);m=re.search(r':id\s*=>\s*:(\w+)', '\n'.join(ls[si:hi]));assert m,(kind,si)
  body(kind,m.group(1),f'R:{path}#lines{si+1}–{hi}; actualownfullsource inreading-ledger/dependency-identities','/root/pbs_creature_current_cloud','Fixedbuiltinregistry definitions;fullmeaning sourceownread, noPBSload needed')
rows=[];missing=[];counts=collections.Counter();literal_occurrences=0
def ref(kind,id,where):
 global literal_occurrences
 literal_occurrences+=1;counts[kind]+=1
 if id not in maps[kind]:missing.append(dict(kind=kind,id=id,where=where));return None
 return maps[kind][id]
field_kind={'Types':'Type','Abilities':'Ability','HiddenAbilities':'Ability','GenderRatio':'GenderRatio','GrowthRate':'GrowthRate','EggGroups':'EggGroup','Incense':'Item','MegaStone':'Item','MegaMove':'Move','Offspring':'Species','Color':'BodyColor','Shape':'BodyShape','Habitat':'Habitat','WildItemCommon':'Item','WildItemUncommon':'Item','WildItemRare':'Item','Item':'Item','Ball':'Item','Items':'Item','Type':'Type','Target':'Target','Resistances':'Type'}
allpaths=[(x['path'],x['family'],x['records'],f'typed-record-facts.v1.json#/paths/{pi}/records') for pi,x in enumerate(t['paths'])]
for i in range(1,6):
 n=f'pokemon-records-{i:02}.complete.v1.json';allpaths.append(('PBS/pokemon.txt','species',json.loads((P/n).read_text())['records'],n+'#/records'))
for path,fam,rs,root in allpaths:
 for ri,r in enumerate(rs):
  coords=[]
  if fam in ['species','forms','metrics','shadow_pokemon']:
   sid=r['id'].split(',')[0];coords.append(['@section',ref('Species',sid,[path,r['id'],'section'])])
  for fi,f in enumerate(r['fields']):
   key=f.get('key');v=f.get('interpreted_value');rr=[]
   if key in field_kind:
    kind=field_kind[key];vs=v if isinstance(v,list) else [v]
    rr=[ref(kind,x,[path,r['id'],key,f.get('line')]) for x in vs if x is not None]
   elif key=='EVs':rr=[ref('Stat',x,[path,r['id'],key,f.get('line')]) for x in f['original_value'].split(',')[::2]]
   elif key=='Moves':
    vs=[x['move'] if isinstance(x,dict) else x[1] for x in v] if fam in ['species','forms'] else v;rr=[ref('Move',x,[path,r['id'],key,f.get('line')]) for x in vs]
   elif key in ['TutorMoves','EggMoves']:rr=[ref('Move',x,[path,r['id'],key,f.get('line')]) for x in v]
   elif key=='Pokemon':rr=[ref('Species',v['species'],[path,r['id'],key,f.get('line')])]
   elif fam=='encounters':
    if 'encounter_method'in v:rr=[ref('EncounterType',v['encounter_method'],[path,r['id'],f.get('line')])]
    elif 'species_id'in v:rr=[ref('Species',v['species_id'],[path,r['id'],f.get('line')])]
   elif fam=='regional_dexes':rr=[ref('Species',x,[path,r['id'],f.get('line')]) for x in v['ordered_species_ids']]
   if rr:coords.append([fi,key or '@ordered',f.get('line'),rr])
  if fam=='trainers':coords.append(['@trainer_type',ref('TrainerType',r['id'].split(',')[0],[path,r['id'],'section'])])
  rows.append([path,r['ordinal'],r['id'],f'{root}/{ri}',coords])
e=json.loads((P/'evolution-author-edges.complete.v2.json').read_text());ec=[]
for i,x in enumerate(e['edges']):
 refs=[ref('Species',x[10],['Evolutionedge',x[0],'target']),ref('Evolution',x[11],['Evolutionedge',x[0],'method'])]
 if x[13] in ['Item','Move','Type','Species']:refs.append(ref(x[13],x[14],['Evolutionedge',x[0],'typedparam']))
 ec.append([x[0],refs,f'evolution-author-edges.complete.v2.json#/edges/{i}'])
defaultrefs=[]
for kind,id,why in [('Item','POKEBALL','Pokemondefaultball'),('Type','NORMAL','Speciesdefaulttype'),('GrowthRate','Medium','Speciesdefaultgrowth'),('GenderRatio','Female50Percent','Speciesdefaultgender'),('EggGroup','Undiscovered','Speciesdefaultegggroup'),('BodyColor','Red','Speciesdefaultcolor'),('BodyShape','Head','Speciesdefaultshape'),('Habitat','None','Speciesdefaulthabitat'),('Evolution','None','familylinkmethod')]:defaultrefs.append([why,ref(kind,id,['default',why])])
assert not missing,missing[:30]
assert len(rows)==2178
out=dict(schema='gr8-primary-exact-literal-reference-body-bindings/v1',utc=U,actual_reader='/root/pbs_creature_current_cloud',R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',record_count=2178,literal_reference_occurrences=literal_occurrences,reference_counts=dict(counts),target_body_count=len(target_records),known_missing_literal_bodies=missing,strict_scope='ExactregisteredIDbody+definition reception coordinates for allactualprimaryfields and typed460Evolutionedges. It is a postreading completeness/binding ledger only, not parser-success/readproof or transitivegameplayapproval. Callback, dynamicflag/map/resource/native behavior remain OPEN where not separately read.',complete_prior_reading_basis=['All11rawfiles2178records actualownFULL; typedcomplete originalpackets preserved.','AllreferenceddefaultMove740/Ability267 fullreadablemetadata vectors previouslyactuallyreceived; originalreader PBSbattle retained.','All229 selectedItemcompletebodies ownactuallyread; Type19default+Shadowtype1 rawownFULL.','Ownfullhardcoded registries, including all64Evolution callbacks,6growth tables/formulas,8GenderRatio,8Stat,15EggGroup,14Shape,10Color,10Habitat,25Nature,26EncounterType,18Target. Register navigation alone is not source meaning proof; earlierfullreads/manualfacts are required.'],target_records=target_records,record_columns=['source_path','ordinal','id','complete_original_record_pointer','referencecoordinates [fieldindex,key,line,[target_body_indices]] orsectionnamedtarget'],records=rows,evolution_typed_edge_targets=ec,default_targets=defaultrefs,mandatory_companions=['mandatory-locator-clarification.v2.json','mandatory-item-schema-clarification.v1.json'],non_resolving_constructor_defaults=[dict(field='Move.type',value='NONE',source='005_Move.rb44',actualdefaultTypebody='ABSENT fromall19PBS/types.txt records; QMARKSispseudotypeanddifferentid',premise='AllactualprimaryShadow18andreceiveddefault740MoveTypefieldsexplicit; noactualprimaryliteralNONEref. Constructordefaultsymbolisnotproofregisteredidentity.',first_binding_check='61f8e7 correctlyreported proposeddefaultNONEbodymissing; 26f07e/f4d55a re-read provedthisisconstructorsentinelnotactualfieldliteral. Originalexit1 preserved; notsilentlyconvertedtoPASS.')],whole_consumer_closure='OPEN separately; thisfield-body finite conclusion doesnot approveallcallback behavior,formal clauses or available alternatives.',behavior='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
f=P/'primary-literal-reference-bindings.complete.v1.json';f.write_text(json.dumps(out,ensure_ascii=False,separators=(',',':'))+'\n');b=f.read_bytes();print(json.dumps(dict(utc=U,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),records=len(rows),references=literal_occurrences,targets=len(target_records),missing=len(missing),bykind=dict(counts))))
