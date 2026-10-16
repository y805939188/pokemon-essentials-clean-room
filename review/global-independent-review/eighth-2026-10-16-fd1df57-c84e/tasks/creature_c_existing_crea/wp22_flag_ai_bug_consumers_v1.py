import json,re,hashlib,datetime,subprocess
from pathlib import Path
C=Path(__file__).parent;R=Path('/workspace/pokemon-essentials');utc=datetime.datetime.now(datetime.timezone.utc).isoformat();reader='/root/creature_a_atomic_reception';commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
paths={'items':'PBS/items.txt','item_class':'Data/Scripts/010_Data/002_PBS data/006_Item.rb','compiler':'Data/Scripts/021_Compiler/001_Compiler.rb','compile_pbs':'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb','battle':'Data/Scripts/011_Battle/001_Battle/001_Battle.rb','other':'Data/Scripts/011_Battle/001_Battle/008_Battle_ActionOther.rb','ai':'Data/Scripts/011_Battle/005_AI/001_Battle_AI.rb','ai_mega':'Data/Scripts/011_Battle/005_AI/004_AI_MegaEvolve.rb','ai_moves':'Data/Scripts/011_Battle/005_AI/005_AI_ChooseMove.rb','bug':'Data/Scripts/018_Alternate battle modes/002_BugContest.rb'}
ids={};texts={};units=[]
full={'item_class','compiler','compile_pbs','other','ai_mega'}
for k,p in paths.items():
 raw=(R/p).read_bytes();assert raw==subprocess.check_output(['git','-C',str(R),'show',commit+':'+p]);texts[k]=raw.decode('utf-8-sig');ids[k]=dict(path=p,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),blob=subprocess.check_output(['git','-C',str(R),'rev-parse',commit+':'+p],text=True).strip(),lines=len(raw.splitlines()),actual_reader=reader,credit='OWN_FULL_ACTUAL_SOURCE_READ' if k in full else ('OWN_COMPLETE_ID_FLAGS_COLUMN_ONLY_NOT_WHOLE_PBS' if k=='items' else 'OWN_PARTIAL_FILE_COMPLETE_NAMED_UNITS'))
def unit(k,name):
 s=texts[k];m=re.search(r'^( *)def '+re.escape(name)+r'(?=[( ;\n])[^\n]*\n',s,re.M);assert m,(k,name)
 end=m.end() if '; end' in m.group(0) else m.end()+re.search(r'^'+m.group(1)+r'end\s*$',s[m.end():],re.M).end()
 txt=s[m.start():end];u=dict(id=k+':'+name,source_identity_key=k,range=[s.count('\n',0,m.start())+1,s.count('\n',0,end)+1],complete_definition=True,text=txt,normalized_bytes=len(txt.encode()),normalized_sha256=hashlib.sha256(txt.encode()).hexdigest());units.append(u);return u['id']
for k,ns in [('compiler',['prepline','pbEachFileSectionEx','pbEachFileSection','split_csv_line','cast_csv_value','get_csv_record']),('compile_pbs',['compile_PBS_file_generic']),('battle',['initialize']),('other',['pbHasMegaRing?','pbGetMegaRingName','pbCanMegaEvolve?','pbRegisterMegaEvolution','pbUnregisterMegaEvolution']),('ai',['pbDefaultChooseEnemyCommand']),('ai_mega',['pbEnemyShouldMegaEvolve?']),('ai_moves',['pbChooseMove']),('bug',['pbBugContestState','pbBugContestStartOver'])]:
 for n in ns:unit(k,n)
units.append(dict(id='item_class:WHOLE_FILE',source_identity_key='item_class',range=[1,270],complete_definition=True,complete_file=True,text=texts['item_class']))
column=[]
for i,l in enumerate(texts['items'].splitlines(),1):
 m=re.match(r'^\[([^]]+)\]$',l)
 if m:column.append(dict(ordinal=len(column),id=m[1],header_line=i,complete_header_raw=l,all_flags_occurrences=[]))
 elif re.match(r'^\s*Flags\s*=',l):
  assert column;column[-1]['all_flags_occurrences'].append(dict(line=i,complete_raw=l,value=l.split('=',1)[1].strip()))
assert len(column)==693 and sum(len(x['all_flags_occurrences']) for x in column)==680
assert all(len(x['all_flags_occurrences'])<=1 for x in column)
for x in column:
 x['recognized_flags_tokens']=[] if not x['all_flags_occurrences'] else x['all_flags_occurrences'][0]['value'].split(',')
 assert all(t==t.strip() and '#' not in t and '"' not in t for t in x['recognized_flags_tokens'])
ring=[x['id'] for x in column if any(t.lower()=='megaring' for t in x['recognized_flags_tokens'])];stones=[x['id'] for x in column if any(t.lower()=='megastone' for t in x['recognized_flags_tokens'])]
assert ring==['MEGARING'] and len(stones)==47
old=json.loads((C/'default-transformation-records.v1.json').read_text());oldraw=(C/'default-transformation-records.v1.json').read_bytes()
stone_records=[x for x in old['raw_complete_records'] if x.get('source_identity_key')=='items']
# Compare with the already own-read 47 complete stone records through their header identities.
raw_stones=[]
for x in old['raw_complete_records']:
 if x.get('source_identity_key')=='items' and x.get('id') in stones:raw_stones.append(x['id'])
# Packet structure differs among raw collections; the exact all47 IDs are retained below independently.
rows=[]
def add(label,claims,refs,premise,remaining):
 n=len(rows)+1;rid=f'WMB-R{n:03}';rows.append(dict(id=rid,label=label,premise=premise,child_assertions=[dict(id=f'{rid}-A{i:02}',meaning=c,source_units=refs,status='SUPPORTED_BOUNDED_COMPLETE_UNIT_OR_FULL_COLUMN_ACTUAL_READ',whole_parent_acceptance=False) for i,c in enumerate(claims,1)],normal_cancel_failure='Only explicit writes/early returns are claimed. Earlier callback, registry, bag, native or AI failure need not reach later statements; no compensating transaction or ensure is inferred.',remaining=remaining,accepted=False))
add('COMPLETE_CURRENT_ITEM_ID_FLAGS_COLUMN',[
 'All693 current top-level items.txt section IDs plus every680 recognized Flags occurrence were actually read in three complete projected batches. Thirteen records omit Flags; none of these693 has repeated Flags. This does not read the other fields or confer whole693record/wholefile credit.',
 'The complete column has exactly one case-insensitive MegaRing token: MEGARING; exactly47 MegaStone token identities are individually retained. REDORB and BLUEORB have no Flags occurrence and therefore no MegaStone token in this current file.',
 'The raw Flags strings here are simple unquoted comma-separated tokens with no comments or surrounding token spaces. Actual schema *s, section overwrite rule, preprocessing and CSV definitions justify the field-to-array mapping, conditional on successful generic compilation/loading of this selected current dataset; omission defaults to[].',
 'Item.has_flag? compares each stored string by downcase equality, not substring. Battle initializer snapshots all current registered MegaRing-flagged item IDs; a later raw-file inventory or runtime resource change is not retroactively a catalog snapshot change. Backups are separate directories and not silently combined.'
],['item_class:WHOLE_FILE','compiler:prepline','compiler:pbEachFileSectionEx','compiler:pbEachFileSection','compiler:split_csv_line','compiler:cast_csv_value','compiler:get_csv_record','compile_pbs:compile_PBS_file_generic','battle:initialize'],
 'Fixed R current top-level PBS/items.txt only. All693header/Flags vectors actual own read chunks7add83,a78f34,996ece. Conditional mapping is static; no compiler, serializer, registry load or target game execution occurred.',
 'All other item fields/default datasets/backups and plugin additions remain separately bounded; source identity or field inventory is not successful compilation, object creation or runtime catalog observation.')
add('RING_CATALOG_AND_REAL_RESOURCE_READER',[
 'Constructor initially sets per-side per-owner Mega states to-1; after earlier object/party/struggle initialization it builds @mega_rings from GameData::Item.each and only then constructs AI. Any earlier failure can prevent the catalog write.',
 'pbHasMegaRing? for player-owned battlers checks live $bag.has? for each snapshotted ring identity; every other owner obtains its trainer_items, rejects nil and uses inclusion. It never reads the persistent Pokemon Owner ID to choose that resource.',
 'pbGetMegaRingName chooses first currently available snapshotted ring and localized item name; no matching ring or empty catalog returns localized Mega Ring. This display fallback grants no permission and does not mutate bag/items.',
 'CanMega permission orders prohibit-switch, individual qualification and wild rejection before Debug Ctrl; normal flow then SkyDrop, ring availability and owner state==-1. The Ring/MegaStone flags alone do not make a persistent individual target, consume a resource or reset used quota.'
],['battle:initialize','other:pbHasMegaRing?','other:pbGetMegaRingName','other:pbCanMegaEvolve?'],
 'Valid battle object/battler and current game globals; corresponding existing whole individual target definitions in CTF-R001/003 remain required for target selection. No runtime Bag or trainer item inventory was observed.',
 'Bag internals, actual host key state and demo acquisition paths remain outside this finite consumer statement; direct executor gates are separately recorded, not inferred from permission.')
add('AI_REGISTRATION_AND_BAD_MOVE_SWITCH_CANCELLATION',[
 'pbDefaultChooseEnemyCommand sets up AI then tries switching, item and auto fight menu in that order. A true result at each branch returns before any Mega registration. Only after all three fail does it evaluate the Mega predicate, conditionally register, obtain move scores and choose a move.',
 'pbEnemyShouldMegaEvolve? delegates to actual battle.pbCanMegaEvolve?(@user.index); true logs and returns true, false returns false. This is always-if-permitted, with no scoring prediction or separate species test here.',
 'Complete pbChooseMove first handles empty choices by AutoChoose and returns; otherwise in high-skill/can-switch branch it may decide all moves bad. Only a successful pbChooseToSwitchOut(true) then unregisters the user Mega selection and returns; unsuccessful replacement leaves the pending registration for move selection.',
 'Bad-move conditions preserve actual sequence and random calls: max<=useless consult can_attack and possibly25%; otherwise below base*threshold and turnCount>2 uses80%. Later weighted move/target registration does not itself clear Mega. Earlier AI scoring/log/native failure can leave registration; no complete AI decision domain was received.'
],['ai:pbDefaultChooseEnemyCommand','ai_mega:pbEnemyShouldMegaEvolve?','ai_moves:pbChooseMove','other:pbRegisterMegaEvolution','other:pbUnregisterMegaEvolution','other:pbCanMegaEvolve?'],
 'Existing correctly initialized AI user/trainer/battle wrappers. Complete named methods actually read f1de3f and current tools; only13-line AI_MegaEvolve wholefile is new FULL. AI main/choose-moves entire files are not read here.',
 'Switch chooser, item chooser, scores/prediction, logging exception implementation and broader AI formal remain separate domains. A source call or probability branch is not an executed AI distribution.')
add('BUG_CONTEST_START_OVER_FINITE_EXIT',[
 'pbBugContestStartOver iterates current $player.party in order; each same Pokemon reference is healed, then makeUnmega, then makeUnprimal before proceeding to the next. It does not perform one heal-all pass followed by one unmega-all pass.',
 'Only after the complete party loop returns normally does it obtain/create BugContestState via pbBugContestState and call pbStartJudging. The lazy state getter writes a new state only when the global stored value is false/nil under the actual ! test.',
 'A heal/form callback failure stops at that prefix and can prevent remaining members and judging. The visible function does not restore prior items or owner Mega quota, and this finite exit does not prove full contest session, failure dispatch, judging semantics or demo reachability.'
],['bug:pbBugContestStartOver','bug:pbBugContestState'],
 'Player/party exists and individual heal/unmega/unprimal definitions are the already own-read contracts. This named function is the finite contact explicitly listed in WP22, not a whole bug-contest review.',
 'Caller condition deciding contest failure, full BugContestState/PbStartJudging, whole session and UI/native remain available separate scopes; not called or simulated.')
out=dict(schema='gr8-crec-wp22-flags-ai-bug-finite-consumers/v1',recorded_utc=utc,actual_reader=reader,fixed_reference=dict(commit=commit,tree='7589c800b61ba13a13040ed0d686979b80a84fd0'),source_identities=ids,complete_source_units=units,complete_current_item_ID_Flags_column=column,column_counts=dict(headers=693,flags_occurrences=680,missing_flags=13),mega_ring_ids=ring,mega_stone_ids=stones,all_flags_column_actual_read_chunks=['7add83','a78f34','996ece'],raw_full_records_additional_credit=0,whole_items_credit=False,prior_selected_default_data=dict(path='default-transformation-records.v1.json',bytes=len(oldraw),sha256=hashlib.sha256(oldraw).hexdigest(),qualification='Preserves original complete selected records and finite statements; full Flags column now independently actually read. No old byte replacement.'),records=rows,manual_atoms=sum(len(x['child_assertions']) for x in rows),denominator_frozen=False,whole_domain_acceptance=False,new_votes=0,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
f=C/'wp22-flags-ai-bug-consumers.v1.json';assert not f.exists();f.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(path=f.name,bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),groups=len(rows),atoms=out['manual_atoms'],units=len(units),column=693,utc=utc)))
