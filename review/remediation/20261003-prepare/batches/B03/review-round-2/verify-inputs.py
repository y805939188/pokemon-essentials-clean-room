#!/usr/bin/env python3
"""Independent Git/document identity audit. Never executes reference behavior.

Run from any directory with --project and --reference. All source reads are
literal bytes. No Ruby loading, deserialization, game vectors or formula solver.
"""
import argparse
import collections
import hashlib
import json
import re
import subprocess
from pathlib import Path

BASE = '9576f00e7d3aeb96f7ca8c42caccfba8f808505e'
CANDIDATE = '3c5728a47142c57abfdf3d55033768bc44a1f627'
HANDOFF = '105a21a0bcba174d4c22a0e67231ed4f38c97693'
APPEND_PARENT = 'cdb689ba7f20ec8699329015fc5bdd520ca3a037'
GLOBAL_REVIEW = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
REFERENCE = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REF_TREE = '7589c800b61ba13a13040ed0d686979b80a84fd0'
AUTHOR = 'review/remediation/20261003-prepare/batches/B03/author/'
AUTHOR_V2 = 'review/remediation/20261003-prepare/batches/B03/author-v2/'
AUTHOR_V3 = 'review/remediation/20261003-prepare/batches/B03/author-v3/'
PRIOR_CANDIDATE = '1e395a21eb3d5ed0be9426ed3d3f4443129b5ce8'
PRIOR_HANDOFF = '76b6f6c6f14f1d676f370be72b61cb2f0a069633'
PRIOR_REPORT = '4706be652a4d9e70656d1e2db1cbc0be9a9194c6'
R1_PREFIX = 'review/remediation/20261003-prepare/batches/B03/review-round-1/'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def stable(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()

def audit(project, reference):
    checks = []
    def require(condition, name):
        checks.append({'check': name, 'pass': bool(condition)})
        if not condition:
            raise AssertionError(name)
    def git(*args, repo=project):
        return subprocess.check_output(['git', '-C', str(repo), *args])
    def contents(rev, path):
        return git('show', rev + ':' + path)
    def obj(rev, path):
        return json.loads(contents(rev, path))
    def identity(rev, path, repo=project):
        data = git('show', rev + ':' + path, repo=repo)
        return {'commit': rev, 'path': path,
                'git_blob': git('rev-parse', rev + ':' + path, repo=repo).decode().strip(),
                'sha256': sha(data), 'bytes': len(data)}
    def names(left, right):
        return git('diff', '--name-only', left, right).decode().splitlines()
    def text_rows(data, pattern):
        pairs = [(m[1], line) for line in data.decode().splitlines()
                 if (m := re.match(pattern, line))]
        require(len(pairs) == len(dict(pairs)), 'unique document row IDs')
        return dict(pairs)

    scope = obj(HANDOFF, AUTHOR + 'scope.json')
    amendment = obj(HANDOFF, AUTHOR_V2 + 'scope-amendment.json')
    formal = amendment['authorized_formal_paths']
    require(len(formal) == len(set(formal)) == 13, '13 authorized formal paths')
    require(amendment['inherited_formal_write_paths'] == scope['write_paths'], 'original seven-file lock')
    candidate_paths = names(BASE, CANDIDATE)
    handoff_paths = names(CANDIDATE, HANDOFF)
    require(len(candidate_paths) == 53, 'complete baseline-to-candidate 53-path diff')
    require(set(formal) <= set(candidate_paths), 'all 13 formal paths included in full diff')
    require(all(p in formal or p.startswith((AUTHOR, AUTHOR_V2, AUTHOR_V3)) for p in candidate_paths), 'candidate scope whitelist')
    require(set(handoff_paths) == {AUTHOR_V3 + p for p in ['README.md', 'candidate-freeze.json', 'candidate-full.diff']}, 'handoff only three evidence additions')
    git('diff', '--check', BASE, HANDOFF)
    payload = []
    for path in formal:
        before, candidate, handoff = [identity(rev, path) for rev in [BASE, CANDIDATE, HANDOFF]]
        require(candidate['git_blob'] == handoff['git_blob'] and candidate['sha256'] == handoff['sha256'], 'formal candidate/handoff byte equality ' + path)
        require((project / path).read_bytes() == contents(HANDOFF, path), 'formal working file equals frozen handoff ' + path)
        payload.append({'path': path, 'base': before, 'candidate': candidate, 'handoff': handoff})
    full_diff = git('diff', '--binary', '--full-index', '--no-ext-diff', '--no-renames', '--unified=0', BASE, CANDIDATE, '--')
    require(full_diff == contents(HANDOFF, AUTHOR_V3 + 'candidate-full.diff'), 'author full diff exact complete frozen Git diff')
    handoff_diff = git('diff', '--unified=0', '--full-index', CANDIDATE, HANDOFF)
    old_author_paths = git('ls-tree', '-r', '--name-only', APPEND_PARENT, '--', AUTHOR).decode().splitlines()
    require(len(old_author_paths) == 16, '16 inherited author evidence files')
    for path in old_author_paths:
        require(contents(APPEND_PARENT, path) == contents(HANDOFF, path), 'old author byte preservation ' + path)

    manifest = obj(HANDOFF, AUTHOR + 'input-manifest.json')
    extra = obj(HANDOFF, AUTHOR_V2 + 'append-input-manifest.json')
    groups = {'frozen_stage': manifest['read_identities'],
              'supplementary_original_review': manifest['supplementary_read_identities'],
              'append_parent': extra['additional_read_identities']}
    verified_inputs = []
    for group, items in groups.items():
        for item in items:
            got = identity(item['commit'], item['path'])
            require(all(got[k] == item[k] for k in ['commit', 'git_blob', 'sha256', 'bytes']), group + ' identity ' + item['path'])
            if item.get('in_fix_base') and item['path'] not in formal:
                require(contents(HANDOFF, item['path']) == contents(item['commit'], item['path']), 'frozen read-only dependency unchanged ' + item['path'])
            verified_inputs.append({'group': group, **got})
    require([len(groups[g]) for g in groups] == [57, 1, 22], '57 + 1 + 22 frozen identity records')
    locks = obj(PLAN, 'review/remediation-20261003-prepare/stage-locks.json')
    author_lock = next(x for x in locks if x['stage'] == 'B03-A')
    require(author_lock['reads'] == scope['read_paths'] and author_lock['writes'] == scope['write_paths'], 'approved B03 stage lock exact')
    handshake = obj(BASE, 'review/remediation/20261003-prepare/batches/B02/acceptance-stage-1/downstream-handshake.json')
    require(handshake['B03_primary_finding_ids'] == scope['primary_finding_ids'] and handshake['B03_contribution_finding_ids'] == scope['contribution_finding_ids'], 'B02 handoff exact 19/27 scope')
    identity_keys = ['commit', 'path', 'git_blob', 'sha256', 'bytes']
    normalized = [{k: x[k] for k in identity_keys} for x in manifest['read_identities']]
    require(handshake['B03_frozen_read_identities'] == normalized, 'B02 handshake frozen identity set (author verification annotations excluded)')
    require(handshake['canonical_required_open'] == 229 and handshake['canonical_closed'] == 0, 'B02 no canonical closure')

    original_path = 'review/global-independent-review/2026-10-03-fd82a639/findings.json'
    original = {x['id']: x for x in obj(GLOBAL_REVIEW, original_path)}
    acceptance_path = 'review/remediation-20261003-prepare/finding-acceptance.json'
    accepted = obj(PLAN, acceptance_path)
    effective = obj(HANDOFF, AUTHOR + 'effective-finding-inputs.json')
    require(len(effective) == 27 and {x['id'] for x in effective} == set(scope['contribution_finding_ids']), '27 complete original effective objects')
    bindings = []
    for item in effective:
        fid = item['id']
        require(item['complete_original_object'] == original[fid], 'entire canonical object including all adjudications/extensions ' + fid)
        require(item['acceptance'] == accepted[fid], 'entire approved acceptance object ' + fid)
        require(item['original_object_sha256'] == sha(stable(original[fid])), 'canonical original-object SHA256 ' + fid)
        bindings.append({'id': fid, 'original_object_sha256': sha(stable(original[fid])),
                         'acceptance_object_sha256': sha(stable(accepted[fid])),
                         'original_priority': original[fid]['priority'],
                         'original_status': original[fid]['status'],
                         'current_qualifications': original[fid]['current_qualifications'],
                         'adjudication_precedence': original[fid]['adjudication_precedence'],
                         'effective_case_constraints': original[fid].get('effective_case_constraints'),
                         'root_adjudication_count': len(original[fid].get('root_adjudications', [])),
                         'extension_count': len(original[fid].get('extensions', [])),
                         'acceptance_gate': accepted[fid]['acceptance_gate']})
    for ver in [AUTHOR, AUTHOR_V2, AUTHOR_V3]:
        responses = obj(HANDOFF, ver + 'finding-responses.json')
        proposals = obj(HANDOFF, ver + 'registry-proposals.json')['requests']
        require({x['id'] for x in responses} == {x['id'] for x in proposals} == set(scope['contribution_finding_ids']), 'all per-ID response/proposal coverage ' + ver)
        require(sum(x['primary_in_B03'] for x in responses) == 19 and all(not x['canonical_edited'] for x in proposals), '19 primary and no closure mutation ' + ver)
        for response in responses:
            fid = response['id']
            require(response['original_object_sha256'] == sha(stable(original[fid])) and response['current_qualifications'] == original[fid]['current_qualifications'], 'response full-input binding ' + ver + fid)

    historical_root = obj(GLOBAL_REVIEW, 'review/global-independent-review/2026-10-03-fd82a639/agents/C/X-C-ROOT-COVERAGE/independent-judgment.json')['scenarios']
    routed = obj(HANDOFF, AUTHOR + 'root002-scenario-routing.json')
    require(len(routed) == len(historical_root) == 34, '34 root002 scenarios retained')
    historical_by_id = {x['id']: x for x in historical_root}
    require(all(x['frozen_input'] == historical_by_id[x['id']]['input'] and x['frozen_expected'] == historical_by_id[x['id']]['expected'] and x['root_closed'] is False for x in routed), 'root002 all exact frozen scenarios and no root closure')

    cat_path = scope['write_paths'][-1]
    old_cat, new_cat = contents(BASE, cat_path), contents(CANDIDATE, cat_path)
    tail = new_cat.split(b'## H.', 1)[1]
    require(old_cat.split(b'## H.', 1)[1] == tail, 'WP15/59/60 shared catalogue tail exact bytes')
    pattern = r'^\| ((?:MP|MV|EV|FW|IM|MR|DG)\d+) \|'
    old_rows, new_rows = [text_rows(c, pattern) for c in [old_cat, new_cat]]
    require(set(old_rows) <= set(new_rows), 'all 139 accepted B03 row IDs preserved')
    counts = dict(collections.Counter(re.sub(r'\d+$', '', x) for x in new_rows))
    require(counts == {'MP': 27, 'MV': 77, 'EV': 39, 'FW': 7, 'IM': 41, 'MR': 17, 'DG': 43}, '251 unexecuted catalogue vectors')
    for family, count in counts.items():
        require({x for x in new_rows if x.startswith(family)} == {family + str(n).zfill(2) for n in range(1, count + 1)}, 'contiguous vector IDs ' + family)
    permitted_old = {'MP05','MV03','MV11','MV13','EV27','EV28','EV29','IM01','MR08','DG01','DG02','DG07','DG08','DG11','DG12','DG23'}
    require(all(new_rows[x] == old_rows[x] for x in old_rows if x not in permitted_old), 'all unassigned accepted static rows unchanged')
    originals = amendment['additional_formal_write_paths']
    preserved = []
    original11_before, original11_after = [contents(rev, originals[0]).decode() for rev in [BASE, CANDIDATE]]
    original_weather_row = next(x for x in original11_before.splitlines() if x.startswith('| 边缘跨图（'))
    require(original_weather_row in original11_after.splitlines() and '天气持续重置 20' in original_weather_row, 'correct original WP11 weather20 row exact')
    original12_before, original12_after = [contents(rev, originals[1]).decode() for rev in [BASE, CANDIDATE]]
    bike_predicate = '**骑行按目的地图许可决定**——无目的地或目的地 `pbCanUseBike?` 为假时清 bicycle。'
    require(bike_predicate in original12_before and bike_predicate in original12_after, 'correct original bike cancellation predicate preserved')
    for literal in ['`sight(N)`/`trainer(N)`', '`counter(N)`', '`s:`']:
        require(all(literal in contents(rev, originals[3]).decode() for rev in [BASE, CANDIDATE]), 'correct original ASCII literal preserved ' + literal)
    for literal in ['move_random_range', 'move_random_UD', 'move_random_LR']:
        require(all(literal in contents(rev, originals[4]).decode() for rev in [BASE, CANDIDATE]), 'correct original route prefix preserved ' + literal)
    for path in originals:
        before, after = [contents(rev, path).decode() for rev in [BASE, CANDIDATE]]
        marker = '## 4. 证据与来源（traceability）' if path.endswith('move-route-matrix.md') else '## 10. 证据与来源（traceability）'
        if marker in before:
            require(before[before.index(marker):] == after[after.index(marker):], 'original historical evidence/unknown/status tail ' + path)
            preserved.append({'path': path, 'marker': marker, 'sha256': sha(before[before.index(marker):].encode())})
    for path in [scope['write_paths'][5], originals[-1]]:
        paragraph = next(x for x in contents(BASE, path).decode().splitlines() if x.startswith('- **大网格奇数参数调整'))
        require(paragraph in contents(CANDIDATE, path).decode().splitlines(), 'B01 original/final first-write failure byte protection ' + path)
        preserved.append({'path': path, 'marker': 'B01 first odd-write failure paragraph', 'sha256': sha(paragraph.encode())})
    for x in ['DG18','DG19','DG20','DG21','DG22']:
        require(new_rows[x] == old_rows[x], 'B01 static catalogue row preserved ' + x)
    categories = collections.Counter()
    matrix_rows = text_rows(contents(CANDIDATE, scope['write_paths'][2]), r'^\| (\d+) \|')
    for row in matrix_rows.values():
        categories[row.split('|')[7].strip().strip('*')] += 1
    require(dict(categories) == {'有实现':66, '标记':2, '空操作':28}, '96 commands classified 66/2/28')
    dummy_ids = {int(code) for code, row in matrix_rows.items() if row.split('|')[7].strip().strip('*') == '空操作'}
    require(dummy_ids == {126,127,128,129,133,301,302,311,312,313,315,316,317,318,319,320,321,322,*range(331,341)}, 'exact 28 dummy identities and 314 excluded')
    for original_path in [originals[2], originals[3]]:
        original_rows = text_rows(contents(BASE, original_path), r'^\| (\d+) \|')
        candidate_rows = text_rows(contents(CANDIDATE, original_path), r'^\| (\d+) \|')
        if '314' in original_rows:
            require(candidate_rows['314'] == original_rows['314'], 'original 314 implementation row byte protection ' + original_path)
    for path in [scope['write_paths'][4], originals[4]]:
        require(set(text_rows(contents(CANDIDATE, path), r'^\| (\d+) \|')) == {str(x) for x in range(46)}, '46 route codes preserved ' + path)
    require(contents(BASE, originals[2]).decode().split('## 3. 统计与口径', 1)[1] == contents(CANDIDATE, originals[2]).decode().split('## 3. 统计与口径', 1)[1], 'original 314/28 classification and history exact')

    require(reference != project and project not in reference.parents, 'reference Git outside main repository')
    require(git('rev-parse', 'HEAD', repo=reference).decode().strip() == REFERENCE, 'reference fixed SHA')
    require(git('rev-parse', 'HEAD^{tree}', repo=reference).decode().strip() == REF_TREE, 'reference fixed tree')
    require(not git('status', '--porcelain', repo=reference).strip(), 'reference clean')
    for ver in [AUTHOR, AUTHOR_V2, AUTHOR_V3]:
        for row in obj(HANDOFF, ver + 'source-reading-log.json'):
            got = identity(REFERENCE, row['path'], repo=reference)
            require(all(got[k] == row[k] for k in ['git_blob','sha256','bytes']), 'author literal source identity ' + row['path'])
    require(git('rev-parse', CANDIDATE + '^').decode().strip() == PRIOR_HANDOFF, 'new candidate exact append parent')
    require(git('rev-parse', HANDOFF + '^').decode().strip() == CANDIDATE, 'new handoff exact candidate parent')
    require(git('merge-base', BASE, CANDIDATE).decode().strip() == BASE, 'accepted baseline ancestry')
    latest_scope = obj(HANDOFF, AUTHOR_V3 + 'scope-and-review-inputs.json')
    require(latest_scope['authorized_formal_paths'] == formal and latest_scope['public_registry_writer'] == 'A-REG only; proposals are not mutations', 'new scope13 and publicwriter freeze')
    require(not latest_scope['integration_authorized'] and not latest_scope['B06_dependency_approved'] and not latest_scope['canonical_closed'], 'no author integration/B06/closure authorization')
    latest_manifest = obj(HANDOFF, AUTHOR_V3 + 'input-manifest.json')
    latest_groups = {k: latest_manifest[k] for k in ['formal_input_identities', 'previous_author_files', 'review_input_identities']}
    require([len(x) for x in latest_groups.values()] == [13,28,12], 'new13formal+28oldauthor+12firstreport identity records')
    for group, items in latest_groups.items():
        for item in items:
            got = identity(item['commit'], item['path'])
            require(all(got[k] == item[k] for k in ['commit','git_blob','sha256','bytes']), 'v3 identity '+group+' '+item['path'])
            if group == 'previous_author_files':
                require(contents(HANDOFF,item['path']) == contents(PRIOR_HANDOFF,item['path']), 'priorauthor exact frozen byte '+item['path'])
            verified_inputs.append({'group': 'v3_'+group, **got})
    first_report_paths = git('ls-tree','-r','--name-only',PRIOR_REPORT,'--',R1_PREFIX).decode().splitlines()
    require(set(first_report_paths) == {x['path'] for x in latest_groups['review_input_identities']}, 'entire immutable first report12 identities')
    prior_cat = contents(PRIOR_CANDIDATE,cat_path)
    def byte_rows(data):
        return {m[1].decode(): line for line in data.splitlines(keepends=True) if (m := re.match(rb'^\| ((?:MP|MV|EV|FW|IM|MR|DG)\d+) \|',line))}
    prior_byte_rows, new_byte_rows = byte_rows(prior_cat), byte_rows(new_cat)
    require(len(prior_byte_rows) == 235, 'old235static exact identity')
    for rid,line in prior_byte_rows.items():
        require(new_byte_rows[rid] == line, 'all prior235 literal row bytes '+rid)
    require(set(new_byte_rows)-set(prior_byte_rows) == {f'MV{i}' for i in range(68,78)} | {f'IM{i}' for i in range(36,42)}, 'exact16added IDs')
    ledger = obj(HANDOFF,AUTHOR_V3+'formal-edit-ledger.json')
    formal_changes = set(names(PRIOR_HANDOFF,CANDIDATE)) & set(formal)
    require(formal_changes == set(ledger['formal_increment_paths']) and len(formal_changes)==9, 'nineformal modified exact list')
    require(len(ledger['edits']) == 17, '17bounded text edits')
    for path in formal:
        expected = contents(PRIOR_HANDOFF,path).decode()
        for edit in [x for x in ledger['edits'] if x['path']==path]:
            require(expected.count(edit['old'])==1, 'exact unique ledger input '+path+edit['clause'])
            require(set(edit['review_issues']) <= {'R-B03-001','R-B03-002','R-B03-003'}, 'ledger assignedissue only')
            expected=expected.replace(edit['old'],edit['new'],1)
        require(contents(CANDIDATE,path).decode()==expected, 'all bytes outside17edits protected '+path)
    for path in [scope['write_paths'][2], originals[2],scope['write_paths'][4], originals[4]]:
        require(text_rows(contents(PRIOR_CANDIDATE,path),r'^\| (\d+) \|') == text_rows(contents(CANDIDATE,path),r'^\| (\d+) \|'), 'all numeric command/route rows exact priorcandidate '+path)
    prior_disposition=obj(PRIOR_REPORT,R1_PREFIX+'finding-dispositions.json')
    prior_by={x['id']:x for x in prior_disposition['dispositions']}
    for response in obj(HANDOFF,AUTHOR_V3+'finding-responses.json'):
        fid=response['id']
        require(response['complete_round_1_scoped_disposition']==prior_by[fid], 'firstreport entire prior disposition preserved '+fid)
        require(response['canonical_status_unchanged']==original[fid]['status'] and response['original_priority']==original[fid]['priority'], 'canonical status/priority preserved '+fid)
        require(response['root_adjudications']==original[fid].get('root_adjudications',[]), 'all adjudications retained '+fid)
        require(all(response[k] == 0 for k in ['runtime_observations','proven_demo_chains','static_vectors_executed']), 'response noexecutionclaim '+fid)
    review_responses=obj(HANDOFF,AUTHOR_V3+'review-responses.json')
    require({x['id'] for x in review_responses} == {'R-B03-001','R-B03-002','R-B03-003'}, 'all three firstround observations responded')
    for response in review_responses:
        old=next(x for x in prior_disposition['new_findings'] if x['id']==response['id'])
        require(response['complete_first_round_finding']==old and response['priority_preserved']=='P2', 'complete firstround counterexample andP2 '+response['id'])
        require(set(response['static_vector_ids']) <= set(new_byte_rows)-set(prior_byte_rows), 'newissue newvectorIDs '+response['id'])
        require(not response['canonical_edited'] and not response['canonical_closed'] and not response['reference_or_solver_execution'], 'response no closure/execution '+response['id'])
    latest_proposals=obj(HANDOFF,AUTHOR_V3+'registry-proposals.json')
    require({x['id'] for x in latest_proposals['new_distinct_root_proposals']}=={'R-B03-001','R-B03-002'}, 'two newroot proposals retain identity')
    require(latest_proposals['combination_aliases']==[{'observation':'R-B03-003','canonical_root':'GIR-FD82-C053','new_root_count_delta':0}], 'C053combination no duplicate root')
    require(latest_proposals['original_aggregate_229_unchanged'] and latest_proposals['canonical_mutations']==0, 'global229 and no publicclosure')
    freeze=obj(HANDOFF,AUTHOR_V3+'candidate-freeze.json')
    require(freeze['candidate_payload_commit']==CANDIDATE and freeze['candidate_payload_tree']==git('rev-parse',CANDIDATE+'^{tree}').decode().strip(), 'freeze candidate SHA/tree')
    require(freeze['full_diff']['sha256']==sha(full_diff) and freeze['full_diff']['bytes']==len(full_diff), 'fullfreeze complete diff sha/bytes')
    for row in freeze['candidate_changed_paths']:
        got=identity(CANDIDATE,row['path'])
        require(all(got[k]==row[k] for k in ['git_blob','sha256','bytes']), 'all53candidate frozenidentity '+row['path'])
    require({x['path'] for x in freeze['candidate_changed_paths']}==set(candidate_paths), 'freeze complete53path topology')
    require(all(not freeze[k] for k in ['integration_authorized','B06_dependency_approved','canonical_closed']), 'freeze no integration/B06/closed')
    relative_links,tables=0,0
    for path in formal:
        txt=contents(CANDIDATE,path).decode()
        for target in re.findall(r'\[[^\]]+\]\(([^)]+\.md)(?:#[^)]*)?\)',txt):
            if not re.match(r'[a-z]+:',target):
                require((project/path).parent.joinpath(target).resolve().is_file(), 'relative link exists '+path+' '+target)
                relative_links+=1
        for block in re.findall(r'(?:^\|[^\n]*\n)+',txt,re.M):
            lines=block.splitlines()
            require(len(lines)>1 and re.match(r'^\|(?:\s*:?-+:?\s*\|)+$',lines[1]) is not None, 'markdown table header '+path)
            tables+=1
    evidence_paths = [p for p in names(BASE, HANDOFF) if p not in formal]
    result = {'audit_type': 'independent frozen Git/document identity audit; no behavioral execution',
              'result': 'PASS_IDENTITY_AND_PROTECTED_BYTES', 'semantic_verdict': 'PASS_SCOPED',
              'checks': checks, 'formal_paths': 13, 'baseline_candidate_paths': 53,
              'candidate_handoff_evidence_additions': 3, 'input_record_counts': {k: len(v) for k,v in groups.items()},
              'second_round_input_record_counts': {k:len(v) for k,v in latest_groups.items()},
              'semantic_verdict_source': 'Independent manual case review; not derived from identity audit',
              'complete_original_and_acceptance_objects': 27, 'primary_ids': 19,
              'prior235_rows_exact_bytes': True, 'new_static_rows_since_prior': 16,
              'previous_author_files_preserved': 28, 'prior_report_files_verified': 12,
              'formal_increment_paths': 9, 'bounded_edits': 17, 'relative_links': relative_links, 'tables': tables,
              'B06_dependency_integration_accepted': False,
              'catalogue_vectors': counts, 'catalogue_total': len(new_rows), 'baseline_catalogue_total': len(old_rows),
              'added_catalogue_vectors': len(new_rows) - len(old_rows), 'catalogue_vectors_executed': 0,
              'tail_sha256': sha(tail), 'runtime_observations': 0, 'proven_demo_chains': 0,
              'reference_execution': 0, 'actual_integration_checked': False}
    identities = {'run_id': '20261003-prepare', 'base': BASE, 'candidate_payload': CANDIDATE,
                  'candidate_tree': git('rev-parse', CANDIDATE + '^{tree}').decode().strip(),
                  'handoff_head': HANDOFF, 'handoff_tree': git('rev-parse', HANDOFF + '^{tree}').decode().strip(),
                  'original_global_review': GLOBAL_REVIEW, 'approved_plan': PLAN,
                  'reference': REFERENCE, 'reference_tree': REF_TREE,
                  'prior_complete_candidate': PRIOR_CANDIDATE, 'prior_handoff': PRIOR_HANDOFF, 'prior_report': PRIOR_REPORT,
                  'baseline_to_candidate_diff': {'format': 'git diff --binary --full-index --no-ext-diff --no-renames --unified=0', 'bytes': len(full_diff), 'sha256': sha(full_diff)},
                  'candidate_to_handoff_diff': {'bytes': len(handoff_diff), 'sha256': sha(handoff_diff)},
                  'formal_payload': payload, 'frozen_inputs': verified_inputs,
                  'all_changed_candidate_paths': [identity(CANDIDATE,p) for p in candidate_paths],
                  'all_handoff_evidence_paths': [identity(HANDOFF,p) for p in evidence_paths],
                  'original_findings_file': identity(GLOBAL_REVIEW, 'review/global-independent-review/2026-10-03-fd82a639/findings.json'),
                  'approved_acceptance_file': identity(PLAN, acceptance_path), 'protected_bytes': preserved}
    return result, identities, bindings

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--project', default='/workspace/pokemon-essentials-clean-room')
    parser.add_argument('--reference', default='/workspace/reference-b03')
    args = parser.parse_args()
    results = audit(Path(args.project).resolve(), Path(args.reference).resolve())
    directory = Path(__file__).resolve().parent
    for name, result in zip(['independent-validation.json', 'input-identity-manifest.json', 'original-finding-bindings.json'], results):
        (directory / name).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k:v for k,v in results[0].items() if k != 'checks'}, ensure_ascii=False, indent=2))
