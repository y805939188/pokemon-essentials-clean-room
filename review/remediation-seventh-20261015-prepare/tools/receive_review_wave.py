"""Immutable bounded review reception; no semantic review or model invocation."""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import subprocess
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[3]
P = ROOT / 'review/remediation-seventh-20261015-prepare'
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
REPO = 'y805939188/pokemon-essentials-clean-room'

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def receive(task):
    commit, prefix = task['result_commit'], task['prefix']
    assert git('rev-parse', commit+'^{tree}').decode().strip() == task['result_tree']
    raw = git('diff', '--name-status', '--no-renames', '-z', B, commit).decode().strip('\0').split('\0')
    changed = list(zip(raw[::2], raw[1::2]))
    assert len(raw) == 2*len(changed) and len(changed) == task['files']
    assert all(s == 'A' and p.startswith(prefix) for s,p in changed), 'Review must contain its evidence only'
    modes = {line.split('\t',1)[1]: line.split()[0] for line in git('ls-tree','-r',commit,prefix).decode().splitlines()}
    assert set(modes) == {p for _,p in changed} and set(modes.values()) <= {'100644','100755'}
    data = {p:git('show',commit+':'+p) for _,p in changed}
    assert sum(map(len,data.values())) == task['bytes']
    local = Path('/workspace/r7-review-reception') / (task['label']+'-'+commit)
    def download(path):
        target = local/path
        url = f'https://raw.githubusercontent.com/{REPO}/{commit}/'+urllib.parse.quote(path)
        attempts=[]
        for attempt in range(1,4):
            try:
                with urllib.request.urlopen(url,timeout=40) as response:
                    actual=response.read(len(data[path])+1)
                    status=response.status
                assert actual == data[path], path
                target.parent.mkdir(parents=True,exist_ok=True)
                if target.exists():
                    assert target.read_bytes() == actual, 'Conflicting existing reception preserved'
                else:
                    target.write_bytes(actual)
                attempts.append(dict(attempt=attempt,http_status=status,complete_byte_match=True))
                return dict(path=path,**identity(actual),git_mode=modes[path],url=url,attempts=attempts)
            except (OSError, TimeoutError) as error:
                attempts.append(dict(attempt=attempt,error=str(error)))
                if attempt == 3:
                    raise
                time.sleep(attempt)
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        records=list(pool.map(download,data))
    output = P/'review-receptions'/task['label']
    output.mkdir(parents=True,exist_ok=True)
    for name in ['report.md','per-id.json','review-input-receipt.json','artifact-manifest.json']:
        content=data[prefix+name]
        path=output/name
        if path.exists():
            assert path.read_bytes() == content
        else:
            path.write_bytes(content)
    receipt=dict(schema='r7.actual-review-complete-reception.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),parent_receipt=task,complete_diff_against_B=[dict(status=s,path=p) for s,p in changed],files=records,local_exact_bytes=str(local),counts=dict(files=len(records),bytes=sum(x['bytes'] for x in records)),qualification='Every immutable remote byte equals actual Git blob; only transport/scope/identity TOOL_VALIDATION. Semantic and independence decisions recorded separately; no model or behavior execution credit.')
    (output/'reception.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    return dict(label=task['label'],files=len(records),bytes=task['bytes'],reception=str(output.relative_to(ROOT)))

def main():
    tasks=json.loads((P/'intake/20261015-review-wave/parent-receipt.json').read_text())['entries']
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(receive,tasks):
            print(json.dumps(result),flush=True)

if __name__ == '__main__':
    main()
