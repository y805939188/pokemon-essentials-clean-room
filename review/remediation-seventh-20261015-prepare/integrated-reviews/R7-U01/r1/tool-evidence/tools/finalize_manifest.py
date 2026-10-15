import hashlib,json,pathlib
D=pathlib.Path('/workspace/r7-ir-R7-U01/checkout/review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U01/r1')
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
p=D/'artifact-manifest.json';j=json.loads(p.read_text());j['files']=[{'path':str(f.relative_to(D)),**identity(f.read_bytes())} for f in sorted(D.rglob('*')) if f.is_file() and f!=p];p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest_members':len(j['files']),'nonself_bytes':sum(x['bytes'] for x in j['files'])}))
