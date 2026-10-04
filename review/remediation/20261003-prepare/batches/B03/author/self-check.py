#!/usr/bin/env python3
"""Document/Git identity audit only. Does not execute reference or behavioral vectors."""
import argparse, collections, hashlib, json, re, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
AUTHOR = Path(__file__).resolve().parent
BASE = '9576f00e7d3aeb96f7ca8c42caccfba8f808505e'
REFERENCE = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
TREE = '7589c800b61ba13a13040ed0d686979b80a84fd0'
PREFIX = 'review/remediation/20261003-prepare/batches/B03/author/'
def git(*args, repo=ROOT):
    return subprocess.check_output(['git', '-C', str(repo), *args])
def digest(data):
    return hashlib.sha256(data).hexdigest()
def get(name):
    return json.loads((AUTHOR / name).read_text())
def require(condition, message):
    if not condition:
        raise AssertionError(message)
def run(ref):
    manifest, scope = get('input-manifest.json'), get('scope.json')
    require(manifest['fix_base_commit'] == BASE, 'fix base')
    require(len(manifest['read_identities']) == 57, '57 read identities')
    require(len(scope['write_paths']) == len(set(scope['write_paths'])) == 7, '7 formal paths')
    require(len(scope['contribution_finding_ids']) == 27 and len(scope['primary_finding_ids']) == 19, 'finding counts')
    locks = json.loads(git('show', BASE + ':review/remediation-20261003-prepare/stage-locks.json'))
    lock = next(x for x in locks if x['stage'] == 'B03-A')
    require(lock['writes'] == scope['write_paths'] and lock['reads'] == scope['read_paths'], 'stage lock equality')
    changed = set(git('diff', '--name-only', BASE).decode().splitlines())
    untracked = set(git('ls-files', '--others', '--exclude-standard').decode().splitlines())
    formal = changed.intersection(scope['write_paths'])
    require(formal == set(scope['write_paths']), 'formal changed set exact 7')
    require(all(p in formal or p.startswith(PREFIX) for p in changed | untracked), 'mutation whitelist including author receipts')
    git('diff', '--check', BASE)
    read_proofs = []
    for item in manifest['read_identities'] + manifest.get('supplementary_read_identities', []):
        rev, path = item['commit'], item['path']
        data = git('show', rev + ':' + path)
        blob = git('rev-parse', rev + ':' + path).decode().strip()
        require(digest(data) == item['sha256'] and len(data) == item['bytes'] and blob == item['git_blob'], 'frozen identity ' + path)
        if item.get('in_fix_base') and path not in formal:
            require((ROOT / path).read_bytes() == data, 'read-only input unchanged ' + path)
        read_proofs.append({'path': path, 'commit': rev, 'git_blob': blob, 'sha256': digest(data), 'bytes': len(data)})
    cat = scope['write_paths'][-1]
    old_cat, new_cat = git('show', BASE + ':' + cat), (ROOT / cat).read_bytes()
    old_tail, new_tail = old_cat.split(b'## H.', 1)[1], new_cat.split(b'## H.', 1)[1]
    require(old_tail == new_tail, 'WP15/59/60 protected catalog tail bytes')
    row_pattern = r'^\| ((?:MP|MV|EV|FW|IM|MR|DG)\d+) \|.*$'
    old_rows = {}
    for line in old_cat.decode().splitlines():
        m = re.match(row_pattern, line)
        if m:
            old_rows[m.group(1)] = line
    new_rows = {}
    for line in new_cat.decode().splitlines():
        m = re.match(row_pattern, line)
        if m:
            require(m.group(1) not in new_rows, 'unique vector ' + m.group(1))
            new_rows[m.group(1)] = line
    require(set(old_rows).issubset(new_rows), 'all existing B03 vectors retained')
    allowed_old = {'MP05','MV03','MV11','MV13','EV27','EV28','EV29','IM01','MR08','DG01','DG02','DG07','DG08','DG11','DG12','DG23'}
    for case, line in old_rows.items():
        if case not in allowed_old:
            require(new_rows[case] == line, 'other accepted vector unchanged ' + case)
    counts = dict(collections.Counter(re.sub(r'\d+$', '', i) for i in new_rows))
    expected_counts = {'MP':27, 'MV':67, 'EV':39, 'FW':7, 'IM':35, 'MR':17, 'DG':43}
    require(counts == expected_counts, 'vector counts')
    for family, count in expected_counts.items():
        require({i for i in new_rows if i.startswith(family)} == {family+str(n).zfill(2) for n in range(1,count+1)}, 'continuous IDs '+family)
    wp14 = scope['write_paths'][5]
    old_text = git('show', BASE + ':' + wp14).decode()
    protected_paragraph = next(line for line in old_text.splitlines() if line.startswith('- **大网格奇数参数调整'))
    require(protected_paragraph in (ROOT / wp14).read_text().splitlines(), 'B01 accepted first-write failure paragraph')
    matrix = (ROOT / scope['write_paths'][2]).read_text()
    matrix_rows = [line.split('|') for line in matrix.splitlines() if re.match(r'^\| \d+ \|',line)]
    categories = collections.Counter(parts[7].strip().strip('*') for parts in matrix_rows)
    require(len(matrix_rows) == len({parts[1].strip() for parts in matrix_rows}) == 96, '96 unique commands')
    require(dict(categories) == {'有实现':66, '标记':2, '空操作':28}, '28/2/66 unchanged')
    noops = {int(parts[1]) for parts in matrix_rows if parts[7].strip().strip('*') == '空操作'}
    require(314 not in noops and set(range(311,323))-{314} <= noops, '314 not a no-op')
    routes = (ROOT / scope['write_paths'][4]).read_text()
    route_ids = re.findall(r'^\| (\d+) \|', routes, re.M)
    require(len(route_ids) == 46 and {int(i) for i in route_ids} == set(range(46)), 'route 0..45 preserved')
    link_count = 0
    for path in scope['write_paths']:
        text = (ROOT / path).read_text()
        require('```' not in text, 'no copied source/program fences in formal spec ' + path)
        for target in re.findall(r'\[[^\]]+\]\(([^)]+\.md)\)', text):
            if not re.match(r'[a-z]+:',target):
                require(((ROOT / path).parent / target).resolve().is_file(), 'relative link '+target)
                link_count += 1
    require(not ref.is_relative_to(ROOT) and not ref.is_relative_to(Path('/workspace/pokemon-essentials-clean-room')), 'reference outside main worktree')
    require(git('rev-parse','HEAD',repo=ref).decode().strip() == REFERENCE, 'reference SHA')
    require(git('rev-parse','HEAD^{tree}',repo=ref).decode().strip() == TREE, 'reference tree')
    require(not git('status','--porcelain',repo=ref).strip(), 'reference clean')
    source_rows = get('source-reading-log.json')
    source_paths = set()
    for item in source_rows:
        data = (ref / item['path']).read_bytes()
        require(digest(data) == item['sha256'] and len(data) == item['bytes'], 'read-only reference identity '+item['path'])
        require(git('rev-parse','HEAD:'+item['path'],repo=ref).decode().strip() == item['git_blob'], 'reference blob '+item['path'])
        source_paths.add(item['path'])
    effective = get('effective-finding-inputs.json')
    originals = {x['id']: x for x in json.loads(git('show', '93e10babe0b9c9ef8b3f5277754541b447beeeb4:review/global-independent-review/2026-10-03-fd82a639/findings.json'))}
    accepted = json.loads(git('show', '41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/finding-acceptance.json'))
    require(len(effective) == 27 and {x['id'] for x in effective} == set(scope['contribution_finding_ids']), 'complete effective 27 set')
    for item in effective:
        id = item['id']
        require(item['complete_original_object'] == originals[id], 'full original including adjudications/extensions ' + id)
        require(item['acceptance'] == accepted[id], 'full approved acceptance ' + id)
        canonical = json.dumps(originals[id], ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
        require(digest(canonical) == item['original_object_sha256'], 'canonical original digest ' + id)
    responses, requests = get('finding-responses.json'), get('registry-proposals.json')['requests']
    require({r['id'] for r in responses} == set(scope['contribution_finding_ids']), '27 responses exact')
    require({r['id'] for r in requests} == set(scope['contribution_finding_ids']), '27 registry proposals exact')
    require(sum(r['primary_in_B03'] for r in responses) == 19, '19 primary dispositions')
    require(all(not r['canonical_edited'] for r in requests), 'no canonical edits')
    require(len(get('root002-scenario-routing.json')) == 34, '34 root scenarios retained/routed')
    require(get('execution-request-receipt.json')['subagents_spawned'] == 0, 'no subagents')
    return {'audit_type':'document and Git identity audit; behavioral vectors unexecuted','result':'PASS_DOCUMENT_AUDIT','fix_base_commit':BASE,'frozen_stage_read_count':57,'supplementary_historical_read_count':len(manifest.get('supplementary_read_identities',[])),'formal_write_count':7,'formal_payload':[{'path':p,'sha256':digest((ROOT/p).read_bytes()),'bytes':len((ROOT/p).read_bytes())} for p in scope['write_paths']],'full_original_and_approved_acceptance_objects_verified':27,'finding_contributions':27,'primary_findings':19,'static_vector_counts':counts,'static_vectors_total':len(new_rows),'new_vector_count':len(new_rows)-len(old_rows),'existing_vector_amendments':sorted(i for i in old_rows if new_rows[i]!=old_rows[i]),'WP15_WP59_WP60_tail_sha256':digest(new_tail),'B01_first_write_failure_paragraph_sha256':digest(protected_paragraph.encode()),'interpreter_categories':dict(categories),'relative_links_checked':link_count,'reference_commit':REFERENCE,'reference_tree':TREE,'reference_clean':True,'reference_files_read':len(source_paths),'source_read_operations_logged':len(source_rows),'all_preexisting_paths_outside_whitelist_unchanged':True,'all_old_unassigned_catalog_rows_unchanged':True,'historical_review_approval_freeze_and_public_registry_unchanged':True,'original_specs_unchanged':True,'runtime_observations':0,'proven_demo_chains':0,'static_vectors_executed':0,'solver_or_reference_execution':False}
if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--reference',default='/workspace/reference-B03-20261003-prepare'); parser.add_argument('--report'); args=parser.parse_args()
    result = run(Path(args.reference).resolve())
    target = Path(args.report) if args.report else AUTHOR / 'self-check-result.json'
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['formal_payload','existing_vector_amendments']},ensure_ascii=False,indent=2))
