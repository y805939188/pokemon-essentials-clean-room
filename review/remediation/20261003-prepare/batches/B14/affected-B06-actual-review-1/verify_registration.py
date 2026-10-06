"""New exact document/JSON/hash bookkeeping; no historical or reference program execution."""
import subprocess,json,pathlib,hashlib,functools,csv,io
D=pathlib.Path(__file__).parent
A='d48197f365c39925f795c1d325988c0d74e59979';C3='c06db6cd964188b3c693a9b7820e3a8aaffe0b04';O='93e10babe0b9c9ef8b3f5277754541b447beeeb4';PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed';B='review/remediation/20261003-prepare/batches/B14/integration-stage-1/'
@functools.lru_cache(maxsize=None)
def raw(s,p):return subprocess.check_output(['git','show',s+':'+p])
def obj(s,p):return json.loads(raw(s,p))
def ptr(v,selector):
 for k in selector.strip('/').split('/'):
  if not k:continue
  k=k.replace('~1','/').replace('~0','~');v=v[int(k)] if isinstance(v,list) else v[k]
 return v

def hashes(v):
 return {str((ascii_,sort_,sep_)):hashlib.sha256(json.dumps(v,ensure_ascii=ascii_,sort_keys=sort_,separators=(',',':') if sep_ else None).encode()).hexdigest() for ascii_ in [False,True] for sort_ in [False,True] for sep_ in [False,True]}
r=obj(A,B+'finding-registration.json');loc=obj(A,B+'clause-location-bindings.json');checks=[]
for q in r['dispositions']:
 i=q['id'];original=ptr(obj(q['original']['commit'],q['original']['path']),q['original']['selector']);acceptance=ptr(obj(q['approved_acceptance']['commit'],q['approved_acceptance']['path']),q['approved_acceptance']['selector']);rec={'id':i,'record_key':q['record_key'],'primary':q['primary'],'canonical_state':q['canonical_state'],'status':q['status'],'accepted_B14':q['accepted_B14_contribution'],'original_selector_matches_id':original['id']==i,'acceptance_selector_matches_id':acceptance['id']==i,'original_whole_object_hash_matches':q['whole_original_object_sha256'] in hashes(original).values(),'acceptance_whole_object_hash_matches':q['whole_acceptance_object_sha256'] in hashes(acceptance).values(),'qualified_current_fields':{k:original.get(k)==v for k,v in q['complete_current_control_fields'].items()},'minimum_acceptance_fields':{k:acceptance.get(k)==v for k,v in q['complete_minimum_acceptance_fields'].items()},'locations':[],'rows':[],'receipts':[]}
 for x in q['current_formal_locations']:
  b=raw(A,x['path']);lines=b.decode().splitlines();heads=[]
  for z in x['current_heading_locators']:
   text=lines[z['line']-1];heads.append({'section':z['section_number'],'line':z['line'],'exact_text':text==z['heading'],'hash':hashlib.sha256(b.splitlines(keepends=True)[z['line']-1]).hexdigest()==z['heading_sha256']})
  rec['locations'].append({'path':x['path'],'actual_byte_identity_matches_current':hashlib.sha256(b).hexdigest()==x['identity']['sha256'] and len(b)==x['identity']['bytes'],'headings':heads})
 for x in q['current_test_rows']:
  b=raw(A,x['path']).splitlines(keepends=True)[x['line']-1];rec['rows'].append({'path':x['path'],'line':x['line'],'id':x['id'],'exact_row_hash':hashlib.sha256(b).hexdigest()==x['row_sha256'],'exact_row_bytes':len(b)==x['row_bytes'],'id_matches':b.split(b'|')[1].strip().decode()==x['id']})
 for x in q['candidate_receipts']:
  p=x['report']['path'];rec['receipts'].append({'owner':x['owner'],'report_sha':x['report_commit'],'reviewed_sha':x['reviewed_candidate'],'candidate_C3':x['reviewed_candidate']==C3,'copied_report_exact':raw(A,p)==raw(x['report_commit'],p),'distinct_report_vs_reviewed':x['report_commit']!=x['reviewed_candidate']})
 rec['locator_registration_equal']=q['current_formal_locations']==loc['records'][i]['current_formal_locations'];checks.append(rec)
public=[]
for path in ['review/remediation/20261003-prepare/approval-ledger.tsv','review/remediation/20261003-prepare/traceability-successor.tsv']:
 rows=list(csv.DictReader(io.StringIO(raw(A,path).decode()),delimiter='\t'))[170:]
 for row in rows:
  details=json.loads(row['remaining_obligations']);i=row['finding_id'];q=next(x for x in r['dispositions'] if x['id']==i);public.append({'path':path,'id':i,'C3_bound':row['candidate_commit']==C3,'canonical_open':row['canonical_state']=='OPEN','contribution_record_key':details.get('record_key')==q['record_key'],'detail_keys':list(details)})
(D/'registration-validation.json').write_text(json.dumps({'ACT':A,'registration24':checks,'public48_appended_rows':public,'counts':{'registrations':len(checks),'primary':sum(x['primary'] for x in checks),'shared':sum(not x['primary'] for x in checks)},'scope':'Document/control/locator/relationship validation only; behavioral quality is separately judged.'},indent=2)+'\n')
fail=[]
for x in checks:
 for k in ['original_selector_matches_id','acceptance_selector_matches_id','original_whole_object_hash_matches','acceptance_whole_object_hash_matches','locator_registration_equal']:
  if not x[k]:fail.append([x['id'],k])
 for k in ['qualified_current_fields','minimum_acceptance_fields']:
  for f,ok in x[k].items():
   if not ok:fail.append([x['id'],k,f])
 for l in x['locations']:
  if not l['actual_byte_identity_matches_current']:fail.append([x['id'],'location_identity',l['path']])
  for h in l['headings']:
   if not all(h[k] for k in ['exact_text','hash']):fail.append([x['id'],'heading',h])
 for l in x['rows']:
  if not all(l[k] for k in ['exact_row_hash','exact_row_bytes','id_matches']):fail.append([x['id'],'row',l])
 for l in x['receipts']:
  if not all(l[k] for k in ['candidate_C3','copied_report_exact','distinct_report_vs_reviewed']):fail.append([x['id'],'receipt',l])
print('Registrations',len(checks),'primary',sum(x['primary'] for x in checks),'shared',sum(not x['primary'] for x in checks),'failure_count',len(fail))
for x in fail[:10]:print(x)
print('Public append failures',[x for x in public if not all(x[k] for k in ['C3_bound','canonical_open','contribution_record_key'])])
