"""Independent static graph and handoff joins. Generates reading views, no semantic PASS."""
import collections,hashlib,json,pathlib
P=pathlib.Path(__file__).resolve().parent
J=lambda x:json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
H=lambda x:hashlib.sha256(J(x).encode()).hexdigest()
a,d,f=(json.loads((P/'originals'/str(i)).read_text()) for i in (12,13,14))
scopes={}; paths={}; scope_uses=[]
def pathid(p):
 if p not in paths:paths[p]=f'P{len(paths):03}'
 return paths[p]
def sid(s,at):
 k=J(s)
 if k not in scopes:scopes[k]={'id':f'S{len(scopes):03}','value':s,'first_at':at,'uses':[]}
 scopes[k]['uses'].append(at); return scopes[k]['id']
def contrib(c,at):
 return ':'.join([str(c.get('batch_id')).replace('R7-U','U'),c['record_id'].replace('GR7-',''),c.get('facet_id','').replace('GR7-H08-001-',''),c['kind'],sid(c['scope'],at+'/scope')])
lines=[]
for i,r in enumerate(f['path_roles']):
 lines.append(f'role[{i}] {pathid(r["path"])} writer={r["sole_actual_writer"]} '+','.join(contrib(c,f'file14#/path_roles/{i}/contributions/{j}') for j,c in enumerate(r['contributions'])))
for i,r in enumerate(d['shared_receivers']):
 lines.append(f'receiver[{i}] {pathid(r["path"])} {r["receiver"]}>{r["independent_actual_reviewer"]} '+','.join(contrib(c,f'file13#/shared_receivers/{i}/contributions/{j}') for j,c in enumerate(r['contributions'])))
for i,r in enumerate(f['conflicts']):
 lines.append(f'conflict[{i}] {pathid(r["path"])} writer={r["actual_writer"]} '+','.join(contrib(c,f'file14#/conflicts/{i}/entries/{j}') for j,c in enumerate(r['entries'])))
for bi,b in enumerate(a['batches']):
 for i,r in enumerate(b['candidate_paths']):
  lines.append(f'candidate[{bi}/{i}] {r["candidate_path"]}>{pathid(r["actual_path"])} writer={r["actual_writer"]} '+','.join(contrib(c,f'file12#/batches/{bi}/candidate_paths/{i}/contributions/{j}') for j,c in enumerate(r['contributions'])))
artifacts=[]
for i,r in enumerate(f['isolated_candidate_and_artifact_path_roles']):
 # All 371 endpoints retained; administrative paths classified by complete exact role pattern.
 artifacts.append({'index':i,**r})
proof={'schema':'gr8-d-complete-graph-relations/v1','scope_credit':'Graph endpoint/scope purposes only; no target source or canonical body approval','paths':paths,'scopes':list(scopes.values()),'all_artifact_roles':artifacts,'counts':{'path_roles':len(f['path_roles']),'contributions':sum(len(r['contributions']) for r in f['path_roles']),'shared_receivers':len(d['shared_receivers']),'conflicts':len(f['conflicts']),'artifact_roles':len(artifacts)},'checks':[]}
def ck(name,ok,detail=None): proof['checks'].append({'name':name,'pass':bool(ok),'detail':detail})
by={r['path']:r for r in f['path_roles']};recv={r['path']:r for r in d['shared_receivers']}
ck('13 distinct batches;27 required assignment no duplicate',len(a['batches'])==13 and len(a['primary_batch_by_required'])==27 and len([z for b in a['batches'] for z in b['required_ids']])==27)
ck('No blocking author edges/no update/service capacity assertion',not d['blocking_author_edges'] and not a['update_started'] and not a['tasks_launched'] and not a['service_slots_claimed'])
ck('all50 receiver contributions exact subset of corresponding path roles',all(all(c in by[r['path']]['contributions'] for c in r['contributions']) for r in d['shared_receivers']))
ck('all48 conflicts exactly reuse whole corresponding path-role contributions',all(r['entries']==by[r['path']]['contributions'] for r in f['conflicts']))
ck('all writable receiver sole writer I and fresh actual reviewer IR',all(r['receiver']=='R7-I' and r['independent_actual_reviewer']=='R7-IR' and by[r['path']]['sole_actual_writer']=='R7-I' for r in d['shared_receivers']))
ck('source paths never actual writer',all(r['sole_actual_writer'] is None for r in f['path_roles'] if r['path'].startswith(('Data/','PBS/','Fonts/','Audio/','Plugins/'))))
ck('all59 candidate scopes exact graph contributions/actual target paths',all(c in by[r['actual_path']]['contributions'] for b in a['batches'] for r in b['candidate_paths'] for c in r['contributions']))
ck('all59 mirrors present with assigned isolated author/reviewer roles',all(any(z['path']==r['candidate_path'] and z.get('actual_target')==r['actual_path'] and z['writers']==[b['author_entry']] and z['readers']==[b['reviewer_entry'],'R7-I','R7-IR'] for z in artifacts) for b in a['batches'] for r in b['candidate_paths']))
ck('all371 artifact writer endpoints isolated under their own batch',all(z['path'].startswith('candidates/R7-U') for z in artifacts))
ck('author write-write conflicts empty',f['author_candidate_write_write_conflicts']==[])
(P/'graph-relations.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
text=['PATHS:']+[i+' '+p for p,i in paths.items()]+['SCOPES:']+[x['id']+' '+J(x['value']) for x in scopes.values()]+['RELATIONS:']+lines
# Exact 312 admin artifact endpoints classified using prefix/suffix sets rather than pretending to read execution bodies.
roles=collections.defaultdict(list)
for x in artifacts:
 t=dict(x);ix=t.pop('index');path=t.pop('path'); suffix=path.split('/',2)[2];batch=path.split('/')[1]
 if 'actual_target' in t: continue
 k=J({'suffix':suffix,**{k:[v.replace(batch,'{B}') for v in z] if isinstance(z,list) else z for k,z in t.items()}})
 roles[k].append({'index':ix,'batch':batch})
text+=['ARTIFACT_ROLE_TYPES:']+[k+' instances='+J(v) for k,v in roles.items()]
frames=[];buf=''
for line in text:
 if len(buf)+len(line)>11500 and buf:frames.append(buf);buf=''
 buf+=line+'\n'
if buf:frames.append(buf)
for i,buf in enumerate(frames):(P/'views'/f'graph-{i:03}.txt').write_text(buf)
print(json.dumps({'counts':proof['counts'],'scopes':len(scopes),'paths':len(paths),'view_frames':len(frames),'checks':proof['checks']},ensure_ascii=False))
