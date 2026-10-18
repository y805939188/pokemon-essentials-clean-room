"""Type exact native numeric-constant records using read bounded native consumers."""
import pathlib,json,struct,hashlib,gzip
ROOT=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes();secs=json.loads((ROOT/'pe-sections.json').read_text())['Game.exe']['sections'];base=5368709120
def off(va):
 for s in secs:
  if s['rva']<=va-base<s['rva']+s['bytes']:return s['offset']+va-base-s['rva']
 raise ValueError(hex(va))
def sha(x):return hashlib.sha256(x).hexdigest()
records=[];ranges={}
for i in range(82):
 p=10908992+32*i;nid,data,method,comment=struct.unpack_from('<QQQQ',b,p);assert nid<2000
 z=off(comment);e=b.index(b'\0',z);text=b[z:e].decode('ascii');row={'record':i,'record_start':p,'numeric_id':nid,'data_va':data,'method_va':method,'comment_start':z,'comment_end':e,'comment':text}
 if data:
  s=off(data);ft,seed,width,cofactor=struct.unpack_from('<IIII',b,s);assert ft in (406,407) and seed<=128 and 0<width<=128 and cofactor<=65536
  end=s+16+seed+6*width;assert end<=len(b);fields=[]
  for j in range(6):
   a=s+16+seed+j*width;fields.append({'field_index':j,'start':a,'end':a+width,'sha256':sha(b[a:a+width])})
  proof={'start':s,'end':end,'bytes':end-s,'sha256':sha(b[s:end]),'field_type_id':ft,'seed_bytes':seed,'numeric_width':width,'cofactor':cofactor,'numeric_fields':fields,'seed_start':s+16,'seed_end':s+16+seed}
  row['data']=proof;ranges[s]=proof
 records.append(row)
evidence={'registry_start':10908992,'registry_end':10911616,'records':records,'distinct_data_records':len(ranges),'native_consumers':['native-1382256.stdout','native-1380928.stdout'],'qualification':'82row bound and32byte stride explicit in full native consumers. Data header gives seed length and fixed numeric width; six successive width-byte values are loaded before construction and cofactor. This is numeric EC parameter/seed storage, not runnable source or plaintext messages. No cryptographic behavior executed.'}
(ROOT/'ec-constant-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
rows=json.loads((ROOT/'game-after-numeric-occurrences.json').read_text());done=[];left=[]
for row in rows:
 hits=[r for r in ranges.values() if r['start']<=row['start'] and row['end_exclusive']<=r['end']]
 if hits:done.append(dict(row,semantic_status='INVENTORY_ONLY_TYPED',type_evidence={'kind':'NATIVE_NUMERIC_CURVE_PARAMETER_BYTES','evidence':'ec-constant-evidence.json','record_start':hits[0]['start'],'record_end':hits[0]['end'],'record_sha256':hits[0]['sha256'],'reason':'Strict subrun inside an exact native record consisting of bounded seed and six fixed-width numeric fields; comments are separate text fields and are not exempted.'}))
 else:left.append(row)
(ROOT/'ec-typed-dispositions.jsonl.gz').write_bytes(gzip.compress(('\n'.join(json.dumps(r,separators=(',',':')) for r in done)+'\n').encode(),mtime=0));(ROOT/'game-after-ec-occurrences.json').write_text(json.dumps(left,separators=(',',':'))+'\n')
print(json.dumps({'registry_rows':len(records),'distinct_data_records':len(ranges),'typed_candidates':len(done),'remaining_occurrences':len(left),'comments':list(dict.fromkeys(r['comment'] for r in records))},ensure_ascii=False))
