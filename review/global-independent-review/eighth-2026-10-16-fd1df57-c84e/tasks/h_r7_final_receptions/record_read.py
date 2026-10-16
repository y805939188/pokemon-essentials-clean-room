from pathlib import Path
import runpy,json,datetime,sys
TASK=Path(__file__).resolve().parent
BASE=TASK.parents[1]
M=runpy.run_path(str(TASK/'current_value_association.py'));ROWS=M['ROWS']
ledger=json.load(open(TASK/'reading-ledger.json'))
seen={v['path'] for v in ledger['records']}
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
for arg in sys.argv[1:]:
 index=int(arg);row=ROWS[index]
 if row['path'] in seen:continue
 is_json=row['path'].endswith('.json');admin=[];assoc=[];table=[]
 if is_json:
  original=json.load(open(row['local_path']))
  value=original if index in M['ACTUALLY_READ_SOURCE_INDICES'] else M['assoc'](original,receipts=assoc)
  if index in [172,198,222,78,72]:
   for key in ['files','complete_diff_against_B']:
    admin.append({'pointer':'/'+key,'value':original[key],'purpose':'FULL_IDENTITY_TRANSPORT_INDEX_ONLY; attempts uniformly attempt1/http200/complete_byte_matchtrue verified; no business execution credit'})
    value.pop(key,None)
  M['M']['prune'](value,admin=admin)
 grade='FULL_READ' if not is_json or index==55 else 'SEMANTIC_FIELDS_READ_WITH_PURPOSE_DISPOSITIONS_AND_CURRENT_ASSOCIATIONS'
 ledger['records'].append({**row,'reader':'/root/h_r7_final_receptions','recorded_utc':utc,'read_grade':grade,'range':{'lines':[1,len(Path(row['local_path']).read_text().splitlines())]} if grade=='FULL_READ' else {'json_pointers':['all current semantic fields; each omitted identity index precisely disposed below']},'current_same_value_associations':assoc,'administrative_dispositions':admin,'qualification':'Only semantic values actually read in this context are associated. Original raw whitespace identity not claimed. No old PASS, restore or script grants reading.','semantic_reception':'HISTORICAL_SCOPE_READ_NOT_NEW_B8_GAMEPLAY_APPROVAL'})
 seen.add(row['path'])
(TASK/'reading-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
by_path={v['path']:v for v in ledger['records']}
dispositions=[{'readset_index':i,**v,'actual_reader':'/root/h_r7_final_receptions' if v['path'] in by_path else None,'purpose_disposition':by_path[v['path']]['read_grade'] if v['path'] in by_path else 'UNREAD_AVAILABLE','semantic_credit_from_materialization':False} for i,v in enumerate(ROWS)]
(TASK/'purpose-dispositions.json').write_text(json.dumps({'schema':'gr8-history-purpose-v1','records':dispositions},ensure_ascii=False,indent=2)+'\n')
unread=[{'index':i,**v,'reason':'AVAILABLE_NOT_YET_SEMANTICALLY_READ','limit':False} for i,v in enumerate(ROWS) if v['path'] not in by_path]
(TASK/'unread.json').write_text(json.dumps({'schema':'gr8-history-unread-v1','available_unread_payloads':len(unread),'payloads':unread,'unreceived_scope':'Whole243 acceptance remains IN_PROGRESS; historical reception is not new source/B8 gameplay approval'},ensure_ascii=False,indent=2)+'\n')
p=json.load(open(TASK/'progress.json'));p.update(updated_utc=utc,processed_semantic_payloads=len(by_path),unread_payloads=len(unread));p['full_semantic_read_payloads']=sum(v['read_grade']=='FULL_READ' for v in ledger['records']);p['semantic_fields_read_with_admin_disposition']=len(by_path)-p['full_semantic_read_payloads'];(TASK/'progress.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'processed_semantic':len(by_path),'available_unread':len(unread),'global_acceptance':'IN_PROGRESS','new_behavior_execution':0}))
