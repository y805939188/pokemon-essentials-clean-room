"""Read fixed blobs in bounded numbered spans and record tool evidence only."""
import datetime, hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path('/workspace/r6-u07-review')
OUT = pathlib.Path(__file__).parent
PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
PUB = '6f6521983006519a0b55a5414177c71a2b59810e'
BASE = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'

def git(args, ref=False):
    cmd = ['git', '--git-dir=/tmp/r6-u07-reference.git'] if ref else ['git', '-C', str(ROOT)]
    return subprocess.check_output(cmd + args)

def read(role, path, start, end):
    ref = role == 'reference'
    commit = {'reference':REF, 'baseline':BASE, 'candidate':PUB, 'prepare':PREP}.get(role, role)
    b = git(['show', commit + ':' + path], ref)
    ident = git(['ls-tree', commit, '--', path], ref).decode().strip()
    lines = b.decode().splitlines()
    end = min(end, len(lines))
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    row = dict(utc=stamp, cwd=str(ROOT), argv=sys.argv, role=role, commit=commit,
               path=path, bytes=len(b), sha256=hashlib.sha256(b).hexdigest(),
               git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),
               tree=git(['rev-parse',commit+'^{tree}'], ref).decode().strip(),
               ls_tree=ident, total_lines=len(lines), read_span=[start,end],
               evidence='TOOL_READ_ONLY; semantic conclusion is separate', exit=0)
    with (OUT/'read-journal.jsonl').open('a') as f:
        f.write(json.dumps(row,ensure_ascii=False)+'\n')
    print(json.dumps(row,ensure_ascii=False))
    for i in range(start-1,end):
        print(f'{i+1}: {lines[i]}')

if __name__ == '__main__':
    read(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))
