#!/usr/bin/env python3
"""Only this review's JSON/text/hash/Git bookkeeping; no behavior vectors."""
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p/'.git').exists())
REPORT = pathlib.Path(__file__).resolve().parent
CANDIDATE = '47f7514765f8569ae9172bb06a2cd615e2b83b8a'
PREDECESSOR = '1e6b11a47370f1c7c4659a32443fc1afda597bac'
BRANCH = 'remediation/20261003-prepare/review-B14-affected-B03-1'
REFERENCE = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
checks = []
def check(name, value):
    checks.append({'check': name, 'pass': bool(value)})
    if not value:
        raise AssertionError(name)
def read(name):
    return json.loads((REPORT/name).read_text())
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()

check('exact candidate before report commit', git('rev-parse', 'HEAD') == CANDIDATE)
check('exact independent review branch', git('branch', '--show-current') == BRANCH)
manifest = read('input-identity-manifest.json')
first = read('independent-first-judgment.json')
final = read('independent-final-judgment.json')
findings = read('findings.json')
dispositions = read('affected-dispositions.json')
receipt = read('execution-request-receipt.json')
validation = read('independent-validation.json')
controls = read('qualified-control-bindings.json')
check('complete unfiltered 30-path fixed delta', manifest['full_unfiltered_diff']['path_count'] == 30 and manifest['full_unfiltered_diff']['sha256'] == '2dbbb69a545b3ab0e02b897b590297d774fa89727d98feb8cfdc2dacdd41d834')
check('candidate and predecessor identities', manifest['reviewed_candidate'] == CANDIDATE and manifest['accepted_predecessor'] == PREDECESSOR)
check('immutable first judgment byte hash', sha(REPORT/'independent-first-judgment.json') == manifest['first_judgment_sha256'] == final['first_judgment_sha256'] == dispositions['first_judgment']['sha256'])
check('preliminary and final verdict history preserved', first['verdict'] == 'PASS_SCOPED' and final['verdict'] == findings['verdict'] == dispositions['candidate_verdict'] == 'REQUEST_CHANGES')
check('single new P2 observation', len(findings['new_findings']) == 1 and findings['new_findings'][0]['id'] == 'B14-AFFECTED-B03-001' and findings['new_findings'][0]['severity'] == 'P2')
check('final single issue reference', final['new_blocking_findings'] == ['B14-AFFECTED-B03-001'])
expected = ['GIR-FD82-002','GIR-FD82-C003','GIR-FD82-C007','GIR-FD82-C094','GIR-FD82-C095','WP80-INTAKE-R01']
check('all six original affected control IDs', [x['id'] for x in dispositions['original_control_dispositions']] == expected)
for item in dispositions['original_control_dispositions']:
    control = next(x for x in controls if x['id'] == item['id'])
    binding = item['complete_qualified_control_binding']
    check('whole qualified object binding '+item['id'], binding['whole_original_object_sha256'] == control['original_object_sha256'] and binding['whole_acceptance_object_sha256'] == control['acceptance_object_sha256'])
    check('scoped original ID has evidence/remaining/acceptance '+item['id'], all(item.get(x) for x in ['reason','evidence','remaining','severity','acceptance']) and item['canonical_state'] == 'OPEN')
issue = findings['new_findings'][0]
check('static direct optional callback case and reverse contrast retained', issue['minimum_counterexample']['kind'] == 'DIRECT_HELPER_OPTIONAL_CALLBACK_STATIC_CASE_NOT_EXECUTED' and bool(issue['paired_reverse_contrast']) and len(issue['determinate_acceptance']) == 3)
for item in issue['project_evidence'] + issue['reference_evidence']:
    cwd = pathlib.Path('/workspace/reference-b03') if item['repository'] == 'reference' else ROOT
    commit = REFERENCE if item['repository'] == 'reference' else CANDIDATE
    raw = subprocess.check_output(['git','show',commit+':'+item['path']],cwd=cwd)
    check('new observation exact evidence '+item['repository']+':'+item['path'], item['commit'] == commit and item['sha256'] == hashlib.sha256(raw).hexdigest() and item['bytes'] == len(raw) and bool(item['lines']))
check('685 metadata checks distinct from semantics', validation['check_count'] == 685 and validation['result'] == 'PASS_FIXED_GIT_AND_DOCUMENT_INVENTORY_ONLY' and validation['semantic_review_verdict_separate'])
check('raw patch-only whitespace warnings disclosed', validation['raw_diffcheck']['returncode'] == 2 and validation['raw_diffcheck']['warnings'] == 57)
check('accepted 251 B03 rows retained', read('catalog-preservation.json')['B03_rows_preserved'] == 251)
check('no reference/behavior/historical-verifier execution', receipt['reference_game_ruby_compiler_converter_generator_deserializer_solver_emulator_execution'] == receipt['static_behavior_vectors_executed'] == receipt['historical_reference_author_reviewer_verifiers_executed'] == 0)
check('requested settings accurately unverified', receipt['requested_model'] == 'gpt-6.1-sol' and receipt['requested_reasoning'] == 'Ultra' and receipt['requested_speed'] == 'Standard(default)' and receipt['effective_model_reasoning_speed'] == 'UNVERIFIED')
check('no probes/children', receipt['configuration_probes'] == receipt['quota_probes'] == receipt['quota_checks'] == receipt['child_tasks'] == 0)
check('actual gate not prepaid', final['actual_integration_checked'] is False and dispositions['actual_integration_checked'] is False)
check('canonical state remains 229 OPEN / 0 CLOSED', all(x['canonical_open'] == 229 and x['canonical_closed'] == 0 for x in [findings,dispositions,final,receipt]))
for path in REPORT.glob('*.json'):
    read(path.name)
check('all review JSON parses', True)
for path in REPORT.glob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
        if not target.startswith(('https://','http://')):
            check('relative document link '+path.name+':'+target, (path.parent/target.split('#',1)[0]).is_file())
        else:
            check('external evidence has fixed source/candidate commit', '/blob/'+CANDIDATE+'/' in target or '/blob/'+REFERENCE+'/' in target)
check('report explicitly retains new P2 and prior verdict history', all(x in (REPORT/'report.md').read_text() for x in ['B14-AFFECTED-B03-001','REQUEST_CHANGES','独立首判','未执行','57 条警告']))
files = [{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(REPORT.iterdir()) if p.is_file() and p.name != 'review-document-validation.json']
result = {'result':'PASS_REVIEW_DOCUMENT_IDENTITY_AND_CONSISTENCY_ONLY','semantic_verdict':'REQUEST_CHANGES','reviewed_candidate':CANDIDATE,'check_count':len(checks),'checks':checks,'review_document_inventory_excluding_this_result':files,'runtime_or_behavior_checks':0,'actual_integration_checked':False,'self_result_hash_included':False}
(REPORT/'review-document-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':result['result'],'checks':len(checks),'bound_documents':len(files),'semantic_verdict':result['semantic_verdict']}))
