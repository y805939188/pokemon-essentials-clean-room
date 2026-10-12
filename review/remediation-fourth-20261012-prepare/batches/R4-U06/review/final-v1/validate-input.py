#!/usr/bin/env python3
"""Independent fixed-input identity checks; TOOL_VALIDATION, no behavior execution."""
import collections
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
REPO = next(p for p in ROOT.parents if (p / 'AGENTS.md').is_file())
PREFIX = 'review/remediation-fourth-20261012-prepare/'
PACK = PREFIX + 'registration/R4-U06/'
FORMAL = 'deliverables/final-specification-set/'
INPUT = '1dd05964f59772886de9b808a929c168c73fa184'
TASK = '7897037ae93af82aa9246a097c4badbd344a15b1'
B = '1f36475d22120a0d1175967d5b17d71fe8311d88'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)

def read(commit, path):
    return git('show', commit + ':' + path)

def obj(commit, path):
    return json.loads(read(commit, path))

def ident(commit, path):
    data = read(commit, path)
    return {'path': path, 'commit': commit, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': git('rev-parse', commit + ':' + path).decode().strip()}

def verify(expected, commit):
    actual = ident(commit, expected['path'])
    for key in ('bytes', 'sha256', 'git_blob'):
        if key in expected:
            assert actual[key] == expected[key], (expected['path'], key)
    return actual

def main():
    assert git('rev-parse', INPUT+'^{tree}').decode().strip() == '778481a38dad208ebb54127ca3b4a58078c4bc0e'
    assert git('rev-parse', TASK+'^{tree}').decode().strip() == 'f4026ead2457d3cccc693beb3bb240c69ec24cad'
    files = obj(INPUT, PACK+'formal-identities.json')['records']
    listed = {r['path'] for r in files}
    actual_paths = set(git('ls-tree', '-r', '--name-only', INPUT, FORMAL).decode().splitlines())
    assert len(files) == len(listed) == 131 and listed == actual_paths
    results = []
    for r in files:
        result = verify(r, INPUT)
        result.update({k:r[k] for k in ('partition','sole_formal_owner','exact_origin_commit','actual_semantic_scope')})
        result['task_publication_equal'] = read(INPUT,r['path']) == read(TASK,r['path'])
        assert result['task_publication_equal']
        result['B_equal'] = read(INPUT,r['path']) == read(B,r['path'])
        assert result['B_equal'] == (r['partition'] == 'B_unchanged')
        results.append(result)
    partitions = collections.Counter(r['partition'] for r in results)
    assert partitions == {'B_unchanged':103,'GR4_scoped_accepted':28}
    changed = set(git('diff','--name-only',B,INPUT,'--',FORMAL).decode().splitlines())
    assert changed == {r['path'] for r in results if not r['B_equal']}
    current = obj(INPUT,PACK+'findings-and-criteria.json')['records']
    assert len(current) == len({r['id'] for r in current}) == 17
    assert sum(len(r['all_actual_criterion_results']) for r in current) == 76
    assert all(len(r['all_actual_criterion_results']) == r['criteria_count'] and not r['CLOSED'] for r in current)
    gates = obj(INPUT,PACK+'dependencies-and-shared-proposals.json')
    assert len(gates['dependency_edges']) == 5 and len(gates['four_final_handshakes']) == 4
    acceptance = [verify(r['acceptance'], INPUT) for r in gates['dependency_edges']]
    scoped = obj(INPUT,PREFIX+'registration/status-ledger.json')
    assert scoped['sole_writer'] == 'fourth-preparation-registrar'
    assert scoped['accepted_scoped_GR4'] == 17 and scoped['effective_CLOSED_GR4'] == 0 and scoped['historical_CLOSED_GR3'] == 23
    packets = []
    for path in git('ls-tree','-r','--name-only',TASK,PACK).decode().splitlines():
        packets.append(ident(TASK,path))
        if path.endswith('.json'):
            obj(TASK,path)
    bounded = obj(INPUT,PACK+'bounded-preparation-check.json')
    for expected in bounded['packet_file_identities']:
        verify(expected,INPUT)
    chain_payloads = {}
    for r in current:
        for expected in r['exact_qualified_chain']['actual_review']['files']:
            checked = verify(expected,INPUT)
            chain_payloads[expected['path']] = checked
        verify(r['exact_qualified_chain']['acceptance'],INPUT)
        for expected in r['current_formal_file_identities']:
            verify(expected,INPUT)
    checks = {
        'fixed_input_tree': '778481a38dad208ebb54127ca3b4a58078c4bc0e',
        'fixed_task_tree': 'f4026ead2457d3cccc693beb3bb240c69ec24cad',
        'formal_tree':git('rev-parse',INPUT+':deliverables/final-specification-set').decode().strip(),
        'formal_paths':131,'partitions':dict(partitions),
        'amended_owner_counts':dict(collections.Counter(r['sole_formal_owner'] for r in results if not r['B_equal'])),
        'findings':17,'criteria':76,'five_dependencies':5,'four_handshakes':4,
        'accepted_scoped':17,'effective_CLOSED_GR4':0,'historical_CLOSED_GR3':23,
        'fixed_input_to_task_formal_delta':[],
        'formal_identities':results,'task_packets':packets,
        'actual_review_payloads':list(chain_payloads.values()),'acceptance_payloads':acceptance}
    out={'status':'PASS_FIXED_INPUT_IDENTITIES_AND_BOUNDARIES','evidence_level':'TOOL_VALIDATION',
         'semantic_review':'Separate independent combination judgments; identities alone are not PASS',
         'historical_tuple_policy':'Prior independent exact candidate/actual qualification reused after inherited payload verification; absent historical trees not falsely freshly read',
         'new_behavior_execution':{'reference':0,'model':0,'host_or_demo':0},'checks':checks,'errors':[]}
    (ROOT/'input-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'formal':131,'findings':17,'criteria':76,'actual_payloads':len(chain_payloads),'errors':[]}))

if __name__ == '__main__':
    main()
