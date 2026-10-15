"""Decode bounded PE data for independent static review; never load/execute it."""
import datetime,hashlib,json,pathlib,struct,subprocess,os
out=pathlib.Path(__file__).resolve().parents[1]
p=pathlib.Path('/workspace/r7-context/R7-U02-reviewer/inputs/reference/Game.exe');d=p.read_bytes()
pe=struct.unpack_from('<I',d,0x3c)[0];assert d[pe:pe+4]==b'PE\0\0'
n=struct.unpack_from('<H',d,pe+6)[0];opt=struct.unpack_from('<H',d,pe+20)[0];base=struct.unpack_from('<Q',d,pe+24+24)[0]
sections=[]
for i in range(n):
 a=pe+24+opt+40*i; name=d[a:a+8].rstrip(b'\0').decode();vs,rva,sz,off=struct.unpack_from('<IIII',d,a+8);sections.append({'name':name,'rva':rva,'virtual_size':vs,'raw_size':sz,'raw_offset':off})
def offset(va):
 for s in sections:
  if s['rva']<=va-base<s['rva']+s['raw_size']: return s['raw_offset']+va-base-s['rva']
 raise ValueError(hex(va))
def va(off):
 for s in sections:
  if s['raw_offset']<=off<s['raw_offset']+s['raw_size']: return base+s['rva']+off-s['raw_offset']
 raise ValueError(off)
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def cstring(off):return d[off:d.index(b'\0',off)]
tables={}
for kind,start,count in [('buttons',11552288,15),('axes',11552480,6)]:
 rows=[]
 for i in range(count+1):
  ptr=struct.unpack_from('<Q',d,start+8*i)[0]
  if i==count:assert ptr==0;break
  off=offset(ptr);b=cstring(off);rows.append({'index':i,'pointer_slot':start+8*i,'va':hex(ptr),'file_offset':off,'name':b.decode(),**identity(b+b'\0')})
 tables[kind]=rows
assert [x['name'] for x in tables['buttons']]==['a','b','x','y','back','guide','start','leftstick','rightstick','leftshoulder','rightshoulder','dpup','dpdown','dpleft','dpright']
assert [x['name'] for x in tables['axes']]==['leftx','lefty','rightx','righty','lefttrigger','righttrigger']
record=d[9797195:9797501].decode();fields=record.strip('\0\r\n').split(',');sample=[x for x in fields if x.split(':')[0] in ['a','misc1','rightshoulder']]
assert sample==['a:b0','misc1:b9','rightshoulder:b5'];assert 'misc1' not in [x['name'] for v in tables.values() for x in v]
ranges=[]
for a,b in [(9797195,9797501),(9797388,9797396),(11552288,11552416),(11552480,11552536),(3873328,3874736),(11551200,11551232),(11551187,11551195),(11552166,11552264),(11552416,11552461)]: ranges.append({'byte_range':[a,b],'va_range':[hex(va(a)),hex(va(b-1)+1)],**identity(d[a:b])})
argv=['objdump','-d','-M','intel','--start-address=0x1403b2630','--stop-address=0x1403b2bb0',str(p)]
t=datetime.datetime.now(datetime.timezone.utc).isoformat();proc=subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE);dis,err=proc.communicate();assert proc.returncode==0
private=pathlib.Path('/workspace/r7-review-bootstrap/R7-U02-r1');(private/'independent-parser-disassembly.txt').write_bytes(dis)
result={'utc':t,'pid':os.getpid(),'binary':str(p),'binary_identity':identity(d),'image_base':hex(base),'sections':sections,'tables':tables,'record_sample_fields_in_order':sample,'record_range':ranges[0],'ranges':ranges,'error_string':cstring(11551200).decode(),'disassembler':{'argv':argv,'pid':proc.pid,'exit_code':proc.returncode,'stdout_identity':identity(dis),'stderr':err.decode(),'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'publication_qualification':'Source machine-code output kept as local read input; public output is locator/identity only, never a model stream.'},'execution':'NATIVE_NOT_EXECUTED; objdump is a static decoder','semantic_qualification':'Name identities/branch content interpreted separately in report; this tool does not certify semantic acceptance.'}
(out/'binary-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'BOUNDED_PE_DATA_VERIFIED','buttons':[x['name'] for x in tables['buttons']],'axes':[x['name'] for x in tables['axes']],'fields':sample,'ranges':ranges,'error_string':result['error_string'],'native_executions':0},ensure_ascii=False,indent=2))
