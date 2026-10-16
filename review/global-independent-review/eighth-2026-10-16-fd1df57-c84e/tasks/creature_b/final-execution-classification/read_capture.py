"""Display and retain exact read I/O inside this one authorized write set."""
from pathlib import Path
import datetime,hashlib,json,sys
here=Path(__file__).resolve().parent;outdir=here/'read-io';outdir.mkdir(exist_ok=True)
p=Path(sys.argv[1]).resolve();b=p.read_bytes();ls=b.decode('utf-8-sig').splitlines(keepends=True)
a=int(sys.argv[2]) if len(sys.argv)>2 else 1;z=int(sys.argv[3]) if len(sys.argv)>3 else len(ls)
assert 1<=a<=z<=len(ls)
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
meta={'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'range':[a,z],'file_lines':len(ls),'began_utc':utc,'purpose':'READ_DISPLAY_ONLY_NO_AUTOMATIC_SEMANTIC_CREDIT'}
text=json.dumps(meta,ensure_ascii=False)+'\n'+''.join(f'{i:05d} '+ls[i-1] for i in range(a,z+1))
if not text.endswith('\n'):text+='\n'
name=f'{len(list(outdir.glob("*.stdout.txt")))+1:04d}.stdout.txt';(outdir/name).write_text(text)
meta.update(ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit_code=0,stdout='read-io/'+name)
with (outdir/'index.jsonl').open('a') as stream:stream.write(json.dumps(meta,ensure_ascii=False)+'\n')
sys.stdout.write(text)
