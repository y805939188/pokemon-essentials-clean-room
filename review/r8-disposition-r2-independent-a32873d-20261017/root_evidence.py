#!/usr/bin/env python3
"""Record review input identities, attribution and immutable protection checks."""
from pathlib import Path
import json,subprocess,hashlib,ast,datetime
O=Path(__file__).resolve().parent;R=O.parents[1];E=O/'evidence';C='a32873d2860b15d9f5e27727db8f131f4ec433b6';P='8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8';PC='5666b7b912e2fb79b5119283ee6a37401a7071db';S='planning/implementation-routing/r8-20261017';PRE='review/r8-disposition-r1-independent-5666b7b-20261017'
def git(*args,cwd=R):return subprocess.check_output(['git',*args],cwd=cwd)
def save(n,x):(E/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def identity(c,p):
 b=git('show',c+':'+p);return {'commit':c,'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':git('rev-parse',c+':'+p).decode().strip()}
files=git('ls-tree','-r','--name-only',C,'--',S).decode().splitlines(); prior=json.loads(git('show',P+':'+PRE+'/evidence/root-input-reading.json'))
priorby={x['path']:x for x in prior['inputs']};records=[]
fullfresh={'AGENTS.md',S+'/README.md',S+'/review-prompt.md',S+'/revisions/r2/README.md',S+'/revisions/r2/review-prompt.md',S+'/routing.py',S+'/revisions/r2/tools/navigation-check.py',S+'/revisions/r2/tools/preservation-check.py',S+'/revisions/r2/tools/run-author-checks.py'}
for p in ['AGENTS.md',*files]:
 x=identity(C,p);b=git('show',C+':'+p)
 if p.endswith('.json'):obj=json.loads(b);x['full_structured_parse']=True
 if p.endswith('.py'):ast.parse(b.decode(),p);x['AST_parse']=True
 if p in fullfresh:x['consumption']='ROOT_FRESH_FULL_TEXT_READ; actual ranges captured in prior tool outputs,740line routing read in parts; no truncation credit'
 elif p in priorby and priorby[p]['sha256']==x['sha256']:x['consumption']='IDENTICAL_FIXED_R1_INPUT_CREDIT_PLUS_CURRENT_DIFF_OR_STRUCTURED_RECONCILIATION';x['prior_reading']=priorby[p]
 elif p.endswith('.json'):x['consumption']='FULL_STRUCTURED_PARSE_PLUS_ATTRIBUTED_DOMAIN_SEMANTIC_RECONCILIATION; not byte-print/full-prose-read claim'
 elif p.endswith('.py'):x['consumption']='ATTRIBUTED_STATIC_CODE_READ_OR_AST; details in combat-author-transform-consistency/source-results and root tool replay'
 else:x['consumption']='IDENTITY_AND_DIFF_OR_GENERATED_PROJECTION; no unsupported whole-body fresh reading claim'
 records.append(x)
r8=[]
for x in prior['inputs']:
 if x['commit']=='4575e80d041ab0c74a42e2e36399d05791dbaa5b':
  now=identity(C,x['path']);assert now['sha256']==x['sha256'];r8.append({'current_identity':now,'fixed_prior_full_read_credit':x,'method':'Identity-bound earlier full root credit, current protocol/contract recheck; combined truncated reprint gives no fresh omitted-text credit.'})
root_ranges=[('combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md',[[166,250]]),('combat-requirements/wp45-weather-terrain-side-and-position-effects.md',[[122,177]]),('creature-rpg/wp20-hp-status-moves-helditem.md',[[162,171]]),('generic-kernel/wp06-stats-directory.md',[[73,103]]),('creature-rpg/wp64-mail-and-mystery-gift.md',[[125,133]]),('user-interface/wp65-trainer-card-appendix.md',[[20,28]])]
save('root-input-reading.json',{'candidate_inputs':records,'R8_required_fixed_credit':r8,'r1_73_inputs':'r1-73-input-identities.json; exact file bytes/blobs, all own domain reports/results fully read/reconciled by attributed reviewers; root REPORT/findings/protocol/code and full aggregate reconciliation.','r2_reports_read_by_root':['pokemon-world-report.md complete','source-report.md complete','combat/kernel/demo reports earlier complete; final changes and structured results reconciled','creature-report.md complete affected/review sections; oversized full dump was truncated, only domain attributed full report/source credit for omitted table rows'],'root_extra_fresh_ranges':[{'identity':identity('908273093e1f6b27fc58249417675dd62d146224','deliverables/final-specification-set/'+p),'ranges':rs}for p,rs in root_ranges],'reading_limits':'All85 candidate-file identities, all131 formal identities/headings and721/736/33 decisions reconciled; no claim that every duplicate JSON prose or all131 files were freshly read by root. Reading byte counts alone never grant semanticPASS.'})
save('task-qualification.json',{'requested':{'model':'gpt-6.1-sol','reasoning_effort':'ultra','service_tier':'default','Fast':False},'authoritative_creation_echo':'UNVERIFIED','actual_execution':{k:'UNVERIFIED'for k in ['model','reasoning_effort','service_tier','speed','Fast','cloud_task_UUID']},'source_thread_id':'01a13f49-a154-7054-9b04-ce31f924d01c','qualification':'No authoritative cloud task/actual runtime echo exposed; native advertised priority does not establish default. Six delegated subcontexts form one independent review, not extra acceptance votes. Existing author revision was not edited or self-approved.'})
paths=git('diff','--name-only',PC,C).decode().splitlines();assert paths and all(p.startswith(S+'/')for p in paths)
formal='deliverables/final-specification-set';assert git('diff',C,'--',formal)==b'';assert git('diff','--cached','--',formal)==b''
ref=Path('/workspace/pokemon-essentials');assert git('rev-parse','HEAD',cwd=ref).decode().strip()=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';assert git('status','--porcelain',cwd=ref)==b''
assert git('rev-parse',C+':'+formal).decode().strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
remote=git('ls-remote','origin','refs/heads/main','refs/heads/codex/r8-disposition-tagging-20261017','refs/heads/codex/r8-disposition-r1-review-5666b7b-20261017').decode()
save('protection-final-precommit.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate':C,'R1_to_R2_change_count':len(paths),'R1_to_R2_paths':paths,'all_candidate_changes_confined_author_routing':True,'formal_candidate_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e','formal_worktree_and_index_diff':'EMPTY','reference_head':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','reference_worktree_status':'CLEAN','remote_refs':remote,'review_worktree_status':git('status','--short').decode(),'source_current_908_tree':git('rev-parse','908273093e1f6b27fc58249417675dd62d146224:'+formal).decode().strip(),'prepared_only_0eee_tree':git('rev-parse','0eee6d141f33758eda34bd8ebad94a3e2b617f5a:'+formal).decode().strip(),'no_force_or_main_push':True})
save('reviewer-attempts.json',{'root_static_first_attempt':'UnicodeDecodeError on gzip entry whose lines:null; fixed reviewer to honor binary, second full static checks pass; exact2150-command log gzip and raw identity retained.','aggregator':'Initial aggregate run exit0; all asserted coverage/counts pass. Subsequent adjudication distinctions recorded in outputs.','agents':'Exact failures/refinements retained in agent reports and probes: creature R1 projection/key assertions; source optional schema defaults/null isolation; ignored Python cache files deleted, no candidate bytes changed.','author_first_freeze':'Five actual errors retained, not silently counted as pass: META398 replacement,FR67 range,FR769 source classification,FR769 overlap,META20 unresolved ref; final seven-command replay passes.','environment_live_test':'environment-live-check.json actual execute/write/readback PASS, not inProgress inference.','execution':'Only static Markdown/JSON/Python schema/Git; Ruby,game,business/host/Showdown/framework prototypes:0.'})
original=json.loads(git('show','d62b41f4d620e50bb04c80a7505374bd284d8210:'+S+'/routing-manifest.json'))
current=json.loads(git('show',C+':'+S+'/routing-manifest.json'));by={x['feature_id']:x for x in current['features']+current['retired_features']};bindings=[]
for f in original['features']:
 if not f['upstream']['batches']:continue
 old=f['upstream'];now=by[f['feature_id']]['upstream'];bindings.append({'feature_id':f['feature_id'],'historical_binding':old,'current_binding':now,'historical_fields_preserved':all(old[k]==now[k]for k in ['batches','required_ids','binding_basis','authority'])})
assert len(bindings)==183 and all(x['historical_fields_preserved']for x in bindings)
save('original183-binding-preservation.json',{'initial':'d62b41f4d620e50bb04c80a7505374bd284d8210','candidate':C,'count':183,'all_preserved':True,'rows':bindings})
print(json.dumps({'candidate_input_identities':len(records),'protected':True,'R1_to_R2_paths':len(paths),'remote_read':True}))
