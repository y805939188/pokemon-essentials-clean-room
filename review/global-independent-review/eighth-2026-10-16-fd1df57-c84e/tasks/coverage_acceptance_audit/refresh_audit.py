import pathlib,json,subprocess,datetime,hashlib
out=pathlib.Path('tasks/coverage_acceptance_audit'); steps=[]
for name in ['audit_coverage.py','extend_audit.py','build_followups.py','audit_native_handoff.py','audit_late_deliveries.py']:
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.run(['python',str(out/name)],stdout=subprocess.PIPE,stderr=subprocess.PIPE);end=datetime.datetime.now(datetime.timezone.utc).isoformat()
 (out/(name+'.stdout.json')).write_bytes(p.stdout);(out/(name+'.stderr.txt')).write_bytes(p.stderr)
 steps.append({'script':name,'script_sha256':hashlib.sha256((out/name).read_bytes()).hexdigest(),'start_utc':start,'end_utc':end,'exit':p.returncode,'stdout':name+'.stdout.json','stderr':name+'.stderr.txt','evidence':'TOOL_VALIDATION; no source/model/host behavior'})
 if p.returncode:break
(out/'refresh-execution.json').write_text(json.dumps({'steps':steps,'behavior_executions':0},ensure_ascii=False,indent=2)+'\n')
a=json.loads((out/'acceptance-register.json').read_text());print(json.dumps({'steps':[(r['script'],r['exit']) for r in steps],'files':a['file_counts'],'issues':a['issues'],'late_counts':{k:len(v) for k,v in a.get('late_deliveries_audit',{}).items() if isinstance(v,list)}},ensure_ascii=False,indent=2))
