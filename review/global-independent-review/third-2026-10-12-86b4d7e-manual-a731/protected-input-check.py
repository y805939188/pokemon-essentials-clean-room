"""Read-only working-byte and identity checks; output only in the new report root."""
from pathlib import Path
import csv,json,hashlib,subprocess,datetime
OUT=Path(__file__).resolve().parent
REPO=OUT.parents[2]
def git(*a,cwd=REPO):return subprocess.check_output(['git',*a],cwd=cwd).decode().strip()
def identities(p):
 b=p.read_bytes();return len(b),hashlib.sha256(b).hexdigest(),hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
manifest=json.loads((REPO/'delivery/2026-10-11/baseline-identities.json').read_text())
baseline=json.loads((OUT/'baseline.json').read_text())
fail=[];groups={}
for group in ['formal131_files','frozen_current151_inputs','closure13_outputs','FINAL1_and_FINAL2_fourteen_complete_outputs','original_global_two_complete_outputs','original_approved_control']:
 rows=manifest[group];rows=rows if isinstance(rows,list) else [rows]
 for x in rows:
  try:
   actual=identities(REPO/x['path'])
   expected=(x['bytes'],x['sha256'],x['git_blob'])
   if actual!=expected:fail.append({'group':group,'path':x['path'],'actual':actual,'expected':expected})
  except Exception as e:fail.append({'group':group,'path':x['path'],'error':str(e)})
 groups[group]={'count':len(rows),'working_bytes_sha256_git_blob_match':not any(x.get('group')==group for x in fail)}
extra=baseline['extra_approved_coverage']
if identities(REPO/extra['path'])!=(extra['bytes'],extra['sha256'],extra['git_blob']):
 fail.append({'group':'extra_approved_coverage','path':extra['path']})
groups['extra_approved_coverage']={'count':1,'working_bytes_sha256_git_blob_match':not any(x.get('group')=='extra_approved_coverage' for x in fail)}
legacy=[]
for x in baseline['old_candidates']:
 try:
  size,sha,blob=identities(REPO/x['path']);ok=size==x['bytes'] and sha==x['sha256'];legacy.append({'path':x['path'],'match':ok})
  if not ok:fail.append({'group':'legacy_candidates','path':x['path']})
 except Exception as e:fail.append({'group':'legacy_candidates','path':x['path'],'error':str(e)})
reference=REPO/'reference/pokemon-essentials';refrows=list(csv.DictReader((OUT/'reference-file-inventory.tsv').open(),delimiter='\t'))
for x in refrows:
 try:
  size,sha,blob=identities(reference/x['path'])
  if (str(size),sha,blob)!=(x['bytes'],x['sha256'],x['git_blob']):fail.append({'group':'reference432','path':x['path']})
 except Exception as e:fail.append({'group':'reference432','path':x['path'],'error':str(e)})
tracked=git('diff','--name-only','86b4d7e1d8645e75af91a215240f8786a5bb4ca8')
illegal=[p for p in tracked.splitlines() if not p.startswith(str(OUT.relative_to(REPO))+'/')]
if illegal:fail.append({'group':'outside_report_tracked_diff','paths':illegal})
state={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'kind':'FINAL_PROTECTED_INPUT_READ_ONLY_CHECK','groups':groups,'reference432':{'count':len(refrows),'working_bytes_match':not any(x.get('group')=='reference432' for x in fail),'HEAD':git('rev-parse','HEAD',cwd=reference),'tree':git('rev-parse','HEAD^{tree}',cwd=reference),'dirty':git('status','--porcelain=v1',cwd=reference)},'old62':{'count':len(legacy),'all_exact_bytes_preserved':all(x['match'] for x in legacy),'records':legacy},'local':{'branch':git('rev-parse','--abbrev-ref','HEAD'),'HEAD':git('rev-parse','HEAD'),'tree':git('rev-parse','HEAD^{tree}'),'main':git('rev-parse','main'),'status':git('status','--porcelain=v1'),'outside_report_tracked_diff':illegal},'mismatches':fail,'behavior_execution':'NONE; file/Git/hash checks only'}
(OUT/'protected-input-check.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'groups':groups,'reference432':len(refrows),'legacy62_preserved':all(x['match'] for x in legacy),'mismatch_count':len(fail)},ensure_ascii=False))
if fail:raise SystemExit(1)
