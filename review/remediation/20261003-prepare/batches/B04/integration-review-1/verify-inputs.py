"""Independent actual-integration Git, hash and document checks. No reference execution.

Run from the main project root; uses only Git object reads and text/JSON/TSV reads.
Never imports, runs, compiles, converts or simulates reference or historical programs.
"""
import collections
import csv
import hashlib
import io
import json
import pathlib
import re
import subprocess

BASE = '6452c0e03025605222f3de9a272221e2b82eeda4'
CAND = '50f9ca2506bf0de21c33c644569c9987f84b80a3'
HANDOFF = '5da06e2baf0879978a871c6952fab1105909b511'
OLD = '99d9c24c43b503763bdbf259db19e5c651e27175'
OLD_HANDOFF = 'da6daba7d6c6365d4578d7173a6d8316acae8bb8'
R1 = 'f0d89a0989cf16d7ea2592fdf75a968b553caefa'
R2 = 'c500ed089fd1192409c1c77a7a91e093c59a8a45'
PAYLOAD = 'caf7b59c2b80a3d4bf6ad54b1ffb1d4c69bc6262'
ACTUAL = '9e2dadfa650e2111b77f9eae1f834cc00b8805d5'
FINAL = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PREFIX = 'review/remediation/20261003-prepare/batches/B04/'
STAGE = PREFIX + 'integration-stage-1/'
checks = []
failures = []
evidence = {}
cache = {}

def git(*args):
    return subprocess.check_output(['git', *args])

def data(commit, path):
    key = (commit, path)
    if key not in cache:
        cache[key] = git('show', commit + ':' + path)
    return cache[key]

def obj(commit, path):
    return json.loads(data(commit, path))

def sha(value):
    return hashlib.sha256(value).hexdigest()

def blob(value):
    return hashlib.sha1(b'blob ' + str(len(value)).encode() + b'\0' + value).hexdigest()

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()

def check(name, condition, details=None):
    record = {'check': name, 'passed': bool(condition)}
    if details is not None:
        record['details'] = details
    checks.append(record)
    if not condition:
        failures.append(record)

def identity(commit, row, prefix='identity'):
    value = data(commit, row['path'])
    check(prefix + ' ' + commit + ':' + row['path'],
          sha(value) == row['sha256'] and blob(value) == row['git_blob'] and len(value) == row['bytes'])

def statuses(base, target):
    return [{'change': line.split('\t', 1)[0], 'path': line.split('\t', 1)[1]}
            for line in git('diff', '--no-ext-diff', '--no-textconv', '--no-renames', '--name-status', base, target).decode().splitlines()]

def paths(base, target):
    return [r['path'] for r in statuses(base, target)]

manifest = obj(ACTUAL, STAGE + 'integration-manifest.json')
freeze = obj(ACTUAL, STAGE + 'diff-and-freeze.json')
registration = obj(ACTUAL, STAGE + 'finding-registration.json')
history = obj(ACTUAL, STAGE + 'historical-repair-registration.json')
handshake = obj(ACTUAL, STAGE + 'downstream-handshake.json')
counts = obj(ACTUAL, STAGE + 'scope-counts.json')
impact = obj(ACTUAL, STAGE + 'merge-and-dependency-impact.json')
formal = sorted(r['candidate']['path'] for r in manifest['formal_candidate_identities'])
public = sorted(r['path'] for r in manifest['current_public_paths'])
check('actual is exact evidence-only child of payload', git('rev-parse', ACTUAL + '^').decode().strip() == PAYLOAD)
check('actual tree exact', git('rev-parse', ACTUAL + '^{tree}').decode().strip() == 'f642c902b9b256c4cc7e54dcbe7500a29aed0119')
check('payload tree exact frozen', git('rev-parse', PAYLOAD + '^{tree}').decode().strip() == freeze['payload_tree'])
check('payload has exact parent', git('rev-parse', PAYLOAD + '^').decode().strip() == freeze['payload_parent'])
check('evidence child adds precisely three files', statuses(PAYLOAD, ACTUAL) == sorted(
    [{'change': 'A', 'path': p} for p in freeze['final_actual_changed_paths']], key=lambda r:r['path']))
check('formal final/original authorized split', len(formal) == 13 and
      set(formal) == set(handshake['B04']['planned_final_writes8'] + handshake['B04']['authorized_original_sync5']) and
      len(handshake['B04']['planned_final_writes8']) == 8 and len(handshake['B04']['authorized_original_sync5']) == 5)
for r in manifest['formal_candidate_identities']:
    for k in ['candidate', 'merged', 'current', 'historical_upstream']:
        ident = r[k]
        identity(ident.get('commit', ACTUAL), ident, 'formal ' + k)
    p = r['candidate']['path']
    check('formal exact candidate and handoff retained ' + p, data(CAND,p) == data(HANDOFF,p) == data(ACTUAL,p))

# Derive source inventory from fixed commits/directories, independently of 96 claims.
source_commits = {'author-round-1/':OLD_HANDOFF, 'freeze-stage-1/':OLD_HANDOFF,
                  'author-round-2/':CAND, 'freeze-stage-2/':HANDOFF,
                  'review-round-1/':R1, 'review-round-2/':R2}
sources = {p:CAND for p in formal}
for directory, commit in source_commits.items():
    for p in git('ls-tree', '-r', '--name-only', commit, PREFIX + directory).decode().splitlines():
        sources[p] = commit
check('96 inventory independently derived', len(sources) == 96 and set(sources) == {r['path'] for r in manifest['source_identities']})
for r in manifest['source_identities']:
    check('registered immutable source equals independently selected original ' + r['path'],
          data(r['commit'], r['path']) == data(sources[r['path']], r['path']))
    identity(r['commit'], r, 'registered source')
    identity(sources[r['path']], r, 'source')
    identity(ACTUAL, r, 'preserved source')
check('both independent immutable report counts', sum('/review-round-1/' in p for p in sources) == 14 and sum('/review-round-2/' in p for p in sources) == 16)
check('author and freeze inventory 53', sum(any('/'+d in p for d in ['author-round-1/','author-round-2/','freeze-stage-1/','freeze-stage-2/']) for p in sources) == 53)
for r in manifest['current_public_paths']:
    identity(ACTUAL, r, 'public')
for key in ['payload_formal_identities','payload_public_and_management_identities','source_identities_preserved']:
    for r in freeze[key]:
        identity(r.get('commit', PAYLOAD), r, 'freeze recorded')
        identity(ACTUAL, r, 'freeze survives actual')

stagepaths = git('ls-tree','-r','--name-only',ACTUAL,STAGE).decode().splitlines()
expected = set(sources) | set(public) | set(stagepaths)
up = statuses(BASE, ACTUAL)
ca = statuses(CAND, ACTUAL)
check('upstream actual complete unfiltered 119 paths', len(up) == 119 and set(r['path'] for r in up) == expected)
check('candidate actual complete unfiltered 57 paths', len(ca) == 57 and set(r['path'] for r in ca) ==
      set(p for p in expected if p not in paths(BASE, CAND)))
check('upstream modifications exactly formal13 + public10', {r['path'] for r in up if r['change']=='M'} == set(formal+public))
check('candidate modifications exactly public10', {r['path'] for r in ca if r['change']=='M'} == set(public))
for key,actual in [('final_actual_complete_upstream_diff_contract',up),('final_actual_complete_candidate_diff_contract',ca)]:
    c = freeze[key]
    expected_status = sorted(c['payload_path_statuses'] + [{'change':'A','path':p} for p in c['final_added_paths']],key=lambda r:r['path'])
    check('complete actual contract '+key,actual == expected_status and len(actual)==c['expected_complete_path_count'])

patches=[]
for r in freeze['full_patches']:
    regenerated=git('diff',*r['git_diff_options'],r['base_commit'],r['target_commit'])
    check('complete unfiltered stored patch exact '+r['path'],regenerated == data(ACTUAL,r['path']) and sha(regenerated)==r['sha256'] and blob(regenerated)==r['git_blob'] and len(regenerated)==r['bytes'])
    check('complete stored patch path statuses '+r['path'],statuses(r['base_commit'],r['target_commit'])==r['complete_path_statuses'] and len(r['complete_path_statuses'])==r['changed_path_count'])
    patches.append({'base':r['base_commit'],'target':r['target_commit'],'path':r['path'],'sha256':sha(regenerated),'bytes':len(regenerated),'complete_path_count':len(r['complete_path_statuses'])})
actualdiffs=[]
for base,label in [(BASE,'upstream'),(CAND,'candidate')]:
    value=git('diff','--no-ext-diff','--no-textconv','--no-color','--no-renames','--binary','--full-index','--unified=3',base,ACTUAL)
    actualdiffs.append({'base':base,'target':ACTUAL,'kind':label,'bytes':len(value),'sha256':sha(value),'path_statuses':statuses(base,ACTUAL)})
    pathlib.Path('/tmp/rb04-actual-'+label+'.diff').write_bytes(value)
evidence['diffs']={'stored_payload_patches':patches,'complete_actual_diffs':actualdiffs}
evidence['source_inventory']=[{'path':p,'source_commit':c,'actual_blob':blob(data(ACTUAL,p)),'actual_sha256':sha(data(ACTUAL,p)),'bytes':len(data(ACTUAL,p))} for p,c in sorted(sources.items())]

for r in impact['normal_merges']:
    parents=git('show','-s','--format=%P',r['commit']).decode().strip().split()
    check('ordinary exact merge parents '+r['commit'],parents==r['parents'] and len(parents)==2)
    check('ordinary exact merge tree '+r['commit'],git('rev-parse',r['commit']+'^{tree}').decode().strip()==r['tree'])
check('first ordinary merge has no formal/source rewrite', set(paths(BASE,impact['normal_merges'][0]['commit']))==set(sources)-{p for p in sources if '/review-round-1/' in p})
check('second ordinary merge adds immutable R1 only', set(paths(impact['normal_merges'][0]['commit'],impact['normal_merges'][1]['commit']))=={p for p in sources if '/review-round-1/' in p})

# Immutable public history, canonical registry, accepted dependency history.
for p in public:
    before,after=data(BASE,p),data(ACTUAL,p)
    if p.endswith('.tsv'):
        check('public original byte prefix retained '+p,after.startswith(before))
    elif p.endswith('test-catalog/README.md'):
        check('catalog index history retained from usage convention '+p,
              before.split('## 使用约定'.encode(),1)[1] in after)
    else:
        lines=before.splitlines(keepends=True)
        check('public original body bytes retained '+p,b''.join(lines[2:]) in after)
for batch in ['B01','B02','B03','B05','B06']:
    p='review/remediation/20261003-prepare/batches/'+batch+'/'
    check('accepted full history immutable '+batch,not paths(BASE,ACTUAL) or not git('diff','--name-only',BASE,ACTUAL,'--',p))
    for p2 in git('ls-tree','-r','--name-only',BASE,p).decode().splitlines():
        check('accepted history blob unchanged '+p2,data(BASE,p2)==data(ACTUAL,p2))
for p in ['review/remediation-20261003-prepare','review/global-independent-review/2026-10-03-fd82a639','review/wp79-coverage-review-2026-10-03/revision-v6']:
    check('canonical and original source judgment histories unchanged '+p,not git('diff','--name-only',BASE,ACTUAL,'--',p))
statsrow=counts['prior_accepted_statistics_identity']
identity(BASE,statsrow,'prior statistics')
check('prior complete accepted statistics object unchanged',obj(BASE,statsrow['path'])==counts['prior_accepted_statistics'] and data(BASE,statsrow['path'])==data(ACTUAL,statsrow['path']))

# Full root / qualifications / adjudication / extension and acceptance equality.
findings={r['id']:r for r in obj(FINAL,'review/global-independent-review/2026-10-03-fd82a639/findings.json')}
acceptance=obj(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
plan={r['id']:r for r in obj(PLAN,'review/remediation-20261003-prepare/batches.json')}
control={r['id']:r for r in obj(R2,PREFIX+'review-round-2/fixed-control-bindings.json')['bindings']}
r2dispositions={r['id']:r for r in obj(R2,PREFIX+'review-round-2/finding-dispositions.json')['rows']}
authorresponses={r['id']:r for r in obj(CAND,PREFIX+'author-round-2/finding-responses.json')['responses']}
ids=plan['B04']['contribution_finding_ids']
primary=plan['B04']['primary_finding_ids']
check('all35 exact assigned IDs and23 primary',len(ids)==35 and len(primary)==23 and {r['id'] for r in registration['dispositions']}==set(ids) and {r['id'] for r in registration['dispositions'] if r['B04_primary']}==set(primary))
for r in registration['dispositions']:
    ident=r['id']; original=findings[ident]; acc=acceptance[ident]
    check('full original object preserved '+ident,control[ident]['original']==original and sha(canonical(original))==r['original_complete_object_sha256'])
    check('full acceptance object preserved '+ident,control[ident]['acceptance']==acc and sha(canonical(acc))==r['acceptance_object_sha256'])
    check('complete scoped R2 independent disposition preserved '+ident,r['independent_candidate_disposition_preserved']==r2dispositions[ident])
    check('complete author response preserved '+ident,r['author_round2_response_preserved']==authorresponses[ident])
    for key in ['current_qualifications','adjudication_precedence','effective_case_constraints','minimum_revision','determinate_recheck']:
        check('current qualification/control '+ident+':'+key,r[key]==original.get(key))
    check('acceptance gate exact '+ident,r['acceptance_gate']==acc['acceptance_gate'])
    contributor_ids=[b['id'] for b in plan.values() if ident in b['contribution_finding_ids']]
    check('all batch obligations kept '+ident,r['all_contributor_batches']==contributor_ids and r['other_batch_obligations']==[b for b in contributor_ids if b!='B04'])
    check('candidate and actual scope do not close canonical '+ident,r['canonical_state']=='OPEN' and not r['canonical_edited'] and r['candidate']==CAND and r['candidate_report']==R2 and r['candidate_verdict']=='PASS_SCOPED' and r['actual_integration_verdict']=='NOT_REVIEWED_PENDING_R_B04_ULTRA')
    for loc in r['formal_clause_bindings']:
        lines=data(ACTUAL,loc['path']).splitlines(keepends=True);a,z=loc['lines']
        check('actual clause range and text '+ident+':'+loc['path']+':'+str(a),sha(b''.join(lines[a-1:z]))==loc['range_sha256'] and loc['heading'] in lines[loc['line']-1].decode())
    for loc in r['static_rows_not_executed']:
        line=data(ACTUAL,loc['path']).splitlines(keepends=True)[loc['line']-1]
        check('actual static row '+ident+':'+loc['id'],sha(line)==loc['sha256'] and len(line)==loc['bytes'] and loc['status']=='STATIC_DESIGN_NOT_EXECUTED' and line.startswith(('| '+loc['id']+' |').encode()))

for p in ['approval-ledger.tsv','traceability-successor.tsv']:
    full='review/remediation/20261003-prepare/'+p
    before=list(csv.DictReader(io.StringIO(data(BASE,full).decode()),delimiter='\t'))
    current=list(csv.DictReader(io.StringIO(data(ACTUAL,full).decode()),delimiter='\t'))
    check('public record denominators '+p,len(before)==79 and len(current)==114 and current[:79]==before and {r['finding_id'] for r in current[79:]}==set(ids))
    byid={r['id']:r for r in registration['dispositions']}
    for r in current[79:]:
        ident=r['finding_id'];reg=byid[ident];rem=json.loads(r['remaining_obligations'])
        check('public candidate identity '+p+':'+ident,r['candidate_commit']==CAND and r.get('candidate_review_commit',r.get('candidate_review_commit'))==R2 and r['canonical_state']=='OPEN')
        check('public all other obligations '+p+':'+ident,rem['all_contributor_batches']==reg['all_contributor_batches'] and rem['other_batch_obligations']==reg['other_batch_obligations'] and rem['batch']=='B04')
        if p.startswith('traceability'):
            check('public actual clause bindings '+ident,json.loads(r['current_clause_inputs'])==reg['formal_clause_bindings'] and r['static_test_ids_not_executed'].split(';')==[v['id'] for v in reg['static_rows_not_executed']])
        else:
            kind='B04_'+('PRIMARY' if ident in primary else 'PARTIAL')+'_CANDIDATE_SCOPED_PENDING_ACTUAL_INTEGRATION'
            check('public actual pending and downstream blocked '+ident,r['integration_verdict']=='NOT_REVIEWED_PENDING_ULTRA' and r['downstream_gate']=='BLOCKED' and r['accepted_contribution_kind']==kind)

identity(R1,history['first_findings_identity'],'immutable R1 defects')
check('first defects preserved complete',history['complete_first_report_new_findings']==obj(R1,PREFIX+'review-round-1/new-findings.json'))
check('second repair verification preserved complete',history['second_round_repair_verification_preserved']==obj(R2,PREFIX+'review-round-2/repair-verification.json'))
check('no canonical additions/closure or observation closure',history['canonical229_inventory_mutations']==history['new_canonical_ids']==history['canonical_closed']==0 and not history['observations_closed'])

# Plan read/write lists and actual read-freezes include authorized fifth readers.
for b,k in [('B04','planned_reads74'),('B07','planned_reads64')]:
    rows=handshake[b][k]
    check('exact full planned readers '+b,{r['path'] for r in rows}==set(plan[b]['read_paths']))
    for r in rows:identity(r.get('commit',ACTUAL),r,'actual or fixed-object planned reader '+b)
check('planned write lists preserved',set(handshake['B04']['planned_final_writes8'])==set(plan['B04']['write_paths']) and set(handshake['B07']['allowed_writes8'])==set(plan['B07']['write_paths']))
for b in ['B06','B07']:
    rows=handshake[b]['all_changed_B04_readers5'];ps={r['current']['path'] for r in rows}
    check('five actual changed readers '+b,len(rows)==5 and ps==set(handshake[b]['planned_B04_readers4']+[handshake[b]['extra_original_reader']]) and set(plan[b]['read_paths'])&set(formal)==ps)
    for r in rows:
        for k in ['current','baseline','candidate']:
            identity(r[k].get('commit',ACTUAL),r[k],'dependency '+b+' '+k)
        identity(ACTUAL,r['current'],'actual dependency '+b)
        old=r['candidate_report_identity_preserved']
        identity(CAND,old,'R2 dependency retained '+b)
        identity(OLD,old['previous'],'R1 dependency retained '+b)
        check('actual dependency bytes equal reviewed candidate '+b+':'+r['current']['path'],data(ACTUAL,r['current']['path'])==data(CAND,r['current']['path']))
    check('R2 changed reader denominator '+b,sum(r['candidate_report_identity_preserved']['changed_since_round1'] for r in rows)==handshake[b]['second_round_changed_readers'])
for r in handshake['B06']['accepted_formal_outputs8']:
    identity(BASE,r,'accepted B06 formal baseline');identity(ACTUAL,r,'accepted B06 survives actual')
for r in handshake['reverse_B07_WP28_WP30']:
    identity(ACTUAL,r['current'],'future reverse review anchor')
    check('future reverse anchor unchanged and gate retained '+r['path'],data(BASE,r['path'])==data(ACTUAL,r['path']) and 'affected B04 review' in r['review_rule'])
for r in handshake['fixed_plan_identities']:identity(PLAN,r,'fixed plan identity')
check('serial downstream not unlocked',handshake['B04_to_B07_mandatory_serial'] and not handshake['B07']['B07_accepted'] and handshake['B04_parent_acceptance']=='NOT_PERFORMED' and handshake['downstream_tasks_dispatched']==0)

rowregex=re.compile(rb'^\| ([A-Z][A-Z0-9-]*[0-9]+[a-z]?) \|')
def rows(commit,path):
    return [(m.group(1).decode(),line) for line in data(commit,path).splitlines(keepends=True) if (m:=rowregex.match(line))]
catalog_counts={}
newrows={}
for p,claimed in counts['catalogs'].items():
    old,cur=rows(BASE,p),rows(ACTUAL,p)
    oldids=collections.Counter(x for x,_ in old);curids=collections.Counter(x for x,_ in cur)
    oldfiltered=[(x,line) for x,line in cur if x in oldids]
    changed=[a for (a,l),(b,n) in zip(old,oldfiltered) if a!=b or l!=n]
    check('catalog every old row order and multiplicity '+p,[x for x,_ in old]==[x for x,_ in oldfiltered])
    check('catalog old edits precisely authorized '+p,changed==claimed['changed_old_rows'])
    check('catalog complete counts independently counted '+p,len(old)==claimed['old_complete_rows'] and len(cur)==claimed['current_complete_rows'] and len(cur)-len(old)==claimed['added_rows'])
    added=[(x,l) for x,l in cur if x not in oldids]
    for x,l in added:newrows[x]=(p,l)
    check('lowercase three rows unchanged '+p,[(x,l) for x,l in old if re.search('[a-z]',x)]==[(x,l) for x,l in cur if x in oldids and re.search('[a-z]',x)])
    catalog_counts[p]={'old_complete':len(old),'actual_complete':len(cur),'new':len(added),'changed_old':changed,'old_duplicates':{x:n for x,n in oldids.items() if n>1}}
check('new static designs114 independently counted',len(newrows)==114 and sum(v['new'] for v in catalog_counts.values())==114)
firstrows={x:(p,line) for p in counts['catalogs'] for x,line in rows(OLD,p) if x not in {a for a,_ in rows(BASE,p)}}
modified=sorted(x for x,v in firstrows.items() if newrows.get(x)!=v)
newids=sorted(set(newrows)-set(firstrows))
check('111 retained108 exact3 modified3 new',len(firstrows)==111 and set(firstrows)<=set(newrows) and modified==['B04-R13','B04-R14','B04-W01'] and newids==['B04-R27','B04-R28','B04-W24'])
evidence['catalog_counts']=catalog_counts
evidence['static_row_ids']=sorted(newrows)
evidence['formal_paths']=formal
evidence['public_paths']=public

hashrows=list(csv.DictReader(io.StringIO(data(ACTUAL,STAGE+'current-hashes.tsv').decode()),delimiter='\t'))
check('current-hashes distinct source/formal/public inventory',len(hashrows)==106 and collections.Counter(r['kind'] for r in hashrows)==collections.Counter({'formal':13,'public':10,'immutable-source':83}) and {r['path'] for r in hashrows}==set(sources)|set(public))
for r in hashrows:
    r['bytes']=int(r['bytes']);identity(ACTUAL,r,'current hash receipt')
check('configuration Plan A no new confirmation gate',manifest['configuration']['Plan_A_accepted'] and not manifest['configuration']['new_confirmation_or_certification_gate'] and manifest['configuration']['effective_model_reasoning_speed']=='UNVERIFIED')
check('no false execution counts',manifest['reference_execution']==manifest['author_reviewer_program_execution']==manifest['behavior_vector_execution']==manifest['runtime_observations']==manifest['proven_Demo_chains']==0)

# Additional independent document checks after first judgment, then comparison of claims.
scope=registration['source_scope_successor_proposals']
identity(BASE,scope['historical_source_judgments_identity'],'original source-scope history')
sourcejudgments=obj(BASE,scope['historical_source_judgments_identity']['path'])
sourceby={r['path']:r for r in sourcejudgments['rows']}
for r in scope['ROOT002']['original_named_rows_preserved']:
    check('ROOT002 exact historical named NA row '+r['path'],sourceby[r['path']]==r)
check('ROOT002 scoped34 designs exact five families',collections.Counter(r['id'].split('-')[1][0] for r in scope['ROOT002']['static_design_pointers'])==collections.Counter({'L':10,'B':5,'D':6,'P':8,'T':5}))
check('source-scope no blanket A059 acceptance',not scope['B06_A059']['whole_BattleAudio_accepted'] and scope['no_original_NA_EXCLUDE_overwrite'])
for r in registration['dispositions']:
    check('all actual clause/static pointers retain candidate commit '+r['id'],all(z['commit']==CAND for z in r['formal_clause_bindings']+r['static_rows_not_executed']))
check('shared C003 full fixed object hashes and scope',handshake['shared_C003']['original_complete_object_sha256']==sha(canonical(findings['GIR-FD82-C003'])) and handshake['shared_C003']['acceptance_object_sha256']==sha(canonical(acceptance['GIR-FD82-C003'])) and handshake['shared_C003']['canonical_state']=='OPEN')

# New Markdown links only: historical carried links are immutable evidence, not new writes.
allactual=set(git('ls-tree','-r','--name-only',ACTUAL).decode().splitlines())
new_links=[]
for p in public+[STAGE+'README.md']:
    if not p.endswith('.md'):continue
    diff=git('diff','--no-ext-diff','--no-textconv','--no-color',BASE,ACTUAL,'--',p).decode()
    added='\n'.join(line[1:] for line in diff.splitlines() if line.startswith('+') and not line.startswith('+++'))
    for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',added):
        if '://' in target or target.startswith('#'):continue
        raw=target.split('#',1)[0]
        normalized=str(pathlib.PurePosixPath(p).parent.joinpath(raw))
        import posixpath
        normalized=posixpath.normpath(normalized)
        check('new public Markdown link '+p+' -> '+target,normalized in allactual)
        new_links.append({'from':p,'target':target,'resolved':normalized})
evidence['new_public_links']=new_links

inspection=obj(ACTUAL,STAGE+'input-inspection.json')
validation=obj(ACTUAL,STAGE+'validation-results.json')
check('input inspector counts and declared checks internally consistent',len(inspection['checks'])==inspection['check_count']==758 and all(r['pass_'] for r in inspection['checks']))
check('registration validation counts and declared checks internally consistent',len(validation['current_checks'])==validation['current_check_count']==1315 and all(r['pass_'] for r in validation['current_checks']))
check('input inspector derived formal and source exact',set(inspection['formal'])==set(formal) and inspection['source_identities']==manifest['source_identities'])
check('input inspector allocates exact114 independently derived designs',len(inspection['allocated_static_designs'])==114 and {r['id'] for r in inspection['allocated_static_designs']}==set(newrows))
for r in inspection['allocated_static_designs']:
    line=data(ACTUAL,r['path']).splitlines(keepends=True)[r['line']-1]
    check('input inspector exact unexecuted design identity '+r['id'],sha(line)==r['sha256'] and len(line)==r['bytes'] and r['status']=='STATIC_DESIGN_NOT_EXECUTED')
for r in inspection['commit_inventory']:
    check('input inspector exact historical commit parents/tree '+r['commit'],git('show','-s','--format=%P',r['commit']).decode().strip().split()==r['parents'] and git('rev-parse',r['commit']+'^{tree}').decode().strip()==r['tree'])
check('A-REG validation explicitly excludes execution',validation['independent1168_assertions_not_executed'] and validation['author900_checks_not_executed'] and not validation['semantic_adjudication_by_A_REG'])

refroot=pathlib.Path('/tmp/rb04-reference')
if refroot.exists():
    check('exact independent detached reference commit',subprocess.check_output(['git','-C',str(refroot),'rev-parse','HEAD']).decode().strip()==REF)
    check('exact independent reference tree',subprocess.check_output(['git','-C',str(refroot),'rev-parse','HEAD^{tree}']).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0')
    check('independent reference origin correct',subprocess.check_output(['git','-C',str(refroot),'remote','get-url','origin']).decode().strip()=='https://github.com/Maruno17/pokemon-essentials.git')
    check('independent reference tree remains clean',not subprocess.check_output(['git','-C',str(refroot),'status','--porcelain']))

evidence['author_comparison']={'inspection_declared_checks':758,'registration_declared_checks':1315,'prior_independent_checks_recorded':1168,'prior_author_checks_recorded':900,'those_historical_programs_executed':False,'sequence':'Detailed check claims compared only after independent first judgment; all numeric counts mean document checks, not behavior execution.'}

result={'kind':'INDEPENDENT_ACTUAL_GIT_AND_DOCUMENT_CHECKS_ONLY','actual_commit':ACTUAL,'candidate_commit':CAND,'baseline_commit':BASE,'all_checks_passed':not failures,'checks_count':len(checks),'failed_checks':failures,'checks':checks,'evidence':evidence,'reference_execution':0,'behavior_vector_execution':0,'runtime_observations':0,'proven_demo_chains':0}
print(json.dumps(result,ensure_ascii=False,indent=2))
