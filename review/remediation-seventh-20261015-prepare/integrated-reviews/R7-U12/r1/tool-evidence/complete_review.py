"""Seal the completed, human-reviewed U12 findings and audit input structure.

This program validates identities and packages stated review observations. It
does not execute behavior or derive a semantic verdict from a successful exit.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parent.parent
E = ROOT / 'tool-evidence'
INPUT = Path('/workspace/r7-ir-R7-U12/actual-input')
MI = '45c80832a41c1b56dcd7e9d93497758cbb7721de'
OLD = '38ea9afb84395d7c20d3beed322281dd50a688e4'
PREFIX = ROOT.relative_to(Path('/workspace/r7-ir-R7-U12/checkout')).as_posix()

def git(*args):
    return subprocess.check_output(['git', *args])

def ident(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())

def save(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')

# Preserve the partial report and every superseded assessment at its real commit.
history = E / 'history' / OLD
history.mkdir(parents=True, exist_ok=True)
for name in ['report.md', 'per-id.json', 'review-input-receipt.json',
             'tool-evidence/content-review-coverage.json',
             'tool-evidence/shared-contribution-receipt.json']:
    target = history / name
    data = git('show', OLD+':'+PREFIX+'/'+name)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        assert target.read_bytes() == data
    else:
        target.write_bytes(data)

actual = INPUT / 'actual'
files = []
for p in sorted(actual.rglob('*')):
    if not p.is_file():
        continue
    rel = p.relative_to(actual).as_posix()
    data = p.read_bytes()
    assert data == git('show', MI+':'+rel)
    files.append(dict(path=rel, commit=MI, **ident(data),
                      physical_lines=len(data.decode().splitlines()),
                      reading='FULL_CONTENT_REVIEWED_WITH_EXACT_LINE_DEDUPLICATION'
                      if not rel.endswith('sync-input.json') else
                      'FULL_STRUCTURED_PARSE; ALL_DISTINCT_NONHASH_STRING_VALUES_READ; '
                      'REPEATED_BINDINGS_AND_NUMERIC_IDENTITY_FIELDS_STRUCTURALLY_CHECKED'))
assert len(files) == 14

sync_path = 'review/remediation-sixth-20261014-prepare/integration/public-sync-20261014/sync-input.json'
sync = json.loads((actual/sync_path).read_text())
unique_strings = {}
leaf_count = 0
def walk(value, pointer=''):
    global leaf_count
    if isinstance(value, dict):
        for key, child in value.items(): walk(child, pointer+'/'+key)
    elif isinstance(value, list):
        for i, child in enumerate(value): walk(child, pointer+'/'+str(i))
    else:
        leaf_count += 1
        if isinstance(value, str): unique_strings.setdefault(value, pointer)
walk(sync)
assert len(unique_strings) == 1134
semantic_strings = {s:p for s,p in unique_strings.items()
                    if not re.fullmatch('[a-f0-9]{40}|[a-f0-9]{64}', s)}
assert len(semantic_strings) == 806
assert len(sync['items']) == 56
assert len({x['id'] for x in sync['items']}) == 56
assert set(sync['documents'][0]['scope_ids']) == {x['id'] for x in sync['items']}
for row in sync['items']:
    assert row['behavior_execution'] == 'NOT_EXECUTED'
    assert row['actual_content_review']['effective_configuration'] == 'UNVERIFIED'
    assert row['formal_acceptance']['id'] == row['id']
    assert row['closure']['id'] == row['id']
    assert row['closed'] is True
    assert row['actual_content_review']['actual_commit'] == sync['actual_formal_commit']
    assert row['formal_acceptance']['actual_formal_tree'] == sync['actual_formal_tree']
    assert row['closure']['actual_formal_tree'] == sync['actual_formal_tree']
assert sync['items'][42]['actual_clause_label'] == 'WP72 §5.2／WP27'
assert sync['qualification']['effective_configuration'] == 'UNVERIFIED'
assert sync['qualification']['new_reference_model_host_Demo_save_record_execution'] == 0

observations = {
    'R7-U13': 'MIDI sound-bank declaration remains Pending, with L04/L09 selection, '
              'acceptance, synthesis and sound unknown. U12 navigation changes none '
              'of its request, nil/empty, failure-prefix or historical-media qualifications.',
    'R7-U11': 'Loader classification and four-target text-tool requests remain finite '
              'static facts. Existing history, API/geometry/timing unknowns and DX '
              'catalog append remain independent of U12 navigation.',
    'R7-U01': 'Integer lookup/equality and composite-header clauses retain the r2 '
              '4000-field/default-vs-absent distinction, r1 FAIL history and source '
              'debt. Its EOF block precedes U02 and its engine index coexists with U13.',
    'R7-U02': 'F8 finite fallback, per-entry trailing input refresh, and 15+6 native '
              'target vocabulary retain local-prefix and NOT_READ bridge limits. '
              'No claim about all physical keys or all cancellation paths is introduced.'
}
shared = json.loads((E/'shared-contribution-receipt.json').read_text())
for row in shared['checks']:
    batch = row['other_batch']
    row['semantic_compatibility'] = 'COMPATIBLE_WITH_U12_SCOPED_NAVIGATION_AFTER_FULL_SHARED_CONTENT_REVIEW'
    row['independent_reason'] = observations[batch]
    row['approval_content_read'] = dict(
        complete_report=f'shared-candidate-review/{batch}/report.md',
        exact_record_scope_and_shared_receivers=f'shared-candidate-review/{batch}/per-id.json',
        exact_root_eligibility=f'shared-root-reception/{batch}/eligibility.json')
    row['receiver_status'] = 'U12_COMPATIBILITY_CHECK_COMPLETE; ROOT_RECEPTION_OF_THIS_NEW_REVIEW_PENDING'
shared['scope_qualification'] = ('Eight checks cover the two complete U12 shared targets. '
    'Engine/UI/DX catalog contributions were additionally aligned at exact journal hunks; '
    'unrelated unchanged catalog bodies and peer source programs receive no new semantic PASS.')
save(E/'shared-contribution-receipt.json', shared)

ledger = dict(schema='r7.u12.completed-content-ledger.v1',
    utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    reviewer_thread='01a1402e-9f4a-72f7-863e-018ee4a4e036',
    prior_partial_commit=OLD, prior_partial_state='WAIT_PRESERVED_IN_HISTORY',
    required_actual_files=files,
    exact_line_deduplication='Blank lines carry no prose; exact repeated complete lines '
        'refer to their first occurrence in complete-content-line-map.json. Page generation '
        'alone was never counted as reading. Truncated displays were supplemented.',
    sync_structured_read=dict(path=sync_path, leaves=leaf_count,
        unique_strings=1134, distinct_nonhash_strings_read=806,
        full_item42_read=True, all_56_rows_structurally_checked=True,
        qualification='All distinct text values were viewed with first JSON pointers. '
        'Hashes, byte sizes and repeated receipt/status structures were parsed and bound '
        'mechanically; no new semantic reapproval of the 56 historical source domains.'),
    full_shared_target_review=dict(paths=['audit/source-traceability.md','planning/feature-matrix.md'],
        peer_observations=observations, eight_preservation_checks_complete=True,
        all56_hunks_rebuilt='all-56-clauses-audit.json',
        engine_catalog='U13 separate S01 plus U01 J01 index at separate baseline boundaries; '
            'U03 pending contribution not assumed present.',
        UI_catalog='U08 HP01–04/L13 changes and U02 appended SS/IN/DB/BT/AX remain '
            'separate exact hunks; U12 changes no UI behavior.',
        DX_catalog='U11 EXT01–12 appended after complete B prefix; DG-U08-01–04 and '
            'fill-bag controls retained; U10 future material not assumed present.',
        same_EOF='U01 then U02 in audit and matrix; root note qualifies candidate-time labels.'),
    prior_five_files=dict(full_current_content_read=True, exact_preservation=True,
        basis='prior-and-history-preservation.json',
        report_and_root_decision_read=True,
        compatibility='WP39 query/fallback and owner-rank premises, WP41 later-slot '
          'scan/exception prefixes, WP34 parental dynamic vs child explicit commit and '
          'their catalogs retain their distinct gates. U12 only changes navigation and '
          'does not generalize cancel/no-write or rollback. No new PASS for their IDs.'),
    domain_consumers=dict(
        WP27='Full current body read; pure precheck, partial direct add, successful sorting '
            'and independent PC/gift and receive/pickup/prize paths remain distinct.',
        WP17='Current §§3.3.1,4,5,6.1,7.1–7.3 read. Explicit quantity cancel0 is '
            'unclamped, independent of default cancellation; local busy/normal/exception '
            'refresh differences do not change add-item return-value handling.',
        DG='Current DG-M11/M30 and DG-U08-01–04 read, plus adjacent DG-U08 controls '
            'for scope; not signed as executed.',
        R='Debug778–797 and adjacent fill-bag; Bag81–93,162–164,263–281. '
            'Full snapshot identities verified; no whole-source semantic claim.',
        historical_B21='All four exact historical objects restored and identity checked; '
            'historical README and static-cases read; traceability/eight-chain navigation '
            'and approval qualification checked without reapproving their entire domains.',
        root='Root README/CURRENT-DELIVERY/sixth delivery/B21 actual-freeze controls read; '
            'M20 historical and M21 current-supplement qualifications remain independent.'),
    reviewer_obligations_remaining=[], input_or_independence_blockers=[],
    root_only_next_gates=['Receive this exact completed result commit/tree',
        'Register semantic/shared/domain/direct-transitive/historical responsibilities '
        'using this review and any separately required peer results',
        'Make separate authorized formal acceptance and closure decisions'],
    no_global_or_peer_PASS=True, all_behavior_execution='NOT_EXECUTED',
    effective_configuration='UNVERIFIED', L01_L14='RETAINED')
save(E/'completion-reading-ledger.json', ledger)

coverage = dict(required_actual_files=14, actual_bytes=sum(x['bytes'] for x in files),
    complete_actual_full_text_semantic_review=True,
    structured_JSON_method=ledger['sync_structured_read'],
    generation_map_is_not_read_receipt=ledger['exact_line_deduplication'],
    transport_or_source_availability_blocker=False, missing=[],
    historical_partial_evidence='history/'+OLD,
    completion_ledger='completion-reading-ledger.json',
    not_a_certificate_for_unrelated_domains=True)
save(E/'content-review-coverage.json', coverage)

per_id = json.loads((ROOT/'per-id.json').read_text())
for row in per_id['records']:
    row['verdict'] = 'PASS_SCOPED_ACTUAL_INTEGRATION'
    row['content_verdict'] = 'COMPLETE_FINITE_STATIC_ACTUAL_CONTENT_REVIEW'
    row['unmet_review_gates'] = []
    row['completed_review_evidence'] = 'tool-evidence/completion-reading-ledger.json'
    row['historical_partial_WAIT'] = dict(commit=OLD, preserved=True,
        reason='Readable remaining review work at that time; completed in this continuation.')
    row['dependencies']['finite_content_and_consumer_compatibility'] = 'SATISFIED_BY_THIS_COMPLETED_STATIC_REVIEW'
    row['dependencies']['reception'] = 'REVIEW_COMPLETE; ROOT_EXACT_RESULT_RECEPTION_AND_RESPONSIBILITY_REGISTRATION_PENDING'
    row['dependencies']['unmet_root_gates'] = ledger['root_only_next_gates']
    row['shared_receiver'] = ('R7-I owns actual reception/registration. U12 independent '
        'compatibility checks for CG01/CG07 complete; no new PASS for other mandatory IDs.')
    for vector in row['vectors']:
        vector['result'] = 'SATISFIED_SCOPED_STATIC_CONTENT'
        vector['whole_integration_content_gate'] = 'COMPLETE_FOR_U12_SCOPE'
        vector['behavior_execution'] = 'NOT_EXECUTED'
per_id['completion_state'] = 'COMPLETE_TWO_SCOPED_ACTUAL_VERDICTS_NO_ACCEPTANCE_OR_CLOSURE'
save(ROOT/'per-id.json', per_id)

receipt = json.loads((ROOT/'review-input-receipt.json').read_text())
receipt['full_semantic_review_complete'] = True
receipt['content_coverage'] = coverage
receipt['completed_review_ledger'] = 'tool-evidence/completion-reading-ledger.json'
receipt['historical_partial_WAIT_commit'] = OLD
extra_path = 'deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md'
extra = Path('/workspace/r7-ir-R7-U12/supplementary-read-inputs')/extra_path
assert extra.read_bytes() == git('show', MI+':'+extra_path)
supp = json.loads((E/'supplementary-input-identities.json').read_text())
if not any(x['path']==extra_path for x in supp['files']):
    supp['files'].append(dict(path=extra_path, commit=MI, local_path=str(extra), **ident(extra.read_bytes())))
save(E/'supplementary-input-identities.json', supp)
receipt['completion_supplement'] = supp['files'][-1]
save(ROOT/'review-input-receipt.json', receipt)
print(json.dumps(dict(required_files=14, required_bytes=coverage['actual_bytes'],
    historical_sync_rows=56, nonhash_text_values_read=806, shared_checks=8,
    semantic_conclusions='Separately authored finite content review; not derived from exit0',
    reference_execution=0, configuration='UNVERIFIED')))
