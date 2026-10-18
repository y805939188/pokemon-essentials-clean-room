import pathlib,json,sys,datetime,hashlib
base=pathlib.Path(__file__).parent;p=base.parents[1]
d=json.loads((p/'delegation/readsets/world_full.json').read_text())
kind=sys.argv[1]
if kind in ['reference','formal']:
 e=d[kind][int(sys.argv[2])];f=pathlib.Path(e['repo'])/e['path']
else:f=pathlib.Path(sys.argv[2])
a=int(sys.argv[3]);b=int(sys.argv[4]); lines=f.read_text().splitlines(); z='\n'.join(f'{i+1:5} {line}' for i,line in enumerate(lines) if a<=i+1<=b)+'\n'; out=base/'read-io';out.mkdir(exist_ok=True);seq=len(list(out.glob('*.txt')))+1;n=f'{seq:04}.txt';(out/n).write_text(z)
with (out/'index.jsonl').open('a') as h:h.write(json.dumps({'sequence':seq,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'path':str(f),'range':[a,min(b,len(lines))],'total_lines':len(lines),'source_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'stdout':n,'stdout_sha256':hashlib.sha256(z.encode()).hexdigest(),'exit':0,'evidence':'SOURCE_STATIC_READ_OUTPUT_ONLY; semantic credit requires reviewer facts'},ensure_ascii=False)+'\n')
print(f'FILE {f} RANGE {a}-{min(b,len(lines))}/{len(lines)} OUTPUT {n}\n'+z)
