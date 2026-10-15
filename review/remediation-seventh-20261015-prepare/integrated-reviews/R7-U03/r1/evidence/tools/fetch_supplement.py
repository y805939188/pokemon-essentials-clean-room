import json,subprocess,urllib.request,urllib.parse,hashlib,gzip,datetime,os
from pathlib import Path
root=Path('/workspace/r7-ir-R7-U03-final');dst=root/'supplement';dst.mkdir(exist_ok=True)
receipt=[]
def identity(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob_content_id=hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest())
def get(repo,c,p,local,expected=None,compressed=False):
 url=f'https://raw.githubusercontent.com/{repo}/{c}/'+urllib.parse.quote(p);start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'R7-U03-independent-static-review'}),timeout=40) as r:b=r.read(4000000);status=r.status
 if compressed:b=gzip.decompress(b)
 actual=identity(b)
 if expected:
  for k,v in expected.items():assert actual[k]==v,(local,k,actual[k],v)
 elif repo=='y805939188/pokemon-essentials-clean-room':assert b==subprocess.check_output(['git','show',c+':'+p],cwd='/workspace/pokemon-essentials-clean-room')
 target=dst/local;target.parent.mkdir(parents=True,exist_ok=True)
 if target.exists():assert target.read_bytes()==b
 else:target.write_bytes(b)
 receipt.append(dict(repository=repo,commit=c,path=p,local_path=str(target),url=url,start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),tool_pid=os.getpid(),http_status=status,**actual))
 (root/'audit/supplement-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
B='e646432c644dec04d306842cc5a559a29c718fbc';MI='94d5eb73f4508b8a8a54319040faa9aea5752059';repo='y805939188/pokemon-essentials-clean-room';prefix='review/remediation-seventh-20261015-prepare/'
for p in ['deliverables/final-specification-set/engine-overworld/wp13-move-route-matrix.md','deliverables/final-specification-set/creature-rpg/wp33-daycare-and-breeding-session.md']:
 for c,label in [(B,'baseline'),(MI,'actual')]:get(repo,c,p,label+'/'+p)
for p in ['integration/wave4/v1/integrated-input.json','integration/wave4/v1/dispatch/R7-U03-R7IR.md']:
 get(repo,'6a02773d62e36a295e9701a8d0ba5b5cb6441614' if p.endswith('integrated-input.json') else '5325e8046f4d625b855e3c216abaa650805fab5e',prefix+p,p)
for u in ['R7-U01','R7-U09','R7-U13']:get(repo,'f622356f3beb9e84ea8cff9db07c7fb382565d3f',prefix+'delegation/contracts/'+u+'.json','shared-contracts/'+u+'.json')
for f in ['report.md','per-id.json','review-input-receipt.json','artifact-manifest.json']:get(repo,'e75aa46a17e99bcc17795e051461a727c795aa6c','candidates/R7-U03/evidence/reviewer/r1/'+f,'prior-r1/'+f)
p='review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M03/spec-coverage.tsv';get(repo,B,p,'history/spec-coverage.tsv')
prov=json.loads((root/'actual-input/candidate-review/candidates/R7-U03/evidence/reviewer/r2/provenance-audit.json').read_text())
for r in prov['supplemental_reference']:
 get('Maruno17/pokemon-essentials',r['fixed_R'],r['path'],'reference/'+r['path'],{k:r[k] for k in ['bytes','sha256']}|{'git_blob_content_id':r['git_blob']})
bindings=json.loads((root/'original/evidence/tasks/R7-C13/raw-binding-manifest.json').read_text())
for r in bindings:
 if r['report_relative_path'] in ['inventory/formal.json','inventory/source.json','tasks/R7-C04/inputs/M05-findings.received.json','tasks/R7-C04/inputs/M06-findings.received.json','evidence/proposal-successor-deltas-C04-C06.json']:
  sha=r['sha256'];p='review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/objects/'+sha[:2]+'/'+sha+'.gz'
  get(repo,'4580645dfbfec4a3c7ccbad56ae293cc619b0d25',p,'original-bound/'+r['report_relative_path'],{k:r[k] for k in ['bytes','sha256']}|{'git_blob_content_id':r['content_git_blob']},True)
print(json.dumps(dict(files=len(receipt),bytes=sum(r['bytes'] for r in receipt),all_complete=True)))
