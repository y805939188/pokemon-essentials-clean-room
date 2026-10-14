#!/usr/bin/env python3
"""Independently validate exact upstream receipts and finite dependency inputs."""
import json
import pathlib
import runpy

helpers = runpy.run_path(str(pathlib.Path(__file__).with_name('verify-inputs.py')))
load, verify, git, save = (helpers[k] for k in ('load', 'verify', 'git', 'save'))
P, C, S, F = (helpers[k] for k in ('INPUT', 'CANDIDATE', 'SUBJECT', 'FROZEN'))
matrix = load(C, P + '/mandatory92-review-matrix.json')['findings']
edges = load(C, P + '/dependency18-handshakes.json')['edges']
graph = load(F, helpers['PREP'] + '/contracts/dependency-graph.json')['edges']
assert {(x['source'], x['target']) for x in edges} == {tuple(x) for x in graph}
analyses = {
 ('R5-U01', 'R5-U02'): 'Default source collection/runtime translation selection and canonical keys remain distinct. Current WP08 supplies selected mutable material to WP11 map-name consumer; empty hit/core/basic-name ordering, relookup keys and reset layers agree. WP06 count/time input qualifications survive U02 movement/push contributions.',
 ('R5-U01', 'R5-U03'): 'U03 consumes accepted item/NPC/content defaults and quantity identities, not candidate prose. Current primary creature, training, wallet, bag and PC rules distinguish resource constructor from clamped writer, stored/dynamic form and consumer refresh. Item ShowQuantity defaults retain their narrow important/nonimportant qualification.',
 ('R5-U03', 'R5-U04'): 'Creature/stat/ability/item identities remain prerequisite inputs for current combat participants and effects. U04 uses current qualified primary facts without transferring whole creature-file acceptance; ordinary action status/PP, move fallback and stat effects keep battle-local and persistent state separate.',
 ('R5-U04', 'R5-U05'): 'Actual healing/effect eligibility is provider fact, while LIFEDEW scoring independently checks recoverability when failure prediction is off. WP52-B119 retains h>=H/fainted/HealBlock guard before HP-awareness score; local score does not write HP or guarantee final AI selection.',
 ('R5-U02', 'R5-U06'): 'World/map/movement inputs and metadata remain available to UI consumers; UI resource/candidate and time/animation contracts do not replace logical movement or persistence rules. Shared world and UI catalogs retain separate entry qualifications.',
 ('R5-U03', 'R5-U06'): 'UI consumes current dynamic form and item/mail/quantity facts. WP66-A225 expressly admits dynamic-read form/cache/stat/conditional registration before resource matching; Summary/body constraints and mail party/box indices survive UI additions. The final PT A05/A06/A41 residual is separately blocked at G03/G09; upstream receipt is not a whole-file guarantee.',
 ('R5-U04', 'R5-U06'): 'Battle-context background/base/time values pass to WP67-A resource chains. WP39§7.3 keeps identity priority separate from file resolution, including no independent base1 fallback; action exceptions do not imply scene recovery.',
 ('R5-U05', 'R5-U06'): 'Qualified local AI score vectors remain distinct from battle interaction and rendering observations. The six U08 administrative mirrors add no prediction, scoring or AI-control behavior.',
 ('R5-U01', 'R5-U07'): 'Compiler/content schemas and author workflow facts supply developer tooling. WP73-A split manual registration, archive save and PBS reverse writing; nested writes survive outer cancellation, and U07 conversion premises retain SC-U07-001 capture-body LF exclusion.',
 ('R5-U03', 'R5-U07'): 'Current quantity/default and dynamic-form primary facts supply editor/debug consumers. WP72 debug condition restricts its explicit UI registration only; lower-level form submission registration is retained even for eggs/preparation.',
 ('R5-U06', 'R5-U07'): 'Developer UI and animation/input prerequisites remain finite. U07 loader/converter/editor facts do not assert host/runtime success or erase prior local UI behavior; source discovery and diagnostic failure scopes stay separate.'
}
rows = []
for e in edges:
    checks = [verify(e['source_accepted_receipt']), verify(e['target_contract'])]
    receipt = load(e['source_accepted_receipt']['commit'], e['source_accepted_receipt']['path'])
    actual = receipt['actual']
    actual_ok = actual == e['source_accepted_actual']
    tree_ok = git('rev-parse', actual['commit'] + '^{tree}').decode().strip() == actual['tree']
    report = receipt['independent_review']
    checked_report = verify({'commit': report['commit'], **report['report']})
    expected_ids = {x['id'] for x in matrix if e['target'] == 'R5-U08' or x['batch'] == e['target']}
    id_ok = set(e['target_required_ids']) == expected_ids
    records_ok = all(x['record']['accepted_actual_subject'] == actual['commit']
                     and x['record']['independent_actual_review'] == report['commit']
                     and not x['record']['whole_shared_file_receipt_implied'] for x in e['target_dependency_records'])
    if e['target'] == 'R5-U08':
        analysis = 'Final finite aggregation consumes this exact accepted owner contribution; current required paragraphs, sync targets and shared-context signatures are explicitly reviewed in criterion-results/shared-file-results. No predecessor CLOSED or whole-file receipt is required. U08 candidate is blocked solely by PT A05/A06/A41 output-scope residual; handshake PASS does not accept those consumer vectors.'
    else:
        analysis = analyses[(e['source'], e['target'])]
    ok = all(x['result'] == 'PASS' for x in checks + [checked_report]) and actual_ok and tree_ok and id_ok and records_ok
    rows.append({'source': e['source'], 'target': e['target'], 'result': 'PASS' if ok else 'FAIL',
                 'upstream_actual': actual, 'receipt_identity': checks[0], 'target_contract_identity': checks[1],
                 'independent_actual_report_identity': checked_report,
                 'target_required_ids': e['target_required_ids'], 'target_ids_exact': id_ok,
                 'accepted_actual_exact': actual_ok, 'actual_tree_exact': tree_ok,
                 'target_records_qualified_exact': records_ok, 'shared_paths': e['shared_paths'],
                 'current_input_contract_judgment': analysis,
                 'PASS_scope': 'Exact accepted upstream and necessary current input contract; no output whole-file/closure or actual-U08 acceptance implied.'})
save('dependency-results.json', {'schema': 'independent.r5.u08.dependencies.v1', 'candidate': C,
     'subject': S, 'edges': rows, 'edge_count': len(rows), 'frozen_edges_exact': True,
     'result': 'PASS' if all(x['result'] == 'PASS' for x in rows) else 'FAIL',
     'aggregate_consumer_gate': 'FAIL_AT_G03_G09_PT_A05_A06_A41', 'CLOSED': 0})
print(json.dumps({'edges': len(rows), 'fail': [x['source']+'>'+x['target'] for x in rows if x['result']!='PASS']}))
