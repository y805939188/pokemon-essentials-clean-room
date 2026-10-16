"""Static objdump only, bounded by real PE runtime-function entries."""
import pathlib,json,struct,subprocess,datetime,sys
ROOT=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes();pe=json.loads((ROOT/'pe-sections.json').read_text())['Game.exe'];s=next(s for s in pe['sections'] if s['name']=='.pdata');rows=[]
for p in range(s['offset'],s['offset']+s['virtual_size'],12):
 a,z,u=struct.unpack_from('<III',b,p);rows.append((a-3072,z-3072,u,p))
report=[]
for arg in sys.argv[1:]:
 n=int(arg);hit=[r for r in rows if r[0]<=n<r[1]];assert len(hit)==1,(n,hit);a,z,u,p=hit[0]
 name='native-'+str(a);cmd=['objdump','-d','-w','--start-address='+hex(pe['image_base']+a+3072),'--stop-address='+hex(pe['image_base']+z+3072),'/workspace/pokemon-essentials/Game.exe'];start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True);(ROOT/(name+'.stdout')).write_bytes(r.stdout);(ROOT/(name+'.stderr')).write_bytes(r.stderr);report.append({'query_offset':n,'function_start':a,'function_end':z,'pdata_record_offset':p,'unwind_rva':u,'command':cmd,'stdout':name+'.stdout','stderr':name+'.stderr','start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':r.returncode})
out=ROOT/('native-window-executions-'+sys.argv[1]+'.json');assert not out.exists();out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
