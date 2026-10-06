"""Same-task own document/Git/hash/JSON reading bookkeeping. No reviewed code runs."""
import pathlib,sys,subprocess,json,gzip,hashlib,re,collections,csv,io
OUT=pathlib.Path(__file__).parent
ACT='d48197f365c39925f795c1d325988c0d74e59979'
PRE='1e6b11a47370f1c7c4659a32443fc1afda597bac'
ORIG='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed'
C3='c06db6cd964188b3c693a9b7820e3a8aaffe0b04'
BASE='review/remediation/20261003-prepare/batches/B14/'
def git(c,p):return subprocess.check_output(['git','show',c+':'+p])
def h(b):return hashlib.sha256(b).hexdigest()
def vh(v):return h(json.dumps([type(v).__name__,v],ensure_ascii=False,separators=(',',':')).encode())
def gzload(n):return json.loads(gzip.decompress((OUT/n).read_bytes()))
def save(n,o):
 b=(json.dumps(o,ensure_ascii=False,separators=(',',':'))+'\n').encode()
 (OUT/n).write_bytes(gzip.compress(b,mtime=0) if n.endswith('.gz') else b)
def at(o,parts):
 for k in parts:o=o[int(k)] if isinstance(o,list) else o[k]
 return o
def parts(ptr):return [x.replace('~1','/').replace('~0','~') for x in ptr.split('/')[1:]] if ptr else []
def verify_map(n):
 d=gzload(n);vals=[None]*len(d['values']);filled=set();results=[]
 for doc in d['documents']:
  ident=doc['identity'];b=git(ident['commit'],ident['path']);assert h(b)==ident['sha256'] and len(b)==ident['bytes']
  try:o=json.loads(b)
  except ValueError:o={'literal_lines':b.decode().splitlines(keepends=True)}
  if 'projection_to_source' in doc:proj={k:at(o,parts(p)) for k,p in doc['projection_to_source'].items()}
  elif 'projection_adjudications_to_source' in doc:
   proj={k:o[k] for k,_ in doc['structure']['object']};proj['adjudications']=[o['adjudications'][r['source_index']] for r in doc['projection_adjudications_to_source']]
  elif isinstance(o,dict) and 'object' in doc['structure'] and set(k for k,_ in doc['structure']['object']).issubset(o):
   # Earlier own selected-dictionary maps omit a projection descriptor. Verify
   # each selected native object and retain source key order separately; never
   # treat the projection as the complete native document.
   wanted=[k for k,_ in doc['structure']['object']];proj={k:o[k] for k in wanted}
   doc['verified_native_selected_key_order']=[k for k in o if k in wanted]
  else:proj=o
  def walk(node,v):
   if 'value' in node:
    i=node['value'];assert type(v).__name__==node['type'];assert h(json.dumps(v,ensure_ascii=False,separators=(',',':')).encode())==d['values'][i]['canonical_json_sha256']
    if i in filled:assert type(v)==type(vals[i]) and v==vals[i]
    vals[i]=v;filled.add(i);return
   if 'array' in node:
    assert isinstance(v,list) and len(v)==len(node['array'])
    for x,y in zip(node['array'],v):walk(x,y)
   else:
    assert isinstance(v,dict) and list(v)==[k for k,_ in node['object']]
    for k,x in node['object']:walk(x,v[k])
  walk(doc['structure'],proj);results.append({'identity':ident,'projection':doc.get('projection_to_source') or doc.get('projection_adjudications_to_source') or doc.get('verified_native_selected_key_order'),'native_types_order_and_relationships_verified':True})
 assert len(filled)==len(vals)
 return d,vals,results
def scalars(o,p=''):
 if isinstance(o,dict):
  for k,v in o.items():yield from scalars(v,p+'/'+k.replace('~','~0').replace('/','~1'))
 elif isinstance(o,list):
  for i,v in enumerate(o):yield from scalars(v,p+'/'+str(i))
 else:yield p,o
def semantic_derivations(v,steps=()):
 # Whole JSON and whole property-line parsing retains outer type/value hash and
 # transformation/context. Mixed path-plus-prose remains a semantic string.
 if not isinstance(v,str):yield steps,v;return
 s=v.strip()
 if len(steps)<8:
  try:z=json.loads(s) if s.startswith(('{','[')) else None
  except ValueError:z=None
  if z is not None:
   if z!=v or type(z)!=type(v):
    for ptr,a in scalars(z):yield from semantic_derivations(a,steps+(('json',ptr),))
    return
  body=s
  if body[:1] in ('+','-') and not body.startswith(('+++','---')):body=body[1:].lstrip();extra=(('diff_body',''),)
  else:extra=()
  if body.startswith('"'):
   try:
    prop=json.loads('{'+body.rstrip(',')+'}')
   except ValueError:pass
   else:
    if len(prop)==1:
     for ptr,a in scalars(prop):yield from semantic_derivations(a,steps+extra+(('property',ptr),))
     return
 yield steps,v
def derive(v,steps):
 for action,ptr in steps:
  if action=='json':v=at(json.loads(v.strip()),parts(ptr))
  elif action=='diff_body':v=v.strip()[1:].lstrip()
  elif action=='property':v=at(json.loads('{'+v.strip().rstrip(',')+'}'),parts(ptr))
  elif action=='tsv':v=v.rstrip('\r\n').split('\t')[int(ptr)]
  elif action=='tsv_csv':v=next(csv.reader(io.StringIO(v),delimiter='\t'))[int(ptr)]
  elif action=='span':
   a,z=map(int,ptr.split(':'));v=v[a:z]
 return v
def pure(v,ptr,known_paths):
 if isinstance(v,str):
  s=v.strip()
  if s in known_paths:return True
  loc=re.fullmatch(r'(.+):[0-9]+(?:[-–][0-9]+)?',s)
  if loc and loc.group(1) in known_paths:return True
  if ptr.endswith('/value_id') and re.fullmatch(r'(?:previous|owner):(?:[0-9a-f]{64}|[0-9]+)',s):return True
  if (ptr.endswith(('/pointer','/selector','/json_pointer')) or re.search(r'/selected_objects/\d+$',ptr)) and re.fullmatch(r'[A-Za-z0-9_~.:-]+(?:/[A-Za-z0-9_~.:-]+)+',s):return True
  if re.search(r'/(?:structure|structures|containers|structural_nodes|native_structure|nodes)/\d+/(?:children|keys|fields)/\d+$',ptr) and re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*',s):return True
  if re.fullmatch(r'https?://\S+',s):return True
  if ';' in s and all(x in known_paths or re.fullmatch(r'(?:WP\d+(?:-[A-Z])?|F\d+-\d+)',x) for x in s.split(';')):return True
  if re.fullmatch(r'[A-Za-z0-9_.-]+\.json#[A-Z0-9-]+',s):return True
  if s in {'dict','list','str','int','float','bool','NoneType','object','array','scalar','key','value','empty_object','empty_array'}:return True
  if re.fullmatch(r'[0-9a-f]{8,64}|[0-9a-f-]{36}',s):return True
  if re.match(r'^[0-9a-f]{40}:',s) and not re.search(r'[\s\u4e00-\u9fff]',s):return True
  if not re.search(r'[\s\u4e00-\u9fff→]',s):
   if re.match(r'^(?:[0-9a-f]{8,40}|original|ORIG|PLAN|acceptance|plan|finding|control|candidate|evidence|actual|snapshot|report|text|root|source|formal|formal_diff|read_[a-z_]+|B\d+-[A-Z0-9-]+|GIR-FD82-[A-Z0-9-]+|WP80-[A-Z0-9-]+)(?:/|:)\S+$',s):return True
  if re.fullmatch(r'(?:GIR-FD82-|WP80-|RUN-|R-B\d+|B14-|B\d+/GIR-)[A-Z0-9_/.-]+',s):return True
  if re.fullmatch(r'(?:MP|MV|EV|IM|MR|DG|FW|WT|FS|FP|BP|GR|F)\d+[A-Z0-9_.-]*',s):return True
  if re.fullmatch(r'(?:[0-9]+[-–,:;/ ]*)+',s):return True
  # Exact structural selectors/hashes/identities, never arbitrary path prefixes.
  if re.fullmatch(r'/[A-Za-z0-9_~./:-]*',s):return True
  if s.startswith(('review/','specs/','deliverables/','Data/','PBS/','planning/','audit/','reference/')):
   if re.fullmatch(r'[A-Za-z0-9_./()#~-]+',s) and not any(x in s for x in [';','=', '→']):return True
  return False
 # Numbers/booleans/null are retained with every native context. Display any
 # value with a behavioral rather than purely identity/counter context.
 if re.search(r'/(?:value_index|value_indices|remaining_unique_value_indices|unique_value_indices|bytes|byte_count|lines|line_count)(?:/.*)?$',ptr):return True
 return not bool(re.search(r'(?:expected|fixture|premise|input|initial|final|state|result|sample|life|opacity|moisture|growth|through|outdoor|shading|faint|selection|registration)',ptr,re.I))
def init():
 snapshot=json.loads((OUT/'preliminary-turn-1/snapshot-manifest.json').read_text())
 for r in snapshot['files']:
  b=(OUT/'preliminary-turn-1'/r['path']).read_bytes();assert h(b)==r['sha256'] and len(b)==r['bytes']
 verified=[];seeds={};maps={}
 for n in ['actual-gate-lossless-map.json.gz','owner-shared-primary-lossless-map.json.gz','gate-primary-lossless-map.json.gz','primary-controls-lossless-map.json.gz','deferred-audit-lossless-map.json.gz']:
  d,v,r=verify_map(n);maps[n]=(d,v);verified.append({'map':n,'compressed_sha256':h((OUT/n).read_bytes()),'documents':r,'all_native_scalar_types_values_and_relationships_verified':True,'semantic_reading_not_implied':True})
 save('completion-cache-reconstruction.json.gz',verified)
 prior=json.loads((OUT/'preliminary-turn-1/reading-log.json').read_text())
 for n,ids in [('owner-shared-primary-lossless-map.json.gz',json.loads((OUT/'owner-shared-prose-index.json').read_text())),('gate-primary-lossless-map.json.gz',range(116)),('actual-gate-lossless-map.json.gz',None)]:
  d,v=maps[n]
  if ids is None:ids=[i for i,a in enumerate(v) if isinstance(a,str) and re.search(r'\s',a)]
  for i in ids:seeds[vh(v[i])]={'kind':'genuinely_consumed_initial_value','map':n,'value':i,'initial_reading_log_sha256':h((OUT/'preliminary-turn-1/reading-log.json').read_bytes())}
 f=json.loads((OUT/'formal-diff-exact-map.json').read_text())
 for g in f['groups']:
  b=subprocess.check_output(['git','diff','--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color',PRE,ACT,'--',g['path']]);assert h(b)==g['sha256'];assert b.decode()==''.join(f['values'][r['value']] for r in g['records'])
 for i,a in enumerate(f['values']):
  for _,v in semantic_derivations(a):seeds[vh(v)]={'kind':'consumed_initial_formal_diff','value':i,'map':'formal-diff-exact-map.json'}
 docs=[];keyset=set()
 def add(c,p,sel=None):
  key=(c,p,json.dumps(sel,sort_keys=True))
  if key in keyset:return
  keyset.add(key);b=git(c,p)
  try:full=json.loads(b);o=full;kind='JSON'
  except ValueError:full={'literal_lines':b.decode().splitlines(keepends=True)};o=full;kind='TEXT_LINES_KEEPENDS'
  if sel is not None:o={s:at(full,parts(s)) for s in sel}
  docs.append({'commit':c,'path':p,'sha256':h(b),'bytes':len(b),'kind':kind,'selection':sel,'object':o})
 inv=json.loads((OUT/'diff-capture-and-inventory.json').read_text())
 for g in inv['streams'][0]['path_hunk_inventory']:add(ACT,g['header'].split(' b/',1)[1])
 old=json.loads(git(PRE,'review/remediation/20261003-prepare/batches/B03/integration-stage-1/finding-registration.json'))
 now=json.loads(git(ACT,BASE+'integration-stage-1/finding-registration.json'));ids=set(r['id'] for r in old['dispositions'])|set(r['id'] for r in now['dispositions'])
 full=json.loads(git(ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json'));selectors=['/'+str(i) for i,x in enumerate(full) if x['id'] in ids]
 add(ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json',selectors)
 add(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json',['/'+i for i in sorted(ids)])
 for n in ['root/adjudication-log.json','root/extension-adjudications.json']:
  p='review/global-independent-review/2026-10-03-fd82a639/'+n;o=json.loads(git(ORIG,p));sels=['/'+k for k in o if k!='adjudications']+['/adjudications/'+str(i) for i,r in enumerate(o['adjudications']) if any(x in json.dumps(r,ensure_ascii=False) for x in ids)];add(ORIG,p,sels)
 for n in ['integration-stage-1/finding-registration.json','integration-stage-1/integration-manifest.json','integration-stage-1/downstream-interface-investigation.json','acceptance-stage-1/acceptance-manifest.json','acceptance-stage-1/downstream-handshake.json','integration-review-1/report.md','integration-review-1/finding-dispositions.json','integration-review-1/regression-review.json']:
  add(PRE,'review/remediation/20261003-prepare/batches/B03/'+n)
 for n in ['report-corrections-successor.json','B14-downstream-contract.json']:
  add(PRE,'review/remediation/20261003-prepare/batches/B09/acceptance-stage-1/'+n)
 for p in subprocess.check_output(['git','ls-tree','-r','--name-only',ACT,'specs/overworld','deliverables/final-specification-set/engine-overworld']).decode().splitlines():
  if re.search(r'/wp1[1-4]-',p):add(ACT,p)
 # All12 changed formal files are complete current bodies, not only changed hunks.
 for p in json.loads(git(ACT,BASE+'integration-stage-1/boundary-and-bindings.json'))['formal_paths']:add(ACT,p)
 add(ACT,'deliverables/final-specification-set/combat-requirements/wp39-battle-context-and-participants.md')
 # Actual role's complete reader set and frozen original/PLAN controls, with
 # exact external bindings. Additional required readers are added as discovered.
 gate=json.loads(git(ACT,BASE+'integration-stage-1/actual-request-B03.json'))
 for r in gate['full_original_controls']['current_owner_controls']['accepted_owner_control_inputs']:add(r['commit'],r['path'])
 known_paths=set()
 for c in [ACT,ORIG,PLAN,PRE]:known_paths.update(subprocess.check_output(['git','ls-tree','-r','--name-only',c]).decode().splitlines())
 # Genuine whole initial literal/JSON bodies listed as consumed, exactly bound.
 consumed=prior['deferred_literal_complete_reads']+prior['public_diff_complete_reads']
 for p in consumed:
  b=git(ACT,p)
  try:o=json.loads(b)
  except ValueError:o={'literal_lines':b.decode().splitlines(keepends=True)}
  for ptr,a in scalars(o):
   for _,v in semantic_derivations(a):seeds[vh(v)]={'kind':'consumed_initial_whole_body','commit':ACT,'path':p,'selector':ptr}
 add(PRE,'review/remediation/20261003-prepare/batches/B09/acceptance-stage-1/report-corrections-successor.json')
 for ptr,a in scalars(json.loads(git(PRE,'review/remediation/20261003-prepare/batches/B09/acceptance-stage-1/report-corrections-successor.json'))):
  for _,v in semantic_derivations(a):seeds[vh(v)]={'kind':'consumed_initial_accepted_B09_corrections','commit':PRE,'selector':ptr}
 claims=[];lookup={};occurrences=[];programs=[]
 for di,d in enumerate(docs):
  if d['path'].endswith('.py'):programs.append(di)
  for ptr,a in scalars(d['object']):
   for steps,v in semantic_derivations(a):
    k=vh(v);ref={'document':di,'selector':ptr,'steps':steps,'native_type':type(a).__name__,'native_value_sha256':vh(a)}
    if k not in lookup:
     lookup[k]=len(claims);claims.append({'value_sha256':k,'type':type(v).__name__,'first':ref,'metadata_only':pure(v,ptr,known_paths),'prior_consumed':seeds.get(k),'length':len(str(v))})
    occurrences.append([lookup[k],di,ptr,steps,type(a).__name__,vh(a)])
  d.pop('object')
 index={'documents':docs,'claims':claims,'occurrences':occurrences,'program_documents':programs,'native_graph_policy':'Original Git byte identity plus native JSON/text order/types/selectors and exact nested-string transformations, with all occurrence relationships retained. Metadata verification is not semantic reading.','snapshot_manifest_sha256':h((OUT/'preliminary-turn-1/snapshot-manifest.json').read_bytes())}
 save('completion-reading-index.json.gz',index)
 pending=[i for i,c in enumerate(claims) if not c['metadata_only'] and not c['prior_consumed']]
 save('completion-pending-claims.json',pending);save('completion-consumption.json',{'read_claims':[],'batches':[],'literal_programs_read':[],'complete':False})
 print('documents',len(docs),'unique claims',len(claims),'occurrences',len(occurrences),'pending semantic claims',len(pending),'pending chars',sum(claims[i]['length'] for i in pending),'programs',len(programs))
def native(d,selector):
 b=git(d['commit'],d['path']);assert h(b)==d['sha256']
 try:o=json.loads(b)
 except ValueError:o={'literal_lines':b.decode().splitlines(keepends=True)}
 if d['selection'] is not None:o={s:at(o,parts(s)) for s in d['selection']}
 return at(o,parts(selector))
def batch(a,z):
 idx=gzload('completion-reading-index.json.gz');pending=json.loads((OUT/'completion-pending-claims.json').read_text());cache={};printed=[]
 print('PENDING POSITIONS',a,z,'TOTAL',len(pending))
 for n in range(a,min(z,len(pending))):
  i=pending[n];c=idx['claims'][i];ref=c['first'];di=ref['document'];d=idx['documents'][di]
  if di not in cache:
   b=git(d['commit'],d['path']);assert h(b)==d['sha256']
   try:o=json.loads(b)
   except ValueError:o={'literal_lines':b.decode().splitlines(keepends=True)}
   if d['selection'] is not None:o={s:at(o,parts(s)) for s in d['selection']}
   cache[di]=o
  v=at(cache[di],parts(ref['selector']));assert vh(v)==ref['native_value_sha256'];v=derive(v,ref['steps']);assert vh(v)==c['value_sha256']
  print(n,'C'+str(i),'D'+str(di),ref['selector'],json.dumps(v,ensure_ascii=False));printed.append(i)
 save('completion-last-display.json',{'pending_start':a,'pending_end':min(z,len(pending)),'claims':printed,'output_truncation_must_be_checked_before_ack':True})
def ack(a,z):
 idx=gzload('completion-reading-index.json.gz');pending=json.loads((OUT/'completion-pending-claims.json').read_text());o=json.loads((OUT/'completion-consumption.json').read_text());o['read_claims']=sorted(set(o['read_claims'])|set(pending[a:z]));o['batches'].append({'pending_positions':[a,z-1],'claim_count':z-a,'acknowledged_after_model_consumption':True});save('completion-consumption.json',o);print('acknowledged',a,z)
if __name__=='__main__':
 if sys.argv[1]=='init':init()
 elif sys.argv[1]=='batch':batch(int(sys.argv[2]),int(sys.argv[3]))
 elif sys.argv[1]=='ack':ack(int(sys.argv[2]),int(sys.argv[3]))
 elif sys.argv[1]=='inventory':
  d=gzload('completion-reading-index.json.gz')
  for i,x in enumerate(d['documents']):print(i,x['commit'][:8],x['path'],('SELECTION '+str(len(x['selection']))) if x['selection'] else 'WHOLE')
 elif sys.argv[1]=='reclassify':
  idx=gzload('completion-reading-index.json.gz');known=set()
  for c in [ACT,ORIG,PLAN,PRE]:known.update(subprocess.check_output(['git','ls-tree','-r','--name-only',c]).decode().splitlines())
  cache={}
  for c in idx['claims']:
   if c['metadata_only']:continue
   r=c['first'];di=r['document'];d=idx['documents'][di]
   if di not in cache:
    b=git(d['commit'],d['path']);assert h(b)==d['sha256']
    try:o=json.loads(b)
    except ValueError:o={'literal_lines':b.decode().splitlines(keepends=True)}
    if d['selection'] is not None:o={s:at(o,parts(s)) for s in d['selection']}
    cache[di]=o
   v=derive(at(cache[di],parts(r['selector'])),r['steps']);assert vh(v)==c['value_sha256'];c['metadata_only']=pure(v,r['selector'],known)
  save('completion-reading-index.json.gz',idx);pending=[i for i,c in enumerate(idx['claims']) if not c['metadata_only'] and not c['prior_consumed']];save('completion-pending-claims.json',pending)
  print('pending',len(pending),'chars',sum(idx['claims'][i]['length'] for i in pending))
 elif sys.argv[1]=='refine_tsv':
  idx=gzload('completion-reading-index.json.gz');old=idx['claims'];lookup={c['value_sha256']:i for i,c in enumerate(old)};cache={};new_occ=[];superseded=[]
  for i,c in enumerate(list(old)):
   r=c['first'];di=r['document'];d=idx['documents'][di]
   if not d['path'].endswith('.tsv') or r['steps'] or not r['selector'].startswith('/literal_lines/'):continue
   if di not in cache:
    b=git(d['commit'],d['path']);assert h(b)==d['sha256'];cache[di]=b.decode().splitlines(keepends=True)
   line=cache[di][int(r['selector'].rsplit('/',1)[1])]
   if '\t' not in line:continue
   count=len(line.rstrip('\r\n').split('\t'));header=cache[di][0].rstrip('\r\n').split('\t');assert count==len(header)
   superseded.append(i);c['decomposed_native_TSV_columns']=[]
   for col,raw in enumerate(line.rstrip('\r\n').split('\t')):
    for sub,v in semantic_derivations(raw):
     steps=[('tsv',str(col))]+list(sub);k=vh(v);ref={**r,'steps':steps,'column_name':header[col]}
     if k not in lookup:
      lookup[k]=len(old);old.append({'value_sha256':k,'type':type(v).__name__,'first':ref,'metadata_only':pure(v,r['selector']+'/'+header[col],set()),'prior_consumed':None,'length':len(str(v))})
     j=lookup[k];c['decomposed_native_TSV_columns'].append([col,j]);new_occ.append([j,di,r['selector'],steps,'str',vh(line)])
   c['metadata_only']=True;c['decomposition_policy']='Full native tab-separated row, header/column order/terminator retained at fixed Git identity; all column semantic values and relationships retained. Not omitted.'
  idx['occurrences']+=new_occ;save('completion-reading-index.json.gz',idx);pending=[i for i,c in enumerate(old) if not c['metadata_only'] and not c['prior_consumed']];save('completion-pending-claims.json',pending)
  print('TSV rows decomposed',len(superseded),'pending',len(pending),'chars',sum(old[i]['length'] for i in pending))
 elif sys.argv[1]=='refine_sentences':
  idx=gzload('completion-reading-index.json.gz');claims=idx['claims'];lookup={c['value_sha256']:i for i,c in enumerate(claims)};cache={};added=[];sup=[]
  consumed=set(json.loads((OUT/'completion-consumption.json').read_text())['read_claims'])
  for i,c in enumerate(list(claims)):
   if c['metadata_only'] or c['type']!='str' or c['length']<180:continue
   r=c['first'];di=r['document'];d=idx['documents'][di]
   if d['path'].endswith('.py'):continue # historical code is read literally
   if di not in cache:
    b=git(d['commit'],d['path']);assert h(b)==d['sha256']
    try:o=json.loads(b)
    except ValueError:o={'literal_lines':b.decode().splitlines(keepends=True)}
    if d['selection'] is not None:o={s:at(o,parts(s)) for s in d['selection']}
    cache[di]=o
   v=derive(at(cache[di],parts(r['selector'])),r['steps']);assert vh(v)==c['value_sha256']
   cuts=[0]+[m.end() for m in re.finditer(r'。|；|(?<=[.!?])\s+|\n',v)]+[len(v)];cuts=sorted(set(cuts))
   if len(cuts)<3:continue
   relations=[]
   for a,z in zip(cuts,cuts[1:]):
    if a==z:continue
    body=v[a:z];k=vh(body);steps=list(r['steps'])+[('span',str(a)+':'+str(z))];ref={**r,'steps':steps}
    if k not in lookup:
     lookup[k]=len(claims);claims.append({'value_sha256':k,'type':'str','first':ref,'metadata_only':pure(body,r['selector'],set()),'prior_consumed':c['prior_consumed'] or ({'kind':'same_task_consumed_parent','parent_claim':i} if i in consumed else None),'length':len(body)})
    j=lookup[k]
    if (c['prior_consumed'] or i in consumed) and not claims[j]['prior_consumed']:claims[j]['prior_consumed']=c['prior_consumed'] or {'kind':'same_task_consumed_parent','parent_claim':i}
    relations.append([a,z,j]);added.append([j,di,r['selector'],steps,r['native_type'],r['native_value_sha256']])
   assert ''.join(v[a:z] for a,z,_ in relations)==v
   c['exact_ordered_sentence_spans']=relations;c['metadata_only']=True;c['decomposition_policy']='Every exact substring, punctuation, separator, original parent value/type/context and ordered concatenation is retained. No prose omitted; child semantic claims require reading unless genuinely consumed in an exact parent body.';sup.append(i)
  idx['occurrences']+=added;save('completion-reading-index.json.gz',idx);pending=[i for i,c in enumerate(claims) if not c['metadata_only'] and not c['prior_consumed']];save('completion-pending-claims.json',pending)
  print('parents losslessly decomposed',len(sup),'pending',len(pending),'chars',sum(claims[i]['length'] for i in pending))
 elif sys.argv[1]=='refine_tsv_quoted':
  idx=gzload('completion-reading-index.json.gz');claims=idx['claims'];lookup={c['value_sha256']:i for i,c in enumerate(claims)};extra=[];sup=[];cache={}
  for i,c in enumerate(list(claims)):
   r=c['first'];di=r['document'];d=idx['documents'][di]
   if not d['path'].endswith('.tsv') or not r['steps'] or r['steps'][0][0]!='tsv':continue
   # Replace prior raw-column derived interpretation with exact CSV decoding.
   if di not in cache:
    b=git(d['commit'],d['path']);assert h(b)==d['sha256'];cache[di]=b.decode().splitlines(keepends=True)
   line=cache[di][int(r['selector'].rsplit('/',1)[1])];col=int(r['steps'][0][1]);cells=next(csv.reader(io.StringIO(line),delimiter='\t'));raw=cells[col]
   c['exact_CSV_column_children']=[]
   for sub,v in semantic_derivations(raw):
    steps=[('tsv_csv',str(col))]+list(sub);k=vh(v);ref={**r,'steps':steps}
    if k not in lookup:
     lookup[k]=len(claims);claims.append({'value_sha256':k,'type':type(v).__name__,'first':ref,'metadata_only':pure(v,r['selector']+'/'+r.get('column_name',''),set()),'prior_consumed':None,'length':len(str(v))})
    j=lookup[k];c['exact_CSV_column_children'].append(j);extra.append([j,di,r['selector'],steps,'str',vh(line)])
   c['metadata_only']=True;c['decomposition_policy']='Raw TSV lexical columns retained; exact csv.reader decoding plus nested JSON children now carries semantic meaning. No string or quote discarded.';sup.append(i)
  idx['occurrences']+=extra;save('completion-reading-index.json.gz',idx);pending=[i for i,c in enumerate(claims) if not c['metadata_only'] and not c['prior_consumed']];save('completion-pending-claims.json',pending)
  print('CSV columns decoded',len(sup),'pending',len(pending),'chars',sum(claims[i]['length'] for i in pending))
 elif sys.argv[1]=='reuse_exact_bodies':
  idx=gzload('completion-reading-index.json.gz');claims=idx['claims'];done=set(json.loads((OUT/'completion-consumption.json').read_text())['read_claims']);cache={}
  def val(c):
   r=c['first'];di=r['document'];d=idx['documents'][di]
   if di not in cache:
    b=git(d['commit'],d['path']);assert h(b)==d['sha256']
    try:o=json.loads(b)
    except ValueError:o={'literal_lines':b.decode().splitlines(keepends=True)}
    if d['selection'] is not None:o={s:at(o,parts(s)) for s in d['selection']}
    cache[di]=o
   v=derive(at(cache[di],parts(r['selector'])),r['steps']);assert vh(v)==c['value_sha256'];return v
  bodies=[]
  for i,c in enumerate(claims):
   if c['type']=='str' and (c['prior_consumed'] or i in done) and c['length']>=20:bodies.append((i,val(c)))
  gram=collections.defaultdict(list)
  for i,b in bodies:
   for g in set(b[j:j+20] for j in range(max(0,len(b)-19))):gram[g].append((i,b))
  reused=[]
  for i,c in enumerate(claims):
   if c['metadata_only'] or c['prior_consumed'] or i in done or c['type']!='str' or c['length']<20:continue
   v=val(c)
   for parent,b in gram.get(v[:20],[]):
    start=b.find(v)
    if start>=0:
     c['prior_consumed']={'kind':'exact_body_substring_already_consumed','parent_claim':parent,'exact_span':[start,start+len(v)],'type':'str','parent_value_sha256':claims[parent]['value_sha256'],'context_not_quality_transfer':True};reused.append(i);break
  save('completion-reading-index.json.gz',idx);pending=[i for i,c in enumerate(claims) if not c['metadata_only'] and not c['prior_consumed']];save('completion-pending-claims.json',pending)
  print('genuine exact body reuse',len(reused),'pending',len(pending),'chars',sum(claims[i]['length'] for i in pending))
 elif sys.argv[1]=='scope_public_history':
  idx=gzload('completion-reading-index.json.gz');owner=json.loads(git(PRE,'review/remediation/20261003-prepare/batches/B03/integration-stage-1/finding-registration.json'));owner_ids={r['id'] for r in owner['dispositions']};decisions={}
  inv=json.loads((OUT/'diff-capture-and-inventory.json').read_text())
  changed={}
  for g in inv['streams'][0]['path_hunk_inventory']:
   p=g['header'].split(' b/',1)[1];lines=set()
   for hh in g['hunks']:
    m=re.search(r'\+(\d+)(?:,(\d+))?',hh);start=int(m[1]);count=int(m[2] or 1);lines.update(range(start,start+count))
   changed[p]=lines
  for di,d in enumerate(idx['documents']):
   if d['commit']!=ACT or d['path'].startswith(BASE):continue
   if d['path'].endswith(('approval-ledger.tsv','traceability-successor.tsv')):
    b=git(ACT,d['path']);oldb=git(PRE,d['path']);assert b.splitlines(keepends=True)[:171]==oldb.splitlines(keepends=True);rows=b.decode().splitlines(keepends=True);active={0}|set(range(171,len(rows)))
    for n,line in enumerate(rows[1:171],1):
     if next(csv.reader(io.StringIO(line),delimiter='\t'))[0] in owner_ids:active.add(n)
    decisions[di]={'path':d['path'],'active_native_line_indexes':sorted(active),'unrelated_accepted_rows':'Exact preserved native/schema/column/order/terminator identities and relationships; unrelated business-domain quality is not reapproved. All current24 and accepted B03 rows semantically active.'}
   elif d['path']=='audit/source-traceability.md':
    b=git(ACT,d['path']);ob=git(PRE,d['path']);assert b.startswith(ob);lines=b.decode().splitlines(keepends=True);active={n-1 for n in changed[d['path']]};active.update(range(0,90));in_owner=False
    for n,line in enumerate(lines):
     if line.startswith('### T-WP'):in_owner=bool(re.match(r'### T-WP1[1-4]-',line))
     if in_owner:active.add(n)
    decisions[di]={'path':d['path'],'active_native_line_indexes':sorted(active),'unrelated_accepted_history':'Full unchanged predecessor prefix is retained exactly; its unrelated domain history is preserved, not reapproved. Every unfiltered changed hunk/context and relevant current/accepted B03 navigation remains active.'}
  active_claims=set();outside=[]
  for occ in idx['occurrences']:
   ci,di,ptr=occ[:3]
   if di not in decisions:active_claims.add(ci);continue
   m=re.match(r'/literal_lines/(\d+)',ptr)
   if not m or int(m[1]) in decisions[di]['active_native_line_indexes']:active_claims.add(ci)
  for i,c in enumerate(idx['claims']):
   if i not in active_claims and not c['metadata_only']:
    c['preserved_unrelated_accepted_history']=True;c['metadata_only']=True;outside.append(i)
  idx['public_preservation_scope']=decisions;save('completion-reading-index.json.gz',idx);save('completion-public-preservation-scope.json',{'decisions':decisions,'pure_preservation_claims':outside,'no_changed_file_or_hunk_excluded':True,'no_automatic_NOT_AFFECTED_or_old_PASS_transfer':True})
  pending=[i for i,c in enumerate(idx['claims']) if not c['metadata_only'] and not c['prior_consumed']];save('completion-pending-claims.json',pending);print('unrelated immutable history clauses',len(outside),'pending',len(pending),'chars',sum(idx['claims'][i]['length'] for i in pending))
