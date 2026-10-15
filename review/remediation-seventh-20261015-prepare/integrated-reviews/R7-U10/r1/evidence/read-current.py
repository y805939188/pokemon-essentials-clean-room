"""Plain fixed-snapshot text reader with exact range receipt; no semantic verdict."""
from pathlib import Path
import sys,hashlib,json,datetime,os
R=Path('/workspace/r7-ir-R7-U10-wave3');p=R/'actual-input/actual'/sys.argv[1];lines=p.read_bytes().splitlines(keepends=True);a=int(sys.argv[2]);b=int(sys.argv[3]);chunk=b''.join(lines[a-1:b]);assert 1<=a<=b<=len(lines)
print(f'FILE {sys.argv[1]} L{a}-{b} / {len(lines)}')
print(chunk.decode(),end='')
o=R/'result-checkout/review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U10/r1/evidence/continuation-read-receipts.jsonl'
with o.open('a') as f:f.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'path':sys.argv[1],'first_line':a,'last_line':b,'total_lines':len(lines),'bytes':len(chunk),'sha256':hashlib.sha256(chunk).hexdigest(),'classification':'TEXT_DELIVERY_ONLY_NOT_SEMANTIC_VERDICT'},ensure_ascii=False)+'\n')
