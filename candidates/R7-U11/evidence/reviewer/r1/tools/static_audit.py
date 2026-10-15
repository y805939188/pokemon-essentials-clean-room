"""Inert archive parsing and bounded native parameter inspection; no behavior runs."""
import datetime,hashlib,json,pathlib,re,subprocess,struct,zlib
out=pathlib.Path(__file__).resolve().parents[1];ref=pathlib.Path('/workspace/r7-context/R7-U11-reviewer/inputs/reference');private=pathlib.Path('/workspace/r7-review-logs')
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def save(name,d):(out/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
class InertMarshal:
 def __init__(self,b):self.b=b;self.p=0;self.symbols=[];self.spans=[]
 def take(self,n):
  assert n>=0 and self.p+n<=len(self.b);a=self.p;self.p+=n;return self.b[a:self.p]
 def integer(self):
  v=int.from_bytes(self.take(1),'little',signed=True)
  if v==0:return 0
  if v>4:return v-5
  if v<-4:return v+5
  n=abs(v);r=int.from_bytes(self.take(n),'little');return r if v>0 else r-(1<<(8*n))
 def value(self,depth=0):
  assert depth<15;t=self.take(1)
  if t==b'[':
   n=self.integer();assert 0<=n<=10;return [self.value(depth+1) for _ in range(n)]
  if t==b'i':return self.integer()
  if t==b'"':
   n=self.integer();a=self.p;s=self.take(n);self.spans.append([a,self.p]);return s
  if t==b':':
   n=self.integer();s=self.take(n);self.symbols.append(s);return ('symbol',s)
  if t==b';':return ('symbol',self.symbols[self.integer()])
  if t==b'T':return True
  if t==b'F':return False
  if t==b'I':
   v=self.value(depth+1);n=self.integer();assert n==1;assert self.value(depth+1)==('symbol',b'E');assert self.value(depth+1) is True;return v
  raise ValueError('Disallowed inert token '+repr(t))
b=(ref/'Data/Scripts.rxdata').read_bytes();p=InertMarshal(b);assert p.take(2)==b'\x04\x08';v=p.value();assert p.p==len(b)==594;assert len(v)==1 and len(v[0])==3 and v[0][1]==b'Main';assert p.spans==[[15,19],[29,590]]
z=zlib.decompressobj();text=z.decompress(v[0][2],10001);assert len(text)<=10000 and z.eof and not z.unused_data and not z.unconsumed_tail;assert len(text.splitlines())==49
(private/'decoded-Main.txt').write_bytes(text)
archive={'archive_identity':ident(b),'bytes_consumed':p.p,'record_count':len(v),'title':'Main','compressed_span':[29,590],'decoded_identity':ident(text),'decoded_lines':49,'inert_tokens_only':True,'reference_Ruby_eval_execution':0,'manual_semantic_ranges':['decoded Main 1-49','scripts_extract.rb 1-183','scripts_combine.rb 1-183','loose Main 1-60'],'facts':['Conditional unencrypted entry has final discovery request','root files sorted before sorted visible-directory recursion','dot rb files allowed; dot directories skipped','open/read precedes eval protection','script-error family separated from ordinary-error and 900-message branch','prefix side effects have no whole-load rollback'],'qualification':'TOOL_VALIDATION structure plus separately reviewed SOURCE_STATIC; no object deserialization or reference execution'}
# Separate aligned callback decode avoids the preceding padding byte.
cmds=[['objdump','-p',str(ref/'extendtext.exe')],['objdump','-d','-Mintel','--start-address=0x40129c','--stop-address=0x4016cd',str(ref/'extendtext.exe')],['objdump','-d','-Mintel','--start-address=0x401219','--stop-address=0x401294',str(ref/'extendtext.exe')]]
commands=[];outputs=[]
for i,cmd in enumerate(cmds):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE);stdout,stderr=proc.communicate();assert proc.returncode==0;outputs.append(stdout)
 (private/f'native-{i}.stdout').write_bytes(stdout);(private/f'native-{i}.stderr').write_bytes(stderr)
 commands.append({'argv':cmd,'subprocess_pid':proc.pid,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':proc.returncode,'stdout_identity':ident(stdout),'stderr_identity':ident(stderr),'public_output':'Derived facts only; full reference disassembly remains local, not republished'})
ins=[]
for line in outputs[1].decode().splitlines():
 m=re.match(r'\s*([0-9a-f]+):\s+(?:[0-9a-f]{2}\s+)+\s*([a-z].*)$',line)
 if m:ins.append((int(m.group(1),16),m.group(2).strip()))
calls=[]
for i,(addr,asm) in enumerate(ins):
 if asm=='call   0x401684':
  pushes=[x for a,x in ins[i-7:i]];assert len(pushes)==7 and all(s.startswith('push') for s in pushes)
  nums=[]
  for s in pushes[:6]:nums.append(int(s.split()[-1],0))
  flags,height,width,y,x,insert=nums;assert insert==0
  calls.append({'call_address':hex(addr),'request_values':{'x':x,'y':y,'width':width,'height':height,'flags':flags},'receiver':'present target/child handle, separately checked by control-flow review'})
expected=[(0,0,840,240,22),(0,0,800,176,22),(0,0,840,144,22),(0,0,800,72,22),(0,0,840,164,22),(0,0,800,92,22),(0,0,840,444,22),(0,0,800,372,22),(25,392,0,0,21),(150,392,0,0,21)]
assert [(r['request_values']['x'],r['request_values']['y'],r['request_values']['width'],r['request_values']['height'],r['request_values']['flags']) for r in calls]==expected
exe=(ref/'extendtext.exe').read_bytes()
assert exe[0xa84:0xa8a]==bytes.fromhex('ff2534314000')
assert exe[0xc94:0xca5].split(b'\0')[0]==b'Batch Text Entry';assert b'FindWindowA' in outputs[0] and b'SetWindowPos' in outputs[0]
labels=['Script outer','Script EDIT','Show Text outer','Show Text EDIT','Comment outer','Comment EDIT','Batch outer','Batch EDIT','Batch id1 position','Batch id2 position']
for r,label in zip(calls,labels):r['target']=label
native={'exe_identity':ident(exe),'commands':commands,'request_sites':calls,'source_ranges':{'callback_gate':['0x40129c','0x401351'],'mutex':['0x401352','0x4013e3'],'loop':['0x4013e8','0x4015ff'],'imports':['0x401600','0x4016cc'],'data_file_offsets':[3072,3348],'entry':['0x401219','0x401293']},'manual_control_flow_checks':['Afx: then RPG Maker XP substring gate; marker reset on each enumeration','duplicate returns0 stops; create failure -1 proceeds to gate and is not closed as valid handle','missing target branches to next lookup; missing EDIT skips child only','Batch buttons queried separately; each request guarded independently; no EDIT prerequisite','SetWindowPos returns unchecked; later calls remain reachable','Sleep150 then marker recheck; no restoration or business cancel','Interpreter diagnostic text does not launch tool'],'reference_native_API_host_execution':0,'qualification':'Inert objdump and parameter extraction are TOOL_VALIDATION; manual bounded control-flow reading is SOURCE_STATIC. All behavior vectors NOT_EXECUTED.'}
save('archive-static-audit.json',archive);save('native-static-audit.json',native)
print(json.dumps({'archive_bytes_consumed':p.p,'decoded_Main_lines':49,'native_request_sites':len(calls),'reference_execution':0,'behavior_vectors':'NOT_EXECUTED'}))
