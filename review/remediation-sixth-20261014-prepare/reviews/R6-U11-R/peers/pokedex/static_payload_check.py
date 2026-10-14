"""Independent byte/row validation only; no reference or author code execution."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path('/workspace/pokemon-essentials-clean-room')
OUT = ROOT / 'review/remediation-sixth-20261014-prepare/reviews/R6-U11-R/peers/pokedex'
M = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
C = '54af598ca85211641348e6057ed0c348044787fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
F = 'e93d0e56750a6a16cc50cc68b2c97f11ea255153'
PREFIX = 'review/remediation-sixth-20261014-prepare/'
FORMAL = 'deliverables/final-specification-set/'
MIRROR = PREFIX + 'candidates/R6-U11/mirror/'
START = datetime.now(timezone.utc).isoformat()
COMMANDS = []

def git(*args):
    argv = ['git', *args]
    t0 = datetime.now(timezone.utc).isoformat()
    p = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    COMMANDS.append({'argv': argv, 'cwd': str(ROOT), 'start_utc': t0,
                     'end_utc': datetime.now(timezone.utc).isoformat(),
                     'exit_code': p.returncode, 'stdout_bytes': len(p.stdout),
                     'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(),
                     'stderr': p.stderr.decode()})
    if p.returncode:
        raise RuntimeError(p.stderr.decode())
    return p.stdout

def identity(ref, path, semantic_ranges=None, semantic_pointers=None):
    b = git('show', ref + ':' + path)
    tree_line = git('ls-tree', ref, '--', path).decode().split()
    entry = {'repository': str(ROOT), 'commit': ref, 'path': path,
             'mode': tree_line[0], 'type': tree_line[1], 'git_blob': tree_line[2],
             'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
             'lines': len(b.splitlines()), 'semantic_ranges': semantic_ranges or [],
             'semantic_pointers': semantic_pointers or []}
    return entry, b

files = [
    ('user-interface/wp66-b-storage-and-pokedex-ui.md', [[1,300]], [[1,313]]),
    ('pokemon-rules/wp62-pokedex-records-regions-and-content.md', [[1,190]], [[1,192]]),
    ('test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',
     [[244,286],[584,613],[775,787],[854,880]],
     [[244,318],[615,644],[806,819],[885,921]]),
    ('test-catalog/pokemon-rules-wp53-60-61-62-69-70.md',
     [[1,269]], [[1,281]])
]
read_set = []
contents = {}
manifest = json.loads(git('show', C + ':' + PREFIX + 'candidates/R6-U11/evidence/candidate-manifest.json'))
expected = {x['path']: x for x in manifest['files']}
checks = []
for suffix, mranges, cranges in files:
    for ref, path, ranges in [(M, FORMAL + suffix, mranges), (C, MIRROR + FORMAL + suffix, cranges)]:
        entry, b = identity(ref, path, ranges)
        read_set.append(entry)
        contents[(ref, suffix)] = b.decode().splitlines()
        if ref == C:
            exp = expected[path]
            equal = all(entry[k] == exp[k] for k in ['bytes','sha256','git_blob','mode'])
            working_equal = (ROOT / path).read_bytes() == b
            checks.append({'kind':'candidate_manifest_and_working_bytes', 'path':path,
                           'manifest_identity_equal':equal, 'working_bytes_equal':working_equal})
            assert equal and working_equal
for path, ranges in [
    ('Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb', [[1,361]]),
    ('Data/Scripts/016_UI/003_UI_Pokedex_Main.rb', [[1,1302]]),
    ('Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb', [[1,619]]),
    ('Data/Scripts/002_Save data/004_Game_SaveValues.rb', [[1,25]]),
    ('Data/Scripts/001_Settings.rb', [[306,314]]),
    ('PBS/pokemon.txt', [[3,29],[469,496]]),
    ('PBS/pokemon_forms.txt', [[74,88]])
]:
    read_set.append(identity(R,path,ranges)[0])

for suffix, ids in [
    (files[2][0], ['B28','B29','B30','B31','B38','R4-DX05','B16-C122','U06-M11-003-F','U06-M11-003-J']),
    (files[3][0], ['PD31','PD32','PD33','PD34','R4-PD05'])
]:
    for row_id in ids:
        result = {'kind':'old_row_exact_preservation', 'path': FORMAL + suffix, 'id':row_id}
        selected=[]
        for ref in [M,C]:
            matches=[(i+1,s) for i,s in enumerate(contents[(ref,suffix)]) if s.startswith('| '+row_id+' |')]
            assert len(matches)==1
            selected.append(matches[0])
        result.update({'formal_line':selected[0][0], 'candidate_line':selected[1][0],
                       'equal':selected[0][1]==selected[1][1]})
        assert result['equal']
        checks.append(result)

for path,ranges,pointers in [
    ('AGENTS.md', [[1,297]], []),
    (PREFIX+'prompts/R6-U11-R.md', [[1,242],[740,1359],[3122,3220],[3390,3446]], []),
    (PREFIX+'contracts/R6-U11.json', [], ['/scope_contracts/1']),
    (PREFIX+'candidates/R6-U11/evidence/author-report.md', [[1,29]], []),
    (PREFIX+'candidates/R6-U11/evidence/candidate-manifest.json', [[1,176]], []),
    (PREFIX+'candidates/R6-U11/evidence/counterevidence-dispositions.json', [[1,159]], []),
    (PREFIX+'candidates/R6-U11/evidence/historical-regression.json', [[1,90]], []),
    (PREFIX+'candidates/R6-U11/evidence/per-id-author-verification.json', [], ['/groups/1']),
    (PREFIX+'inputs/evidence/tasks/R6-UI/root/counterreview-storage.json', [[1,118]], []),
    (PREFIX+'inputs/evidence/tasks/R6-F/countercheck-ui-entry-stale-command.json', [[1,19]], []),
    (PREFIX+'inputs/evidence/tasks/R6-K/imported-ui-party-storage-bag-facts.json', [],
     ['/140','/141','/142','/143','/144','/145','/146','/162','/165','/172','/193'])
]:
    entry,b = identity(F,path,ranges,pointers)
    if ranges and max(x[1] for x in ranges)>entry['lines']:
        entry['semantic_ranges']=[[lo,min(hi,entry['lines'])] for lo,hi in ranges]
    read_set.append(entry)

history = [
    (M,'review/wp66bc-wp71-review-2026-09-30/recheck-v3/report.md', [[1,107]], []),
    (M,'review/remediation/20261003-prepare/batches/B16/author-draft-1/traceability.json', [[4272,4437]], ['/trace/18']),
    (M,'review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/findings.json', [], ['/22']),
    ('9366d9d17aaeac3b4414236468affa650fb3dd27','review/remediation-fourth-20261012-prepare/registration/R4-U03/acceptance.json', [[1115,1420]], []),
    (M,'review/remediation-fifth-20261013-prepare/registration/successors/20261014-u06-formal-acceptance/U06-formal-acceptance.json', [],
     ['/accepted_finding_owner_results/14','/accepted_finding_owner_results/15','/accepted_actual_file_contributions/15','/signature_boundary']),
    ('13fddb0a217b36974c75657aa68da0caf104ee48','review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-closure-candidate/closure-candidate.json', [], ['/records/81','/records/82']),
    ('12df95a8e81061a606d50d3f0a0528793b2e6b2c','review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-activation/activation-receipt.json', [],
     ['/state_resolution/selection/81','/state_resolution/selection/82','/status','/closing_candidate','/effective_counts','/closure_scope','/preserved_exclusions','/history_preserved','/execution','/new_behavior_execution'])
]
for ref,path,ranges,pointers in history:
    read_set.append(identity(ref,path,ranges,pointers)[0])
trees={ref:git('rev-parse',ref+'^{tree}').decode().strip() for ref in [M,C,R,F]}
result={'schema':'r6-u11-pokedex-independent-static-payload-validation.v1',
        'evidence_level':'TOOL_VALIDATION_ONLY', 'cwd':str(ROOT), 'argv':sys.argv,
        'start_utc':START, 'end_utc':datetime.now(timezone.utc).isoformat(),
        'runtime':sys.version, 'exit_code':0, 'requested_configuration':
        {'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'default','fast':False},
        'actual_configuration':dict.fromkeys(['model','effort','tier','speed','platform_uuid'],'UNVERIFIED'),
        'trees':trees,'read_set':read_set,'checks':checks,'subprocess_receipts':COMMANDS,
        'reference_execution':0,'author_script_execution':0,'full_model_execution':0,
        'semantic_read_range_note':'Explicit ranges/pointers are personal semantic reading; hashing whole object is not full semantic reading. Earlier tool outputs/exit codes remain in platform transcript; missing early UTC is not backfilled.'}
(OUT/'static-payload-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':'PASS_TOOL_VALIDATION_ONLY','read_payloads':len(read_set),
                  'checks':len(checks),'start_utc':START,'end_utc':result['end_utc']},ensure_ascii=False))
