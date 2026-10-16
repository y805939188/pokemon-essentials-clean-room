"""Identity-only checks of fixed, inert inputs. No restored code is executed."""
import datetime
import hashlib
import json
import pathlib
import subprocess

REPO = pathlib.Path('/workspace/pokemon-essentials-clean-room')
REF = pathlib.Path('/workspace/pokemon-essentials')
ROOT = REPO / 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
TASK = ROOT / 'tasks/receive_external_combat_presentation'
OUT = TASK / 'continuation-results/01_scene_input_objects'
CONTRACT = '35d85e4484b892ebc32542346861440638d2183c'

def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])

def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())

def main():
    d = json.loads((TASK/'continuation/01_scene_input_objects/readset.complete.json').read_text())
    c = json.loads((TASK/'continuation-contracts.json').read_text())
    results = []
    for f in d['original_complete_readset']['files']:
        raw = git(REPO, 'show', d['target_commit']+':'+f['remote_path_at_target_commit'])
        cached = TASK/'recovered'/d['target_commit']/f['relative_to_target_task']
        actual = identity(raw)
        mode = git(REPO, 'ls-tree', d['target_commit'], '--', f['remote_path_at_target_commit']).decode().split()[0]
        assert all(actual[k] == f[k] for k in actual), f
        assert mode == f['mode']
        assert cached.read_bytes() == raw
        results.append(dict(path=f['remote_path_at_target_commit'], cache=str(cached.relative_to(REPO)),
                            mode=mode, **actual, cache_equal=True))
    target_dir = results[0]['path'].rsplit('/', 1)[0]
    assert git(REPO, 'rev-parse', d['target_commit']+'^{tree}').decode().strip() == d['target_checkout_tree']
    assert git(REPO, 'rev-parse', d['target_commit']+':'+target_dir).decode().strip() == d['target_task_tree']
    observed_set = set(git(REPO, 'ls-tree', '-r', '--name-only', d['target_commit'], '--', target_dir).decode().splitlines())
    assert observed_set == {x['path'] for x in results}
    ids = [v for j in c['jobs'] for v in j['ids']]
    assert len(ids) == len(set(ids))
    j = next(x for x in c['jobs'] if x['id'] == '01_scene_input_objects')
    assert j['ids'] == [x['id'] for x in d['primary_objects']]
    assert j['groups'] == [x['id'] for x in d['source_groups']]
    inputs = []
    sources = {x['source']['path']: x['source'] for x in d['primary_objects']}
    for f in [*sources.values(), *d['all_dependency_identity_candidates']]:
        repo = REF if f['commit'] == d['fixed_R'] else REPO
        raw = git(repo, 'show', f['commit']+':'+f['path'])
        actual = identity(raw)
        assert all(actual[k] == f[k] for k in actual), f
        assert (repo/f['path']).read_bytes() == raw
        inputs.append(dict(repo=str(repo), commit=f['commit'], path=f['path'], **actual))
    for kind in ['prompt','readset']:
        p = ROOT/j[kind+'_identity']['path']
        actual = identity(p.read_bytes())
        assert all(actual[k] == j[kind+'_identity'][k] for k in actual)
    receipt = dict(schema='r8-cp01-input-identities/v1', utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   contract_commit=CONTRACT, embedded_readset_contract=d['contract_commit'],
                   effective_contract_rule='User fixed 35d85e; embedded 40f45d is historical provenance, not substituted HEAD.',
                   target_commit=d['target_commit'], target_tree=d['target_checkout_tree'], target_task_tree=d['target_task_tree'],
                   target_files=results, target_file_count=len(results), target_bytes=sum(x['bytes'] for x in results),
                   source_and_dependency_identities=inputs, primary_object_count=len(j['ids']),
                   source_partition_unique_count=len(ids), identity_check='PASS', semantic_credit=0,
                   restored_code_executed=False, business_execution='NOT_EXECUTED')
    (OUT/'input-identities.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ['identity_check','target_file_count','target_bytes','primary_object_count','source_partition_unique_count','semantic_credit']}))

if __name__ == '__main__':
    main()
