import datetime
import difflib
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
OWN=ROOT/'review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/recording-save'
formal,start,end=sys.argv[1:4]
start,end=int(start),int(end)
mirror='review/remediation-sixth-20261014-prepare/candidates/R6-U13/mirror/'+formal
a=subprocess.check_output(['git','show','8ea169fbd0f33f378b5d732fd6bea59e854e04a6:'+formal],cwd=ROOT)
b=(ROOT/mirror).read_bytes()
left,right=a.decode().splitlines(),b.decode().splitlines()
rows=[]
for tag,i,j,k,l in difflib.SequenceMatcher(None,left,right,autojunk=False).get_opcodes():
    if tag=='equal':
        rows.extend((i+t+1,k+t+1,left[i+t]) for t in range(j-i))
    else:
        rows.extend((n+1,None,left[n]) for n in range(i,j))
        rows.extend((None,n+1,right[n]) for n in range(k,l))
end=len(rows) if end==0 else min(end,len(rows))
ids=[]
for role,data,path in [('formal',a,formal),('candidate',b,mirror)]:
    ids.append(dict(role=role,path=path,bytes=len(data),lines=len(data.decode().splitlines()),
                    sha256=hashlib.sha256(data).hexdigest(),
                    git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()))
print(json.dumps(dict(identities=ids,paired_rows=len(rows)),ensure_ascii=False))
for i in range(start,end+1):
    ln,rn,s=rows[i-1]
    print(f'{i} [F{ln or "-"}/C{rn or "-"}]: {s}')
with (OWN/'reading-ledger.jsonl').open('a') as f:
    rec=dict(kind='paired_complete_text',identities=ids,paired_range=[start,end],paired_rows=len(rows),
             formal_range=[min([r[0] for r in rows[start-1:end] if r[0]]),max([r[0] for r in rows[start-1:end] if r[0]])],
             candidate_range=[min([r[1] for r in rows[start-1:end] if r[1]]),max([r[1] for r in rows[start-1:end] if r[1]])],
             utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),argv=sys.argv,cwd=str(ROOT),
             note='Unchanged lines presented once with both positions; every baseline and candidate line is present in union, including deleted and inserted lines. Complete text, not diff-only.')
    f.write(json.dumps(rec,ensure_ascii=False)+'\n')
