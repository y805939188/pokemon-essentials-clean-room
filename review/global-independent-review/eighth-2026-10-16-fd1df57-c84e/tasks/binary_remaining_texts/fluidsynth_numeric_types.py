"""Exact double ranges from actually received native numeric consumers."""
import pathlib,json,struct,hashlib,gzip,math
P=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes()
defs=[
 ('cent_remainder_double_table',13430112,1200,'native-8342416.stdout','complete function; unsigned integer quotient/remainder by1200 and scale8mulsd; no claim for arbitrary nonfinite/outofrange input'),
 ('attenuation_double_table',13418560,1441,'native-8342640.stdout;native-8343216.stdout','complete functions; ordinary finite0<=input<1441, conversion to index, scale8movsd'),
 ('concave_double_table',13417536,128,'native-8343344.stdout','complete function; finite0<=input<128 scale8movsd'),
 ('convex_double_table',13416512,128,'native-8343408.stdout','complete function; finite0<=input<128 scale8movsd'),
 ('pan_proven_indexed_subrange',13408488,999,'native-8343120.stdout','complete function; finite -500<input<500, truncation+500 index1..999. Unreferenced arraytail/firstentry deliberately not included'),
 ('linear_interpolation_double_matrix',13467840,256*2,'native-8382704.stdout lines1–110','local typed proof only:32bitfraction >>24 gives0..255, rowstride16, mulsd offsets0/8; restfunctionnotfullyread'),
 ('cubic_interpolation_double_matrix',13459648,256*4,'native-8383632.stdout.assembly-view.txt lines65–155','local typed proof only:32bitfraction >>24 gives0..255, rowstride32, double offsets0/8/16/24; complete nativeCFGnotread'),
 ('sinc_interpolation_double_matrix',13445312,256*7,'native-8385952.stdout.assembly-view.txt lines65–155','local typed proof only:32bitfraction >>24 gives0..255, rowstride(8*i-i)*8=56, double offsets0/8/16/24/32/40/48; complete nativeCFGnotread')]
ranges=[]
for name,s,n,source,reason in defs:
 raw=b[s:s+n*8];v=struct.unpack('<'+'d'*n,raw);assert all(math.isfinite(x) for x in v);ranges.append({'kind':'PROVEN_NUMERIC_DOUBLE_BYTES','name':name,'start':s,'end':s+n*8,'elements':n,'element_bytes':8,'sha256':hashlib.sha256(raw).hexdigest(),'min':min(v),'max':max(v),'source':source,'reason':reason})
e={'ranges':ranges,'supplemental_schema_files':['fluidsynth-type-reference/gen_conv.c','fluidsynth-type-reference/fluid_conv.c','fluidsynth-type-reference/fluid_conv_tables.h','fluidsynth-type-reference/gen_rvoice_dsp.c'],'qualification':'Numeric byte type only, exact referenced table or matrix range; no audio hearing/selection/FluidSynth wholeprogram equivalence. Supplemental C source read but neither compiled nor executed; no synthesis vectors run.'};(P/'fluidsynth-numeric-type-evidence.json').write_text(json.dumps(e,indent=2)+'\n')
u=json.loads((P/'game-after-iconv-occurrences.json').read_text());done=[];left=[]
for row in u:
 s,z=row['start'],row['end_exclusive'];hits=[r for r in ranges if r['start']<z and s<r['end']];pos=s
 for a,c in sorted((max(s,r['start']),min(z,r['end'])) for r in hits):
  if a>pos:break
  pos=max(pos,c)
 if pos>=z:done.append(dict(row,semantic_status='INVENTORY_ONLY_TYPED',type_evidence={'kind':'PROVEN_NUMERIC_DOUBLE_BYTES','evidence':'fluidsynth-numeric-type-evidence.json','ranges':hits}))
 else:left.append(row)
(P/'fluidsynth-typed-dispositions.jsonl.gz').write_bytes(gzip.compress(('\n'.join(json.dumps(r,separators=(',',':')) for r in done)+'\n').encode(),mtime=0));(P/'game-after-fluidsynth-occurrences.json').write_text(json.dumps(left,separators=(',',':'))+'\n');print(json.dumps({'ranges':ranges,'new_numeric_candidates':len(done),'remaining_candidates':len(left)}))
