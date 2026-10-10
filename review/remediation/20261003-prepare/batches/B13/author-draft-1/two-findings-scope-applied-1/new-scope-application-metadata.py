import subprocess,pathlib,json,hashlib,datetime
repo=pathlib.Path('/workspace/pokemon-essentials-clean-room')
base='8e67f780c204d593d89f364f585d2c6c2fe74631'
prior='c52c0df80bcba45ac77f8da2cdee264890846327'
scope_commit='231c9f25df4dd64961fb9290ff52302782a9fdb8'
scope_dir='review/remediation/20261003-prepare/batches/B13/scope-amendment-2/'
author_dir=pathlib.Path('review/remediation/20261003-prepare/batches/B13/author-draft-1/two-findings-scope-applied-1')
def git(*args):return subprocess.run(['git',*args],cwd=repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True).stdout
def ident(b):return {'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def bound(record):
 b=git('show',record['commit']+':'+record['path'])
 assert ident(b)=={k:record[k] for k in ['git_blob','sha256','bytes']},record['path']
 return b
assert git('rev-parse','HEAD').decode().strip()==prior
assert git('status','--porcelain')==b''
scope_bytes=git('show',scope_commit+':'+scope_dir+'scope-amendment.json')
scope=json.loads(scope_bytes)
assert scope['status']=='GRANTED_EXACT_FIXED_PATCH_SCOPE_ONLY'
assert scope['formal_FIX_BASE']=={'commit':base,'tree':'ae2f491294eb4f97be6b75f75706c16279f9bf46'}
assert scope['source_publication_commit']==prior and scope['source_repair_commit']=='235c9a599f20346bf82add2fa1d7220f5bfacdb2'
assert scope['quality_PASS'] is None and scope['B027_original_extension'] is False
original='specs/combat/wp58-battle-recording-and-playback.md'
assert scope['allowed_original_write_paths']==[original] and len(scope['records'])==1
proposal=json.loads(bound(scope['source_proposal']))
bound(scope['source_proposal_README'])
patch=bound(scope['source_whole_patch'])
assert hashlib.sha256(patch).hexdigest()=='8d186d65c9eb2bc0e03a27728bfa0ea8476f4753bb863054b41cdb3b79459b0d'
record=scope['records'][0]
assert record['path']==original and record['write_authorized'] is True and record['quality_PASS'] is None
assert bound(record['whole_patch_binding'])==patch
before=bound(record['before']);after=bound(record['after_to_apply'])
assert (repo/original).read_bytes()==before
assert record['exact_before_clause']==proposal['records'][0]['exact_before_clause']
assert record['exact_after_clause']==proposal['records'][0]['exact_after_clause']
old_clause=record['exact_before_clause'].encode();new_clause=record['exact_after_clause'].encode()
assert before.count(old_clause)==1 and before.replace(old_clause,new_clause,1)==after
assert before.splitlines()[103]==old_clause and b'\n'.join(after.splitlines()[103:110])==new_clause
patchfile=pathlib.Path('/tmp/B13-scope2-exact-whole.patch');patchfile.write_bytes(patch)
check=git('apply','--check',str(patchfile))
git('apply',str(patchfile))
actual=(repo/original).read_bytes()
assert actual==after
assert git('diff','--name-only').decode().splitlines()==[original]
subprocess.run(['git','diff','--check','--',original],cwd=repo,check=True)
target=repo/author_dir;target.mkdir(parents=True,exist_ok=False)
management=[]
for name in ['scope-amendment.json','scope-disposition.md','identity-and-patch-verification.json','validation-results.json']:
 content=git('show',scope_commit+':'+scope_dir+name)
 out=target/'scope-inputs'/name;out.parent.mkdir(exist_ok=True);out.write_bytes(content)
 management.append({'commit':scope_commit,'path':scope_dir+name,**ident(content),'frozen_read_only_copy':str(author_dir/'scope-inputs'/name)})
receipt={'role':'B13_AUTHOR_ONLY_EXACT_SCOPE2_APPLICATION_NOT_QUALITY_PASS','timestamp_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'formal_FIX_BASE':base,'formal_FIX_BASE_tree':'ae2f491294eb4f97be6b75f75706c16279f9bf46','reviewed_OLD':'5845e8084ced280e51c51a4081ec8583a9c2ca39','previous_repair_publication':prior,'management_scope_commit':scope_commit,'management_is_formal_input':False,'management_merged_or_cherry_picked':False,'scope_inputs':management,'source_whole_patch':scope['source_whole_patch'],'original_path':original,'allowed_clause':record['allowed_clause'],'before':record['before'],'expected_after':record['after_to_apply'],'actual_after':ident(actual),'entire_file_exact_after_equal':True,'only_direct_formal_changed_path':original,'outside_clause_byte_equal':True,'old_scope1_permission_not_extended':True,'old_pending_proposal_immutable':True,'B027_original_extension':False,'accepted_neighbor_writes':False,'patch_check':'PASS_TEXT_PATCH_ONLY','formal_whitespace_check':'PASS','applied':True,'quality_PASS':None,'independent_review_performed_by_author':False,'canonical_increment':0,'B030_increment':0,'G':False,'C':False,'B16_release':False,'reference_Ruby_game_vectors_old_programs_executed':False}
(target/'scope-application-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'scope':'EXACT_MATCH','applied_path':original,'whole_patch_sha256':ident(patch)['sha256'],'after':ident(actual),'quality_PASS':None,'receipt':str(author_dir/'scope-application-receipt.json')},ensure_ascii=False))
