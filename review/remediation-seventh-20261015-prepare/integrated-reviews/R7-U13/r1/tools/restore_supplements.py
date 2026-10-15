from pathlib import Path
import json,gzip,urllib.request,sys,subprocess,datetime
sys.path.insert(0,str(Path(__file__).resolve().parent));from run_logged import identity
root=Path('/workspace/r7-ir-R7-U13');dest=root/'supplemental';dest.mkdir(exist_ok=True)
record=[]
rows=json.loads((root/'actual-input/candidate/candidates/R7-U13/evidence/author/targeted-recovery.json').read_bytes())['files']
for r in rows:
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+r['publication_commit']+'/'+r['transport_path']
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 data=urllib.request.urlopen(url,timeout=60).read(r['encoded']['bytes']+1)
 assert identity(data)==r['encoded'];d=gzip.decompress(data);assert identity(d)==r['decoded']
 p=dest/r['logical_path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(d)
 record.append(dict(url=url,utc=start,local_path=str(p),encoded=identity(data),decoded=identity(d),qualification='fixed bounded supplemental recovery, no source execution'))
repo=root/'checkout';MI='45c80832a41c1b56dcd7e9d93497758cbb7721de';B='e646432c644dec04d306842cc5a559a29c718fbc'
paths=['deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md','deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md','deliverables/final-specification-set/generic-kernel/wp07-file-network-io-and-external-boundary.md','deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md','deliverables/final-specification-set/scope-statement.md','review/remediation-seventh-20261015-prepare/current-navigation-errata.json','delivery/2026-10-14-sixth/seventh-review-inputs.json']
allpaths=subprocess.check_output(['git','-C',str(repo),'ls-tree','-r','--name-only',MI,'--','deliverables/final-specification-set/generic-kernel']).decode().splitlines()
paths=[p for p in paths if 'wp07-' not in p]+[p for p in allpaths if '/wp07-' in p]
for path in paths:
 data=subprocess.check_output(['git','-C',str(repo),'show',MI+':'+path]);p=dest/'actual'/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 record.append(dict(commit=MI,path=path,local_path=str(p),**identity(data)))
(Path(__file__).resolve().parent/'supplemental-recovery.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))
