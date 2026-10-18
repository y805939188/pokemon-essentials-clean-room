"""Own strict-purpose aid for metadata-only nested historical inventories.

This does not claim literal reading of paths/hash/offset rows. Every key and
nonidentity constant is checked. A purpose table binds each original parent
record and exact administrative subarray range to a finite metadata-only shape.
Historical/source/semantic approval, original I/O and remote fetch are not
certified. Unknown keys/types/strings fail before a purpose view is written.
"""
import collections,datetime,hashlib,json,re
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;begin=datetime.datetime.now(datetime.timezone.utc).isoformat();l=json.loads((P/'reading-ledger.json').read_text());r=l['snapshot_payloads'][137];raw=(B/r['snapshot']).read_bytes();assert hashlib.sha256(raw).hexdigest()==r['sha256'];d=json.loads(raw)
allowed=set('pointer value bytes sha256 git_blob purpose binding_id json_pointer canonical_sha256 input_sha256 raw_member_byte_offsets raw_member_bytes raw_member_sha256 commit path git_blob_content_id status identity_fields git_mode role base_B_identity_or_explicit_new_file url attempts attempt http_status complete_byte_match local_path tree plan group repository restored_identity logical_path transport_path encoded_identity identity_id mode changed_against_B base_B_identity file file_bytes file_sha256 remote_path restored_local_path identity _already_read_this_context_same_values'.split())
constants={'status':{'A'},'role':{'author_evidence'},'base_B_identity_or_explicit_new_file':{'NEW_AUTHOR_EVIDENCE_FILE'},'plan':{'original-plans','actual-plans'},'group':{'artifacts','evidence','fixed_read_inputs'},'repository':{'y805939188/pokemon-essentials-clean-room','Maruno17/pokemon-essentials'}}
hashkeys={'sha256','canonical_sha256','input_sha256','raw_member_sha256','file_sha256'};gitkeys={'git_blob','git_blob_content_id','commit','tree'};pathkeys={'pointer','json_pointer','path','local_path','logical_path','transport_path','file','remote_path','restored_local_path','_already_read_this_context_same_values'};numkeys={'bytes','raw_member_bytes','file_bytes','attempt','http_status'}
counts=collections.Counter();shapes=collections.Counter();strings=collections.Counter();purposes=[];outershapes=[];bindings=[];typed=[];rangeviews=[]
def inspect(x,parent=''):
 if isinstance(x,dict):
  assert set(x)<=allowed,(parent,set(x)-allowed);shapes[tuple(sorted(x))]+=1
  for k,v in x.items():counts[k]+=1;inspect(v,k)
 elif isinstance(x,list):
  if parent=='raw_member_byte_offsets':assert len(x)==2 and all(type(z)is int and z>=0 for z in x) and x[0]<=x[1]
  for v in x:inspect(v,parent)
 elif isinstance(x,str):
  if parent in hashkeys:assert re.fullmatch('[0-9a-f]{64}',x);strings['64hex recovery identity']+=1
  elif parent in gitkeys:assert re.fullmatch('[0-9a-f]{40}',x);strings['40hex Git identity']+=1
  elif parent in constants:assert x in constants[parent];strings[parent+':'+x]+=1
  elif parent in ['mode','git_mode']:assert re.fullmatch('[0-7]{6}',x);strings[parent+':'+x]+=1
  elif parent=='binding_id':assert re.fullmatch('p[0-9]+-[0-9a-f]+',x);strings['binding_id recovery locator']+=1
  elif parent=='url':assert x.startswith('https://raw.githubusercontent.com/');strings['immutable raw.githubusercontent URL locator']+=1
  elif parent=='identity_id':assert re.fullmatch('I[0-9a-f]{16}',x);strings['identity_id I plus16hex recovery locator']+=1
  elif parent=='value':assert re.fullmatch(r'candidates/R7-U[0-9]{2}/[A-Za-z0-9_.\-/]+',x) and '..' not in x.split('/');strings['565 candidate relative paths in10 inventory lists; locator only']+=1
  elif parent in pathkeys:assert '\n' not in x;strings[parent+' locator only']+=1
  elif parent=='purpose':assert x in purposes;strings['explicit purpose string']+=1
  else:raise AssertionError(('unclassified string',parent,x))
 elif isinstance(x,bool):assert parent in ['complete_byte_match','changed_against_B'];strings[parent+':'+str(x)]+=1
 elif type(x)is int:
  assert parent in numkeys|{'raw_member_byte_offsets'} and x>=0
  if parent=='attempt':assert x==1
  if parent=='http_status':assert x==200
 elif x is None:raise AssertionError(('unclassified null',parent))
 else:raise AssertionError((parent,type(x).__name__))
for ri,rec in enumerate(d['records']):
 arr=rec.get('administrative_dispositions',[]);bs=[]
 for ai,a in enumerate(arr):
  assert set(a) in ({'pointer','value','purpose'},{'pointer','identity_fields','purpose'})
  if a['purpose'] not in purposes:purposes.append(a['purpose'])
  shape=[sorted(a),sorted(a.get('value',a.get('identity_fields'))) if isinstance(a.get('value',a.get('identity_fields')),dict) else 'list']
  if shape not in outershapes:outershapes.append(shape)
  s=outershapes.index(shape);pi=purposes.index(a['purpose']);inspect(a);bs.append([s,pi])
  typed.append({'parent_record':ri,'administrative_index':ai,'object':a,'qualification':'RECOVERY_METADATA_ONLY_NOT_PERSONALLY_LITERAL_READ'})
 spans=[]
 for ai,pair in enumerate(bs):
  if spans and spans[-1][2:]==pair:spans[-1][1]=ai+1
  else:spans.append([ai,ai+1,*pair])
 assert [pair for a,b,*pair in spans for _ in range(a,b)]==bs;bindings.append(spans)
 sr=rec['semantic_range']
 if set(sr)=={'continuous_lines'}:rangeviews.append([ri,'continuous_lines',sr['continuous_lines']])
 else:
  assert set(sr)=={'json_root_pointer','excluded_pure_administrative_pointers','exact_same_value_associations'} and sr['json_root_pointer']==''
  assert sr['excluded_pure_administrative_pointers']==[a['pointer'] for a in arr]
  assert sr['exact_same_value_associations']==rec.get('current_same_value_associations',[])
  rangeviews.append([ri,'root_pointer_empty','excluded_pointers_exact_admin_order_with_duplicates',len(arr),'associations_exact_own_already_read_nonhash_array',len(rec.get('current_same_value_associations',[]))])
side=P/'h137-admin-exact-metadata-recovery-only.json';side.write_text(json.dumps(typed,ensure_ascii=False,indent=2)+'\n');sraw=side.read_bytes();view={'qualification':'STRICT ADMINISTRATIVE PURPOSE ONLY; not7797 literal object/path/hash/offset reading. Unknown key/type/string fails. All current effective nonidentity constants and all finite per-record class/range bindings below require actual reading. No source/clause/case/premise/callback/approval-stage body is present in these inventories; GitA is pathstatus only. Uniform1910HTTPattempt metadata remains a carrier claim, not own remote verification. Original referenced semantic values, read_I/O, task completion and historicalPASS not certified.','source':{k:r[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},'metadata_recovery':{'path':side.name,'bytes':len(sraw),'sha256':hashlib.sha256(sraw).hexdigest(),'objects':len(typed),'literal_values_read':False},'all_nested_key_counts':dict(counts),'all_nested_object_shapes':[{'keys':list(k),'count':n} for k,n in shapes.items()],'all_scalar_class_or_effective_constant_counts':dict(strings),'complete_purposes':purposes,'outer_shapes':outershapes,'encoding':'bindings row ordinal is original parent record; spans=[startInclusive,endExclusive,outerShapeIdx,purposeIdx]. No subarray omitted; original object values retained recovery-only, no literal read claimed. semantic_range records carry exact continuous lines or exact same ordered adminpointer/currentassociation arrays, mechanically equal only.','ordered243_admin_purpose_bindings':bindings,'complete243_semantic_range_qualifications':rangeviews}
lines=['{'];ks=list(view)
for k in ks:
 v=view[k]
 if k in ['all_nested_object_shapes','complete_purposes','outer_shapes','ordered243_admin_purpose_bindings','complete243_semantic_range_qualifications']:
  lines.append(json.dumps(k)+':[')
  for i,x in enumerate(v):lines.append(json.dumps(x,ensure_ascii=False,separators=(',',':'))+(',' if i+1<len(v) else ''))
  lines.append(']'+(',' if k!=ks[-1] else ''))
 else:lines.append(json.dumps(k)+':'+json.dumps(v,ensure_ascii=False,separators=(',',':'))+',')
lines.append('}');data=('\n'.join(lines)+'\n').encode();assert json.loads(data)==view;out=P/'h137-admin-semantic-range-STRICT-PURPOSE-view.json';out.write_bytes(data);m={'begin_utc':begin,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':137,'source_sha256':r['sha256'],'output':out.name,'bytes':len(data),'lines':len(lines),'sha256':hashlib.sha256(data).hexdigest(),'all_admin_objects':len(typed),'all_admin_shape_const_checks':True,'all_semantic_ranges_exact_relation_checked':True,'generation_reading_credit':0,'full_literal_json_credit':False};(P/'h137-admin-STRICT-PURPOSE-generation.json').write_text(json.dumps(m,indent=2)+'\n');print(json.dumps(m))
