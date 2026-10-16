"""Check complete inert structural encoding metadata; no Ruby/Marshal or decoded source execution."""
import collections,datetime,json
from pathlib import Path
OUT=Path(__file__).resolve().parent
rows=[]
for filename in ['messages_core.dat.json','Scripts.rxdata.json']:
 doc=json.loads((OUT/'static-recovery-001/current-serialized'/filename).read_text())
 types=collections.Counter(); ivar_shapes=collections.Counter(); symbols=collections.Counter(); strings=0; utf8=0; nonutf8=0; links=0
 def walk(x):
  global strings,utf8,nonutf8,links
  if not isinstance(x,dict) or 'type' not in x:return
  tag=x['type'];types[tag]+=1
  if tag=='I':
   shape=(x['wrapped']['type'],tuple((a['type'],a.get('value'),b['type'],b.get('value')) for a,b in x['ivars']))
   ivar_shapes[shape]+=1
  if tag in [':',';']:symbols[(tag,x['symbol_index'],x['value'])]+=1
  if tag=='"':
   strings+=1;raw=bytes.fromhex(x['bytes_hex']);assert len(raw)==x['byte_length']
   try:decoded=raw.decode('utf8');assert decoded==x['text_utf8'];utf8+=1
   except UnicodeDecodeError:assert x['text_utf8'] is None;nonutf8+=1
  if tag=='@':links+=1
  if 'wrapped' in x:walk(x['wrapped'])
  for a,b in x.get('ivars',[]):walk(a);walk(b)
  for z in x.get('items',[]):walk(z)
  for a,b in x.get('pairs',[]):walk(a);walk(b)
  if 'default' in x:walk(x['default'])
 walk(doc['root'])
 assert dict(types)==doc['summary']['node_counts']
 rows.append({'source':doc['source'],'all_node_types':dict(types),'all_nodes':sum(types.values()),'all_ivar_shape_groups':[{'wrapped_type':shape[0],'complete_metadata_pairs':[list(v) for v in shape[1]],'count':count} for shape,count in ivar_shapes.items()],'all_symbol_groups':[{'type':t,'index':i,'value':v,'count':n} for (t,i,v),n in symbols.items()],'all_string_objects':strings,'all_valid_utf8_strings':utf8,'all_invalid_utf8_raw_strings':nonutf8,'links':links,'parsed_bytes':doc['summary']['parsed_bytes']})
result={'schema':'gr8-full-inert-serialization-metadata/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'complete_artifacts':rows,'target_execution':False,'generation_semantic_credit':0}
(OUT/'serialized-encoding-closure-structure.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
