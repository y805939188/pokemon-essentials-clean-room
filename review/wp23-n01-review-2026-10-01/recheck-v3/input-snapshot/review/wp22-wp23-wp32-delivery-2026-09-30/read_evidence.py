"""Text-only evidence reader with an audit log, not a reference interpreter."""
from pathlib import Path
import sys,json,hashlib
root=Path(__file__).resolve().parents[2]
out=Path(__file__).resolve().parent
log=out/'reading-log.json'
rows=json.loads(log.read_text()) if log.exists() else []
package=sys.argv[1]
for request in json.load(sys.stdin):
    path,ranges,note=request
    p=root/path
    raw=p.read_bytes();lines=raw.decode('utf-8-sig').splitlines()
    if ranges=='all':ranges=[[1,len(lines)]]
    print('\nFILE '+path+' — '+note)
    for start,end in ranges:
        for i in range(start,min(end,len(lines))+1):print(f'{i}: {lines[i-1]}')
    rows.append({'package':package,'path':path,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'ranges':ranges,'purpose':note})
log.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
