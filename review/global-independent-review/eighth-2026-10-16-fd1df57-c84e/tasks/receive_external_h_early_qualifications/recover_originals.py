"""Bounded inert gzip recovery against exact B8 transport, never run original code."""
from pathlib import Path
import gzip,json,hashlib,subprocess,datetime
T=Path(__file__).resolve().parent
rows=json.loads((T/'inputs/target/inputs/readset.json').read_text())['files'];proof=[]
for r in rows:
 e=r['encoded_identity'];p=subprocess.check_output(['git','show','fd1df570cad987dc3852a3b958f03916e317f7fe:'+r['transport_path']])
 assert len(p)==e['transport_bytes'] and hashlib.sha256(p).hexdigest()==e['transport_sha256'] and hashlib.sha1(f'blob {len(p)}\0'.encode()+p).hexdigest()==e['transport_git_blob_content_id']
 out=T/'inputs/original-transport'/e['transport_path'];out.parent.mkdir(parents=True,exist_ok=True);assert not out.exists();out.write_bytes(p)
 d=gzip.decompress(p);assert len(d)==r['bytes'] and hashlib.sha256(d).hexdigest()==r['sha256'] and hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()==r['git_blob']
 out=T/'.transport/originals'/r['logical_path'];out.parent.mkdir(parents=True,exist_ok=True);assert not out.exists();out.write_bytes(d)
 proof.append({'input':r,'decoded_local_path':str(out.relative_to(T)),'transport_local_path':str((T/'inputs/original-transport'/e['transport_path']).relative_to(T)),'B8_transport_verified':True,'semantic_credit':0})
(T/'evidence/original-recovery.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':proof,'count':len(proof),'decoded_bytes':sum(x['input']['bytes']for x in proof)},ensure_ascii=False,indent=2)+'\n')
print('VERIFIED',len(proof),sum(x['input']['bytes']for x in proof))
