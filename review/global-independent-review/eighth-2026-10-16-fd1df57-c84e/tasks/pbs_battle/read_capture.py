import pathlib,sys,json,hashlib,subprocess,datetime
out=pathlib.Path(__file__).parent
root=pathlib.Path(sys.argv[1]); rel=sys.argv[2]; start=int(sys.argv[3]) if len(sys.argv)>3 else 1; end=int(sys.argv[4]) if len(sys.argv)>4 else 10**9
p=root/rel; raw=p.read_bytes(); lines=raw.decode('utf-8-sig').splitlines(); end=min(end,len(lines)); stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
result='\n'.join(f'{i+1:05d} {lines[i]}' for i in range(start-1,end))+'\n'
idx=sum(1 for _ in (out/'read-io').glob('*.txt'))+1; name=f'{idx:03d}.txt'; (out/'read-io'/name).write_text(result)
rec={'utc':stamp,'reader':'/root/pbs_battle','repo':str(root),'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),'lines':len(lines),'read_range':[start,end],'io':f'read-io/{name}','status':'OUTPUT_FOR_ACTUAL_READING_NOT_AUTOMATIC_CREDIT'}
with (out/'read-io/index.jsonl').open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(json.dumps(rec,ensure_ascii=False)); print(result,end='')
