"""Present inert evidence with exact output identity. Output generation is not reading."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
T=Path(__file__).resolve().parent
mode,name=sys.argv[1:3]
if mode=='consumer':
 rows=json.loads((T/'inputs/target/consumer-reads/manifest.json').read_text());rows+=json.loads((T/'evidence/additional-consumers.json').read_text()) if (T/'evidence/additional-consumers.json').exists() else [];r=next(x for x in rows if x['name']==name)
 b=subprocess.check_output(['git','-C',r['repo'],'show',r['commit']+':'+r['path']]);assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
 ranges=[list(map(int,q.split(':')))for q in sys.argv[3:]]or r['ranges'];lines=b.decode().splitlines(True)
 out=''.join(f'[{name} {r["commit"]} {r["path"]} L{a}-{z}]\n'+''.join(f'{n}: {lines[n-1]}'for n in range(a,z+1))for a,z in ranges).encode()
 identity=dict(r,actual_presented_ranges=ranges)
elif mode in ('file','original'):
 rpath=Path(name);assert not rpath.is_absolute() and '..'not in rpath.parts
 p=(T/'inputs/target' if mode=='file' else T/'.transport/originals')/rpath;b=p.read_bytes();out=b
 identity={'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
else:raise ValueError(mode)
name=mode+'-'+name.replace('/','_').replace('.','_')+('-'+','.join(sys.argv[3:])if sys.argv[3:]else'')
p=T/'.transport/presented'/name;assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(out)
rec={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input':identity,'output_bytes':len(out),'output_sha256':hashlib.sha256(out).hexdigest(),'local_inert_output':str(p.relative_to(T)),'generation_credit':0,'actual_semantic_read_status':'AWAITING_EXPLICIT_REVIEWER_ENTRY'}
r=T/'evidence/presentations'/f'{name}.json';r.parent.mkdir(parents=True,exist_ok=True);r.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
sys.stdout.buffer.write(out)
