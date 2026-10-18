#!/usr/bin/env python3
"""Read-only numbered text recovery; logs original stdout/stderr/exit/UTC under own write set. Does not execute reference material."""
from pathlib import Path
import sys,json,datetime,hashlib
root=Path(__file__).resolve().parent
index=sys.argv[1]; path=Path(sys.argv[2]); start=int(sys.argv[3]); end=int(sys.argv[4])
begin=datetime.datetime.now(datetime.timezone.utc).isoformat(); stdout=''; stderr=''; status=0
try:
 raw=path.read_bytes(); lines=raw.decode('utf-8').splitlines(); end=min(end,len(lines))
 if not 1<=start<=end: raise ValueError('Invalid interval')
 stdout=''.join(f'{i}: {lines[i-1]}\n' for i in range(start,end+1)); identity={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
except Exception as exc:
 stderr=f'{type(exc).__name__}: {exc}\n'; status=1; identity=None
finish=datetime.datetime.now(datetime.timezone.utc).isoformat(); (root/'io').mkdir(exist_ok=True)
record={'argv':sys.argv,'operation':'STATIC_TEXT_READ_NOT_BUSINESS_EXECUTION','start_utc':begin,'end_utc':finish,'path':str(path),'start_line':start,'end_line':end,'identity':identity,'stdout':stdout,'stderr':stderr,'exit_code':status,'reader':'/root/com_ai','semantic_credit':'ONLY_AFTER_ACTUAL_CONTEXT_READING_AND_LEDGER'}
(root/'io'/f'{index}.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
sys.stdout.write(stdout); sys.stderr.write(stderr); sys.exit(status)
