"""Mechanical R7-U01 artifact checks. Never executes reference/behavior code."""
import argparse, datetime, difflib, gzip, hashlib, json, re, subprocess
from pathlib import Path
BASE='e646432c644dec04d306842cc5a559a29c718fbc'
REPO=Path(__file__).resolve().parents[4]
ROOT=REPO/'candidates/R7-U01'
EVIDENCE=ROOT/'evidence/author'
PREFIX='candidates/R7-U01/'
TARGETS=['audit/source-traceability.md','deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md','deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md','deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md','deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md','planning/feature-matrix.md']
def ident(data):
 return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
def git(*args):return subprocess.check_output(['git',*args],cwd=REPO)
def check_identity(data,expected):
 actual=ident(data)
 for k,v in actual.items():
  key='git_blob_content_id' if k=='git_blob' and 'git_blob_content_id' in expected else k
  if key in expected:assert v==expected[key],(key,v,expected[key])
 return actual

def main():
 p=argparse.ArgumentParser();p.add_argument('--context',type=Path);p.add_argument('--bootstrap',type=Path);p.add_argument('--write-manifest',action='store_true');a=p.parse_args()
 files=sorted(x for x in ROOT.rglob('*') if x.is_file())
 for f in files:assert not f.is_symlink()
 mirrors=sorted(str(f.relative_to(ROOT)) for f in files if EVIDENCE not in f.parents)
 assert mirrors==sorted(TARGETS),mirrors
 assert git('branch','--show-current').decode().strip()=='codex/r7-u01-author-20261015-pilot1'
 changes=git('diff','--name-only',BASE).decode().splitlines()+git('ls-files','--others','--exclude-standard').decode().splitlines()
 assert all(x.startswith(PREFIX) for x in changes),changes
 protected=git('diff',BASE,'--','.',':(exclude)candidates/R7-U01').decode();assert not protected
 assert git('rev-parse',BASE+':deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
 for target in TARGETS:assert (REPO/target).read_bytes()==git('show',BASE+':'+target)
 contribution=json.loads((EVIDENCE/'contributions.json').read_text())
 for row in contribution['files']:
  check_identity(git('show',BASE+':'+row['formal_target']),row['base'])
  check_identity((REPO/row['candidate_path']).read_bytes(),row['candidate'])
 for target in [TARGETS[0],TARGETS[3],TARGETS[4],TARGETS[5]]:
  old=git('show',BASE+':'+target);assert (ROOT/target).read_bytes().startswith(old),target
 per=json.loads((EVIDENCE/'per-id.json').read_text())
 assert [x['id'] for x in per['records']]==['GR7-M01-001','GR7-J01-001']
 expected=['GR7-M01-001-V'+str(i) for i in range(1,4)]+['J01-V'+str(i).zfill(2) for i in range(1,14)]
 vectors=[x for r in per['records'] for x in r['vectors']];assert [x['id'] for x in vectors]==expected
 catalog=(ROOT/TARGETS[4]).read_text();new_catalog=catalog.split('## R7-U01：',1)[1]
 for v in vectors:
  assert new_catalog.count('| '+v['id']+' |')==1
  assert v['behavior_execution']=='NOT_EXECUTED'
  loc=v['candidate_catalog'];line=(REPO/loc['path']).read_text().splitlines()[loc['lines'][0]-1];assert '| '+v['id']+' |' in line
 for r in per['records']:
  assert r['status']=='CANDIDATE_READY_NOT_REVIEWED' and all(r[k]=='NOT_REACHED' for k in ['independent_candidate_review','integrated_review','formal_acceptance','closed'])
  for loc in r['forward_map'].values():assert 1<=loc['lines'][0]<=loc['lines'][1]<=len((REPO/loc['path']).read_text().splitlines())
 assert per['conditional_targets']['adopted']==[]
 correction_path=EVIDENCE/'r1-correction/correction.json'
 correction_vectors=0
 if correction_path.exists():
  correction=json.loads(correction_path.read_text());prior=correction['previous_candidate_commit']
  assert prior=='de550bb9fe5d2b80312b1a4f6f166d2a6aa5fc67'
  old_per=json.loads(git('show',prior+':'+PREFIX+'evidence/author/per-id.json'))
  assert per['records'][0]==old_per['records'][0],'M01 reviewed contribution changed'
  assert per['records'][1]['vectors']==old_per['records'][1]['vectors'],'Original J01 vectors changed'
  changed=correction['change'];previous=git('show',prior+':'+changed['path'])
  assert previous.count(changed['old'].encode())==1
  assert (REPO/changed['path']).read_bytes()==previous.replace(changed['old'].encode(),changed['new'].encode()),'WP03 exceeded one-sentence correction'
  assert (ROOT/TARGETS[4]).read_bytes().startswith(git('show',prior+':'+PREFIX+TARGETS[4])),'Original catalog bytes changed'
  for target in [TARGETS[0],TARGETS[2],TARGETS[3],TARGETS[5]]:
   assert (ROOT/target).read_bytes()==git('show',prior+':'+PREFIX+target),'Unrelated mirror changed'
  assert ident(git('show',prior+':'+PREFIX+'evidence/author/artifact-manifest.json'))==correction['previous_author_manifest']
  expected_cases=[('R1-J01-DEFAULT-01',True,4000,4000,'present_record_field_default'),('R1-J01-DEFAULT-02',True,4000,4000,'present_record_explicit_field'),('R1-J01-CONTROL-01',True,5000,5000,'present_record_explicit_field'),('R1-J01-CONTROL-02',False,None,4000,'missing_record_fallback')]
  assert len(correction['vectors'])==len(expected_cases)
  for v,expected in zip(correction['vectors'],expected_cases):
   assert (v['id'],v['record_presence'],v['record_gauge_size'],v['expected_consumer_result'],v['value_origin'])==expected
   assert v['behavior_execution']=='NOT_EXECUTED' and catalog.count('| '+v['id']+' |')==1
   loc=v['candidate_catalog'];assert '| '+v['id']+' |' in (REPO/loc['path']).read_text().splitlines()[loc['lines'][0]-1]
   correction_vectors+=1
  assert correction['independent_new_candidate_review']=='NOT_REACHED' and not correction['ACCEPTED'] and not correction['CLOSED']
 # Validate new Markdown links against candidate snapshots, preserving preexisting links.
 anchor=lambda s: re.sub(r'[^\w\- ]','',s.lower(),flags=re.UNICODE).replace(' ','-')
 new_links=0
 for target in TARGETS:
  old=git('show',BASE+':'+target).decode().splitlines();new=(ROOT/target).read_text().splitlines()
  for tag,i,j,k,l in difflib.SequenceMatcher(None,old,new,autojunk=False).get_opcodes():
   if tag not in ['insert','replace']:continue
   for line in new[k:l]:
    for link in re.findall(r'\]\(([^)]+)\)',line):
     if '://' in link:continue
     path,_,fragment=link.partition('#');dest=(ROOT/target).parent/path
     assert dest.is_file(),(target,link)
     if fragment:assert fragment in [anchor(re.sub(r'^#+\s*','',h)) for h in dest.read_text().splitlines() if h.startswith('#')],link
     new_links+=1
 # Encoded, decoded, fixed snapshots and exact dispatch pointers are mechanical identities only.
 restored=raw_bindings=0
 if a.context:
  receipt=json.loads((EVIDENCE/'recovery-receipt.json').read_text());assert receipt['status']=='BOUNDED_RESTORE_BYTES_VERIFIED'
  for row in receipt['files']:check_identity((a.context/row['local_path']).read_bytes(),row);restored+=1
  assert restored==40 and sum(r['bytes'] for r in receipt['files'])==7539352
  extra=json.loads((EVIDENCE/'extra-source-receipt.json').read_text());check_identity((a.context/'inputs/reference'/extra['identity']['path']).read_bytes(),extra['identity'])
  for row in json.loads((EVIDENCE/'read-ledger.json').read_text())['files']:
   path=a.context/'inputs'/row['repository']/row['path'];check_identity(path.read_bytes(),row)
   for lo,hi in row['read_lines']:assert 1<=lo<=hi<=len(path.read_text().splitlines()),(row['path'],lo,hi)
 if a.bootstrap and a.context:
  plan=json.loads((a.bootstrap/'recovery/batches/R7-U01.json').read_text())
  for row in plan['evidence']:
   encoded=(a.context/'transport'/row['transport_path']).read_bytes();check_identity(encoded,row['encoded_identity']);check_identity(gzip.decompress(encoded),row)
  contract=json.loads((a.bootstrap/'dispatch/R7-U01.json').read_text());known={}
  for f in (a.context/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs').glob('*.raw'):known[hashlib.sha256(f.read_bytes()).hexdigest()]=f.read_bytes()
  refs=[]
  def walk(x):
   if isinstance(x,dict):
    if x.get('input_sha256') in known and 'raw_member_byte_offsets' in x:refs.append(x)
    for v in x.values():walk(v)
   elif isinstance(x,list):
    for v in x:walk(v)
  walk(contract)
  seen=set()
  for r in refs:
   key=(r['input_sha256'],r['json_pointer'],tuple(r['raw_member_byte_offsets']))
   if key in seen:continue
   seen.add(key);data=known[r['input_sha256']];lo,hi=r['raw_member_byte_offsets'];sl=data[lo:hi]
   assert len(sl)==r['raw_member_bytes'] and hashlib.sha256(sl).hexdigest()==r['raw_member_sha256']
   x=json.loads(data)
   for part in r['json_pointer'].split('/')[1:]:
    part=part.replace('~1','/').replace('~0','~');x=x[int(part)] if isinstance(x,list) else x[part]
   canonical=json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode();assert hashlib.sha256(canonical).hexdigest()==r['canonical_sha256'];raw_bindings+=1
 manifest_path=EVIDENCE/'artifact-manifest.json'
 rows=[]
 for f in files:
  if f==manifest_path:continue
  path=str(f.relative_to(REPO));row={'path':path,**ident(f.read_bytes())}
  rel=str(f.relative_to(ROOT))
  row['role']='candidate_mirror' if rel in TARGETS else 'author_evidence'
  row['base_target_identity']={'path':rel,**ident(git('show',BASE+':'+rel))} if rel in TARGETS else None
  rows.append(row)
 if a.write_manifest:
  manifest_path.write_text(json.dumps({'schema':'r7.u01-author-artifact-manifest.v1','base_commit':BASE,'status':'CANDIDATE_READY_NOT_REVIEWED','files':rows,'self_identity':'artifact-manifest.json cannot contain its own content hash. Its complete bytes/blob are bound by actual Git commit/tree and external final remote readback. All other artifacts are enumerated exactly.','integration':'Candidate mirrors are complete B files but only exact contribution clauses may be integrated by R7-I.','effective_configuration':'UNVERIFIED'},ensure_ascii=False,indent=2)+'\n')
 else:
  manifest=json.loads(manifest_path.read_text());assert manifest['files']==rows,'Artifact manifest stale'
 print(json.dumps({'status':'MECHANICAL_CHECKS_OK_NOT_SEMANTIC_PASS','mirrors':len(mirrors),'vectors':len(vectors),'r1_correction_vectors':correction_vectors,'new_links_checked':new_links,'restored_files_verified':restored,'raw_pointer_bindings_verified':raw_bindings,'formal_paths_unchanged':True,'manifest_members_excluding_self':len(rows),'reference_behavior_executed':False,'independent_candidate_review':'NOT_REACHED'},ensure_ascii=False))
if __name__=='__main__':main()
