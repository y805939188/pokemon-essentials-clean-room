import json, pathlib, subprocess, sys, hashlib, datetime
W=pathlib.Path.cwd(); A=W/'review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/CA'
B='1f36475d22120a0d1175967d5b17d71fe8311d88'; R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
RR=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
def git(root,*args): return subprocess.check_output(['git','-C',str(root),*args]).decode()
def content(kind,path):
 if kind=='B': return git(W,'show',B+':'+path)
 if kind=='R': return git(RR,'show',R+':'+path)
 return (W/path).read_text()
def record(name,x):
 p=A/name; d=json.loads(p.read_text()) if p.exists() else []
 d.append(x);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def read(kind,path,ranges):
 t=content(kind,path);ls=t.splitlines(); actual=[]
 print(kind,path)
 for item in ranges.split(','):
  a,b=map(int,(item.split('-') if '-' in item else [item,item]));b=min(b,len(ls));actual.append([a,b])
  print('\n'.join(f'{i}: {ls[i-1]}' for i in range(a,b+1)))
 record('read-ledger.json',{'kind':kind,'path':path,'ranges':actual,'sha256':hashlib.sha256(t.encode()).hexdigest()})
def search(kind,identifier,pattern):
 root,commit,prefix=(W,B,'deliverables/final-specification-set/') if kind=='B' else (RR,R,'Data/Scripts/')
 paths=[p for p in git(root,'ls-tree','-r','--name-only',commit,'--',prefix).splitlines() if p.endswith('.md' if kind=='B' else '.rb')]
 results=[]
 for p in paths:
  t=content(kind,p)
  r=subprocess.run(['rg','-n','-i','-e',pattern],input=t,text=True,capture_output=True)
  if r.returncode not in [0,1]: raise RuntimeError(r.stderr)
  if r.stdout:
   nums=[int(x.split(':',1)[0]) for x in r.stdout.splitlines()]
   results.append({'path':p,'lines':nums})
   print(p+'\n'+r.stdout,end='')
 record('search-ledger.json',{'kind':kind,'id':identifier,'pattern':pattern,'baseline':commit,'scope':prefix,'files_searched':len(paths),'hits':results})
 print('FILES_SEARCHED',len(paths),'MATCHED_FILES',len(results))
if __name__=='__main__':
 if sys.argv[1]=='read':read(*sys.argv[2:])
 if sys.argv[1]=='search':search(*sys.argv[2:])
