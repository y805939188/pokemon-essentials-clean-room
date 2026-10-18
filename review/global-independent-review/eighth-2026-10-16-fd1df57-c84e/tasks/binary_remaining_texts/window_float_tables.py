"""Exact linked float windows proven by full native pointer selector/multiplier."""
import pathlib,json,struct,hashlib,math,gzip
ROOT=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes();slot=11842688
ptrs=json.loads((ROOT/'game-relocation-pointers.json').read_text())['entries'];rel={r['slot_offset']:r for r in ptrs};windows=[]
for i in range(8):
 p=slot+8*i;r=rel[p];start=r['target']['file_offset'];n=32<<i;end=start+n*4;assert end<=11875392
 vals=struct.unpack_from('<'+'f'*n,b,start);assert all(math.isfinite(v) and 0<v<=1 for v in vals);assert list(vals)==sorted(vals)
 windows.append({'index':i,'pointer_slot':p,'start':start,'end':end,'float_count':n,'element_bytes':4,'sha256':hashlib.sha256(b[start:end]).hexdigest(),'first':vals[0],'last':vals[-1],'all_finite_unit_interval':True,'nondecreasing':True})
ordered=sorted(windows,key=lambda r:r['start']);assert ordered[0]['start']==11842752 and ordered[-1]['end']==11875392;assert all(a['end']==z['start'] for a,z in zip(ordered,ordered[1:]))
ev={'pointer_table_start':slot,'pointer_table_end':slot+64,'windows':windows,'read_native_consumers':['native-6625280.stdout','native-6625296.stdout'],'proof':'Eight genuine DIR64 pointers select completefloat32 windows; full nativeconsumer indexes pointertable atscale8, then loads/multiplies coefficients asfloat32 scalar/SIMD inforward/reversewindowsegments. Adjacentlengths32through4096exactlytile11842752–11875392; every coefficient finiteandnondecreasing withinunitinterval. No audiooperationexecuted.','qualification':'Exact numeric byte type only, not decoder equivalence or finalaudio.'}
(ROOT/'window-float-table-evidence.json').write_text(json.dumps(ev,indent=2)+'\n');rows=json.loads((ROOT/'game-after-hrtf-occurrences.json').read_text());done=[];left=[]
for row in rows:
 hits=[w for w in windows if w['start']<=row['start'] and row['end_exclusive']<=w['end']]
 if hits:done.append(dict(row,semantic_status='INVENTORY_ONLY_TYPED',type_evidence={'kind':'FLOAT32_AUDIO_WINDOW_COEFFICIENTS','evidence':'window-float-table-evidence.json','window':hits[0]['index'],'start':hits[0]['start'],'end':hits[0]['end'],'reason':'Exact linkedfloat32coefficientarray; fullselector/multiplicationconsumerread; binaryASCII subrunnotatextmessage.'}))
 else:left.append(row)
(ROOT/'float-typed-dispositions.jsonl.gz').write_bytes(gzip.compress(('\n'.join(json.dumps(r,separators=(',',':')) for r in done)+'\n').encode(),mtime=0));(ROOT/'game-after-float-occurrences.json').write_text(json.dumps(left,separators=(',',':'))+'\n');print(json.dumps({'windows':windows,'newly_typed':len(done),'remaining_occurrences':len(left)}))
