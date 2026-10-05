"""Write evidence metadata only; do not execute or copy reference source."""
import hashlib
import json
import pathlib
import subprocess

OUT = pathlib.Path(__file__).resolve().parent
ROOT = OUT.parents[5]
REF = pathlib.Path('/tmp/r-b14-b02-reference')
C2 = 'af39efbf32549be964cb083bd49bed6d1d5c0d2a'
BASE = '1e6b11a47370f1c7c4659a32443fc1afda597bac'
REF_SHA = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'

def git(*args, cwd=ROOT):
    return subprocess.check_output(['git', *args], cwd=cwd)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

assert git('rev-parse', 'HEAD').decode().strip() == C2
assert git('status', '--porcelain', cwd=REF) == b''
sources = [
    ('S01', 'Data/Scripts/012_Overworld/003_Overworld_Time.rb', ['1–200'], '24 tones, two clock layers, >=30 gate, switch/cache/application distinctions'),
    ('S02', 'Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb', ['440–517'], 'FLY committed prefix, optional yield, wait, ordered record clears and outer return'),
    ('S03', 'Data/Scripts/007_Objects and windows/002_MessageConfig.rb', ['550–595'], 'Fade ensure boundary; no swallowed exception or domain-record cleanup'),
    ('S04', 'Data/Scripts/012_Overworld/001_Overworld visuals/002_Overworld_Overlays.rb', ['1–68'], 'D guard before delayed timestamp/window/message/map gates'),
    ('S05', 'Data/Scripts/012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb', ['210–238', '239–312'], 'Resource selection; active splash reset255/early return versus ordinary life gate; drift excluded'),
    ('S06', 'Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb', ['1–178', '272–289', '308–329', '430–471'], 'Common timestamp order; early returns, mulch/replant distinction; old display update call; qty/counter guards and outer reset'),
    ('S07', 'Data/Scripts/012_Overworld/001_Overworld.rb', ['1–18', '80–112', '164–198', '241–255', '604–632'], 'Infection outer gate; poison premises; normal31-bit wrap and route early return; map-weather local write; escape clear'),
    ('S08', 'Data/Scripts/004_Game classes/006_Game_Character.rb', ['965–992'], 'Actual completion general notification before player post-step'),
    ('S09', 'Data/Scripts/004_Game classes/008_Game_Player.rb', ['534–559'], 'Player post-step entry and automatic-movement/interruption conditions'),
    ('S10', 'Data/Scripts/016_UI/001_UI_PauseMenu.rb', ['201–240'], 'Named ordinary FLY callers do not supply optional block; no exhaustive plugin claim'),
    ('S11', 'Data/Scripts/012_Overworld/005_Overworld_Fishing.rb', ['1–45', '87–110'], 'Common event overrides whole start; normal end cleanup; input-before-strict-timeout'),
    ('S12', 'Data/Scripts/013_Items/002_Item_Effects.rb', ['276–320'], 'Current-coordinate outgoing passage; surf exception; counter precedes encounter request'),
    ('S13', 'Data/Scripts/019_Utilities/001_Utilities.rb', ['521–540'], 'Common-event missing/negative rejection and normal true'),
    ('S14', 'Data/Scripts/014_Pokemon/001_Pokemon.rb', ['815–831'], 'Lower infection count only stage1'),
    ('S15', 'Data/Scripts/004_Game classes/005_Game_MapFactory.rb', ['91–113', '136–151'], 'Connection call after enter-map notification writes duration20'),
    ('S16', 'Data/Scripts/005_Sprites/006_Spriteset_Global.rb', ['27–41'], 'Later weather consumer reads intended type/max/duration'),
]
entries = []
for sid, p, ranges, purpose in sources:
    data = (REF / p).read_bytes()
    entries.append({'id': sid, 'repository': 'reference', 'commit': REF_SHA, 'path': p, 'git_blob': git('rev-parse', REF_SHA + ':' + p, cwd=REF).decode().strip(), 'sha256': sha(data), 'bytes': len(data), 'lines_read': ranges, 'purpose': purpose, 'mode': 'STATIC_TEXT_ONLY', 'code_executed': False})
write('source-reading.json', {'reference': {'local_path_outside_main_git': str(REF), 'origin': git('remote', 'get-url', 'origin', cwd=REF).decode().strip(), 'head': REF_SHA, 'tree': git('rev-parse', 'HEAD^{tree}', cwd=REF).decode().strip(), 'detached': git('branch', '--show-current', cwd=REF) == b'\n' or git('branch', '--show-current', cwd=REF) == b'', 'clean_at_finalization': True}, 'entries': entries, 'searches_only': ['pbFlyToNewLocation/fly_destination/LocationWindow name search across Data/Scripts', 'pbOnStepTaken/stepcount wrap/callers name search', 'fishing common-event, rod counter, infection and weather_duration name search'], 'reading_ranges_are_not_branch_coverage': True, 'reference_source_copied_into_main_git': False, 'runtime_observations': 0, 'demo_chains': 0, 'static_behavior_vectors_executed': 0, 'named_unread': 'All unlisted reference ranges/files; Scripts.rxdata and binary/serialized data; real map/event data; media/images/audio/fonts/soundfont; executables/DLLs/mkxp.json and host/capacity; eight cup-list files and pokemon_metrics samples; backup/gen; actual plugin combinations/dynamic dispatch/old aliases/EventScene/dynamic-shadow reachability and real Demo chains', 'retained_limits': ['U01–U10', 'G01–G12', 'AX01–AX20']})

old = json.loads(git('show', BASE + ':review/remediation/20261003-prepare/batches/B02/integration-review-1/finding-dispositions.json'))
affected = {'GIR-FD82-A010': ['S06'], 'GIR-FD82-C003': ['S01', 'S04', 'S05', 'S07', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16'], 'GIR-FD82-C081': ['S07', 'S08', 'S09']}
records = []
for r in old['dispositions']:
    fid = r['id']
    records.append({'id': fid, 'severity_preserved': r['severity_preserved'], 'aliases_preserved': r['aliases_preserved'], 'current_candidate': C2, 'B02_role': r['B02_role'], 'decision': 'PASS_SCOPED_PARTIAL_INTERFACE' if fid == 'GIR-FD82-C003' else ('PASS_SCOPED_INTERFACE' if fid in affected else 'NOT_AFFECTED_AT_EXACT_CANDIDATE'), 'evidence': ['input-identities.json#B02_formal13_byte_unchanged_against_accepted_predecessor', 'bookkeeping.json#catalogs', 'report.md#4-原-b02-逐-id-当前结论及剩余责任'], 'fresh_source_ids': affected.get(fid, []), 'canonical_status': 'OPEN', 'canonical_closed': False, 'prior_exact_B02_actual_report': '361e4e69126559c266a08fdf093082dbbcd83f8d', 'prior_PASS_automatically_transferred': False, 'remaining_gate': 'Exact future actual affected review and parent/A-REG/global/all-contributor gate; detailed current responsibilities in report table', 'current_B08_note': 'B08 is accepted; preserve effective31-bit constraints/global gate, do not label historical B02 WP36 residue as still unfixed' if fid == 'GIR-FD82-C081' else None})
write('finding-dispositions.json', {'run_id': '20261003-prepare', 'role': 'R-B02', 'batch_reviewed': 'B14', 'mode': 'BOUNDED_AFFECTED_CANDIDATE2', 'verdict': 'PASS_SCOPED', 'accepted_predecessor': BASE, 'reviewed_candidate': C2, 'candidate1': '47f7514765f8569ae9172bb06a2cd615e2b83b8a', 'original_B02_contributions': 12, 'dispositions': records, 'new_findings': [], 'new_blocking_findings': [], 'foreign_candidate1_findings_remain_separate': [{'id': 'B14-AFFECTED-B03-001', 'severity': 'P2'}, {'id': 'R-B14-1-001', 'severity': 'P3'}, {'id': 'B14-B04-R1-01', 'severity': 'P2'}], 'foreign_owner_gates_signed_by_this_review': False, 'whole_WP59_WP60_WP61_reapproval': False, 'canonical_required_OPEN': 229, 'canonical_CLOSED': 0, 'integration_actual': None, 'future_actual_review': 'PENDING_PARENT_EXACT_SHA_DISPATCH'})
write('execution-request-receipt.json', {'role': 'R-B02', 'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'Ultra', 'requested_speed': 'inherited Standard(default)', 'Plan_A_explicit_parameters_and_platform_accepted_task_used_as_basis': True, 'effective_model_reasoning_speed': 'UNVERIFIED', 'effective_configuration_independently_verified': False, 'configuration_probes': 0, 'quota_probes': 0, 'quota_checks_disabled_by_user': True, 'downgrade_or_acceleration_actions': 0, 'child_tasks': 0, 'reference_game_Ruby_compiler_converter_generator_deserializer_emulator_solver_execution': 0, 'historical_author_reviewer_verifier_execution': 0, 'runtime_observations': 0, 'demo_chains': 0, 'static_behavior_vectors_executed': 0, 'own_bookkeeping_scripts': 'Git/hash/text/JSON metadata only; no reference behavior functions implemented or executed', 'configuration_treated_as_independent_platform_attestation': False})
write('report-manifest.json', {'reviewed_candidate': C2, 'accepted_predecessor': BASE, 'candidate_tree': git('rev-parse', C2 + '^{tree}').decode().strip(), 'review_branch': git('branch', '--show-current').decode().strip(), 'report_sha_policy': 'Report commit SHA is delivered externally after ordinary push/readback; no self-reference', 'reviewed_candidate_branch_remote_readback': {'ref': 'refs/heads/remediation/20261003-prepare/batch-B14', 'sha_observed': C2}, 'verdict': 'PASS_SCOPED_B02_AFFECTED_INTERFACE_ONLY', 'files': [{'path': str(p.relative_to(ROOT)), 'sha256': sha(p.read_bytes()), 'bytes': p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file() and p.name != 'report-manifest.json'], 'formal_edits_by_reviewer': 0, 'public_registry_edits_by_reviewer': 0, 'reference_source_edits_by_reviewer': 0, 'future_actual_gate_pending': True})
print(json.dumps({'source_files': len(entries), 'B02_dispositions': len(records), 'verdict': 'PASS_SCOPED', 'manifest_files': len(list(OUT.iterdir()))}, ensure_ascii=False))
