"""Independent static disassembly and verified RIP edge inventory, no target execution."""
import pathlib,json,struct,subprocess,datetime,hashlib,re,gzip,bisect
P=pathlib.Path(__file__).resolve().parent;target=pathlib.Path('/workspace/pokemon-essentials/Game.exe');b=target.read_bytes();pe=json.loads((P/'pe-sections.json').read_text())['Game.exe'];base=pe['image_base']
def sha(v):return hashlib.sha256(v).hexdigest()
def fileoff(va):
 rva=va-base
 for s in pe['sections']:
  if s['rva']<=rva<s['rva']+s['bytes']:return s['offset']+rva-s['rva']
 return None
rawpath=P/'Game.independent.objdump.stdout'
assert not rawpath.exists() and not (P/'Game.independent.objdump.stdout.gz').exists()
cmd=['objdump','-d','-w',str(target)];start=datetime.datetime.now(datetime.timezone.utc).isoformat()
with rawpath.open('wb') as out:(r:=subprocess.run(cmd,stdout=out,stderr=subprocess.PIPE))
(P/'Game.independent.objdump.stderr').write_bytes(r.stderr)
execution={'command':cmd,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':r.returncode,'kind':'TOOL_VALIDATION_STATIC_DISASSEMBLER','business_execution_count':0};assert r.returncode==0
pd=next(s for s in pe['sections'] if s['name']=='.pdata');funcs=[]
for q in range(pd['offset'],pd['offset']+pd['virtual_size'],12):
 a,z,u=struct.unpack_from('<III',b,q);funcs.append((base+a,base+z,q))
starts=[r[0] for r in funcs];edges=[];rejected=[];linecount=0;instruction_count=0
pat=re.compile(r'^\s*([0-9a-f]+):\s*((?:[0-9a-f]{2}\s+)+)\s*(.*)$')
for linecount,line in enumerate(rawpath.open(),1):
 m=pat.match(line)
 if not m:continue
 va=int(m[1],16);raw=bytes.fromhex(m[2]);asm=m[3];o=fileoff(va);assert o is not None and b[o:o+len(raw)]==raw;instruction_count+=1
 if '(%rip)' not in asm:continue
 d=re.search(r'(-?0x[0-9a-f]+)\(%rip\)',asm);t=re.search(r'#\s*0x([0-9a-f]+)',asm)
 if not(d and t):rejected.append({'offset':o,'reason':'no numeric RIP target','assembly':asm});continue
 disp=int(d[1],16);tv=int(t[1],16);assert va+len(raw)+disp==tv and struct.pack('<i',disp) in raw,(o,asm)
 to=fileoff(tv)
 if to is None:continue
 k=bisect.bisect_right(starts,va)-1;fn=funcs[k] if k>=0 and va<funcs[k][1] else None
 edges.append({'instruction_offset':o,'instruction_end':o+len(raw),'instruction_sha256':sha(raw),'instruction_bytes_hex':raw.hex(),'target_offset':to,'assembly':asm,'stdout_line':linecount,'containing_pdata_function':{'start':fileoff(fn[0]),'end':fileoff(fn[1]-1)+1,'pdata_record_offset':fn[2]} if fn else None})
raw=rawpath.read_bytes();execution.update({'stdout_bytes':len(raw),'stdout_sha256':sha(raw),'stdout_lines':linecount,'verified_instructions':instruction_count,'verified_RIP_edges':len(edges),'uninterpreted_RIP_instructions':len(rejected)})
(P/'Game.independent.objdump.stdout.gz').write_bytes(gzip.compress(raw,mtime=0));rawpath.unlink();(P/'native-reference-execution.json').write_text(json.dumps(execution,indent=2)+'\n')
(P/'native-direct-reference-edges.jsonl.gz').write_bytes(gzip.compress(('\n'.join(json.dumps(r,separators=(',',':')) for r in edges)+'\n').encode(),mtime=0));(P/'native-reference-rejected.json').write_text(json.dumps(rejected,indent=2)+'\n');print(json.dumps(execution))
