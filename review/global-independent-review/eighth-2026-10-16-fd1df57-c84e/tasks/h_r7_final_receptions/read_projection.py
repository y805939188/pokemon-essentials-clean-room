import json,sys
from pathlib import Path
BASE=Path('/workspace/pokemon-essentials-clean-room/review/global-independent-review/eighth-2026-10-16-fd1df57-c84e')
ROWS=json.load(open(BASE/'delegation/readsets/h_r7_final_receptions.json'))['files']
PURE_ID_KEYS={'bytes','sha256','git_blob','git_blob_content_id','mode','path','commit','tree','repository','repo','pointer','json_pointer','binding_id','canonical_sha256','input_sha256','raw_member_byte_offsets','raw_member_bytes','raw_member_sha256','git_mode','transport_path','transport_bytes','transport_sha256','transport_git_blob_content_id','logical_path','local_path','source_binding','file','file_bytes','file_sha256','identity_id','verified','matches'}
def prune(x,pointer='',admin=None):
 if isinstance(x,dict):
  transport_keys={'path','bytes','sha256','git_blob','git_blob_content_id','git_mode','mode','url','attempts'}
  if 'path' in x and 'attempts' in x and set(x).issubset(transport_keys):
   if admin is not None:admin.append({'pointer':pointer,'value':x,'purpose':'PURE_IDENTITY_TRANSPORT_FILE_ROW; retains original HTTP attempts/failed transport exactly; no semantic/behavior execution credit'})
   return {'_identity_locator_inventory_only':True}
  if x.get('role')=='author_evidence' and set(x).issubset({'path','bytes','sha256','git_blob','git_mode','role','base_B_identity_or_explicit_new_file'}) and x.get('base_B_identity_or_explicit_new_file')=='NEW_AUTHOR_EVIDENCE_FILE':
   if admin is not None:admin.append({'pointer':pointer,'value':x,'purpose':'PURE_AUTHOR_EVIDENCE_IDENTITY_INDEX_ROW; no rule/case/dependency/stage/status'})
   return {'_author_evidence_identity_inventory_only':True}
  if x and set(x).issubset(PURE_ID_KEYS):
   if admin is not None:admin.append({'pointer':pointer,'value':x,'purpose':'EXACT_IDENTITY_AND_LOCATOR_ONLY_NO_SEMANTIC_CREDIT'})
   return {'_identity_locator_inventory_only':True}
  if 'path' in x and 'bytes' in x and ('sha256' in x or 'git_blob' in x):
   idkeys={'bytes','sha256','git_blob','git_blob_content_id','git_mode','mode'}
   if admin is not None:admin.append({'pointer':pointer,'identity_fields':{k:v for k,v in x.items() if k in idkeys},'purpose':'MIXED_RECORD_IDENTITY_FIELDS_ONLY; all other fields remain for semantic reading'})
   x={k:v for k,v in x.items() if k not in idkeys}
  return {k:prune(v,pointer+'/'+k.replace('~','~0').replace('/','~1'),admin) for k,v in x.items()}
 if isinstance(x,list):
  inventory_keys=PURE_ID_KEYS|{'role','base_B','base_B_identity_or_explicit_new_file','independently_verified','git_tree_and_restored_and_freeze_match','git_object_match','raw_vs_actual_git_bytes','full_byte_match','base_B_identity'}
  inventory_names={'files','candidate_files','candidate_file_identities','candidate_and_author_evidence_files','bootstrap_file_identities'}
  if pointer.rsplit('/',1)[-1] in inventory_names and x and all(isinstance(v,dict) and 'path' in v and set(v).issubset(inventory_keys) and v.get('role') in {None,'candidate_mirror','author_evidence','reviewer_evidence_or_public_tool_io'} for v in x):
   if admin is not None:admin.append({'pointer':pointer,'value':x,'purpose':'EXACT_FILE_IDENTITY_ROLE_INVENTORY_ONLY; no rule/case/dependency/adoption/status fields; all original locator/identity values retained'})
   return {'_file_identity_role_inventory_only_count':len(x)}
  formal_id_keys={'path','bytes','sha256','git_blob_content_id','changed_against_B','git_blob','git_mode','base_B_identity'}
  if pointer.rsplit('/',1)[-1] in {'all131_actual_identities','all_formal_file_identities'} and all(isinstance(v,dict) and set(v).issubset(formal_id_keys) for v in x):
   if admin is not None:admin.append({'pointer':pointer,'value':x,'purpose':'FULL_FORMAL_FILE_IDENTITY_AND_B_COMPARISON_INVENTORY_ONLY; no rule/case/approval-stage; scope counts/qualifications read separately'})
   return {'_formal_identity_B_comparison_inventory_only_count':len(x)}
  readlog_keys={'utc','tool_pid','path','lines','returned_utf8_bytes'}
  if pointer.rsplit('/',1)[-1] in {'recorded_reads','latest_reference_reads'} and all(isinstance(v,dict) and set(v).issubset(readlog_keys) for v in x):
   if admin is not None:admin.append({'pointer':pointer,'value':x,'purpose':'READ_REQUEST_UTC_PID_RANGE_INVENTORY_ONLY; not semantic-read certification; all document-level qualification remains visible'})
   return {'_read_request_inventory_only_count':len(x)}
  identity_restore_keys={'plan','group','identity_id','repository','commit','path','local_path','bytes','sha256','git_blob_content_id','restored_identity','logical_path','transport_path','encoded_identity'}
  if pointer.rsplit('/',1)[-1]=='all_restored_inputs' and all(isinstance(v,dict) and set(v).issubset(identity_restore_keys) for v in x):
   if admin is not None:admin.append({'pointer':pointer,'value':x,'purpose':'RESTORED_IDENTITY_INDEX_ONLY; no semantic read, all original encoded/decoded identities retained'})
   return {'_restored_identity_inventory_only_count':len(x)}
  if pointer.rsplit('/',1)[-1]=='complete_diff_against_B' and all(isinstance(v,dict) and set(v)=={'path','status'} for v in x):
   if admin is not None:admin.append({'pointer':pointer,'value':x,'purpose':'PURE_GIT_PATH_STATUS_INVENTORY; no game rules or reception stage; actual semantic target classes retained separately'})
   return {'_git_diff_inventory_only_count':len(x)}
  if pointer.rsplit('/',1)[-1] in {'validated_declared_files','declared_files','restored_context_files','restored_files'} and all(isinstance(v,str) and '/' in v for v in x):
   if admin is not None:admin.append({'pointer':pointer,'value':x,'purpose':'PURE_PATH_INVENTORY_NO_CURRENT_RULE_CASE_DEPENDENCY_OR_STATE'})
   return {'_path_inventory_only_count':len(x)}
  return [prune(v,pointer+'/'+str(i),admin) for i,v in enumerate(x)]
 return x
def squash(x):
 if isinstance(x,dict):return {k:squash(v) for k,v in x.items()}
 if isinstance(x,list):
  omitted=[i for i,v in enumerate(x) if isinstance(v,dict) and (v=={'_author_evidence_identity_inventory_only':True} or v=={'_identity_locator_inventory_only':True})]
  if len(omitted)>3:
   return {'_administrative_inventory_only_count':len(omitted),'_administrative_inventory_only_index_bounds':[min(omitted),max(omitted)],'semantic_rows':[{'original_index':i,'value':squash(v)} for i,v in enumerate(x) if i not in omitted]}
  return [squash(v) for v in x]
 return x
if __name__=='__main__':
 i=int(sys.argv[1]);d=json.load(open(ROWS[i]['local_path']));admin=[]
 if len(sys.argv)>2:
  for k in sys.argv[2].split('/'):
   if k:d=d[int(k)] if isinstance(d,list) else d[k]
 q=prune(d,sys.argv[2] if len(sys.argv)>2 else '',admin)
 print(json.dumps(squash(q),ensure_ascii=False,indent=2))
