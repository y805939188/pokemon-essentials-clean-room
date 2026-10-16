"""Recover fixed font envelope only; no VM/render/target-code or third-party helper execution."""
import datetime,hashlib,json,struct
from pathlib import Path
OUT=Path(__file__).resolve().parent/'font-envelope-recovery-001'
OUT.mkdir(exist_ok=True)
game=Path('/workspace/pokemon-essentials/Game.exe').read_bytes()
assert hashlib.sha256(game).hexdigest()=='5c75e92fcbb6ec50b9f8fc61913d751a8945d6a1fc69c3017c7b8686b532bf04'
f=game[10217888:10568088]
assert hashlib.sha256(f).hexdigest()=='e5b0af421ea2bfbc1ac8d251d647268087ae82786234c57f757d1f0b90fa8b49'
version,count,srange,selector,shift=struct.unpack_from('>IHHHH',f)
entries=[];tables={}
for i in range(count):
 at=12+16*i;tag,checksum,start,size=struct.unpack_from('>4sIII',f,at);tag=tag.decode()
 entries.append({'tag':tag,'checksum':checksum,'relative_span':[start,start+size],'source_span':[10217888+start,10217888+start+size],'bytes':size,'directory_span':[10217888+at,10217888+at+16]})
 tables[tag]=f[start:start+size]
position=12+16*count;gaps=[]
for row in sorted(entries,key=lambda z:z['relative_span'][0]):
 start,end=row['relative_span'];assert position<=start
 if position<start:gaps.append({'relative_span':[position,start],'whole_hex':f[position:start].hex()})
 position=end
assert position==len(f) and all(set(bytes.fromhex(x['whole_hex']))<={0} for x in gaps)
name=tables['name'];fmt,n,storage=struct.unpack_from('>HHH',name);records=[];used=set()
for i in range(n):
 row=struct.unpack_from('>6H',name,6+12*i);records.append(dict(zip(['platform','encoding','language','nameID','length','offset'],row)))
 used.update(range(storage+row[5],storage+row[5]+row[4]))
unused=[];start=None
for i in range(storage,len(name)):
 if i not in used and start is None:start=i
 if i in used and start is not None:unused.append({'table_span':[start,i],'whole_hex':name[start:i].hex()});start=None
if start is not None:unused.append({'table_span':[start,len(name)],'whole_hex':name[start:].hex()})
assert storage==6+12*n and len(used)+sum((x['table_span'][1]-x['table_span'][0]) for x in unused)+storage==len(name)
assert all(set(bytes.fromhex(x['whole_hex']))<={0} for x in unused)
post=tables['post'];ph=struct.unpack_from('>IihhIIIII',post)
post_header=dict(zip(['format_raw16_16','italicAngle_raw16_16','underlinePosition','underlineThickness','isFixedPitch','minMemType42','maxMemType42','minMemType1','maxMemType1'],ph))
cmap=tables['cmap'];cv,cn=struct.unpack_from('>HH',cmap);crecords=[];segments=[]
for i in range(cn):
 platform,encoding,offset=struct.unpack_from('>HHI',cmap,4+8*i);fmt,length,language=struct.unpack_from('>HHH',cmap,offset)
 crecords.append({'platform':platform,'encoding':encoding,'offset':offset,'format':fmt,'length':length,'language':language})
 if fmt==4 and not segments:
  h=struct.unpack_from('>7H',cmap,offset);ns=h[3]//2
  end=struct.unpack_from('>'+str(ns)+'H',cmap,offset+14);start=struct.unpack_from('>'+str(ns)+'H',cmap,offset+16+2*ns);delta=struct.unpack_from('>'+str(ns)+'h',cmap,offset+16+4*ns);roffset=struct.unpack_from('>'+str(ns)+'H',cmap,offset+16+6*ns)
  assert all(x==0 for x in roffset) and length==16+8*ns
  segments=[dict(zip(['start','end','signed_delta','range_offset'],row)) for row in zip(start,end,delta,roffset)]
  fmt4={'segCountX2':h[3],'searchRange':h[4],'entrySelector':h[5],'rangeShift':h[6],'reservedPad':struct.unpack_from('>H',cmap,offset+14+2*ns)[0],'glyphIdArrayCount':0}
 if fmt==6:
  first,entries6=struct.unpack_from('>HH',cmap,offset+6);fmt6={'firstCode':first,'entryCount':entries6,'glyphIdArrayType':'uint16be whole256 entries; fullmappingreceivedearlier'};assert length==10+2*entries6
result={'schema':'gr8-current-font-complete-envelope/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'font_span':[10217888,10568088],'font_sha256':hashlib.sha256(f).hexdigest(),'header':{'sfntVersion':version,'numTables':count,'searchRange':srange,'entrySelector':selector,'rangeShift':shift},'complete_directory':entries,'all_intertable_gaps':gaps,'coverage':{'header':12,'directory':16*count,'tables':sum(z['bytes'] for z in entries),'padding':sum(len(bytes.fromhex(z['whole_hex'])) for z in gaps),'total':len(f)},'name_structure':{'format':fmt if False else struct.unpack_from('>H',name)[0],'count':n,'storageOffset':storage,'all_records':records,'text_byte_union':len(used),'all_unused_storage':unused,'unused_storage_bytes':sum(len(bytes.fromhex(z['whole_hex'])) for z in unused),'table_bytes':len(name),'text_reading':'All30entiretextsactualreadearlier; no newtextreadcreditfromthishelper'},'post_header':post_header,'post_remaining_body':'Whole2587nameIndexnumericmap and2333customtextsactualreadearlier; no newbodycreditfromthishelper','cmap_header':{'version':cv,'count':cn,'records':crecords,'format4':fmt4,'all127_format4_segments':segments,'format6':fmt6},'target_execution':False,'generation_semantic_credit':0}
assert sum(result['coverage'][k] for k in ['header','directory','tables','padding'])==350200
(OUT/'structure.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
