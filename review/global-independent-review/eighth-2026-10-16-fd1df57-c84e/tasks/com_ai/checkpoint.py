from pathlib import Path
import json,datetime
out=Path(__file__).resolve().parent
ident=json.loads((out/'identities.json').read_text()); now=datetime.datetime.now(datetime.timezone.utc).isoformat()
logs=[json.loads(p.read_text()) for p in sorted((out/'io').glob('*.json'))]
files=[]
for x in ident['files']:
 p=str(Path(x['repo'])/x['path']); ints=sorted((r['start_line'],r['end_line']) for r in logs if r['path']==p and r['exit_code']==0); merged=[]
 for a,b in ints:
  if merged and a<=merged[-1][1]+1: merged[-1][1]=max(b,merged[-1][1])
  else: merged.append([a,b])
 read=sum(b-a+1 for a,b in merged); full=read==x['line_count']; files.append({**x,'semantic_status':'FULL_TEXT_ACTUALLY_READ' if full else 'PARTIAL_TEXT_ACTUALLY_READ' if read else 'UNREAD','read_intervals':merged,'read_lines':read,'unread_lines':x['line_count']-read,'mapping_status':'IN_PROGRESS_NOT_ACCEPTED_FROM_READ_ALONE','evidence_level':'SOURCE_STATIC' if x['kind']=='reference' and read else 'FORMAL_TEXT_READ' if read else 'INVENTORY_ONLY','reader':'/root/com_ai'})
ledger={'schema':'gr8-com-ai-reading-ledger/v1','updated_utc':now,'reader':'/root/com_ai','read_scope':'Full continuous text per intervals. These do not alone certify every formal assertion or consumer. Manual semantic units are in semantic-units.json.','files':files,'all_files':29,'full_read':sum(x['unread_lines']==0 for x in files),'unread_files':sum(x['read_lines']==0 for x in files),'partial_files':sum(x['read_lines']>0 and x['unread_lines']>0 for x in files),'remaining_unread_lines':sum(x['unread_lines'] for x in files),'business_execution':'NOT_EXECUTED','new_behavior_runs':0}
(out/'reading-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
progress=json.loads((out/'progress.json').read_text());progress.update({'updated_utc':now,'read_full':ledger['full_read'],'reference_full_read':sum(x['kind']=='reference' and x['unread_lines']==0 for x in files),'formal_full_read':sum(x['kind']=='formal' and x['unread_lines']==0 for x in files),'partially_read':ledger['partial_files'],'unread_files':ledger['unread_files'],'remaining_unread_lines':ledger['remaining_unread_lines'],'mapping':'IN_PROGRESS; full text read is not semantic acceptance'});(out/'progress.json').write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:progress[k] for k in ('updated_utc','read_full','reference_full_read','formal_full_read','unread_files','remaining_unread_lines')}))
