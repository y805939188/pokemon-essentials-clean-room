"""Fetch exact navigation-bound objects into a new isolated bare cache only."""
from pathlib import Path
import datetime
import json
import subprocess

REPO=Path('/workspace/pokemon-essentials-clean-room')
TASK=Path(__file__).resolve().parent
CACHE=TASK/'object-cache.git'
ORIGIN='https://github.com/y805939188/pokemon-essentials-clean-room.git'
NAV=REPO/'delivery/2026-10-14-sixth/history-navigation.json'

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()

def main():
    if CACHE.exists() or CACHE.is_symlink() or any(p.is_symlink() for p in CACHE.parents):
        raise ValueError('isolated bare cache must not already exist or include symlinks')
    nav=json.loads(NAV.read_text())
    targets=[{'commit':nav['original_sixth_report']['commit'],'archive_tag':nav['original_sixth_report']['archive_tag'],'purpose':'Original R6 report'}]
    targets += [{'commit':x['report_commit'],'purpose':'Original actual group'+x['group']} for x in nav['actual_independent_reports']]
    targets += [{'commit':nav['final_independent_registry_audit']['audit_commit'],'purpose':'Final independent registry audit'}]
    rows=[]
    def run(argv):
        row={'argv':argv,'cwd':str(REPO),'start_utc':utc()}
        p=subprocess.run(argv,cwd=REPO,capture_output=True,text=True)
        row.update(end_utc=utc(),exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
        rows.append(row)
        (TASK/'isolated-git-recovery-io.json').write_text(json.dumps({'targets':targets,'commands':rows},ensure_ascii=False,indent=2)+'\n')
        if p.returncode:raise RuntimeError('Command failed; exact real I/O is preserved')
        return p.stdout.strip()
    run(['git','init','--bare',str(CACHE)])
    (CACHE/'objects/info/alternates').write_text(str((REPO/'.git/objects').resolve())+'\n')
    run(['git','--git-dir',str(CACHE),'remote','add','origin',ORIGIN])
    run(['git','--git-dir',str(CACHE),'config','remote.origin.promisor','true'])
    run(['git','--git-dir',str(CACHE),'config','remote.origin.partialclonefilter','blob:none'])
    run(['git','--git-dir',str(CACHE),'fetch','--no-tags','--depth=1','--filter=blob:none','origin',*[t['commit'] for t in targets]])
    result=[]
    for t in targets:
        typ=run(['git','--git-dir',str(CACHE),'cat-file','-t',t['commit']])
        tree=run(['git','--git-dir',str(CACHE),'rev-parse',t['commit']+'^{tree}'])
        result.append({**t,'type':typ,'tree':tree,'status':'EXACT_COMMIT_FETCHED','semantic_credit':False})
    (TASK/'isolated-git-recovery.json').write_text(json.dumps({'completed_utc':utc(),'cache':str(CACHE),'origin':ORIGIN,'read_only_alternates':str(REPO/'.git/objects'),'files_restored':0,'objects':result,'semantic_credit':False},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'fetched_exact_commits':len(result),'cache':str(CACHE),'semantic_credit':False}))

if __name__=='__main__':main()
