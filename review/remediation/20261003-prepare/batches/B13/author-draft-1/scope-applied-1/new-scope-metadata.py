from pathlib import Path
import subprocess,json,hashlib,datetime
r=Path('/workspace/pokemon-essentials-clean-room');base='8e67f780c204d593d89f364f585d2c6c2fe74631';prev='d4bfb88e461383d689f0e2db5d08c5f143b1e5f5';amend='2b23c82947bcecec4ab059d63048f9b67586575b';aroot='review/remediation/20261003-prepare/batches/B13/author-draft-1/';a=r/(aroot+'scope-applied-1');a.mkdir(parents=True,exist_ok=True);mp='review/remediation/20261003-prepare/batches/B13/scope-amendment-1/'
def git(*args):return subprocess.check_output(['git','-C',str(r),*args])
def ident(d):return {'git_blob':subprocess.check_output(['git','hash-object','--stdin'],input=d,cwd=r).decode().strip(),'sha256':hashlib.sha256(d).hexdigest(),'bytes':len(d)}
def eq(binding,d):assert ident(d)=={k:binding[k] for k in ['git_blob','sha256','bytes']},binding
assert git('rev-parse','HEAD').decode().strip()==prev
assert git('status','--porcelain','--untracked-files=no').decode()==''
md=git('show',amend+':'+mp+'scope-disposition.md');raw=git('show',amend+':'+mp+'scope-amendment.json');m=json.loads(raw);assert m['status']=='GRANTED_EXACT_FIXED_PATCH_SCOPE_ONLY' and m['quality_PASS'] is None;assert m['frozen_formal_base']['commit']==base
proposal=git('show',prev+':'+m['source_proposal']['path']);eq(m['source_proposal'],proposal);patch=git('show',prev+':'+m['source_whole_patch']['path']);eq(m['source_whole_patch'],patch);assert patch==(r/m['source_whole_patch']['path']).read_bytes()
assert len(m['allowed_original_write_paths'])==4;paths=[];checks=[]
for x in m['records']:
 assert x['write_authorized'] and x['quality_PASS'] is None
 path=x['path'];paths.append(path);before=(r/path).read_bytes();frozen=git('show',base+':'+path);eq(x['before'],before);assert before==frozen
 after=git('show',x['after_to_apply']['commit']+':'+x['after_to_apply']['path']);eq(x['after_to_apply'],after)
 part=x['per_file_patch'];seg=patch[part['byte_offset']:part['byte_offset']+part['bytes']];assert hashlib.sha256(seg).hexdigest()==part['sha256']
 checks.append({'path':path,'before':ident(before),'expected_after':ident(after),'canonical_finding_ids':x['canonical_finding_ids'],'supplementary_label':x['supplementary_label'],'allowed_clauses':x['allowed_clauses'],'per_file_patch':part})
assert paths==m['allowed_original_write_paths']
subprocess.run(['git','-C',str(r),'apply','--check','-'],input=patch,check=True,capture_output=True)
# Mutation is only the already confirmed exact immutable four-file patch. No text editing or normalization.
subprocess.run(['git','-C',str(r),'apply','-'],input=patch,check=True,capture_output=True)
for x in checks:
 after=(r/x['path']).read_bytes();assert ident(after)==x['expected_after'];x['applied_after']=ident(after);x['exact_after_equal']=True
changed=git('diff','--name-only',prev).decode().splitlines();assert changed==sorted(paths),changed
# New own evidence supersedes old pending flags for fixed bytes only; historical proposal/packet remains immutable.
(a/'scope-disposition.md').write_bytes(md);(a/'scope-amendment.json').write_bytes(raw)
receipt={'stage':'EXACT_ORIGINAL_SCOPE_APPLIED_AUTHOR_ONLY','timestamp_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'formal_FIX_BASE':base,'formal_FIX_BASE_tree':m['frozen_formal_base']['tree'],'scope_management_commit':amend,'scope_management_not_formal_input':True,'scope_documents':[{'commit':amend,'path':mp+'scope-disposition.md',**ident(md)},{'commit':amend,'path':mp+'scope-amendment.json',**ident(raw)}],'source_publication':prev,'source_proposal':m['source_proposal'],'source_whole_patch':m['source_whole_patch'],'applied_original_write_count':4,'records':checks,'scope_pending_resolved_for_exact_four_fixed_patches':True,'historical_pending_proposal_and_freeze_unchanged':True,'old_batch_permission_reused':False,'patch_changed':False,'WP55_supplementary_canonical_count_delta':0,'quality_PASS':None,'independent_review_started_by_author':False,'G':False,'C':False,'reference_game_Ruby_vectors_old_programs_executed':0,'additional_reference_or_historical_reading':0,'B030_required':False}
(a/'scope-application-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');(a/'new-scope-metadata.py').write_bytes(Path('/tmp/B13-apply-scope-20261010.py').read_bytes())
print('APPLIED exactly 4 scoped original patches; all before/after/whole/per-file identities match; 7 final outputs untouched; quality PASS remains null')
