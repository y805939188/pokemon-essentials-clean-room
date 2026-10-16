"""Authorized ordinary publication of this task directory using isolated index."""
from pathlib import Path
import json,os,subprocess,hashlib,datetime,argparse
T=Path(__file__).parent;REPO=T.parents[4];W=T/'.publication-work'
BRANCH='refs/heads/codex/r8-external-h-c2-current-records-20261016'
CONTRACT='30cfed0996003b6ebf4b5c51cc04f31ca9255440'
def run(args,**kw):return subprocess.check_output(['git',*args],cwd=REPO,**kw)
ap=argparse.ArgumentParser();ap.add_argument('phase',choices=['core','binding']);a=ap.parse_args()
parent=run(['rev-parse',BRANCH]).decode().strip()
if a.phase=='core':assert parent=='3fdc7fc5bfaf51edd1e01c9fe8216aa2dd9eecb0'
else:assert parent==json.loads((W/'completion-core.json').read_text())['commit']
prefix=str(T.relative_to(REPO))+'/'
paths=run(['ls-files','--others','--exclude-standard','--',prefix]).decode().splitlines()
assert paths and all(p.startswith(prefix) for p in paths)
env=dict(os.environ,GIT_INDEX_FILE=str(W/f'completion-{a.phase}.index'))
assert not Path(env['GIT_INDEX_FILE']).exists()
run(['read-tree',parent],env=env)
oldpaths=run(['ls-tree','-r','--name-only',parent,'--',prefix]).decode().splitlines()
for path in set(oldpaths)-set(paths):run(['update-index','--force-remove','--',path],env=env)
rows=[]
for path in sorted(paths):
    data=(REPO/path).read_bytes();blob=run(['hash-object','-w','--stdin'],input=data).decode().strip()
    run(['update-index','--add','--cacheinfo','100644',blob,path],env=env)
    rows.append(dict(path=path,mode='100644',blob=blob,bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
tree=run(['write-tree'],env=env).decode().strip()
commit=run(['commit-tree',tree,'-p',parent],input=f'R8 H-C2 external: {a.phase} complete record and purpose evidence\n'.encode()).decode().strip()
changed=run(['diff-tree','--no-commit-id','--name-only','-r',CONTRACT,commit]).decode().splitlines()
assert set(changed)==set(paths),(len(changed),len(paths),set(changed)^set(paths))
tasktree=run(['rev-parse',commit+':'+prefix.rstrip('/')]).decode().strip()
record=dict(phase=a.phase,commit=commit,parent=parent,workspace_tree=tree,report_tree=tasktree,report_path=prefix.rstrip('/'),
    branch=BRANCH,files=len(rows),bytes=sum(x['bytes'] for x in rows),payloads=rows,only_own_directory_delta=True,
    utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
(W/f'completion-{a.phase}.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
run(['update-ref',BRANCH,commit,parent])
result=subprocess.run(['git','push','origin',BRANCH+':'+BRANCH],cwd=REPO,capture_output=True,text=True,timeout=55)
record['ordinary_push']={'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr}
(W/f'completion-{a.phase}.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
assert result.returncode==0,record['ordinary_push']
print(json.dumps({k:v for k,v in record.items() if k!='payloads'},ensure_ascii=False,indent=2))
