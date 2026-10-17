#!/usr/bin/env python3
"""Record this root's completed reading; Git calls only bind identities.

Reading ranges and judgments below are manually attested by the actual root,
not inferred from hashing, original ledgers, helper output or command success.
Only this r1 directory is written. No reference source or business code runs.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
SOURCE = Path('/workspace/pokemon-essentials')
ACTUAL = '0eee6d141f33758eda34bd8ebad94a3e2b617f5a'
BINDING = '5ff355c53b73171a0277c95af97e1cbd40eb8b28'
LATEST = '2e2d5e6ab3f531ee902f60574b22e20fb065e04b'
REFERENCE = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
CANDIDATE = '16f986afc1c85e64131f1dc8c6f2477a79c04029'
REVIEW = '052236414f6cb350f1781efe98761f336bb43108'
commands = []

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def git(root, *argv):
    p = subprocess.run(['git', *argv], cwd=root, capture_output=True)
    commands.append({'cwd': str(root), 'argv': ['git', *argv],
                     'exit_code': p.returncode, 'stdout_bytes': len(p.stdout),
                     'stdout_sha256': sha(p.stdout),
                     'stderr_utf8': p.stderr.decode(errors='replace')})
    if p.returncode:
        raise RuntimeError(commands[-1])
    return p.stdout

def identity(root, commit, path):
    raw = git(root, 'show', commit + ':' + path)
    line = git(root, 'ls-tree', commit, '--', path).decode().strip()
    metadata, observed_path = line.split('\t')
    assert observed_path == path
    mode, kind, blob = metadata.split()
    return {'repo': str(root), 'commit': commit, 'path': path,
            'mode': mode, 'kind': kind, 'blob': blob, 'bytes': len(raw),
            'sha256': sha(raw), 'line_count': len(raw.splitlines())}, raw

def local_identity(path):
    raw = path.read_bytes()
    return {'path': str(path.relative_to(REPO)), 'bytes': len(raw), 'sha256': sha(raw)}

inventory = json.loads((HERE / 'continuation-input-inventory.json').read_text())
changes = json.loads(git(REPO, 'show', ACTUAL + ':review/remediation-eighth-20261016-prepare/integration/U06/actual-changes.json'))
contracts = {x['id']: x for x in inventory['lossless_documents'] if x['id'] != 'READSET'}
formal = []
for target in changes['targets']:
    item, raw = identity(REPO, ACTUAL, target['target'])
    assert item['sha256'] == target['new_sha256']
    formal.append({**item, 'root_reading': 'DIRECT_FULL_TEXT_READ',
                   'inclusive_ranges': [[1, item['line_count']]],
                   'completion_basis': 'Root consecutive text chunks; truncated gaps repaired in actual review, not hash-derived.',
                   'semantic_use': 'ACTUAL_U06_FULL_FILE_AND_CUMULATIVE_PRESERVATION'})
assert len(formal) == 12
assert sum(x['line_count'] for x in formal) == 3652
assert sum(x['bytes'] for x in formal) == 534372

# The following are exact ranges the root read in this continuation.
# Whole-file identity is metadata; partial ranges never become whole-file FULL.
source_ranges = {
 'Challenge_Data': ('002_Challenge_Data.rb', [[113,219]]),
 'Pokemon': ('014_Pokemon/001_Pokemon.rb', [[1040,1128],[84,97],[244,283]]),
 'Battle_Exp': ('003_Battle_ExpAndMoveLearning.rb', [[1,90],[193,271]]),
 'Battle': ('001_Battle/001_Battle.rb', [[329,411],[208,210]]),
 'StartEnd': ('002_Battle_StartAndEnd.rb', [[16,165],[4,6],[247,347],[405,512]]),
 'Priority': ('004_Battle_ActionAttacksPriority.rb', [[136,278]]),
 'AbilityEffects': ('008_Battle_AbilityEffects.rb', [[140,149],[720,735],[844,858]]),
 'UseMove': ('007_Battler_UseMove.rb', [[295,347]]),
 'Battler': ('001_Battle_Battler.rb', [[518,533],[561,566],[107,112]]),
 'SuccessChecks': ('009_Battler_UseMoveSuccessChecks.rb', [[303,390],[183,248]]),
 'ActionSwitch': ('005_Battle_ActionSwitching.rb', [[142,204],[220,226],[274,374]]),
 'WorldBattle': ('001_Overworld_BattleStarting.rb', [[142,169],[306,329],[204,206],[354,441]]),
 'GameCharacter': ('006_Game_Character.rb', [[356,360]]),
 'AI_BattlerOther': ('003_AI_MoveEffects_BattlerOther.rb', [[760,845]]),
 'AIBattler': ('010_AIBattler.rb', [[285,315]]),
 'AIUtilities': ('008_AI_Utilities.rb', [[231,382]]),
 'ChooseMove': ('005_AI_ChooseMove.rb', [[232,324],[1,231],[325,392],[393,393]]),
 'DebugScene': ('009_Battle_DebugScene.rb', [[1,106]]),
 'Challenge_Battles': ('004_Challenge_Battles.rb', [[1,144]]),
 'BattleSim': ('004_ChallengeGenerator_BattleSim.rb', [[377,438]]),
 'RecordedBattle': ('005_RecordedBattle.rb', [[1,287]]),
 'CommandPhase': ('009_Battle_CommandPhase.rb', [[1,265]]),
 'SceneAnimations': ('008_Battle_Scene_Animations.rb', [[202,215],[610,657]]),
 'ScenePlayAnimations': ('004_Scene_PlayAnimations.rb', [[313,326]]),
 'BaseAnimation': ('007_Battle_Scene_BaseAnimation.rb', [[1,64]]),
 'SpeciesFiles': ('009_Species_files.rb', [[183,244]]),
 'SceneInit': ('002_Scene_Initialize.rb', [[1,11],[14,92],[183,190]]),
 'Scene': ('001_Battle_Scene.rb', [[230,267],[408,419],[7,8],[36,53],[79,130],[164,180]]),
 'PictureEx': ('010_PictureEx.rb', [[1,185],[311,335],[357,548]]),
 'Audio': ('008_Audio/001_Audio.rb', [[1,154]]),
 'AudioPlay': ('002_Audio_Play.rb', [[1,39],[202,219]]),
 'FileTests': ('001_FileTests.rb', [[109,117],[181,193],[203,231],[238,242]]),
 'GameSystem': ('002_Game_System.rb', [[237,249]]),
 'RubyUtilities': ('002_RubyUtilities.rb', [[390,406]]),
 'BattlerChangeSelf': ('003_Battler_ChangeSelf.rb', [[1,151]]),
 'Stat': ('008_Stat.rb', [[1,119]]),
 'AttackPhase': ('010_Battle_AttackPhase.rb', [[1,202]]),
 'AIcore': ('001_Battle_AI.rb', [[10,116]]),
 'AITrainer': ('009_AITrainer.rb', [[28,99]]),
 'Target': ('017_Target.rb', [[1,64]]),
 'PBSmoves': ('PBS/moves.txt', [[5802,5813]]),
 'BattleSettings': ('002_BattleSettings.rb', [[4,19]]),
 'WorldBattleIntro': ('002_Overworld_BattleIntroAnim.rb', [[51,152]]),
 'SceneMenus': ('005_Battle_Scene_Menus.rb', [[459,502]])
}
source_paths = git(SOURCE, 'ls-tree', '-r', '--name-only', REFERENCE).decode().splitlines()
source = []
source_by_key = {}
for key, (suffix, ranges) in source_ranges.items():
    matches = [p for p in source_paths if p.endswith(suffix)]
    assert len(matches) == 1, (key, matches)
    item, raw = identity(SOURCE, REFERENCE, matches[0])
    lines = raw.splitlines(keepends=True)
    slices, covered = [], set()
    for first, last in ranges:
        assert 1 <= first <= last <= len(lines), (key, first, last, len(lines))
        selected = b''.join(lines[first-1:last])
        covered.update(range(first,last+1))
        slices.append({'inclusive_lines': [first,last], 'bytes': len(selected),
                       'sha256': sha(selected)})
    item.update({'key': key, 'root_reading': 'DIRECT_TEXT_RANGES_READ',
                 'ranges': slices, 'entire_file_in_read_ranges': len(covered) == len(lines),
                 'outside_range_credit': 'NONE',
                 'qualification': 'Static source read only; a complete named method may be inside a partial outer method/file. No old reader FULL is inherited.'})
    source.append(item)
    source_by_key[key] = item

formal_suffix_ranges = [
 ('wp36-wild-encounters-and-modifiers.md',[[112,164]],'U05 Repel collection vs battle populations'),
 ('wp15-resource-matching-and-audio.md',[[1,193]],'U08 localization/resource/audio boundary'),
 ('wp26-acquisition-gifts-and-script-trade.md',[[32,62],[134,167]],'U09 recording storage attribution'),
 ('wp76-facility-content-generation-and-simulation.md',[[145,172]],'U09/debug default AI vs direct helper'),
 ('wp28-item-use-and-training.md',[[227,232],[342,358]],'Ordinary lawful EV domain'),
 ('wp54-entry-eligibility-level-adjustment-and-clauses.md',[[72,105]],'Facility eligibility domain'),
 ('wp54-entry-rules-and-cup-data.md',[[72,105]],'Facility entry data scope'),
 ('wp55',[[94,105]],'Facility default non-internal early gate'),
 ('wp51-ai-action-selection-and-skill.md',[[127,155]],'AI generic score dispatch consumer'),
 ('wp48-ability-calculation-modifiers.md',[[35,100]],'Ability bracket vs refusal and stage behavior'),
 ('wp16-world-rendering-and-visual-transitions.md',[[293,313]],'Parallel scheduler/update completion'),
 ('wp74-battle-animation-authoring-and-exchange.md',[[1,41],[297,355]],'Shared animation player vs native presentation policy'),
 ('scope-statement.md',[[88,127]],'Static source/host/material limits'),
 ('user-interface-wp17-63-65-66-67-68-69-70-71.md',[[360,426]],'Complete relevant K01–59/HP01–04 families'),
 ('combat-requirements-wp54-55-56-58.md',[[1,11],[156,190]],'RC01–29 identity and recording boundaries'),
 ('engine-overworld/wp16-pre-battle-transitions.md',[[1,126]],'Outer wrapper prefixes and normal-return boundary'),
 ('wp61-field-passive-effects-and-blackout.md',[[1,203]],'After-battle animation direction vs blackout and Repel state'),
 ('audit/source-traceability.md',[[476,489],[928,940],[1023,1035],[1036,1048],[1049,1061],[1062,1075],[1144,1156],[1224,1236],[1343,1355]],'All relevant current public target entries'),
 ('planning/feature-matrix.md',[[182,182],[199,199],[247,247]],'Current relevant public feature rows')]
formal_paths = git(REPO, 'ls-tree', '-r', '--name-only', ACTUAL).decode().splitlines()
consumers = []
for suffix, ranges, purpose in formal_suffix_ranges:
    if suffix in ['wp54','wp55','wp51','wp48']:
        matches = [p for p in formal_paths if p.startswith('deliverables/final-specification-set/combat-requirements/'+suffix+'-') and p.endswith('.md')]
    else:
        matches = [p for p in formal_paths if p.endswith(suffix) and
                   (p.startswith('deliverables/final-specification-set/') or
                    p.startswith('audit/') or p.startswith('planning/'))]
    assert len(matches) == 1, (suffix,matches)
    item, raw = identity(REPO,ACTUAL,matches[0])
    lines = raw.splitlines(keepends=True)
    covered = set()
    slices = []
    for first,last in ranges:
        assert 1 <= first <= last <= len(lines), (suffix,first,last,len(lines))
        selected = b''.join(lines[first-1:last]);covered.update(range(first,last+1))
        slices.append({'inclusive_lines':[first,last],'bytes':len(selected),'sha256':sha(selected)})
    consumers.append({**item,'root_reading':'DIRECT_TEXT_RANGES_READ',
                      'ranges':slices,'purpose':purpose,
                      'entire_file_in_read_ranges':len(covered)==len(lines),
                      'outside_range_credit':'NONE'})

protocol_paths = [
 'AGENTS.md',
 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md',
 'review/remediation-eighth-20261016-prepare/coordination/actual-integration-review-prompt.md',
 'review/remediation-eighth-20261016-prepare/integration/U06/reviewer-entry.md',
 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/history-qualifications.json',
 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/accepted-facts-and-mandatory-companions.json',
 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/policy-and-preservation.json']
protocol = []
for path in protocol_paths:
    item,raw = identity(REPO,BINDING,path)
    protocol.append({**item,'root_reading':'DIRECT_FULL_TEXT_READ'})

root = {'context':'current cloud root /root','thread':'01a14a49-64c1-764e-b294-c70bb87680fd',
        'turn':'01a14a49-6d4e-7396-ae92-2903e357f766',
        'creation_evidence':'continuation-parent-creation-receipt.json',
        'created_requested_configuration':{'model':'gpt-6.1-sol','thinking':'ultra','service_tier':'default'},
        'runtime_echo':{k:'UNVERIFIED_NOT_EXPOSED' for k in ['model','effort','tier','speed','Fast']},
        'semantic_helper_count':0,'mechanical_helper_semantic_credit':0,
        'independent_from_author_and_integrator':True,'continuation_adds_new_reviewer':False}
reading = {
 'schema':'r8-u06-actual-continuation-reading-ledger/v1',
 'recorded_utc':datetime.now(timezone.utc).isoformat(),
 'manual_attestation_rule':'The root attests actual reading reflected in conversation; scripts only add fixed byte identities, no automatic FULL credit.',
 'bookkeeping_repairs':[
     {'attempt':'Initial identity binding for consumer suffix wp36','result':'Guard rejected specs/ duplicate alongside formal deliverable; selection restricted to formal/public roots.'},
     {'attempt':'Short wp54/wp51 consumer suffixes','result':'Guards rejected multiple current files; exact filenames used and both read WP54 files retained.'},
     {'attempt':'RC catalog requested read range156:192','result':'Identity guard established actual EOF190; effective previously returned read range recorded156:190.'}],
 'root':root,'input_binding':BINDING,'actual_snapshot':ACTUAL,'latest_registration':LATEST,
 'protocol_and_companions':protocol,'all12_actual_formal_full_reads':formal,
 'actual_formal_totals':{'files':12,'lines':3652,'bytes':534372},
 'complete_contract_records':[
     {k:v for k,v in row.items() if k!='tree'} | {'root_reading':'COMPLETE_CURRENT_RECORD_READ_WITH_WRAPPER_AND_SEVEN_GROUPS'}
     for row in contracts.values()],
 'complete_batch_readset':{
     'path':'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/batches/R8-U06/readset.json',
     'root_reception':'Complete top-level/current contents, source60, root64, companions8, fourteen contract bindings, delta72 and inherited9 metadata; conditional F05 complete.',
     'source_locator_credit':'Reading source locators is not source text FULL.',
     'original_inherited_readset_reception':'60/64/8 exact identity mapping; old10 contracts exact current leaves plus root-read17 full original nonidentity differences. Old status/freeze retained in purpose.',
     'delta_evidence':'continuation-inherited-readset-delta.json'},
 'reviewer_prompt_reception':{
     'path':'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/batches/R8-U06/reviewer-prompt.md',
     'root_reception':'Complete preamble, assignment, all14 embedded entire contract records and final notes.',
     '28_embedded_contract_equivalences':inventory['fenced_equality_summary']},
 'actual_changes':{'patch':'review/remediation-eighth-20261016-prepare/integration/U06/actual-changes.patch','patch_lines_read':[1,220],
                   'records_read':'ALL14 plus ALL12 targets, top-level facets and public contribution declarations'},
 'direct_reference_read_ranges':source,'necessary_formal_consumers_and_public_indexes':consumers,
 'candidate_and_review_reception':{
     'candidate':CANDIDATE,'candidate_files':27,'independent_review':REVIEW,'review_files':19,
     'mirror_reuse':'Exact12 source mirror byte identities; full semantic root reading is of actual formal files above.',
     'Markdown_diff_script_semantics':'Complete candidate README, independent-review, tagging-handoff, patch196 lines, prepublication, verify_candidate.py; complete review report/results, identity-scope, qualification-reception, full-semantic154 lines, battle-controls60 lines, optional-audio45 lines, verify_identity.py218 lines. Scripts read as text, not replayed into old directories.',
     'JSON_qualification_narrative':{
         **local_identity(HERE/'continuation-qualification-narrative.jsonl'),
         'root_reading':'ALL704 original narrative value rows, Unicode chars0:144634, consecutive repaired chunks.',
         'identity_and_navigation_projection':'continuation-qualification-projection.json',
         'credit':'NARRATIVE_CONTENT_AND_QUALIFICATION_RECEPTION; not whole-carrier literal FULL or old source reader credit.'},
     'identity_transport_tool_logs':'Complete bytes parsed and identities checked mechanically. No source or human whole-carrier semantic FULL inferred from 527/821 successful mechanical commands.',
     'all1856_pointer_checks':inventory['pointer_check_counts'],
     'all79_owning_commit_identities':'continuation-final-mechanical.json#/payload_79',
     'existing_registry_difference':'continuation-final-mechanical.json#/existing_registry_successor_difference',
     'historical_role_limits':'Original NATIVE helper tiers remain their original unverified/not-set qualification. This root neither uses parent tier transfer nor counts those helpers as fresh qualified actual semantic reviewers.'},
 'credit_exclusions':['No automatic credit from navigation log ranges, hashing, JSON parse or pointer resolution.',
                     'No root claim of full old143 source units/67 paths or whole global history archive.',
                     'No credit for truncated output until root separately repaired the missing range.',
                     'No independent vote from native mechanical helper or continued turn.',
                     'No business Ruby/game/host/media/save/replay execution.'],
 'business_execution':'NOT_EXECUTED','identity_commands':commands}

table = []
for line in (HERE/'continuation-report.md').read_text().splitlines():
    if line.startswith('| GR8-'):
        cells = [v.strip() for v in line.strip('|').split('|')]
        assert len(cells)==4 and cells[2]=='PASS'
        table.append(cells)
assert len(table)==14
assert [x[0] for x in table]==changes['required_ids']+changes['selected_optional_ids']
record_sources = {
 'GR8-CRE-001':['Challenge_Data','Pokemon','Battle_Exp','Battle','StartEnd','Stat'],
 'GR8-COM-001':['Priority','AbilityEffects','SuccessChecks'],
 'GR8-COM-002':['StartEnd','WorldBattle','WorldBattleIntro','SceneInit','SceneMenus','CommandPhase'],
 'GR8-COM-003':['StartEnd','Priority','CommandPhase','ChooseMove','AttackPhase','SceneInit','Scene','SceneMenus','Battler'],
 'GR8-COM-004':['WorldBattle'],
 'GR8-COM-005':['WorldBattle','GameCharacter'],
 'GR8-COM-006':['UseMove','Battler','BattlerChangeSelf'],
 'GR8-COM-007':['SuccessChecks','AbilityEffects','BattleSettings'],
 'GR8-COM-008':['Priority','ActionSwitch','AbilityEffects','StartEnd'],
 'GR8-AI-001':['AI_BattlerOther','AIBattler','ChooseMove','AIcore','AITrainer','Target','PBSmoves'],
 'GR8-UI-FAINT-AUDIO-001':['SceneAnimations','ScenePlayAnimations','BaseAnimation','SpeciesFiles','PictureEx','Audio','AudioPlay','FileTests','GameSystem','RubyUtilities','BattlerChangeSelf'],
 'GR8-AI-002':['AIUtilities'],
 'GR8-UI-BATTLE-END-MARK-001':['Scene','SceneAnimations','SceneInit'],
 'GR8-COM-RECORD-DEBUG-RNG-001':['DebugScene','Challenge_Battles','BattleSim','RecordedBattle','CommandPhase','ChooseMove']}
records = []
change_by_id = {x['id']:x for x in changes['records']}
for finding_id,category,verdict,basis in table:
    c=contracts[finding_id]; actual=change_by_id[finding_id]
    records.append({'id':finding_id,'classification':actual['classification'],
                    'severity':actual['severity'],'selected_optional':actual['selected_optional'],
                    'actual_verdict':verdict,'actual_integrated_PASS':True,
                    'locations':actual['locations'],
                    'contract':{k:c[k] for k in ['carrier_commit','carrier_path','carrier_pointer','parsed_value_canonical_sha256']},
                    'independent_actual_reasoning':basis,
                    'reference_evidence':[{'key':key,'repo':source_by_key[key]['repo'],
                                          'commit':REFERENCE,'path':source_by_key[key]['path'],
                                          'ranges':[x['inclusive_lines'] for x in source_by_key[key]['ranges']]}
                                         for key in record_sources[finding_id]],
                    'full_actual_file_evidence':'continuation-reading-ledger.json#/all12_actual_formal_full_reads',
                    'candidate_correspondence':'continuation-final-mechanical.json#/formal_targets_12',
                    'candidate_stage_verdict_received':'PASS_CANDIDATE_ONLY',
                    'blocking_dependencies':[],'business_execution':'NOT_EXECUTED',
                    'ACCEPTED_registered_by_this_review':False,'CLOSED_registered_by_this_review':False})
result={'schema':'r8-u06-actual-continuation-results/v1',
        'recorded_utc':datetime.now(timezone.utc).isoformat(),'batch':'R8-U06',
        'actual_verdict':'PASS','actual_integrated_PASS':True,
        'input_binding':BINDING,'actual_snapshot':ACTUAL,'latest_registration':LATEST,
        'candidate':CANDIDATE,'candidate_independent_review_source':REVIEW,
        'root':root,'scope':'11 required +3 selected optional; actual static integration only',
        'counts':{'required':11,'required_P2':2,'required_P3':9,'selected_optional':3,'actual_PASS':14,'actual_FAIL':0,'actual_BLOCKED':0},
        'records':records,'unresolved_U06_blocking_dependencies':[],
        'resolved_historical_blocks':[
            {'id':'B01','old_state':'BLOCKED','current_state':'RESOLVED','evidence':'continuation-parent-creation-receipt.json','qualification':'Parent actual creation attestation; runtime echo remains UNVERIFIED.'},
            {'id':'B02','old_state':'INCOMPLETE','current_state':'COMPLETED','evidence':'continuation-reading-ledger.json','qualification':'Independent complete actual12 and14 contracts plus required consumers; no native helper semantic credit.'}],
        'remaining_downstream_dependencies':[
            {'dependency':'Owner receipt and batch acceptance registration','blocks_this_actual_static_PASS':False,'owner_action_required':True},
            {'dependency':'Tagging repair and independent tagging/final cumulative whole-round acceptance','blocks_this_actual_static_PASS':False,'not_signed_by_this_review':True},
            {'dependency':'Other-batch independent acceptance','blocks_this_actual_static_PASS':False,'not_signed_by_this_review':True},
            {'dependency':'Game/host/media/save/replay and static behavior-vector execution','blocks_this_actual_static_PASS':False,'qualification':'NOT_EXECUTED; no runtime equivalence claim.'}],
        'cross_batch_interfaces_received':['X02 Repel vs battle actor collections','X03 localization slots vs faint audio assets','X04 ordinary lawful EV/gift domains vs internal battle growth','X06 recording stream/storage vs direct DebugScene helper and default AI','X09 full WP67-A lifecycle and shared catalogs'],
        'public_contributions_required':[],'historical_roots_reopened':[],
        'six_batch_fixed_evidence_preserved':True,
        'write_scope':'review/remediation-eighth-20261016-prepare/reviews/actual-U06/r1/',
        'formal_or_coordination_main_tag_writes':False,'force_push':False,
        'ACCEPTED_registered_by_this_review':False,'CLOSED_registered_by_this_review':False,
        'business_execution':'NOT_EXECUTED','all_behavior_vectors':'NOT_EXECUTED',
        'evidence':['continuation-report.md','continuation-reading-ledger.json','continuation-final-mechanical.json','continuation-inherited-readset-delta.json','continuation-input-inventory.json'],
        'publication_qualification':'Successor publication receipt binds its already-existing payload commit. Final output commit is supplied externally, not invented here.'}
for name,obj in [('continuation-reading-ledger.json',reading),('continuation-results.json',result)]:
    (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'actual_verdict':result['actual_verdict'],'records':len(records),
                  'formal_totals':reading['actual_formal_totals'],
                  'source_range_paths':len(source),'consumer_paths':len(consumers),
                  'identity_commands':len(commands)},ensure_ascii=False))
