import pathlib,json,hashlib,sys,datetime
r=pathlib.Path(__file__).resolve().parent.parent
task=sys.argv[1]
modules=[f'M{i:02d}' for i in (range(1,7) if task=='CA' else range(7,13) if task=='CB' else range(1,13))]
paths=[]
pending=[]
for m in modules:
 launch=json.loads((r/'tasks'/(m+'-launch.json')).read_text())
 if launch['status']!='PROCESS_COMPLETED':
  assert task=='J' and m=='M11' and '--allow-pending-M11' in sys.argv,(m,launch['status'])
  pending.append({'module':m,'status':launch['status'],'scope':'No unsealed submission consumed. Fixed B/R direct source junction review proceeds independently.'})
  continue
 paths.extend(p for p in (r/'modules'/m).rglob('*') if p.is_file())
paths.extend(p for p in (r/'modules/ROOT').glob('*') if p.is_file())
if task=='J':paths.extend([r/'evidence/junction-navigation.json',r/'evidence/legacy-projection-links.json'])
files=[]
for p in sorted(paths):
 b=p.read_bytes();files.append({'path':str(p.relative_to(r)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()})
x={'schema_version':'1.0','task':task,'frozen_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'formal_baseline':'1f36475d22120a0d1175967d5b17d71fe8311d88','reference_baseline':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','modules':modules,'pending_domain_submissions':pending,'files':files,'scope':'Complete immutable-by-procedure local submissions for review; fixed repository report commit supplied at final publication. Original module files will not be rewritten by integrator.'}
(r/'tasks'/(task+'-input-identities.json')).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');print({'task':task,'input_files':len(files)})
