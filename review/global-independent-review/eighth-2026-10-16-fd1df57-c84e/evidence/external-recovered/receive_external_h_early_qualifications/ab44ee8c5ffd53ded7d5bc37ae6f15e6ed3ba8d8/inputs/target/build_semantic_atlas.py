"""Lossless value de-duplication for human reading; no automatic semantic credit."""
from pathlib import Path
import hashlib,json,re
TASK=Path(__file__).resolve().parent
ROOT=TASK/'recovered-early-history'
SOURCES=['tasks/R7-H12/subreaders/r1/qualification.json','tasks/R7-H12/subreaders/r3-r4/qualification.json','tasks/R7-H12/earlier-round-qualification-full.json']
IDENTITY_KEYS={'sha256','git_blob','git_blob_content_id','bytes','total_lines','utf8_byte_offset','line_start','line_end','record_sha256','source_record_sha256','transport_bytes','transport_sha256','transport_git_blob_content_id','commit','tree','repository_tree','workspace_tree','formal_tree','reference_tree','path','logical_path','logical_source_path','mode','logical_posix_mode','repository','repo','pointer','logical_id','canonical_platform_id','actual_platform_UUID','source_commit','source_path','file_identity','range_identity','identity','read_range','read_ranges','read_fields','fields_read','logs','log','log_paths','original_lines','source_bindings','scope_input_identities','lines','source_record_lines','schema_result_indices','record_index','original_lines','field_ranges','field_pointers','record_key','label'}
ROUTE_KEYS={'superseded_other_fields_routing','old_other_fields_routing','original_other_fields_routing','original_object','record_source','original_source','scope_source','closure_source','provenance','superseded_formal_routes','original_actual_text','参考与已读','最终条目','场景/向量'}
groups={};admin=[];dict_refs={};identities={}
def esc(s):return str(s).replace('~','~0').replace('/','~1')
def walk(x,path,ptr='',ancestor_admin=False):
 if isinstance(x,dict):
  if not x:leaf(x,path,ptr,ancestor_admin)
  for k,v in x.items():walk(v,path,ptr+'/'+esc(k),ancestor_admin or k in IDENTITY_KEYS or k in ROUTE_KEYS)
 elif isinstance(x,list):
  if not x:leaf(x,path,ptr,ancestor_admin)
  for i,v in enumerate(x):walk(v,path,ptr+'/'+str(i),ancestor_admin)
 else:leaf(x,path,ptr,ancestor_admin)
def leaf(v,path,ptr,force_admin):
 s=v if isinstance(v,str) else ''
 identity_value=isinstance(v,str) and bool(re.fullmatch(r'[0-9a-f]{8,64}|D\d{4,}|/[A-Za-z0-9_~./-]+|(?:GR\d|R\d|T-WP|WP\d|SC-|INC-|CUR-|M\d|C\d|B\d)[A-Za-z0-9_./:#@+-]*',s))
 if isinstance(v,str) and re.fullmatch(r'\d{4}-\d\d-\d\d(?:T| )[0-9:.+Z-]+',s):identity_value=True
 if isinstance(v,str) and ('/' in s or '\\' in s) and not re.search(r'[\s；。]',s) and re.search(r'\.(?:md|json|jsonl|rb|py|stdout|stderr|txt|gz)(?:#.*)?$',s):identity_value=True
 if force_admin or identity_value:
  admin.append({'source':path,'pointer':ptr,'type':type(v).__name__,'value_sha256':hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),'purpose':'identity/locator/old-reader routing only; no body reading credit'})
  if isinstance(v,str) and re.fullmatch(r'D\d{4,}',v):dict_refs.setdefault(v,[]).append({'source':path,'pointer':ptr})
  return
 # Whole exact values only; key/context associations remain recoverable for every occurrence.
 key=json.dumps(v,ensure_ascii=False,sort_keys=True)
 if key not in groups:groups[key]={'value':v,'occurrences':[]}
 groups[key]['occurrences'].append({'source':path,'pointer':ptr})
for path in SOURCES:
 b=(ROOT/path).read_bytes();identities[path]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()};walk(json.loads(b),path)
rows=[]
for i,(key,g) in enumerate(groups.items()):
 row={'id':f'V{i+1:05d}','value':g['value'],'occurrences':g['occurrences']}
 for occ in g['occurrences']:
  name=occ['pointer'].rsplit('/',1)[-1]
  if re.fullmatch(r'D\d{4,}',name):row.setdefault('dictionary_context_refs',[]).extend(dict_refs.get(name,[]))
 rows.append(row)
out=TASK/'semantic-atlas';out.mkdir(exist_ok=True)
(out/'associations.json').write_text(json.dumps({'source_identities':identities,'groups':rows,'administrative_leaves':admin,'semantic_credit':False},ensure_ascii=False,indent=2)+'\n')
chunks=[];texts=[];weight=0
for row in rows:
 occ=row['occurrences'][0]
 # This is an exact value presentation, not a prose summary. All associations live in the index.
 contexts=row.get('dictionary_context_refs',[])
 context=contexts[0] if contexts else occ
 alias={'tasks/R7-H12/subreaders/r1/qualification.json':'R1','tasks/R7-H12/subreaders/r3-r4/qualification.json':'R34','tasks/R7-H12/earlier-round-qualification-full.json':'H'}[context['source']]
 text=f"{row['id']} {alias}#{context['pointer']} ({len(row['occurrences'])} exact)\n"+json.dumps(row['value'],ensure_ascii=False)+'\n\n'
 w=sum(1 if ord(c)>127 else .25 for c in text)
 if texts and weight+w>6000:
  chunks.append(texts);texts=[];weight=0
 texts.append((row['id'],text));weight+=w
if texts:chunks.append(texts)
manifest=[]
for i,c in enumerate(chunks):
 name=f'chunk-{i+1:03d}.txt';b=''.join(t for _,t in c).encode();(out/name).write_bytes(b);manifest.append({'file':name,'first':c[0][0],'last':c[-1][0],'groups':len(c),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'status':'UNREAD'})
(out/'manifest.json').write_text(json.dumps({'groups':len(rows),'administrative_leaf_occurrences':len(admin),'chunks':manifest,'credit':'none until named human reader reads exact complete chunk; context associations required'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'groups':len(rows),'administrative_leaf_occurrences':len(admin),'chunks':len(chunks),'presentation_bytes':sum(r['bytes'] for r in manifest)},ensure_ascii=False))
