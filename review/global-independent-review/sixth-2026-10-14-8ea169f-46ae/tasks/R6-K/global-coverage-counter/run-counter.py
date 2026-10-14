from pathlib import Path
import subprocess,datetime,json,hashlib,sys
P=Path(__file__).parent
names=['check-ranges.py','check-mappings.py','check-types.py','check-finite-contracts.py','check-source-chains.py'];out=[]
for n in names:
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run([sys.executable,str(P/n)],capture_output=True,text=True);end=datetime.datetime.now(datetime.timezone.utc).isoformat()
 stem=n[:-3];(P/(stem+'.stdout.log')).write_text(r.stdout);(P/(stem+'.stderr.log')).write_text(r.stderr)
 z={'command':[sys.executable,str(P/n)],'script_sha256':hashlib.sha256((P/n).read_bytes()).hexdigest(),'start_utc':start,'end_utc':end,'exit_code':r.returncode,'stdout_log':stem+'.stdout.log','stderr_log':stem+'.stderr.log','stdout_sha256':hashlib.sha256(r.stdout.encode()).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr.encode()).hexdigest(),'evidence':'TOOL_VALIDATION_ADMINISTRATIVE_STATIC_REVIEW_PAYLOADS_ONLY','reference_functions_executed':0,'native_or_host':0}
 out.append(z)
 with(P/'commands.jsonl').open('a')as w:w.write(json.dumps(z,ensure_ascii=False)+'\n')
 print(n,r.returncode,flush=True)
 if r.returncode:break
(P/'run-result.json').write_text(json.dumps({'commands':out,'all_completed':len(out)==len(names)and all(x['exit_code']==0 for x in out),'actual_UTC_captured_here_not_backfilled_for_earlier_attempts':True},ensure_ascii=False,indent=2)+'\n')
