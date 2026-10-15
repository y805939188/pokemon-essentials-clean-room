"""Bind actual C1, fully remote-read C0/C1, package identities and final scope.

The later C2 commit identity is deliberately external to this file.
"""
import datetime,hashlib,json,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1];P=R.parents[2]
def read(p):return json.loads((R/p).read_bytes())
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def git(*a):return subprocess.check_output(['git','-C',str(P),*a]).decode().strip()
def main():
 out=R/'publication/final-delivery-binding.json';assert not out.exists()
 receipt=read('publication/remote-readback-C1.json');core_remote=read('publication/remote-core-readback.json');assert receipt['status']=='FULL_REMOTE_READBACK_VERIFIED' and core_remote['status']=='FULL_REMOTE_CORE_VERIFIED'
 c1='0a56a4ecedfacbf22eecb0dbd8ceec1f3f0964fe';c0='28e0d9df6ca4f75de9773a502ebdaa177cc0752c';assert receipt['publication_commit']==c1 and core_remote['core_commit']==c0
 expected={}
 for line in subprocess.check_output(['git','-C',str(P),'ls-tree','-r','-z',c1,'--',str(R.relative_to(P))]).split(b'\0'):
  if not line:continue
  meta,path=line.split(b'\t',1);mode,kind,oid=meta.decode().split();assert kind=='blob';expected[path.decode()]=(mode,oid)
 actual={v['path']:(v['mode'],v['git_blob']) for v in receipt['physical_members']};assert actual==expected
 index=read('publication-transport/core/payload-index.json');decoded={v['logical_path']:v for v in receipt['decoded_logical_members']};assert len(decoded)==34251
 for v in index['logical_files']:assert all(decoded[v['logical_path']][k]==v[k] for k in ('bytes','sha256','git_blob_content_id'))
 package=read('publication/package-identities.json');by={v['path']:v for v in receipt['physical_members']}
 for v in package['members']:assert all(by[v['path']][k]==v[k] for k in ('bytes','sha256','git_blob'))
 tree=git('rev-parse',c1+'^{tree}');reporttree=git('rev-parse',c1+':'+str(R.relative_to(P)));assert tree==receipt['workspace_tree'] and reporttree==receipt['report_tree']
 status={'schema':'r7.final-delivery-binding.v1','status':'REVIEW_REPORT_AND_MANUAL_HANDOFF_PUBLISHED_REMOTE_VERIFIED','bound_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'update_started':False,'update_status':'UPDATE_NOT_STARTED','branch':'codex/review-seventh-2026-10-14-e646432-7a91','origin':'https://github.com/y805939188/pokemon-essentials-clean-room.git',
 'fixed_inputs':read('startup/fixed-inputs.json'),'core':read('publication/core-identity.json')['core'],
 'publication':{'commit':c1,'workspace_tree':tree,'report_path':str(R.relative_to(P)),'report_tree':reporttree,'handoff_path':str((R/'handoff').relative_to(P)),'handoff_tree':git('rev-parse',c1+':'+str((R/'handoff').relative_to(P)))},
 'prompt_and_manifest':[v for v in package['members'] if 'cloud-seventh-update-handoff-' in v['path']],
 'all_handoff_members':package['members'],'all_C1_report_members':receipt['physical_members'],
 'remote_readback':{'C1':{'path':str((R/'publication/remote-readback-C1.json').relative_to(P)),**ident((R/'publication/remote-readback-C1.json').read_bytes()),'counts':receipt['counts'],'completed_utc':receipt['completed_utc']},
                   'C0':{'path':str((R/'publication/remote-core-readback.json').relative_to(P)),**ident((R/'publication/remote-core-readback.json').read_bytes()),'counts':core_remote['counts']},
                   'decoded_logical_payloads':34251,'unique_objects':21449,'logical_decoded_bytes':index['counts']['decoded_bytes'],'unique_decoded_bytes':index['counts']['unique_decoded_bytes'],
                   'qualification':'All actual C1 physical bytes and every logical payload decoded and hashed from new remote bare objects. C0 separately verified, unchanged exact C1 full-byte cache reused with explicit provenance. Raw private platform streams remain local, public I/O projections are real published members.'},
 'coverage':read('coverage/summary.final.json'),'classification_counts':{'required':27,'P2':10,'P3':17,'P1':0,'optional_entries':7,'additional_optional_navigation_facets':2,'no_required_revision':1,'policy_entries':2,'inherited_R6':{'optional':8,'FLOAT':1,'policy':7,'limits':14,'no_required':1}},
 'finite_handoff':{'batches':13,'first_wave':read('batch-plan.final.json')['first_wave'],'first_wave_count':13,'author_blocking_edges':0,'entries':26,'actual_update_tasks_launched':0,'sole_actual_writer':'R7-I','fresh_integrated_reviewer':'R7-IR'},
 'execution':read('execution/phase-summary.final.json'),'limits':'All14 retained in full inherited/current purpose records and handoff manifest; no host/Demo/native media/full-model/real-save certification.',
 'protection_evidence':['startup/local-protection-verification.post-C1-v1.json','publication-staging/post-C1-protection.json','publication-staging/original-refs-final.json','publication-staging/other-worktrees-final.json','publication/remote-protected-refs.json'],
 'independent_package_reception':{'path':'publication-staging/C21/validation.json','status':'STRUCTURE_AND_IDENTITY_VERIFIED_SCOPED','actual_context':'01a13e0a-7a77-7572-8d38-bfe7d3082fe1','scope':'Full structure/identities and final three-file recovery delta, not repeated source semantics.'},
 'self_binding':{'C2_commit_tree':None,'rule':'C2 own immutable identity and final newly added binding-file readback are supplied externally in final delivery. No recursive C3 receipt or self hash.'}}
 out.write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'status':status['status'],'C1_files':len(actual),'logical':len(decoded),'core_files':core_remote['counts']['core_files'],'update_started':False}))
if __name__=='__main__':main()
