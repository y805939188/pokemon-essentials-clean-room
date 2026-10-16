"""Restore navigation-bound historical bytes from the isolated exact-object cache."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

TASK=Path(__file__).resolve().parent
CACHE=TASK/'object-cache.git'
DEST=TASK/'recovered-cache-r6'

def main():
    assert not DEST.exists() and not DEST.is_symlink()
    assert not any(p.is_symlink() for p in DEST.parents)
    fetched=json.loads((TASK/'isolated-git-recovery.json').read_text())
    commits={x['commit']:x for x in fetched['objects']}
    old=json.loads((TASK/'recovered-transport/history/recovery-identity-verification.json').read_text())
    selected=[r['declared'] for r in old if r['declared']['commit'] in commits]
    DEST.mkdir()
    receipts=[]
    for row in selected:
        p=Path(row['path']);assert not p.is_absolute() and '..' not in p.parts
        argv=['git','--git-dir',str(CACHE),'show',row['commit']+':'+row['path']]
        start=datetime.datetime.now(datetime.timezone.utc).isoformat()
        command=subprocess.run(argv,capture_output=True)
        record={'argv':argv,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'exit_code':command.returncode,'stderr':command.stderr.decode(errors='replace'),
                'declared':row,'semantic_credit':False}
        if command.returncode:
            record['status']='FAILED_EXACT_BYTE_RESTORATION'
        else:
            data=command.stdout
            actual={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                    'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
            assert all(actual[k]==row[k] for k in actual),(row['path'],actual)
            target=DEST/row['commit']/p;target.parent.mkdir(parents=True,exist_ok=True)
            with target.open('xb') as f:f.write(data)
            entry=subprocess.check_output(['git','--git-dir',str(CACHE),'ls-tree',row['commit'],'--',row['path']]).decode().split()
            assert entry[2]==actual['git_blob']
            record.update(status='RESTORED_EXACT_ORIGINAL_BYTES',actual=actual,mode=entry[0],
                          tree=commits[row['commit']]['tree'],local_path=str(target))
        receipts.append(record)
        (TASK/'cached-r6-recovery-manifest.json').write_text(json.dumps({'files':receipts,'cache':str(CACHE)},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'files':len(receipts),'failed':sum(r['status']!='RESTORED_EXACT_ORIGINAL_BYTES' for r in receipts),
                      'bytes':sum(r.get('actual',{}).get('bytes',0) for r in receipts),'semantic_credit':False}))

if __name__=='__main__':main()
