import sys,subprocess,hashlib,json,datetime,pathlib
root=pathlib.Path('/workspace/pokemon-essentials-clean-room')
ledger=pathlib.Path(__file__).with_name('reading-ledger.jsonl')
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
kind,identity=sys.argv[1:3]
if kind=='git':
 p=subprocess.run(['git','show',identity],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.PIPE);data=p.stdout
 if p.returncode: print(p.stderr.decode());sys.exit(p.returncode)
else:
 data=(root/identity).read_bytes()
lines=data.decode('utf-8').splitlines();ranges=[list(map(int,v.split('-'))) for v in sys.argv[3:]] or [[1,len(lines)]]
for a,b in ranges:
 print(f'READ {identity} L{a}-{b} / {len(lines)}')
 for n in range(a,b+1):print(f'{n:5} {lines[n-1]}')
blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
record=dict(reader='/root/variants',kind=kind,input=identity,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=blob,total_lines=len(lines),presented_ranges=ranges,evidence_level='SOURCE_STATIC' if kind=='git' and identity.startswith('8c591') else 'DOCUMENT_STATIC',cwd=str(root),argv=sys.argv,start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),read_result='presented_and_semantically_read')
with ledger.open('a') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
