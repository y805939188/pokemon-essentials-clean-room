"""Local artifact consistency or exact remote readback for this review directory.
Does not run reference code, invoke restored scripts, or modify other project files.
"""
import argparse, datetime, hashlib, json, os, re, subprocess, tempfile
from pathlib import Path
OUT = Path(__file__).resolve().parent
REPO = next(p for p in OUT.parents if (p / 'AGENTS.md').is_file())
PREFIX = str(OUT.relative_to(REPO))
CONTRACT = '35d85e4484b892ebc32542346861440638d2183c'
BRANCH = 'codex/r8-cp-reception-04-20261016'
def run(args, **kwargs):
    return subprocess.run(args, check=True, capture_output=True, **kwargs)
def git(*args):
    return run(['git', '-C', str(REPO), *args]).stdout
def load(name):
    return json.loads((OUT / name).read_text())
def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
def local():
    x = json.loads((OUT.parent.parent / 'continuation/04_author_player/readset.complete.json').read_text())
    f = load('frozen-denominator.json')
    a = load('reception-ledger.json')
    i = load('interfaces.json')
    l = load('reading-ledger.json')
    q = load('qualifications.json')
    assert git('branch', '--show-current').decode().strip() == BRANCH
    expected = [r['id'] for r in x['primary_objects']]
    assert expected == f['primary_ids'] == [r['id'] for r in a['primary']]
    assert len(expected) == len(set(expected)) == 67
    original = {r['id']: r for r in x['primary_objects']}
    by_path = {r['path']: r for r in l['inputs']}
    for r in a['primary']:
        assert r['original_complete'] == original[r['id']]
        assert r['accepted_complete_meaning'] and r['normal_or_counter_control']
        assert r['current_formal_locator'] and r['necessary_unreceived'] == []
        assert r['execution'] == 'NOT_EXECUTED'
        o = original[r['id']]
        span = o['source_range']
        assert any(s <= span[0] <= span[1] <= e for s, e in by_path[o['source']['path']]['read_intervals'])
    reverse = [s['id'] for g in x['reverse_current_contribution_objects'] for s in g['subassertions']]
    assert reverse == f['reverse_ids'] == [r['id'] for r in i['reverse_current_contribution']]
    assert len(reverse) == len(set(reverse)) == 21
    assert f['interface_ids'] == [r['id'] for r in i['selected_reverse_interfaces']]
    assert len(f['interface_ids']) == 3
    for r in i['reverse_current_contribution']:
        assert r['accepted_meaning_and_reason'] and r['source_object_links']
        assert set(r['source_object_links']) <= set(expected)
    for r in i['selected_reverse_interfaces']:
        assert set(r['accepted_source_ids']) <= set(expected)
        assert set(r['accepted_source_ids']).isdisjoint(r['foreign_index_ids_without_atom_credit'])
        assert r['necessary_unreceived'] == []
    assert a['primary_unreceived'] == 0 and a['necessary_units_unreceived'] == []
    assert q['H001']['decision'] == 'NO_REQUIRED_REVISION_SUPPORTED_BY_THIS_HYPOTHESIS'
    assert q['H001']['independent_receiver'] == a['actual_receiver']
    assert a['actual_receiver'] not in (a['original_author'], a['parent_receiver'])
    for obj in (a, i, q, l, f):
        assert obj['UPDATE_NOT_STARTED'] is True
    # Independent mechanical value comparison supports, but does not grant, reading credit.
    source_path = '/workspace/pokemon-essentials/Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb'
    source = Path(source_path).read_text()
    formal = (REPO / 'deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md').read_text()
    src = {}
    for typ, values in re.findall(r'^\s*:(\w+)\s*=>\s*\[([^\]]*)\]', source, flags=re.M):
        src[typ] = re.findall(r':(\w+)|\b(nil)\b', values)
        src[typ] = [a or None for a, b in src[typ]]
    dst = {}
    for line in formal.splitlines():
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) == 7 and cells[0] in src:
            dst[cells[0]] = [None if c == '空' else c for c in cells[1:]]
    assert len(src) == len(dst) == 18 and src == dst
    for r in l['inputs']:
        root = Path('/workspace/pokemon-essentials') if r['commit'] == x['fixed_R'] else REPO
        raw = (root / r['path']).read_bytes()
        assert len(raw) == r['bytes'] and hashlib.sha256(raw).hexdigest() == r['sha256']
        assert raw == run(['git', '-C', str(root), 'show', r['commit'] + ':' + r['path']]).stdout
    changed = git('diff', '--name-only', CONTRACT).decode().splitlines()
    untracked = git('ls-files', '--others', '--exclude-standard').decode().splitlines()
    assert all(p.startswith(PREFIX + '/') for p in changed + untracked), changed + untracked
    result = dict(schema='gr8-cp04-local-validation/v1', utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  status='PASS_TOOL_VALIDATION_ONLY', primary_exact=67, reverse_exact=21, selected_interfaces_exact=3,
                  default_table=dict(types=18, cells=108, source_equals_formal=True),
                  source_and_formal_identities_checked=len(l['inputs']), exclusive_write_set=PREFIX + '/',
                  assertions_not_proven_by_tool='内容判断来自各条具名判断与实读；此脚本只核ID/来源/值/连续覆盖/边界及写集一致性。',
                  reference_or_model_business_executions=0, UPDATE_NOT_STARTED=True)
    write('validation.json', result)
    print(json.dumps(result, ensure_ascii=False))
def remote(commit, output, reuse):
    assert re.fullmatch('[0-9a-f]{40}', commit)
    assert not output or Path(output).name == output
    origin = git('remote', 'get-url', 'origin').decode().strip()
    work = tempfile.mkdtemp(prefix='r8-cp04-readback-')
    bare = str(Path(work) / 'remote.git')
    commands = [['git', 'init', '--bare', '--quiet', bare],
                ['git', '--git-dir=' + bare, 'remote', 'add', 'origin', origin],
                ['git', '--git-dir=' + bare, 'fetch', '--no-tags', '--depth=1', '--filter=blob:none', 'origin', commit]]
    # An optional previous independent bare contains only transport state, not semantic credit.
    if reuse:
        bare = reuse
        commands = [['git', '--git-dir=' + bare, 'fetch', '--no-tags', '--depth=1', '--filter=blob:none', 'origin', commit]]
    receipts = []
    for cmd in commands:
        result = run(cmd)
        receipts.append(dict(command=cmd, exit=result.returncode, stdout=result.stdout.decode(), stderr=result.stderr.decode()))
    def remote_git(*args):
        return run(['git', '--git-dir=' + bare, *args]).stdout
    local_tree = git('ls-tree', '-r', '-z', commit, '--', PREFIX)
    remote_tree = remote_git('ls-tree', '-r', '-z', commit, '--', PREFIX)
    assert local_tree == remote_tree
    files = []
    for entry in local_tree.split(b'\0'):
        if not entry:
            continue
        meta, raw_path = entry.split(b'\t', 1)
        mode, typ, blob = meta.decode().split()
        assert typ == 'blob'
        path = raw_path.decode()
        raw = remote_git('show', commit + ':' + path)
        local_raw = git('show', commit + ':' + path)
        assert raw == local_raw
        assert hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == blob
        files.append(dict(path=path, mode=mode, git_blob=blob, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest()))
    roots = {}
    for label, suffix in [('checkout_tree', '^{tree}'), ('task_tree', ':' + PREFIX)]:
        actual = remote_git('rev-parse', commit + suffix).decode().strip()
        assert actual == git('rev-parse', commit + suffix).decode().strip()
        roots[label] = actual
    result = dict(schema='gr8-cp04-remote-readback/v1', utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  commit=commit, branch=BRANCH, origin=origin, **roots, files=files, file_count=len(files),
                  collection_equal=True, all_mode_blob_bytes_sha256_equal=True, commands=receipts,
                  bare=bare, reused_transport_cache=bool(reuse), semantic_credit=0, UPDATE_NOT_STARTED=True)
    if output:
        write(output, result)
    print(json.dumps(dict(commit=commit, **roots, file_count=len(files), equal=True, bare=bare, output=output), ensure_ascii=False))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--remote')
    parser.add_argument('--output')
    parser.add_argument('--reuse')
    args = parser.parse_args()
    if args.remote:
        remote(args.remote, args.output, args.reuse)
    else:
        local()
