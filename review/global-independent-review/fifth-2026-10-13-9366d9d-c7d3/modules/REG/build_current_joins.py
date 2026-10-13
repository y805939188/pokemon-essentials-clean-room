"""Construct auditable candidate addresses; never transfers historic or fresh PASS."""
from current_evidence import *
D=json.loads((HERE/'regression-legacy-scope.json').read_text())
manual=json.loads((HERE/'manual_scope_selectors.json').read_text())
manual_caps=json.loads((HERE/'manual_capability_joins.json').read_text())
catalog_names={
'B01':['generic-kernel-wp02-03-04.md','generic-kernel-wp05-06-07-08-09-10.md'],
'B02':['generic-kernel-wp05-06-07-08-09-10.md'],
'B03':['engine-overworld-wp11-15-59-60.md'],
'B04':['engine-overworld-wp11-15-59-60.md','engine-overworld-wp16.md','user-interface-wp17-63-65-66-67-68-69-70-71.md'],
'B05':['creature-rpg-wp18-20-24-25-26.md','pokemon-rules-wp19-21-22-23-34.md'],
'B06':['creature-rpg-wp18-20-24-25-26.md','creature-rpg-wp27-28-29-30-33.md'],
'B07':['creature-rpg-wp27-28-29-30-33.md','pokemon-rules-wp31-32-37-38.md'],
'B08':['creature-rpg-wp27-28-29-30-33.md','creature-rpg-wp35-36-57-64-68.md','pokemon-rules-wp19-21-22-23-34.md','pokemon-rules-wp31-32-37-38.md'],
'B09':['combat-requirements-wp39-40-41-42-45.md','pokemon-rules-wp31-32-37-38.md'],
'B10':['pokemon-rules-wp43-44-46-48-50.md','combat-requirements-wp47-ab.md'],
'B11':['pokemon-rules-wp43-44-46-48-50.md','combat-requirements-wp49-51-52.md'],
'B12':['combat-requirements-wp49-51-52.md','pokemon-rules-wp53-60-61-62-69-70.md'],
'B13':['combat-requirements-wp54-55-56-58.md','creature-rpg-wp35-36-57-64-68.md'],
'B14':['engine-overworld-wp11-15-59-60.md','pokemon-rules-wp53-60-61-62-69-70.md'],
'B15':['user-interface-wp17-63-65-66-67-68-69-70-71.md','creature-rpg-wp35-36-57-64-68.md','pokemon-rules-wp53-60-61-62-69-70.md'],
'B16':['user-interface-wp17-63-65-66-67-68-69-70-71.md'],
'B17':['user-interface-wp17-63-65-66-67-68-69-70-71.md','demo-dx-wp72-73-74-75-76-77.md'],
'B18':['user-interface-wp17-63-65-66-67-68-69-70-71.md','creature-rpg-wp35-36-57-64-68.md'],
'B19':['demo-dx-wp72-73-74-75-76-77.md'],
'B20':['demo-dx-wp72-73-74-75-76-77.md'],'B21':[]}

filelist=subprocess.check_output(['git','-C',str(ROOT),'ls-tree','-r','--name-only',B,'deliverables/final-specification-set','specs','audit']).decode().splitlines()
for r in D['contributions']:
 b=r['batch_owner'];local=r['accepted_local_scope_fields'];iden=r['historical_identity_scope_reuse']['identity'];bind=r['historical_identity_scope_reuse']['fixed_scoped_disposition'];raw=pointer_get(history_obj(bind['commit'],bind['path']),bind['pointer'])
 if b=='B12':local['original_accepted_finite_basis']=raw['reused_candidate_evidence']
 if b=='B19':
  ep=local['original_formal_catalog_trace_coherence']['actual_internal_semantic_check']['path'];ev=history_obj(bind['commit'],ep);idx={x['ref']:x for x in ev['wp73a_actual_crosscheck']['fixed_files']};sc=local['exact_local_semantic_scope'];expanded=[]
  for _,o,_ in walk(sc):
   fid=o.get('actual_file',o.get('file'))
   if fid in idx and 'line_ranges' in o:expanded.append({**idx[fid],'lines':o['line_ranges']})
  if 'coherence_proof_pointer' in sc:
   checks=pointer_get(ev['wp72_actual_crosscheck'],sc['coherence_proof_pointer'])
   expanded += [{**a,'commit':iden['actual'],'lines':a['line_ranges']} for a in checks['range_checks']]
  local['resolved_ACT_scope_anchors']=expanded
  r['current_B5_navigation']['candidate_paths']=list(dict.fromkeys(x['path'] for x in expanded if x['path'].startswith('deliverables/')))
  r['current_B5_navigation']['original_paths']=list(dict.fromkeys(x['path'] for x in expanded if x['path'].startswith('specs/')))
 if b=='B01' and r['id']=='WP80-B02-R02':
  r['current_B5_navigation']['candidate_paths']=[]
  r['current_B5_navigation']['historical_administrative_scope']=local['accepted_candidate_paths']
 if b=='B02' and r['id']=='GIR-FD82-A017':r['current_B5_navigation']['current_audit_scope']=['audit/source-traceability.md']
 anchors=[];seen=set()
 def add(p,rs,method,selector,changed=None,role=None):
  if not p.startswith(('deliverables/','specs/','audit/')) or p not in filelist:return
  for rng in rs:
   if rng[0]<1 or rng[1]>len(lines(p)) or rng[0]>rng[1]:continue
   key=(p,*rng)
   if key in seen:continue
   seen.add(key);anchors.append({'path':p,'version':B,'lines':rng,'selector':selector,'historical_scope_role':role,'mapping_method':method,'changed_old_lines_unmapped':changed or [],'semantic_status':'not_reviewed','range_sha256':digest(('\n'.join(lines(p)[rng[0]-1:rng[1]])+'\n').encode())})
 # Explicit scoped locators; whole-file hashes are never mistaken for local scope.
 for group in [local,r['original_contribution_scope']]:
  for ptr,o,p in walk(group):
   if not p or p not in filelist:continue
   if '/original/' in ptr or '/original_affected_paths' in ptr:continue
   text=' '.join(str(o[k]) for k in ['section','section_number','heading','anchor','clause','clauses','selector'] if k in o)
   heads=matching_sections(p,text)
   if not heads and text:
    for h in section_ranges(p):
     if any(str(o.get(k,'' )).strip('# ').strip()==h['number'] for k in ['section','section_number','heading','anchor']):heads.append(h)
   if heads:
    for h in heads:add(p,[h['lines']],'same_named_current_section',text,role=o.get('role',o.get('scope_role')))
   else:
    rng=pairs(o.get('lines',o.get('line_ranges',o.get('line',[]))))
    if 'line_start' in o:rng=[[o['line_start'],o.get('line_end',o['line_start'])]]
    if rng:
     c=o.get('commit',iden['actual'])
     if c==B:add(p,rng,'explicit_B5_range',ptr,role=o.get('role',o.get('scope_role')))
     else:
      try:rr,changed=remap(p,c,rng);add(p,rr,'exact_unchanged_text_translation_from_'+c,ptr,changed,role=o.get('role',o.get('scope_role')))
      except subprocess.CalledProcessError:pass
  # Path literal followed by finite section references.
  for text in [v for _,o,_ in walk(group) for v in o.values() if isinstance(v,str)]:
   for m in re.finditer(r'((?:deliverables/final-specification-set|specs)/[^\s;；]+?\.md)\s*([^;；]*)',text):
    p,sel=m.groups()
    if p in filelist:
     for h in matching_sections(p,sel):add(p,[h['lines']],'path_and_current_section',sel)
 # WP-labelled bounded scope strings. Only link paths already explicitly assigned to this local contribution.
 text=json.dumps(local,ensure_ascii=False)
 for p in r['current_B5_navigation']['candidate_paths']:
  if p not in filelist:continue
  wp=re.match(r'wp(\d+)(?:-([abc]))?(?:-|\.)',Path(p).name)
  if not wp:continue
  num,part=wp.groups();pat=rf'WP{num}(?:[- ]?{part.upper()})?' if part else rf'WP{num}(?!\d)'
  for match in re.finditer(pat,text,re.I):
   tail=text[match.end():];tail=re.split(r'WP\d+|[；;\n\"→]',tail,maxsplit=1)[0]
   for h in matching_sections(p,tail):add(p,[h['lines']],'WP_label_named_section_candidate',tail)
 for basename,sections in manual.get(r['record_key'],{}).items():
  for p in filelist:
   if p.startswith('deliverables/') and Path(p).name==basename:
    for h in section_ranges(p):
     if h['number'] in sections:add(p,[h['lines']],'REG_named_finite_scope_selector',h['heading'])
 if r['record_key'] in ['B03/GIR-FD82-C038','B03/GIR-FD82-C042']:
  code='314' if r['id']=='GIR-FD82-C038' else '251'
  p='deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md'
  for n,t in enumerate(lines(p),1):
   if t.startswith('| '+code+' |'):add(p,[[n,n]],'exact_current_command_row',code)
 # IDs only identify static rows in a named current catalogue. This is navigation, not execution or adjudication.
 ids={x for x in re.findall(r'[A-Za-z0-9]+(?:[-/][A-Za-z0-9]+)*',str(r['current_B5_navigation']['static_vector_ids'])+' '+text) if re.search(r'[A-Z]',x) and re.search(r'\d',x)}
 catalogs=[p for p in r['current_B5_navigation']['candidate_paths'] if '/test-catalog/' in p]
 if not catalogs:
  catalogs=[p for p in filelist if '/test-catalog/' in p and Path(p).name in catalog_names[b]]
 if b=='B21' or (b=='B01' and r['id'] in ['GIR-FD82-001','WP80-B02-R02']) or (b=='B18' and r['id'] in ['GIR-FD82-001','WP80-INTAKE-R02']):catalogs=[]
 for p in catalogs:
  for n,line in enumerate(lines(p),1):
   if line.startswith('|'):
    cell=line.split('|')[1].strip().strip('`*')
    if cell in ids:add(p,[[n,n]],'exact_static_vector_identity',cell)
 r['current_B5_navigation']['clause_candidates']=anchors
 bounded={a['path'] for a in anchors}
 r['current_B5_navigation']['paths_still_needing_finite_selector']=[p for p in r['current_B5_navigation']['candidate_paths'] if p not in bounded]
 r['current_B5_navigation']['mapping_status']='candidate_addresses_generated_not_semantic_review'
 if b=='B08':
  loc=local['actual_clause_locator']; nums=set(re.findall(r'WP(\d+)',loc))
  nav=r['current_B5_navigation'];nav['batch_identity_context_paths']=nav['candidate_paths']
  nav['candidate_paths']=[p for p in nav['candidate_paths'] if '/test-catalog/' in p or (re.match(r'wp(\d+)',Path(p).name) and re.match(r'wp(\d+)',Path(p).name).group(1) in nums)]
  nav['read_only_consumer_contexts']=[]
  if 'READ_ONLY' in loc:
   p='deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md'
   nav['read_only_consumer_contexts'].append({'path':p,'version':B,'lines':[1,len(lines(p))],'scope':'WP34 body READ_ONLY in exact B08 A052 acceptance, no authored contribution/whole-ID signature','qualification_retained':True})
  nav['paths_still_needing_finite_selector']=[p for p in nav['candidate_paths'] if p not in bounded]

# Central contribution targets preserve exact local consumer projections, not whole-file signatures.
bykey={x['record_key']:x for x in D['contributions']}
suppver='e58486178e746273fb6fab55df00722807f1dc44'
suppath='review/remediation/20261003-prepare/batches/B21/author-draft-1/traceability.json'
sup=history_obj(suppver,suppath)
for r in D['contributions']:
 b=r['batch_owner']; nav=r['current_B5_navigation']
 if b=='B21':
  i,ss=next((i,v) for i,v in enumerate(sup['records']) if v['id']==r['id'])
  r['effective_current_scope_supplement']={'version':suppver,'path':suppath,'pointer':f'/records/{i}','author_revision':ss['author_revision'],'affected_boundary':ss['affected_boundary'],'static_cases':ss['static_case_navigation_not_executed'],'not_historical_verdict_transfer':True}
  r['delegated_consumer_contributions']=[{'record_key':v['record_key'],'pointer':'/contributions/'+str(j),'use':'Current R5 finite consumer projection; original scoped qualification retained, not transitive old PASS'} for j,v in enumerate(D['contributions']) if v['id']==r['id'] and v['batch_owner']!='B21']
  current=[]
  for v in D['contributions']:
   if v['id']==r['id'] and v['batch_owner']!='B21':
    current += [{**a,'projection_from':v['record_key']} for a in v['current_B5_navigation']['clause_candidates']]
  nav['clause_candidates']=current
  nav['candidate_paths']=list(dict.fromkeys(a['path'] for a in current if a['path'].startswith('deliverables/')))
 if (b=='B01' and r['id']=='GIR-FD82-001') or (b=='B21' and r['id'] in ['GIR-FD82-001','WP80-INTAKE-C01','WP80-INTAKE-R02']):
  for p in ['deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md']:
   nav['clause_candidates'].append({'path':p,'version':B,'lines':[1,len(lines(p))],'selector':'Current scope/index qualification only','mapping_method':'C00_full_current_semantic_scope','semantic_status':'not_reviewed','not_product_capability':True,'range_sha256':digest(('\n'.join(lines(p))+'\n').encode())})
 if (b in ['B02','B21'] and r['id']=='GIR-FD82-A017') or (b in ['B01','B21'] and r['id']=='WP80-B02-R02'):
  rs=[[130,144]] if r['id']=='GIR-FD82-A017' else [[220,232]]
  nav['administrative_current_anchors']=[{'path':'audit/source-traceability.md','version':B,'lines':rng,'role':'Current qualified source-navigation / original-material receiver'} for rng in rs]
 if b=='B18' and r['id']=='GIR-FD82-001':
  for p in nav['candidate_paths']:
   matches=[[i,i] for i,t in enumerate(lines(p),1) if 'audit/source-traceability.md' in t]
   for rr in matches:nav['clause_candidates'].append({'path':p,'version':B,'lines':rr,'selector':'root audit link','mapping_method':'exact_current_navigation_clause','semantic_status':'not_reviewed','not_product_capability':True,'range_sha256':digest((lines(p)[rr[0]-1]+'\n').encode())})
 if b=='B21' and r['id']=='GIR-FD82-C007':
  for p in filelist:
   if p.endswith('/wp75-project-conversion-and-authoring-tools.md'):
    for h in section_ranges(p):
     if h['number']=='8.6':nav['clause_candidates'].append({'path':p,'version':B,'lines':h['lines'],'selector':'B21 independently scoped new §8.6','mapping_method':'exact_current_new_scope','semantic_status':'not_reviewed','range_sha256':digest(('\n'.join(lines(p)[h['lines'][0]-1:h['lines'][1]])+'\n').encode())})
modules=['M01','M02','M03','M04','M05','M06','M07','M08','M09','M10','M11','M12','M12B','C00']
units=[];caps=[];manifest=[]
for m in modules:
 u,meta=fresh_units(m);units+=u;caps+=fresh_caps(m)
 if meta:manifest.append(meta)
# Stable selected-record snapshots retain what the address pointed to when joined.
pool={};
def pooladd(x,kind):
 key=digest([x['file'],x['file_sha256'],x['pointer'],x['record_sha256']]);pool[key]={'kind':kind,**x};return {'snapshot_id':key,'file':x['file'],'file_sha256':x['file_sha256'],'pointer':x['pointer'],'record_sha256':x['record_sha256'],'status_from_primary':x.get('status'),'use_boundary':'Fresh primary record; REG applicability review separately recorded.'}
for r in D['contributions']:
 ps=set(r['current_B5_navigation']['candidate_paths']);anchors=r['current_B5_navigation']['clause_candidates'];joins=[]
 for u in units:
  aas=[a for a in anchors if a['path']==u['path']]
  if not aas:continue
  if any(max(a['lines'][0],q[0])<=min(a['lines'][1],q[1]) for a in aas for q in u['ranges']):joins.append(pooladd(u,'inverse_clause'))
 r['current_R5_semantic_review']['fresh_evidence_joins']=joins
 r['current_R5_semantic_review']['status']='not_reviewed'
 r['current_R5_semantic_review']['reason']='Finite addresses matched; actual applicability/comparison review and primary completion gate still required. NOT missing_material.'
# Resolve canonical capabilities referenced by selected inverse units, or directly supported exact source ranges.
for r in D['contributions']:
 refs=r['current_R5_semantic_review']['fresh_evidence_joins'];js=[pool[x['snapshot_id']]['snapshot'] for x in refs];text=json.dumps(js,ensure_ascii=False);selected=[]
 ids_in_text=set(re.findall(r'[A-Za-z0-9_.-]+',text))
 for cap in caps:
  if cap['id'] in ids_in_text or cap['id'] in manual_caps.get(r['record_key'],[]):selected.append(pooladd(cap,'source_capability'))
 r['current_R5_semantic_review']['fresh_capability_joins']=selected
for r in D['controls']:
 subs=[x for x in D['contributions'] if x['id']==r['id']]
 r['current_B5_paths']=list(dict.fromkeys(p for x in subs for p in x['current_B5_navigation']['candidate_paths']))
 r['current_R5_semantic_review']['scope_mapping']='See all scoped contribution pointers; no union collapses local/NOT_AFFECTED qualifications.'
 r['current_R5_semantic_review']['fresh_evidence_joins']=list({x['snapshot_id']:x for s in subs for x in s['current_R5_semantic_review']['fresh_evidence_joins']}.values())
save('regression-legacy-scope.json',D)
save('fresh-evidence-snapshots.json',{**BASE,'complete':False,'boundary':'Selected current primary review records, with exact file and record hashes. Automatically selected addresses are not REG semantic review.','files':manifest,'records':pool})
print('Fresh selected snapshots',len(pool),'inverse units available',len(units))
for b in sorted(set(r['batch_owner'] for r in D['contributions'])):
 rs=[r for r in D['contributions'] if r['batch_owner']==b];print(b,len(rs),'anchors',sum(bool(r['current_B5_navigation']['clause_candidates']) for r in rs),'freshinverse',sum(bool(r['current_R5_semantic_review']['fresh_evidence_joins']) for r in rs),'unboundedpaths',sum(len(r['current_B5_navigation']['paths_still_needing_finite_selector']) for r in rs))
