"""Exact whole-array bytes from explicit numeric declarations, not vocabulary classification."""
import pathlib,re,struct,json,hashlib,gzip,ast,operator
P=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes()
def sha(x):return hashlib.sha256(x).hexdigest()
types={'long':'i','int':'i','short':'h','char':'B','unsigned int':'I','unsigned long':'I','unsigned short':'H','unsigned char':'B','float':'f','double':'d','u8':'B','u32':'I','u64':'Q','uint8_t':'B','uint16_t':'H','uint32_t':'I','uint64_t':'Q','ogg_uint32_t':'I','ogg_int32_t':'i','BN_ULONG':'Q','DES_LONG':'I','CAST_LONG':'I','BF_LONG':'I','FT_Byte':'B','FT_UShort':'H','FT_Short':'h','FT_UInt':'I','FT_Int':'i','FT_UInt32':'I','FT_Int32':'i','FT_ULong':'I','FT_Long':'i','FT_Fixed':'i'}
pat=re.compile(r'(?:static\s+)?const\s+('+'|'.join(sorted(types,key=len,reverse=True))+r')\s+(\w+)\s*((?:\[[^\]]*\])+?)\s*=\s*\{')
num=r'[+-]?(?:0[xX][0-9a-fA-F]+|(?:[0-9]+\.[0-9]*|\.[0-9]+|[0-9]+)(?:[eE][+-]?[0-9]+)?)[fFuUlL]*'
arrays=[];unadmitted=[]
for project in ['vorbis','openssl','freetype']:
 for f in sorted((P/(project+'-type-reference')).rglob('*')):
  if not f.is_file():continue
  # Latin1 maps every source byte one-to-one; numeric tokens are strictASCII.
  # Some FreeType historical author comments are not UTF8.
  src=f.read_text(encoding='latin1');src=re.sub(r'/\*.*?\*/|//[^\n]*',lambda m:'\n'*m.group().count('\n'),src,flags=re.S)
  # Drop directive lines only to locate a complete literal initializer across
  # FreeType's declaration/data conditional. No branch choice or C execution.
  src=re.sub(r'^[ \t]*#[^\n]*', '', src, flags=re.M)
  for m in pat.finditer(src):
   typ,name,dims=m.groups();j=m.end();depth=1
   while depth and j<len(src):depth+=(src[j]=='{')-(src[j]=='}');j+=1
   body=src[m.end():j-1]
   # Permit only suffix macros that wrap a single integer literal, with explicit representation below.
   body=re.sub(r'\b(?:U64|C64|UINT64_C|UINT32_C)\(\s*('+num+r')\s*\)',r'\1',body)
   if re.sub(r'[\s,{}]','',re.sub(num,'',body)):
    unadmitted.append({'file':str(f.relative_to(P)),'symbol':name,'reason':'nonliteral initializer not interpreted'});continue
   tokens=re.findall(num,body);fmt=types[typ]
   try:
    if fmt in 'fd':vals=[float(re.sub(r'[fFlL]+$','',x)) for x in tokens]
    else:
     vals=[]
     for x in tokens:
      v=re.sub(r'[uUlL]+$','',x);v=int(v,16 if re.fullmatch(r'[+-]?0[xX][0-9a-fA-F]+',v) else 10)
      if typ=='char' and -128<=v<=255:v&=255
      vals.append(v)
    ds=re.findall(r'\[([^\]]*)\]',dims)
    # These two exact definitions were actually read in masking.h/psy.h;
    # no other preprocessor expression is interpreted.
    if project=='vorbis':ds=[{'P_BANDS':'17','EHMER_MAX':'56'}.get(d.strip(),d) for d in ds]
    if len(ds)==1 and not ds[0].strip():pass
    elif all(re.fullmatch(r'[0-9]+[uUlL]*',d.strip()) for d in ds):
     n=1
     for d in ds:n*=int(re.sub(r'[uUlL]+$','',d.strip()))
     if len(ds)==1:assert len(vals)<=n;vals+=([0]*(n-len(vals)))
     else:assert len(vals)==n
    else:raise ValueError('dimension not wholly literal; not proved complete array')
    raw=struct.pack('<'+fmt*len(vals),*vals)
   except (ValueError,struct.error,AssertionError):unadmitted.append({'file':str(f.relative_to(P)),'symbol':name,'reason':'literal or type/cardinality not admitted'});continue
   if len(raw)<128:continue
   hits=[];q=10648064
   while True:
    q=b.find(raw,q,13663232)
    if q<0:break
    hits.append({'start':q,'end':q+len(raw),'sha256':sha(raw)});q+=1
   if hits:arrays.append({'project':project,'source_file':str(f.relative_to(P)),'source_sha256':sha(f.read_bytes()),'declaration_line':src[:m.start()].count('\n')+1,'type':typ,'symbol':name,'dimensions':dims,'elements':len(vals),'LE_representation':fmt,'element_bytes':struct.calcsize(fmt),'array_sha256':sha(raw),'matched_complete_ranges':hits})
ranges=[dict(r,symbol=a['symbol'],source_file=a['source_file'],type=a['type'],element_bytes=a['element_bytes']) for a in arrays for r in a['matched_complete_ranges']]
(P/'scalar-complete-array-type-evidence.json').write_text(json.dumps({'arrays':arrays,'unadmitted_initializers':unadmitted,'qualification':'Only complete explicit scalar numeric initializer arrays>=128B with exact entire source bytes matched. External source not compiled/executed. OpenSSL target version1.1.1i differs supplement1.1.1w; no version or wholealgorithm equivalence asserted. Aliases/LLP64 formats explicit, matching original bytes only grants numeric type for exact full arrays; no adjacent diagnostics/config exemptions.'},indent=2)+'\n')
u=json.loads((P/'game-after-fluidsynth-occurrences.json').read_text());done=[];left=[]
for row in u:
 s,z=row['start'],row['end_exclusive'];hits=[r for r in ranges if r['start']<z and s<r['end']];pos=s
 for a,c in sorted((max(s,r['start']),min(z,r['end'])) for r in hits):
  if a>pos:break
  pos=max(pos,c)
 if pos>=z:done.append(dict(row,semantic_status='INVENTORY_ONLY_TYPED',type_evidence={'kind':'EXACT_COMPLETE_DECLARED_SCALAR_NUMERIC_ARRAY','evidence':'scalar-complete-array-type-evidence.json','ranges':hits}))
 else:left.append(row)
(P/'scalar-typed-dispositions.jsonl.gz').write_bytes(gzip.compress(('\n'.join(json.dumps(r,separators=(',',':')) for r in done)+'\n').encode(),mtime=0));(P/'game-after-scalar-occurrences.json').write_text(json.dumps(left,separators=(',',':'))+'\n')
(P/'scalar-array-declaration-view.txt').write_text('\n'.join('%d %s:%d %s %s %d elems %s'%(i,a['source_file'],a['declaration_line'],a['type'],a['symbol'],a['elements'],','.join(str(r['start'])+'-'+str(r['end']) for r in a['matched_complete_ranges'])) for i,a in enumerate(arrays,1))+'\n');print(json.dumps({'matched_arrays':len(arrays),'range_count':len(ranges),'new_numeric_candidates':len(done),'remaining':len(left)}))
