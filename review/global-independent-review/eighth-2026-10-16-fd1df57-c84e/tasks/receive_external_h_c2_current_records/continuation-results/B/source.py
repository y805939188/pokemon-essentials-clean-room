"""Display fixed bytes by explicit continuous lines; identities only in public receipt."""
from pathlib import Path
import argparse,json,subprocess,hashlib,datetime
T=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('kind');ap.add_argument('path');ap.add_argument('first',type=int);ap.add_argument('last',type=int);ap.add_argument('--note',required=True);a=ap.parse_args()
repo='/workspace/pokemon-essentials' if a.kind=='R' else '/workspace/pokemon-essentials-clean-room'
c='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' if a.kind=='R' else 'fd1df570cad987dc3852a3b958f03916e317f7fe'
b=subprocess.check_output(['git','show',c+':'+a.path],cwd=repo);lines=b.decode('utf-8-sig').splitlines();a.last=a.last or len(lines);assert 1<=a.first<=a.last<=len(lines)
txt='\n'.join(f'{i}: {lines[i-1]}' for i in range(a.first,a.last+1));print(a.kind,c,a.path,'range',a.first,a.last,'file lines',len(lines));print(txt)
p=T/'source-displays.json';s=json.loads(p.read_text()) if p.exists() else []
s.append(dict(repo=repo,commit=c,path=a.path,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),lines=[a.first,a.last],file_lines=len(lines),display_sha256=hashlib.sha256(txt.encode()).hexdigest(),purpose=a.note,display_only=True,utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
p.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
