"""Read an exact pushed report commit in a new remote-only bare store.

Unchanged recovered input bytes may reuse the independently fetched exact target
cache. All newly authored report blobs are fetched and read from the new store.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess
import sys

TASK = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/receive_external_pbs_creature_backups'
REMOTE = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
TARGET_CACHE = '/tmp/r8-receive-pbs-target.git'

def run(args, **kwargs):
    return subprocess.check_output(args, **kwargs)

def listing(command, commit):
    result={}
    for item in run(command+['ls-tree','-rz',commit,'--',TASK]).split(b'\0'):
        if item:
            metadata,path=item.split(b'\t',1)
            mode,typ,blob=metadata.decode().split()
            assert typ=='blob' and mode=='100644'
            result[path.decode()]=(mode,blob)
    return result

def main():
    commit,phase=sys.argv[1:]
    assert re.fullmatch('[0-9a-f]{40}',commit) and re.fullmatch('[a-z0-9-]+',phase)
    bare=Path('/tmp/r8-receiver-readback-'+phase+'.git')
    receipt=Path('/tmp/r8-receiver-readback-'+phase+'.json')
    assert not bare.exists() and not receipt.exists()
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    run(['git','init','--bare',str(bare)])
    command=['git','--git-dir='+str(bare)]
    run(command+['remote','add','origin',REMOTE])
    fetch=subprocess.run(command+['fetch','--no-tags','--depth=1','--filter=blob:none','origin',commit],capture_output=True)
    assert fetch.returncode==0,fetch.stderr.decode()
    local=['git']
    expected=listing(local,commit)
    actual=listing(command,commit)
    assert expected==actual
    local_tree=run(local+['rev-parse',commit+'^{tree}']).decode().strip()
    remote_tree=run(command+['rev-parse',commit+'^{tree}']).decode().strip()
    local_task_tree=run(local+['rev-parse',commit+':'+TASK]).decode().strip()
    remote_task_tree=run(command+['rev-parse',commit+':'+TASK]).decode().strip()
    assert local_tree==remote_tree and local_task_tree==remote_task_tree
    original=json.loads(Path(TASK+'/recovery.json').read_text())
    input_blobs={r['git_blob'] for r in original['files']}
    rows=[]
    for path,(mode,blob) in sorted(actual.items()):
        is_input=path.startswith(TASK+'/recovered-target/') and blob in input_blobs
        source=['git','--git-dir='+TARGET_CACHE] if is_input else command
        data=run(source+['cat-file','blob',blob])
        local_data=run(local+['cat-file','blob',blob])
        assert data==local_data
        assert hashlib.sha1(('blob '+str(len(data))+'\0').encode()+data).hexdigest()==blob
        rows.append(dict(path=path,mode=mode,blob=blob,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                         byte_read_origin='EXACT_TARGET_INDEPENDENT_REMOTE_CACHE' if is_input else 'NEW_REMOTE_ONLY_BARE_STORE'))
    output=dict(schema='r8-complete-report-remote-readback/v1',utc_start=started,utc_end=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        remote=REMOTE,commit=commit,checkout_tree=remote_tree,task_tree=remote_task_tree,
        bare=str(bare),no_alternates=True,fetch_command=command+['fetch','--no-tags','--depth=1','--filter=blob:none','origin',commit],
        fetch_exit=fetch.returncode,fetch_stdout=fetch.stdout.decode(),fetch_stderr=fetch.stderr.decode(),
        collection_exact=True,files=rows,count=len(rows),bytes=sum(r['bytes'] for r in rows),
        all_authored_report_blobs_read_from_new_remote_store=True,unchanged_input_alias_cache_count=sum(r['byte_read_origin']=='EXACT_TARGET_INDEPENDENT_REMOTE_CACHE' for r in rows),
        semantic_credit=0,behavior_execution='NOT_EXECUTED',task_status='INCOMPLETE')
    receipt.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(receipt=str(receipt),commit=commit,checkout_tree=remote_tree,task_tree=remote_task_tree,count=len(rows),bytes=output['bytes'],collection_exact=True,task_status='INCOMPLETE')))

if __name__ == '__main__':
    main()
