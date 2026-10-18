import pathlib,json,re,collections,hashlib,datetime
ROOT=pathlib.Path('.');OUT=ROOT/'tasks/coverage_acceptance_audit';B=pathlib.Path('/workspace/pokemon-essentials-clean-room');R=pathlib.Path('/workspace/pokemon-essentials');a=json.loads((OUT/'acceptance-register.json').read_text());claims=a['all_ledger_claims']
def load(p):return json.loads((ROOT/p).read_text())
def check(reader,repo,p,rs):
 b=(R if repo=='R' else B)/p;n=len(b.read_bytes().splitlines());cov=[r for x in claims if x['reader']==reader and x['path']==p and x['repo']==repo and x.get('eligible_current_baseline',True) for r in x['clipped_read_ranges']];errs=[]
 for s,e in rs:
  if not 1<=s<=e<=n:errs.append('OUT_OF_BOUNDS')
  if not any(x<=s<=e<=y for x,y in cov):errs.append('NOT_CONTAINED_BY_SINGLE_REPORTED_RANGE')
 return {'actual_lines':n,'errors':sorted(set(errs))}
ui=load('tasks/ui_navigation_audit/forward.json');uiids={f['id'] for f in ui['facts']};uifa=[]
for i,f in enumerate(ui['facts']):
 checks=[{'path':s['path'],'range':[s['line_start'],s['line_end']],**check('/root/ui_navigation_audit','R',s['path'],[[s['line_start'],s['line_end']]])} for s in f['source']]
 for loc in f.get('spec_locations',[]):
  rr=[loc['line'],loc['line']]
  checks.append({'path':loc['path'],'range':rr,**check('/root/ui_navigation_audit','B8',loc['path'],[rr])})
 if 'spec' in f:checks.append({'path':f['spec']['path'],'range':f['spec']['lines'],**check('/root/ui_navigation_audit','B8',f['spec']['path'],[f['spec']['lines']])})
 uifa.append({'row':i,'id':f['id'],'status':f['status'],'locator_checks':checks,'relation':f.get('relation'),'scope':'Finite source assertion report; all-formal atomic receipt remains explicitly incomplete'})
uir=[]
for i,r in enumerate(load('tasks/ui_navigation_audit/reverse.json')['records']):
 uir.append({'row':i,'id':r['line_unit_id'],'path':r['path'],'line':r['line'],'range_check':check('/root/ui_navigation_audit','B8',r['path'],[[r['line'],r['line']]]),'unknown_fact_ids':[x for x in r['linked_source_fact_ids'] if x not in uiids],'linked_fact_count':len(r['linked_source_fact_ids']),'disposition':r['disposition'],'atomic_denominator_final':r['atomic_denominator_final'],'acceptance':'UNRECEIVED; broad section links never approve every child'})
w=load('tasks/world_topology_audit/forward.json');wids={f['fact_id'] for f in w['facts']};wf=[]
for i,f in enumerate(w['facts']):
 cc=[]
 for s in f['sources']:
  rs=[[int(x) for x in re.findall(r'\d+',seg)] for seg in s['lines'].split(',')]
  rs=[r*2 if len(r)==1 else r for r in rs]
  cc.append({'path':s['path'],'ranges':rs,**check('/root/world_topology_audit','R',s['path'],rs)})
 wf.append({'row':i,'id':f['fact_id'],'checks':cc,'status':f['status']})
wr=load('tasks/world_topology_audit/reverse.json');wa=[]
for r in wr['wp11_clauses']:
 wa.append({'id':r['clause_id'],'path':r['path'],'line':r['line'],'range_check':check('/root/world_topology_audit','B8',r['path'],[[r['line'],r['line']]]),'unknown_fact_ids':[x for x in r['source_facts'] if x not in wids],'assertion_count':len(r['assertions']),'status':r['status'],'qualification':'Substantive manually written assertion list read; local bounded support preserved, independent findings and shared/transitive reception still pending'})
ws=load('tasks/world_topology_audit/structure-index.json')['units'];wsa=[{'id':r['unit_id'],'path':r['path'],'range':[r['start'],r['end']],'check':check('/root/world_topology_audit','R',r['path'],[[r['start'],r['end']]]),'reported_full_definition_read':r['full_definition_read'],'disposition':r['disposition']} for r in ws]
pf=load('tasks/pbs_world_record_audit/forward.json')['rows'];contracts=load('tasks/pbs_world_record_audit/field-contracts.json')['contracts'];pr=[]
for i,r in enumerate(pf):
 contract=r['fact_consumer_formal_ref'].split('/')[-1];errs=[]
 if r['record_pointer']!=f'records.json#/records/{i}':errs.append('RECORD_POINTER')
 if contract not in contracts:errs.append('UNKNOWN_CONTRACT')
 for f in r['fields']:
  if f['fact_contract'] not in contracts:errs.append('UNKNOWN_FIELD_CONTRACT')
 pr.append({'row':i,'source':r['source'],'record':r['record'],'line':r['line'],'contract':contract,'fields':len(r['fields']),'errors':errs,'reported_status':r['status'],'audit_qualification':'Named reader reports complete current record semantics; shared10contracts preserve exact per-record field values. Full runtime/primary domain receipt not inferred.'})
rr=[]
for i,r in enumerate(load('tasks/pbs_world_record_audit/reverse.json')['rows']):
 ptrs=r.get('source_record_pointers',[]);bad=[]
 for p in ptrs:
  m=re.fullmatch(r'forward.json#/rows/(\d+)',p)
  if not m or int(m.group(1))>=len(pf):bad.append(p)
 rr.append({'row':i,'clause':r['clause'],'linked_records':len(ptrs),'unknown_record_pointers':bad,'qualification':'Exact bounded subassertion/record family receipt claimed; no whole formal-clause census'})
contract_checks=[]
for name,c in contracts.items():
 cc=[]
 for s in c['definition_or_producer']+c['consumer']:
  if 'path' in s:cc.append({'path':s['path'],'range':s['range'],**check('/root/pbs_world_record_audit','R',s['path'],[s['range']])})
 contract_checks.append({'contract':name,'checks':cc,'acceptance':c['acceptance'],'qualification':'Named external reader-based consumer entries remain their explicit bounded/pending receipts'})
a['late_deliveries_audit']={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'UI_forward':uifa,'UI_reverse':uir,'UI_interfaces':load('tasks/ui_navigation_audit/interfaces.json'),'WORLD_forward':wf,'WORLD_WP11_reverse':wa,'WORLD_catalog':wr['catalog_all_rows'],'WORLD_structure_all':wsa,'WORLD_remaining':wr['read_only_not_reverse_received'],'PBS_world_forward':pr,'PBS_world_reverse':rr,'PBS_world_contracts':contract_checks,'PBS_world_interfaces':load('tasks/pbs_world_record_audit/interfaces.json'),'counter_COM_read_ledger':'All55payload identities/ranges ingested in all_ledger_claims; historicald152WP39 explicitly excluded from currentB8reading credit; only two candidate-specific rebuttals, no whole-domain PASS.'}
(OUT/'acceptance-register.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'UIforward':len(uifa),'UIreverse':len(uir),'UIunknown_factlinks':sum(bool(r['unknown_fact_ids']) for r in uir),'UIreverse_locator_errors':sum(bool(r['range_check']['errors']) for r in uir),'UIforward_locator_issues':[(r['id'],c) for r in uifa for c in r['locator_checks'] if c['errors']],'WORLDfacts':len(wf),'WORLDreverse':len(wa),'WORLDstructures':len(wsa),'WORLDstructure_partial_locators':sum(bool(r['check']['errors']) for r in wsa),'WORLDreverse_unknown_ids':sum(bool(r['unknown_fact_ids']) for r in wa),'WORLDreverse_errors':sum(bool(r['range_check']['errors']) for r in wa),'PBSforward':len(pr),'PBSreverse':len(rr),'PBScontract_checks':contract_checks},ensure_ascii=False,indent=2))
