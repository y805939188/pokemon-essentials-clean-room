from pathlib import Path
import sys,subprocess,json,datetime
base=Path(__file__).resolve().parent
idx=len(list((base/'io').glob('read-*.json')))+1
p=Path(sys.argv[1]);lines=p.read_text().splitlines(True);start=int(sys.argv[2]) if len(sys.argv)>2 else 1;end=int(sys.argv[3]) if len(sys.argv)>3 else len(lines)
t=datetime.datetime.now(datetime.timezone.utc).isoformat();out=''.join(f'{i+1:5d} '+x for i,x in enumerate(lines) if start<=i+1<=end)
r={'kind':'SOURCE_STATIC_READ','command':sys.argv,'path':str(p),'start_line':start,'end_line':min(end,len(lines)),'total_lines':len(lines),'start_utc':t,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'stdout':out,'stderr':'','exit':0,'semantic_credit':'Only after actual reader interpretation; this log alone grants none.'}
(base/'io'/f'read-{idx:04}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(out,end='')
