"""Read exactly three complete fixed embedded numeric font tables, without font execution."""
import datetime,hashlib,json,struct
from pathlib import Path
OUT=Path(__file__).resolve().parent
raw=Path('/workspace/pokemon-essentials/Game.exe').read_bytes()
assert len(raw)==14732288 and hashlib.sha256(raw).hexdigest()=='5c75e92fcbb6ec50b9f8fc61913d751a8945d6a1fc69c3017c7b8686b532bf04'
tables={}
for tag,start,end,sha in [('FFTM',10568060,10568088,'a97728020ac8bd8a1d94eead7fdaad7a4fe8e6df9721c1f8faf0b1a1005f42ca'),('OS/2',10218328,10218424,'a04ee0cc42d0974c110eb574d5e72a1058fe9c4196537002bce485529b2d31b0'),('gasp',10546372,10546388,'ed0c69fa6b09906a5907f5f21d01eb5f968ecb14e10f606ef09910a5d113419d')]:
 data=raw[start:end];assert hashlib.sha256(data).hexdigest()==sha
 tables[tag]={'source_span':[start,end],'bytes':len(data),'sha256':sha,'entire_original_hex':data.hex()}
 if tag=='FFTM':
  values=struct.unpack('>IQQQ',data)
  tables[tag]['fields']=dict(zip(['version','FFTimeStamp','sourceCreated','sourceModified'],values))
 elif tag=='gasp':
  version,count=struct.unpack_from('>HH',data,0);assert len(data)==4+4*count
  tables[tag].update(version=version,count=count,ranges=[{'maxPPEM':a,'behavior':b,'set_bits':[n for n in range(16) if b&(1<<n)]} for a,b in struct.iter_unpack('>HH',data[4:])])
 else:
  fields=[('version','H'),('xAvgCharWidth','h'),('usWeightClass','H'),('usWidthClass','H'),('fsType','H')]
  fields += [(n,'h') for n in ['ySubscriptXSize','ySubscriptYSize','ySubscriptXOffset','ySubscriptYOffset','ySuperscriptXSize','ySuperscriptYSize','ySuperscriptXOffset','ySuperscriptYOffset','yStrikeoutSize','yStrikeoutPosition','sFamilyClass']]
  fields += [('panose','10s')]+[(f'ulUnicodeRange{i}','I') for i in range(1,5)]+[('achVendID','4s')]
  fields += [(n,'H') for n in ['fsSelection','usFirstCharIndex','usLastCharIndex']]+[(n,'h') for n in ['sTypoAscender','sTypoDescender','sTypoLineGap']]+[(n,'H') for n in ['usWinAscent','usWinDescent']]
  fields += [('ulCodePageRange1','I'),('ulCodePageRange2','I'),('sxHeight','h'),('sCapHeight','h'),('usDefaultChar','H'),('usBreakChar','H'),('usMaxContext','H')]
  offset=0;rows=[]
  for name,fmt in fields:
   size=struct.calcsize('>'+fmt);value=struct.unpack_from('>'+fmt,data,offset)[0]
   if name=='panose':value=list(value)
   elif isinstance(value,bytes):value=value.decode('ascii')
   row={'name':name,'type':fmt,'table_span':[offset,offset+size],'value':value}
   if name.startswith('ulUnicodeRange') or name.startswith('ulCodePageRange') or name in ['fsType','fsSelection']:
    row['set_bits']=[n for n in range(32 if fmt=='I' else 16) if value&(1<<n)]
   rows.append(row);offset+=size
  assert offset==len(data)==96 and rows[0]['value']==3
  tables[tag]['all_fields']=rows
result={'schema':'gr8-complete-three-font-metadata-structure/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':'Game.exe','font_span':[10217888,10568088],'tables':tables,'target_execution':False,'generation_semantic_credit':0}
(OUT/'font-three-metadata-structure.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
