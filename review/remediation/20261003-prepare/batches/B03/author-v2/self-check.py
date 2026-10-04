#!/usr/bin/env python3
"""Document/Git metadata audit only; no reference or behavioral vector execution."""
import argparse, collections, hashlib, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
V2 = Path(__file__).resolve().parent
V1 = V2.with_name('author')
BASE = '9576f00e7d3aeb96f7ca8c42caccfba8f808505e'
PARENT = 'cdb689ba7f20ec8699329015fc5bdd520ca3a037'
REFERENCE = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
TREE = '7589c800b61ba13a13040ed0d686979b80a84fd0'
V1_PREFIX = str(V1.relative_to(ROOT)) + '/'
V2_PREFIX = str(V2.relative_to(ROOT)) + '/'

def git(*args, repo=ROOT):
    return subprocess.check_output(['git', '-C', str(repo), *args])
def sha(data):
    return hashlib.sha256(data).hexdigest()
def read(name, directory=V1):
    return json.loads((directory / name).read_text())
def need(condition, label):
    if not condition:
        raise AssertionError(label)
def rows(text, pattern):
    found = {}
    for line in text.splitlines():
        match = re.match(pattern, line)
        if match:
            need(match[1] not in found, 'duplicate row ' + match[1])
            found[match[1]] = line
    return found
def unchanged_sections(old, new, markers):
    for marker in markers:
        def extract(text):
            start = text.index(marker)
            rest = text[start + len(marker):]
            stop = re.search(r'^#{1,4} ', rest, re.M)
            return marker + (rest[:stop.start()] if stop else rest)
        need(extract(old) == extract(new), 'protected section ' + marker)

def run(ref):
    scope, manifest = read('scope.json'), read('input-manifest.json')
    amendment = read('scope-amendment.json', V2)
    formal = amendment['authorized_formal_paths']
    originals = amendment['additional_formal_write_paths']
    need(len(formal) == len(set(formal)) == 13, '13 authorized formal paths')
    need(amendment['inherited_formal_write_paths'] == scope['write_paths'], 'original 7 write lock')
    need(len(scope['read_paths']) == len(manifest['read_identities']) == 57, '57 frozen stage reads')
    need(len(scope['contribution_finding_ids']) == 27 and len(scope['primary_finding_ids']) == 19, '27/19 finding scope')
    lock = next(x for x in json.loads(git('show', BASE + ':review/remediation-20261003-prepare/stage-locks.json')) if x['stage'] == 'B03-A')
    need(lock['reads'] == scope['read_paths'] and lock['writes'] == scope['write_paths'], 'original stage lock untouched')
    changed = set(git('diff', '--name-only', BASE).decode().splitlines())
    untracked = set(git('ls-files', '--others', '--exclude-standard').decode().splitlines())
    need(changed.intersection(formal) == set(formal), 'complete candidate changes all 13 formal paths versus B02')
    need(all(p in formal or p.startswith((V1_PREFIX, V2_PREFIX)) for p in changed | untracked), 'full mutation whitelist')
    git('diff', '--check', BASE)
    frozen_v1 = git('ls-tree', '-r', '--name-only', PARENT, '--', V1_PREFIX).decode().splitlines()
    need(set(frozen_v1) == {str(p.relative_to(ROOT)) for p in V1.iterdir() if p.is_file()}, 'old author exact file set')
    for p in frozen_v1:
        need((ROOT / p).read_bytes() == git('show', PARENT + ':' + p), 'immutable author-v1 bytes ' + p)
    append = read('append-input-manifest.json', V2)
    for item in append['additional_read_identities']:
        data = git('show', PARENT + ':' + item['path'])
        need(sha(data) == item['sha256'] and len(data) == item['bytes'], 'append input frozen ' + item['path'])
        need(git('rev-parse', PARENT + ':' + item['path']).decode().strip() == item['git_blob'], 'append input blob')
    for item in manifest['read_identities'] + manifest.get('supplementary_read_identities', []):
        data = git('show', item['commit'] + ':' + item['path'])
        need(sha(data) == item['sha256'] and len(data) == item['bytes'], 'frozen stage input ' + item['path'])
        need(git('rev-parse', item['commit'] + ':' + item['path']).decode().strip() == item['git_blob'], 'stage input blob')
        if item.get('in_fix_base') and item['path'] not in formal:
            need((ROOT / item['path']).read_bytes() == data, 'read-only upstream ' + item['path'])
    formal_increment = set(git('diff', '--name-only', PARENT, '--', *formal).decode().splitlines())
    need(formal_increment == set(originals + [scope['write_paths'][5], scope['write_paths'][6]]), 'v2 six original paths plus two C048 clarifications')
    for p in scope['write_paths'][:-2]:
        need((ROOT / p).read_bytes() == git('show', PARENT + ':' + p), 'other final v1 payload unchanged ' + p)
    final14 = scope['write_paths'][5]
    old_final14 = git('show', PARENT + ':' + final14).decode()
    expected_final14 = old_final14.replace('  - 墙顶：在指定墙型上方的第二层绘制。', '  - 墙顶：正南第一墙层为外墙 2/内墙 1/内墙 3 时，在本格第三图块层绘制（层索引 2）。')
    need((ROOT / final14).read_text() == expected_final14, 'only C048 summary layer change in final WP14')
    protected_history = []
    for p in originals:
        old, new = git('show', PARENT + ':' + p).decode(), (ROOT / p).read_text()
        marker = '## 4. 证据与来源（traceability）' if p.endswith('move-route-matrix.md') else '## 10. 证据与来源（traceability）'
        if marker in old:
            need(old[old.index(marker):] == new[new.index(marker):], 'historical traceability/unknowns/approval exact ' + p)
            protected_history.append({'path':p,'marker':marker,'sha256':sha(old[old.index(marker):].encode())})
        first = '## 1.'
        if first in old:
            need(old[:old.index(first)] == new[:new.index(first)], 'historical header exact ' + p)
    wp11, wp12, im, main13, mr, wp14 = [(ROOT / p).read_text() for p in originals]
    old11, old12, oldim, oldmain, oldmr, old14 = [git('show', PARENT + ':' + p).decode() for p in originals]
    edge = next(l for l in old11.splitlines() if l.startswith('| 边缘跨图（'))
    need(edge in wp11.splitlines() and '天气持续重置 20' in edge, 'correct original WP11 weather20 row exact')
    predicate = '**骑行按目的地图许可决定**——无目的地或目的地 `pbCanUseBike?` 为假时清 bicycle。'
    need(predicate in old12 and predicate in wp12, 'correct bike predicate retained')
    for literal in ['`sight(N)`/`trainer(N)`', '`counter(N)`', '`s:`']:
        need(literal in oldmain and literal in main13, 'original ASCII literal retained ' + literal)
    for literal in ['move_random_range', 'move_random_UD', 'move_random_LR']:
        need(literal in oldmr and literal in mr, 'original route literal retained ' + literal)
    b01 = next(l for l in old14.splitlines() if l.startswith('- **大网格奇数参数调整'))
    final_b01 = next(l for l in git('show', BASE + ':' + final14).decode().splitlines() if l.startswith('- **大网格奇数参数调整'))
    need(b01 in wp14.splitlines() and final_b01 in (ROOT / final14).read_text().splitlines(), 'B01 original/final first odd-write failure respective baseline bytes exact')
    b01_rows = [l for l in old14.splitlines() if l.startswith('| ') and '（GR-006） |' in l]
    need(len(b01_rows) == 5 and all(l in wp14.splitlines() for l in b01_rows), 'five original B01 static rows unchanged')
    unchanged_sections(old11, wp11, ['## 1.', '## 2.', '### 3.1', '### 3.2', '### 5.2', '## 6.', '## 7.', '## 8.', '### 9.1'])
    unchanged_sections(old12, wp12, ['## 1.', '## 2.', '### 3.1', '### 5.2', '## 6.', '## 7.', '### 9.1'])
    unchanged_sections(oldmain, main13, ['## 1.', '## 2.', '### 3.1', '### 3.2', '### 4.2', '### 6.2', '## 7.', '## 8.', '### 9.1'])
    unchanged_sections(old14, wp14, ['## 1.', '## 2.', '### 3.1', '### 3.2', '### 3.3', '### 3.4', '### 4.3', '### 6.2', '## 7.', '### 9.1'])
    im_pattern = r'^\| (\d+) \|'
    old_im_rows, new_im_rows = rows(oldim, im_pattern), rows(im, im_pattern)
    allowed_im = {'101','102','106','111','411','413','201','205','206','223','231','232','233','234','235','251'}
    need(set(old_im_rows) == set(new_im_rows) and len(new_im_rows) == 96, 'original 96 command identities')
    need({c for c in old_im_rows if old_im_rows[c] != new_im_rows[c]} == allowed_im, 'exact 16 original assigned rows; 124/314 preserved')
    need(oldim.split('## 3. 统计与口径',1)[1] == im.split('## 3. 统计与口径',1)[1], 'original 28/2/66 statistics and historical notes exact')
    old_route, new_route = rows(oldmr, im_pattern), rows(mr, im_pattern)
    need(set(new_route) == set(old_route) == {str(i) for i in range(46)}, 'original route 0..45')
    need({c for c in old_route if old_route[c] != new_route[c]} == {'15','45'}, 'only two original assigned route rows')
    cat = scope['write_paths'][6]
    old_cat, v1_cat, new_cat = [git('show', rev + ':' + cat) for rev in [BASE, PARENT]] + [(ROOT / cat).read_bytes()]
    need(old_cat.split(b'## H.',1)[1] == new_cat.split(b'## H.',1)[1], 'WP15/59/60 protected tail')
    pattern = r'^\| ((?:MP|MV|EV|FW|IM|MR|DG)\d+) \|'
    baseline_rows, v1_rows, new_rows = [rows(t.decode(), pattern) for t in [old_cat,v1_cat,new_cat]]
    expected_v2_cat = v1_cat.decode().replace('；墙顶只认正南墙层外2/内1/内3 |','；墙顶只认正南第一墙层外2/内1/内3，并写本格第三图块层（索引2） |')
    joins = [('MP15','MP16'),('MV41','MV42'),('EV31','EV32'),('IM12','IM13'),('MR09','MR10'),('DG24','DG25')]
    for last, first in joins:
        pattern_join = r'(^\| ' + last + r' \|[^\n]*\n)\n(?=\| ' + first + r' \|)'
        expected_v2_cat, count = re.subn(pattern_join, r'\1', expected_v2_cat, flags=re.M)
        need(count == 1, 'one exact B03 table join ' + last + '/' + first)
    need(new_cat.decode() == expected_v2_cat, 'catalog only DG43 output layer and six exact B03 table joins')
    counts = dict(collections.Counter(re.sub(r'\d+$','',c) for c in new_rows))
    need(counts == {'MP':27,'MV':67,'EV':39,'FW':7,'IM':35,'MR':17,'DG':43}, '235 frozen B03 vectors')
    allowed_old = {'MP05','MV03','MV11','MV13','EV27','EV28','EV29','IM01','MR08','DG01','DG02','DG07','DG08','DG11','DG12','DG23'}
    need(set(baseline_rows).issubset(new_rows), 'all old static IDs retained')
    need(all(new_rows[c] == line for c,line in baseline_rows.items() if c not in allowed_old), 'all unassigned baseline rows untouched')
    need(all(new_rows[c] == baseline_rows[c] for c in ['DG18','DG19','DG20','DG21','DG22']), 'B01 catalog rows untouched')
    matrix = rows((ROOT / scope['write_paths'][2]).read_text(), im_pattern)
    categories = collections.Counter(l.split('|')[7].strip().strip('*') for l in matrix.values())
    need(dict(categories) == {'有实现':66,'标记':2,'空操作':28}, 'final command classification')
    need(len(rows((ROOT / scope['write_paths'][4]).read_text(), im_pattern)) == 46, 'final route identities')
    link_count, table_count = 0, 0
    for p in formal:
        text = (ROOT / p).read_text()
        need('```' not in text, 'no copied source fences ' + p)
        for target in re.findall(r'\[[^\]]+\]\(([^)]+\.md)(?:#[^)]*)?\)', text):
            if not re.match(r'[a-z]+:', target):
                need(((ROOT / p).parent / target).resolve().is_file(), 'relative link ' + p + ':' + target)
                link_count += 1
        blocks = re.findall(r'(?:^\|[^\n]*\n)+', text, re.M)
        for block in blocks:
            lines = block.splitlines()
            need(len(lines)>1 and re.match(r'^\|(?:\s*:?-+:?\s*\|)+$', lines[1]), 'contiguous Markdown table ' + p)
            table_count += 1
    effective = read('effective-finding-inputs.json')
    original_objects = {x['id']:x for x in json.loads(git('show','93e10babe0b9c9ef8b3f5277754541b447beeeb4:review/global-independent-review/2026-10-03-fd82a639/findings.json'))}
    accepted = json.loads(git('show','41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/finding-acceptance.json'))
    for item in effective:
        need(item['complete_original_object'] == original_objects[item['id']] and item['acceptance'] == accepted[item['id']], 'full effective/adjudicated finding ' + item['id'])
        need(sha(json.dumps(original_objects[item['id']],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()) == item['original_object_sha256'], 'effective object digest')
    responses, proposals = read('finding-responses.json', V2), read('registry-proposals.json', V2)['requests']
    need({x['id'] for x in responses} == {x['id'] for x in proposals} == set(scope['contribution_finding_ids']), '27 v2 per-ID handoffs')
    need(sum(x['primary_in_B03'] for x in responses) == 19 and all(not x['canonical_edited'] for x in proposals), 'primary counts/public registry unmodified')
    need(not ref.is_relative_to(ROOT) and not ref.is_relative_to(Path('/workspace/pokemon-essentials-clean-room')), 'reference isolated outside main repo')
    need(git('rev-parse','HEAD',repo=ref).decode().strip() == REFERENCE and git('rev-parse','HEAD^{tree}',repo=ref).decode().strip() == TREE, 'fixed reference SHA/tree')
    need(not git('status','--porcelain',repo=ref).strip(), 'reference clean/read-only')
    source_log = read('source-reading-log.json') + read('source-reading-log.json', V2)
    for item in source_log:
        data = (ref / item['path']).read_bytes()
        need(sha(data) == item['sha256'] and len(data) == item['bytes'], 'reference read identity ' + item['path'])
        need(git('rev-parse', 'HEAD:' + item['path'],repo=ref).decode().strip() == item['git_blob'], 'reference blob')
    request = read('execution-request-receipt.json')
    need(request['actual_effective_model'] == request['actual_effective_reasoning'] == request['actual_effective_speed'] == 'UNVERIFIED' and request['subagents_spawned'] == 0, 'strategy A actual config unverified/no delegation')
    return {'result':'PASS_DOCUMENT_AND_GIT_IDENTITY_AUDIT','semantic_review_status':'AUTHOR_V2_AWAITING_FRESH_INDEPENDENT_ULTRA','audit_type':'document/Git identity and protected-byte audit only; no behavioral execution','fix_base_commit':BASE,'append_parent_commit':PARENT,'formal_write_count':13,'formal_increment_paths':sorted(formal_increment),'formal_payload':[{'path':p,'sha256':sha((ROOT/p).read_bytes()),'bytes':len((ROOT/p).read_bytes())} for p in formal],'frozen_stage_read_count':57,'supplementary_historical_read_count':len(manifest.get('supplementary_read_identities',[])),'old_author_files_byte_preserved':len(frozen_v1),'frozen_original_and_acceptance_objects_verified':27,'finding_contributions':27,'primary_findings':19,'protected_original_history':protected_history,'static_vector_counts':counts,'static_vectors_total':len(new_rows),'new_vectors_since_author_v1':0,'new_vectors_since_B02':len(new_rows)-len(baseline_rows),'v2_catalog_amendments':['DG43'],'v2_B03_table_joins':joins,'WP15_WP59_WP60_tail_sha256':sha(new_cat.split(b'## H.',1)[1]),'B01_original_first_write_failure_paragraph_sha256':sha(b01.encode()),'B01_final_first_write_failure_paragraph_sha256':sha(final_b01.encode()),'interpreter_categories':dict(categories),'relative_links_checked':link_count,'markdown_tables_checked':table_count,'reference_commit':REFERENCE,'reference_tree':TREE,'reference_clean':True,'reference_files_read':len({x['path'] for x in source_log}),'inherited_source_read_operations':48,'v2_source_read_operations':3,'all_existing_paths_outside_authorized_scope_unchanged':True,'all_historical_review_approval_stage_lock_and_public_registry_files_unchanged':True,'all_other_original_specs_unchanged':True,'runtime_observations':0,'proven_demo_chains':0,'static_vectors_executed':0,'solver_or_reference_execution':False,'effective_execution_configuration':'UNVERIFIED, inherited strategy A'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--reference',default='/workspace/reference-B03-20261003-prepare')
    parser.add_argument('--report')
    args = parser.parse_args()
    result = run(Path(args.reference).resolve())
    target = Path(args.report) if args.report else V2/'self-check-result.json'
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['formal_payload','protected_original_history']},ensure_ascii=False,indent=2))
