"""Read back every newly published A blob from GitHub into an isolated bare."""
import os, sys, json, pathlib, hashlib, subprocess, datetime
from recover import T, save

commit, base, output = sys.argv[1:]
repo = T.parents[6]
prefix = str(T.relative_to(repo)) + '/'
url = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
bare = T/'.work/publication.git'
env = os.environ.copy()
for key in ('GIT_ALTERNATE_OBJECT_DIRECTORIES','GIT_OBJECT_DIRECTORY','GIT_COMMON_DIR','GIT_DIR','GIT_WORK_TREE'):
    env.pop(key,None)
def run(args, payload=None):
    p = subprocess.run(args, input=payload, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, env=env)
    if p.returncode:
        raise RuntimeError((args,p.returncode,p.stderr.decode(errors='replace')[-4000:]))
    return p.stdout, p.stderr
def local(*args): return run(['git','-C',str(repo),*args])[0]
def remote(*args, payload=None): return run(['git','--git-dir='+str(bare),*args],payload)
if not bare.exists():
    run(['git','init','--bare',str(bare)])
    remote('remote','add','origin',url)
    remote('config','remote.origin.promisor','true')
    remote('config','remote.origin.partialclonefilter','blob:none')
assert not (bare/'objects/info/alternates').exists()
fetch_out, fetch_err = remote('-c','protocol.version=2','fetch','--depth=1','--filter=blob:none','origin',commit)
remote_commit = remote('rev-parse','FETCH_HEAD')[0].decode().strip()
assert remote_commit == commit
assert remote('cat-file','commit',commit)[0] == local('cat-file','commit',commit)
changed = [s for s in local('diff','--name-only','-z',base,commit).decode().split('\0') if s]
assert changed and all(s.startswith(prefix)for s in changed)
assert remote('ls-tree','-r','-z',commit,'--',prefix)[0] == local('ls-tree','-r','-z',commit,'--',prefix)
assert remote('rev-parse',commit+':'+prefix[:-1])[0] == local('rev-parse',commit+':'+prefix[:-1])
rows=[]
for path in changed:
    entry=local('ls-tree',commit,'--',path).decode().strip()
    assert entry
    mode, typ, rest=entry.split(' ',2);oid=rest.split('\t')[0]
    assert typ=='blob'
    rows.append({'path':path,'mode':mode,'git_blob':oid})
# --batch auto-fetches missing promisor blobs from the configured remote.
# All stdout remains inside this process; only hashes/counts are printed.
payload=''.join(r['git_blob']+'\n' for r in rows).encode()
raw, blob_fetch_err = remote('cat-file','--batch',payload=payload)
offset=0
for r in rows:
    end=raw.index(b'\n',offset);header=raw[offset:end].decode().split(' ')
    assert header[0]==r['git_blob'] and header[1]=='blob'
    size=int(header[2]);start=end+1;data=raw[start:start+size]
    assert raw[start+size:start+size+1]==b'\n'
    offset=start+size+1
    expected=local('show',commit+':'+r['path'])
    assert data==expected
    r.update(bytes=size,sha256=hashlib.sha256(data).hexdigest(),same_bytes=True)
assert offset==len(raw)
receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'result':'PASS_FULL_OWN_INCREMENT_REMOTE_READBACK','commit':commit,'base':base,
 'remote_url':url,'ordinary_exact_fetch':True,'filter':'blob:none; all changed blobs fetched and read in full',
 'cache':'A/.work/publication.git; no alternates; inherited Git object environment removed',
 'fetch_stdout':fetch_out.decode(),'fetch_stderr':fetch_err.decode(),
 'auto_blob_fetch_stderr':blob_fetch_err.decode(),
 'checkout_tree':local('rev-parse',commit+'^{tree}').decode().strip(),
 'A_tree':local('rev-parse',commit+':'+prefix[:-1]).decode().strip(),
 'complete_A_path_mode_blob_tree_equal':True,'changed_count':len(rows),
 'changed_bytes':sum(r['bytes']for r in rows),'files':rows,
 'behavior':'NOT_EXECUTED','semantic_credit':0,
 'qualification':'Only this receiver new publication delta was verified; old input publication identity was reused. This is transport equality, not semantic acceptance.'}
save(T/output,receipt)
print(json.dumps({k:receipt[k]for k in ('result','commit','base','changed_count','changed_bytes','checkout_tree','A_tree','complete_A_path_mode_blob_tree_equal')},ensure_ascii=False))
