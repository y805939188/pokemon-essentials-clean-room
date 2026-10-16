"""Display fixed source/spec slices, retaining only identities in the report."""
from recover import T,ident,save
import argparse,json,subprocess,datetime
p=argparse.ArgumentParser();p.add_argument('repo',choices=['R','B']);p.add_argument('path');p.add_argument('start',type=int,nargs='?',default=1);p.add_argument('end',type=int,nargs='?',default=1000000);a=p.parse_args()
repo='/workspace/pokemon-essentials' if a.repo=='R' else '/workspace/pokemon-essentials-clean-room'
c='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' if a.repo=='R' else 'fd1df570cad987dc3852a3b958f03916e317f7fe'
b=subprocess.check_output(['git','-C',repo,'show',c+':'+a.path]);lines=b.decode().splitlines();end=min(a.end,len(lines));shown='\n'.join(f'{i+1:5}: {lines[i]}' for i in range(a.start-1,end))
f=T/'source-displays.json';rows=json.loads(f.read_text()) if f.exists() else [];r=dict(repo=a.repo,commit=c,path=a.path,identity=ident(b),range=[a.start,end],total_lines=len(lines),display=ident(shown.encode()),utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),credit='DISPLAY_ONLY; semantic judgment in reception ledger');rows.append(r);save(f,rows)
print(json.dumps(r,ensure_ascii=False));print(shown)
