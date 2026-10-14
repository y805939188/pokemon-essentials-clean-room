"""Package the root review already written in report.md, without modifying inputs."""
import datetime
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
PREP_ROOT = ROOT.parents[1]
verification = json.loads((ROOT / 'static-verification.json').read_text())
contract = json.loads((PREP_ROOT / 'contracts/R6-U01.json').read_text())
report = (ROOT / 'report.md').read_text()
timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
requested = {'model': 'gpt-6.1-sol', 'effort': 'ultra', 'tier': 'default', 'speed': 'default', 'Fast': False}
provenance = {'logical_id': 'R6-U01-R', 'canonical_task': '/root', 'author': False,
              'user_author_task_reference': '01a13ab1-de65-75f0-ac96-124bc93cd02b',
              'user_source_thread_reference': '01a10d94-84b9-759e-aa1d-edb0d9b6d0e2',
              'requested': requested,
              'effective_echo': {k: 'UNVERIFIED' for k in ['model', 'effort', 'tier', 'speed', 'platform_UUID']},
              'no_cli_or_configuration_proof_agent': True,
              'semantic_owner': '/root directly reviews all three IDs',
              'mechanical_support': '/root/payload_audit; bytes/tree/manifest only; no per-ID adjudication',
              'runtime_execution': {'reference': 0, 'surrogate_reference': 0, 'independent_gameplay_model': 0,
                                    'native_game': 0, 'native_UI': 0, 'Demo': 0, 'real_save': 0, 'production_service': 0},
              'initial_metadata_limits': 'Early reads lack separate local UTC/stdout/stderr; exact platform transcript retained. Initial log number 5 collision lost the first patch stdout. v2 unique IDs, independent actual diff and new source reads repair semantic coverage, not old provenance.',
              'preserved_failures': 'Three source Git exit128 before fetch completion; absent local historical c0ff commit exit128; support early compile SyntaxError; all retained, later reads separate.',
              'write_allowlist': str(ROOT.relative_to(pathlib.Path('/workspace/pokemon-essentials-clean-room'))) + '/',
              'created_utc': timestamp}
(ROOT / 'reviewer-provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + '\n')

group_keys = ['identity_and_verdict', 'bidirectional_evidence', 'premises_and_counterexample',
              'minimum_revision_contract', 'acceptance_and_regression', 'independent_adjudication',
              'dependencies_and_receivers']
records = []
for scope in contract['scope_contracts']:
    key = scope['id']
    section = report.split('## ' + key + '：', 1)[1].split('\n## ', 1)[0]
    paragraphs = re.split(r'\*\*[1-7]\. ', section)[1:]
    assert len(paragraphs) == 7
    records.append({'id': key, 'classification': 'required', 'severity': scope['identity_and_verdict']['severity'],
                    'verdict': 'PASS', 'state': 'CANDIDATE_PASS_STATIC', 'required_repairs': [],
                    'groups': dict(zip(group_keys, [x.strip() for x in paragraphs])),
                    'candidate_payloads': [x for x in verification['mirrors'] if x['formal_path'] in scope['minimum_revision_contract']['candidate_formal_write_set']],
                    'original_contract': {'prepare_commit': '469a268b92daed7b4d28d7fd0da75520cbb7228f',
                                          'path': str(PREP_ROOT.relative_to(pathlib.Path('/workspace/pokemon-essentials-clean-room')) / 'contracts/R6-U01.json'),
                                          'full_payload_identity': verification['contract_identity'],
                                          'scope_pointer': '/scope_contracts/' + str(len(records)),
                                          'full_original_proposal_read': True},
                    'evidence': ['SOURCE_STATIC', 'DERIVED_VECTOR'], 'behavior_execution': 0})
bindings = {'prepare': '469a268b92daed7b4d28d7fd0da75520cbb7228f',
            'frozen_candidate_commit': '0f2bf0318405ab281682023c6cf0a68eabdd73ad',
            'frozen_candidate_tree': '7091593ae08af02d265250fa94cb7f552e51fba7',
            'frozen_candidate_directory_tree': 'ac42282d00a116314741915d6c489ec67aee0bee',
            'author_core': 'd13dc8446d0e47c659f81c86413aeafb2279da01',
            'main': '8ea169fbd0f33f378b5d732fd6bea59e854e04a6',
            'reference': '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'}
(ROOT / 'findings.json').write_text(json.dumps({'schema': 'r6-u01-independent-review.v1', 'bindings': bindings,
        'reviewer': provenance, 'records': records, 'required_repairs': [],
        'formal_acceptance': 'NOT_GRANTED', 'CLOSED': 'NOT_REGISTERED',
        'integration_gates': contract['closure_gate'], 'created_utc': timestamp}, ensure_ascii=False, indent=2) + '\n')

readset = []
for row in verification['mirrors']:
    readset.append({'kind': 'formal_full_semantic_then_candidate_effective_overlay', 'commit': bindings['main'],
                   'path': row['formal_path'], 'ranges': [[1, row['baseline_lines']]], 'identity': row['baseline'],
                   'candidate_commit': bindings['frozen_candidate_commit'], 'candidate_path': row['candidate_path'],
                   'candidate_identity': row['candidate'], 'coverage': 'All original lines and every actual changed line read by root; byte-exact overlay validated',
                   'candidate_file_changed': row['changed']})
for row in verification['source_payloads']:
    ranges = [[1, row['lines']]]
    coverage = 'full Ruby unit semantically read by root'
    if row['path'] == 'PBS/pokemon.txt':
        ranges = [[11113, 11140]]
        coverage = 'Complete Shellos record only, plus focused fields search and full-byte identity validation; not whole-PBS semantic reading'
    if row['path'] == 'PBS/pokemon_forms.txt':
        ranges = [[1119, 1130]]
        coverage = 'Complete Shellos form record plus adjacent Gastrodon record and focused fields search; not whole-PBS semantic reading'
    readset.append({'kind': 'source', **row, 'semantic_ranges': ranges, 'coverage': coverage})
ledger = {'read_owner': '/root direct semantic reviewer', 'new_readset': readset,
          'full_contracts': 'Fixed complete reviewer prompt prose and complete contract object, including original_full_proposal for all three IDs; complete recovery metadata parsed and all115 cached body identities validated',
          'original_counters_full': ['findings/independent-K-%03d.json' % i for i in range(1, 4)] + ['tasks/R6-O/counter-K-%03d.json' % i for i in range(1, 4)],
          'author_evidence_read': 'Complete author-report, all three author-findings seven groups, validation.py, exact actual deltas, shared-context, policy/limits projection; identity structures verified independently',
          'history': 'history-verification.json: all exact qualification fields for6contributions/GR4 plus four original closure records and exclusion boundary, matched original immutable remote bodies; no full archive join semantic credit',
          'additional_consumers': ['WP33:120 through EOF (includes5.3)', 'WP35:59–176 (hatching/cache/dynamic-form intersections)'],
          'repaired_truncation': ['WP18 root output repaired1–135 and130–162', 'WP27 tail208–221', 'actual diff all changed lines re-read independently'],
          'commands': 'commands.jsonl + logs; initial provenance gaps recorded in reviewer-provenance.json',
          'evidence_levels_not_collapsed': True, 'reference_or_model_or_host_execution': 0}
(ROOT / 'reading-ledger.json').write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'records': [(x['id'], x['verdict']) for x in records], 'seven_groups_each': True,
                  'formal_full_documents': 9, 'formal_original_lines': sum(x['baseline_lines'] for x in verification['mirrors']),
                  'reference_full_Ruby_units': 11, 'reference_partial_PBS': 2, 'required_repairs': 0}, ensure_ascii=False))
