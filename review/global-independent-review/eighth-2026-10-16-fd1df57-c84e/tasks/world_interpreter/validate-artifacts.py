import pathlib,json,hashlib,datetime
D=pathlib.Path(__file__).parent
required=['progress.json','identities.json','reading-ledger.json','forward-mapping.json','reverse-mapping.json','interfaces.json','proposals.json','review.md']
checks=[]
def check(name,ok,detail=None):
 checks.append({'name':name,'pass':bool(ok),'detail':detail})
check('eight_required_present',all((D/p).is_file() for p in required))
J={p:json.loads((D/p).read_text()) for p in required if p.endswith('.json')}
fw=J['forward-mapping.json'];rv=J['reverse-mapping.json'];facts={f['id'] for u in fw['units'] for f in u['facts']};used={f for c in rv['clauses'] for a in c['subassertions'] for f in a['source_fact_ids']};atoms=[a['id'] for c in rv['clauses'] for a in c['subassertions']]
check('forward136_469',len(fw['units'])==136 and len(facts)==469,fw['counts'])
check('reverse330_1007',len(rv['clauses'])==330 and len(atoms)==1007,rv['counts'])
check('unique_reverse_assertion_ids',len(atoms)==len(set(atoms)))
check('every_reverse_fact_id_exists',used<=facts,sorted(used-facts))
check('all_source_fact_text_nonempty',all(f['assertion'].strip() for u in fw['units'] for f in u['facts']))
check('all_reverse_premises_nonempty',all(c['premises'] for c in rv['clauses']))
rs=json.loads((D.parents[1]/'delegation/readsets/world_interpreter.readset.json').read_text());CAT=pathlib.Path(rs['catalog_assigned']['repo'])/rs['catalog_assigned']['path'];wanted=set()
for n,l in enumerate(CAT.read_text().splitlines(),1):
 if any(a<=n<=z for a,z in rs['catalog_assigned']['assigned_line_ranges']) and l.startswith('|'):
  s=l.split('|')[1].strip()
  if s not in ['ID','---'] and not s.startswith('---'):wanted.add(s)
got={c['id'][4:] for c in rv['clauses'] if c['id'].startswith('WIV-')};check('169_assigned_vector_ids_exact',len(wanted)==169 and wanted==got,{'missing':sorted(wanted-got),'extra':sorted(got-wanted)})
check('96_matrix_46_route_rows',sum(c['id'].startswith('WIF-C') and c['id'][5:].isdigit() for c in rv['clauses'])==96 and sum(c['id'].startswith('WIF-ROUTE') for c in rv['clauses'])==46)
L=J['reading-ledger.json'];check('unread_dependencies_remain_nonzero',sum(len(x['unread_ranges']) for x in L['files'])==28 and L['counts']['partial_files']==11,L['counts'])
identity_mismatch=[]
for f in L['files']:
 b=(pathlib.Path(f['repo'])/f['path']).read_bytes()
 if len(b)!=f['bytes'] or hashlib.sha256(b).hexdigest()!=f['sha256']:identity_mismatch.append(f['path'])
check('all37_read_input_bytes_still_bound',len(L['files'])==37 and not identity_mismatch,identity_mismatch)
check('proposals_complete_required_contract_sections',all(all(k in p for k in ['id','classification','root_cause_key','dual_evidence','minimal_revision_contract','acceptance_and_regression','independent_adjudication','dependency_and_reception']) for p in J['proposals.json']['records']))
check('exact_two_proposal_ids',{p['id'] for p in J['proposals.json']['records']}=={'GR8-WORLD-INT-001','GR8-WORLD-INT-002'})
check('business_not_executed_and_update_not_started',J['progress.json']['behavior_execution_count']==0 and J['progress.json']['update_started'] is False and J['progress.json']['update_state']=='UPDATE_NOT_STARTED')
result={'schema':'gr8-world-interpreter-mechanical-validation/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'all_pass':all(x['pass'] for x in checks),'qualification':'Mechanical validation only. No semantic reading, independent adjudication, game/model/host execution, or whole-domain approval is inferred.','files':[{'path':p,'bytes':(D/p).stat().st_size,'sha256':hashlib.sha256((D/p).read_bytes()).hexdigest()} for p in required]}
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(0 if result['all_pass'] else 1)
