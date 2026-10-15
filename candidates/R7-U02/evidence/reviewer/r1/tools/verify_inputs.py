"""Independent byte/range/scope checks, with no execution of restored programs."""
import datetime,difflib,hashlib,json,os,pathlib,shutil,subprocess
OUT=pathlib.Path(__file__).resolve().parents[1]
BOOT=pathlib.Path('/workspace/r7-review-bootstrap/R7-U02-r1')
CONTEXT=pathlib.Path('/workspace/r7-context/R7-U02-reviewer')
CAND=pathlib.Path('/workspace/r7-review-input/R7-U02-r1-84e2cca132ada38405657f19cbbd3d6891d4794f')
B='e646432c644dec04d306842cc5a559a29c718fbc'; C='84e2cca132ada38405657f19cbbd3d6891d4794f'; F='aa369555b0e8b6c8b077f964b54ed63d3b924f26'; D='95c260d8f3fb4a171675dde877137fcd4c2f1c8d'
def git(*args): return subprocess.check_output(['git',*args])
def identity(d): return {'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()}
def check(d,row):
 a=identity(d)
 for k,v in a.items():
  ek='git_blob_content_id' if k=='git_blob' and k not in row else k
  if ek in row: assert v==row[ek],(k,row,a)
 return a
freeze=json.loads((BOOT/'candidate-input.json').read_bytes())
assert freeze['candidate_commit']==C and freeze['candidate_tree']==git('rev-parse',C+'^{tree}').decode().strip()
assert git('rev-parse',F+'^{tree}').decode().strip()=='08bd0f362c74ef7645b5bbd70b557489c122ae29'
files=[]; declared={x['path']:x for x in freeze['candidate_and_author_evidence_file_identities']}
plan=json.loads((BOOT/'candidate-restore/R7-U02.json').read_bytes())
changed=git('diff','--name-only',B,C).decode().splitlines()
assert sorted(changed)==sorted(declared)==sorted(x['path'] for x in plan['artifacts'])
rawtree=git('ls-tree','-r',C,'candidates/R7-U02').decode().splitlines()
tree={line.split('\t',1)[1]:line.split('\t',1)[0].split() for line in rawtree}
for row in plan['artifacts']:
 p=row['path'];d=(CAND/row['local_path']).read_bytes(); a=check(d,row);check(d,declared[p])
 assert git('show',C+':'+p)==d
 assert tree[p]==['100644','blob',a['git_blob']]
 assert p.startswith('candidates/R7-U02/')
 files.append({'path':p,**a,'mode':'100644','git_tree_and_restored_and_freeze_match':True})
assert len(files)==63 and sum(x['bytes'] for x in files)==1088679
mirrors=[]
for row in files:
 p=row['path']; rel=p.removeprefix('candidates/R7-U02/')
 if rel.startswith('evidence/'): continue
 a=git('show',B+':'+rel);b=(CAND/'candidate'/p).read_bytes()
 ops=difflib.SequenceMatcher(None,a.splitlines(keepends=True),b.splitlines(keepends=True),autojunk=False).get_opcodes()
 edits=[{'kind':tag,'B_lines':[i+1,j],'candidate_lines':[k+1,l]} for tag,i,j,k,l in ops if tag!='equal']
 mirrors.append({'path':p,'base_path':rel,'B_identity':identity(a),'candidate_identity':identity(b),'edits':edits,'unchanged_blocks_exact_bytes':True})
origplan=json.loads(pathlib.Path('/workspace/r7-bootstrap/R7-U02-reviewer/recovery/batches/R7-U02.json').read_bytes())
original=[]
for row in origplan['artifacts']+origplan['evidence']+origplan['fixed_read_inputs']:
 d=(CONTEXT/row['local_path']).read_bytes();original.append({'path':row['local_path'],**check(d,row)})
bootstrap=[]
for fixed,p,local in [(D,'review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U02/reviewer-dispatch.md',BOOT/'reviewer-dispatch.md')]+[(F,'review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U02/'+p,BOOT/p) for p in ['candidate-input.json','candidate-restore/R7-U02.json','mirror-diffs.patch','remote-readback.json']]+[('658488c81f1f3181a488298ab27850c8af951d73','review/remediation-seventh-20261015-prepare/tools/restore_container_context.py',pathlib.Path('/workspace/r7-bootstrap/R7-U02-reviewer/tools/restore_container_context.py')),('658488c81f1f3181a488298ab27850c8af951d73','review/remediation-seventh-20261015-prepare/recovery/batches/R7-U02.json',pathlib.Path('/workspace/r7-bootstrap/R7-U02-reviewer/recovery/batches/R7-U02.json'))]:
 d=local.read_bytes();assert d==git('show',fixed+':'+p);bootstrap.append({'commit':fixed,'path':p,**identity(d),'git_object_match':True})
receipts=OUT/'restoration';receipts.mkdir(exist_ok=True)
for root,prefix in [(CONTEXT,'original'),(CAND,'candidate')]:
 for p in root.glob('recovery-receipt-*.json'): shutil.copyfile(p,receipts/(prefix+'-'+p.name))
for root,prefix in [(pathlib.Path('/workspace/r7-bootstrap/R7-U02-reviewer'),'restore-original'),(BOOT,'restore-candidate')]:
 for ext in ['stdout','stderr']: shutil.copyfile(root/(prefix+'.'+ext),receipts/(prefix+'.'+ext))
r={'schema':'r7.u02.independent-byte-validation.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'candidate_commit':C,'candidate_tree':freeze['candidate_tree'],'freeze_commit':F,'dispatch_commit':D,'B':B,'reviewer_context':os.environ.get('CODEX_THREAD_ID','NOT_EXPOSED'),'author_context':json.loads((CAND/'candidate/candidates/R7-U02/evidence/author/context.json').read_bytes())['actual_context_thread_id'],'candidate_files':files,'original_files':original,'bootstrap':bootstrap,'mirrors':mirrors,'complete_diff_scoped':True,'qualification':'TOOL_VALIDATION only; no semantic PASS or execution of source/author/native programs.'}
assert r['reviewer_context']!=r['author_context'] and r['reviewer_context']!='NOT_EXPOSED'
(OUT/'byte-validation.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'BYTES_SCOPE_IDENTITIES_VERIFIED','candidate_files':len(files),'candidate_bytes':sum(x['bytes'] for x in files),'original_files':len(original),'original_bytes':sum(x['bytes'] for x in original),'mirrors':mirrors,'different_exposed_contexts':True},ensure_ascii=False,indent=2))
