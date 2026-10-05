"""Independent B08 Git/JSON/text checks only. No reference behavior is executed."""
import hashlib, json, pathlib, re, subprocess, collections

REPO = pathlib.Path('/workspace/r-b08-review')
REF_REPO = pathlib.Path('/workspace/r-b08-reference')
BASE = '759eee80ce7856570fde2de12d5dcf98ce7e6017'
CAND = '0f35a393d9de467cd5f7e695b6072687bb582186'
WIP = 'd6367692610c83fd24bd1ab8d2ab0cfa6757314d'
GLOBAL = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
ROOT = 'review/remediation/20261003-prepare/batches/B08/'
results, failures, cache = {}, [], {}

def git(*args, ref=False):
    return subprocess.check_output(['git', '-C', str(REF_REPO if ref else REPO), *args])

def contents(commit, path):
    key = (commit, path)
    if key not in cache:
        cache[key] = git('show', commit + ':' + path, ref=commit == REF)
    return cache[key]

def obj(commit, path):
    return json.loads(contents(commit, path))

def check(name, okay, detail=None):
    results[name] = {'pass': bool(okay), 'detail': detail}
    if not okay:
        failures.append(name)

def identity(commit, path):
    data = contents(commit, path)
    return {'git_blob': git('rev-parse', commit + ':' + path, ref=commit == REF).decode().strip(),
            'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

changed = git('diff', '--name-only', BASE, CAND).decode().splitlines()
formal = [p for p in changed if p.startswith('deliverables/')]
original = [p for p in changed if p.startswith('specs/')]
evidence = [p for p in changed if p.startswith(ROOT)]
check('complete_changed_scope', len(changed) == 57 and len(formal) == 8 and len(original) == 4
      and len(evidence) == 45 and len(formal + original + evidence) == len(changed), changed)
check('no_historical_or_public_mutation', not any(p.startswith(('audit/', 'review/remediation-20261003-prepare/')) for p in changed))
stage1 = git('ls-tree', '-r', '--name-only', CAND, ROOT + 'author-stage-1/').decode().splitlines()
check('all25_stage1_files_frozen_at_WIP', len(stage1) == 25 and all(contents(WIP,p) == contents(CAND,p) for p in stage1), len(stage1))
new_in_base = []
for p in evidence:
    test = subprocess.run(['git','-C',str(REPO),'cat-file','-e',BASE+':'+p],capture_output=True)
    if test.returncode == 0:
        new_in_base.append(p)
check('all45_evidence_files_new_since_baseline', not new_in_base, new_in_base)
check('no_WP34_original_or_final_body_change', all(contents(BASE,p) == contents(CAND,p) for p in [
    'specs/pokemon-rules/wp34-inheritance-and-offspring.md',
    'deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md']))

docs = {}
for p in evidence:
    if p.endswith('.json'):
        docs[p] = obj(CAND,p)
check('all_new_JSON_parse', True, len(docs))
controls = docs[ROOT+'author-stage-1/fixed-contribution-controls.json']
global_objects = {x['id']: x for x in obj(GLOBAL,'review/global-independent-review/2026-10-03-fd82a639/findings.json')}
accepted = obj(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
check('full17_original_control_objects_equal_fixed_global', len(controls)==17 and all(x['complete_original_object']==global_objects[x['id']] for x in controls))
check('full17_acceptance_objects_equal_approved_plan', all(x['complete_approved_acceptance']==accepted[x['id']] for x in controls))
check('exact_primary9', sum(x['B08_primary'] for x in controls)==9, [x['id'] for x in controls if x['B08_primary']])

identities, bad, unresolved = 0, [], []
def walk(value, where, default_commit=CAND, stage_commit=CAND):
    global identities
    if isinstance(value, dict):
        if where.endswith('/baseline'):
            default_commit = BASE
        commit = value.get('commit', default_commit)
        if not isinstance(commit,str) or not re.fullmatch('[0-9a-f]{40}',commit):
            commit = stage_commit
        if all(k in value for k in ['path','git_blob','sha256','bytes']):
            try:
                actual = identity(commit, value['path'])
                identities += 1
                if any(value[k] != actual[k] for k in actual):
                    bad.append({'where': where, 'commit': commit, 'path': value['path'], 'actual': actual})
            except subprocess.CalledProcessError:
                unresolved.append({'where': where, 'commit': commit, 'path': value['path']})
        for k,v in value.items():
            walk(v,where+'/'+k,commit,stage_commit)
    elif isinstance(value,list):
        for i,v in enumerate(value):
            walk(v,where+'/'+str(i),default_commit,stage_commit)
for p,o in docs.items():
    walk(o,p,WIP if '/author-stage-1/' in p else CAND,WIP if '/author-stage-1/' in p else CAND)
check('all_author_git_SHA256_byte_identities', not bad and not unresolved, {'checked': identities, 'mismatches': bad, 'unresolved': unresolved})

manifest = docs[ROOT+'author-stage-2/candidate-content-manifest.json']['all_other_changed_file_identities']
check('candidate_manifest_covers_all_other56_changes', set(x['path'] for x in manifest)==set(changed)-{ROOT+'author-stage-2/candidate-content-manifest.json'} and len(manifest)==56)
patch = contents(CAND,ROOT+'author-stage-1/original-sync-prepared-v2.patch')
check('authorized_original_patch_SHA256', hashlib.sha256(patch).hexdigest()=='05b75bcafcb1fd9359e9a35e935e8b7cbb7dd038a0f3349a1172d1fe3ba88f25')
original_diff = git('diff','--binary',BASE,CAND,'--',*original)
request=docs[ROOT+'author-stage-1/original-sync-request-v2.json']
expected_after_ok=all(identity(CAND,x['path'])==x['prepared_after'] and identity(BASE,x['path'])==x['before'] for x in request['paths'])
reverse_check=subprocess.run(['git','-C',str(REPO),'apply','--reverse','--check','--'],input=patch,capture_output=True)
check('actual_four_originals_exact_authorized_results',expected_after_ok and reverse_check.returncode==0, {'actual_diff_sha256':hashlib.sha256(original_diff).hexdigest(), 'note':'Prepared patch omits Git diff/index headers; expected before/after bytes and reverse apply-check prove its result scope.', 'reverse_apply_check_exit':reverse_check.returncode})
check('stage2_all_output_diff_exact', contents(CAND,ROOT+'author-stage-2/all-output-predecessor-to-candidate.diff')==git('diff','--binary',BASE,CAND,'--',*formal,*original))
check('stage2_authorized_original_WIP_diff_exact', contents(CAND,ROOT+'author-stage-2/authorized-originals-WIP-to-candidate.diff')==git('diff','--binary',WIP,CAND,'--',*original))
for p in evidence:
    if '/author-stage-2/reverse-' in p:
        filename=pathlib.Path(p).name[len('reverse-'):-len('.diff')]
        target=next(x for x in formal if pathlib.Path(x).name==filename)
        check('reverse_diff_exact_'+filename,contents(CAND,p)==git('diff','--binary',BASE,CAND,'--',target))

catalogs = [p for p in formal if '/test-catalog/' in p]
catalog_checks={}
for p in catalogs:
    old, new = contents(BASE,p).decode(), contents(CAND,p).decode()
    def rows(text):
        return [(line.split('|')[1].strip(),line) for line in text.splitlines()
                if re.match(r'^\|\s*(?:[A-Z]+-?\d+[a-z]?)\s*\|',line)]
    ro, rn=rows(old),rows(new)
    oldids=[x[0] for x in ro]; newids=[x[0] for x in rn]
    added=[i for i in newids if i not in oldids]
    revised=[i for i,row in rn if i in dict(ro) and row!=dict(ro)[i]]
    locked=[]
    # Every unchanged-owner section is compared in full, with separators kept.
    owned={'creature-rpg-wp27-28-29-30-33.md':{'DC'},'creature-rpg-wp35-36-57-64-68.md':{'EG','EN'},
           'pokemon-rules-wp19-21-22-23-34.md':{'BR'},'pokemon-rules-wp31-32-37-38.md':{'RM'}}[pathlib.Path(p).name]
    def sections(t):
        return {re.split('[：:]',s.splitlines()[0])[0].strip():s for s in re.split(r'^## ',t,flags=re.M)[1:]}
    os,ns=sections(old),sections(new)
    for name,s in os.items():
        if name not in owned:
            locked.append({'section':name,'equal':s==ns.get(name)})
    goodcols=all(len(line.split('|'))==5 for i,line in rn if i in added or i in revised)
    check('catalog_preservation_'+pathlib.Path(p).name,
          [i for i in newids if i in oldids]==oldids and len(newids)==len(set(newids)) and goodcols and all(x['equal'] for x in locked))
    catalog_checks[p]={'old_rows':len(ro),'new_rows':len(rn),'added':added,'revised':revised,'other_owner_sections':locked,'changed_rows_three_columns':goodcols}
check('catalog_exact15_new_and5_revised',sum(len(x['added']) for x in catalog_checks.values())==15 and sum(len(x['revised']) for x in catalog_checks.values())==5,catalog_checks)

output_check=subprocess.run(['git','-C',str(REPO),'diff','--check',BASE,CAND,'--',*formal,*original],capture_output=True)
full_check=subprocess.run(['git','-C',str(REPO),'diff','--check',BASE,CAND],capture_output=True)
check('all12_outputs_diff_check',output_check.returncode==0,output_check.stdout.decode())
warnings=full_check.stdout.decode()
pathlines=[x for x in warnings.splitlines() if x.startswith(ROOT)]
allowed_saved_diff=all('.diff:' in x or '.patch:' in x for x in pathlines)
diagnostics=[]
for line in pathlines:
    match=re.match(r'^(.*):(\d+): (.*)$',line)
    path,number,cause=match.groups()
    actual_line=contents(CAND,path).decode().splitlines()[int(number)-1]
    diagnostics.append({'path':path,'line':int(number),'cause':cause,'actual_line':actual_line})
check('unfiltered_whitespace_warnings_only_saved_patch_diff_artifacts',bool(pathlines) and allowed_saved_diff and all(x['actual_line']==' ' for x in diagnostics),
      {'exit':full_check.returncode,'diagnostics':len(pathlines),'trailing_whitespace_diagnostics':sum(x['cause']=='trailing whitespace.' for x in diagnostics),
       'new_blank_line_at_EOF_diagnostics':sum(x['cause']=='new blank line at EOF.' for x in diagnostics),
       'all_offending_lines_exact_single_space_unified_diff_context':True,'paths':sorted(set(x.split(':')[0] for x in pathlines))})
check('reference_exact_clean',git('rev-parse','HEAD',ref=True).decode().strip()==REF and not git('status','--porcelain',ref=True))
check('checkout_skills_absent',not git('ls-tree','-r','--name-only',CAND,'.agents/skills'))

handshake = obj(BASE,'review/remediation/20261003-prepare/batches/B07/acceptance-stage-1/downstream-handshake.json')
check('full17_controls_equal_accepted_B07_downstream_contract', controls == handshake['contribution_controls'])
check('exact8_formal_paths_equal_accepted_B08_allowlist',set(formal)==set(handshake['allowed_formal_write_paths']))
frozen=docs[ROOT+'author-stage-1/input-freeze.json']['inputs']
check('planned79_identity_freeze_matches_accepted_contract',len(frozen)==79 and all(
    all(x.get(k)==y[k] for k in ['path','git_blob','sha256','bytes']) and x['commit'] in (BASE,GLOBAL)
    for x,y in zip(frozen,handshake['planned_reads'])))
canonical=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
check('canonical_full_control_SHA256',all(canonical(x['complete_original_object'])==x['original_complete_object_sha256'] and
      canonical(x['complete_approved_acceptance'])==x['acceptance_object_sha256'] for x in controls))
for stage in ['author-stage-1','author-stage-2']:
    mapped=docs[ROOT+stage+'/finding-contribution-map.json']
    check('exact17_contribution_map_'+stage,[x['id'] for x in mapped]==handshake['contribution_finding_ids'] and
          [x['id'] for x in mapped if x['primary']]==handshake['primary_finding_ids'] and
          all(x['original_complete_object_sha256']==y['original_complete_object_sha256'] and
              x['acceptance_object_sha256']==y['acceptance_object_sha256'] for x,y in zip(mapped,controls)))
    proposals=docs[ROOT+stage+'/A-REG-proposals.json']
    check('local_AREG_proposals_no_closure_'+stage,proposals['canonical_required_open']==229 and proposals['canonical_closed']==0 and
          [x['id'] for x in proposals['contributions']]==handshake['contribution_finding_ids'] and
          all(x['canonical_state']=='OPEN' for x in proposals['contributions']))
check('stage1_full_formal_diff_frozen_exact',contents(CAND,ROOT+'author-stage-1/formal-predecessor-to-candidate.diff')==git('diff','--binary',BASE,WIP,'--',*formal))
for p in evidence:
    if '/author-stage-1/reverse-' in p:
        filename=pathlib.Path(p).name[len('reverse-'):-len('.diff')]
        target=next(x for x in formal if pathlib.Path(x).name==filename)
        check('stage1_reverse_diff_frozen_'+filename,contents(CAND,p)==git('diff','--binary',BASE,WIP,'--',target))
check('WIP_candidate_formal_only_two_table_separator_fixes',all(contents(CAND,p)==contents(WIP,p) for p in formal if p not in [
    'deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md',
    'deliverables/final-specification-set/test-catalog/pokemon-rules-wp31-32-37-38.md']) and all(
    [l for l in contents(CAND,p).splitlines() if l]==[l for l in contents(WIP,p).splitlines() if l]
    for p in formal))
navigation=docs[ROOT+'author-stage-1/project-bounded-reading.json']
check('project_navigation_receipts_valid_bounded_not_full_claim',all(
    all(1<=a<=b<=len(contents(x['commit'],x['path']).splitlines()) for a,b in x.get('line_ranges',[])) and
    all(1<=i<=len(contents(x['commit'],x['path']).splitlines()) for i in x.get('all_match_lines_navigation',x.get('matching_lines_navigation',[]))) and
    ('not whole-file semantic coverage' in x['mode'] or 'remainder not semantic coverage' in x['mode']) for x in navigation),len(navigation))
for item in docs[ROOT+'author-stage-2/document-self-check.json']['catalog_rows']:
    p=item['path']; actual=catalog_checks[p]
    check('author_catalog_claim_rechecked_'+pathlib.Path(p).name,item['preserved_ID_occurrences'] and
          len(item['old_ordered_ids'])==actual['old_rows'] and len(item['candidate_ordered_ids'])==actual['new_rows'] and
          len(item['changed_old_rows'])==len(actual['revised']) and len(item['added_rows'])==len(actual['added']))
check('accepted_C004_default0_and_positive_reverse_vectors_preserved',contents(BASE,'deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md')==contents(CAND,'deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md') and
      contents(BASE,'deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md')==contents(CAND,'deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md') and
      b'KL22' in contents(CAND,'deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md'))

result={'scope':'Independent document/Git bookkeeping only; not behavioral tests','candidate':CAND,'baseline':BASE,'reference':REF,
        'checks':results,'failed_checks':failures,'all_checks_pass':not failures,
        'reference_execution':0,'behavior_vectors_executed':0,'runtime_observations':0,'proven_Demo_chains':0}
pathlib.Path('/tmp/r-b08-review-inputs/document-check-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(results),'failed':failures,'identity_checks':identities,'identity_mismatches':[x['where'] for x in bad],'identity_unresolved':unresolved},ensure_ascii=False,indent=2))
