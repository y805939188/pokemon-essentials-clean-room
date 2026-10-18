import pathlib,subprocess,json,datetime,uuid,sys
P=pathlib.Path(__file__).resolve().parent
args=sys.argv[1:]
assert args and args[0] in ('rg','git')
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=subprocess.run(args,capture_output=True,text=True,cwd='/workspace/pokemon-essentials')
end=datetime.datetime.now(datetime.timezone.utc).isoformat();n='command-'+uuid.uuid4().hex
(P/'io').mkdir(exist_ok=True)
(P/'io'/f'{n}.stdout').write_text(r.stdout)
(P/'io'/f'{n}.stderr').write_text(r.stderr)
(P/'io'/f'{n}.json').write_text(json.dumps({'argv':args,'cwd':'/workspace/pokemon-essentials','start_utc':start,'end_utc':end,'exit':r.returncode,'stdout':f'{n}.stdout','stderr':f'{n}.stderr','business_execution':'NOT_EXECUTED'},ensure_ascii=False,indent=2)+'\n')
sys.stdout.write(r.stdout);sys.stderr.write(r.stderr)
print(json.dumps({'io':n,'exit':r.returncode,'utc':end}))
raise SystemExit(r.returncode)
