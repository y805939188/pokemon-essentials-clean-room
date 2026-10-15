import datetime,hashlib,json,os,pathlib,urllib.request,urllib.parse
r=pathlib.Path('/workspace/r7-ir-R7-U01')
rows=json.loads((r/'actual-input/candidate-review/candidates/R7-U01/evidence/reviewer/r2/tool-evidence/extra-source-receipt.json').read_bytes())
out=[]
for row in rows:
    t=datetime.datetime.now(datetime.timezone.utc).isoformat()
    url='https://raw.githubusercontent.com/Maruno17/pokemon-essentials/'+row['commit']+'/'+urllib.parse.quote(row['path'],safe='/')
    with urllib.request.urlopen(url,timeout=60) as response:
        b=response.read();code=response.status
    actual={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
    assert all(actual[k]==row[k] for k in actual)
    p=r/'extra-input'/row['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b);p.chmod(0o444)
    out.append({'path':row['path'],'commit':row['commit'],**actual,'url':url,'http_status':code,'start_utc':t,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool_pid':os.getpid(),'status':'EXACT_BYTES_VERIFIED','identity_basis':row['identity_source']})
(r/'tool-evidence/extra-source-receipt.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
