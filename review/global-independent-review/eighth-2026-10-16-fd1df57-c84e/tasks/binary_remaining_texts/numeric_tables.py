"""Exact ranges derived from complete named native windows already read by reviewer."""
import pathlib,json,struct,hashlib,gzip,collections
ROOT=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes()
sections=json.loads((ROOT/'pe-sections.json').read_text())['Game.exe']['sections']
def off(x):
 for s in sections:
  if s['rva']<=x<s['rva']+s['bytes']:return x-s['rva']+s['offset']
 raise ValueError(hex(x))
def sha(x):return hashlib.sha256(x).hexdigest()
def dump(n,x):(ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
defs=[
 (8096272,0xc1a160,[(0xc19ea0,0x2000,0x266f),(0xc1a040,0,0x45f),(0xc18920,0x4e00,0x9f9f),(0xc19da0,0x3000,0x33df),(0xc17dc0,0xf900,0xfa0f),(0xc17e20,0xac00,0xd79f),(0xc17d80,0xff00,0xffef)]),
 (8095616,0xc8e780,[(0xc8e4c0,0x2000,0x264f),(0xc8e660,0,0x45f),(0xc8d060,0x4e00,0x9cef),(0xc8e420,0x3000,0x322f),(0xc8cfa0,0xff00,0xffef),(0xc8cfe0,0x9e00,0x9faf)]),
 (8094992,0xc972e0,[(0xc971b0,0x2100,0x212f),(0xc971c0,0,0x45f),(0xc95d20,0xff00,0xff5f),(0xc95d40,0x4e00,0x9faf)]),
 (8154320,0xc8c140,[(0xc8c080,0x300,0x3bf),(0xc8c0c0,0,0x1ff),(0xc8c000,0x1e00,0x1fbf),(0xc8bfe0,0x3000,0x303f),(0xc8bf60,0x3200,0x33ff),(0xc8b3a0,0x4e00,0x7cff),(0xc8ae60,0x7e00,0x92cf),(0xc8ac20,0x9400,0x9cef),(0xc8aba0,0x9e00,0x9f8f),(0xc8ab80,0xff00,0xff4f)])]
ranges=[];proofs=[]
for fn,out,descs in defs:
 hi=0;sub=[]
 for va,cp0,cp1 in descs:
  assert cp0%16==0 and cp1%16==15;n=(cp1-cp0+1)//16;s=off(va);z=s+4*n;entries=[struct.unpack_from('<HH',b,s+4*i) for i in range(n)]
  mx=max((idx+bits.bit_count() for idx,bits in entries if bits),default=0);hi=max(hi,mx)
  row={'kind':'NUMERIC_SUMMARY_INDEX_BITMAP','function':fn,'codepoint_start':cp0,'codepoint_end_inclusive':cp1,'start':s,'end':z,'records':n,'record_bytes':4,'sha256':sha(b[s:z]),'maximum_exclusive_output_index':mx,'source':'native-'+str(fn)+'.stdout'};sub.append(row);ranges.append(row)
 s=off(out);z=s+2*hi;row={'kind':'NUMERIC_UINT16_OUTPUT_TABLE','function':fn,'start':s,'end':z,'records':hi,'record_bytes':2,'sha256':sha(b[s:z]),'source':'native-'+str(fn)+'.stdout','reason':'Full native function selects 4-byte index/bitmap rows by guarded scalar ranges, counts bits below input nibble, adds uint16start index, reads this table at scale2, rotates the loaded word and writes two outputbytes.'};ranges.append(row);proofs.append({'function':fn,'output':row,'summary_ranges':sub})
# Complete read function8116496 has a further two-stage64-codepoint block directory.
# Its maximum accepted scalar is0x2a6bf; each nonnegative int16directory entry
# selects64logical positions, each16positions selects an index/bitmap row.
s=off(0xbedf80);n=(0x2a6bf>>6)+1;z=s+2*n;directory=list(struct.unpack_from('<'+'h'*n,b,s))
ranges.append({'kind':'NUMERIC_SIGNED16_PAGE_DIRECTORY','function':8116496,'start':s,'end':z,'records':n,'record_bytes':2,'sha256':sha(b[s:z]),'source':'native-8116496.stdout'})
used=sorted({page*4+j for page in directory if page>=0 for j in range(4)});st=off(0xbe5d80);mx=0
for i in used:
 idx,bits=struct.unpack_from('<HH',b,st+4*i);mx=max(mx,idx+bits.bit_count())
# Only actual selected rows are typed; gaps are not silently included.
for i in used:ranges.append({'kind':'NUMERIC_SUMMARY_INDEX_BITMAP','function':8116496,'start':st+4*i,'end':st+4*i+4,'records':1,'record_bytes':4,'sha256':sha(b[st+4*i:st+4*i+4]),'source':'native-8116496.stdout'})
s=off(0xbe87e0);z=s+2*mx;ranges.append({'kind':'NUMERIC_UINT16_OUTPUT_TABLE','function':8116496,'start':s,'end':z,'records':mx,'record_bytes':2,'sha256':sha(b[s:z]),'source':'native-8116496.stdout'})
dump('numeric-table-evidence.json',{'complete_window_descriptors':proofs,'ranges':ranges,'qualification':'Pure byte-type evidence for exact ranges. Charset choice, native dispatch and full engine equivalence remain unproved. Numeric tables not copied into clean-room specs.'})
u=json.loads((ROOT/'game-pending-occurrences.json').read_text());done=[];left=[]
for row in u:
 s,e=row['start'],row['end_exclusive'];hits=[x for x in ranges if x['start']<e and x['end']>s];intervals=sorted((max(s,x['start']),min(e,x['end'])) for x in hits);pos=s
 for a,z in intervals:
  if a>pos:break
  pos=max(pos,z)
 if pos>=e:
  done.append(dict(row,semantic_status='INVENTORY_ONLY_TYPED',type_evidence={'kind':'PROVEN_INDEXED_NUMERIC_TABLE_BYTES','evidence':'numeric-table-evidence.json','ranges':[{'start':r['start'],'end':r['end'],'kind':r['kind'],'function':r['function']} for r in hits],'reason':'Every candidate byte belongs to the exact numerically indexed input/output table ranges proven by the complete guarded native consumers.'}))
 else:left.append(row)
raw=('\n'.join(json.dumps(r,separators=(',',':')) for r in done)+'\n').encode();(ROOT/'numeric-typed-dispositions.jsonl.gz').write_bytes(gzip.compress(raw,mtime=0));dump('game-after-numeric-occurrences.json',left)
ids={r['candidate_id'] for r in left};texts=[]
for row in json.loads((ROOT/'game-pending-readset.json').read_text()):
 refs=[r for r in row['refs'] if r['candidate_id'] in ids]
 if refs:texts.append(dict(row,refs=refs))
dump('game-after-numeric-readset.json',texts);(ROOT/'game-after-numeric-view.txt').write_text('\n'.join(r['read_id']+' '+r['text'].replace('\r','\\r').replace('\n','\\n') for r in texts)+'\n')
print(json.dumps({'newly_typed':len(done),'remaining_occurrences':len(left),'remaining_texts':len(texts),'output_tables':[r for r in ranges if r['kind']=='NUMERIC_UINT16_OUTPUT_TABLE']}))
