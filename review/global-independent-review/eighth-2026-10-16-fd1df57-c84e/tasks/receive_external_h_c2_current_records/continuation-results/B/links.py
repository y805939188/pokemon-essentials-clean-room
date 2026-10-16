"""Check every Markdown destination of the three frozen navigation inputs."""
from pathlib import Path
import subprocess, json, re, posixpath, hashlib, urllib.parse
T=Path(__file__).resolve().parent
R='/workspace/pokemon-essentials-clean-room'
commits=['e646432c644dec04d306842cc5a559a29c718fbc','fd1df570cad987dc3852a3b958f03916e317f7fe']
paths=['deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md']
out=[]
G=['git','--git-dir='+str(T/'.work/target.git')]
def git(*args):return subprocess.check_output(G+list(args),cwd=R)
for c in commits:
    rows=[]
    for path in paths:
        b=git('show',c+':'+path)
        for n,line in enumerate(b.decode().splitlines(),1):
            for label,url in re.findall(r'\[([^\]]*)\]\(([^\s)]+)\)',line):
                u=urllib.parse.urlsplit(url);row=dict(path=path,line=n,label=label,url=url)
                if u.scheme or u.netloc:row.update(kind='external',network_checked=False)
                elif not u.path:row.update(kind='anchor',body_credit=0)
                else:
                    p=posixpath.normpath(posixpath.join(posixpath.dirname(path),urllib.parse.unquote(u.path)))
                    q=subprocess.run(G+['cat-file','-t',c+':'+p.rstrip('/')],cwd=R,capture_output=True)
                    row.update(kind='local',target=p,exists=q.returncode==0,git_type=q.stdout.decode().strip(),anchor=u.fragment)
                rows.append(row)
    local=[r for r in rows if r['kind']=='local']
    out.append(dict(commit=c,local_count=len(local),local_resolved=sum(r['exists'] for r in local),missing_occurrences=[r for r in local if not r['exists']],missing_unique=sorted({r['target'] for r in local if not r['exists']}),all_destinations=rows))
h='e58486178e746273fb6fab55df00722807f1dc44';root='review/remediation/20261003-prepare/batches/B21/author-draft-1/'
f=subprocess.run(G+['fetch','--no-tags','https://github.com/y805939188/pokemon-essentials-clean-room.git',h],cwd=R,capture_output=True)
(T/'historical-fetch.json').write_text(json.dumps(dict(commit=h,exit=f.returncode,stdout=f.stdout.decode(),stderr=f.stderr.decode(),semantic_credit=0),indent=2)+'\n');assert f.returncode==0
targets=[]
for name in ['README.md','traceability.json','eight-chains.json','static-cases.json']:
    p=root+name;b=git('show',h+':'+p);mode,kind,blob=git('ls-tree',h,'--',p).decode().split('\t')[0].split();targets.append(dict(commit=h,path=p,mode=mode,type=kind,git_blob=blob,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),semantic_credit=0,purpose='HISTORICAL_NAVIGATION_IDENTITY_AND_RETRIEVAL_ONLY'))
report=dict(schema='r8.B.M19.navigation.v1',method='Complete destinations; directories accepted as tree objects; anchors separate. External URLs are immutable navigation, not network availability claims.',inputs=out,historical_targets=targets)
(T/'link-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(summaries=[{k:v for k,v in x.items() if k!='all_destinations'} for x in out],historical_targets=targets),ensure_ascii=False,indent=2))
