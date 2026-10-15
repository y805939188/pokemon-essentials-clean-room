"""Collect bounded immutable-input identities and honest execution qualifications."""
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[4]
E = Path(__file__).parent
C = Path('/workspace/r7-context/R7-U13-author')
BOOT = Path('/workspace/r7-bootstrap/R7-U13-author')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
P = '6ec1d09e9c470954964d72761c83a760ef4f0364'
C2 = '4580645dfbfec4a3c7ccbad56ae293cc619b0d25'

def ident(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

def git_file(commit,path):
    return subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT)

def write(name,obj):
    (E/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

integrity=[]
for rel in ['tools/restore_container_context.py','recovery/batches/R7-U13.json']:
    path=BOOT/rel
    actual=path.read_bytes()
    fixed=git_file('658488c81f1f3181a488298ab27850c8af951d73','review/remediation-seventh-20261015-prepare/'+rel)
    assert actual==fixed or actual==fixed+b'\n'
    row={'path':str(path),'before':ident(actual),'pinned':ident(fixed),'before_exact_match':actual==fixed,
         'difference':'one extra trailing LF introduced by bootstrap text materialization' if actual!=fixed else 'none'}
    if actual!=fixed:path.write_bytes(fixed)
    assert path.read_bytes()==fixed
    row['after_exact_match']=True
    integrity.append(row)
write('bootstrap-integrity.json',{'pinned_commit':'658488c81f1f3181a488298ab27850c8af951d73','files':integrity,
    'qualification':'Initial restoration used identical program/plan content plus one terminal LF; original fresh receipt retained. Exact pinned bytes restored before resume verification; no evidence bytes overwritten.'})
command=['python3',str(BOOT/'tools/restore_container_context.py'),'--plan-directory',str(BOOT/'recovery/batches'),'--batch','R7-U13','--destination',str(C),'--resume']
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
result=subprocess.run(command,capture_output=True,text=True)
write('recovery-command.json',{'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'argv':command,'stdout':result.stdout,'stderr':result.stderr,'exit_code':result.returncode})
assert result.returncode==0,result.stderr
receipts=[]
for path in sorted(C.glob('recovery-receipt-*.json')):
    data=path.read_bytes();(E/path.name).write_bytes(data)
    receipts.append({'path':path.name,**ident(data)})

plan=json.loads((BOOT/'recovery/batches/R7-U13.json').read_text())
scopes={
 'inputs/reference/mkxp.json':'SOURCE_STATIC: L57–72 (required L64–66)',
 'inputs/reference/Data/Scripts/001_Technical/002_Files/001_FileTests.rb':'SOURCE_STATIC: L109–115,181–236,262–273',
 'inputs/reference/Data/Scripts/008_Audio/002_Audio_Play.rb':'SOURCE_STATIC: L1–68,102–118,152–168,202–233',
 'inputs/reference/Data/Scripts/004_Game classes/002_Game_System.rb':'SOURCE_STATIC: L44–149,153–249',
 'inputs/reference/Data/Scripts/008_Audio/001_Audio.rb':'SOURCE_STATIC: full L1–154; duration, no bank parser assertion',
 'inputs/reference/Game.exe':'BYTE_IDENTITY_ONLY: full identity; native code semantically UNREAD in this author context; prior finite map read separately',
 'inputs/project/AGENTS.md':'PROJECT_INSTRUCTION: full',
 'inputs/project/deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md':'SOURCE_STATIC_FORMAL: full L1–222',
 'inputs/project/deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md':'SOURCE_STATIC_FORMAL: B04-R section L400–436; all remaining bytes identity-checked only',
 'inputs/project/planning/feature-matrix.md':'SOURCE_STATIC_FORMAL: F05-01/F05-02 with neighboring context L162–181; other bytes identity only',
 'inputs/project/audit/source-traceability.md':'SOURCE_STATIC_FORMAL: T-WP15-01 L313–326 and adjacent headings; other bytes identity only',
 'evidence/tasks/R7-C13/inputs/evidence/received-final-proposals/GR7-D07-001/counter-review.json':'RECEIVED_NON_AUTHOR_EVIDENCE: full; original C11 review, no new independent review credit',
 'evidence/tasks/R7-C13/inputs/delta-j16/findings.json':'ROOT_RECEPTION: /records/30 including original D07 proposal/vectors; unrelated records not semantically read',
 'evidence/tasks/R7-C13/inputs/late-reception/evidence/late-author-payload-receptions.json':'ROOT_RECEPTION: /records/3; remaining records identity only',
 'evidence/tasks/R7-C17/limits-and-alias-reception.json':'BOUNDARY_RECEPTION: full L01–L14, overlays, aliases and execution qualifications',
 'evidence/tasks/R7-C13/identity-index.json':'IDENTITY: exact ten batch read identities; remaining entries identity only',
 'evidence/tasks/R7-C13/raw-binding-manifest.json':'IDENTITY_BINDING: schema and targeted D07 lookup; no matching D07 binding; other contents not semantically reviewed',
 'evidence/tasks/R7-C13/input-manifest.json':'IDENTITY_BINDING: schema and first entries; no inherited reading of listed reports',
 'dispatch/delegation/contracts/R7-U13.json':'CONTRACT: complete seven groups and all path clauses',
 'dispatch/delegation/prompts/R7-U13-author.md':'CONTRACT: full; no-submit restriction superseded only by fixed P dispatch/user authorization',
 'dispatch/delegation/prompts/R7-U13-reviewer.md':'BYTE_IDENTITY_ONLY: role not invoked; reviewer not created'
}
reads=[]
for row in plan['artifacts']+plan['evidence']+plan['fixed_read_inputs']:
    data=(C/row['local_path']).read_bytes();actual=ident(data)
    assert all(actual[k]==row[k] for k in actual)
    reads.append({'path':str(C/row['local_path']),'original_locator':{k:row[k] for k in ['repository','commit','path']},
                  **actual,'reading_scope':scopes[row['local_path']]})

prefix='review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/'
index=json.loads(git_file(C2,prefix+'payload-index.json'))
targeted=[]
for logical in ['tasks/R7-C11/challenges/native/forward-map.json','tasks/R7-D07/findings.json']:
    row=next(x for x in index['logical_files'] if x['logical_path']==logical)
    encoded=git_file(C2,prefix+row['transport_path']);data=gzip.decompress(encoded)
    assert (C/'evidence'/logical).read_bytes()==data
    assert all(ident(data)[k]==row[k] for k in ident(data))
    targeted.append({'publication_commit':C2,'logical_path':logical,'transport_path':prefix+row['transport_path'],
                     'encoded':ident(encoded),'decoded':ident(data),
                     'reading_scope':'full prior finite native forward map, no new machine-code interpretation' if 'forward-map' in logical else 'full original D07 payload /findings/0; proposal, six vectors and boundary qualifications'})
write('targeted-recovery.json',{'method':'git show exact fixed compressed object, gzip decode, verify bytes/SHA256/blob against exact logical-path payload-index entry',
      'whole_core_scanned':False,'manifest_80MB_read':False,'files':targeted,'semantic_execution_credit':False})
for commit,path,scope in [
 (P,'review/remediation-seventh-20261015-prepare/delegation/parallel-dispatch/authors/R7-U13-author.md','CONTRACT: full fixed user-selected dispatch; nested older preparation hash is historical, P selected by user controls'),
 ('f622356f3beb9e84ea8cff9db07c7fb382565d3f','review/remediation-seventh-20261015-prepare/delegation/conflict-groups.json','CONFLICT: full; CG01/CG04/CG07 govern this batch'),
 ('658488c81f1f3181a488298ab27850c8af951d73','review/remediation-seventh-20261015-prepare/recovery/independent-containers.md','CONTRACT: full cross-container recovery instructions')]:
    reads.append({'original_locator':{'repository':'y805939188/pokemon-essentials-clean-room','commit':commit,'path':path},**ident(git_file(commit,path)),'reading_scope':scope})
write('read-set.json',{'schema':'r7-u13-author-read-set.v1','reads':reads,'targeted_reads':targeted,'receipts':receipts,
 'skills_check':{'repository_dot_agents_directory':'ABSENT at B and P','workspace_dot_agents_directory':'empty/read-only mount','executor_skill_catalog':'empty','relevant_skill_available':False,'qualification':'No named local .agents/skills file was provided or found; project AGENTS.md fully read. No approval/parallel-agent requirement inferred.'},
 'reading_log_qualification':'Initial read-only terminal calls are preserved in platform tool I/O; their separate local UTC/stdout/stderr files were not recorded. This ledger does not backfill timestamps or create semantic credit. Public logged checks and exact replayed input identities begin in commands.jsonl; raw reference source is not copied into candidate evidence.'})

counter=json.loads((C/'evidence/tasks/R7-C13/inputs/evidence/received-final-proposals/GR7-D07-001/counter-review.json').read_text())['findings'][0]
original=json.loads((C/'evidence/tasks/R7-D07/findings.json').read_text())['findings'][0]
root_record=json.loads((C/'evidence/tasks/R7-C13/inputs/delta-j16/findings.json').read_text())['records'][30]
assert original['regression_vectors']==root_record['original_proposal']['regression_vectors']
observations=[
 '§7 note and S01 preserve the supplied identity only; native consumption is explicitly unknown.',
 'Controlled record80/pitch100/options100 and no override are stated in S01; unchanged §6.1/6.2 preserve normal requests without sound certification.',
 'S01 varies only a paper declared identity to absent-bank.sf2; no reference/config mutation or dynamic outcome occurs.',
 'Original B04-R17 bytes preserved: broad six suffixes and specialized four suffixes/literal path remain distinct; FileTests L109–115 read.',
 'Original generic nil/empty-name early returns retained; S01 explicitly rejects bank initialization/free/cancel inference.',
 'Paper trace of Game_System L60–99: registration B precedes request12; ArgumentError retry0 then ordinary error leaves paused and saved12 intact, with frame-reset and resume cleanup unreached. No rollback or SF2-handler claim.',
 'Original missing BGM/BGS registration without that request remains; ordinary WAV control preserves request behavior but does not remove the bank declaration.',
 '§7 and S01 make no future format/backend/API/legacy-profile selection; GR6-POL-001 remains separate.'
]
vectors=[]
for i,v in enumerate(counter['regression_vectors']):
    vectors.append({**v,'source_pointer':'counter-review.json#/findings/0/regression_vectors/'+str(i),
                    'stage':'DERIVED_VECTOR','behavior_result':'NOT_EXECUTED','author_document_review':observations[i]})
d07_notes=[observations[0],observations[1],
 'Declaration and request do not certify SF2 acceptance/guards/synthesis; §7 states all unknowns and preserves earlier L09 structure facts.',
 observations[4],
 'Source L51–59 permits only the position0 ArgumentError retry; ordinary failure or SF2 handling is not generalized. C11-V06 keeps the more precise double-failure prefix.',
 observations[6]]
for i,v in enumerate(original['regression_vectors']):
    vectors.append({**v,'source_pointer':'tasks/R7-D07/findings.json#/findings/0/regression_vectors/'+str(i),
                    'stage':'DERIVED_VECTOR','behavior_result':'NOT_EXECUTED','author_document_review':d07_notes[i]})
vectors.append({'id':'GR7-D07-001-S01','stage':'DERIVED_VECTOR','execution':'DERIVED_VECTOR / NOT_EXECUTED',
                'behavior_result':'NOT_EXECUTED','catalog_path':'candidates/R7-U13/deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md',
                'qualification':'One additional declaration vector; original fourteen vectors above retain IDs, premises, expected results and execution qualifications.'})
write('per-id.json',{'schema':'r7-u13-author-per-id.v1','batch_id':'R7-U13','records':[{
 'id':'GR7-D07-001','root_classification':'required','priority':'P3','root_status_preserved':'REQUIRED_OPEN_FOR_MANUAL_UPDATE',
 'author_status':'CANDIDATE_READY_NOT_REVIEWED','original_non_author_decision':{k:v for k,v in root_record['independent_adjudication'].items() if k!='decision_record'},
 'minimum_contract':counter['minimal_correction'],'preserved_scope':counter['must_preserve'],'read_set':'read-set.json',
 'write_set':'artifact-manifest.json#/artifacts','conditional_writes':[],'conditional_anchors_untouched':['WP15 §11','F05-01'],
 'normal_cancel_failure_partial':counter['outcomes'],
 'precise_partial_prefix':observations[5],'acceptance_document_checks':[{'id':v['id'],'check':v['check'],'author_result':'DOCUMENTARY_CHECK_ONLY; NOT_INDEPENDENT_ACCEPTANCE' if v['id']!='C11-A07' else 'PENDING_DIFFERENT_ACTUAL_CONTEXT_REVIEW'} for v in counter['acceptance']],
 'vectors':vectors,'author_blocking_predecessors':[],'open_dependencies':[
  {'id':'CG01','path':'audit/source-traceability.md','status':'OPEN','owner':'R7-I','gate':'serial clause integration and fresh R7-IR'},
  {'id':'CG04','path':'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md','status':'OPEN','owner':'R7-I','gate':'serial clause integration and fresh R7-IR'},
  {'id':'CG07','path':'planning/feature-matrix.md','status':'OPEN','owner':'R7-I','gate':'serial clause integration and fresh R7-IR'},
  {'id':'candidate-non-author-review','status':'OPEN','owner':'R7-I','gate':'freeze candidate-input.json and use a different actual ultra reviewer context'},
  {'id':'L04/L09-native-audio','status':'OPEN','gate':'actual native config supply/selection/parse/dispatch, bank acceptance/guards/synthesis/sound remain unknown; known finite SF2/readable/native facts retained'},
  {'id':'history-direct-transitive','status':'OPEN','gate':'R7-I reception and dependency/historical-case checks; no old56/92 closure promotion'}],
 'execution':{'SOURCE_STATIC':'named configuration and scoped script/formal reads only','DERIVED_VECTOR':'15 paper/documentary vectors, behavior NOT_EXECUTED','TOOL_VALIDATION':'identity, scope and transport checks only','REFERENCE_OBSERVATION':0,'independent_full_behavior_model':0,'game_host':0,'Demo':0,'native_media':0,'synthesis':0,'sound':0,'real_save_replay':0},
 'boundaries':{'L01_L14':'RETAINED','old56_92':'UNCHANGED','progress_denominator':'27 items / 13 batches; author candidate is not accepted progress','unselected_optional_navigation_policy':'NOT_ADOPTED','GR6-POL-001':'INDEPENDENT_POLICY_UNCHANGED'},
 'configuration':'execution-context.json; effective model/effort/tier/speed individually UNVERIFIED',
 'tool_failure_history':[{'event':'first build exited1 on feature-matrix column-count assertion after writing three isolated mirrors','resolution':'corrected column indices/count, reused only byte-identical partial mirrors, completed four mirrors; both exits preserved in commands.jsonl','reference_or_host_execution':0}],
 'approval_or_acceptance_claim':False
}]})
print(json.dumps({'status':'EVIDENCE_COLLECTED','bounded_receipts':receipts,'read_entries':len(reads),'targeted_entries':len(targeted),'vectors_retained':14,'new_catalog_vectors':1,'all_behavior_results':'NOT_EXECUTED','bootstrap_exact_after':True},ensure_ascii=False,indent=2))
