"""Data-only exact-byte checks of the finite, actually-read Game evidence.

This does not execute Game, shaders, font bytecode, controller bindings or audio.
It checks provenance and preserves static fields for semantic review separately.
"""
from pathlib import Path
import hashlib, json, re, struct, subprocess, datetime

OUT = Path(__file__).resolve().parent
BASE = OUT.parent.parent
INP = BASE / 'tasks/binary_remaining_texts'
GAME = Path('/workspace/pokemon-essentials/Game.exe')
b = GAME.read_bytes()
assert b == subprocess.run(['git','-C','/workspace/pokemon-essentials','show',
    '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:Game.exe'],capture_output=True,check=True).stdout
pe = struct.unpack_from('<I', b, 0x3c)[0]
assert b[pe:pe+4] == b'PE\0\0'
n = struct.unpack_from('<H', b, pe+6)[0]
osize = struct.unpack_from('<H', b, pe+20)[0]
opt = pe+24
imagebase = struct.unpack_from('<Q', b, opt+24)[0]
sections=[]
for i in range(n):
    p=opt+osize+40*i
    name=b[p:p+8].rstrip(b'\0').decode()
    vs,rva,rs,off=struct.unpack_from('<IIII',b,p+8)
    sections.append({'name':name,'rva':rva,'virtual_size':vs,'raw_size':rs,'offset':off})
def fileoff(va):
    rva=va-imagebase
    for s in sections:
        if s['rva']<=rva<s['rva']+s['raw_size']:
            return s['offset']+rva-s['rva']
    raise ValueError(hex(va))
def sha(d): return hashlib.sha256(d).hexdigest()
def cstr(va):
    p=fileoff(va); z=b.index(0,p); return b[p:z].decode('ascii')

extension=json.loads((BASE/'delegation/readsets/resource_media_serialized_cloud.extension.json').read_text())
units=[]
for u in extension['new_program_and_data_units_full']:
    if 'start' not in u: continue
    d=b[u['start']:u['end_exclusive']]
    assert len(d)==u['bytes'] and sha(d)==u['sha256']
    units.append({'id':u['id'],'span':[u['start'],u['end_exclusive']], 'bytes':len(d), 'sha256':sha(d)})

natives=[]
for name in ['209072','3823040','6817536','7396800','3879264','3874736','3874224','3873328','3984304','3984576','3447632']:
    p=INP/('native-'+name+'.stdout'); lines=p.read_text().splitlines()
    if name=='3447632': lines=lines[1309:1342]
    count=0;spans=[]
    for line in lines:
        m=re.match(r'\s*([0-9a-f]+):\s*([0-9a-f]{2}(?: [0-9a-f]{2})*)\s+\S',line)
        if not m: continue
        va=int(m[1],16);d=bytes.fromhex(m[2]);off=fileoff(va)
        assert b[off:off+len(d)]==d,(name,hex(va))
        spans.append([va,va+len(d),off]);count+=1
    natives.append({'evidence':str(p.relative_to(BASE)), 'read_lines':[1310,1342] if name=='3447632' else [1,len(lines)],'instruction_rows':count,'all_instruction_bytes_match':True,'first_va':hex(spans[0][0]),'end_va':hex(spans[-1][1]),'qualification':'exact read window only' if name=='3447632' else 'complete supplied function read; downstream callees not inherited'})

font_size=struct.unpack_from('<I',b,fileoff(0x1409bff94))[0]
font_bytes_at=fileoff(0x1409bffa0)
assert font_size==350200 and font_bytes_at==10217888
assert sha(b[font_bytes_at:font_bytes_at+font_size])==units[0]['sha256']
font_tables={}
for source in [GAME]+sorted(Path('/workspace/pokemon-essentials/Fonts').glob('*.ttf')):
    raw=b[10217888:10568088] if source==GAME else source.read_bytes()
    cnt=struct.unpack_from('>H',raw,4)[0];ts={}
    for j in range(cnt):
        tag,check,off,size=struct.unpack_from('>4sIII',raw,12+16*j)
        ts[tag.decode()]=raw[off:off+size]
    font_tables[str(source)]=ts
embedded=font_tables[str(GAME)]
font_comparisons=[{'path':s,'whole_equal':Path(s).read_bytes()==b[10217888:10568088],
  'equal_whole_corresponding_tables':[tag for tag,d in ts.items() if tag in embedded and d==embedded[tag]]}
  for s,ts in font_tables.items() if s!=str(GAME)]

programs=[]
for name,field in [('compiled-shader-token-programs.json','instructions'),('compiled-shader-aon9-programs.json','instructions')]:
    xs=json.loads((INP/name).read_text())
    for c in xs:
        for ins in c[field]:
            raw=b''.join(struct.pack('<I',int(v,16)) for v in ins['raw_tokens'])
            assert b[ins['offset']:ins['offset']+len(raw)]==raw
    programs.append({'file':name,'containers':len(xs),'instructions':sum(len(c[field]) for c in xs),'all_raw_instruction_tokens_match_original_Game':True})
pixel_pairs=[]
p=fileoff(0x140b1afe0)
for i in range(11):
    va,size=struct.unpack_from('<QQ',b,p+16*i);off=fileoff(va)
    pixel_pairs.append({'index':i,'start':off,'size':size,'sha256':sha(b[off:off+size])})
    u=next(u for u in units if u['span'][0]==off)
    assert u['bytes']==size
controller=json.loads((INP/'builtin-controller-readset.json').read_text())
for r in controller['records']:
    raw=b[r['start']:r['end']]
    assert raw.decode()==r['raw_text'] and sha(raw)==r['sha256'] and b[r['end']]==0
    fields=r['raw_text'].split(',')
    assert fields[:2]==[r['guid'],r['name']]
    parsed=[f.split(':',1) for f in fields[2:] if f]
    assert parsed==r['ordered_fields']
    if r['pointer_slot'] is not None:
        assert fileoff(struct.unpack_from('<Q',b,r['pointer_slot'])[0])==r['start']
for pat in controller['patterns']:
    assert all(controller['records'][i]['ordered_fields']==pat['ordered_fields'] for i in pat['records'])
assert sorted(i for pat in controller['patterns'] for i in pat['records'])==list(range(257))
assert sorted(i for q in controller['names'] for i in q['records'])==list(range(257))
assert struct.unpack_from('<Q',b,controller['pointer_table_end_with_null']-8)[0]==0
report={'schema':'gr8-media-independent-static-verification/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
  'Game':{'bytes':len(b),'sha256':sha(b),'git_blob':subprocess.check_output(['git','hash-object',str(GAME)],text=True).strip()},
  'sections':sections,'units':units,'native_evidence':natives,
  'font_literal_global':{'size_va':'0x1409bff94','data_va':'0x1409bffa0','size':font_size,'offset':font_bytes_at},
  'original8_font_comparisons':font_comparisons,'shader_token_checks':programs,'pixel_pointer_size_pairs':pixel_pairs,
  'controller_record_checks':{'all257_raw_text_fields_pointers_match':True,'all119_patterns_cover_exactly257':True,'all209_names_cover_exactly257':True,'null_pointer_terminator':True},
  'native_strings':{hex(va):cstr(va) for va in [0x140b05ab9,0x140b05ada,0x140b058d2,0x140b058da,0x140b058e1,0x140b05828,0x140b05848,0x140b057e0,0x140b05808,0x140b1af38,0x140b1af68,0x140b1af98]},
  'business_execution':'NOT_EXECUTED','update_started':False}
(OUT/'static-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
