from current_evidence import *
mods={f'M{i:02d}':f'M{i:02d}' for i in range(1,13)}
own=json.loads((HERE/'source-to-spec.json').read_text())['capabilities']
source_by_id={r['historical_control']:r for r in own}
selected_ids=json.loads((HERE/'finite_scope_selection.json').read_text())
r3paths={}
for z in jfixed(R3PATH)['records']:
 r3paths[z['id']]={q.get('formal_path',q.get('path')) for q in z['formal_clauses'] if isinstance(q,dict)}
r4prefixes={
'GR4-M01-001':['wp08-'], 'GR4-M01-002':['wp08-','wp17-'],
'GR4-M02-001':['wp06-','wp09-'], 'GR4-M02-002':['wp07-','wp64-'], 'GR4-M02-003':['wp06-'],
'GR4-M03-001':['wp12-','wp13-move-route'], 'GR4-M03-002':['wp11-','wp12-','wp16-world','wp59-'], 'GR4-M03-003':['wp13-'],
'GR4-M04-001':['wp18-','wp15-','wp21-','wp35-','wp66-a-'], 'GR4-M05-001':['wp28-'], 'GR4-M06-001':['wp34-'],
'GR4-M10-001':['wp17-','wp65-','wp13-'], 'GR4-M10-002':['wp15-','wp17-','wp65-'], 'GR4-M10-003':['wp17-','wp66-a-'], 'GR4-M10-004':['wp67-a-','wp74-'],
'GR4-M11-001':['wp62-','wp66-b-'],'GR4-M12-001':['wp73-b-','wp36-']}
def relevant_formal(fid,path):
 if '/test-catalog/' in path:return True
 if fid.startswith('GR3-'):return path in r3paths[fid]
 return any(Path(path).name.startswith(p) for p in r4prefixes[fid])
cache={};snapshots={};ledgers={}
for module in list(mods)+['M12B']:
 caps=fresh_caps(module);units,meta=fresh_units(module);cache[module]=(caps,units)
 p=HERE.parent/module/'reading-coverage.json'
 if p.exists():
  raw=p.read_bytes();ledgers[module]=(str(p.relative_to(ROOT)),digest(raw),json.loads(raw))
def overlap(a,b):return any(max(x[0],y[0])<=min(x[1],y[1]) for x in a for y in b)
def snap(x,kind):
 key=digest([x['file'],x['file_sha256'],x['pointer'],x['record_sha256']]);snapshots[key]={'kind':kind,**x}
 return {k:x[k] for k in ['file','file_sha256','pointer','record_sha256']}|{'snapshot_id':key,'status_from_primary':x.get('status')}
for name in ['regression-fourth-17.json','regression-third-23.json']:
 d=json.loads((HERE/name).read_text())
 for r in d['records']:
  module=r['id'].split('-')[1];ms=list(cache);reg=source_by_id[r['id']];sources={a['path']:pairs(a['lines']) for a in reg['source_anchors']};specs={a['path']:pairs(a['lines']) for a in reg['spec_anchors']};cc=[];uu=[];rr=[]
  for m in ms:
   caps,units=cache[m]
   for c in caps:
    found=[]
    for _,a,p in walk(c['snapshot'].get('source_anchors',[])):
     rng=pairs(a.get('lines',a.get('line_ranges',[])))
     if p in sources and rng and overlap(rng,sources[p]):found.append(p)
    if c['id'] in selected_ids.get(r['id'],[]):cc.append(snap(c,'source_capability')|{'overlapping_REG_source_paths':list(dict.fromkeys(found))})
   for u in units:
    if u['path'] in specs and relevant_formal(r['id'],u['path']) and overlap(u['ranges'],specs[u['path']]):uu.append(snap(u,'inverse_clause'))
   if m in ledgers:
    fn,sha,l=ledgers[m]
    for ptr,o,p in walk(l):
     if p in sources and len(ptr.strip('/').split('/'))==2 and any(k in o for k in ['review_extent','semantic_ranges','segments','read_ranges','ranges']):rr.append({'file':fn,'file_sha256':sha,'pointer':ptr,'record_sha256':digest(o),'path':p,'review_extent':o.get('review_extent'),'REG_requested_ranges':sources[p]})
  chosenpaths={p for c in cc for _,a,p in walk(snapshots[c['snapshot_id']]['snapshot'].get('source_anchors',[])) if p}
  context_rr=[a for a in rr if a['path'] not in chosenpaths];rr=[a for a in rr if a['path'] in chosenpaths]
  r['current_R5_semantic_review']['fresh_global_review_join']={'status':'mapped_pending_final_integrity_check','capability_selection':'REG curated exact semantic role; unrelated source-file overlaps excluded','source_capabilities':cc,'inverse_clauses':uu,'reading_ledger':rr,'related_context_ledger_not_primary_signature':context_rr,'boundary':'REG direct source/spec criterion judgments above remain independent; address overlap alone not semantic corroboration and not source whole-file signoff.'}
 save(name,d)
save('finite-fresh-snapshots.json',{**BASE,'complete':False,'records':snapshots})
for name in ['regression-fourth-17.json','regression-third-23.json']:
 d=json.loads((HERE/name).read_text());print(name)
 for r in d['records']:
  j=r['current_R5_semantic_review']['fresh_global_review_join'];print(r['id'],len(j['source_capabilities']),len(j['inverse_clauses']),len(j['reading_ledger']))
