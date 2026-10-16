"""Freeze current controller rows and finite string candidates for a new reader.

Reads pinned Git objects and current bytes only. No target image is loaded.
"""
from pathlib import Path
import collections, hashlib, json, re, subprocess
O=Path(__file__).resolve().parent
R=Path('/workspace/pokemon-essentials')
C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
D=O/'handoff';D.mkdir(exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
write=lambda p,v:p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def frozen(name):
 b=(R/name).read_bytes();g=subprocess.run(['git','-C',str(R),'show',C+':'+name],check=True,capture_output=True).stdout
 assert b==g,name
 return b

b=frozen('Game.exe');off=9774912;size=442647;raw=b[off:off+size]
assert sha(raw)=='8883f85acfad455feedca7a95203e18629d5c60fc3933d7f511eebd731089cfe'
assert raw==(O/'current-controller/raw.txt').read_bytes()
text=raw.decode('ascii');rows=[];pos=off;records=[];groups={}
for ln,linebytes in enumerate(raw.splitlines(keepends=True),1):
 line=linebytes.rstrip(b'\r\n').decode('ascii');row=dict(line=ln,start=pos,end_exclusive=pos+len(linebytes),raw_bytes=len(linebytes),sha256=sha(linebytes),text=line,reading_status='UNREAD_FOR_NEW_READER')
 pos+=len(linebytes)
 if not line or line.startswith('#'):row['kind']='comment_or_empty'
 else:
  fields=line.split(',');assert len(fields)>=3
  guid,name=fields[:2];assert re.fullmatch('[0-9a-fA-F]{32}',guid)or guid=='xinput'
  pairs=[]
  for f in fields[2:]:
   if not f:continue
   k,v=f.split(':',1);pairs.append([k,v])
  key=tuple(tuple(x)for x in pairs)
  if key not in groups:groups[key]=len(groups)
  rec=dict(line=ln,guid=guid,name=name,mapping=pairs,pattern_group=groups[key])
  records.append(rec);row.update(kind='mapping',record_index=len(records)-1,**rec)
 rows.append(row)
assert pos==off+size and len(rows)==1678 and len(records)==1666 and len(groups)==790
assert records==json.loads((O/'current-controller/records.json').read_text())
platforms=collections.Counter(v for x in records for k,v in x['mapping']if k=='platform')
write(D/'controller-readset.json',dict(source_commit=C,source_path='Game.exe',source_bytes=len(b),source_sha256=sha(b),offset=off,length=size,end_exclusive=off+size,region_sha256=sha(raw),decoder='Exact byte slice, strict ASCII; splitlines(keepends=True); strip CR/LF only; comma split; GUID/name first2 fields; remaining nonempty fields split once at colon, preserving order and duplicates; no API or SDL execution',record_count=len(records),line_count=len(rows),pattern_count=len(groups),platform_counts=dict(platforms),rows=rows,qualification='All records remain UNREAD semantic reception for a new reader; structural parsing and old record identities do not grant acceptance. Runtime selector, platform activation and physical input remain unknown.'))

known=json.loads((O/'current-programs-v2/inventory.json').read_text())
new=json.loads((O/'literal-discovery-reception.json').read_text())['rows']
false_ids={'PC-0027','PC-0030','PC-0031','PC-0064','PC-0065','PC-0066','PC-0067','PC-0714','PC-0715','PC-0716'}
summary=[]
for name in ['Game.exe','x64-msvcrt-ruby310.dll','zlib1.dll','animmaker.exe','extendtext.exe']:
 data=frozen(name);scount=collections.Counter();out=D/(name+'.strings.jsonl')
 with out.open('w')as f:
  for encoding,pat in [('ascii',rb'[\x20-\x7e]{4,}'),('utf-16-le-ascii-subset',rb'(?:[\x20-\x7e]\x00){4,}')]:
   for m in re.finditer(pat,data):
    rawstr=m.group();s=rawstr.decode('ascii'if encoding=='ascii'else'utf-16-le')
    k=[x for x in known if Path(x['path']).name==name and x['start']<=m.start()and m.end()<=x['end_exclusive']]
    n=[x for x in new if x['path']==name and x['start']<=m.start()and m.end()<=x['end_exclusive']]
    if k:
     cls='CONTAINED_IN_PREVIOUSLY_FULL_READ_UNIT';refs=[x['id']for x in k]
     if all(x['id']in false_ids for x in k):cls='CONTAINED_IN_PREVIOUSLY_READ_NONPROGRAM_UNIT'
    elif n:
     cls='CONTAINED_IN_NEWLY_READ_FINITE_SCAN_CANDIDATE';refs=[x['id']for x in n]
    else:cls='UNREAD_FINITE_STRING_CANDIDATE';refs=[]
    row=dict(path=name,encoding=encoding,start=m.start(),end_exclusive=m.end(),bytes=len(rawstr),sha256=sha(rawstr),text=s,classification=cls,previous_read_refs=refs,independent_acceptance='PENDING')
    f.write(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n');scount[encoding]+=1;scount[cls]+=1
 summary.append(dict(path=name,source_bytes=len(data),source_sha256=sha(data),inventory=str(out.relative_to(O)),inventory_bytes=out.stat().st_size,inventory_sha256=sha(out.read_bytes()),counts=dict(scount)))
oldpaths=['recovered-resource-evidence/tasks/R7-M17/binary_text.py','recovered-resource-evidence/tasks/R7-M17/controller-structure.json','recovered-resource-evidence/temporary/binary-tools/audit_binaries.py','recovered-resource-evidence/temporary/binary-tools/binary-interface-audit.json','recovered-resource-evidence/tasks/R7-D09/literal_candidates.py','recovered-resource-evidence/tasks/R7-D09/multiline-literal-inventory.json','recovered-resource-evidence/tasks/R7-D09/program-literal-candidates.json']
old=[dict(path=p,bytes=(O/p).stat().st_size,sha256=sha((O/p).read_bytes()),qualification='Historical navigation/decoder only, no inherited semantic credit. New worker must read a tool before executing/adapting it.')for p in oldpaths]
write(D/'readset-index.json',dict(source_commit=C,controller='handoff/controller-readset.json',current_raw_table='current-controller/raw.txt',current_parsed_table='current-controller/records.json',current_decoder='freeze_controller_string_readset.py',string_rules={'ascii':'[0x20–0x7e]{4,}, maximal regex runs, no LF or TAB','utf-16-le-ascii-subset':'(?:[0x20–0x7e] 0x00){4,}, maximal regex runs, any byte alignment'},strings=summary,previous_program_inventory='current-programs-v2/inventory.json',previous_exact_five_rule_inventory='current-literal-discovery.json',previous_exact_five_rule_reception='literal-discovery-reception.json',historical_navigation=old,actual_configuration={k:'UNVERIFIED'for k in ['model','effort','tier','speed','platform_session_id']},requested_configuration={'model':'gpt-6.1-sol','effort':'ultra','tier':'default普速','speed':'Fast off'},unread_qualifier='UNREAD finite string candidates and1666controller records are available readable inputs, not L04. Known extracted programs were fully read by proposer but require independent reception. Finite regex inventory does not prove all encodings, compressed programs or native CFG recovered.',consumer_denominator_pending=['mkxp.json configuration declarations (read, wiring unknown)','Game.exe SDL native table selection/activation unknown','B8 formal input/device/resource clauses: new worker must identify full relevant clause denominator, no proof of table-specific mandatory contract currently accepted','R current input consumers beyond this task named resource source set: readset not yet selected; new worker must locate and fully read actual callers'],opaque_boundary='Do not reverse-engineer unlimited machine CFG or guess arbitrary encoding. Existing indexed ASCII/UTF16 and metadata/resource materials are not opaque merely because unreceived.'))
print(json.dumps({'controller':{'offset':off,'length':size,'rows':len(rows),'records':len(records),'patterns':len(groups),'platforms':dict(platforms)},'strings':summary,'index':'handoff/readset-index.json'},ensure_ascii=False))
