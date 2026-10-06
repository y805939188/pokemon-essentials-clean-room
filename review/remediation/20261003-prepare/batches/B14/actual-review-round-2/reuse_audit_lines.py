"""New exact document value reuse bookkeeping. Does not execute inspected programs."""
import pathlib,json,subprocess,hashlib
import complete_reader as c
p=pathlib.Path(__file__).parent
m=json.loads((p/'audit-complete-context-map.json').read_text());primary={}
# Every selected whole formal text line has actually been consumed; its complete
# context map proves where it was delivered/reused, not behavior.
f=json.loads((p/'formal-complete-context-map.json').read_text())
for i,inp in enumerate(f['inputs']):
 if inp['role']=='FORMAL_UNFILTERED_HUNK':continue
 for n,line in enumerate(c.show(inp['sha'],inp['path']).decode().splitlines(),1):primary.setdefault(line,{'phase':'formal','input':i,'ordinal':[n],'sha256':c.digest(line)})
# All unique string values of completed semantic phases have been consumed.
done=json.loads((p/'semantic-consumption.json').read_text())
for phase,rec in done.items():
 if phase.startswith('audit') or not isinstance(rec,dict) or not rec.get('semantic_values_actually_consumed'):continue
 cm=json.loads((p/(phase+'-complete-context-map.json')).read_text())
 for x in cm['semantic_pool']:
  if x['type']!='str':continue
  q=x['first_context'];inp=cm['inputs'][q['input']];ord=q['ordinal']
  if inp.get('role')=='FORMAL_UNFILTERED_HUNK':
   lines=subprocess.check_output(['git','diff','--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color',c.BASE,c.ACT,'--',inp['path']]).decode().splitlines();v=lines[ord[0]-1][1:]
   primary.setdefault(v,{'phase':phase,'semantic_id':x['id'],'sha256':x['sha256']});continue
  v=c.show(inp['sha'],inp['path'],inp['sha']==c.REF).decode().splitlines()[ord[0]-1] if q['key']=='literal_line' else c.parsed_json(inp['sha'],inp['path'])
  if q['key']!='literal_line':
   for k in ord:v=list(v.values())[k] if isinstance(v,dict) else v[k]
  primary.setdefault(v,{'phase':phase,'semantic_id':x['id'],'sha256':x['sha256']})
reuses=[];cache={}
for x in m['semantic_pool']:
 if x['type']!='str':continue
 q=x['first_context'];inp=m['inputs'][q['input']];key=inp['sha'],inp['path'];ord=q['ordinal']
 if key not in cache:cache[key]=c.show(*key).decode().splitlines() if q['key']=='literal_line' else c.parsed_json(*key)
 v=cache[key]
 if q['key']=='literal_line':v=v[ord[0]-1]
 else:
  for k in ord:v=list(v.values())[k] if isinstance(v,dict) else v[k]
 options=[(v,{'identity':True})]
 ending='\r\n' if v.endswith('\r\n') else '\n' if v.endswith('\n') else ''
 if ending:options.append((v[:-len(ending)],{'line_ending':ending}))
 if inp['path'].endswith('.diff') and v[:1] in ['+','-',' ']:options.append((v[1:],{'diff_prefix':v[:1]}))
 for val,transform in options:
  if val in primary:
   reuses.append({'semantic_id':x['id'],'type':x['type'],'original_sha256':x['sha256'],'original_context':q,'exact_value_sha256':c.digest(val),'transform':transform,'own_consumed_target':primary[val]});break
(p/'audit-display-exact-reuse.json').write_text(json.dumps({'policy':'Genuinely consumed own exact strings or losslessly decoded literal diff-prefix/terminator values, every original source/context/order retained. Not quality or behavior proof.','reuses':reuses},ensure_ascii=False,separators=(',',':'))+'\n')
print('Additional exact own-consumed audit string reuses',len(reuses))
