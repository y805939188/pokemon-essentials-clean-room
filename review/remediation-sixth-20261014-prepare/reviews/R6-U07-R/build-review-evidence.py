"""Package the reviewer's written assessment; tools do not decide semantics."""
import datetime
import hashlib
import json
import pathlib
import subprocess
from fractions import Fraction as F

ROOT = pathlib.Path('/workspace/r6-u07-review')
OUT = pathlib.Path(__file__).parent
PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
PUB = '6f6521983006519a0b55a5414177c71a2b59810e'
BASE = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
PREFIX = 'review/remediation-sixth-20261014-prepare/'


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def write(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def identity(commit, path):
    b = git('show', commit + ':' + path)
    return {'commit': commit, 'path': path, 'bytes': len(b),
            'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()}


contract_bytes = git('show', PREP + ':' + PREFIX + 'contracts/R6-U07.json')
contract = json.loads(contract_bytes)
report = (OUT / 'report.md').read_text()
bindings = {'core': '6c4966cb1e9e7936d33faa2f79aa2ff368d66492',
            'publication': PUB, 'workspace_tree': '53f252f3c2de955f736cadd6180e9c84b92eab79',
            'candidate_directory_tree': '13ab6f277dba32ba4d4535aca1f8fc450346dec9'}
vectors = [
    [('normal_0_2', 'unlocked user patterns at 0/2', 'count 2; Delete 0 allowed'),
     ('renumber_2_60', 'ordinary renumber 2→60', 'two stored users; count 1; Delete 0 refused; no deletion'),
     ('renumber_back', '60→2', 'count 2 and allowed behavior restored'),
     ('last_or_locked', 'only slot0; separately locked slot', 'refused'),
     ('ordinary_pattern', 'unlocked ordinary pattern', 'last-user gate does not reject'),
     ('missing_slot', 'selected nonexistent slot', 'prior presence gate; no invented successful deletion'),
     ('clear_and_cross_frame', 'Clear / cross-frame tool', 'current-frame guard; refused Clear retains X/Y/pattern/focus/lock'),
     ('cancel_and_ranges', 'cancel renumber; snapshot/TAB/render consumers', 'no renumber; distinct storage/copy/TAB/render ranges preserved')],
    [('same_object', 'normal same-member Focus Target then add cel', 'member position 1 and new cel focus 1'),
     ('delete_back_focus', 'A position4, valid bitmap, Delete→BACK→Focus Target', 'collection B position1, canvas A position4'),
     ('new_cel_save_export', 'add cel after detachment, save/export', 'new cel on A focus4; persistence/export sees B1, excludes A edit'),
     ('focus_cancel', 'valid current member, Focus cancellation', 'neither position changed'),
     ('reload', 'explicit Load B', 'canvas rebinds; later new cel uses B1'),
     ('shrink_nil', 'selected member nil after shrink', 'failure before Focus menu; host result unknown'),
     ('cache_clear', 'old collection references still held', 'clearing cache changes later lookup only, no rollback')],
    [('moving_user', 'captured center128,224; user-focused slot0 X200 and ordinary slot2 X128', 'requests 200/128; preview border requests264/192'),
     ('target', 'analogous target-focused ordinary particle', 'uses captured target center'),
     ('screen', 'screen-focused particle', 'independent of moving battler center'),
     ('both', 'both-focused particle', 'uses established line transform'),
     ('stationary', 'no battler movement', 'ordinary prior result preserved'),
     ('ball_burst', 'explicit target-origin override', 'specified override is a separate reachable exception'),
     ('cleanup', 'normal vs exceptional exit', 'normal restoration retained; exception cleanup not guaranteed')],
    [('all_11', 'each Batch constructor and consumer', 'all independent ranges/defaults enumerated in report'),
     ('opacity_default', 'old opacity17; only check opacity', 'writes255'),
     ('independent_zoom', 'only check Zoom X', 'writes100; Zoom Y unchanged'),
     ('priority', 'only check Priority', 'writesFront1'),
     ('zero', 'checked numeric zero', 'zero is written'),
     ('none_cancel', 'none selected / Cancel', 'no animation write; no accidental empty cel creation'),
     ('focus', 'legacy default0 / missing4, explicit selection', 'canvas default compatibility and existing selection mapping retained'),
     ('gradient_clamp', 'legal compatibility X550; confirm checked / cancel', 'working500; confirm writes500; cancel retains550'),
     ('gradient_normal', 'X20; Y analogous signed boundary; RGBA/opacity', '20 retained; field-specific clamps retained'),
     ('gradient_selection', 'none selected vs at least one', 'false/no write vs selected value and nil for unselected'),
     ('aliases', 'shared attributes / empty cel', 'pre-existing alias and consumer gates preserved')],
    [('post_replace_failure', 'typed length1/frame0nil/graphic empty/timing empty; healthy I/O/menus', 'conversion skips nil; collection replaced; next drawing consumes nil and fails outside import rescue'),
     ('committed_prefix', 'same fixture, before exit', 'old slot not restored; cache member replaced; save and cleanup/BGM restoration not reached'),
     ('normal_import', 'valid frame and local resources', 'normal import/load path retained'),
     ('wrong_type_encoding', 'bad encoding / wrong type', 'refusal before replacement, old slot retained'),
     ('conversion_failure', 'error during conversion before assignment', 'old collection member retained; decoded temporary may already mutate'),
     ('scope', 'original independent P3 correction', 'coverage gap only; no claim old prose guaranteed global rollback')],
    [('retained_P', 'same window P→reopen Curve→no line→BACK→OK', 'visible points cleared; old nonempty P retained and writes X/Y, expands if necessary'),
     ('first_curve_back', 'no prior P; early Curve BACK', 'path nil; OK does not write'),
     ('line_back', 'curve line was displayed then BACK', 'new curve path replaces P'),
     ('outer_cancel', 'outer Cancel/BACK', 'no animation write'),
     ('freehand_early_esc', 'first waiting stage ESC', 'empty path replaces P; OK expands then fails at first point; expansion remains'),
     ('freehand_record_esc', 'ESC during recording', 'recorded stroke retained'),
     ('sampling', 'initial curve/freehand/changed frame count', 'N vs N+2, rounding, firstN and coordinate rules preserved')],
    [('auto_points', 'endpoints0,0 and300,0', 'decimal factors0.3333/0.6666; requested99.99/199.98 approximately, not exact100/200'),
     ('explicit_N5', 'explicit dragged controls0,1,8,11; N5', 'Catmull-Rom requested0,.3046875,4.375,9.1015625,11'),
     ('outer_cancel', 'construct controls then outer cancel', 'control point request does not commit animation'),
     ('host_quantization', 'no native Sprite execution', 'integer and actual pixel effects remain unknown'),
     ('optional_boundary', 'generalN float accumulation/curve endpoints', 'independent optional; not a required bitwise compatibility rule')]
]
groups = ['identity_and_verdict', 'bidirectional_evidence', 'premises_and_counterexample',
          'minimum_revision_contract', 'acceptance_and_regression',
          'independent_adjudication', 'dependencies_and_receivers']
rows = []
for i, original in enumerate(contract['scope_contracts']):
    ident = original['id']
    start = report.index('### ' + ident)
    end = report.find('\n### ', start + 1)
    if end == -1:
        end = report.index('\n## 必要接口', start)
    rows.append({'id': ident, 'verdict': 'CANDIDATE_PASS',
                 'binding': bindings,
                 'frozen_contract_pointer': '/scope_contracts/' + str(i),
                 'frozen_seven_groups': {k: original[k] for k in groups},
                 'original_full_proposal': {'read': 'complete prompt, not author summary',
                                            'pointer': '/scope_contracts/' + str(i) + '/original_full_proposal'},
                 'reviewer_assessment': report[start:end].strip(),
                 'all_static_vectors': [{'name': n, 'premises': p, 'independently_derived_result': r,
                                         'verdict': 'PASS_STATIC', 'behavior_execution': 0}
                                        for n, p, r in vectors[i]],
                 'blocking_failures': [], 'minimal_substantive_revision': None,
                 'closure': 'candidate only; integration/formal acceptance/CLOSED not granted'})
write('per-id-review.json', {'reviewer': 'R6-U07-R', 'verdict': 'CANDIDATE_PASS',
      'contract': identity(PREP, PREFIX + 'contracts/R6-U07.json'),
      'candidate': bindings, 'rows': rows, 'count': 7,
      'method': 'Manual source/prose/counterexample judgments packaged after direct full reading. No automatic semantic PASS.'})

# Finite exact arithmetic validates the explicit fixture, not Ruby/Sprite execution.
def catmull(a, b, c, d, u):
    return ((2*b) + (-a+c)*u + (2*a-5*b+4*c-d)*u*u + (-a+3*b-3*c+d)*u*u*u) / 2

points = [F(0), F(1), F(8), F(11)]
result = []
for t in [F(0), F(1,4), F(1,2), F(3,4), F(1)]:
    pos = t*3
    idx = min(int(pos), 2)
    u = pos-idx
    vals = [points[max(0,idx-1)], points[idx], points[idx+1], points[min(3,idx+2)]]
    result.append(catmull(*vals, u))
assert result == [F(0), F(39,128), F(35,8), F(1165,128), F(11)]
assert F('0.3333')*300 == F('99.99') and F('0.6666')*300 == F('199.98')
write('finite-arithmetic.json', {'kind': 'TOOL_VALIDATION_OF_STATIC_REQUESTS',
      'reference_execution': 0, 'host_execution': 0,
      'auto_decimal_requests': ['99.99', '199.98'],
      'explicit_N5_exact_results': [str(x) for x in result],
      'explicit_N5_decimal_results': [float(x) for x in result],
      'optional_generalN_bitwise_endpoint': 'excluded; no inference from exact N5 fixture'})

# Independently reconstruct the author's diff in temporary files only.
temp = pathlib.Path('/tmp/r6-u07-patch-reconstruction')
temp.mkdir(exist_ok=True)
paths = contract['candidate_formal_paths']
for path in paths:
    dest = temp / (PREFIX + 'candidates/R6-U07/mirror/' + path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(git('show', BASE + ':' + path))
patch_path = PREFIX + 'candidates/R6-U07/evidence/candidate.patch'
patch = git('show', PUB + ':' + patch_path)
commands = []
for flags in [['--check'], []]:
    argv = ['git', 'apply', '--unidiff-zero', *flags, '-']
    r = subprocess.run(argv, input=patch, cwd=temp, capture_output=True)
    commands.append({'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                     'cwd': str(temp), 'argv': argv, 'exit': r.returncode,
                     'stdout': r.stdout.decode(), 'stderr': r.stderr.decode()})
    assert r.returncode == 0, r.stderr
reconstructed = []
for path in paths:
    dest_path = PREFIX + 'candidates/R6-U07/mirror/' + path
    actual = (temp / dest_path).read_bytes()
    expected = git('show', PUB + ':' + dest_path)
    assert actual == expected
    reconstructed.append({'path': dest_path, 'bytes': len(actual),
                          'sha256': hashlib.sha256(actual).hexdigest(), 'match': True})
write('patch-reconstruction.json', {'kind': 'TOOL_VALIDATION_NOT_SEMANTIC_REVIEW',
      'patch': identity(PUB, patch_path), 'commands': commands, 'all_three_mirrors': reconstructed})

journal = [json.loads(line) for line in (OUT / 'read-journal.jsonl').read_text().splitlines()]
coverage = []
for path in contract['read_only_reference_paths']:
    rs = [r for r in journal if r['role'] == 'reference' and r['path'] == path]
    assert rs
    read = set()
    for r in rs:
        read.update(range(r['read_span'][0], r['read_span'][1]+1))
    total = rs[0]['total_lines']
    assert read == set(range(1,total+1)), path
    coverage.append({'path': path, 'total_lines': total, 'complete_numbered_read': True,
                     'identity': {k: rs[0][k] for k in ['commit','bytes','sha256','git_blob']},
                     'actual_recorded_spans': [r['read_span'] for r in rs]})
write('execution-and-read-coverage.json', {
    'written_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'logical_reviewer': 'R6-U07-R',
    'requested': {'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'default','fast':False},
    'actual': {'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','task_uuid':'UNVERIFIED'},
    'author_task':'01a13ab2-df02-712f-a724-7b7695163036',
    'delegating_thread':'01a10d94-84b9-759e-aa1d-edb0d9b6d0e2',
    'independent_direct_review': True, 'subagents': 0, 'model_config_cli_probes': 0,
    'reference_source_execution':0,'behavior_harness_execution':0,'native_host_execution':0,'demo_execution':0,
    'prompt': identity(PREP,PREFIX+'prompts/R6-U07-R.md'),
    'prompt_read': {'unicode_characters':333606,'lines':6736,
                    'consecutive_complete_character_spans':[[a,min(a+24000,333606)] for a in range(0,333606,24000)],
                    'record_type':'retrospective attestation of actual tool-displayed reads; no invented timestamps'},
    'contract':identity(PREP,PREFIX+'contracts/R6-U07.json'),
    'contract_read':'complete exact-equal embedded contract in fully read prompt; standalone identity verified',
    'source_full_reads':coverage,
    'formal_full_read_displays':[
        {'file':'/tmp/r6-u07-paired-0.txt','spans':[[1,135],[136,265],[266,390],[391,512]]},
        {'file':'/tmp/r6-u07-paired-1.txt','spans':[[1,80],[81,150],[151,220],[221,285],[286,337]]},
        {'file':'/tmp/r6-u07-paired-2.txt','spans':[[1,120],[121,230],[231,348]]}],
    'original_counterevidence_full_read':['counter-animation.json:71 lines','animation/counter-editor.json:461 lines; unrelated E findings do not expand scope'],
    'author_material_boundary':'read after independent source/full-prose review; matching frozen fields de-duplicated only by exact object equality; all novel per-ID fields read',
    'attempts_and_recovery':[
        {'attempt':'oversized prompt/contract or author-row output','result':'tool output truncated',
         'recovery':'prompt consecutive bounded chunks fully read; duplicate contract/frozen row fields checked for exact equality; all remaining fields read bounded'},
        {'attempt':'author history-scoped-inputs full numbered output','result':'middle truncated',
         'recovery':'375–575 read separately, filling the entire omitted range'},
        {'attempt':'canonical history commit read before fetch','result':'path/commit unavailable; not a tree object',
         'recovery':'fetch exact c0ff330 commit, then full raw bytes and exact selected field/pointer verification'},
        {'attempt':'require selected history excerpt equals entire canonical record','result':'AssertionError: excerpt intentionally omits old current-quality fields',
         'recovery':'all supplied excerpt keys matched original values; canonical qualified scope read separately; no old quality transfer'},
        {'attempt':'wide legacy-control and file-navigation output','result':'output truncated',
         'recovery':'not claimed as a full semantic read; bounded qualified B20 scopes and relevant GR4-M10-004 record used'},
        {'attempt':'original-worktree status long-running','result':'completed clean at baseline work branch',
         'recovery':'all edits performed only in isolated fixed-publication worktree'}],
    'remaining_blockers':[],
    'pending_stages':['unique writer integration','shared full-file independent review','actual interface/history acceptance','formal acceptance','CLOSED registration']})

write('regression-review.json', {
    'candidate':bindings,'evidence_level':'manual static, not execution or historical PASS transfer',
    'R1':{'origin': 'baseline:review/wp74-review-2026-10-02/recheck-v4/report.md',
          'qualification':'18 CLOSED in original WP74 scope only',
          'fresh_affected_results':[
              'last individual/current-frame guard and slot60: PASS_STATIC',
              'Delete at current last index leaves detached/selected append behavior: PASS_STATIC',
              'snapshot copy/paste vs Insert shallow property alias: PASS_STATIC',
              'three bitmap entry predicates remain separate: PASS_STATIC',
              'path old-P/nil/empty, N/N+2/rounding and pre-failure expansion: PASS_STATIC',
              'immediate slider clamp and preview fixed anchors: PASS_STATIC'],
          'unaffected':'sorting/name compilation/organizer/file matrices/count statements unchanged in full reading; no full historical re-signature'},
    'R2':{'counts':{'controls':229,'batches':21,'contributions':341,'not_interchangeable':True},
          'canonical_origin':'c0ff33024aea424c68d29f9778fe7c8e807d21e8:review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/regression-legacy-scope.json',
          'selected_original_field_verification':'history-origin-verification.json',
          'fresh_scope_results':[
              {'id':'B20/GIR-FD82-003','scope':'§4.3/6.1 implementation-neutral copy isolation and Insert property coupling','result':'PASS_STATIC'},
              {'id':'B20/GIR-FD82-C020','scope':'§3.4/11.2 normal resource/loading/cleanup vs post-replacement failure prefix','result':'PASS_STATIC'},
              {'id':'B20/GIR-FD82-C025','scope':'§6.3/14.1 all-frame copy/TAB/storage slot60 vs0–59 tool gates','result':'PASS_STATIC'},
              {'id':'B20/GIR-FD82-C026','scope':'§10.2a shared layers, captured RGBA, zero-duration, skipped timing, A+B175 vs150','result':'PASS_STATIC'},
              {'id':'B20/GIR-FD82-C031','scope':'§12/16 Yes/No/Cancel/zero-item organizer adjacent exit semantics','result':'NOT_AFFECTED; full prose retained'},
              {'id':'B20/GIR-FD82-C032','scope':'§8.6 window coordinates, curve clamping/freehand difference/+64 redraw','result':'PASS_STATIC'},
              {'id':'B20/GIR-FD82-C033','scope':'§4.6 ALT pixel inspection inverse zoom/mirror/origin; angle ignored','result':'NOT_AFFECTED; full prose and source retained'},
              {'id':'B20/GIR-FD82-D024','scope':'§8.6 N/N+2, half-away rounding, explicit dragged N5, empty-path expansion failure','result':'PASS_STATIC'}],
          'excluded':'unselected controls/contributions not new semantic acceptance; no theme-based finding matching'},
    'R3':{'required':23,'criteria':76,'scope':'fixed required23 navigation plus current full WP67-A; no direct animation finding guessed',
          'neighbor':'GR3-M10-002 quantity and GR3-M10-003 battle command/message contract spans unchanged',
          'result':'NOT_AFFECTED outside candidate changes; historical verdicts not transferred'},
    'R4':{'required':17,'criteria':76,'B5_qualified_required':16,'B5_qualified_criteria':75,
          'affected_finding':'GR4-M10-004', 'original_pointer':'/records/14',
          'source_units':['PA412–518','Battle838–843','Move1–96','Target26–33/136–141','MiscPBSData39–53','PBS FLAMETHROWER/EMBER/SUNNYDAY/TACKLE'],
          'all_three_criteria':[
              {'number':1,'scope':'complete18×6 identities and six-slot interpretation preserved','result':'PASS_STATIC'},
              {'number':2,'scope':'conditional10→20→30→nil and opponent11-before10; explicit healthy containers','result':'PASS_STATIC'},
              {'number':3,'scope':'exact hitNum vs defaults; identity/mapping/database/media/showAnims distinct','result':'PASS_STATIC'}],
          'shared_catalog_other_domains':'NOT_AFFECTED; exact row sequence and untouched row contents preserved',
          'runtime':0},
    'R5':{'closed':92,'P2':51,'P3':41,
          'qualified_candidate':'13fddb0a217b36974c75657aa68da0caf104ee48',
          'qualified_candidate_tree':'92a241ab8ca04f4f60211e60a2fa7cf284eb0c86',
          'qualified_review':'044c3483229e7e76bedf1fc244fc84d274bf059c',
          'qualified_review_tree':'5c85cf971b9d71f4170ed54a504150e516053beb',
          'rule':'unique final92 qualification retained; older OPEN/WAIT/errors not rewritten, no new92 signature',
          'GR5-M12-202':'animmaker documentation-only optional unchanged; no capability count inflation'},
    'all_direct_transitive_interfaces':'per-ID documented storage→editor→player→collection/cache→save/export/import; all required static affected consumers checked',
    'AN007_optional_boundary':'mandatory approximate auto controls PASS; independent general float endpoint optional not upgraded',
    'runtime_and_policy':'source/host/Demo0; six policies and limits retained; no permanent source-defect product decision',
    'failures':[]})

assert len(rows) == 7 and [r['id'] for r in rows] == contract['required_ids']
assert all(len(r['frozen_seven_groups']) == 7 for r in rows)
for p in OUT.glob('*.json'):
    json.loads(p.read_text())
print(json.dumps({'packaged_manual_verdict':'CANDIDATE_PASS','ids':len(rows),
                  'static_vectors':sum(len(v) for v in vectors),
                  'source_full_read_lines':sum(c['total_lines'] for c in coverage),
                  'patch_reconstruction':'3/3 exact','finite_arithmetic':'PASS',
                  'reference_behavior_execution':0},ensure_ascii=False))
