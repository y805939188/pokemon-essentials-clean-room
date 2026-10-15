"""Identity, raw binding and bounded static decoding only; never execute reference programs."""
from pathlib import Path
import datetime,hashlib,json,re,subprocess,zlib
C=Path('/workspace/r7-context/R7-U11-author'); E=Path(__file__).resolve().parent
P=Path('/workspace/r7-bootstrap/R7-U11-author/recovery/batches/R7-U11.json')
plan=json.loads(P.read_bytes())
def ident(d): return {'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'git_blob_content_id':hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()}
files=[]
for row in plan['artifacts']+plan['evidence']+plan['fixed_read_inputs']:
 d=(C/row['local_path']).read_bytes(); a=ident(d)
 assert all(a[k]==row[k] for k in a),(row['local_path'],a)
 files.append({'path':row['local_path'],**a,'full_bytes_read':True,'execution':False})
contract=json.loads((C/'dispatch/delegation/contracts/R7-U11.json').read_bytes())
norm=json.loads((C/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json').read_bytes())
rawdir=C/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs'
refs=[]
def raw_path(sha):
 p=rawdir/(sha+'.raw')
 return p if p.exists() else Path('/workspace/r7-bootstrap/R7-U11-author/supplemental')/(sha+'.raw')
def walk(value):
 if isinstance(value,dict):
  if all(k in value for k in ['input_sha256','json_pointer','raw_member_byte_offsets','raw_member_sha256','canonical_sha256']):
   data=raw_path(value['input_sha256']).read_bytes(); a,b=value['raw_member_byte_offsets']; member=data[a:b]
   assert len(member)==value['raw_member_bytes'] and hashlib.sha256(member).hexdigest()==value['raw_member_sha256']
   obj=json.loads(data)
   for token in value['json_pointer'].split('/')[1:]:
    token=token.replace('~1','/').replace('~0','~'); obj=obj[int(token)] if isinstance(obj,list) else obj[token]
   canon=json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
   assert hashlib.sha256(canon).hexdigest()==value['canonical_sha256'],value['json_pointer']
   assert json.loads(member)==obj
   refs.append({'binding_id':value['binding_id'],'pointer':value['json_pointer'],'input_sha256':value['input_sha256'],'raw_span':[a,b],'raw_sha256':value['raw_member_sha256'],'canonical_sha256':value['canonical_sha256']})
  for v in value.values(): walk(v)
 elif isinstance(value,list):
  for v in value: walk(v)
walk(contract)
for i in [20,22]: walk(norm['records'][i]['groups'])
bindings=json.loads((C/'evidence/tasks/R7-C13/raw-binding-manifest.json').read_bytes())
for b in sorted({r['binding_id'] for r in refs}):
 rows=[r for r in bindings if r['binding_id']==b]; assert len(rows)==1
 row=rows[0]; d=raw_path(row['sha256']).read_bytes(); a=ident(d)
 assert a['bytes']==row['bytes'] and a['sha256']==row['sha256'] and a['git_blob_content_id']==row['content_git_blob']
# Deliberately small inert reader, restricted to token kinds in this fixed archive.
archive=(C/'inputs/reference/Data/Scripts.rxdata').read_bytes(); pos=2; symbols=[]
assert archive[:2]==bytes([4,8])
def integer():
 global pos
 c=int.from_bytes(archive[pos:pos+1],'little',signed=True);pos+=1
 if c==0:return 0
 if c>4:return c-5
 if c< -4:return c+5
 n=abs(c); v=int.from_bytes(archive[pos:pos+n],'little',signed=c<0);pos+=n
 if c<0 and v>=0:v-=1<<(8*n)
 return v
def token():
 global pos
 t=chr(archive[pos]);pos+=1
 if t=='[': return [token() for _ in range(integer())]
 if t=='i': return integer()
 if t=='"':
  n=integer();d=archive[pos:pos+n];pos+=n;return d
 if t==':':
  n=integer();d=archive[pos:pos+n];pos+=n;symbols.append(d);return d
 if t==';':return symbols[integer()]
 if t=='T':return True
 if t=='I':
  obj=token();n=integer()
  for _ in range(n):token();token()
  return obj
 raise ValueError(('unsupported inert token',t,pos-1))
a=token();assert pos==len(archive)==594 and len(a)==1 and len(a[0])==3 and a[0][1]==b'Main'
compressed=a[0][2];assert compressed==archive[29:590]
z=zlib.decompressobj(); decoded=z.decompress(compressed,65537);decoded+=z.flush();assert z.eof and not z.unused_data and len(decoded)<65536
loader=decoded.decode();assert len(loader.splitlines())==49 and loader.rstrip().endswith('load_scripts_from_folder("Data/Scripts")')
archive_result={'stage':'TOOL_VALIDATION','bytes_consumed':pos,'records':1,'title':'Main','compressed_span':[29,590],'compressed':ident(compressed),'decoded':ident(decoded),'decoded_lines':49,'final_discovery_invocation_present':True,'Ruby_eval_reference_host_execution':'NOT_EXECUTED'}
exe=C/'inputs/reference/extendtext.exe'
args=['objdump','-d','-M','intel','--start-address=0x40129c','--stop-address=0x4016cc',str(exe)]
p=subprocess.run(args,capture_output=True,check=True); dis=p.stdout.decode(); assert not p.stderr
ins=[]
for line in dis.splitlines():
 m=re.match(r'\s*([0-9a-f]+):\s+(?:[0-9a-f]{2}\s+)+\s*([a-z]+)\s*(.*)',line)
 if m:ins.append((int(m[1],16),m[2],m[3]))
requests=[]
for i,(addr,op,arg) in enumerate(ins):
 if op=='call' and arg=='0x401684':
  pushes=[arg for _,op,arg in ins[:i] if op=='push'][-7:]
  flags=int(pushes[0],16)
  if flags==0x16: requests.append({'address':hex(addr),'kind':'size','width':int(pushes[2],16),'height':int(pushes[1],16),'position_z_activation':'PRESERVED_REQUEST'})
  else:
   assert flags==0x15
   requests.append({'address':hex(addr),'kind':'position','x':int(pushes[4],16),'y':int(pushes[3],16),'size_z_activation':'PRESERVED_REQUEST'})
expected=[(840,240),(800,176),(840,144),(800,72),(840,164),(800,92),(840,444),(800,372)]
assert [(r['width'],r['height']) for r in requests if r['kind']=='size']==expected
assert [(r['x'],r['y']) for r in requests if r['kind']=='position']==[(25,392),(150,392)]
b=exe.read_bytes(); strings={}
for off in [0x94,0xa5,0xad,0xb7,0xbc,0xc3,0x100,0x10d]:
 a=3072+off;strings[hex(0x402000+off)]=b[a:b.index(b'\0',a)].decode()
assert set(strings.values())=={'Batch Text Entry','Comment','Show Text','EDIT','Script','#32770','RPG Maker XP','Afx:'}
entry=subprocess.run(['objdump','-d','-M','intel','--start-address=0x401219','--stop-address=0x401294',str(exe)],capture_output=True,check=True)
assert 'call   0x4013c2' in entry.stdout.decode()
imports=subprocess.run(['objdump','-p',str(exe)],capture_output=True,check=True)
assert all(n in imports.stdout.decode() for n in ['strstr','SetWindowPos','CreateMutexA','GetLastError','Sleep','EnumWindows','FindWindowA','FindWindowExA','GetDlgItem'])
static={'stage':'SOURCE_STATIC','exe':ident(b),'business_and_trampolines_span':[1692,2764],'data_span':[3072,3348],'entry_span':[1561,1684],'strings':strings,'request_sites':requests,'entry_calls_business':True,'manual_control_flow_findings':{'targets':'four independent branches, no ownership filter','missing_EDIT':'outer already requested, next branch reachable','missing_batch_buttons':'each independent, reachable without EDIT','false_API_result':'not tested before next request','mutex':'existing 183 maps 0; creation failure maps -1; business stops only on 0','exit':'next marker check after Sleep150, valid handle close only, no restore'},'reference_native_API_execution':'NOT_EXECUTED','raw_disassembly_publication':'not copied; public evidence contains bounded facts and identities only','objdump_commands':[args,['objdump','-d','-M','intel','--start-address=0x401219','--stop-address=0x401294',str(exe)],['objdump','-p',str(exe)]],'objdump_exit_codes':[p.returncode,entry.returncode,imports.returncode]}
result={'schema':'r7.u11.input-audit.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'fixed_restored_files':files,'raw_binding_checks':refs,'archive':archive_result,'native_static':static,'qualification':'Identities and bounded decoding only. Manual control-flow interpretation is author SOURCE_STATIC, not independent review; no native/reference/model/host behavior executed.'}
(E/'input-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'INPUT_IDENTITIES_AND_STATIC_DECODING_VERIFIED','files':len(files),'raw_binding_checks':len(refs),'archive_bytes':pos,'decoded_lines':49,'native_request_sites':requests,'execution':{'reference':0,'native':0,'API':0,'independent_behavior_model':0,'host':0,'Demo':0,'real_save_replay':0}},ensure_ascii=False,indent=2))
