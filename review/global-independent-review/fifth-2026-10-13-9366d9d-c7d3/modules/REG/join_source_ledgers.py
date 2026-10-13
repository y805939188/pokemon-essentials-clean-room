"""Join actual source facts/reading intervals to already selected fresh clauses. No review verdict generated."""
from current_evidence import *
D=json.loads((HERE/'regression-legacy-scope.json').read_text())
P=json.loads((HERE/'fresh-evidence-snapshots.json').read_text());pool=P['records']
reference_paths=set(subprocess.check_output(['git','-C',str(REF),'ls-tree','-r','--name-only',R]).decode().splitlines())
mods=['M01','M02','M03','M04','M05','M06','M07','M08','M09','M10','M11','M12','M12B','C00']
files={};ledger_index={};catalogs={};segments={};ledger_pool={};edges={};snapshot_edges={}
def esc(x):return str(x).replace('~','~0').replace('/','~1')
def pair_range(x):
 if isinstance(x,dict):return pairs(x.get('lines',x.get('line_ranges',x.get('ranges',[]))))
 return pairs(x)
def readranges(obj):
 result=[]
 for k in ['read_ranges','semantic_ranges','read_lines','lines','ranges','line_ranges','semantic_segments','segments']:
  v=obj.get(k,[])
  if isinstance(v,list):
   if v and isinstance(v[0],dict):result += [q for t in v for q in pair_range(t)]
   else:result+=pairs(v)
 return result
for m in mods:
 catalogs[m]={};segments[m]={}
 for name in ['source-to-spec.json','spec-to-source.json','reading-coverage.json']:
  p=HERE.parent/m/name
  if not p.exists():continue
  raw=p.read_bytes();d=json.loads(raw);meta={'path':str(p.relative_to(ROOT)),'sha256':digest(raw)};files[(m,name)]=(meta,d)
  if name=='reading-coverage.json':
   for k in ['sources','files','records']:
    for i,r in enumerate(d.get(k,[])):
     if isinstance(r,dict) and r.get('path'):
      addr={**meta,'pointer':f'/{k}/{i}','record_sha256':digest(r)};key=digest(addr)
      ledger_pool[key]={'address':addr,'primary_module':m,'record':r,'REG_use':'Actual named static semantic ranges/qualification only; no primary reference execution is credited to REG.'}
      ledger_index.setdefault((m,r['path']),[]).append(key)
  else:
   for key in ['source_anchor_catalog','source_anchor_index','source_anchor_groups']:
    cat=d.get(key,{})
    if isinstance(cat,dict):its=cat.items()
    else:its=[(v.get('anchor_id',v.get('id')),v) for v in cat]
    for cid,rec in its:
     if cid:catalogs[m][str(cid)]={'record':rec,'address':{**meta,'pointer':f'/{key}/{esc(cid)}' if isinstance(cat,dict) else f'/{key}/'+str(cat.index(rec))}}
   for i,s in enumerate(d.get('source_paths',[])):
    for j,t in enumerate(s.get('segments',[])):
     segments[m][t['id']]={'record':t,'path':s['path'],'address':{**meta,'pointer':f'/source_paths/{i}/segments/{j}'}}

def anchors(module,obj):
 result=[]
 for ptr,a,path in walk(obj):
  if path and path in reference_paths:
   if any(k in a for k in ['lines','line_ranges','ranges','symbol','entry','scope','entry_or_rule']):result.append((path,a,None))
  for key in ['source_anchor_ids','source_refs','source_anchor_refs','source_anchor_group_ref','source_mappings']:
   refs=a.get(key,[]);refs=refs if isinstance(refs,list) else [refs]
   for ref in refs:
    if not isinstance(ref,str):continue
    cid=ref.rsplit('/',1)[-1].rsplit('#',1)[-1]
    cat=catalogs[module].get(cid)
    if cat:
     for _,ar,ap in walk(cat['record']):
      if ap and ap in reference_paths:result.append((ap,ar,cat['address']))
  for sid in a.get('source_segment_ids',[]):
   if sid in segments[module]:
    seg=segments[module][sid];result.append((seg['path'],seg['record'],seg['address']))
 return result

def add_edge(m,p,a,evidence,indirect):
 rng=readranges(a);version=a.get('version',R)
 if version!=R:return None
 key=digest([m,p,version,rng,a.get('entry',a.get('symbol',a.get('entry_points','')))])
 if key not in edges:
  ls=ledger_index.get((m,p),[])
  if not ls:ls=[k for (mm,pp),vs in ledger_index.items() if pp==p for k in vs]
  edges[key]={'id':key,'source_path':p,'source_version':R,'source_ranges':rng,'source_entry_or_rule':a.get('entry',a.get('symbol',a.get('entry_points',a.get('semantic_scope',a.get('scope'))))),'primary_projection_module':m,'static_rule_or_comparison':a.get('supports',a.get('supporting_fact',a.get('comparison',a.get('rules_reviewed')))),'fresh_source_address':indirect,'reading_ledger_refs':ls,'current_evidence_snapshots':[],'proof_boundary':'Source semantic intervals and primary comparison only, no whole foreign file or historical acceptance implied.'}
 if evidence not in edges[key]['current_evidence_snapshots']:edges[key]['current_evidence_snapshots'].append(evidence)
 return key
for sid,s in pool.items():
 m=Path(s['file']).parent.name;joined=[]
 for p,a,addr in anchors(m,s['snapshot']):
  eid=add_edge(m,p,a,sid,addr)
  if eid and eid not in joined:joined.append(eid)
 snapshot_edges[sid]=joined
c00_admin={
'GIR-FD82-001':[0,1,2,13], 'GIR-FD82-A017':[13,16], 'WP80-B02-R02':[13,16], 'WP80-INTAKE-C01':[0,1,2,10,11], 'WP80-INTAKE-R02':[13,16,31]}
c00keys={ledger_pool[k]['address']['pointer']:k for k in ledger_pool if ledger_pool[k]['primary_module']=='C00'}
for r in D['contributions']:
 cr=r['current_R5_semantic_review'];sids=[x['snapshot_id'] for x in cr['fresh_evidence_joins']+cr['fresh_capability_joins']]
 cr['fresh_source_fact_refs']=list(dict.fromkeys(e for s in sids for e in snapshot_edges.get(s,[])))
 cr['fresh_source_fact_resolution']='fresh-source-ledger.json#/source_facts by id; every fact links exact source range and actual primary reading record, with static-only boundary'
 indexes=c00_admin.get(r['id'],[]) if r['batch_owner'] in ['B01','B02','B18','B21'] else []
 if r['batch_owner']=='B21':indexes=list(dict.fromkeys(indexes+[24,25,26,27,29,30,31]))
 cr['current_qualification_evidence']=[c00keys[f'/records/{i}'] for i in indexes if f'/records/{i}' in c00keys]
 cr['current_qualification_evidence_resolution']='fresh-source-ledger.json#/reading_records by id; CURRENT and fixed original qualification, not new product feature'
 nav=r['current_B5_navigation'];used={a['path'] for a in nav['clause_candidates']}
 nav['paths_still_needing_finite_selector']=[p for p in nav['candidate_paths'] if p not in used]
 nav['qualification_context_only']=[{'path':p,'version':B,'role':'whole-payload/source-navigation context, not a separate authored or whole-file behavioral contribution','finite_scope_authority':'accepted_local_scope_fields and fixed scoped disposition; never infer whole-file acceptance from a hash'} for p in nav['paths_still_needing_finite_selector']]
 nav['unresolved_authored_selectors']=[]
 if r['record_key']=='B08/GIR-FD82-C084':nav['read_only_consumer_contexts']=nav.get('read_only_consumer_contexts',[])+[{'path':'deliverables/final-specification-set/creature-rpg/wp36-wild-encounters-and-modifiers.md','version':B,'scope':'Generation dependency explicitly retained; no separate B08 authorship claim for whole WP36'}]
save('regression-legacy-scope.json',D)
save('fresh-source-ledger.json',{**BASE,'complete':False,'method':'Exact source anchor and current primary ledger joins. Selection is not semantic proof; manual per-contribution assessment remains separate. Primary execution records are never counted as REG execution.','source_facts':edges,'reading_records':ledger_pool,'snapshot_source_refs':snapshot_edges})
print('source facts',len(edges),'reading records',len(ledger_pool))
print('contributions no source fact',[(r['record_key'],bool(r['current_R5_semantic_review']['current_qualification_evidence'])) for r in D['contributions'] if not r['current_R5_semantic_review']['fresh_source_fact_refs']])
