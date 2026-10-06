"""Fresh static Git/text/JSON identity bookkeeping. Never executes reviewed programs."""
import argparse,subprocess,json,hashlib,pathlib,re
OUT=pathlib.Path(__file__).parent
BASE='1e6b11a47370f1c7c4659a32443fc1afda597bac'
C2='af39efbf32549be964cb083bd49bed6d1d5c0d2a'
C3='c06db6cd964188b3c693a9b7820e3a8aaffe0b04'
F='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
A='41fffb540c6483f5296ea0d33b789b75180d27ed'
OLD='b5f95815647a4ba047cf64dc3c81121d0b142cd5'
ROOT='review/global-independent-review/2026-10-03-fd82a639/'
PLAN='review/remediation-20261003-prepare/'
def git(*args,repo=None):return subprocess.check_output(['git',*args],cwd=repo)
def sha(b):return hashlib.sha256(b).hexdigest()
def append(file,entry):
 p=OUT/file; d=json.loads(p.read_text()) if p.exists() else [];d.append(entry);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def read(c,p,repo=None):
 b=git('show',c+':'+p,repo=repo)
 ident={'commit':c,'path':p,'git_blob':git('rev-parse',c+':'+p,repo=repo).decode().strip(),'sha256':sha(b),'bytes':len(b),'lines':len(b.splitlines()),'repository':'reference' if repo else 'project'}
 append('input-identities.json',ident);return b,ident
parser=argparse.ArgumentParser();parser.add_argument('mode');parser.add_argument('args',nargs='*');parser.add_argument('--repo');parser.add_argument('--start',type=int,default=0);parser.add_argument('--end',type=int,default=100000);v=parser.parse_args()
if v.mode=='read':
 c,p,*rr=v.args;b,i=read(c,p,v.repo);lines=b.decode().splitlines();lo=int(rr[0]) if rr else 1;hi=int(rr[1]) if len(rr)>1 else len(lines)
 print(json.dumps(i,ensure_ascii=False));print('\n'.join(str(n)+': '+lines[n-1] for n in range(lo,min(hi,len(lines))+1)))
 append('reading-log.json',{'identity':i,'range':[lo,min(hi,len(lines))],'stage':'displayed for semantic inspection','whole_file_claim':lo==1 and hi>=len(lines)})
elif v.mode=='scopes':
 out=[]
 for x in [BASE,C2]:
  b=git('diff','--no-ext-diff','--no-textconv','--binary',x,C3);ns=git('diff','--name-status',x,C3).decode().splitlines();files=[]
  for line in ns:
   status,p=line.split('\t');z={'status':status,'path':p}
   for name,c in [('before',x),('after',C3)]:
    try:
     if name=='before' and status=='A':z[name]=None;continue
     bb,i=read(c,p);z[name]=i
    except subprocess.CalledProcessError:z[name]=None
   files.append(z)
  out.append({'before':x,'after':C3,'unfiltered':True,'sha256':sha(b),'bytes':len(b),'lines':len(b.splitlines()),'paths':files})
 (OUT/'complete-diff-identities.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps([{k:y[k] for k in ['before','after','sha256','bytes','lines']}|{'path_count':len(y['paths'])} for y in out],indent=2))
elif v.mode=='diff':
 x,p=v.args;b=git('diff','--no-ext-diff','--no-textconv',x,C3,'--',p);ll=b.decode().splitlines();print('DIFF_LINES',len(ll));print('\n'.join(str(n+1)+': '+x for n,x in enumerate(ll) if v.start<=n<v.end));append('reading-log.json',{'kind':'formal diff','before':x,'after':C3,'path':p,'sha256':sha(b),'bytes':len(b),'semantic_read':'displayed'})
elif v.mode=='objects':
 ids=v.args;d,i=read(F,ROOT+'findings.json');f={x['id']:x for x in json.loads(d)};d,j=read(A,PLAN+'finding-acceptance.json');a=json.loads(d)
 # Each primitive unique value is displayed once; ordered trees retain every key,
 # type, array position and value identity, allowing lossless reconstruction.
 vals={};maps=[];trees={}
 def walk(x,path):
  if isinstance(x,dict):return {k:walk(w,path+'/'+k) for k,w in x.items()}
  if isinstance(x,list):return [walk(w,path+'/'+str(k)) for k,w in enumerate(x)]
  key=json.dumps(x,ensure_ascii=False,separators=(',',':'));h=sha(key.encode());vals[h]=x;maps.append({'pointer':path,'value_sha256':h});return {'$value':h[:12]}
 for id in ids:trees[id]={'finding':walk(f[id],id+'/finding'),'acceptance':walk(a[id],id+'/acceptance')}
 # Full values, not summaries, are shown with first pointer context.
 for idx,(h,x) in enumerate(vals.items()):
  if idx<v.start or idx>=v.end:continue
  where=next(m['pointer'] for m in maps if m['value_sha256']==h);print(idx,where if isinstance(x,str) and len(x)>65 else '',json.dumps(x,ensure_ascii=False))
 append('deduplication-map.json',{'kind':'full finding and acceptance objects','ids':ids,'identities':[i,j],'values':[{'sha256':h,'type':type(x).__name__} for h,x in vals.items()],'ordered_trees':trees,'mapping':maps,'lossless':True})
 print('FULL_ORDERED_MAPPING_RECORDED',len(vals),'unique values; displayed',v.start,min(v.end,len(vals)))
 append('reading-log.json',{'kind':'lossless full control object projection','ids':ids,'unique_value_indices':[v.start,min(v.end,len(vals))],'total_unique_values':len(vals),'semantic_read':'displayed'})
elif v.mode=='bundle':
 group=v.args[0];known=set()
 for m in json.loads((OUT/'deduplication-map.json').read_text()):
  if m.get('kind')=='full finding and acceptance objects' or m.get('group') in ('pre','old') and group=='history' or m.get('group')=='pre':known.update(x['sha256'] for x in m['values'])
 known.update(x['sha256'] for x in json.loads((OUT/'semantic-duplicate-seeds.json').read_text())['values'])
 selections=[]
 if group=='old':
  prefix='review/remediation/20261003-prepare/batches/B14/affected-B07-review-1/'
  selections=[(OLD,x) for x in git('ls-tree','-r','--name-only',OLD,prefix).decode().splitlines()]
 elif group=='pre':
  selections=[(BASE,'review/remediation/20261003-prepare/batches/B09/acceptance-stage-1/B14-downstream-contract.json'),(BASE,'review/remediation/20261003-prepare/batches/B07/acceptance-stage-1/acceptance-manifest.json'),(A,PLAN+'batches.json'),(A,PLAN+'cross-chain-acceptance.md'),(C3,'review/remediation/20261003-prepare/batches/B14/candidate-3/scope-authorization-1.json'),('c0dc3037f6aafd736915af1d0bd920455012b30a','review/remediation/20261003-prepare/batches/B14/candidate-3/scope-proposal-1/scope-manifest.json')]
 elif group=='history':
  prefix='review/remediation/20261003-prepare/batches/B14/'
  selections=[(C3,x.split('\t')[1]) for x in git('diff','--name-status',BASE,C3).decode().splitlines() if x.startswith('A\t'+prefix)]
 else:raise ValueError(group)
 vals={};mapping=[];trees={};idents=[]
 def walk(x,pointer):
  if isinstance(x,dict):return {k:walk(y,pointer+'/'+k) for k,y in x.items()}
  if isinstance(x,list):return [walk(y,pointer+'/'+str(n)) for n,y in enumerate(x)]
  key=json.dumps(x,ensure_ascii=False,separators=(',',':'));h=sha(key.encode());mapping.append({'pointer':pointer,'value_sha256':h});
  if h not in known:vals[h]=x
  return {'$value':h}
 for c,p in selections:
  b,i=read(c,p);idents.append(i)
  if p.endswith('.json'):
   d=json.loads(b)
   if group=='pre' and p.endswith('/batches.json'):d=[x for x in d if x['id'] in ['B07','B14']]
  else:d=b.decode().splitlines()
  trees[c+':'+p]=walk(d,p)
 for idx,(h,x) in enumerate(vals.items()):
  if idx<v.start or idx>=v.end:continue
  pointer=next(y['pointer'] for y in mapping if y['value_sha256']==h)
  print(idx,json.dumps(x,ensure_ascii=False))
 print('BUNDLE',group,'FILES',len(selections),'UNIQUE_NEW_VALUES',len(vals),'RANGE',v.start,min(v.end,len(vals)))
 append('deduplication-map.json',{'kind':'lossless bundle','group':group,'identities':idents,'ordered_trees':trees,'mapping':mapping,'values':[{'sha256':h,'type':type(x).__name__} for h,x in vals.items()],'duplicate_values_resolve_to_prior_control_mapping':True})
 append('reading-log.json',{'kind':'lossless full payload projection','group':group,'range':[v.start,min(v.end,len(vals))],'total_unique_new_values':len(vals),'semantic_read':'displayed'})
