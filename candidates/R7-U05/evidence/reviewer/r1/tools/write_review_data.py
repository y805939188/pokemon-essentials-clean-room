"""Serialize the reviewer's manually reasoned findings; no behavioral computation."""
import datetime
import hashlib
import json
from pathlib import Path

OUT=Path(__file__).resolve().parents[1]
CHECK=json.loads((OUT/'tools/input-validation.json').read_bytes())
FREEZE=json.loads(Path('/workspace/r7-review-bootstrap/R7-U05/candidate-input.json').read_bytes())
CONTRACT=json.loads(Path('/workspace/r7-bootstrap/R7-U05-reviewer/R7-U05-contract.json').read_bytes())
ANCHORS=CHECK['candidate_anchors']

configuration={'requested':{'model':'gpt-6.1-sol','effort':'ultra','service_tier':'default','speed':'ordinary','Fast':'forbidden'},
               'effective':{k:'UNVERIFIED' for k in ['model','effort','tier','speed']},
               'qualification':'No effective configuration return; request, context and exit status are separate evidence.'}
sources={
 'daycare':{'path':'Data/Scripts/012_Overworld/007_Overworld_DayCare.rb','lines':[[1,564]]},
 'pokemon':{'path':'Data/Scripts/014_Pokemon/001_Pokemon.rb','lines':[[90,210],[420,545],[1080,1227]]},
 'handlers':{'path':'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb','lines':[[1,792]]},
 'time':{'path':'Data/Scripts/012_Overworld/003_Overworld_Time.rb','lines':[[1,5],[187,208]]},
 'species':{'path':'Data/Scripts/010_Data/002_PBS data/008_Species.rb','lines':[[80,110],[250,270]]},
 'compile':{'path':'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb','lines':[[4,68],[292,477]]},
 'strings':{'path':'Data/Scripts/021_Compiler/001_Compiler.rb','lines':[[410,440]]},
 'pokedex':{'path':'Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb','lines':[[185,270]]},
 'pbs_base':{'path':'PBS/pokemon.txt','lines':[[11113,11139],[15229,15255]]},
 'pbs_forms':{'path':'PBS/pokemon_forms.txt','lines':[[1397,1408]]},
 'hatching':{'path':'Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb','lines':[[1,131],[190,268]]},
 'images':{'path':'Data/Scripts/010_Data/002_PBS data/009_Species_files.rb','lines':[[1,190]]}
}
index=json.loads(Path('/workspace/r7-context/R7-U05-reviewer/evidence/tasks/R7-C13/identity-index.json').read_bytes())
for row in sources.values():
 row['identity']=next(r for r in index['identities'] if r['repository_id']=='reference' and r['path']==row['path'])
 row['qualification']='New static reading of named ranges only; full-file identity is not execution or whole-tree semantic credit.'

vector_notes=[
 ('PF01',['GR7-M07-002-C1','PF01'],'Normal author-data month2 mother0 -> mother1 completed before inherited child1; legal string flag and absence of earlier dynamic read checked. Recalculation does not require numerical change; cache clearing is not a final-empty invariant.',['daycare','pokemon','handlers','time','species','compile','strings','pokedex','pbs_base','pbs_forms']),
 ('PF02',['GR7-M07-002-C2','PF02'],'Month1 yields stored0 and skips changed parent submission; explicit child0 still submits. Parent equality guard must not be added to the child setter.',['daycare','pokemon','handlers','time']),
 ('PF03',['GR7-M07-002-C3','PF03'],'Forced mother0 returns before dynamic dispatch; mother stored0 unchanged, explicit child0 side effects retained.',['daycare','pokemon']),
 ('PF04',['GR7-M07-002-C3','PF04'],'Storage and independent battle guards suppress the parent dynamic commit; explicit child setter still executes. No UI reachability inferred.',['daycare','pokemon']),
 ('PF05',['GR7-M07-002-C4','PF05'],'Removing the author flag restores default DEERLING; no maternal read and no qualified Everstone alternative under common premises. No claim about unrelated reads.',['daycare','species','pbs_base','handlers']),
 ('PF06',['GR7-M07-002-C4','PF07'],'Default SHELLOS has maternal flag and no corresponding registration/copy target in the fully read fixed handler file. BR27-31 child same-value, N0 and order controls remain separate.',['daycare','pokemon','handlers','pbs_base','pokedex']),
 ('PF07',['GR7-M07-002-C5','PF06'],'Collection generates before party capacity check; full party rejects before entry/reset and does not undo reached parent/record prefix. Named generation has no interactive cancel.',['daycare','pokemon','pokedex']),
 ('PF08',['normal_cancel_failure_partial_commit/partial_commit'],'At parent recalculation fault, form/cache prefix reached but registration/inherited child assignment not reached; at parent registration refresh fault, reached records remain; later child fault cannot undo completed mother prefix. Conditional faults not injected; no rollback or host recovery promise.',['daycare','pokemon','handlers','pokedex']),
 ('PF09',['GR7-M07-002-C1/conditional_registration'],'Nullable player/dex registration guards checked alongside constructor fallback for nil owner, absence of DEERLING creation/egg handlers and normal remaining dependencies. Generation conclusion only; collection requiring player excluded.',['daycare','pokemon','handlers','pokedex'])]
vectors=[]
for i,(suffix,mapping,note,refs) in enumerate(vector_notes,1):
 vectors.append({'candidate_vector':'R7-U05-'+suffix,'original_vector_mapping':mapping,
                 'candidate_anchor':ANCHORS[i+1], 'common_premise_anchor':ANCHORS[1],
                 'static_result':'PASS_CONDITIONAL_STATIC','reason':note,'source_keys':refs,
                 'execution':'NOT_EXECUTED','runtime_equivalence_asserted':False})

preserved=[
 ('default_author_data_only','PASS','Default DEERLING lack of flag independently checked in fixed PBS; author-data fixture assumed validly loaded and never created/compiled/run.'),
 ('maternal_then_first_eligible_Everstone_and_child_same_value','PASS','WP34 section5.2 and BR07/BR27-31 bytes unchanged; fixed generation ordering and setter checked.'),
 ('no_extra_parent_owner_IV_EV_EXP_write','PASS','New sentence limits additional direct inheritance writes; source distinguishes form/cache/stats/conditional dex from independent daycare growth.'),
 ('forced_battle_storage_equality_guards','PASS','Ordinary parent read uses these guards; explicit child setter does not acquire equality guard.'),
 ('no_clone_or_source_architecture_requirement','PASS','Candidate states independent behavior and uses existing WP21 semantics, with no framework or source-structure prescription.')]
historical=[
 {'ids':['BR07','BR27','BR28','BR29','BR30','BR31'],'result':'PASS_STATIC_COMPATIBILITY','reason':'Full unchanged rows read; form setter, dex prefix, N0 and ordered maternal/Everstone consumers newly checked. Prior child behavior not counted again.','source_keys':['daycare','pokemon','handlers','pokedex']},
 {'ids':['EG-13','EG-20'],'result':'PASS_STATIC_COMPATIBILITY','reason':'Fixed B catalog rows read; named fixed R hatching caller newly read confirms ordinary dynamic form read precedes later owned/seen-egg writes under normal presentation premises. Parent and hatching receivers remain distinct.','source_keys':['hatching','pokemon','handlers','time']},
 {'ids':['R4-IF01','R4-IF02','R4-IF03','R4-IF04','R4-IF05','R4-IF06'],'result':'PASS_STATIC_COMPATIBILITY','reason':'All six unchanged rows read; strict timeout, forced-return distinction, individual-image read before resolution, direct explicit form request and nonrollback of reached prefix checked. No pixel/runtime approval.','source_keys':['images','handlers','pokemon']}]
for row in historical: row['execution']='NOT_EXECUTED';row['new_historical_closure_credit']=0

unmet=[
 'R7-I clause-level integration and WP21/WP33/shared-catalog receiver reception',
 'New independent R7-IR review of actual cumulative integrated commit/tree',
 'R7-I formal acceptance and satisfaction of exact direct/transitive dependencies and historical regression closure gates',
 'Runtime equivalence, real host/Demo/native media/save/replay remain unverified; no such execution performed here']
per_id={'schema':'r7.u05.independent-reviewer-per-id.v1','batch_id':'R7-U05','record_id':'GR7-M07-002',
        'result':'PASS_SCOPED_CANDIDATE','qualification':'Limited static candidate content review; no runtime equivalence, actual integration approval, formal acceptance or closure.',
        'dispatch_commit':'6ec1d09e9c470954964d72761c83a760ef4f0364','freeze_commit':'58c6427f2ba48aa7dd3b59d4ab1e40c54394fd3a',
        'freeze_tree':'41849a965da575666d2b8363125ba14eb46bd6ec','candidate_commit':FREEZE['candidate_commit'],'candidate_tree':FREEZE['candidate_tree'],
        'fixed_B':FREEZE['fixed_B'],'fixed_B_workspace_tree':FREEZE['fixed_B_tree'],'fixed_B_formal_subtree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c',
        'contract':FREEZE['original_contract_commit_path_identity'],'author_context':FREEZE['author_task_id'],
        'reviewer_context':CHECK['task_context'],'configuration':configuration,
        'acceptance_conditions':[{'id':'AC1','result':'PASS','reason':'Only required WP34 section9.10 and explicitly author-data parent-form catalog contribution changed; all preserved scope retained.'},
          {'id':'AC2','result':'PASS_CONDITIONAL_STATIC','reason':'All C1-C5, original PF01-PF07 and candidate PF01-PF09 checked separately for premises, normal/cancel/failure/partial prefixes; none executed.'},
          {'id':'AC3','result':'PASS','reason':'Different actual reviewer context freshly read fixed source, accepted nonauthor counterproof and exact candidate content; future integrated review remains separate.'}],
        'minimum_clause_anchor':ANCHORS[0],'vectors':vectors,
        'preserved_scope':[dict(id=i,result=r,reason=n) for i,r,n in preserved],
        'four_paths':{'normal':'PASS_STATIC: changed mother prefix before inherited child assignment; no forced numeric HP/stat change.',
                      'cancel':'PASS_STATIC: no interactive cancel in the named DEERLING generation chain; no rollback inferred from later choices.',
                      'failure':'PASS_STATIC: full-party refusal after generation and before entry/reset.',
                      'partial_commit':'PASS_STATIC: retain only actually reached mutation/recalculation/registration prefixes; no atomic rollback, recovery or save guarantee.'},
        'historical_regressions':historical,'source_read_set':sources,
        'findings_requiring_revision':[],'missing_input_or_independence_blockers':[],
        'optional_or_policy_adopted':[],'conditional_sync':[],'conflict_groups':[],
        'unmet_downstream_dependencies':unmet,'integrated_PASS':False,'ACCEPTED':False,'CLOSED':False,
        'execution':{'source_static':'READ_NAMED_RANGES','derived_vectors':'NOT_EXECUTED',
                     'tool_validation':'INPUT_IDENTITY_SCOPE_AND_PUBLIC_TRANSPORT_ONLY',
                     'reference_observation':0,'independent_behavior_model':0,'host_Demo_native_media_real_save_replay':0},
        'limits':{'L01_L14':'RETAINED','old_56_92_closure':'UNCHANGED_NO_NEW_APPROVAL','denominator':'27 required items / 13 batches',
                  'unselected':'7 optional / 2 extra navigation facets / 1 no-required / 2 policy unchanged',
                  'negative_evidence':'Named freshly read chain only; old all-131 lexical search not inherited as semantic reading or proof of arbitrary plugin absence.'}}

supplements=[]
for label in ['restore-named-compiler','restore-hatch-consumer','restore-image-consumer']:
 log=json.loads((OUT/'tools/logs'/f'{label}.json').read_bytes());supplements.append(json.loads(log['stdout']))
receipt={'schema':'r7.u05.independent-review-input-receipt.v1','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'task_context':CHECK['task_context'],'configuration':configuration,
         'author_context':FREEZE['author_context_and_qualification'],'different_actual_context':True,
         'immutable_bindings':CHECK['fixed_bindings'],'candidate_commit':FREEZE['candidate_commit'],'candidate_tree':FREEZE['candidate_tree'],
         'candidate_files':CHECK['candidate_files'],'candidate_count':CHECK['candidate_files_count'],'candidate_bytes':CHECK['candidate_bytes'],
         'candidate_complete_diff':CHECK['complete_candidate_diff'],'candidate_anchors':ANCHORS,
         'context_restore':{'receipt':'tools/context-restore-receipt.json','files':23,'bytes':6954154},
         'candidate_restore':{'receipt':'tools/candidate-restore-receipt.json','files':14,'bytes':209484},
         'restored_context_files':CHECK['context_files'],'supplemental_inputs':supplements,
         'contract_read':'Complete f622356f contract and full 6ec1d09e reviewer dispatch read; original seven semantic groups and C05/original/root members inspected with repeated lineage metadata checked by exact pointers.',
         'author_evidence_read':'All 12 frozen author evidence files read, including validate.py as text only; no author tool executed.',
         'candidate_content_read':'Complete WP34 candidate and all342 catalog lines read; old B bytes independently compared including removed old WP34 sentence.',
         'raw_member_checks':CHECK['raw_members'],'input_verification':'tools/input-validation.json',
         'read_only_snapshots':True,'no_shared_directory_assumption':True,'new_subtasks':0,
         'initial_log_qualification':'Initial reconnaissance/text-read I/O is in platform tool history; no retroactive standalone UTC/stdout/stderr transcript invented. Saved restoration receipts retain actual HTTP UTC; later logged checks are new checks.',
         'skill_check':'Actual AGENTS.md read; no .agents/.codex skill files in fixed B or dispatch Git tree and /workspace/.agents empty.',
         'branch':'codex/r7-u05-reviewer-20261015-r1','branch_base':FREEZE['fixed_B'],
         'allowed_write_prefix':'candidates/R7-U05/evidence/reviewer/r1/',
         'no_candidate_or_formal_mutation':True,'execution':'All behavior vectors NOT_EXECUTED; no model/host/Demo/native/save/replay run.'}
for name,value in [('per-id.json',per_id),('review-input-receipt.json',receipt)]:
 with (OUT/name).open('x') as stream: json.dump(value,stream,ensure_ascii=False,indent=2);stream.write('\n')
print(json.dumps({'record_id':per_id['record_id'],'result':per_id['result'],'vectors':len(vectors),
                  'historical_groups':len(historical),'independent_context':CHECK['task_context']['actual_thread_id'],
                  'missing_input_or_independence_blockers':[],'findings_requiring_revision':[],'runtime_execution':False},indent=2))
