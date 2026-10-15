import json,hashlib,subprocess,difflib
from pathlib import Path
ROOT=Path('/workspace/r7-ir-R7-U11');OUT=Path(__file__).resolve().parents[1];REPO=ROOT/'review-checkout'
def git(*a):return subprocess.check_output(['git',*a],cwd=REPO)
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def check(b,r):assert ident(b)==r,(ident(b),r)
j=json.loads((ROOT/'actual-input/integration/applied-clauses.json').read_text());result=[]
for f in j['files']:
 exists=subprocess.run(['git','cat-file','-e',j['fixed_B']+':'+f['path']],cwd=REPO,stderr=subprocess.DEVNULL).returncode==0
 if not exists: assert f['path']=='review/remediation-seventh-20261015-prepare/current-navigation-errata.json' and f['baseline_identity']['bytes']==0
 base=git('show',j['fixed_B']+':'+f['path']) if exists else b''
 check(base,f['baseline_identity']);lines=base.decode().splitlines(keepends=True)
 cur=0;parts=[];hs=[]
 for h in sorted(f['hunks'],key=lambda h:(h['base_line_indices_half_open'][0],h['batch_order'])):
  a,b=h['base_line_indices_half_open'];assert a>=cur,(f['path'],a,cur)
  removed=''.join(lines[a:b]).encode();added=h['added_text'].encode();assert removed==h['removed_text'].encode();check(removed,h['removed_identity']);check(added,h['added_identity'])
  # Candidate transport independently verified by fixed raw restore and Git where available.
  own=(ROOT/'actual-input/candidate'/h['candidate_path'])
  shared=ROOT/'actual-input/shared-candidate'/h['batch_id']/f['path']
  candidate=own if own.exists() else shared if shared.exists() else None
  if candidate:
   c,d=h['candidate_line_indices_half_open'];assert ''.join(candidate.read_text().splitlines(keepends=True)[c:d]).encode()==added
   assert candidate.read_bytes()==git('show',h['candidate_commit']+':'+h['candidate_path'])
  parts.append(''.join(lines[cur:a]));parts.append(h['added_text']);cur=b
  hs.append({'batch':h['batch_id'],'base_lines_zero_half_open':[a,b],'actual_lines_zero_half_open':h['actual_final_line_indices_half_open'],'added_identity':h['added_identity'],'candidate_slice_compared':candidate is not None})
 parts.append(''.join(lines[cur:]));assembled=''.join(parts).encode();check(assembled,f['assembled_candidate_clauses_identity'])
 expected=assembled
 for adj in j['root_administrative_reception_adjustments']:
  if adj['path']==f['path'] and 'added_text' in adj:check(expected,adj['before_identity']);expected+=adj['added_text'].encode();check(expected,adj['after_identity'])
 actual=git('show','45c80832a41c1b56dcd7e9d93497758cbb7721de:'+f['path'])
 if f['path'].endswith('current-navigation-errata.json'):
  before=json.loads(expected);after=json.loads(actual)
  diff=list(difflib.unified_diff(expected.decode().splitlines(),actual.decode().splitlines(),n=1))
 else: assert expected==actual
 result.append({'path':f['path'],'identity':ident(actual),'hunks':hs,'exact_reconstruction':expected==actual,'administrative_diff':diff if f['path'].endswith('current-navigation-errata.json') else None})
shared=[]
for s in json.loads((ROOT/'actual-plans/R7-U11.json').read_text())['shared_preservation_checks']:
 f=next(f for f in result if f['path']==s['path']);own=[h for h in f['hunks'] if h['batch']==s['other_batch']];assert own
 shared.append({**s,'hunks':own,'receiver':'R7-I exact-clause assembly; this IR checks preservation/compatibility only, no new semantic PASS for other IDs'})
(OUT/'clause-reconstruction.json').write_text(json.dumps({'files':result,'shared_preservation':shared,'same_boundary_insertions':j['same_boundary_insertions'],'qualification':'Byte reconstruction does not replace semantic reading.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'targets':len(result),'hunks':sum(len(f['hunks']) for f in result),'shared_checks':len(shared),'exact_reconstruction_targets':sum(f['exact_reconstruction'] for f in result)}))
