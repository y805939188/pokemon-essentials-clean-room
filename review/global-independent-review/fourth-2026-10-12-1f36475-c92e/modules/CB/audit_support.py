"""CB-only static audit helper. Never executes reference behavior or writes outside CB."""
import json,pathlib,subprocess,hashlib
ROOT=pathlib.Path.cwd()
CB=ROOT/'review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/CB'
R=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
BREF='1f36475d22120a0d1175967d5b17d71fe8311d88'
RREF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PREFIX='deliverables/final-specification-set/'
def content(kind,path):
 root,ref=(R,RREF) if kind=='R' else (ROOT,BREF)
 return subprocess.check_output(['git','-C',str(root),'show',ref+':'+path]).decode()
def read(kind,path,ranges=None):
 if kind=='B' and not path.startswith(PREFIX):path=PREFIX+path
 s=content(kind,path);lines=s.splitlines();ranges=ranges or [(1,len(lines))]
 print('\nFILE '+kind+' '+path)
 for a,b in ranges:
  for i in range(a,min(b,len(lines))+1): print(f'{i}: {lines[i-1]}')
 logpath=CB/'read-log.json';log=json.loads(logpath.read_text()) if logpath.exists() else []
 log.append({'kind':kind,'path':path,'commit':RREF if kind=='R' else BREF,'ranges':ranges,'sha256':hashlib.sha256(s.encode()).hexdigest()})
 logpath.write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
def search(sid,pattern):
 # rg over all 131 formal files; each searched worktree file checked against fixed B blob.
 records=json.loads((ROOT/'delivery/2026-10-12/formal-identities.json').read_text())['records']
 paths=[v['path'] for v in records]
 for p in paths:
  if (ROOT/p).read_text()!=content('B',p):raise RuntimeError('Formal input drift: '+p)
 args=['rg','-n','-i','--no-heading',pattern,*paths]
 res=subprocess.run(args,text=True,capture_output=True)
 if res.returncode not in [0,1]:raise RuntimeError(res.stderr)
 entry={'id':sid,'pattern':pattern,'scope':'all 131 fixed B formal files, including scope/shared/appendices/tests','file_count':len(paths),'method':'rg -n -i; searched bytes compared to git show B','matches':res.stdout.splitlines()}
 p=CB/'negative-evidence.json';d=json.loads(p.read_text()) if p.exists() else {'schema_version':'1.0','searches':[]}
 d['searches'].append(entry);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 print('SEARCH '+sid)
 groups={}
 for line in res.stdout.splitlines():
  path,num,txt=line.split(':',2);groups.setdefault(path,[]).append(num)
 for path,nums in groups.items(): print(path+':'+','.join(nums))
