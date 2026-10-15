"""Bounded supplementary fixed Git/HTTPS reads; never execute downloaded inputs."""
import datetime,hashlib,json,subprocess,urllib.request
from pathlib import Path
E=Path(__file__).resolve().parent;root=Path('/workspace/r7-u07-reviewer-r2');base='e646432c644dec04d306842cc5a559a29c718fbc'
def ident(d):return {'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()}
rows=[]
for path,spans in [('deliverables/final-specification-set/creature-rpg/wp57-factory-rentals-and-swaps.md',[(9,57),(87,116)]),('deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md',[(70,90)]),('deliverables/final-specification-set/combat-requirements/wp39-battle-context-and-participants.md',[(1,95)])]:
 d=subprocess.check_output(['git','show',base+':'+path],cwd=root);assert d==(root/path).read_bytes()
 rows.append({'repository':'y805939188/pokemon-essentials-clean-room','commit':base,'path':path,**ident(d),'semantic_read_ranges':spans,'qualification':'New finite static read; no entire domain or runtime certification'})
 print(json.dumps(rows[-1],ensure_ascii=False))
 for lo,hi in spans:
  for n,line in enumerate(d.decode().splitlines()[lo-1:hi],lo):print(f'{n:04}: {line}')
# Preserve old r1 bytes and administrative facts only, after fresh current-version source/candidate review.
commit='c651d5599badf5fb9f99c05d307f1d7d70374ab7'
for name in ['report.md','per-id.json','review-input-receipt.json','artifact-manifest.json']:
 path='candidates/R7-U07/evidence/reviewer/r1/'+name
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+path
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with urllib.request.urlopen(url,timeout=60) as resp:d=resp.read();status=resp.status
 dest=E/'prior-r1'/name;dest.parent.mkdir(exist_ok=True)
 if dest.exists():assert dest.read_bytes()==d
 else:dest.write_bytes(d)
 rows.append({'repository':'y805939188/pokemon-essentials-clean-room','commit':commit,'path':path,'http_status':status,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),**ident(d),'purpose':'Retain old PASS plus prohibited-helper disclosure and final root WAIT. Not inherited semantic approval.'})
 print(json.dumps(rows[-1],ensure_ascii=False))
 if name=='report.md':print(d.decode())
(E/'supplemental-input-receipt.json').write_text(json.dumps({'files':rows,'qualification':'Static reads and exact received bytes only'},ensure_ascii=False,indent=2)+'\n')
