#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json
OUT=Path(__file__).resolve().parent;RR=OUT.parents[2]
def sha(b):return hashlib.sha256(b).hexdigest()
def get(n):return json.loads((OUT/n).read_bytes())
def put(n,d):
 with (OUT/n).open('w') as f:json.dump(d,f,ensure_ascii=False,separators=(',',':'));f.write('\n')
idx=get('index.json');inp=get('inputs.json');u=get('unmatched.json');v=get('validation.json')
fixed={(r['kind'],r['path']) for r in idx['rows']}
regraw=(RR/'adjudication/root-primary-task-final-registry.v1.json').read_bytes();reg=json.loads(regraw)
tasks={x['task'] for x in reg['accepted']}
gaps=[]
for task in ['com_ability_item','com_battler']:
 p=RR/'delegation/readsets'/f'{task}.json';raw=p.read_bytes();d=json.loads(raw);members=[]
 def walk(x,j=''):
  if isinstance(x,dict):
   for k,y in x.items():walk(y,j+'/'+k.replace('~','~0').replace('/','~1'))
  elif isinstance(x,list):
   for i,y in enumerate(x):walk(y,j+'/'+str(i))
  elif isinstance(x,str):
   for kind,path in fixed:
    if x==path:members.append({'kind':kind,'path':path,'readset_pointer':j})
 walk(d)
 uniq={(x['kind'],x['path']):x for x in members}
 gap={'logical_original_scope':task,'current_registry_sha256':sha(regraw),'current_registry_count':len(reg['accepted']),'exact_task_entry_present':task in tasks,'task_final_receipt':'NO_EXACT_CURRENT_REGISTRY_TASK_ENTRY' if task not in tasks else next(x['receipt'] for x in reg['accepted'] if x['task']==task),'readset_identity':{'path':str(p.relative_to(RR)),'bytes':len(raw),'sha256':sha(raw)},'members':list(uniq.values()),'qualification':'Whole named domain approval remains separate from original personally FULL/finite/associated source facts and accepted necessary consumers. Existing actual reading is preserved; missing whole task-final does not erase it.'}
 if task=='com_ability_item':gap['item_receipt_boundary']={'receipt':'adjudication/root-item-task-final-acceptance.v1.json','original_scope_pointers':['/fixed_qualified_producer','/final_catalog_schema_tail'],'qualification':'Root-item exact Item contribution/catalog/schema qualification only; never substitutes whole Ability WP48/49/50 task-final. Current CONT01 transport/semantic recovery remains root-owned.'}
 gaps.append(gap)
 for row in idx['rows']:
  if (row['kind'],row['path']) in uniq:
   row.setdefault('whole_foreign_primary_receipt_guards',[]).append({'scope':task,'artifact':'whole-scope-receipt-gaps.json','qualification':'No exact current whole-scope task-final found; original candidate source-reader/range/finite-reception fields unchanged.'})
put('whole-scope-receipt-gaps.json',{'schema':'gr8-original-whole-domain-receipt-gaps/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'CURRENT_ROOT_REGISTRY_EXACT_MEMBER_CHECK_ONLY_NO_SEMANTIC_REVIEW','gaps':gaps,'parent_reported_transport_only_not_semantically_accepted':[{'scope':'Battler','head':'d1e713ccd22454a2039a16c615ffb578f2646a8f'},{'scope':'Hearly','head':'4dd33cacb54cdf1a95a9a6c5ce053082d71b12e7'},{'scope':'Legacy','head':'b5ed789c44dcd78eec891871ba9716dbd8009f1a'},{'scope':'ELR','head':'c699d3642655a8e50038162e48dd60fcfeda1ced'}],'transport_qualification':'Parent message provenance only; no retrieval/identity/semantic credit added by this mechanical index.'})
u['whole_foreign_scope_receipt_gaps']='whole-scope-receipt-gaps.json';put('unmatched.json',u);put('index.json',idx)
v['whole_foreign_scope_receipt_gaps_preserved']=[x['logical_original_scope'] for x in gaps if not x['exact_task_entry_present']];put('validation.json',v)
text=(OUT/'report.md').read_text();text+='\n整域收据缺口另见 `whole-scope-receipt-gaps.json`：当前23 registry 无 COM-ABILITY-ITEM、Battler 的 exact 整域 task-final；逐一列原 readset 成员。root-item 只保其精确 Item/目录/schema 范围，不替代 WP48/49/50 Ability 整义。原有限必要源事实的实际阅读/接收仍保留，不因此回退为未读。父报4个新远端head仅记 transport 信息，未授语义接收。\n';(OUT/'report.md').write_text(text)
print(json.dumps({'current_registry':len(reg['accepted']),'whole_receipt_gaps':[{'scope':x['logical_original_scope'],'source_members':sum(y['kind']=='reference' for y in x['members']),'formal_members':sum(y['kind']=='formal' for y in x['members']),'exact_task_entry':x['exact_task_entry_present']} for x in gaps]},ensure_ascii=False))

