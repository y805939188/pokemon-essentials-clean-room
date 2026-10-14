"""Self-authored static identity and document-composition checks; no source execution."""
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
BASE='review/remediation-sixth-20261014-prepare/'
OUT=ROOT/BASE/'actual-reviews/group-D/peers/u11/final-increment'
A='86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
B='9d5b4e99b617828690e6529b77a1e555d7c9eb1b'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
C13='9971fe84896786645cdcda3ab45e5caf7785cabc'
V13='411b563309a4e642e628dcf8289e36c6fe3fd37f'
PREFIX='deliverables/final-specification-set/'
P62=PREFIX+'pokemon-rules/wp62-pokedex-records-regions-and-content.md'
P66=PREFIX+'user-interface/wp66-b-storage-and-pokedex-ui.md'
UI=PREFIX+'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
DOM=PREFIX+'test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'
P53=PREFIX+'pokemon-rules/wp53-safari-and-bug-catching-contest.md'
readset=[];checks=[]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*argv):
    return subprocess.check_output(['git',*argv],cwd=ROOT)
def read(commit,path,ranges=(),pointers=(),qualification='PERSONAL_NEW_SEMANTIC_READ'):
    b=git('show',commit+':'+path)
    mode,typ,blob=git('ls-tree',commit,'--',path).decode().split('\t')[0].split()
    readset.append(dict(repository=str(ROOT),commit=commit,path=path,mode=mode,type=typ,git_blob=blob,bytes=len(b),lines=len(b.splitlines()),sha256=hashlib.sha256(b).hexdigest(),semantic_ranges=list(ranges),semantic_pointers=list(pointers),qualification=qualification))
    return b
def check(label,value,detail):
    checks.append(dict(name=label,passed=bool(value),detail=detail))

data={}
for p,ranges in [(P62,()),(P66,()),(UI,()),(DOM,[(1,286)]),(P53,[(1,288)])]:
    data[p]=read(A,p,ranges,qualification='PERSONAL_NEW_FULL_TEXT' if ranges else 'EXACT_IDENTITY_PRIOR_9D_SEMANTIC_READ_REUSED; no new full-text claim')
for p in (P62,P66,UI):
    check('same exact prior actual blob '+p,data[p]==git('show',B+':'+p) and git('rev-parse',A+':'+p)==git('rev-parse',B+':'+p),'Explicit identity reuse only; final domain/interface decision separately reviewed.')
check('domain non-SF suffix intact',data[DOM].decode().split('## BP：',1)[1]==git('show',B+':'+DOM).decode().split('## BP：',1)[1],'All BP/FP/PD/R6-PD/VF/LT/HAB/R4-PD/later controls kept, shifted +5 lines.')
check('final WP53 equals repaired mirror',data[P53]==git('show',C13+':'+BASE+'candidates/R6-U13/mirror/'+P53),'Full semantic final WP53 read is independent of byte check.')
u13dom=git('show',C13+':'+BASE+'candidates/R6-U13/mirror/'+DOM)
check('final SF section equals repaired U13',data[DOM].decode().split('## BP：',1)[0]==u13dom.decode().split('## BP：',1)[0],'SF30 d/e and SF36-40 received together; U11 suffix retained separately.')
def row(b,rid):
    rows=[s for s in b.decode().splitlines() if s.startswith('| '+rid+' |')]
    return rows[0] if len(rows)==1 else None
old=git('show',B+':'+DOM)
for rid in ['PD%02d'%i for i in range(1,35)]+['R6-PD%02d'%i for i in range(1,4)]+['R4-PD%02d'%i for i in range(1,6)]:
    check('U11 and historical row '+rid,row(data[DOM],rid) is not None and row(data[DOM],rid)==row(old,rid),'Exact preservation plus new whole-final-catalog semantic read; not runtime test.')
for rid in ['SF%02d'%i for i in range(1,41)]:
    check('final raw SF row unique '+rid,row(data[DOM],rid) is not None,'Raw row lookup checks uniqueness before building any index; document identity only.')

input_path=BASE+'integration/U01-U14-final-composite-20261014/actual-review-input.json'
inp=json.loads(read(A,input_path,pointers=['/batches/10','/batches/13','/files/33','/files/34','/files/46','/files/47','/files/50','/resolutions','/delta_from_prior_actual/base_commit','/delta_from_prior_actual/base_workspace_tree','/delta_from_prior_actual/base_formal_tree','/delta_from_prior_actual/changed_formal_paths[WP53,domain]','/delta_from_prior_actual/existing_actual_reviews/1','/pending_candidates','/file_stability_qualification','/receiver_delta','/reading_qualification','/review_requirements','/administrative_sync','/state','/INTEGRATED_PASS','/formal_acceptance','/CLOSED','/actual_commit_binding','/prior_actual_input'],qualification='PERSONAL_NEW_COMPLETE_RELEVANT_INPUT_NODES; not all3243lines semantic'))
for f in inp['files']:
    if f['path'] in data:
        b=data[f['path']]; e=f['actual']
        check('final input fingerprint '+f['path'],len(b)==e['bytes'] and hashlib.sha256(b).hexdigest()==e['sha256'] and git('rev-parse',A+':'+f['path']).decode().strip()==e['git_blob'],'Complete input actual identities independently checked.')
for p in ('AGENTS.md',BASE+'contracts/R6-U11.json'):
    b=read(A,p,qualification='EXACT_IDENTITY_PREVIOUS_FULL_APPLICABLE_INSTRUCTION_OR_SEVEN_GROUP_READ_REUSED')
    check('unchanged applicable '+p,b==git('show',B+':'+p),'Original finite semantic range/contract groups stay in previous report; no new full read claim.')

source={
 'Data/Scripts/016_UI/001_UI_PauseMenu.rb':[(97,151),(250,321)],
 'Data/Scripts/016_UI/014_UI_Save.rb':[(1,139)],
 'Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb':[(83,123)],
 'Data/Scripts/003_Game processing/001_StartGame.rb':[(105,126)],
 'Data/Scripts/002_Save data/001_SaveData.rb':[(1,73)],
 'Data/Scripts/002_Save data/002_SaveData_Value.rb':[(1,178),(263,284)],
 'Data/Scripts/002_Save data/004_Game_SaveValues.rb':[(1,8),(72,104)],
 'Data/Scripts/018_Alternate battle modes/001_SafariZone.rb':[(1,93),(110,176)],
 'Data/Scripts/018_Alternate battle modes/002_BugContest.rb':[(1,90),(94,156),(278,304)]
}
for p,ranges in source.items():read(R,p,ranges)
read(V13,BASE+'reviews/R6-U13-R/repair-01/review-report.md',[(1,len(git('show',V13+':'+BASE+'reviews/R6-U13-R/repair-01/review-report.md').splitlines()))],qualification='PERSONAL_NEW_FULL_INDEPENDENT_REPAIR_RECEIPT; not U13 whole-batch adjudication')
read(A,BASE+'contracts/R6-U13.json',pointers=['/scope_contracts[GR6-F-S001]/premises_and_counterexample','/scope_contracts[GR6-F-S001]/acceptance_and_regression'],qualification='PERSONAL_NEW_COMPLETE_RELEVANT_SAVE_PREMISE_CONTROL_NODES; source locators partial only; not U13 seven-group review')

previous=[]
prior_dir=OUT.parent
expected={'peer-review.md':'64ab14d249b9fcbaa0455dc55ad1654d9fe414faa061d3f297290506e128016d','peer-review.json':'8e082253406ef43aaddec6671d35d89446354d2b6a764a84dc03b3115776f6fd','static-validation.json':'af2c8cda66d935d5f1be275abe7686efb366449efdee0c5004b64d5d859e6ecf'}
for name,digest in expected.items():
    b=(prior_dir/name).read_bytes(); sha=hashlib.sha256(b).hexdigest()
    previous.append(dict(path=str((prior_dir/name).relative_to(ROOT)),bytes=len(b),sha256=sha,qualification='FROZEN_PRIOR_9D_REPORT_AND_READSET; not changed or re-signed in place'))
    check('prior report untouched '+name,sha==digest,'No rewrite, move or signature migration; final increment is separate.')
prior=json.loads((prior_dir/'peer-review.json').read_text())
for c in prior['counterevidence_reuse']['records']:
    b=git('show',A+':'+c['input_path']); e=c['actual']
    check('same original counterpayload '+c['id'],len(b)==e['bytes'] and hashlib.sha256(b).hexdigest()==e['sha256'] and git('rev-parse',A+':'+c['input_path']).decode().strip()==e['git_blob'],'Reuse named independent complete payload readers from prior9d/V; no new full-original-payload credit.')

result=dict(schema='r6-u11-final-increment-static-validation.v1',evidence_level='TOOL_VALIDATION_ONLY',cwd=str(ROOT),argv=sys.argv,start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),fixed_actual_commit=A,workspace_tree=git('rev-parse',A+'^{tree}').decode().strip(),formal_tree=git('rev-parse',A+':deliverables/final-specification-set').decode().strip(),reference_commit=R,read_set=readset,prior_actual_review_artifacts=previous,prior_read_set_path=str((prior_dir/'static-validation.json').relative_to(ROOT))+'#/read_set',checks=checks,passed=all(x['passed'] for x in checks),reference_execution=0,author_script_execution=0,full_behavior_model_execution=0,host_Demo_real_save_execution=0,reading_note='Prior unchanged full-text scopes are explicitly reused. Final domain286/WP53288 are newly fully semantically read. Hash/row checks do not establish behavioral runtime or semantic reading. Early per-read UTC absent; this UTC covers checker only.',initial_read_attempt='Specified final input path initially git show exit128 during parent fetch; later same fixed object/path resolved; no missing-path conclusion retained. Oversized combined output was repaired by smaller reads/selected complete nodes.')
OUT.mkdir(parents=True,exist_ok=True)
target=OUT/'read-set-and-validation.json'
if target.exists():
    (OUT/'read-set-and-validation.prior-pass.json').write_bytes(target.read_bytes())
target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(passed=result['passed'],checks=len(checks),identities=len(readset),failures=[x for x in checks if not x['passed']]),ensure_ascii=False))
sys.exit(0 if result['passed'] else 1)
