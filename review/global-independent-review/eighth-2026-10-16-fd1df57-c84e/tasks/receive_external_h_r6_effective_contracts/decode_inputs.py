"""Verify and decode bounded gzip input objects; never execute their contents."""
import gzip,hashlib,json,pathlib,subprocess,io
T=pathlib.Path(__file__).resolve().parent
C='a96ec67a948e3fc86b25ad407cd977b6752e2d77'
P='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/external_h_r6_effective_contracts/'
cat=json.loads((T/'inputs/payload-catalog.json').read_text());out=T/'decoded';assert not out.exists();out.mkdir()
rows=[];seen=set()
for r in cat['rows']:
 i=r['input'];sha=i['sha256'];b=subprocess.check_output(['git','show',C+':'+P+r['decoded_object']])
 with gzip.GzipFile(fileobj=io.BytesIO(b)) as stream:data=stream.read(i['bytes']+1)
 assert len(data)==i['bytes'] and hashlib.sha256(data).hexdigest()==sha
 assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==i['git_blob']
 if sha not in seen:(out/(sha+'.txt')).write_bytes(data);seen.add(sha)
 rows.append(dict(row=r['row'],input=i,decoded_path='decoded/'+sha+'.txt',semantic_credit=0,decoded_identity_verified=True))
(T/'decoded-index.json').write_text(json.dumps(dict(roles=rows,unique=len(seen),bytes_with_roles=sum(x['input']['bytes'] for x in rows),semantic_credit=0),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(roles=len(rows),unique=len(seen),bytes_with_roles=sum(x['input']['bytes'] for x in rows),semantic_credit=0)))
