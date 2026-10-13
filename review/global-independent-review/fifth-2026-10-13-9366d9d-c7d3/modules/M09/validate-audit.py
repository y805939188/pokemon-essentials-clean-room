"""Audit metadata validation only, never reference/model execution."""
from pathlib import Path
import json,re,collections
O=Path(__file__).parent;W=Path.cwd();R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
files=['reading-coverage.json','source-to-spec.json','spec-to-source.json','findings.json','shared-interfaces.json','progress.json'];ds={n:json.loads((O/n).read_text()) for n in files};errors=[]
for n,d in ds.items():
 if d.get('schema_version')!='gr5.review.v1':errors.append([n,'schema_version'])
 if d['source_baseline']['commit']!='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b':errors.append([n,'source version'])
 if d['specification_baseline']['commit']!='9366d9d17aaeac3b4414236468affa650fb3dd27':errors.append([n,'spec version'])
rd=ds['reading-coverage.json'];fw=ds['source-to-spec.json'];rv=ds['spec-to-source.json'];finds=ds['findings.json']['findings'];shared=ds['shared-interfaces.json']['interfaces']
paths={s['path']:s for s in rd['sources']};segments={s['id']:(p,s) for p in fw['source_paths'] for s in p['segments']};clauses={c['id']:(p,c) for p in rv['documents'] for c in p['clauses']};regs={r['id']:r for r in fw['registration_ledger']};caps={c['id']:c for c in fw['capabilities']};interfaces={x['id'] for x in shared}
for p in rd['sources']:
 required=['path','version','review_extent','material_availability','evidence_level','unreviewed_intervals','semantic_segments']
 for k in required:
  if k not in p:errors.append([p['path'],'missing '+k])
 n=len((R/p['path']).read_text(encoding='utf-8-sig').splitlines())
 if n!=p['total_lines']:errors.append([p['path'],'line count'])
 for s in p['semantic_segments']:
  for a,b in s.get('line_ranges',[]) or ([s['lines']] if s.get('lines') else []):
   if not (1<=a<=b<=n):errors.append([p['path'],'bad source range',a,b,n])
 if p.get('scope_role')=='primary_assigned':
  if p['review_extent']!='full' or p['unreviewed_intervals']:errors.append([p['path'],'primary not full'])
  if p.get('remaining_assigned_semantic_scope'):errors.append([p['path'],'primary unfinished'])
for p in rv['documents']+rv['test_documents']:
 n=len(Path(p['path']).read_text().splitlines())
 for c in p['clauses']:
  a,b=c['lines']
  if not 1<=a<=b<=n:errors.append([p['path'],'bad spec range',c['id']])
  if not c['source_segment_ids']:errors.append([p['path'],'empty sources',c['id']])
  for k in c['source_segment_ids']:
   if k not in segments:errors.append(['missing source segment',k])
  for k in c['capability_ids']:
   if k not in caps:errors.append(['missing cap',k])
  for k in c.get('registration_ids',[]):
   if k not in regs:errors.append(['missing reg',k])
for c in caps.values():
 for k in c['source_segment_ids']:
  if k not in segments:errors.append(['cap missing source',c['id'],k])
 for k in c['spec_clause_ids']:
  if k not in clauses:errors.append(['cap missing clause',c['id'],k])
 if not c['support_boundary']:errors.append(['cap boundary',c['id']])
# Check literal declaration joins, not handler behavior execution.
declarations=collections.defaultdict(list);unseen=[]
for r in regs.values():
 if not r['semantic_segment_ids'] or not r['spec_anchors']:errors.append(['unlinked registration',r['id']])
 key=(r['group'],r['source_key'])
 if r['operation']=='copy':
  if key not in declarations:unseen.append(r['id'])
  for k in r['copy_destination_keys']:
   if k in ['AI','Handlers','MORE_TYPE_EFFECTS']:errors.append(['bad lexical destination',r['id'],k])
   declarations[(r['group'],k)].append(r['id'])
 else:declarations[key].append(r['id'])
if unseen!=['REG-0548','REG-0737','REG-0745']:errors.append(['unexpected missing predecessor literal declarations',unseen])
req='id title module severity disposition status reviewer category source_baseline specification_baseline source_anchors spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change affected_files shared_contracts acceptance_criteria dependencies related_capabilities related_findings root_cause_group priority batch_owner history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution'.split()
for f in finds:
 for k in req:
  if k not in f:errors.append([f['id'],'missing finding '+k])
 if f['status']!='candidate_pending_independent_counterevidence' or f['review_resolution']['final_required_confirmed']:errors.append([f['id'],'improper final confirmation'])
 for k in f['shared_contracts']:
  if k not in interfaces:errors.append([f['id'],'shared identity unresolved',k])
 for k in f['related_capabilities']:
  if k not in caps:errors.append([f['id'],'cap unresolved',k])
 for a in f['source_anchors']+f['spec_anchors']:
  base=R if a in f['source_anchors'] else W;path=base/a['path']
  if not path.exists():errors.append([f['id'],'missing anchor file',a['path']]);continue
  n=len(path.read_text(encoding='utf-8-sig').splitlines());lo,hi=a['lines']
  if not 1<=lo<=hi<=n:errors.append([f['id'],'bad anchor range',a])
for i in shared:
 if not i['source_anchors']:errors.append([i['id'],'shared no sources'])
 for a in i['specification_anchors']:
  if not Path(a['path']).exists():errors.append([i['id'],'missing shared doc'])
# Verify each nonblank main-document line belongs to a clause unit and each primary source's non-comment line to a semantic segment.
for p in rv['documents']:
 covered={k for c in p['clauses'] for k in range(c['lines'][0],c['lines'][1]+1)}
 missed=[i for i,s in enumerate(Path(p['path']).read_text().splitlines(),1) if s.strip() and i not in covered]
 if missed:errors.append([p['path'],'unmapped formal lines',missed])
for p in rd['sources']:
 if p.get('scope_role')!='primary_assigned':continue
 covered=set()
 for s in p['semantic_segments']:
  for a,b in s.get('line_ranges',[]) or ([s['lines']] if s.get('lines') else []):covered.update(range(a,b+1))
 missed=[i for i,s in enumerate((R/p['path']).read_text(encoding='utf-8-sig').splitlines(),1) if s.strip() and not s.lstrip().startswith('#') and i not in covered]
 if missed:errors.append([p['path'],'unmapped semantic source lines',missed])
 if not any(x['spec_clause_ids'] for x in next(x for x in fw['source_paths'] if x['path']==p['path'])['segments']):errors.append([p['path'],'no reverse primary link'])
vectors=[c['id'] for p in rv['test_documents'] for c in p['clauses'] if not c['id'].startswith('TESTMETA')]
if len(vectors)!=402:errors.append(['vector count expected 402',len(vectors)])
if len(vectors)!=len(set(vectors)):errors.append(['duplicate canonical vector IDs'])
result={'schema_version':'gr5.review.v1','module':'M09','validation_kind':'metadata_and_anchor_integrity_only','not_semantic_evidence_by_itself':True,'reference_or_model_execution':False,'errors':errors,'pass':not errors,'counts':{'primary_source_files':sum(x.get('scope_role')=='primary_assigned' and x['path'].endswith('.rb') for x in rd['sources']),'primary_pbs_files':sum(x.get('scope_role')=='primary_assigned' and x['path'].startswith('PBS/') for x in rd['sources']),'dependency_source_paths':sum(x.get('scope_role')!='primary_assigned' for x in rd['sources']),'formal_documents':len(rv['documents']),'formal_clause_units_including_navigation':len(clauses),'test_vectors':len(vectors),'registration_statements':len(regs),'behavioral_capabilities':len(caps),'capability_statuses':dict(collections.Counter(x['status'] for x in caps.values())),'shared_interfaces':len(shared),'original_drafts':len(rd['original_drafts'])},'known_lexical_copy_predecessor_absences':unseen,'all_primary_noncomment_lines_semantically_mapped':not any('unmapped semantic source lines' in e for e in errors),'all_formal_nonblank_lines_mapped':not any('unmapped formal lines' in e for e in errors),'scope_boundary':'完整性检查只防遗漏/断链；实质结论必须阅读手工分段比较与候选反证，不能把数量相等当语义通过。'}
(O/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
