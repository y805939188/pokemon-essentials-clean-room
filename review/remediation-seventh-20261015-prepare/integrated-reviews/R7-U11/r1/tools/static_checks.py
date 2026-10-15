import json,hashlib,zlib,subprocess,struct
from pathlib import Path
ROOT=Path('/workspace/r7-ir-R7-U11'); OUT=Path(__file__).resolve().parents[1]
def ident(b): return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def save(n,x): (OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
# Strict inert decoder: only the array/int/string/encoding tokens actually allowed here.
b=(ROOT/'original/inputs/reference/Data/Scripts.rxdata').read_bytes(); pos=2; symbols=[]; tokens=[]
assert b[:2]==b'\x04\x08'
def integer():
 global pos
 c=struct.unpack('b',b[pos:pos+1])[0];pos+=1
 if c==0:return 0
 if c>4:return c-5
 if c< -4:return c+5
 n=abs(c);v=int.from_bytes(b[pos:pos+n],'little',signed=False);pos+=n
 return v if c>0 else v-(1<<(8*n))
def token():
 global pos
 start=pos;t=b[pos:pos+1];pos+=1
 if t==b'[': v=[token() for _ in range(integer())]
 elif t==b'i':v=integer()
 elif t in [b'"',b':']:
  n=integer();assert 0<=n<=1024;v=b[pos:pos+n];pos+=n
  if t==b':':symbols.append(v)
 elif t==b';':v=symbols[integer()]
 elif t==b'T':v=True
 elif t==b'I':
  v=token();n=integer();assert n==1
  assert token()==b'E' and token() is True
 else:raise ValueError((start,t))
 tokens.append({'offset':start,'end':pos,'tag':t.decode()});assert len(tokens)<=32
 return v
obj=token();assert pos==len(b) and len(obj)==1 and len(obj[0])==3 and obj[0][0]==62054200 and obj[0][1]==b'Main'
compressed=obj[0][2];assert compressed==b[29:590]
d=zlib.decompressobj();text=d.decompress(compressed,8193);assert len(text)<=8192 and d.eof and not d.unused_data
save('archive-static-audit.json',{'archive':ident(b),'tokens':tokens,'bytes_consumed':pos,'records':1,'record_title':'Main','compressed_interval':[29,590],'compressed_identity':ident(compressed),'decoded_identity':ident(text),'decoded_lines':len(text.splitlines()),'source_execution':'NOT_EXECUTED','parser':'Restricted inert tokens and bounded zlib; no Marshal runtime/object construction or eval','independent_content_read':'49 decoded lines read; sorted root files before sorted visible folders, rb suffix insensitive; open/read before local evaluation rescue; ScriptError distinct; ordinary message threshold 900; final discovery invocation','no_behavior_model_execution':True})
exe=ROOT/'original/inputs/reference/extendtext.exe'
def objdump(*args):return subprocess.check_output(['objdump',*args,str(exe)]).decode()
dis=objdump('-d','-j','.text','-Mintel','--start-address=0x401219','--stop-address=0x4016cc')
imports=objdump('-p');data=exe.read_bytes()
requests=[(0x401415,'Script','outer',[840,240],0x16),(0x401449,'Script','first_EDIT',[800,176],0x16),(0x40147b,'Show Text','outer',[840,144],0x16),(0x4014ac,'Show Text','first_EDIT',[800,72],0x16),(0x4014de,'Comment','outer',[840,164],0x16),(0x40150f,'Comment','first_EDIT',[800,92],0x16),(0x40155f,'Batch Text Entry','outer',[840,444],0x16),(0x401593,'Batch Text Entry','first_EDIT',[800,372],0x16),(0x4015b0,'Batch Text Entry','button_1_position',[25,392],0x15),(0x4015d0,'Batch Text Entry','button_2_position',[150,392],0x15)]
for address,*_ in requests:assert f'{address:x}:' in dis and 'call' in next(l for l in dis.splitlines() if f'{address:x}:' in l)
for name in ['SetWindowPos','FindWindowA','FindWindowExA','EnumWindows','CreateMutexA','GetLastError','CloseHandle','Sleep','strstr']:assert name in imports
assert 'GetWindowThreadProcessId' not in imports
save('native-static-audit.json',{'identity':ident(data),'business_interval_file':[1692,2764],'data_interval_file':[3072,3348],'entry_interval_file':[1561,1684],'imports_verified':True,'code_and_data_read_in_this_context':True,'requests':[{'call_va':hex(a),'title':t,'target':target,'dimensions_or_position':v,'flags':hex(f)} for a,t,target,v,f in requests],'marker':'case-sensitive strstr for Afx: class, then RPG Maker XP title; separate from exact #32770 target lookup','independent_paths':'missing outer skips only that target; missing EDIT skips child only; buttons independently retained before edit lookup; all SetWindowPos returns unchecked','mutex':'helper duplicate closes handle and returns 0; failed create returns -1; caller tests only 0; close helper excludes both 0 and -1','loop':'initial marker check before targets; target loop then Sleep(150), marker recheck; exit closes valid mutex, no geometry restore','reference_execution':'NOT_EXECUTED','qualification':'Manual source/control-flow read plus identity/tool checks. No host, API geometry, startup remainder, ownership, localization or timing certification.'})
print(json.dumps({'archive_bytes_consumed':pos,'decoded_bytes':len(text),'decoded_lines':len(text.splitlines()),'native_request_points':len(requests),'reference_program_runs':0}))
