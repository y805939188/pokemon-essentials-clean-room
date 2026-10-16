from pathlib import Path
import sys,datetime,json
repo={'R':'/workspace/pokemon-essentials','B':'/workspace/pokemon-essentials-clean-room'}[sys.argv[1]]
p=Path(repo)/sys.argv[2]
a=int(sys.argv[3]) if len(sys.argv)>3 else 1
lines=p.read_text(encoding='utf-8-sig').splitlines()
b=min(int(sys.argv[4]) if len(sys.argv)>4 else len(lines),len(lines))
s=f'FILE {sys.argv[1]} {sys.argv[2]} L{a}-{b}/{len(lines)}\n'+'\n'.join(str(i)+' '+line for i,line in enumerate(lines[a-1:b],a))+'\n'
print(s,end='')
root=Path(__file__).parent/'units';root.mkdir(exist_ok=True)
import hashlib
key=hashlib.sha256((sys.argv[1]+':'+sys.argv[2]+':'+str(a)+':'+str(b)).encode()).hexdigest()[:16]
(root/(key+'.txt')).write_text(s)
with (Path(__file__).parent/'unit-invocations.jsonl').open('a') as f:f.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repo':sys.argv[1],'path':sys.argv[2],'lines':[a,b],'total_lines':len(lines),'output':'evidence/units/'+key+'.txt','evidence_level':'RENDER_ONLY','semantic_credit':False})+'\n')
