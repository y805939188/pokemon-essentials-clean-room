import hashlib,json,sys,datetime
from pathlib import Path
OUT=Path(__file__).resolve().parent
name=sys.argv[1]
if name not in ['R4-qualification-projection.json','R5-qualification-projection.json','R5-metadata-projection.jsonl']:raise SystemExit('unbound projection')
raw=(OUT/name).read_bytes();lines=raw.decode().splitlines();start=int(sys.argv[2]);end=min(int(sys.argv[3]),len(lines))
if start<1 or end<start:raise SystemExit('invalid range')
rec={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'PROJECTION_FULL_CONTENT_PRESENTED_FOR_ELIGIBILITY_SEMANTIC_REVIEW','path':name,'sha256':hashlib.sha256(raw).hexdigest(),'start_line':start,'end_line':end,'total_lines':len(lines),'semantic_pass':False,'source_game_semantics_reviewed':False,'exit_status':0}
with (OUT/'reading-ledger.jsonl').open('a')as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(json.dumps(rec,ensure_ascii=False))
for n in range(start,end+1):print(f'{n:06d} {lines[n-1]}')
