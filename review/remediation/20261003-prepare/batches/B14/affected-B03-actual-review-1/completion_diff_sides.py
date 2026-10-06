"""Own complete unfiltered diff/native side mapping; no raw private archive is published."""
import completion_read as R
import subprocess,json,re,hashlib
idx=R.gzload('completion-reading-index.json.gz');lookup={c['value_sha256']:i for i,c in enumerate(idx['claims'])};old_count=len(idx['claims']);streams=[]
expected={R.PRE:'1f88e677993c91905b72b747b187f6e94a52881178b08716fe6791bd6cbab444',R.C3:'5d639c30c53bb37035d2d133b715da5cc5c706afd13d278c8a7ad718368da5d9'}
flags=['--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color']
for before in [R.PRE,R.C3]:
 b=subprocess.check_output(['git','diff']+flags+[before,R.ACT]);assert R.h(b)==expected[before]
 groups=[];g=None;old=0;new=0;last_marker=None;last_body=None
 for line in b.decode().splitlines(keepends=True):
  if line.startswith('diff --git '):
   g={'path':line.rstrip().split(' b/',1)[1],'old_native_lines':[],'new_native_lines':[],'hunks':[]};groups.append(g)
  elif line.startswith('@@ '):
   m=re.match(r'@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@',line);assert m;old,new=map(int,m.groups());g['hunks'].append(line.rstrip())
  elif line.startswith(('--- ','+++ ','index ','new file mode ','deleted file mode ','old mode ','new mode ')):continue
  elif line.startswith('\\ No newline at end of file'):
   assert last_body.endswith('\n');sha=R.h(last_body[:-1].encode())
   if last_marker in (' ','-'):g['old_native_lines'][-1][1]=sha
   if last_marker in (' ','+'):g['new_native_lines'][-1][1]=sha
   g.setdefault('no_final_newline_markers',[]).append({'side_marker':last_marker,'old_next':old,'new_next':new})
  elif g and line[:1] in (' ','+','-'):
   marker=line[0];body=line[1:]
   last_marker,last_body=marker,body
   if marker in (' ','-'):g['old_native_lines'].append([old,R.h(body.encode())]);old+=1
   if marker in (' ','+'):g['new_native_lines'].append([new,R.h(body.encode())]);new+=1
 # Resolve every context/removed line against its exact native Git body.
 for g in groups:
  current_lines=R.git(R.ACT,g['path']).decode().splitlines(keepends=True)
  for n,sha in g['new_native_lines']:assert R.h(current_lines[n-1].encode())==sha
  if not g['old_native_lines']:continue
  raw=R.git(before,g['path']);lines=raw.decode().splitlines(keepends=True)
  for n,sha in g['old_native_lines']:assert R.h(lines[n-1].encode())==sha
  if g['path'].startswith(('specs/','deliverables/final-specification-set/engine-overworld/','deliverables/final-specification-set/pokemon-rules/')) or g['path'].endswith(('test-catalog/engine-overworld-wp11-15-59-60.md','test-catalog/pokemon-rules-wp53-60-61-62-69-70.md')):
   g['semantic_binding']='Initial completely consumed12 formal diff groups, exact same predecessor→ACT stream; C3→ACT has no formal changes.';continue
  sels=['/literal_lines/'+str(n-1) for n,sha in g['old_native_lines']];sels=list(dict.fromkeys(sels));di=len(idx['documents'])
  idx['documents'].append({'commit':before,'path':g['path'],'sha256':R.h(raw),'bytes':len(raw),'kind':'TEXT_LINES_KEEPENDS','selection':sels,'supplement':'Every old/context line from this complete unfiltered stream, full native line and order retained.'})
  g['old_semantic_document']=di
  for p in sels:
   a=lines[int(p.rsplit('/',1)[1])];ptr='/'+p.replace('~','~0').replace('/','~1')
   for steps,v in R.semantic_derivations(a):
    k=R.vh(v);ref={'document':di,'selector':ptr,'steps':steps,'native_type':type(a).__name__,'native_value_sha256':R.vh(a)}
    if k not in lookup:lookup[k]=len(idx['claims']);idx['claims'].append({'value_sha256':k,'type':type(v).__name__,'first':ref,'metadata_only':False,'prior_consumed':None,'length':len(str(v))})
    idx['occurrences'].append([lookup[k],di,ptr,steps,type(a).__name__,R.vh(a)])
  g['semantic_binding']='Native complete old hunk/context selection, every scalar preserved and matched to existing/new semantic claim identity.'
 streams.append({'before':before,'after':R.ACT,'flags':flags,'path_filter':None,'bytes':len(b),'sha256':R.h(b),'groups':groups,'raw_diff_publication':'not duplicated; exact hash/endpoints/flags and complete native-side reading map retained'})
R.save('completion-unfiltered-native-sides.json.gz',streams);R.save('completion-reading-index.json.gz',idx)
q=json.loads((R.OUT/'completion-pending-claims.json').read_text());q.extend(range(old_count,len(idx['claims'])));R.save('completion-pending-claims.json',q)
print('new old-side semantic claims',len(idx['claims'])-old_count,'documents',len(idx['documents']),'queue',len(q))
