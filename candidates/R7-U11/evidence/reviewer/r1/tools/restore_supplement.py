import pathlib,json,hashlib,urllib.request,gzip,io,datetime,concurrent.futures
root=pathlib.Path('/workspace/r7-review-supplement/R7-U11-r1');root.mkdir(parents=True,exist_ok=True)
bindings=json.loads(pathlib.Path('/workspace/r7-context/R7-U11-reviewer/evidence/tasks/R7-C13/raw-binding-manifest.json').read_bytes())
wanted={'p02-b879c9a306446f46733b','p02-85e3801098ab8f9287ae','p02-c881417f203d17538f84','p02-fba319259e6423bc2131','p02-b5cd1721b33b03008ddd'}
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def restore(r):
 h=r['sha256'];u='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/4580645dfbfec4a3c7ccbad56ae293cc619b0d25/review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/objects/'+h[:2]+'/'+h+'.gz';start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with urllib.request.urlopen(u,timeout=40) as resp:encoded=resp.read(400001);status=resp.status
 assert len(encoded)<=400000
 with gzip.GzipFile(fileobj=io.BytesIO(encoded)) as f:b=f.read(r['bytes']+1)
 actual=ident(b);assert actual=={'bytes':r['bytes'],'sha256':h,'git_blob':r['content_git_blob']},r
 p=root/(h+'.raw')
 with p.open('xb') as f:f.write(b)
 return {'binding_id':r['binding_id'],'path':str(p),'identity':actual,'encoded_identity':ident(encoded),'url':u,'http_status':status,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'credit':'TOOL_VALIDATION'}
rows=list(concurrent.futures.ThreadPoolExecutor(max_workers=4).map(restore,[r for r in bindings if r['binding_id'] in wanted]));(root/'receipt.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps({'files':len(rows),'bytes':sum(x['identity']['bytes'] for x in rows),'status':'BYTES_VERIFIED'}))
