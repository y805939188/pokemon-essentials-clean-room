"""Decode .text bytes for finite candidate type evidence; never execute input."""
from pathlib import Path
import collections, datetime, gzip, hashlib, json, re, subprocess
O=Path(__file__).resolve().parent
meta=json.loads((O/'pe-metadata.json').read_text())['files']
sha=lambda b:hashlib.sha256(b).hexdigest()
utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
out=[]
for f in meta:
 name=f['path'];b=Path('/workspace/pokemon-essentials',name).read_bytes();assert sha(b)==f['sha256']
 cmd=['objdump','-d','-w','-j','.text','/workspace/pokemon-essentials/'+name]
 start=utc();r=subprocess.run(cmd,capture_output=True);end=utc()
 (O/(name+'.objdump.stdout.gz')).write_bytes(gzip.compress(r.stdout,mtime=0))
 (O/(name+'.objdump.stderr')).write_bytes(r.stderr)
 sec=next(s for s in f['meta']['sections']if s['name']=='.text');bias=f['meta']['image_base']+sec['rva']-sec['offset'];inst=[];targets=collections.defaultdict(list)
 for ln,line in enumerate(r.stdout.decode('utf8','replace').splitlines(),1):
  m=re.match(r'^\s*([0-9a-f]+):\s*((?:[0-9a-f]{2} )+)\s*(.*)$',line)
  if not m:continue
  a=int(m[1],16)-bias;raw=bytes.fromhex(m[2]);assert b[a:a+len(raw)]==raw
  ins=dict(start=a,end_exclusive=a+len(raw),assembly=m[3],stdout_line=ln)
  inst.append(ins)
  for q in re.finditer(r'#\s+([0-9a-f]{8,16})',m[3]):
   va=int(q[1],16);rva=va-f['meta']['image_base']
   for s in f['meta']['sections']:
    if s['size'] and s['rva']<=rva<s['rva']+s['size']:
     at=s['offset']+rva-s['rva'];targets[at].append(dict(instruction_offset=a,stdout_line=ln,assembly=m[3]));break
 with gzip.open(O/(name+'.instructions.jsonl.gz'),'wt')as h:
  for ins in inst:h.write(json.dumps(ins,separators=(',',':'))+'\n')
 with gzip.open(O/(name+'.rip-targets.json.gz'),'wt')as h:json.dump(targets,h,separators=(',',':'))
 receipt=dict(path=name,command=cmd,start_utc=start,end_utc=end,exit=r.returncode,stdout_bytes=len(r.stdout),stdout_sha256=sha(r.stdout),stderr_bytes=len(r.stderr),stderr_sha256=sha(r.stderr),instructions=len(inst),kind='TOOL_VALIDATION',qualification='Linear disassembly is type/location evidence. It does not prove executable reachability, native CFG, message composition or library selection. Managed CIL in animmaker is not interpreted as native code.')
 out.append(receipt);print(json.dumps(receipt))
(O/'disassembly-execution.json').write_text(json.dumps(out,indent=2)+'\n')
