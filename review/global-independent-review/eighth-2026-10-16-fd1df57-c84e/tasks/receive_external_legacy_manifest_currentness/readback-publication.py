"""Read exact published bytes through an isolated remote-only bare repository."""
from pathlib import Path
import argparse, subprocess, hashlib, json, datetime

TASK = Path(__file__).resolve().parent
REPO = TASK.parents[4]
PREFIX = str(TASK.relative_to(REPO))
URL = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
BRANCH = 'refs/heads/codex/r8-receive-legacy-manifest-currentness-20261016'
BARE = Path('/tmp/r8-receive-legacy-publication.git')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('commit')
    parser.add_argument('--receipt')
    args = parser.parse_args()
    assert len(args.commit) == 40 and all(c in '0123456789abcdef' for c in args.commit)
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    operations = []
    def run(argv, data=None):
        began = datetime.datetime.now(datetime.timezone.utc).isoformat()
        p = subprocess.run(argv, input=data, capture_output=True, cwd=REPO)
        operations.append({'argv':argv,'start_utc':began,
                           'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                           'exit':p.returncode,'stdout':p.stdout.decode(errors='replace') if not argv[-2:-1]==['blob'] else 'BINARY_BYTES_CHECKED',
                           'stderr':p.stderr.decode(errors='replace')})
        if p.returncode:
            raise RuntimeError(json.dumps(operations[-1],ensure_ascii=False))
        return p.stdout
    if not BARE.exists():
        run(['git','init','--bare',str(BARE)])
    assert not BARE.is_symlink() and not (BARE/'objects/info/alternates').exists()
    remote = run(['git','ls-remote',URL,BRANCH]).decode().strip().split()
    assert remote == [args.commit,BRANCH],remote
    git = ['git','--git-dir='+str(BARE)]
    run(git+['fetch','--no-tags','--depth=1','--filter=blob:none',URL,args.commit])
    tree = run(git+['rev-parse',args.commit+'^{tree}']).decode().strip()
    task_tree = run(git+['rev-parse',args.commit+':'+PREFIX]).decode().strip()
    listing = run(git+['ls-tree','-rz',args.commit,PREFIX])
    expected = subprocess.check_output(['git','ls-tree','-rz',args.commit,PREFIX],cwd=REPO)
    assert listing == expected
    entries = []
    for row in listing.split(b'\0'):
        if row:
            header,path=row.split(b'\t')
            mode,kind,blob=header.decode().split()
            assert kind=='blob' and mode=='100644'
            entries.append((mode,blob,path.decode()))
    # Batch all requested blobs from the remote, avoiding one network call per file.
    wanted='\n'.join(sorted({blob for _,blob,_ in entries}))+'\n'
    run(git+['fetch','--no-tags','--filter=blob:none','--stdin',URL],wanted.encode())
    verified=[]
    for mode,blob,path in entries:
        data=subprocess.check_output(git+['cat-file','blob',blob],cwd=REPO)
        local=subprocess.check_output(['git','cat-file','blob',blob],cwd=REPO)
        sha=hashlib.sha256(data).hexdigest()
        assert data==local
        assert hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()==blob
        verified.append({'path':path,'mode':mode,'blob':blob,'bytes':len(data),'sha256':sha,'full_remote_bytes_read':True})
    assert subprocess.check_output(['git','rev-parse',args.commit+'^{tree}'],cwd=REPO).decode().strip()==tree
    assert subprocess.check_output(['git','rev-parse',args.commit+':'+PREFIX],cwd=REPO).decode().strip()==task_tree
    receipt={'schema':'r8-lmc-publication-remote-readback/v1','start_utc':start,
             'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'commit':args.commit,'tree':tree,'task_tree':task_tree,'branch':BRANCH,
             'bare':str(BARE),'remote_only_no_alternates':True,'exact_set':True,
             'files':verified,'file_count':len(verified),'bytes':sum(r['bytes'] for r in verified),
             'operations':operations,'all_modes_blobs_bytes_sha256_match':True,
             'semantic_credit':0,'task_semantic_status':'INCOMPLETE','update_started':False}
    if args.receipt:
        rel=Path(args.receipt)
        assert not rel.is_absolute() and '..' not in rel.parts
        output=TASK/rel
        assert not output.exists() and not any(p.is_symlink() for p in output.parents)
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in {'files','operations'}},ensure_ascii=False))

if __name__=='__main__':
    main()
