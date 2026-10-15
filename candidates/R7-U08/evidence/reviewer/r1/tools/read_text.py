import datetime,hashlib,json,sys,pathlib
p=pathlib.Path(sys.argv[1]);a=int(sys.argv[2]);b=int(sys.argv[3]);data=p.read_bytes();lines=data.decode().splitlines(keepends=True)
assert a>=1 and b<=len(lines)
out=''.join(f'{i}: '+lines[i-1] for i in range(a,b+1))
r={'read_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'path':str(p),'start_line':a,'end_line':b,'file_bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'output_bytes':len(out.encode()),'output_sha256':hashlib.sha256(out.encode()).hexdigest(),'output_location':'Platform tool transcript; source and candidate text not duplicated in result branch','qualification':'Actual textual read; semantics assessed separately; does not certify absence of tool display truncation'}
with open('/workspace/r7-u08-reviewer/candidates/R7-U08/evidence/reviewer/r1/tool-evidence/reading-receipts.jsonl','a') as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(out,end='')
