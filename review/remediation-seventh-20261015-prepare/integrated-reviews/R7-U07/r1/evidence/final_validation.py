"""Reviewer-owned byte checks. Does not execute reference or author programs."""
import pathlib, json, hashlib, subprocess, datetime, os
ROOT=pathlib.Path('/workspace/r7-ir-R7-U07-wave3')
REPO=ROOT/'result'
OUT=REPO/'review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U07/r1/evidence'
B='e646432c644dec04d306842cc5a559a29c718fbc'
MI='e54f54a2cb32e546eabd46aaf53ed45b30a8af89'
FI='b98fa82f8a08b5630ac568cbe8c34f607f623cfb'
def ident(d):
 return {'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'git_blob':hashlib.sha1(('blob '+str(len(d))+'\0').encode()+d).hexdigest()}
def git(*args):return subprocess.check_output(['git','-C',str(REPO),*args])
def save(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def check_identity(d,row):
 real=ident(d)
 for k,v in real.items():
  key=k if k in row else 'git_blob_content_id' if k=='git_blob' else k
  if key in row:assert row[key]==v,(k,row[key],v)
 return real
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'stage':'TOOL_VALIDATION_ONLY','tree_checks':[]}
for rev,path,want in [(B,'','84f79ec6e772aacbf3a464fde68cdc5a280e2950'),(B,'deliverables/final-specification-set','ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'),(MI,'','b3b6b166b69d2e4dc513cd8d72950b47306191fd'),(MI,'deliverables/final-specification-set','e1dfe28acd4f559b22da505238ef3a899aed4542'),(FI,'','eaf9f0831cea151c8a77ad716ad4c8fc5b71dc66')]:
 got=git('rev-parse',rev+(':'+path if path else '^{tree}')).decode().strip();assert got==want;result['tree_checks'].append({'commit':rev,'path':path,'tree':got})
restored=[]
for plan_name,dest in [('actual-plans/R7-U07.json','actual-input'),('original-plans/R7-U07.json','original')]:
 plan=json.loads((ROOT/plan_name).read_text());rows=[]
 for row in plan['artifacts']+plan['evidence']+plan['fixed_read_inputs']:
  data=(ROOT/dest/row['local_path']).read_bytes();real=check_identity(data,row)
  rows.append({'commit':row['commit'],'path':row['path'],'local_path':row['local_path'],**real})
 restored.append({'plan':plan_name,'files':len(rows),'bytes':sum(x['bytes'] for x in rows),'members':rows})
assert restored[0]['files']==185 and restored[0]['bytes']==4584535
assert restored[1]['files']==23 and restored[1]['bytes']==5526711
result['restorations']=restored
formal=json.loads((ROOT/'supplemental/FI/integrated-input.json').read_text())['all_formal_file_identities'];paths=set();changed=[];unchanged=[]
for row in formal:
 p=row['path'];paths.add(p);data=git('show',MI+':'+p);check_identity(data,row)
 base=git('show',B+':'+p);(changed if base!=data else unchanged).append(p)
 for location in [ROOT/'actual-input/actual'/p,ROOT/'supplemental/actual'/p]:
  if location.exists():assert location.read_bytes()==data
entries=git('ls-tree','-r','-z',MI,'deliverables/final-specification-set').split(b'\0');git_paths=set()
for entry in entries:
 if not entry:continue
 meta,p=entry.split(b'\t');mode,kind,blob=meta.split();assert mode==b'100644' and kind==b'blob';git_paths.add(p.decode())
assert paths==git_paths and len(paths)==131 and len(changed)==30 and len(unchanged)==101
def rebuild_tree(items):
 dirs={};files={}
 for p,blob in items:
  first,sep,rest=p.partition('/')
  if sep:dirs.setdefault(first,[]).append((rest,blob))
  else:files[first]=blob
 entries=[(n+'/',b'40000 '+n.encode()+b'\0'+bytes.fromhex(rebuild_tree(q))) for n,q in dirs.items()]
 entries.extend((n,b'100644 '+n.encode()+b'\0'+bytes.fromhex(blob)) for n,blob in files.items())
 body=b''.join(v for _,v in sorted(entries,key=lambda x:x[0].encode()))
 return hashlib.sha1(('tree '+str(len(body))+'\0').encode()+body).hexdigest()
recomputed_tree=rebuild_tree([(p.removeprefix('deliverables/final-specification-set/'),ident(git('show',MI+':'+p))['git_blob']) for p in sorted(paths)])
assert recomputed_tree=='e1dfe28acd4f559b22da505238ef3a899aed4542'
result['formal_scope']={'files':131,'changed_vs_B':changed,'unchanged_vs_B':unchanged,'full_git_bytes_match_FI_and_snapshots':True}
result['formal_scope']['tree_recomputed_from_all_file_bytes']=recomputed_tree
manifest_checks=[]
for dest,p in [('candidate','candidates/R7-U07/evidence/author/artifact-manifest.json'),('candidate-review','candidates/R7-U07/evidence/reviewer/r2/artifact-manifest.json')]:
 m=json.loads((ROOT/'actual-input'/dest/p).read_text());count=0
 for row in m['files']:
  data=(ROOT/'actual-input'/dest/row['path']).read_bytes();check_identity(data,row.get('after',row));count+=1
 manifest_checks.append({'path':p,'nonself_entries':count,'all_declared_bytes_match':True,'self_identity':ident((ROOT/'actual-input'/dest/p).read_bytes())})
assert [x['nonself_entries'] for x in manifest_checks]==[31,95]
result['input_manifests']=manifest_checks
candidate_git=[]
for dest,rev,want,count,prefix in [('candidate','2649ed2bd2cc3afdfa636cd643fc1975de5eae32','6b2e6a6122cb24b330a052137750dc985908e796',32,'candidates/R7-U07/'),('candidate-review','1bd0799d1819ef87c3c383a7f8e50d78756333c4','b82145b91a4f03999ec96b8cce0046982dab0b23',96,'candidates/R7-U07/evidence/reviewer/r2/')]:
 assert git('rev-parse',rev+'^{tree}').decode().strip()==want
 snapshot=ROOT/'actual-input'/dest
 members=sorted(str(p.relative_to(snapshot)) for p in snapshot.rglob('*') if p.is_file());assert len(members)==count
 diff=git('diff','--name-only','-z',B,rev).decode().strip('\0').split('\0');assert sorted(diff)==members
 for p in members:
  assert p.startswith(prefix) and git('show',rev+':'+p)==(snapshot/p).read_bytes()
 candidate_git.append({'commit':rev,'tree':want,'files':count,'complete_diff_vs_B_matches_snapshot':True,'full_Git_blob_bytes_match':True})
result['candidate_and_r2_complete_Git_comparison']=candidate_git
dispatch='72c93538d6e6cc15cb0be15ccfc3b8268d4b0af7';dispatch_path='review/remediation-seventh-20261015-prepare/integration/wave3/v1/dispatch/R7-U07-R7IR.md'
assert git('show',dispatch+':'+dispatch_path)==(ROOT/'bootstrap/contract.md').read_bytes()
result['dispatch_identity']={'commit':dispatch,'path':dispatch_path,'tree':git('rev-parse',dispatch+'^{tree}').decode().strip(),**ident(git('show',dispatch+':'+dispatch_path))}
approvals=[]
J=json.loads((ROOT/'actual-input/integration/applied-clauses.json').read_text())
for bind in J['new_source_bindings']+J['prior_source_bindings']:
 p=ROOT/'supplemental/approvals'/bind['id']/'per-id.json';j=json.loads(p.read_text());rows=[]
 for row in j['records']:
  rid=row.get('record_id',row.get('id'));verdict=next((row[k] for k in ['decision','verdict','conclusion'] if k in row),None);assert verdict=='PASS_SCOPED_CANDIDATE',(bind['id'],rid,verdict);rows.append({'id':rid,'original_candidate_verdict':verdict})
 assert set(x['id'] for x in rows)==set(bind['required_ids'])
 approvals.append({'batch':bind['id'],'candidate_commit':bind['candidate_commit'],'review_commit':bind['candidate_review_commit'],'review_per_id_identity':ident(p.read_bytes()),'review_report_identity':ident((p.parent/'report.md').read_bytes()),'records':rows,'current_scope':'Contribution preservation and compatibility only; no new semantics PASS for other batches'})
result['approval_alignment']=approvals
clauses=[]
for path,ranges in [('deliverables/final-specification-set/combat-requirements/wp55-facility-session-and-restoration.md',[(93,95),(126,126)]),('deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md',[(104,116)]+[(n,n) for n in range(110,116)])]:
 data=git('show',MI+':'+path);lines=data.splitlines(keepends=True)
 for start,end in ranges:
  a=sum(map(len,lines[:start-1]));z=sum(map(len,lines[:end]));d=data[a:z];clauses.append({'path':path,'lines_1_based_inclusive':[start,end],'byte_offsets_0_based_half_open':[a,z],**ident(d)})
result['U07_actual_clause_identities']=clauses
result['all_behavior']='NOT_EXECUTED'
save('final-byte-validation.json',result)
print(json.dumps({'formal_files':131,'changed':len(changed),'unchanged':len(unchanged),'restored':[x['files'] for x in restored],'input_manifests':[x['nonself_entries'] for x in manifest_checks],'approved_bindings':len(approvals),'clause_identities':len(clauses),'result':'PASS_TOOL_VALIDATION'},ensure_ascii=False))
