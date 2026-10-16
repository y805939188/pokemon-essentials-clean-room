from pathlib import Path
import datetime,hashlib,json,sys,traceback
P=Path(__file__).resolve().parent;now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();started=now();q=json.loads(sys.argv[1]);out=[];ids=[];err='';code=0
try:
 for r in q['reads']:
  p=Path(r['path']);b=p.read_bytes();lines=b.decode('utf-8-sig').splitlines(keepends=True);a,z=r.get('range',[1,len(lines)]);out.append('PATH '+str(p)+' RANGE '+str(a)+'–'+str(z)+'\n'+''.join(lines[a-1:z]));ids.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'range':[a,z],'file_lines':len(lines)})
except Exception:code=1;err=traceback.format_exc()
end=now();folder=P/'io';folder.mkdir(exist_ok=True);s='\n'.join(out);(folder/(q['id']+'.stdout.txt')).write_text(s);(folder/(q['id']+'.stderr.txt')).write_text(err);(folder/(q['id']+'.json')).write_text(json.dumps({'id':q['id'],'request':q,'started_utc':started,'ended_utc':end,'reads':ids,'underlying_exit_code':code,'qualification':'IO only; actual model reading separately ledgered'},ensure_ascii=False,indent=2)+'\n');sys.stdout.write(s);sys.stderr.write(err);sys.exit(code)
