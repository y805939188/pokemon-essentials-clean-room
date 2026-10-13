"""Read-only corpus-to-PBS data provenance joins, no reference execution."""
import json,hashlib,re
from collections import defaultdict
import review_state as s
FAMDOM={
 'pokemon':{'Name':'SPECIES_NAMES','Category':'SPECIES_CATEGORIES','Pokedex':'POKEDEX_ENTRIES','FormName':'SPECIES_FORM_NAMES'},
 'pokemon_forms':{'Category':'SPECIES_CATEGORIES','Pokedex':'POKEDEX_ENTRIES','FormName':'SPECIES_FORM_NAMES'},
 'moves':{'Name':'MOVE_NAMES','Description':'MOVE_DESCRIPTIONS'},
 'items':{'Name':'ITEM_NAMES','NamePlural':'ITEM_NAME_PLURALS','PortionName':'ITEM_PORTION_NAMES','PortionNamePlural':'ITEM_PORTION_NAME_PLURALS','Description':'ITEM_DESCRIPTIONS'},
 'abilities':{'Name':'ABILITY_NAMES','Description':'ABILITY_DESCRIPTIONS'},
 'types':{'Name':'TYPE_NAMES'},'trainer_types':{'Name':'TRAINER_TYPE_NAMES'},'ribbons':{'Name':'RIBBON_NAMES','Description':'RIBBON_DESCRIPTIONS'}}
def h(x):return hashlib.sha256(x.encode()).hexdigest()
def normal(x):
 # Relevant source normalization: trim edges; collapse runs of 2+ whitespace.
 # Isolated internal LF/TAB are not blindly replaced. This is a text-key join,
 # not a test of the reference normalizer.
 return re.sub(r'\s{2,}',' ',x.strip())
index=defaultdict(lambda:defaultdict(list));files=s.read('pbs-data-inspection.json')['files']
for f in files:
 if f['family'] not in FAMDOM:continue
 ledger=s.read('pbs-records-'+f['path'][4:].replace('/','--').replace(' ','_')+'.json');lines=(s.REF/f['path']).read_text(encoding='utf-8-sig').splitlines()
 for rec in ledger['records']:
  for prop in rec['properties']:
   dom=FAMDOM[f['family']].get(prop['key'])
   if not dom:continue
   val=lines[prop['line']-1].split('=',1)[1].strip()
   index[dom][h(normal(val))].append({'path':f['path'],'version':s.R,'git_blob':f['git_blob'],'record_key':rec['record_key'],'field':prop['key'],'line':prop['line'],'default_active':f['path'].count('/')==1})
summary=[]
for dom,keys in index.items():
 data=s.read('text-records-'+dom+'.json');bound=[];unlinked=[]
 for rec in data['records']:
  sources=keys.get(rec['key_sha256'],[])
  rec['pbs_origin_matches']=sources
  rec['record_semantic_obligations']=['hash domain is '+dom,'English key/value identity presentation; no effect behavior inferred','domain data getter uses raw authored field; language lookup/core-default fallback handled by WP08','source linkage does not establish a reachable gameplay consumer']
  rec['semantic_status']='payload_and_field_provenance_checked_consumer_contract_pending'
  if not sources:unlinked.append(rec['record'])
  bound.append({'record':rec['record'],'lines':rec['lines'],'sources':sources,'text_key_equals_value':rec['text_key_equals_value'],'binary_match':rec['matches_binary_entry']})
 s.write('text-records-'+dom+'.json',data)
 textkeys={r['key_sha256'] for r in data['records']};currentmissing=[a for k,v in keys.items() if k not in textkeys for a in v if a['default_active']]
 s.write('text-pbs-bridge-'+dom+'.json',{'schema_version':'gr5.review.v1','domain':dom,'source_baseline':s.R,'records':bound,'unmatched_corpus_record_indices':unlinked,'current_pbs_fields_without_core_key':currentmissing,'semantic_status':'field_provenance_only_not_completed_review'})
 summary.append({'domain':dom,'records':len(bound),'unmatched_corpus_record_indices':unlinked,'current_pbs_fields_without_core_key':currentmissing})
s.write('text-pbs-bridge.json',{'schema_version':'gr5.review.v1','module':'M01','source_baseline':s.R,'boundary':'All17non-script domains joined per record/field to all73PBS paths. This proves text provenance/identity matching, not source-effect correctness or runtime availability. Unmatched core entries remain callable hash data; not asserted dead.','domains':summary})
for x in summary:print(x['domain'],'records',x['records'],'unlinked',len(x['unmatched_corpus_record_indices']),'rootfields notcore',len(x['current_pbs_fields_without_core_key']))
