#!/usr/bin/env python3
"""Documentation/identity checks only; does not execute reference or a behavior model."""
import hashlib, importlib.util, json, os, re, subprocess, tempfile, sys
sys.dont_write_bytecode=True
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('rebuild',ROOT/'rebuild-candidate.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def record(name,condition,detail):
 checks.append(dict(check=name,result='PASS' if condition else 'FAIL',detail=detail,evidence_level='TOOL_VALIDATION'))
 if not condition:raise AssertionError(name)
def main():
 c=json.loads(m.git('show',m.FREEZE+':'+m.CONTRACT));edit=json.loads((ROOT/'edits.json').read_text());fm=json.loads((ROOT/'fragment-manifest.json').read_text());vv=json.loads((ROOT/'derived-vectors.json').read_text())['vectors']
 required=c['required_ids'];operations=edit['operations'];groups={}
 for o in operations:groups.setdefault(o['target'],[]).append(o)
 record('finding-set',set(f for o in operations for f in o['finding_ids'])==set(required),'Exactly the frozen 14 required findings; optional/policy excluded.')
 record('vector-identities',len(vv)==len({v['id'] for v in vv}) and all(v['execution_status']=='NOT_EXECUTED_THIS_UPDATE' and v['evidence_level']=='DERIVED_VECTOR' for v in vv),{'derived_vectors':len(vv),'new_behavior_execution':0})
 for finding in required:
  actual={o['target'] for o in operations if finding in o['finding_ids']}
  record('sync-files/'+finding,actual==set(c['per_finding_formal_permissions'][finding]),sorted(actual))
 for target,ops in groups.items():
  b=m.git('show',m.B5+':'+target);s=b.decode()
  for o in ops:
   record('anchor/'+o['id'],s.count(o['before'])==1,{'target':target,'before_sha256':hashlib.sha256(o['before'].encode()).hexdigest()})
   s=s.replace(o['before'],o['after'],1)
  data=s.encode();p=next(p for p in fm['projection_files'] if p['target']==target)
  record('projection/'+target,m.identity(data)==p['projected'],'Complete projected bytes match deterministic edit result.')
  if target in c['candidate_direct_mirrors']:
   record('mirror/'+target,(m.REPO/c['candidate_direct_mirrors'][target]).read_bytes()==data,'Complete mirror compared.')
  for o in ops:
   if target in c['shared_fragment_outputs']:
    text=(m.REPO/c['shared_fragment_outputs'][target]).read_text();mark=o['id'];payload=text.split('<!-- BEGIN '+mark+' -->\n')[1].split('\n<!-- END '+mark+' -->')[0]
    record('fragment/'+mark,payload==o['after'],'Complete marker-delimited replacement matches edits.json.')
   for link in re.findall(r'\]\(([^)]+)\)',o['after']):
    if '://' in link or link.startswith('#'):continue
    import posixpath
    path=posixpath.normpath(posixpath.join(posixpath.dirname(target),link.split('#')[0]))
    r=subprocess.run(['git','cat-file','-e',m.B5+':'+path],cwd=m.REPO,capture_output=True)
    record('new-link/'+o['id']+'/'+link,r.returncode==0,'Target exists in immutable B5; contributed target is projected by this package if changed.')
 # Isolated index verifies the actual unified patch, without writing live formal files.
 with tempfile.TemporaryDirectory(prefix='r5-u02-patch-') as tmp:
  env=os.environ.copy();env['GIT_INDEX_FILE']=tmp+'/index'
  def run(*a):return subprocess.check_output(['git',*a],cwd=m.REPO,env=env)
  run('read-tree',m.B5);run('apply','--cached','--check',str(ROOT/'formal-diff.patch'));run('apply','--cached',str(ROOT/'formal-diff.patch'))
  changed=set(run('diff','--cached','--name-only',m.B5).decode().splitlines())
  record('patch-only-allowed-targets',changed==set(groups),{'changed_formal_projections':len(changed),'live_formal_writes':0})
  for target,p in [(p['target'],p) for p in fm['projection_files']]:
   record('patch-bytes/'+target,m.identity(run('show',':'+target))==p['projected'],'Independent patch application compared complete result bytes.')
  run('diff','--cached','--check')
 # Protect all prior catalog rows except seven intentional premise clarifications.
 exceptions={'MV24','FS14','FS16','DG10','DG38','BP13','T02'};changed_old=[];preserved_rows=0
 for target in groups:
  if '/test-catalog/' not in target:continue
  baseline=m.git('show',m.B5+':'+target).decode();projection=(Path('/tmp/r5-u02-projection')/target).read_text()
  from collections import Counter
  oldrows=[l for l in baseline.splitlines() if l.startswith('| ') and any(ch.isdigit() for ch in l.split('|')[1])]
  newrows=Counter(l for l in projection.splitlines() if l.startswith('| ') and any(ch.isdigit() for ch in l.split('|')[1]))
  for line in oldrows:
   key=line.split('|')[1].strip()
   if not newrows[line]:
    record('existing-row-qualified/'+key,key in exceptions,'Changed only named premise/receiver/repair boundary; old valid result retained.')
    changed_old.append(key)
   else:preserved_rows+=1;newrows[line]-=1
 record('prior-catalog-row-protection',set(changed_old)==exceptions,{'unchanged_rows':preserved_rows,'qualified_rows':sorted(changed_old)})
 # Rebuild is byte-stable; evidence metadata is not part of generated documentation.
 generated=[ROOT/'formal-diff.patch',ROOT/'fragment-manifest.json']+list((ROOT/'formal').rglob('*.md'))+list((ROOT/'fragments').rglob('*.md'))
 before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in generated}
 subprocess.check_output(['python',str(ROOT/'rebuild-candidate.py')],cwd=m.REPO)
 record('rebuild-idempotence',before=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in generated},{'generated_files':len(generated)})
 m.dump(ROOT/'validation-results.json',dict(schema='r5-u02.tool-validation.v1',new_behavior_execution=0,reference_execution=0,behavior_model_execution=0,host_demo_execution=0,status='PASS_TOOL_VALIDATION_ONLY',independent_review='NOT_PERFORMED_BY_AUTHOR',checks=checks))
 print(json.dumps({'checks':len(checks),'tool_result':'PASS','semantic_review':'PENDING_INDEPENDENT_REVIEW','new_behavior_execution':0}))
if __name__=='__main__':main()
