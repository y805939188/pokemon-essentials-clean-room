import sys,subprocess,json,hashlib,datetime
from pathlib import Path
base=Path(__file__).resolve().parent;loc=sys.argv[1];mode=sys.argv[2]
t0=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(['git','show',loc],stdout=subprocess.PIPE,stderr=subprocess.PIPE);t1=datetime.datetime.now(datetime.timezone.utc).isoformat();assert r.returncode==0
b=r.stdout;x=json.loads(b);ptr=[]
if mode=='actualcommon':
 keys=[k for k in x if k not in ['files','batches','files_stable_against_remaining_primary_write_sets','required_ids','unchanged_prospective_paths','delta_from_prior_actual']];y={k:x[k] for k in keys};ptr=['/'+k for k in keys]
elif mode=='actualfiles':
 terms=['wp53','wp56','wp58','wp18','wp66-a-party','combat-requirements-wp54','pokemon-rules-wp53'];y={}
 for key in ['files','batches']:
  selected=[(i,v) for i,v in enumerate(x[key]) if (any(t in json.dumps(v) for t in terms) if key=='files' else v['batch'] in ['R6-U10','R6-U11','R6-U13'])];y[key]=[v for i,v in selected];ptr+=['/'+key+'/'+str(i) for i,v in selected]
elif mode=='contractgeneral':
 y={k:v for k,v in x.items() if k!='scope_contracts'};ptr=['/'+k for k in y]
else: raise ValueError(mode)
rec={'locator':loc,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'semantic_JSON_pointers_presented':ptr,'argv':sys.argv,'cwd':str(Path.cwd()),'start_utc':t0,'end_utc':t1,'git_show_exit':r.returncode,'git_show_stderr':r.stderr.decode(),'evidence_level':'IMMUTABLE_JSON_PROJECTION_PRESENTATION'}
with (base/'reading-ledger.jsonl').open('a') as f: f.write(json.dumps(rec,ensure_ascii=False)+'\n')
(base/(mode+'-projection.json')).write_text(json.dumps(y,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(rec,ensure_ascii=False));print(json.dumps(y,ensure_ascii=False,separators=(',',':')))
