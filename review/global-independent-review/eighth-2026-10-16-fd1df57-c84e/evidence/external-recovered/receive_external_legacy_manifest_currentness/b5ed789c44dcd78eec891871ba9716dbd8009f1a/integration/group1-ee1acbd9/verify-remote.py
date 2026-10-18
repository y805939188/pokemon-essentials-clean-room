"""Read immutable report blobs through a fresh remote-only partial bare repository."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

TASK = Path(__file__).resolve().parent
REPO = TASK.parents[4]
PREFIX = TASK.relative_to(REPO).as_posix()
URL = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
ORIGINAL = 'refs/heads/codex/r8-legacy-reception-group-1-20261016'
BRANCH = 'refs/heads/codex/r8-recovery-legacy-g1-20261016'
CONTRACT = '2d44dafe215842de6355f46de7d4d273d8b4c264'

def run(argv):
    return subprocess.check_output(argv, cwd=REPO)

def main():
    commit, bare_name = sys.argv[1:3]
    bare = Path(bare_name)
    assert len(commit) == 40 and all(c in '0123456789abcdef' for c in commit)
    assert bare.is_absolute() and str(bare).startswith('/tmp/r8-recovery-legacy-g1-')
    if not bare.exists():
        run(['git','init','--bare',str(bare)])
        for key,value in [('remote.origin.url',URL),('remote.origin.promisor','true'),('remote.origin.partialclonefilter','blob:none')]:
            run(['git','--git-dir='+str(bare),'config',key,value])
    assert not (bare/'objects/info/alternates').exists()
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    run(['git','--git-dir='+str(bare),'fetch','--depth=1','--filter=blob:none','origin',commit])
    def remote(*args):
        return run(['git','--git-dir='+str(bare),*args])
    def local(*args):
        return run(['git',*args])
    tree = remote('rev-parse',commit+'^{tree}').decode().strip()
    task_tree = remote('rev-parse',commit+':'+PREFIX).decode().strip()
    assert tree == local('rev-parse',commit+'^{tree}').decode().strip()
    assert task_tree == local('rev-parse',commit+':'+PREFIX).decode().strip()
    raw_entries = remote('ls-tree','-rz',commit,'--',PREFIX)
    assert raw_entries == local('ls-tree','-rz',commit,'--',PREFIX)
    rows = []
    for entry in raw_entries.split(b'\0'):
        if not entry:
            continue
        meta,path = entry.split(b'\t')
        mode,kind,blob = meta.decode().split()
        assert mode == '100644' and kind == 'blob'
        name = path.decode()
        data = remote('show',commit+':'+name)
        expected = local('show',commit+':'+name)
        assert data == expected
        measured_blob = hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
        assert measured_blob == blob
        rows.append({'path':name,'mode':mode,'blob':blob,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    refs_raw = local('ls-remote','--heads','origin',ORIGINAL,BRANCH,'refs/heads/main').decode()
    refs = {line.split()[1]:line.split()[0] for line in refs_raw.splitlines()}
    assert refs[BRANCH] == commit
    assert refs[ORIGINAL] == CONTRACT, 'Original branch has delivered or moved: inspect and deduplicate before continuing.'
    changed = local('diff','--name-only',CONTRACT,commit).decode().splitlines()
    assert changed and all(x.startswith(PREFIX+'/') for x in changed)
    result = {'schema':'r8-recovery-legacy-g1-remote-verification/v1','start_utc':start,
       'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':commit,'checkout_tree':tree,
       'task_tree':task_tree,'branch':BRANCH,'bare_repository':str(bare),'local_alternates':False,
       'path_set_mode_blob_full_bytes_sha256_verified':True,'file_count':len(rows),
       'bytes':sum(r['bytes'] for r in rows),'files':rows,'remote_refs':refs,
       'original_branch_has_no_post_contract_delivery_at_check':True,
       'changed_paths_confined_to_recovery_directory':True,'semantic_credit':0,'business':'NOT_EXECUTED'}
    if len(sys.argv)>3:
        assert sys.argv[3] == 'write-receipt'
        (TASK/'remote-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='files'},ensure_ascii=False))

if __name__ == '__main__':
    main()
