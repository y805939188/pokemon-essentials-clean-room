"""Independent byte/row checks only. Never executes source or author scripts."""
import datetime
import difflib
import hashlib
import json
import pathlib
import subprocess
import sys

REPO = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = REPO / 'review/remediation-sixth-20261014-prepare/actual-reviews/group-D/peers/u11'
A = '9d5b4e99b617828690e6529b77a1e555d7c9eb1b'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
M = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
C = 'e93d0e56750a6a16cc50cc68b2c97f11ea255153'
V = '2b6832d1049650e08a071dccabce23326cc2c9ef'
BASE = 'review/remediation-sixth-20261014-prepare/'
PREFIX = 'deliverables/final-specification-set/'
WP62 = PREFIX + 'pokemon-rules/wp62-pokedex-records-regions-and-content.md'
WP66 = PREFIX + 'user-interface/wp66-b-storage-and-pokedex-ui.md'
DOMAIN = PREFIX + 'test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'
UI = PREFIX + 'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
ledger = []
checks = []
start = datetime.datetime.now(datetime.timezone.utc).isoformat()

def git(*args):
    return subprocess.run(['git', *args], cwd=REPO, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout

def data(commit, path):
    return git('show', commit + ':' + path)

def record(commit, path, ranges=(), pointers=(), qualification='PERSONAL_NEW_SEMANTIC_RANGES'):
    b = data(commit, path)
    mode, typ, blob = git('ls-tree', commit, '--', path).decode().split('\t')[0].split()
    obj = dict(repository=str(REPO), commit=commit, path=path, mode=mode, type=typ, git_blob=blob,
               bytes=len(b), sha256=hashlib.sha256(b).hexdigest(), lines=len(b.splitlines()),
               semantic_ranges=list(ranges), semantic_pointers=list(pointers), reading_qualification=qualification)
    ledger.append(obj)
    return b

def check(name, success, detail):
    checks.append(dict(name=name, passed=bool(success), detail=detail))

actual = {}
for path, ranges in [(WP62,[(1,196)]),(WP66,[(1,313)]),(DOMAIN,[(1,281)]),
                     (UI,[(244,317),(334,334),(358,358),(615,645),(743,760),(806,819),(885,911),(947,1026)])]:
    actual[path] = record(A,path,ranges)
    check('working bytes equal fixed A: '+path, (REPO/path).read_bytes()==actual[path], 'Full-byte TOOL_VALIDATION; semantic ranges separately supplied.')

input_path = BASE + 'integration/U01-U12-U14-composite-20261014/actual-review-input.json'
inp = json.loads(record(A,input_path,pointers=['/batches/10','/files/29','/files/40','/files/41','/files/44','/resolutions/0','/pending_candidates','/receiver_delta','/reading_qualification','/review_requirements','/administrative_sync','/actual_commit_binding','/prior_actual_input'],qualification='PERSONAL_NEW_COMPLETE_U11_BINDING_AND_CONDITIONS; not all 2661 lines semantic'))
check('actual input working bytes equal fixed A', (REPO/input_path).read_bytes()==data(A,input_path),'Fixed input only; externally binds A, no invented self SHA.')
for f in inp['files']:
    if f['path'] in actual:
        b = actual[f['path']]
        expected = f['actual']
        check('input binds actual '+f['path'],len(b)==expected['bytes'] and hashlib.sha256(b).hexdigest()==expected['sha256'] and git('rev-parse',A+':'+f['path']).decode().strip()==expected['git_blob'],'Input actual byte/SHA256/blob binding checked independently.')

record(A,'AGENTS.md',[(1,297)])
record(A,BASE+'contracts/R6-U11.json',pointers=['/scope_contracts/0','/scope_contracts/2','/frozen_main','/frozen_reference','/candidate_formal_paths','/read_only_reference_paths','/additional_read_set','/closure_gate','/policy_limits','/state'],qualification='PERSONAL_NEW_ALL_SEVEN_GROUPS_0_2_AND_ORIGINALS; scope1 exact-identity previous personal full read reused')
record(A,PREFIX+'user-interface/wp17-messages-windows-input.md',[(80,145)])
record(A,PREFIX+'pokemon-rules/wp34-inheritance-and-offspring.md',[(171,184)])
record(A,PREFIX+'pokemon-rules/wp21-dynamic-forms-and-display.md',[(190,202)])

source_ranges = {
 'Data/Scripts/016_UI/017_UI_PokemonStorage.rb':[(679,714),(733,790),(793,835),(837,990),(1020,1062),(1314,1392),(1490,1662),(1958,2022)],
 'Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb':[(1,148),(183,226),(293,361)],
 'Data/Scripts/016_UI/003_UI_Pokedex_Main.rb':[(348,415),(748,773),(868,894)],
 'Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb':[(139,200),(424,485),(488,555),(576,619)],
 'Data/Scripts/002_Save data/004_Game_SaveValues.rb':[(1,8),(97,103)],
 'Data/Scripts/001_Settings.rb':[(220,224),(303,315)],
 'Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb':[(54,86),(231,260)],
 'Data/Scripts/012_Overworld/007_Overworld_DayCare.rb':[(1,255),(350,385),(395,435),(450,502)],
 'Data/Scripts/014_Pokemon/001_Pokemon.rb':[(132,184),(316,399),(434,514),(1130,1227)],
 'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb':[(1,792)],
 'Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb':[(1,64)],
 'Data/Scripts/019_Utilities/001_Utilities.rb':[(384,420)],
 'Data/Scripts/021_Compiler/001_Compiler.rb':[(970,1038)],
 'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb':[(590,631),(1274,1321)],
 'Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb':[(362,393)],
 'Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb':[(1145,1210)],
 'Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb':[(1320,1410)],
 'PBS/pokemon.txt':[(11113,11140)]
}
for p, ranges in source_ranges.items():
    record(R,p,ranges)

review_paths = [
 'review-report.md','historical-and-receivers.json','peers/storage/peer-review.md',
 'peers/pokedex/peer-review.json','peers/pokedex/static-payload-validation.json'
]
for p in review_paths:
    path=BASE+'reviews/R6-U11-R/'+p
    b=record(V,path,qualification='PERSONAL_NEW_COMPLETE_PUBLISHED_REVIEW_READ; previous exact-identity evidence reused, verdict not migrated')
    ledger[-1]['semantic_ranges']=[(1,len(b.splitlines()))]

old = json.loads(data(V,BASE+'reviews/R6-U11-R/peers/pokedex/static-payload-validation.json'))
for item in old['read_set']:
    b=data(item['commit'],item['path'])
    check('reused payload identity '+item['path'],len(b)==item['bytes'] and hashlib.sha256(b).hexdigest()==item['sha256'] and git('rev-parse',item['commit']+':'+item['path']).decode().strip()==item['git_blob'],'Same fixed identity; earlier personal semantic ranges retained, not claimed newly full-read here.')
    ledger.append({**item,'reading_qualification':'EXACT_IDENTITY_PREVIOUS_PERSONAL_SEMANTIC_READ_REUSED_FROM_V; not current-task new full reading'})

counter_path = BASE+'reviews/R6-U11-R/peers/evidence/counter-payload-audit.json'
counter = json.loads(record(V,counter_path,pointers=['/bindings','/payload_records/*/{id,input_path,actual,full_semantic_read,original_targets,content,application,preserved_limits}','/findings','/historical_preservation','/outcome'],qualification='PERSONAL_NEW_COMPLETE_IDENTITY_APPLICATION_AND_LIMIT_NODES; full original nine payload reading reused from named independent peer'))
for item in counter['payload_records']:
    b = record(A,item['input_path'],qualification='EXACT_IDENTITY_PREVIOUS_PEER_FULL_READ_REUSED; reader /root/evidence_audit/counter_payloads at V, not personal new full read')
    expected = item['actual']
    check('counter original identity '+item['id'],len(b)==expected['bytes'] and hashlib.sha256(b).hexdigest()==expected['sha256'] and git('rev-parse',A+':'+item['input_path']).decode().strip()==expected['git_blob'] and b==data(C,item['input_path']),'Current A input equals C and independently reviewed V receipt; original recovery commit was not fetched or re-read.')

candidate={p:record(C,BASE+'candidates/R6-U11/mirror/'+p,qualification='BYTE_VALIDATION_ONLY; candidate semantic review bound in published V') for p in actual}
for p in (WP66,DOMAIN):
    check('fixed actual equals U11 candidate '+p,actual[p]==candidate[p],'Does not replace new actual full semantic read.')
ui_changes = list(difflib.SequenceMatcher(a=candidate[UI].decode().splitlines(),b=actual[UI].decode().splitlines(),autojunk=False).get_opcodes())
ui_changes = [v for v in ui_changes if v[0] != 'equal']
allowed = [('replace',333,334,333,334),('replace',357,358,357,358),('insert',945,945,945,1026)]
check('actual UI difference from U11 C limited to U12 C12/C36 and U10/U12 appendix',ui_changes==allowed,repr(ui_changes)+'; complete U11 blocks preserved, C12/C36 assigned to U12 and do not change U11 semantics.')
clause=candidate[WP62].decode().splitlines()[173]
check('WP62 U11 last-form clause retained exactly',clause in actual[WP62].decode().splitlines(),'C174 to actual176; U01/U09 additions separately source-reviewed.')

def row(b, rid):
    found=[v for v in b.decode().splitlines() if v.startswith('| '+rid+' |')]
    return found[0] if len(found)==1 else None

for p,ids in [(UI,['B03','B04','B05','B06','B07','B17','B28','B29','B30','B31','B38','B16-004','B16-C120','B16-C122','R4-CM01','R4-CM02','R4-CM03','R4-CM04','R4-DX01','R4-DX02','R4-DX03','R4-DX04','R4-DX05','U06-M11-003-F','U06-M11-003-J']),
              (DOMAIN,['PD31','PD32','PD33','PD34','R4-PD01','R4-PD02','R4-PD03','R4-PD04','R4-PD05'])]:
    oldb=data(M,p)
    for rid in ids:
        check('protected old row '+rid,row(oldb,rid) is not None and row(oldb,rid)==row(actual[p],rid),'Exact row preservation only; relevant semantics freshly checked against source.')
for p,ids in [(UI,['R6-BX%02d'%i for i in range(1,12)]+['R6-DX%02d'%i for i in range(1,5)]),(DOMAIN,['R6-PD%02d'%i for i in range(1,4)])]:
    for rid in ids:
        check('received candidate row '+rid,row(candidate[p],rid) is not None and row(candidate[p],rid)==row(actual[p],rid),'Current actual independently reviewed; no runtime result.')

out=dict(schema='r6-u11-actual-static-validation.v1',evidence_level='TOOL_VALIDATION_ONLY',cwd=str(REPO),
         argv=sys.argv,start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
         fixed_actual_commit=A,workspace_tree=git('rev-parse',A+'^{tree}').decode().strip(),formal_tree=git('rev-parse',A+':deliverables/final-specification-set').decode().strip(),
         read_set=ledger,checks=checks,passed=all(c['passed'] for c in checks),
         reference_execution=0,author_script_execution=0,full_behavior_model_execution=0,host_Demo_real_save_execution=0,
         semantic_note='Static file/row parsing does not grant semantic reading. Only recorded personally completed spans/pointers or explicitly marked prior receipts are credited. No per-read UTC was captured earlier; validation UTC is not backdated semantic-read UTC.')
OUT.mkdir(parents=True,exist_ok=True)
prior = OUT/'static-validation.json'
if prior.exists():
    suffix = 1
    while (OUT/('static-validation.attempt-%02d.json'%suffix)).exists():
        suffix += 1
    (OUT/('static-validation.attempt-%02d.json'%suffix)).write_bytes(prior.read_bytes())
prior.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(passed=out['passed'],checks=len(checks),identities=len(ledger),failures=[c for c in checks if not c['passed']]),ensure_ascii=False))
sys.exit(0 if out['passed'] else 1)
