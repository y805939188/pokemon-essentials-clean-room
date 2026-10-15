"""Compare every new/changed publication file with immutable remote HTTP bytes."""
from pathlib import Path
import argparse
import concurrent.futures
import datetime
import hashlib
import json
import subprocess
import time
import urllib.parse
import urllib.request

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--since',required=True)
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[3]
    def git(*argv):
        return subprocess.check_output(['git','-C',str(root),*argv])
    commit=git('rev-parse','HEAD').decode().strip()
    paths=git('diff','--name-only','--diff-filter=AM',args.since,commit).decode().splitlines()
    output=Path('/workspace/r7-remote-readback')/commit
    def receive(path):
        expected=git('show',commit+':'+path)
        url=f'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/{commit}/'+urllib.parse.quote(path)
        attempts=[]
        for attempt in range(1,4):
            try:
                with urllib.request.urlopen(url,timeout=40) as response:
                    actual=response.read(len(expected)+1)
                    status=response.status
                assert actual==expected,path
                target=output/path
                target.parent.mkdir(parents=True,exist_ok=True)
                if target.exists():
                    assert target.read_bytes()==actual
                else:
                    target.write_bytes(actual)
                attempts.append(dict(attempt=attempt,http_status=status,complete_byte_match=True))
                return dict(path=path,bytes=len(actual),sha256=hashlib.sha256(actual).hexdigest(),git_blob=hashlib.sha1(f'blob {len(actual)}\0'.encode()+actual).hexdigest(),url=url,attempts=attempts)
            except (OSError,TimeoutError) as error:
                attempts.append(dict(attempt=attempt,error=str(error)))
                if attempt==3:
                    raise
                time.sleep(attempt)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        files=list(pool.map(receive,paths))
    receipt=dict(schema='r7.publication-delta-full-byte-readback.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),commit=commit,tree=git('rev-parse','HEAD^{tree}').decode().strip(),since=args.since,scope='Every new/changed file since preceding already received publication; no redundant full-package scan',files=files,counts=dict(files=len(files),bytes=sum(r['bytes'] for r in files)),all_match=True)
    output.mkdir(parents=True,exist_ok=True)
    (output/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='files'}))

if __name__=='__main__':
    main()
