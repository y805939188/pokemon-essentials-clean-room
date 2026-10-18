"""Restore complete finite built-in table selected by read native function."""
import pathlib,json,struct,hashlib,collections
ROOT=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes();secs=json.loads((ROOT/'pe-sections.json').read_text())['Game.exe']['sections'];base=5368709120
def off(v):
 for s in secs:
  if s['rva']<=v-base<s['rva']+s['bytes']:return v-base-s['rva']+s['offset']
 raise ValueError(hex(v))
def sha(x):return hashlib.sha256(x).hexdigest()
starts=[(None,11551680)];p=11619560
while True:
 v=struct.unpack_from('<Q',b,p)[0]
 if not v:break
 starts.append((p,off(v)));p+=8;assert len(starts)<4096
records=[];patterns=collections.defaultdict(list);names=collections.defaultdict(list)
for i,(ptr,s) in enumerate(starts):
 e=b.index(b'\0',s);raw=b[s:e];text=raw.decode('ascii');fields=text.split(',');guid,name=fields[:2];kv=[]
 for fld in fields[2:]:
  if not fld:continue
  k,sep,v=fld.partition(':');assert sep;kv.append((k,v))
 row={'record':i,'pointer_slot':ptr,'start':s,'end':e,'sha256':sha(raw),'guid':guid,'name':name,'ordered_fields':kv,'raw_text':text};records.append(row);patterns[tuple(kv)].append(i);names[name].append(i)
patrows=[{'pattern':i,'records':ids,'ordered_fields':list(kv)} for i,(kv,ids) in enumerate(patterns.items())]
evidence={'source':'Game.exe','pointer_table_start':11619560,'pointer_table_end_with_null':p+8,'pointer_table_sha256':sha(b[11619560:p+8]),'hardcoded_first_record':11551680,'records':records,'patterns':patrows,'names':[{'name':n,'records':ids} for n,ids in names.items()],'native_consumer':'native-3879264.stdout','qualification':'Complete current built-in table, separate from prior442647byte external table. Memory identity and ordered field restoration only until actual reader receivesviews; registration outcome/platformselection/priorityandgamebridge separate.'}
(ROOT/'builtin-controller-readset.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
view=['P'+str(r['pattern'])+' records='+','.join(map(str,r['records']))+' '+','.join(k+':'+v for k,v in r['ordered_fields']) for r in patrows]
(ROOT/'builtin-controller-pattern-view.txt').write_text('\n'.join(view)+'\n');(ROOT/'builtin-controller-name-view.txt').write_text('\n'.join(str(i)+' records='+','.join(map(str,ids))+' '+n for i,(n,ids) in enumerate(names.items()))+'\n')
print(json.dumps({'records':len(records),'patterns':len(patrows),'names':len(names),'keys':sorted({k for r in records for k,v in r['ordered_fields']}),'ptr_start':11619560,'ptr_end':p+8,'first':records[0],'last':records[-1]},ensure_ascii=False))
