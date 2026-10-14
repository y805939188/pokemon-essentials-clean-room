"""Read-only frozen-input inventory and finite Markdown block denominator."""
import collections, datetime, hashlib, json, pathlib, subprocess
root = pathlib.Path(__file__).resolve().parents[1]
base = root.parents[2]
main = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
rcommit = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
ref = base/'reference/pokemon-essentials'
def git(repo, *args): return subprocess.check_output(['git','-C',str(repo),*args])
def entries(repo, rev, path=None):
    argv=['ls-tree','-rz','--full-tree',rev]
    if path: argv += ['--',path]
    for item in git(repo,*argv).split(b'\0'):
        if not item: continue
        info,p=item.split(b'\t',1);mode,kind,blob=info.decode().split()
        if kind=='blob': yield p.decode(),blob,mode
def ident(repo,rev,tree,p,blob,mode,purpose):
    b=git(repo,'cat-file','blob',blob)
    suffix=pathlib.Path(p).suffix.lower()
    istext = suffix in {'.md','.rb','.txt','.json','.yml','.tsv','.csv','.py','.html','.url'} or p in {'LICENSE','.gitignore'}
    return {'repository':str(repo),'commit':rev,'tree':tree,'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
            'git_blob':blob,'mode':mode,'type':'text' if istext else 'binary','purpose':purpose,
            'lines':len(b.splitlines()) if istext else None,'reading_status':'NOT_YET_READ'}
def save(name,obj): (root/'inventory'/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
r=[ident(ref,rcommit,git(ref,'rev-parse',rcommit+'^{tree}').decode().strip(),p,blob,m,'reference_behavior_or_material') for p,blob,m in entries(ref,rcommit)]
f=[ident(base,main,'1046fbb657882e84b3dfc6d017943a9edf7782e5',p,blob,m,'formal_current') for p,blob,m in entries(base,main,'deliverables/final-specification-set')]
save('reference.json',r);save('formal131.json',f)
allmain=[{'path':p,'git_blob':blob,'mode':m,'commit':main,'tree':'6ab3429170d2762607fbc2237014c3a160449fa1','disposition':'UNCLASSIFIED'} for p,blob,m in entries(base,main)]
save('workspace-tracked.json',allmain)
protected=[]
for p in (base/'review/global-independent-review/third-2026-10-11-86b4d7e').rglob('*'):
    if p.is_file():
        b=p.read_bytes();protected.append({'path':str(p.relative_to(base)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save('protected-untracked.json',protected)
save('reference-extra-files.json',[str(p.relative_to(ref)) for p in ref.rglob('*') if p.is_file() and '.git' not in p.parts and str(p.relative_to(ref)) not in {x['path'] for x in r}])
clauses=[]
for fi,x in enumerate(f,1):
    lines=git(base,'cat-file','blob',x['git_blob']).decode('utf-8-sig').splitlines(); ci=0;start=0
    for i,line in enumerate(lines+[''],1):
        if start and (not line.strip() or line.startswith('#') or line.startswith('|') or line.startswith('- ') or line.startswith('* ')):
            ci+=1;clauses.append({'id':f'F{fi:03d}-C{ci:04d}','path':x['path'],'start_line':start,'end_line':i-1,'status':'NOT_YET_REVIEWED'});start=0
        if line.strip():
            if line.startswith(('#','|','- ','* ')):
                ci+=1;clauses.append({'id':f'F{fi:03d}-C{ci:04d}','path':x['path'],'start_line':i,'end_line':i,'status':'NOT_YET_REVIEWED'})
            elif not start:start=i
save('formal-block-denominator.json',clauses)
save('initial-counts.json',{'reference_tracked_files':len(r),'formal_files':len(f),'formal_finite_blocks':len(clauses),'workspace_tracked_files':len(allmain),'protected_untracked_files':len(protected),'reference_bytes':sum(x['bytes'] for x in r),'formal_bytes':sum(x['bytes'] for x in f),'inventory_is_not_semantic_reading':True,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
print(json.dumps(json.loads((root/'inventory/initial-counts.json').read_text()),ensure_ascii=False))
