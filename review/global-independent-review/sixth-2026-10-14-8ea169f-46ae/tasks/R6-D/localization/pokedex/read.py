"""Narrow review display/ledger tool. No source execution or mutation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys
ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = Path(__file__).resolve().parent
REF = ROOT/'reference/pokemon-essentials'
SOURCE = REF/'Text_english_core/POKEDEX_ENTRIES.txt'
def sha(b): return hashlib.sha256(b).hexdigest()
def append(name, obj):
    with (OUT/name).open('a') as f: f.write(json.dumps(obj, ensure_ascii=False)+'\n')
def write(name, obj): (OUT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
def event(action, **kwargs): append('command-log.jsonl', {'utc': datetime.now(timezone.utc).isoformat(), 'action': action, **kwargs})
def records():
    raw = SOURCE.read_bytes(); lines = raw.decode('utf-8-sig').splitlines()
    assert len(lines)==2060 and lines[3]=='[POKEDEX_ENTRIES]'
    rows=[]
    for n in range(1028):
        k,v=lines[4+2*n:6+2*n]
        assert k==v
        rows.append({'unit': f'POKEDEX_ENTRIES:{n}', 'lines': [5+2*n,6+2*n], 'key_sha256':sha(k.encode()), 'value_sha256':sha(v.encode()), 'duplicate_identity':True, 'file_sha256':sha(raw), 'semantic_status':'not_read'})
    return lines,rows
def status(rows):
    n=sum(r['semantic_status']=='semantic_read' for r in rows)
    write('reviewed-records.json',rows)
    write('task-status.json',{'task':'R6-D/localization/pokedex', 'stage':'semantic_reading' if n<1028 else 'complete', 'records':1028,'semantic_read':n,'semantic_unread':1028-n,'actual_model':'UNVERIFIED','actual_effort':'UNVERIFIED','actual_tier':'UNVERIFIED','actual_speed':'UNVERIFIED','actual_uuid':'UNVERIFIED','scope':'Pokédex localization text semantics; no gameplay truth inferred from lore','findings_status':'proposal_only'})
if sys.argv[1]=='init':
    lines,rows=records();status(rows)
    event('initialize_independent_identity_inventory', file=str(SOURCE.relative_to(ROOT)), records=len(rows), sha256=sha(SOURCE.read_bytes()), semantic_status='not_read', note='Original records independently constructed from text; sibling inventory not used as semantic evidence')
    for path in ['AGENTS.md','review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-D/localization/read-compact.py','review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-D/localization/audit.py']:
        p=ROOT/path
        append('reading-ledger.jsonl',{'path':path,'line_range':[1,len(p.read_text().splitlines())],'sha256':sha(p.read_bytes()),'review_extent':'semantic_read','method':'full file displayed and read before authoring isolated reader; retrospective entry'})
    event('preinitialization_commands', commands=['cat AGENTS.md','pwd and scoped rg inventory','cat sibling read-compact.py and audit.py','broad rg filename lookup (output truncated; no semantic claim)','git rev-parse HEAD HEAD^{tree} (both repositories), wc corpus, narrow Intl path lookup'], note='Read-only shell commands before local logging initialized; no parsed corpus marked read')
elif sys.argv[1]=='read':
    a,b=map(int,sys.argv[2:4]);lines,rows=records();assert 0<=a<=b<1028
    for n in range(a,b+1): print(str(n)+': '+lines[4+2*n])
    append('reading-ledger.jsonl',{'path':str(SOURCE.relative_to(REF)), 'unit_range':[a,b], 'line_range':[5+2*a,6+2*b],'sha256':sha(SOURCE.read_bytes()),'review_extent':'semantic_display','method':'every unique key/body in contiguous numbered range displayed; byte-identical translation copy deduplicated; acceptance separate'})
    event('display_contiguous_corpus',unit_range=[a,b],line_range=[5+2*a,6+2*b])
elif sys.argv[1]=='accept':
    a,b=map(int,sys.argv[2:4]);note=sys.argv[4];rows=json.loads((OUT/'reviewed-records.json').read_text())
    for n in range(a,b+1):
        rows[n].update({'semantic_status':'semantic_read','consumer':'species entry display localization; MessageTypes.POKEDEX_ENTRIES domain 3; hash lookup with original-text fallback','source_traceability':['Data/Scripts/010_Data/002_PBS data/008_Species.rb:238-241','Data/Scripts/001_Technical/003_Intl_Messages.rb:481-489','Data/Scripts/001_Technical/003_Intl_Messages.rb:600-610'],'formal_mapping':['deliverables/final-specification-set/generic-kernel/wp08-localization.md:25 (section 3.1)','deliverables/final-specification-set/generic-kernel/wp08-localization.md:30 (section 3.2)','deliverables/final-specification-set/generic-kernel/wp08-localization.md:51 (section 5.1)','deliverables/final-specification-set/generic-kernel/wp08-localization.md:61 (section 5.2)','deliverables/final-specification-set/generic-kernel/wp08-localization.md:113 (section 6.2)'],'semantic_result':'plain species/form lore text; no executable mechanics requirement inferred','review_note':note})
    status(rows)
    append('reading-ledger.jsonl',{'path':str(SOURCE.relative_to(REF)),'unit_range':[a,b],'line_range':[5+2*a,6+2*b],'review_extent':'semantic_read','method':'manual semantic acceptance after complete contiguous range display; no parsing-as-reading claim','note':note})
    event('manual_semantic_acceptance',unit_range=[a,b],semantic_read=sum(r['semantic_status']=='semantic_read' for r in rows))
elif sys.argv[1]=='source':
    path=sys.argv[2];a,b=map(int,sys.argv[3:5]);p=ROOT/path;raw=p.read_bytes();lines=raw.decode('utf-8-sig').splitlines();assert 1<=a<=b<=len(lines)
    print('\n'.join(f'{i+1}: {lines[i]}' for i in range(a-1,b)))
    append('reading-ledger.jsonl',{'path':path,'line_range':[a,b],'sha256':sha(raw),'review_extent':'semantic_display','method':'contiguous complete displayed range'})
    event('display_source_or_formal_range',path=path,line_range=[a,b],sha256=sha(raw))
