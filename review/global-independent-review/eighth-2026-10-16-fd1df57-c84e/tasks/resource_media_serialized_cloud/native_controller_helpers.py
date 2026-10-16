"""Recover only five complete PE runtime-function spans; static objdump, no target execution."""
import datetime,hashlib,json,pathlib,re,struct,subprocess
OUT=pathlib.Path(__file__).resolve().parent/'native-controller-followup-002'
OUT.mkdir(exist_ok=True)
source=pathlib.Path('/workspace/pokemon-essentials/Game.exe');data=source.read_bytes()
assert len(data)==14732288 and hashlib.sha256(data).hexdigest()=='5c75e92fcbb6ec50b9f8fc61913d751a8945d6a1fc69c3017c7b8686b532bf04'
u16=lambda p:struct.unpack_from('<H',data,p)[0]
u32=lambda p:struct.unpack_from('<I',data,p)[0]
pe=u32(60);optional=pe+24;section_start=optional+u16(pe+20)
image_base=struct.unpack_from('<Q',data,optional+24)[0]
sections=[]
for i in range(u16(pe+6)):
 off=section_start+40*i;vs,rva,rs,fo=struct.unpack_from('<IIII',data,off+8)
 sections.append({'name':data[off:off+8].split(b'\0')[0].decode(),'rva':rva,'vsize':vs,'file':fo,'rawsize':rs})
def fileoff(rva):
 s=next(s for s in sections if s['rva']<=rva<s['rva']+s['rawsize'])
 return rva-s['rva']+s['file']
pdata=next(s for s in sections if s['name']=='.pdata')
functions=[struct.unpack_from('<III',data,p) for p in range(pdata['file'],pdata['file']+pdata['rawsize']-11,12)]
results=[]
for target in [0x4236a0,0x3b0d70,0x3b0da0,0x3b0dc0]:
 matches=[r for r in functions if r[0]<=target<r[1]];assert len(matches)==1
 start,end,unwind=matches[0];assert start==target
 argv=['objdump','-d','--insn-width=16','--start-address='+hex(image_base+start),'--stop-address='+hex(image_base+end),str(source)]
 began=datetime.datetime.now(datetime.timezone.utc).isoformat();run=subprocess.run(argv,capture_output=True);ended=datetime.datetime.now(datetime.timezone.utc).isoformat()
 stem=hex(target)[2:];(OUT/(stem+'.stdout')).write_bytes(run.stdout);(OUT/(stem+'.stderr')).write_bytes(run.stderr)
 assert run.returncode==0
 rows=[]
 for line in run.stdout.decode().splitlines():
  m=re.match(r'\s*([0-9a-f]+):\s+((?:[0-9a-f]{2} ?)+)\s*\t(.*)',line)
  if not m:continue
  va=int(m.group(1),16);raw=bytes.fromhex(m.group(2));offset=fileoff(va-image_base)
  assert data[offset:offset+len(raw)]==raw
  rows.append({'va':hex(va),'bytes':raw.hex(),'mnemonic':m.group(3)})
 assert rows and int(rows[0]['va'],16)==image_base+start
 assert int(rows[-1]['va'],16)+len(bytes.fromhex(rows[-1]['bytes']))==image_base+end
 span=[fileoff(start),fileoff(end-1)+1]
 result={'function_rva':hex(start),'end_rva_exclusive':hex(end),'unwind_rva':hex(unwind),'span':span,'source_bytes':end-start,'source_sha256':hashlib.sha256(data[span[0]:span[1]]).hexdigest(),'argv':argv,'started_utc':began,'ended_utc':ended,'exit':run.returncode,'instruction_rows':len(rows),'stdout_lines':len(run.stdout.splitlines()),'all_original_instruction_bytes_match':True,'actual_semantic_reading_credit':0,'business':'NOT_EXECUTED'}
 (OUT/(stem+'.execution.json')).write_text(json.dumps(result,indent=2)+'\n');(OUT/(stem+'.instructions.json')).write_text(json.dumps(rows,indent=2)+'\n');results.append(result)
(OUT/'recovery.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
