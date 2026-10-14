"""Validate and finalize this narrow static review after manual reading."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess
ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=Path(__file__).resolve().parent
REF=ROOT/'reference/pokemon-essentials'
def sha(b): return hashlib.sha256(b).hexdigest()
def write(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def append(name,obj):
    with (OUT/name).open('a') as f: f.write(json.dumps(obj,ensure_ascii=False)+'\n')
def command(args,cwd=ROOT):
    p=subprocess.run(args,cwd=cwd,capture_output=True,check=True)
    append('command-log.jsonl',{'utc':datetime.now(timezone.utc).isoformat(),'action':'read_only_git_validation','argv':args,'cwd':str(cwd),'exit_code':p.returncode,'stdout_bytes':len(p.stdout),'stdout_sha256':sha(p.stdout),'stderr':p.stderr.decode()})
    return p.stdout
source=REF/'Text_english_core/POKEDEX_ENTRIES.txt'
raw=source.read_bytes(); lines=raw.decode('utf-8-sig').splitlines()
rows=json.loads((OUT/'reviewed-records.json').read_text())
assert len(rows)==1028 and all(r['semantic_status']=='semantic_read' for r in rows)
baseline={'reference_commit':command(['git','rev-parse','HEAD'],REF).decode().strip(),'reference_tree':command(['git','rev-parse','HEAD^{tree}'],REF).decode().strip(),'formal_main_commit':command(['git','rev-parse','HEAD']).decode().strip(),'formal_main_tree':command(['git','rev-parse','HEAD^{tree}']).decode().strip(),'formal_tree':command(['git','rev-parse','HEAD:deliverables/final-specification-set']).decode().strip()}
assert baseline=={'reference_commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','formal_main_commit':'8ea169fbd0f33f378b5d732fd6bea59e854e04a6','formal_main_tree':'6ab3429170d2762607fbc2237014c3a160449fa1','formal_tree':'1046fbb657882e84b3dfc6d017943a9edf7782e5'}
assert raw==command(['git','show','HEAD:Text_english_core/POKEDEX_ENTRIES.txt'],REF)
sources=[('reference/pokemon-essentials/Data/Scripts/010_Data/002_PBS data/008_Species.rb',230,245),('reference/pokemon-essentials/Data/Scripts/001_Technical/003_Intl_Messages.rb',475,492),('reference/pokemon-essentials/Data/Scripts/001_Technical/003_Intl_Messages.rb',590,615),('reference/pokemon-essentials/Data/Scripts/001_Technical/003_Intl_Messages.rb',675,685),('reference/pokemon-essentials/Data/Scripts/001_Technical/003_Intl_Messages.rb',748,772),('reference/pokemon-essentials/Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb',241,270),('reference/pokemon-essentials/Text_english_core/POKEDEX_ENTRIES.txt',1,4),('specs/kernel/wp08-localization.md',1,195),('deliverables/final-specification-set/generic-kernel/wp08-localization.md',1,214),('deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md',149,156),('deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md',225,233)]
for path,a,b in sources:
    p=ROOT/path
    append('reading-ledger.jsonl',{'path':path,'line_range':[a,b],'sha256':sha(p.read_bytes()),'review_extent':'semantic_read','method':'manual acceptance after complete numbered range display; only this range accepted'})
    if p.is_relative_to(REF):
        assert p.read_bytes()==command(['git','show','HEAD:'+str(p.relative_to(REF))],REF)
    else:
        assert p.read_bytes()==command(['git','show','HEAD:'+str(p.relative_to(ROOT))])
ledger=[json.loads(l) for l in (OUT/'reading-ledger.jsonl').read_text().splitlines()]
displayed=set();accepted=set()
for r in ledger:
    if r.get('path')=='Text_english_core/POKEDEX_ENTRIES.txt' and 'unit_range' in r:
        a,b=r['unit_range'];target=accepted if r['review_extent']=='semantic_read' else displayed
        target.update(range(a,b+1))
assert displayed==accepted==set(range(1028))
identity=json.loads((OUT.parent/'records-POKEDEX_ENTRIES.json').read_text())
for n,r in enumerate(rows):
    key,val=lines[4+2*n:6+2*n]
    assert key==val and r['unit']==f'POKEDEX_ENTRIES:{n}' and r['lines']==[5+2*n,6+2*n]
    assert r['key_sha256']==r['value_sha256']==sha(key.encode())
    for f in ['unit','lines','key_sha256','value_sha256','duplicate_identity']: assert r[f]==identity[n][f]
    r['path']='Text_english_core/POKEDEX_ENTRIES.txt'
    r['source_traceability']+=['Data/Scripts/001_Technical/003_Intl_Messages.rb:682','Data/Scripts/001_Technical/003_Intl_Messages.rb:752-754','Data/Scripts/001_Technical/003_Intl_Messages.rb:768-770','Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb:247-266']
    r['source_traceability']=list(dict.fromkeys(r['source_traceability']))
    r['formal_mapping']=['deliverables/final-specification-set/generic-kernel/wp08-localization.md:25 (section 3.1)','deliverables/final-specification-set/generic-kernel/wp08-localization.md:30 (section 3.2)','deliverables/final-specification-set/generic-kernel/wp08-localization.md:51 (section 5.1)','deliverables/final-specification-set/generic-kernel/wp08-localization.md:61 (section 5.2)','deliverables/final-specification-set/generic-kernel/wp08-localization.md:113 (section 6.2)','deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md:154','deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md:231']
    r['classification']=['Generic Kernel: localization lookup','Pokémon Rules: encyclopedia description content','User Interface: owned-species information page']
    r['finding_proposal']=None
write('reviewed-records.json',rows)
keys=[lines[4+2*n] for n in range(1028)]
structure={'records':1028,'physical_lines':len(lines),'identity_pairs':sum(lines[4+2*n]==lines[5+2*n] for n in range(1028)),'unique_bodies':len(set(keys)),'empty_bodies':sum(not k for k in keys),'numeric_only_bodies':sum(bool(re.fullmatch(r'\d+',k)) for k in keys),'leading_hash':sum(k.startswith('#') for k in keys),'leading_or_trailing_whitespace':sum(k!=k.strip() for k in keys),'placeholder_candidates':sum(bool(re.search(r'\{[^{}]*\}',k)) for k in keys),'angle_escape_candidates':sum(bool(re.search(r'<<[^<>]*>>',k)) for k in keys),'backslash_candidates':sum('\\' in k for k in keys),'tag_candidates':sum(bool(re.search(r'</?[^>]+>',k)) for k in keys),'control_characters':sum(any(ord(c)<32 for c in k) for k in keys),'semantic_read':len(accepted),'semantic_unread':1028-len(accepted),'displayed_units':len(displayed),'identity_inventory_comparison':'1028/1028 match; inventory used for identity verification only'}
write('validation.json',structure)
write('provenance.json',{**baseline,'source_sha256':sha(raw),'reviewer_runtime':{'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','uuid':'UNVERIFIED'},'method':'static read only; all unique natural-language bodies displayed and manually accepted in this run; no reference source execution, no deserialization, no network','formal_files':[{'path':p,'sha256':sha((ROOT/p).read_bytes()),'range':[a,b]} for p,a,b in sources if p.startswith('deliverables/final-specification-set/')],'context_only_files':[{'path':p,'sha256':sha((ROOT/p).read_bytes()),'range':[a,b]} for p,a,b in sources if p.startswith('specs/')]})
write('task-status.json',{'task':'R6-D/localization/pokedex','stage':'complete','records':1028,'semantic_read':1028,'semantic_unread':0,'identity_pairs_deduplicated':1028,'manual_ranges':[[0,99],[100,199],[200,299],[300,399],[400,499],[500,599],[600,699],[700,799],[800,899],[900,999],[1000,1027]],'actual_model':'UNVERIFIED','actual_effort':'UNVERIFIED','actual_tier':'UNVERIFIED','actual_speed':'UNVERIFIED','actual_uuid':'UNVERIFIED','scope':'Pokédex localization text semantics; no gameplay truth inferred from lore','findings_status':'proposal_only','finding_proposals':0,'parent_merge_required':True,'runtime_or_demo_executed':False})
write('feature-matrix.json',[{'feature':'F02-05 / POKEDEX_ENTRIES text corpus','classification':['Generic Kernel','Pokémon Rules','User Interface'],'review_scope':'domain 3 species/form lore localization only','units':1028,'semantic_read':1028,'semantic_unread':0,'consumer_evidence':'Species entry accessor -> text-key lookup -> current-language game/core -> original input; owned species Info page consumes result','formal_evidence':['WP08 sections 3.1,3.2,5.1,5.2,6.2','WP62 section 6 entry-page row','WP66-B section 7.1 Info page'],'finding_proposal':None,'status':'independent subtask complete; parent merge pending; no global completion verdict'}])
write('findings.json',{'status':'proposal_only','proposals':[],'conclusion':'No additional localization behavior mismatch identified from the fully read Pokédex corpus within this narrow static scope. Lore assertions are not evidence of executable game rules.','not_adjudicated':['global R6-D closure','all-language coverage','rendering and layout','gameplay accuracy of lore','demo or runtime behavior']})
append('command-log.jsonl',{'utc':datetime.now(timezone.utc).isoformat(),'action':'additional_read_only_commands_audit','commands':['rg -n consumer wrappers/domain constant; git rev-parse formal tree; shasum WP08 pair','diff -u WP08 pair (truncated; not counted as semantic read)','rg -n pokedex_entry in 016_UI','initial glob lookup for formal Pokédex paths failed before search (zsh no matches); no coverage counted','rg --files formal tree | rg pokedex/species','rg clause lookup for WP62 and WP66-B (WP66-B search truncated); semantic coverage only from subsequent complete narrow displayed ranges'],'note':'Actions performed outside reader helper; no source/formal mutations'})
append('command-log.jsonl',{'utc':datetime.now(timezone.utc).isoformat(),'action':'final_validate','argv':['python3',str(Path(__file__).relative_to(ROOT))],'records':1028,'semantic_unread':0,'result':'pass','note':'Structural checks validate audit coverage/identity, not semantic understanding'})
report='''# R6-D Pokédex localization independent subtask

All 1,028 records in `Text_english_core/POKEDEX_ENTRIES.txt` were semantically read in this run. Remaining unread: **0**. Each original key and translation body is byte-identical, so each pair's unique body was displayed with its duplicate copy omitted; no natural-language body was omitted. Consecutive ranges were 0–99, 100–199, 200–299, 300–399, 400–499, 500–599, 600–699, 700–799, 800–899, 900–999 and 1000–1027 (zero-based record identities; physical lines 5–2060). Range 0–99 was displayed again without aggregate-output truncation. File instructions/header lines 1–4 were separately read.

The bodies describe species and forms: appearance, habitats, diet, social behavior, legends, anatomy, evolution narratives and purported combat powers. All are lore data. Numeric temperatures, distances, percentages, times, named moves, conditional transformations, guaranteed wins or invulnerability assertions do not establish executable game rules. The later regional, Mega, weather, appliance, size, fused and flavor descriptions remain ordinary localized strings. No body requires placeholder substitution or contains a control escape; punctuation, accents and typography are content.

The independently inspected consumer path is the species entry accessor (`Data/Scripts/010_Data/002_PBS data/008_Species.rb:238–241`), domain 3 (`001_Technical/003_Intl_Messages.rb:682`), forwarding helpers (`752–754`, `768–770`), key normalization (`481–489`) and text-key lookup (`600–610`). The owned-species information page submits the resulting entry text for rendering (`016_UI/004_UI_Pokedex_Entry.rb:247–266`). Thus these bodies are lookup keys and returned description values, with current-language game precedence over core and original-input fallback. The accessor itself does not interpret the lore as instructions. This is static evidence, not an executed or rendered scenario.

Formal mapping uses only the independently read frozen `deliverables/final-specification-set/` baseline. Relevant WP08 clauses: §3.1/domain 3 (line 25), §3.2/text keys (30), §5.1/game→core→original (51), §5.2/empty-hit behavior (61), and §6.2/two-line hash export (113). The UI use maps to WP62 §6/entry-page row (154) and WP66-B §7.1/Info page (231). The legacy `specs/kernel/wp08-localization.md` was read for context and is not the formal baseline. The supplied corpus has no actual empty translation, numeric-only body, control escape or placeholder; the corpus therefore supplies no new counterexample to those generic boundary clauses. Those broader contracts are not proved exhaustively by this narrow pass.

No additional finding is proposed for this corpus. This is **proposal only**, not final R6-D adjudication or global completeness. No gameplay truth was inferred from lore, and no source text, architecture or framework implementation was produced. No reference source execution, deserialization, game/Demo execution, installation or network access occurred. Only files under this subtask directory were written.

The fixed reference commit/tree and formal commit/tree were checked directly and are recorded in `provenance.json`. Relevant on-disk files were compared byte-for-byte with their pinned Git objects. Actual model, reasoning effort, service tier, speed and UUID are **UNVERIFIED**.

`reviewed-records.json` gives every record identity, exact physical line pair, key/value/file hashes, semantic acceptance, consumer mapping and formal mapping. `reading-ledger.jsonl` separates displays, structural evidence and manual semantic acceptance. `command-log.jsonl` records reading actions and validations, including truncated searches/diffs for which no coverage was claimed. `validation.json` checks contiguous coverage and identity; parsing is not asserted as semantic reading. `feature-matrix.json` is the local merge proposal for the parent global Feature Matrix. Uncertainty remains in runtime presentation, rendering, other language values and gameplay semantics outside this scope.
'''
(OUT/'report.md').write_text(report)
print(json.dumps({'semantic_read':1028,'semantic_unread':0,'finding_proposals':0,'validation':'pass','output':str(OUT)},ensure_ascii=False))
