"""Own exact table-text span reuse, retaining every original character and context."""
import completion_read as R
import json,re
idx=R.gzload('completion-reading-index.json.gz');claims=idx['claims'];lookup={c['value_sha256']:i for i,c in enumerate(claims)};done=set(json.loads((R.OUT/'completion-consumption.json').read_text())['read_claims']);cache={};count=0
for i,c in enumerate(list(claims)):
 if c.get('decomposition_policy') or c.get('preserved_unrelated_accepted_history') or c['type']!='str':continue
 r=c['first'];di=r['document'];d=idx['documents'][di]
 if not d['path'].endswith('.md') or r['steps'] or not r['selector'].startswith('/literal_lines/'):continue
 if di not in cache:
  b=R.git(d['commit'],d['path']);assert R.h(b)==d['sha256'];cache[di]=b.decode().splitlines(keepends=True)
 v=cache[di][int(r['selector'].rsplit('/',1)[1])];assert R.vh(v)==c['value_sha256']
 if not v.startswith('|') or not v.rstrip().endswith('|'):continue
 # This is a literal text partition, not a Markdown parser or behavior model.
 # Even a pipe occurring inside code remains in the exact original parent.
 cuts=sorted(set([0,len(v)]+[n for m in re.finditer(r'\|',v) for n in (m.start(),m.end())]));children=[]
 for a,z in zip(cuts,cuts[1:]):
  if a==z:continue
  body=v[a:z];key=R.vh(body);steps=list(r['steps'])+[('span',str(a)+':'+str(z))];ref={**r,'steps':steps};prior=c['prior_consumed'] or ({'kind':'same_task_consumed_parent','parent_claim':i} if i in done else None)
  if key not in lookup:
   lookup[key]=len(claims);claims.append({'value_sha256':key,'type':'str','first':ref,'metadata_only':body=='|' or not body.strip() or bool(re.fullmatch(r'\s*[-:]+\s*',body)),'prior_consumed':prior,'length':len(body)})
  j=lookup[key]
  if prior and not claims[j]['prior_consumed']:claims[j]['prior_consumed']=prior
  children.append([a,z,j]);idx['occurrences'].append([j,di,r['selector'],steps,r['native_type'],r['native_value_sha256']])
 assert ''.join(v[a:z] for a,z,j in children)==v
 c['exact_ordered_table_text_spans']=children;c['metadata_only']=True;c['decomposition_policy']='Every exact character, pipe, whitespace, original line/type/native context/order and span concatenation retained; semantic spans require reading or verified exact reuse from own genuinely consumed bodies. Not a normalization or behavior assertion.';count+=1
R.save('completion-reading-index.json.gz',idx);print('literal table parents partitioned',count)
