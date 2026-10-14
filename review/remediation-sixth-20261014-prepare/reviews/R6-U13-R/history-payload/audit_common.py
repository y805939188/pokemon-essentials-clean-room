from pathlib import Path
import json,hashlib,subprocess,datetime,collections
ROOT=Path('/workspace/pokemon-essentials-clean-room')
OUT=Path(__file__).resolve().parent
BASE=ROOT/'review/remediation-sixth-20261014-prepare/inputs'
DUP=[]
def pairs(xs):
 d={}
 for k,v in xs:
  if k in d:DUP.append(k)
  d[k]=v
 return d
def types(x,p='',dst=None):
 dst={} if dst is None else dst
 dst.setdefault(p,collections.Counter())[type(x).__name__]+=1
 if isinstance(x,dict):
  for k,v in x.items():types(v,p+'/'+k,dst)
 if isinstance(x,list):
  for v in x:types(v,p+'/*',dst)
 return dst
files=[]
for p in sorted(BASE.glob('*.json')):
 b=p.read_bytes();DUP.clear();j=json.loads(b,object_pairs_hook=pairs)
 schema={k:dict(v) for k,v in types(j).items()}
 files.append({'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'lines':len(b.splitlines()),'duplicate_json_keys':DUP[:],'complete_recursive_structure':schema,'semantic_scope':'metadata and structure only except relevant historical/F records independently read'})
(OUT/'common-structure-audit.json').write_text(json.dumps(files,ensure_ascii=False,indent=2)+'\n')
j=json.loads((BASE/'frozen-inputs.json').read_text())
checks=[]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
for kind,key,commit in [('source','source_materials',j['reference_commit']),('formal','formal_materials','8ea169fbd0f33f378b5d732fd6bea59e854e04a6')]:
 for r in j[key]:
  proc=subprocess.run(['git','show',commit+':'+r['path']],cwd=ROOT,capture_output=True)
  entry=subprocess.run(['git','ls-tree',commit,'--',r['path']],cwd=ROOT,capture_output=True)
  b=proc.stdout
  got={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
  ok=proc.returncode==0 and all(got[k]==r[k] for k in got)
  checks.append({'kind':kind,'commit':commit,'path':r['path'],'declared':r,'observed':got,'git_entry':entry.stdout.decode().strip(),'exit':proc.returncode,'stderr':proc.stderr.decode(),'identity_equal':ok,'evidence_level':'HASH_BYTES_OBJECT_IDENTITY_ONLY'})
(OUT/'common-frozen-identities.json').write_text(json.dumps({'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'common_json_files':len(files),'recursive_schema_nodes':sum(len(f['complete_recursive_structure']) for f in files),'duplicate_key_files':[f['path'] for f in files if f['duplicate_json_keys']],'source_identities':sum(x['kind']=='source' for x in checks),'formal_identities':sum(x['kind']=='formal' for x in checks),'identity_mismatches':[x['path'] for x in checks if not x['identity_equal']],'identities_imply_semantic_read':False},ensure_ascii=False))
