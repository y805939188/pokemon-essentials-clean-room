import pathlib,subprocess,sys,json,datetime,os
root=pathlib.Path(__file__).resolve().parents[5];e=pathlib.Path(__file__).resolve().parent;logs=e/'commands';logs.mkdir(exist_ok=True);label=sys.argv[1];args=sys.argv[2:];start=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (logs/(label+'.stdout')).open('wb') as out,(logs/(label+'.stderr')).open('wb') as err:
 p=subprocess.Popen(args,cwd=root,stdout=out,stderr=err);pid=p.pid;status=p.wait()
row={'label':label,'argv':args,'cwd':str(root),'pid':pid,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':status,'stdout':'commands/'+label+'.stdout','stderr':'commands/'+label+'.stderr'}
with (e/'commands.jsonl').open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
print(json.dumps(row,ensure_ascii=False));sys.exit(status)
