"""Read only this task's new publication delta through an isolated ordinary fetch."""
import argparse
import datetime
import json
import pathlib
import subprocess
from check_inputs import REPO, OUT, CONTRACT, git, identity

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--commit',required=True)
    parser.add_argument('--bare',required=True)
    parser.add_argument('--receipt',action='store_true')
    args=parser.parse_args()
    commit=args.commit
    bare=pathlib.Path(args.bare)
    prefix=str(OUT.relative_to(REPO))
    remote=git(REPO,'remote','get-url','origin').decode().strip()
    if not bare.exists():
        subprocess.run(['git','init','--bare',str(bare)],check=True,stdout=subprocess.DEVNULL)
        subprocess.run(['git','-C',str(bare),'remote','add','origin',remote],check=True)
    subprocess.run(['git','-C',str(bare),'fetch','--filter=blob:none','--depth=1','origin',commit],check=True)
    changed=git(REPO,'diff','--name-only',CONTRACT,commit).decode().splitlines()
    assert changed and all(p.startswith(prefix+'/') for p in changed)
    local=git(REPO,'ls-tree','-r',commit,'--',prefix)
    fetched=git(bare,'ls-tree','-r',commit,'--',prefix)
    assert local==fetched
    rows=[]
    for row in fetched.decode().splitlines():
        left,path=row.split('\t',1)
        mode,kind,blob=left.split()
        assert kind=='blob' and mode=='100644'
        raw=git(bare,'show',commit+':'+path)
        assert raw==git(REPO,'show',commit+':'+path)
        actual=identity(raw)
        assert blob==actual['git_blob']
        rows.append(dict(path=path,mode=mode,**actual,remote_bytes_equal=True))
    assert set(changed)=={x['path'] for x in rows}
    tree=git(bare,'rev-parse',commit+'^{tree}').decode().strip()
    subtree=git(bare,'rev-parse',commit+':'+prefix).decode().strip()
    assert tree==git(REPO,'rev-parse',commit+'^{tree}').decode().strip()
    assert subtree==git(REPO,'rev-parse',commit+':'+prefix).decode().strip()
    result=dict(schema='r8-cp01-publication/v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        contract_commit=CONTRACT,core_commit=commit,checkout_tree=tree,task_tree=subtree,
        branch='codex/r8-cp-reception-01-20261016',repository='y805939188/pokemon-essentials-clean-room',
        isolated_bare=str(bare),readback='PASS_ALL_SELF_DELTA_FILES',files=rows,file_count=len(rows),
        total_bytes=sum(x['bytes'] for x in rows),scope='This task new report files only; no re-read of unchanged global/source input payloads.',
        proof='Ordinary independent remote fetch; exact file set/mode/blob/bytes/SHA256 and checkout/subtree equal.',
        final_receipt_rule='This receipt binds preceding semantic core; successor receipt commit is returned externally. Its own future commit is intentionally absent.',
        semantic_credit=0,reference_execution='NOT_EXECUTED',UPDATE_NOT_STARTED=True)
    if args.receipt:
        (OUT/'publication.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['core_commit','checkout_tree','task_tree','readback','file_count','total_bytes']}))

if __name__=='__main__':
    main()
