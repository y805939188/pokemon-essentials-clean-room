"""Match complete, explicitly typed integer arrays, never text shape or table envelope."""
import pathlib,re,struct,json,hashlib,gzip,ast,operator
P=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes()
def sha(v):return hashlib.sha256(v).hexdigest()
def integer(s):
 node=ast.parse(s,mode='eval').body
 def f(n):
  if isinstance(n,ast.Constant) and type(n.value)==int:return n.value
  if isinstance(n,ast.BinOp) and type(n.op) in (ast.Mult,ast.Add,ast.Sub):return {ast.Mult:operator.mul,ast.Add:operator.add,ast.Sub:operator.sub}[type(n.op)](f(n.left),f(n.right))
  raise ValueError('unsupported dimension')
 return f(node)
pat=re.compile(r'static\s+const\s+(unsigned short|unsigned char|unsigned int|short|int|ucs4_t|Summary16)\s+(\w+)\s*((?:\[[^\]]*\])+)?\s*=\s*\{')
arrays=[];rejected=[]
for p in sorted((P/'libiconv-type-reference').glob('*')):
 src=p.read_text();clean=re.sub(r'/\*.*?\*/|//[^\n]*',lambda m:'\n'*m.group().count('\n'),src,flags=re.S)
 for m in pat.finditer(clean):
  i=m.end();depth=1;j=i
  while depth and j<len(clean):
   depth+=(clean[j]=='{')-(clean[j]=='}');j+=1
  val=clean[i:j-1];typ,name,dims=m.groups();line=clean[:m.start()].count('\n')+1
  # No expression evaluation of C. Only wholly numeric initializers admitted.
  stripped=re.sub(r'-?(?:0[xX][0-9a-fA-F]+|[0-9]+)(?:[uUlL]*)','',val)
  if re.sub(r'[\s,{}]','',stripped):rejected.append({'path':p.name,'symbol':name,'reason':'nonliteral initializer'});continue
  vals=[int(re.sub(r'[uUlL]+$','',x),0) if not re.fullmatch(r'-?0[0-9]+',re.sub(r'[uUlL]+$','',x)) else int(re.sub(r'[uUlL]+$','',x),10) for x in re.findall(r'-?(?:0[xX][0-9a-fA-F]+|[0-9]+)(?:[uUlL]*)',val)]
  fmt={'unsigned short':'H','unsigned char':'B','unsigned int':'I','short':'h','int':'i','ucs4_t':'I','Summary16':'H'}[typ]
  if dims:
   ds=re.findall(r'\[([^\]]*)\]',dims)
   if all(ds):
    count=1
    try:
     for d in ds:count*=integer(d)
    except ValueError:rejected.append({'path':p.name,'symbol':name,'reason':'dimension expression not admitted'});continue
    expected=count*(2 if typ=='Summary16' else 1)
    if len(vals)!=expected:
     if len(ds)==1 and typ!='Summary16' and len(vals)<expected:vals+=([0]*(expected-len(vals)))
     else:rejected.append({'path':p.name,'symbol':name,'reason':'nontrivial implicit initializer layout'});continue
  try:raw=struct.pack('<'+fmt*len(vals),*vals)
  except struct.error:rejected.append({'path':p.name,'symbol':name,'reason':'literal outside exact type range'});continue
  if len(raw)<128:continue
  starts=[];pos=10648064
  while True:
   pos=b.find(raw,pos,13663232)
   if pos<0:break
   starts.append(pos);pos+=1
  if starts:arrays.append({'source_file':p.name,'source_sha256':sha(p.read_bytes()),'declaration_line':line,'symbol':name,'type':typ,'dimensions':dims,'numeric_elements':len(vals),'element_bytes':struct.calcsize(fmt),'bytes':len(raw),'raw_little_endian_sha256':sha(raw),'matched_complete_ranges':[{'start':s,'end':s+len(raw),'sha256':sha(b[s:s+len(raw)])} for s in starts]})
ranges=[dict(r,source_file=a['source_file'],symbol=a['symbol'],type=a['type'],declaration_line=a['declaration_line']) for a in arrays for r in a['matched_complete_ranges']]
e={'schema':'gr8.binary.complete-integer-array-type-proof/v1','supplemental_source':'libiconv-fetch-r2.json','source_authenticity':'UNVERIFIED_MIRROR; type proof depends only on literal declarations, complete array bytes and native evidence, not version/authenticity assertion','arrays':arrays,'rejected_or_unadmitted':rejected,'qualification':'Only complete explicitly typed numeric initializer arrays >=128B, exact whole bytes matched within actualGame.rdata. No C compiled/executed; no arbitrary neighboring ranges covered; labels/options/diagnostics not exempt. Full charset algorithm/dispatch/runtime equivalence not proved.'}
(P/'iconv-complete-array-type-evidence.json').write_text(json.dumps(e,indent=2)+'\n')
u=json.loads((P/'game-after-float-occurrences.json').read_text());done=[];left=[]
for row in u:
 s,z=row['start'],row['end_exclusive'];hits=[r for r in ranges if r['start']<z and s<r['end']];pos=s
 for a,c in sorted((max(s,r['start']),min(z,r['end'])) for r in hits):
  if a>pos:break
  pos=max(pos,c)
 if pos>=z:done.append(dict(row,semantic_status='INVENTORY_ONLY_TYPED',type_evidence={'kind':'EXACT_COMPLETE_DECLARED_NUMERIC_ARRAY_BYTES','evidence':'iconv-complete-array-type-evidence.json','ranges':hits},qualification='Numeric byte type only; complete native conversion behavior and dispatch remain separate.'))
 else:left.append(row)
(P/'iconv-typed-dispositions.jsonl.gz').write_bytes(gzip.compress(('\n'.join(json.dumps(r,separators=(',',':')) for r in done)+'\n').encode(),mtime=0))
(P/'game-after-iconv-occurrences.json').write_text(json.dumps(left,separators=(',',':'))+'\n')
view=['%s:%s %s %s %dB %s ->%s'%(a['source_file'],a['declaration_line'],a['type'],a['symbol'],a['bytes'],a['raw_little_endian_sha256'],','.join(str(r['start'])+'..'+str(r['end']) for r in a['matched_complete_ranges'])) for a in arrays]
(P/'iconv-complete-array-type-view.txt').write_text('\n'.join(view)+'\n')
print(json.dumps({'matched_complete_arrays':len(arrays),'ranges':len(ranges),'new_exact_numeric_candidates':len(done),'remaining_other_candidates':len(left),'matched_numeric_bytes_sum_before_overlap':sum(r['end']-r['start'] for r in ranges)}))
