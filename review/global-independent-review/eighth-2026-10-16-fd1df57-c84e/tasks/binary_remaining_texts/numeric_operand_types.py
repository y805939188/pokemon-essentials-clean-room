"""Exact fixed-width numeric RIP operands. No adjacent region/table inference."""
import pathlib,json,gzip,hashlib,re
P=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes();edges=[json.loads(l) for l in gzip.decompress((P/'native-direct-reference-edges.jsonl.gz').read_bytes()).splitlines()]
# Only intrinsically numeric/logical operations, not genericmov/copy/lea/stringops.
widths={}
for op in ['add','sub','mul','div','sqrt','min','max','comi','ucomi']:
 for suffix,n in [('ss',4),('sd',8)]:widths[op+suffix]=n
for op in ['addps','subps','mulps','divps','sqrtps','minps','maxps','addpd','subpd','mulpd','divpd','sqrtpd','minpd','maxpd','andps','andnps','orps','xorps','andpd','andnpd','orpd','xorpd','pand','pandn','por','pxor','paddb','paddw','paddd','paddq','psubb','psubw','psubd','psubq','pmullw','pmulhw','pmuludq','pcmpeqb','pcmpeqw','pcmpeqd','pcmpgtb','pcmpgtw','pcmpgtd']:widths[op]=16
ranges=[]
for e in edges:
 op=e['assembly'].split()[0]
 if op not in widths:continue
 n=widths[op];s=e['target_offset'];z=s+n
 if not(10648064<=s<z<=13663232):continue
 ranges.append({'start':s,'end':z,'operand_bytes':n,'instruction_offset':e['instruction_offset'],'instruction_sha256':e['instruction_sha256'],'instruction_raw_hex':e['instruction_bytes_hex'],'assembly':e['assembly'],'pdata_function':e['containing_pdata_function'],'sha256':hashlib.sha256(b[s:z]).hexdigest()})
u=json.loads((P/'game-after-scalar-occurrences.json').read_text());done=[];left=[];used=set()
for row in u:
 s,z=row['start'],row['end_exclusive'];hits=[(i,r) for i,r in enumerate(ranges) if r['start']<z and s<r['end']];pos=s
 for a,c in sorted((max(s,r['start']),min(z,r['end'])) for _,r in hits):
  if a>pos:break
  pos=max(pos,c)
 if pos>=z:
  used.update(i for i,r in hits);done.append(dict(row,semantic_status='INVENTORY_ONLY_TYPED',type_evidence={'kind':'EXACT_FIXED_WIDTH_NUMERIC_NATIVE_OPERAND','evidence':'numeric-operand-type-evidence.json','range_indexes':[i for i,r in hits]},qualification='Known numeric operand use only. Does not prove arbitrary neighboring bytes, wholeCFG, behavior or universal absence of other consumers.'))
 else:left.append(row)
(P/'numeric-operand-type-evidence.json').write_text(json.dumps({'ranges':ranges,'used_range_indexes':sorted(used),'qualification':'Instruction raw bytes, length/displacement target independently verified. Only intrinsic arithmetic/compare/bitmask instructions with fixed known operand widths; genericmov/copy/lea alone excluded. All original literal texts already actually received; tool adds byte-type evidence, never reading credit.'},indent=2)+'\n')
(P/'operand-typed-dispositions.jsonl.gz').write_bytes(gzip.compress(('\n'.join(json.dumps(r,separators=(',',':')) for r in done)+'\n').encode(),mtime=0));(P/'game-after-operands-occurrences.json').write_text(json.dumps(left,separators=(',',':'))+'\n');v=['%d [%d,%d) @%d %s'%(i,ranges[i]['start'],ranges[i]['end'],ranges[i]['instruction_offset'],ranges[i]['assembly']) for i in sorted(used)];(P/'numeric-operand-type-view.txt').write_text('\n'.join(v)+'\n');print(json.dumps({'all_numeric_operand_ranges':len(ranges),'ranges_used':len(used),'new_numeric_candidates':len(done),'remaining':len(left),'view_lines':len(v)}))
