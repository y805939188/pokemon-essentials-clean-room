"""Match entire declared GUID constants, preserving interface name as metadata."""
import pathlib,re,json,struct,hashlib,gzip
P=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes();a=[]
for f in sorted((P/'guid-type-reference').glob('*.c')):
 src=f.read_text();clean=re.sub(r'/\*.*?\*/|//[^\n]*','',src,flags=re.S)
 for m in re.finditer(r'DEFINE_GUID\s*\(([^()]*)\)\s*;',clean,re.S):
  v=[x.strip() for x in m[1].split(',')]
  if len(v)!=12 or any(not re.fullmatch(r'(?:0[xX][0-9a-fA-F]+|[0-9]+)[uUlL]*',x) for x in v[1:]):continue
  vals=[int(re.sub(r'[uUlL]+$','',x),16 if x.lower().startswith('0x') else 10) for x in v[1:]]
  try:raw=struct.pack('<IHH8B',*vals)
  except struct.error:continue
  if sum(x!=0 for x in raw)<6:continue
  hits=[];q=10648064
  while True:
   q=b.find(raw,q,13663232)
   if q<0:break
   hits.append({'start':q,'end':q+16,'sha256':hashlib.sha256(raw).hexdigest()});q+=1
  if hits:a.append({'name':v[0],'numeric_fields':vals,'source_file':f.name,'source_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'raw_hex':raw.hex(),'complete_matches':hits})
ranges=[dict(r,GUID_name=r0['name'],source_file=r0['source_file']) for r0 in a for r in r0['complete_matches']]
u=json.loads((P/'game-after-operands-occurrences.json').read_text());done=[];left=[]
for row in u:
 s,z=row['start'],row['end_exclusive'];hits=[r for r in ranges if r['start']<z and s<r['end']];pos=s
 for lo,hi in sorted((max(s,r['start']),min(z,r['end'])) for r in hits):
  if lo>pos:break
  pos=max(pos,hi)
 if pos>=z:done.append(dict(row,semantic_status='INVENTORY_ONLY_TYPED',type_evidence={'kind':'EXACT_COMPLETE_GUID_INTEGER_FIELDS','evidence':'guid-complete-constant-type-evidence.json','ranges':hits},qualification='GUID name retained as metadata; raw candidate letters are a subrun of the entire16byte value. No interface instantiation/selected backend or universal otherconsumer assertion.'))
 else:left.append(row)
(P/'guid-complete-constant-type-evidence.json').write_text(json.dumps({'constants':a,'qualification':'Explicit11numeric GUID fields ->16byte IHH8B layout, completeexact bytes. Supplemental source not compiled/executed. Only candidatebytes whollycovered; no broad GUID-looking region exemption.'},indent=2)+'\n');(P/'guid-typed-dispositions.jsonl.gz').write_bytes(gzip.compress(('\n'.join(json.dumps(r,separators=(',',':')) for r in done)+'\n').encode(),mtime=0));(P/'game-after-guid-occurrences.json').write_text(json.dumps(left,separators=(',',':'))+'\n');(P/'guid-type-view.txt').write_text('\n'.join('%d %s %s'%(i,r['name'],','.join(str(x['start'])+'-'+str(x['end']) for x in r['complete_matches'])) for i,r in enumerate(a,1))+'\n');print(json.dumps({'complete_matched_GUIDs':len(a),'complete_ranges':len(ranges),'new_numeric_candidates':len(done),'remaining':len(left)}))
