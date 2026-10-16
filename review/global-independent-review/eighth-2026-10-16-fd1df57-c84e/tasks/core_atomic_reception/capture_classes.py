"""Static exact source class reader; never invokes Ruby or game code."""
import pathlib,sys,json,hashlib,datetime,uuid,subprocess
P=pathlib.Path(__file__).resolve().parent;R=pathlib.Path('/workspace/pokemon-essentials');C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';start=datetime.datetime.now(datetime.timezone.utc).isoformat();selected=[]
for name in sys.argv[1:]:
 matches=[]
 for f in sorted((R/'Data/Scripts/011_Battle/003_Move').glob('*.rb')):
  b=f.read_bytes();ss=b.decode().splitlines(keepends=True)
  for i,s in enumerate(ss):
   if s.startswith('class Battle::Move::'+name+' '):
    j=next(j for j in range(i+1,len(ss))if ss[j].strip()=='end'and ss[j].startswith('end'));path=str(f.relative_to(R));fixed=subprocess.run(['git','show',C+':'+path],cwd=R,capture_output=True,check=True).stdout;assert b==fixed;t=''.join(ss[i:j+1]);matches.append(dict(id=name,path=path,commit=C,parent_bytes=len(b),parent_sha256=hashlib.sha256(b).hexdigest(),blob=subprocess.run(['git','rev-parse',C+':'+path],cwd=R,capture_output=True,text=True,check=True).stdout.strip(),range=[i+1,j+1],text=t,text_sha256=hashlib.sha256(t.encode()).hexdigest(),actual_reader='/root/core_atomic_reception',parent_FULL=False))
 assert len(matches)==1,(name,len(matches));selected+=matches
stem='classes-'+uuid.uuid4().hex;payload=dict(argv=sys.argv,utc_start=start,utc_end=datetime.datetime.now(datetime.timezone.utc).isoformat(),reader='/root/core_atomic_reception',business='NOT_EXECUTED',helper_exit=0,units=selected);out=P/'io'/(stem+'.json');out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n');print(json.dumps(payload,ensure_ascii=False,indent=2));print('CAPTURE',out.name,len(out.read_bytes()),hashlib.sha256(out.read_bytes()).hexdigest())
