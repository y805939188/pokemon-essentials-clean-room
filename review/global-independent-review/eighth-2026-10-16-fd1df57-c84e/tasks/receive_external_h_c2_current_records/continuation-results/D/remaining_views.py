"""Exact-value dictionaries for the remaining semantic fields; generation credits zero."""
from pathlib import Path
import hashlib,json,re
P=Path(__file__).resolve().parent
def raw(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
IDENTITY_KEYS={'path','original_path','logical_path','transport_path','sha256','git_blob','git_blob_content_id',
 'transport_sha256','transport_git_blob_content_id','workspace_tree','formal_tree','reference_tree','tree',
 'commit','file_sha256','canonical_sha256','raw_member_sha256','input_sha256','identity_id',
 'pointer','json_pointer','contract_pointer','snapshot','proposer_path','counter_path','mechanical_proof_ref',
 'successor_pointer','successor_path','original_pointer','output_entry','completed_evidence','evidence',
 'actual_session_log','platform_uuid_evidence','input_B','input_R','formal_tree','B','R','fixed_B','fixed_R',
 'argv','command_argv','session_path','log_path','stdout_path','stderr_path','raw_member_byte_offsets',
 'byte_offsets','byte_range','byte_ranges','ranges','lines','range','text_sha256'}
old={}; long_values={};field_map=[];vocab=[];identities=[];unresolved=[];containers=[]
def walk(x,at,key='',seed=False):
 if isinstance(x,dict):
  if set(x) & {'$same_value','$prior_exact','$delegated_open'}:
   if not seed:unresolved.append({'at':at,'association':x})
   return
  if not seed:containers.append({'at':at,'kind':'dict','keys':list(x)})
  for k,v in x.items():walk(v,at+'/'+k,k,seed)
 elif isinstance(x,list):
  if not seed:containers.append({'at':at,'kind':'list','length':len(x)})
  for n,v in enumerate(x):walk(v,at+'/'+str(n),key,seed)
 else:
  if key in IDENTITY_KEYS or (isinstance(x,str) and re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}',x)):
   if not seed:identities.append({'at':at,'key':key,'value':x,'purpose':'IDENTITY_OR_LOCATOR_ONLY; no target-body reading'})
   return
  token=raw([key,x])
  if seed:
   old.setdefault(token,at)
   if isinstance(x,str) and len(x)>60:long_values.setdefault(x,at)
   return
  if isinstance(x,str) and len(x)>60 and x in long_values:
   field_map.append({'at':at,'same_exact_value':long_values[x],'key':key});return
  if token in old:field_map.append({'at':at,'same_exact_key_value':old[token]});return
  ref='V'+str(len(vocab)).zfill(4);old[token]=ref
  if isinstance(x,str) and len(x)>60:long_values[x]=ref
  vocab.append({'id':ref,'first_at':at,'key':key,'value':x});field_map.append({'at':at,'value_id':ref})

# These complete projections/record texts were actually displayed previously.
for i in (0,1,15,18,16,5,19,20,21,22,11):walk(json.loads((P/'views'/f'scope-{i}.json').read_text()),f'file{i}#',seed=True)
legacy=json.loads((P/'originals/6').read_text())
readset=json.loads((P.parents[1]/'continuation-v2/D.complete.json').read_text())
for row in readset['semantic_objects']:
 walk(legacy[row['kind']][row['index']],f"file6#/{row['kind']}/{row['index']}",seed=True)
starts={}
for i in (12,13,14,10):
 starts[i]=len(vocab);walk(json.loads((P/'views'/f'scope-{i}.json').read_text()),f'file{i}#')
 print('FILE',i,'VOCAB',starts[i],len(vocab),'CHARS',sum(len(raw(x)) for x in vocab[starts[i]:]))
frames=[];current=[];size=0
last_prefix=None
for v in vocab:
 at=v['first_at'];parts=at.split('/')
 if at.startswith('file10#/coverage_and_qualification_sections/tasks/tasks/'):
  prefix='/'.join(parts[:5]);tail='/'.join(parts[5:])
 elif at.startswith('file10#/coverage_and_qualification_sections/tasks/preserved_prior_logical_entries/'):
  prefix='/'.join(parts[:5]);tail='/'.join(parts[5:])
 else:prefix='/'.join(parts[:2]);tail='/'.join(parts[2:])
 line=('\n# '+prefix+'\n' if prefix!=last_prefix else '')+v['id']+' '+tail+'='+raw(v['value'])+'\n';last_prefix=prefix
 if size+len(line)>11000 and current:
  frames.append(''.join(current));current=[];size=0
 current.append(line);size+=len(line)
if current:frames.append(''.join(current))
for n,s in enumerate(frames):(P/'views'/f'remaining-{n:03}.jsonl').write_text(s)
(P/'private/remaining-map.json').write_text(json.dumps({'schema':'gr8-d-exact-key-value-dictionary/v1',
 'rule':'All nonidentity leaves retained. Exact same-key/value associations retain every original pointer. Dictionary construction grants zero semantic credit.',
 'vocabulary':vocab,'field_map':field_map,'identity_fields':identities,'containers':containers,
 'unresolved_associations':unresolved,'start_indices':starts,
 'frames':[{'id':n,'chars':len(s),'sha256':hashlib.sha256(s.encode()).hexdigest()} for n,s in enumerate(frames)]},ensure_ascii=False,indent=2)+'\n')
print('FRAMES',len(frames),'VOCAB',len(vocab),'IDENTITY_LEAVES',len(identities),'ASSOCIATIONS',len(unresolved))
