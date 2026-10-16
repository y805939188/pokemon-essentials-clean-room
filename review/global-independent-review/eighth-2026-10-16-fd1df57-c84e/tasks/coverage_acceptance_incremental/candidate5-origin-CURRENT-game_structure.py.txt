"""Bounded binary structure evidence. Reads target bytes only; no target execution."""
import json,pathlib,struct,hashlib,gzip,datetime,collections
ROOT=pathlib.Path(__file__).resolve().parent;R=pathlib.Path('/workspace/pokemon-essentials');b=(R/'Game.exe').read_bytes()
def sha(x):return hashlib.sha256(x).hexdigest()
def dump(n,x): (ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def u16(p):return struct.unpack_from('>H',b,p)[0]
def i16(p):return struct.unpack_from('>h',b,p)[0]
def u32(p):return struct.unpack_from('>I',b,p)[0]
pe=json.loads((ROOT/'pe-sections.json').read_text())['Game.exe'];base=pe['image_base'];secs=pe['sections']
def rvaoff(v):
 for s in secs:
  if s['rva']<=v<s['rva']+s['bytes']:return s['offset']+v-s['rva']
 raise ValueError(hex(v))
def target(v):
 for s in secs:
  if s['rva']<=v-base<s['rva']+s['virtual_size']:return {'section':s['name'],'rva':v-base,'file_offset':s['offset']+v-base-s['rva'] if v-base-s['rva']<s['bytes'] else None}
 return None
h=struct.unpack_from('<I',b,60)[0];o=h+24
rv,sz=struct.unpack_from('<II',b,o+112+8*5);p=rvaoff(rv);end=p+sz;relocs=[]
while p<end:
 page,size=struct.unpack_from('<II',b,p);assert size>=8 and size%2==0 and p+size<=end
 for q in range(p+8,p+size,2):
  w=struct.unpack_from('<H',b,q)[0];ty=w>>12;v=page+(w&4095)
  if ty==10:
   z=rvaoff(v);val=struct.unpack_from('<Q',b,z)[0];t=target(val)
   relocs.append({'slot_offset':z,'slot_rva':v,'value':val,'reloc_record_offset':q,'target':t,'bytes_hex':b[z:z+8].hex()})
  else:assert ty==0,ty
 p+=size
assert p==end
dump('game-relocation-pointers.json',{'directory_rva':rv,'directory_offset':rvaoff(rv),'directory_bytes':sz,'dir64_count':len(relocs),'in_image_count':sum(r['target'] is not None for r in relocs),'entries':relocs})
fontbase=10217888;n=u16(fontbase+4);assert b[fontbase:fontbase+4]==b'\x00\x01\x00\x00'
tables={}
for j in range(n):
 p=fontbase+12+j*16;tag=b[p:p+4].decode('ascii');check,off,size=struct.unpack_from('>III',b,p+4);start=fontbase+off
 raw=b[start:start+size];padding=raw+b'\0'*((-len(raw))%4)
 if tag=='head':padding=padding[:8]+b'\0'*4+padding[12:]
 got=sum(struct.unpack('>'+'I'*(len(padding)//4),padding))&0xffffffff
 assert got==check,(tag,hex(got),hex(check))
 tables[tag]={'directory_offset':p,'start':start,'end':start+size,'bytes':size,'sha256':sha(raw),'declared_checksum':check,'computed_checksum':got}
fontend=max(t['end'] for t in tables.values());font=b[fontbase:fontend];(ROOT/'embedded-font.ttf').write_bytes(font)
glyphs=u16(tables['maxp']['start']+4);locfmt=i16(tables['head']['start']+50);metrics=u16(tables['hhea']['start']+34)
assert tables['loca']['bytes']==(glyphs+1)*(4 if locfmt else 2)
assert tables['hmtx']['bytes']==metrics*4+(glyphs-metrics)*2
loca=[(u32(tables['loca']['start']+4*i) if locfmt else 2*u16(tables['loca']['start']+2*i)) for i in range(glyphs+1)]
assert loca==sorted(loca) and loca[-1]<=tables['glyf']['bytes']
glyphrows=[]
for i,(a,z) in enumerate(zip(loca,loca[1:])):
 start=tables['glyf']['start']+a;end=tables['glyf']['start']+z
 row={'glyph':i,'start':start,'end':end,'sha256':sha(b[start:end])}
 if a<z:
  assert z-a>=10;row.update(contours=i16(start),bbox=[i16(start+q) for q in [2,4,6,8]])
 glyphrows.append(row)
names=[];nt=tables['name']['start'];fmt,count,so=struct.unpack_from('>HHH',b,nt);assert fmt==0
for i in range(count):
 p=nt+6+i*12;platform,encoding,lang,nameid,l,o=struct.unpack_from('>HHHHHH',b,p);s=nt+so+o;e=s+l
 assert nt<=s<=e<=tables['name']['end'];raw=b[s:e]
 codec='utf-16-be' if platform in (0,3) else 'mac_roman' if platform==1 else 'ascii'
 text=raw.decode(codec)
 names.append({'record':i,'platform':platform,'encoding':encoding,'language':lang,'name_id':nameid,'start':s,'end':e,'bytes':l,'sha256':sha(raw),'text':text})
cm=tables['cmap']['start'];cmaprows=[];maps=[]
for i in range(u16(cm+2)):
 p=cm+4+i*8;plat,enc,off=struct.unpack_from('>HHI',b,p);s=cm+off;f=u16(s);row={'platform':plat,'encoding':enc,'format':f,'start':s};m=[]
 if f==4:
  length=u16(s+2);seg=u16(s+6)//2;en=s+14;st=en+seg*2+2;delta=st+seg*2;rg=delta+seg*2
  for k in range(seg):
   for cp in range(u16(st+2*k),u16(en+2*k)+1):
    if cp==65535:continue
    d=i16(delta+2*k);r=u16(rg+2*k)
    gi=(cp+d)&65535 if not r else u16(rg+2*k+r+2*(cp-u16(st+2*k)))
    if r and gi:gi=(gi+d)&65535
    assert gi<glyphs
    if gi:m.append([cp,gi])
  row['bytes']=length
 elif f==0:
  length=u16(s+2);m=[[cp,gi] for cp,gi in enumerate(b[s+6:s+262]) if gi];row['bytes']=length
 elif f==6:
  length=u16(s+2);first=u16(s+6);cnt=u16(s+8);assert length==10+2*cnt
  m=[[first+j,u16(s+10+2*j)] for j in range(cnt) if u16(s+10+2*j)];assert all(g<glyphs for c,g in m);row['bytes']=length
 else:raise ValueError(('cmap format',f))
 row['mappings']=len(m);row['end']=s+row['bytes'];assert row['end']<=tables['cmap']['end'];cmaprows.append(row);maps.append({'subtable':i,'mappings':m})
po=tables['post']['start'];assert u32(po)==0x20000;ng=u16(po+32);assert ng==glyphs
indices=[u16(po+34+2*i) for i in range(ng)];custom=max(indices)-257;p=po+34+2*ng;postnames=[]
for i in range(custom):
 l=b[p];start=p+1;end=start+l;assert end<=tables['post']['end'];postnames.append({'index':258+i,'start':start,'end':end,'text':b[start:end].decode('ascii')});p=end
assert p<=tables['post']['end']
comparisons=[]
for f in sorted((R/'Fonts').glob('*.ttf')):
 raw=f.read_bytes();same=[]
 if raw[:4]==b'\x00\x01\x00\x00':
  for i in range(struct.unpack_from('>H',raw,4)[0]):
   tag,cs,off,size=struct.unpack_from('>4sIII',raw,12+16*i);tag=tag.decode()
   if tag in tables and sha(raw[off:off+size])==tables[tag]['sha256']:same.append(tag)
 comparisons.append({'path':str(f),'bytes':len(raw),'sha256':sha(raw),'exact_font_equal':raw==font,'equal_complete_tables':same})
meta={'source':'Game.exe','base':fontbase,'end':fontend,'bytes':len(font),'sha256':sha(font),'tables':tables,'name_records':names,'glyphs':glyphs,'units_per_em':u16(tables['head']['start']+18),'loca_format':locfmt,'horizontal_metrics':metrics,'cmap':cmaprows,'post_custom_names':postnames,'original_8_font_comparisons':comparisons,'semantic_boundary':'SFNT structure and byte identity. No font rasterization, bytecode execution or complete media semantics.'}
dump('embedded-font-structure.json',meta);dump('embedded-font-glyph-index.json',glyphrows);dump('embedded-font-cmap.json',maps)
u=[json.loads(l) for l in (ROOT/'remaining-unread.jsonl').read_text().splitlines() if json.loads(l)['path']=='Game.exe']
ptrs={r['slot_offset']:r for r in relocs if r['target']};dis=[];pending=[]
for row in u:
 s,e=row['start'],row['end_exclusive'];entry=None
 if s==792 and e==797:
  entry={'kind':'PE_SECTION_HEADER_NAME','evidence':'pe-sections.json/Game.exe/.rsrc','reason':'Exact section name field in complete PE section table.'}
 if fontbase<=s and e<=fontend:
  ts=[t for t,v in tables.items() if s<v['end'] and e>v['start']]
  if 'name' not in ts:
   entry={'kind':'SFNT_BINARY_SUBRUN' if 'post' not in ts else 'SFNT_GLYPH_NAME_IDENTITY','evidence':'embedded-font-structure.json','tables':ts,'reason':'Exact checksummed SFNT table byte range; glyph instruction/outline/metric/name-identity data, not independent diagnostic/program text. Font semantic review remains separate.'}
 if entry is None:
  for slot in range(s//8*8-8,s//8*8+9):
   r=ptrs.get(slot)
   if r and slot<=s and e<=slot+8:
    entry={'kind':'PE_RELOCATED_POINTER_BYTES','evidence':'game-relocation-pointers.json','slot_offset':slot,'reloc_record_offset':r['reloc_record_offset'],'value':r['value'],'target':r['target'],'reason':'Candidate is a strict byte subrun of a genuine DIR64 relocated image pointer. Its referenced content is not exempted.'};break
 if entry:dis.append(dict(row,semantic_status='INVENTORY_ONLY_TYPED',type_evidence=entry))
 else:pending.append(row)
raw=('\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in dis)+'\n').encode();(ROOT/'game-typed-dispositions.jsonl.gz').write_bytes(gzip.compress(raw,mtime=0))
dump('game-structure-summary.json',{'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate_count':len(u),'typed_count':len(dis),'typed_types':dict(collections.Counter(r['type_evidence']['kind'] for r in dis)),'pending_count':len(pending),'font_candidate_count':sum(fontbase<=r['start'] and r['end_exclusive']<=fontend for r in u),'font_identity':{k:meta[k] for k in ['base','end','bytes','sha256','glyphs']},'name_records':names,'font_comparisons':comparisons})
dump('game-pending-occurrences.json',pending)
pending_ids={r['candidate_id'] for r in pending};texts=[]
for line in (ROOT/'remaining-text-readset.jsonl').read_text().splitlines():
 r=json.loads(line);refs=[x for x in r['refs'] if x['candidate_id'] in pending_ids]
 if refs:texts.append(dict(r,refs=refs))
dump('game-pending-readset.json',texts)
(ROOT/'game-pending-view.txt').write_text('\n'.join(r['read_id']+' '+r['text'].replace('\r','\\r').replace('\n','\\n') for r in texts)+'\n')
print(json.dumps({'font':{k:meta[k] for k in ['base','end','bytes','sha256','glyphs']},'typed':len(dis),'pending_occurrences':len(pending),'pending_texts':len(texts),'types':dict(collections.Counter(r['type_evidence']['kind'] for r in dis)),'names':names,'cmap':cmaprows,'font_comparisons':comparisons},ensure_ascii=False))
