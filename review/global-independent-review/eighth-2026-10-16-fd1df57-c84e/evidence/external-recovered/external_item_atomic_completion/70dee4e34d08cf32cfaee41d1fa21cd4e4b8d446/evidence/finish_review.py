"""Assemble auditable projections of the completed finite reading.
No reference/game/model behavior is executed. Files stay in this task directory.
"""
exec(compile((__import__('pathlib').Path(__file__).parent/'build_review.py').read_text(),'build_review.py','exec'))

now=datetime.datetime.now(datetime.timezone.utc).isoformat()
readset=json.loads((ROOT/REPORT/'delegation/readsets/external_item_atomic_completion.complete.json').read_text())
ids=[]
def identity(repo,path,commit,purpose):
    x=ident(repo,path,commit); x['purpose']=purpose;ids.append(x);return x
for path in [PRIMARY,HELPER,BATTLER,STAGE,TRIGGER,CALC,'Data/Scripts/003_Game processing/005_Event_Handlers.rb','Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb','Data/Scripts/011_Battle/002_Battler/004_Battler_Statuses.rb','Data/Scripts/011_Battle/001_Battle/001_Battle.rb','Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb','Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb','Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb','Data/Scripts/011_Battle/001_Battle/007_Battle_ActionRunning.rb','Data/Scripts/011_Battle/001_Battle/010_Battle_AttackPhase.rb','Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb','Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb','Data/Scripts/011_Battle/003_Move/011_MoveEffects_Items.rb','Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb','Data/Scripts/011_Battle/005_AI/011_AIMove.rb','Data/Scripts/011_Battle/005_AI/010_AIBattler.rb','Data/Scripts/011_Battle/005_AI/002_AI_Switch.rb','Data/Scripts/011_Battle/006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb','Data/Scripts/010_Data/001_Hardcoded data/008_Stat.rb','Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb','Data/Scripts/010_Data/002_PBS data/006_Item.rb','Data/Scripts/010_Data/002_PBS data/008_Species.rb','Data/Scripts/010_Data/001_GameData.rb','Data/Scripts/014_Pokemon/001_Pokemon.rb','Data/Scripts/021_Compiler/001_Compiler.rb','Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb','Data/Scripts/002_BattleSettings.rb','Data/Scripts/001_Settings.rb']:
    identity(REF,path,R,'PRIMARY_FULL' if path==PRIMARY else 'FINITE_COMPLETE_DEFINITIONS_OR_PROVIDER_OBJECTS_ONLY; whole file identity is not whole reading')
for path in [MAIN,COVER,CAT1,CAT2]:identity(ROOT,path,B8,'PRIMARY_FULL' if path in [MAIN,COVER] else 'SHARED_CATALOG_FULL_READ; foreign source domains not thereby approved')
for path in ['deliverables/final-specification-set/generic-kernel/wp05-events-extensions-plugins.md','deliverables/final-specification-set/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md','deliverables/final-specification-set/pokemon-rules/wp43-types-accuracy-and-damage.md']:identity(ROOT,path,B8,'FINITE_OPERATIVE_CLAUSES_ONLY')
for path in ['AGENTS.md',f'{REPORT}/inputs/eighth-global-review-prompt.md',f'{REPORT}/inputs/review-SKILL.md',f'{REPORT}/delegation/prompts/external_item_atomic_completion.md',f'{REPORT}/delegation/readsets/external_item_atomic_completion.complete.json',f'{REPORT}/delegation/external-cross-domain-reception.current.json']:
    identity(ROOT,path,CONTRACT,'FULL_CONTRACT_READ' if not path.endswith('current.json') else 'FINITE_APPLICABLE_ROUTE_AND_COMMON_PREMISE_READ; other routes not adopted')
for entry in readset['reference']+readset['formal']+readset['shared_catalogs']:
    a=next(x for x in ids if x['path']==entry['path'])
    assert a['bytes']==entry['bytes'] and a['sha256']==entry['sha256'] and a['blob']==entry['git_blob']
for record in (OUT/'evidence/read-operations.ndjson').read_text().splitlines():
    record=json.loads(record)
    if record['repo']==str(REF) and record['path'] not in {a['path'] for a in ids}:
        identity(REF,record['path'],R,'FINITE_LOGGED_RANGE_ONLY; not whole-file reading')

# Recover the complete original input objects; preserve original readers and
# distinguish parse/full-byte recovery from this context's finite meaning read.
oldmanifest=json.loads((ROOT/REPORT/'tasks/com_ability_item/delivery-manifest.json').read_text())
old={}; recovery=[]
for name in ['source-facts.json','forward-mapping.json','reverse-mapping.json','reading-ledger.json','received-contributions.json','interfaces.json']:
    binding=next(e for e in oldmanifest['files'] if e['path']==name)
    raw=subprocess.check_output(['git','-C',str(ROOT),'cat-file','blob',binding['content_git_blob']])
    assert len(raw)==binding['bytes'] and hashlib.sha256(raw).hexdigest()==binding['sha256']
    x=json.loads(raw);old[name]=x
    archive=f'evidence/compressed/{binding["sha256"]}.gz'
    physical=ROOT/REPORT/'tasks/com_ability_item'/name
    transport='original path' if physical.exists() else archive
    if not physical.exists():assert gzip.decompress((ROOT/REPORT/archive).read_bytes())==raw
    recovery.append(dict(original_path=f'tasks/com_ability_item/{name}',original_reader='/root/com_ability_item',source_reader='/root/com_move',fixed_transport_commit=CONTRACT,transport=transport,bytes=len(raw),sha256=binding['sha256'],blob=binding['content_git_blob'],full_bytes_recovered=True,full_structure_parsed=True,semantic_credit='Finite item family/caller/operative joins actually received; unrelated ability domain remains with its original primary. No inherited ALL_CONCRETE or old sentence-split atom credit.'))
old_item=[u for u in old['source-facts.json']['identity_units'] if u['id'].startswith('ItemEffects:')]
assert len(old_item)==196
assert old['forward-mapping.json']['source_unit_fact_rows']==old['source-facts.json']['identity_units']
dump('evidence/old-evidence-recovery.json',dict(schema='gr8-old-item-evidence-recovery/v1',inputs=recovery,exact_source_facts_forward_duplicate=True,original_pair_count=463,item_pair_count=196,old_formal_rows=441,old_sentence_locators=1479,qualification='Old two-reference/four-formal attestations and source reader facts remain intact. This new task has exactly one fresh primary source/two formal files; it does not erase or duplicate the old scope.',old_item_association=[dict(id=u['id'],source_range=u['source_range'],old_formal_lines=[a['line'] for a in u.get('concrete_formal_assertions',[])],new_handler_id='H-'+u['family']+'-'+u['identity']) for u in old_item]))

# A finite data projection: whole selected current records were read; backups
# receive only the complete necessary field values, never whole-file credit.
itemnames={u['item'] for u in units}; projections=[]
for path in ['PBS/items.txt',*[f'PBS/Gen {i} backup/items.txt' for i in range(5,9)],'PBS/Shadow Pokémon backup/items_shadow_pkmn.txt']:
    ident0=identity(REF,path,R,'Selected held-handler identity/Flags/Name/use/consumable fields; not every PBS record')
    data=(REF/path).read_text(encoding='utf-8-sig');records=[]
    for m in re.finditer(r'^\[([^]]+)\]\r?\n(.*?)(?=^\[|\Z)',data,re.M|re.S):
        if m[1] not in itemnames:continue
        vals={k:v for k,v in re.findall(r'^([A-Za-z]+)\s*=\s*(.*)$',m[2],re.M)}
        records.append(dict(id=m[1],range=[data[:m.start()].count('\n')+1,data[:m.end()].count('\n')],fields={k:vals.get(k) for k in ['Name','Flags','FieldUse','BattleUse','Consumable']},meaning='Berry/TypeGem full case-insensitive flag matching; omitted use fields initialize0, omitted consumable follows importance. Passive consumption follows the actual callback rather than a universal consumable flag.'))
    projections.append(dict(identity=ident0,records=records,missing=sorted(itemnames-{x['id'] for x in records}),activation='Default discovery is top-level PBS/*.txt; backup subdirectories require explicit valid replacement/selection and recompilation, not automatic concurrent activation.'))
dump('evidence/data-reception.json',dict(schema='gr8-finite-item-data-reception/v1',paths=projections,default_selected_records=len(projections[0]['records']),default_absent=['STICK'],STICK='The fixed registry copy definition is actually read even though default Item data lacks STICK. Gen5/6/7 backups contain it; Gen8 matches current fields. This does not invalidate the copy definition or establish a default attainable STICK holder.',original_peer_reader='/root/creature_b and /root/pbs_battle retain their whole-record duties',mandatory_schema_companion=dict(sha256='708d62e93db2e05400d442be3da03219250e7ec6f2bac11fa0b0ce5108cfe3a7',transport=f'{REPORT}/evidence/compressed/708d62e93db2e05400d442be3da03219250e7ec6f2bac11fa0b0ce5108cfe3a7.gz',meaning='Read complete corrected Pocket positive-v, Price unsigned-u and use inline enums; original overbroad unsigned wording not adopted.'),execution='NOT_EXECUTED'))

# Complete primary reverse view. Meaning atoms are manual; retaining a line
# locator does not make a paragraph or registry row a semantic atom.
exec(compile((OUT/'evidence/finite_body_reception.py').read_text(),'finite_body_reception.py','exec'))
line_atoms=collections.defaultdict(list)
for a in atoms:
    for op in a['operative']:line_atoms[(op['path'],op['line'])].append(a['id'])
extra={
 3:('Scope and fixed counts',[]),7:('Observable outputs and separation of calculation/trigger/consumption',['G-CONSUME','G-HP']),
 9:('Field aliases and explicit finite central dependencies',['G-CONSUME','G-HP','G-STAGE','G-REWARD']),
 11:('Current identity/active-item/species premises',['G-ACTIVE']),
 17:('Speed/weight actual consumer order',['G-ACTIVE']),18:('Accuracy containers and ordering',['G-MOVE-HIT']),19:('Damage slots and ordering',['G-MOVE-HIT']),20:('Critical early veto and empty target family',['E-CriticalCalcFromTarget']),
 21:('HP/status/end-move/forced ordered entry',['G-ENTRY']),22:('Per-hit actual caller',['G-MOVE-HIT']),23:('After-move actual caller',['G-MOVE-HIT']),24:('Stat-drop actual caller',['G-ENTRY']),25:('Round-end actual caller',['G-EOR']),26:('Terrain/entry/Intimidate actual caller',['G-ENTRY','G-FIELD']),27:('Reward actual callers',['G-REWARD']),
 29:('Triggered suffix and foreign-item distinction',['G-CONSUME']),31:('Records, removal, recursion and restoration conditions',['G-CONSUME']),
 53:('Ordinary accuracy integer threshold and critical earlier veto',['G-PRIORITY']),57:('P/A/D/F slot meanings',['G-MOVE-HIT']),74:('Berry and pinch modes',['G-PINCH']),
 88:('Mental/White Herb distinct direct writes',['H-StatusCure-MENTALHERB','H-OnEndOfUsingMoveStatRestore-WHITEHERB']),
 90:('Disable counter vs identity and later gates',['H-StatusCure-MENTALHERB']),94:('Active stock vs passive records and integer Sitrus amount',['G-CONSUME']),
 100:('Per-hit shared premises',['G-MOVE-HIT']),113:('Forced positive berries retain local eligibility',['G-ENTRY']),
 117:('NaturalGift/Jaboca/Oran ordinary chain',['G-U04','H-OnBeingHit-JABOCABERRY','H-HPHeal-ORANBERRY']),119:('Committed C/I/R/P/Belch prefix before later nil failure',['G-U04','G-CONSUME']),121:('High-HP and single-hit independent controls',['G-U04','G-CONSUME']),123:('Conditional normal terminal restoration and AI separation',['G-U04']),
 155:('Direct-core registry-external routing',[]),159:('FocusSash/Band own WP43 primary',[]),160:('KingsRock/RazorFang finite WP43 flinch interface',[]),161:('Command selection gates remain with WP40',[]),162:('Ground/type core gates remain with WP43',[]),163:('Contact/powder/weather gates remain with core',[]),164:('Root/binding/wall/power-herb direct definitions remain with their primaries',[]),165:('Attract/reflection primary remains WP44',[]),166:('Entry hazards primary remains field rules',[]),167:('ExpShare/money/world primary remains growth/results',[]),169:('Configuration/default data, registry empty families and direct definitions',['G-REGISTRY']),
 173:('Existing static-vector catalog and common assumptions',[]),175:('Additional HI34/35/36 fixture qualifications',[]),179:('Cross-domain/history acceptance language',[]),180:('Static boundary and retained global combinations',[]),181:('Historical WP50-R01 CLOSED qualifier',[])}
reverse=[]
for path in [MAIN,COVER]:
    for n,line in enumerate((ROOT/path).read_text().splitlines(),1):
        if not line.strip() or line.startswith(('#','| ---')):continue
        aid=list(line_atoms[(path,n)])
        category='OPERATIVE_BODY'
        meaning=extra.get(n,('Current body clause',[]))[0] if path==MAIN else 'Identity/parameter table; operative behavior remains in main body'
        group_refs=extra.get(n,('',[]))[1] if path==MAIN else []
        if path==MAIN and n in finite_by_line:category='FINITE_FOREIGN_OPERATIVE_JOIN_RECEIVED'
        if path==MAIN and n in [179,181]:category='HISTORICAL_QUALIFICATION_NOT_REAPPROVED'
        if path==MAIN and n in [3,7,9,53,57,94,113,155,169,173,175,180]:category='COMMON_PREMISE_OR_SCOPE' if not aid else 'OPERATIVE_WITH_COMMON_PREMISES'
        if line.startswith('|') and all(x in ['',' '] for x in line.replace('|','')):continue
        if path==COVER:
            first=line.split('|')[1].strip() if line.startswith('|') else ''
            family=re.match(r'(\w+)（\d+）',first)
            item_tokens=set(re.findall(r'(?<![A-Z0-9_])[A-Z][A-Z0-9_]*(?![A-Z0-9_])',line))
            matching=[u for u in units if u['family']==family[1]] if family else [u for u in units if u['item'] in item_tokens] if 50<=n<=67 else []
            aid=list(dict.fromkeys(z for u in matching for z in u['atom_ids']))
            group_refs=list(dict.fromkeys(z for u in matching for z in u['shared_semantic_groups']))
            category='IDENTITY_AND_PARAMETER_CORROBORATION_ONLY'
        if (path==MAIN and n in [15,37,76,102,136,157]) or (path==COVER and n in [9,48]):category='TABLE_SCHEMA_READ'
        reverse.append(dict(id=f'R-{Path(path).stem}-{n:03d}',path=path,line=n,full_current_clause=line,meaning_class=category,manual_supporting_atoms=aid,required_group_support=group_refs,manual_clause_role=meaning,disposition=('READ_NOT_INHERITED; current historical acceptance belongs root/history' if category=='HISTORICAL_QUALIFICATION_NOT_REAPPROVED' else 'READ_FINITE_BOUNDARY_PRESERVED; no new whole foreign domain approval' if category=='FINITE_FOREIGN_PRIMARY_ROUTING' else 'READ_AND_CHECKED_WITH_ACTUAL_SOURCE_AND_COMMON_PREMISES'),execution='NOT_EXECUTED'))
        if path==MAIN and n in finite_by_line:reverse[-1]['finite_complete_receipt']=dict(path='evidence/finite-body-reception.json',id=finite_by_line[n])
        if path==MAIN and n in [173,175]:reverse[-1]['complete_fixture_reception']='evidence/catalog-reception.json; entire shared text actually read; finite item controls only'
        if path==MAIN and n==180:reverse[-1]['required_group_support']=['G-HP','H-OnEndOfUsingMove-LEPPABERRY']
        if path==MAIN and n==181:
            reverse[-1]['required_group_support']=['G-CONFUSION','G-PINCH','G-CONSUME','G-STATBERRY']
            reverse[-1]['qualification_split']='Current gameplay clauses freshly checked with these full groups; only the parenthetic historical CLOSED acceptance is not reapproved.'
dump('reverse-mapping.json',dict(schema='gr8-manual-primary-reverse/v1',rows=reverse,assertion_store='evidence/semantic-atoms.json.gz',qualification='Manual behavioral assertions are independently authored in the decoded store. Rows are locators, not the meaning denominator. Registry table corroboration cannot replace operative body support. Historical acceptance clauses explicitly unadopted.',primary_unread_ranges=[],current_historical_status_not_reapproved=[179,181]))

# Exact published input identities for finite peer objects actually read.
peer_specs=[('tasks/com_ability_item/received-contributions.json','/root/com_move','Source contribution ItemEffects/ItemStatuses/ItemHit/Battler006/Rewards/ActiveSitrus/Running complete objects and Battler contribution finite facts; unrelated ability domain not adopted'),('tasks/com_ability_item/interfaces.json','/root/com_ability_item','Complete old interface object, historical receipt preserved rather than inherited'),('tasks/com_ai/interfaces.json','/root/com_ai','IF-COMAI-ABILITY-ITEM-CALLBACKS, IF-COMAI-ACTIVE-SITRUS-FINITE and IF-COMAI-R7-U06-DIRECT-TAIL complete objects'),('coverage/root-active-snapshot-16/core_atomic_reception/ability-tuple-units.json.ndjson','/root/core_atomic_reception','All463 arrays actually displayed and parsed as9-field NDJSON; navigation only, not behavior atoms'),('coverage/root-active-snapshot-16/core_atomic_reception/ability-tuple-units.format-clarification.v1.json','/root/core_atomic_reception','Complete format clarification; original JSON Extra data failure retained'),('tasks/h_r7_final_receptions/history-current-acceptance.json','/root/h_r7_final_receptions','Only current_final_authority/shared_reception/retained_unknowns and selected full batch objects read; does not certify WP50-R01 exact old closure')]
peer=[]
for path,reader,scope in peer_specs:
    x=identity(ROOT,f'{REPORT}/{path}',CONTRACT,'FINITE_PEER_OBJECT_RECEPTION');peer.append(dict(identity=x,original_reader=reader,actual_receiving_context='/root (delegated external_item_atomic_completion)',received_scope=scope,not_full_foreign_domain=True))
interface_entries=[
 dict(id='I-CORE',provider='Original /root/com_move; central/core authors preserved',status='FINITE_RECEIVED_AND_NECESSARY_SOURCE_REREAD',scope='Central activity/HP/status/stage/records/consume/symbiosis, priority, rewards, field, actual hit/after-move/round-end/switch/run joins',evidence=['evidence/semantic-atoms.json.gz','evidence/read-operations.ndjson','evidence/old-evidence-recovery.json']),
 dict(id='I-MOVE',provider='/root/com_move and /root/com_move/attributes_calling',status='FINITE_RECEIVED_AND_NECESSARY_SOURCE_REREAD',scope='Per-hit current identity, resist berry deferred removal, gem marker/deferred removal, explicit forced consumer distinctions, NatGift/JABO/ORAN prefix; no whole MOVE re-review',evidence=['evidence/semantic-atoms.json.gz','evidence/old-evidence-recovery.json','evidence/read-operations.ndjson']),
 dict(id='I-AI',provider='/root/com_ai; source /root/com_move',status='FINITE_COMPLETE_OBJECTS_RECEIVED',scope='AI real callback invocation vs valuation/rough replacement, no target berry callback, gem marker clear, ZoomLens approximation, empty target-critical default; no real consumption simulation',evidence=['evidence/peer-reception.json']),
 dict(id='I-KERNEL',provider='Handler source personally read; original kernel owner retained',status='FINITE_SOURCE_AND_OPERATIVE_CLAUSE_RECEIVED',scope='Symbol/id normalization, exact/conditional/copy/defaults, compile selected item data clear/register/save/load and nonrecursive PBS discovery. No compiler-wide or arbitrary-plugin approval',evidence=['evidence/semantic-atoms.json.gz','evidence/data-reception.json','evidence/read-operations.ndjson']),
 dict(id='I-DATA',provider='Current selected original records personally read; original /root/creature_b and /root/pbs_battle retained',status='FINITE_NECESSARY_FIELDS_COMPLETE',scope='All180 registry names,179 selected default full records, necessary backup field values, corrected item schema, Nature/Stat and persistent identity/PP interface',evidence=['evidence/data-reception.json','evidence/read-operations.ndjson']),
 dict(id='I-ROOT',provider='Main reviewer',status='PENDING_INDEPENDENT_ROOT_RECEPTION',scope='Receive all this frozen task core/remote payload and decide cumulative global/foreign historical qualification. This is not a missing readable source body in this task.',blocks='Root final signoff only; not a reason to stop this task before publication',evidence=['next-dispatch.json']),
 dict(id='I-HISTORY-QUALIFICATION',provider='root/history',status='EXACT_OLD_QUALIFIER_NOT_RECEIVED',scope='WP50 main179/181 old bounded dependency PASS/WP50-R01 CLOSED remains read but not reapproved. The new item source/body review does not depend on inheriting it.',blocks='Adopting those historical status assertions and global closure only; no gameplay evidence deficit',evidence=['reverse-mapping.json','evidence/peer-reception.json'])]
dump('interfaces.json',dict(schema='gr8-item-finite-interfaces/v1',entries=interface_entries,finite_necessary_gameplay_joins_received=5,finite_necessary_gameplay_joins_unreceived=0,root_signoff_pending=1,old_status_qualifier_not_received=1,not_limits=['I-ROOT','I-HISTORY-QUALIFICATION'],no_foreign_full_credit=True,update_started=False))
dump('evidence/peer-reception.json',dict(schema='gr8-item-peer-reception/v1',objects=peer,rule='Original actual readers are retained; exact full selected objects/common premises received, not an entire foreign report based on a status/hash. Source re-reads are a separate ledger.',original_unknowns_preserved=['AbilityPBS whole-corpus receipt in the old task is not upgraded by this task.','Old two-reference/four-formal full reading attestations remain with their named readers.','No virtual context, second vote or independently executed counterreview is created.']))

catalog=[]
for path in [CAT1,CAT2]:
    for n,line in enumerate((ROOT/path).read_text().splitlines(),1):
        if not line.startswith('|') or line.startswith('| ---'):continue
        head=line.split('|')[1].strip()
        relevant=(path==CAT1 and (re.match(r'HI\d',head) or head.startswith('U04-HI'))) or (path==CAT2 and head=='I08')
        catalog.append(dict(path=path,line=n,id=head,disposition='FINITE_ITEM_FIXTURE_AND_COMMON_PREMISES_RECEIVED' if relevant else 'FULL_TEXT_READ_FOR_COMMON_PREMISES_AND_CONSISTENCY; primary source judgment remains foreign owner',execution='NOT_EXECUTED'))
dump('evidence/catalog-reception.json',dict(schema='gr8-item-full-catalog-reception/v1',files=[CAT1,CAT2],complete_lines=669,rows=catalog,scope='All full shared text read; only item-relevant fixtures and common premises adopted, no non-item effect approval.'))

# No counterreviewer is invented. These are proposal-search controls, not new
# mandatory findings or a global no-required-update decision.
controls=[
 ('NC01','Confusion berries only mapped to registry row','The new fresh assertion store explicitly maps each of five berry stat/taste identities to WP50:80 and all14 G-CONFUSION meanings, plus actual helper and Nature definitions. Gen6/7/8, H101, forced full HP, Ripen, normal/forced/OwnTempo/nature-for-stats distinctions were checked.','H100 h25 Gen8 Figy normal heals33 before eligible confusion; forced H100 h100 can heal0 and still return true. Gen7 request50, Gen6 request12.'),
 ('NC02','All berries share one Gluttony/Unnerve/forced gate','Refuted: false half-mode ORAN/SITRUS differs default pinch, forced bypass differs by handler, resist helper has no ordinary eating query.','H100 h50 ORAN10 succeeds without Gluttony; h51 rejects; Gen8 Figy at50 rejects without Gluttony; OCCA still reduces under opposing Unnerve.'),
 ('NC03','False return means no committed item change','Refuted by existing correct EJECTPACK rule and source.','Eligible EJECTPACK consumes before negative replacement result, returns false with item absent.'),
 ('NC04','No switch implies no REDCARD consumption','Refuted by current correct consume-before-SuctionCups/Ingrain body.','Eligible random replacement exists, attacker rooted: item consumed, no actual replacement.'),
 ('NC05','All alias counts prove all behavior','Refuted as an audit method. All31 destinations bind exact family copies and inherit resolved local facts plus shared premises; no automatic cross-family copy.','STICK has a copied critical definition but is absent in default item data; alternate activation is conditional.'),
 ('NC06','WhiteHerb uses central stat increase / Leppa respects usual move-ID sync','Refuted by current correct direct-stage and same-index PP exceptions.','WhiteHerb attack-2 becomes0 while Speed+3 stays; persistent X PP0 and transformed battle Y same slot both receive10 numerically.'),
 ('NC07','All query defaults are false or all callbacks consume','Refuted by wrappers and real consumers.','Speed/weight/critical retain input on nil; bracket0, EXP-1, EV registration boolean; notification nil can accompany container mutations.'),
 ('NC08','Every per-hit berry is suppressed by after-move SheerForce','Refuted by actual per-hit and after-move separation.','Kee/Maranga per-hit callback remains separate from SheerForce stage2/3; fainted target item allowance does not activate ordinary Ripen.'),
 ('NC09','Source no execution / host missing excuses unread definitions','Rejected as process. Entire primary1948 and operative formal252 plus full catalog669 actually read; source-derived facts are not runtime tests.','All behavior execution categories remain NOT_EXECUTED, independent of Python/Git/static-check exits.'),
 ('NC10','AI callback invocation guarantees pure read or actual consumption','Refuted by finite received AI packet and source.','GemConsumed is set by real helper and cleared by AI rough damage; target berries omitted; ZoomLens uses rough priority/speed; valuations do not consume held items.'),
]
dump('proposals.json',dict(schema='gr8-item-proposals/v1',proposals=[],new_proposal_count=0,accepted_required=0,accepted_optional=0,accepted_policy=0,new_no_required_records=0,negative_controls=[dict(id=i,hypothesis=h,reason=r,finite_control=v,evidence_level='SOURCE_STATIC / DERIVED_VECTOR',execution='NOT_EXECUTED') for i,h,r,v in controls],independent_counterreviewer=None,independent_status='No new finding was authored. Root must independently receive this finite no-new-proposal assessment; this context cannot give itself a second vote.',global_NO_REQUIRED_UPDATE=False,update_started=False))

# Preserve static scan result as search evidence, never as reading credit.
hits=[]
for path in sorted((REF/'Data/Scripts').rglob('*.rb')):
    for n,line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(),1):
        if re.search(r'Battle::ItemEffects::\w+\.(?:add|copy)\(',line):hits.append([str(path.relative_to(REF)),n])
dump('evidence/negative-registration-search.json',dict(schema='gr8-item-negative-registration-search/v1',scope='All fixed Data/Scripts/**/*.rb literal ItemEffects family add/copy starts',hits=hits,statement_count=len(hits),outside_primary=[h for h in hits if h[0]!=PRIMARY],qualification='Literal static search only; does not exclude unbounded dynamic registration. Exact family definitions were personally read, not inferred from this scan.'))
assert len(hits)==186 and not [h for h in hits if h[0]!=PRIMARY]

initial_reads=[(PRIMARY,[[1,360],[361,730],[731,1100],[1101,1500],[1501,1900],[1901,1948]],'R'),(MAIN,[[1,95],[96,181]],'B8'),(COVER,[[1,71]],'B8'),(CAT1,[[1,105],[106,215],[216,320]],'B8'),(CAT2,[[1,110],[111,230],[231,349]],'B8'),('AGENTS.md',[[1,297]],'CONTRACT'),(f'{REPORT}/inputs/eighth-global-review-prompt.md',[[1,115],[116,241]],'CONTRACT'),(f'{REPORT}/inputs/review-SKILL.md',[[1,51]],'CONTRACT')]
initial=[dict(path=p,ranges=r,ref=ref,actual_reader='current delegated context /root',status='FULL_ACTUAL_NONTRUNCATED_READ',qualification='Actual tool stream read. Earlier combined truncated output was not credited; explicit contiguous rereads supersede only lost display ranges.') for p,r,ref in initial_reads]
supplemental=[dict(path=HELPER,ranges=[[198,476]],status='FINITE_COMPLETE_ITEM_HELPERS_PERSONALLY_READ'),dict(path=BATTLER,ranges=[[20,145],[240,454],[586,707],[518,534]],status='FINITE_COMPLETE_UNITS_PERSONALLY_READ'),dict(path=STAGE,ranges=[[1,295]],status='FINITE_COMPLETE_RAISE_LOWER_CORE_PERSONALLY_READ; tail wrappers not whole-file credit'),dict(path=TRIGGER,ranges=[[1,218]],status='FULL_ACTUAL_READ'),dict(path=CALC,ranges=[[110,220],[280,395],[444,515]],status='FINITE_PERSONAL_READ; complete calculation envelope also finite provider received'),dict(path='Data/Scripts/011_Battle/005_AI/011_AIMove.rb',ranges=[[90,378],[433,548]],status='FINITE_PERSONAL_READ'),dict(path='Data/Scripts/003_Game processing/005_Event_Handlers.rb',ranges=[[97,205],[275,298]],status='FINITE_COMPLETE_REGISTRY_CLASSES_PERSONALLY_READ')]
dump('reading-ledger.json',dict(schema='gr8-item-reading-ledger/v1',utc=now,initial_complete_reads=initial,initial_finite_reads=supplemental,later_exact_read_operations='evidence/read-operations.ndjson',full_peer_objects='evidence/peer-reception.json',old_input_recovery='evidence/old-evidence-recovery.json',data_fields='evidence/data-reception.json',own_primary_read=dict(reference_files=1,source_lines=1948,formal_files=2,formal_lines=252,shared_catalog_files=2,shared_catalog_lines=669,source_unread=0,formal_unread=0,shared_unread=0),actual_reception=dict(necessary_gameplay_joins=5,unreceived_necessary_gameplay_joins=0,root_signoff_pending=1,exact_old_historical_qualifier_not_received=1),foreign_personal_unread='All foreign complete files outside listed full or finite ranges remain personally unread; no whole-file foreign credit. Their original primary ownership is unchanged and they are not added to this one-file primary.',not_material_limits=['Root independent acceptance','Exact historical status qualifier'],business_execution='NOT_EXECUTED',all_combinations_approved=False))
dump('identities.json',dict(schema='gr8-item-identities/v1',fixed=dict(contract_commit=CONTRACT,contract_tree=git(ROOT,'rev-parse',CONTRACT+'^{tree}'),B8=B8,B8_tree=git(ROOT,'rev-parse',B8+'^{tree}'),formal_tree=git(ROOT,'rev-parse',B8+':deliverables/final-specification-set'),R=R,R_tree=git(REF,'rev-parse',R+'^{tree}')),local_mapping=dict(cleanroom=str(ROOT),reference=str(REF),Mac_handoff_paths='NOT_PRESENT_IN_CLOUD; no claim that cloud is the Mac workspace'),payloads=ids,readset_identity_match=True,original_evidence_recovery='evidence/old-evidence-recovery.json',protected='Reference, formal/planning/audit, other task directories, main, tags and historical payloads unchanged.'))

failures=[dict(kind='TOOL_OUTPUT_TRUNCATION',events=['Combined skill/cross-domain/global prompt output43737 tokens','Broad cross-domain top-level dump18282 tokens','Combined old source facts/families/battler dump15821 tokens','Broad JSON rg accidentally matched long one-line objects','A few combined dependency navigation reads exceeded display budget'],disposition='No full-reading credit from truncated portions. Global contract/primary/catalog reread in complete windows; old finite item facts shown in compact full-object form; broad foreign navigation remains unadopted.'),dict(kind='MISSING_OR_WRONG_PATH',events=['Original large old maps/source-facts not materialized at task path: recovered exactly from fixed gzip and known blobs','Initial Stat basename wrong, then exact119-line file read','A few wrong working-directory source/formal paths returned not found','Nominal companion path absent: recovered by exact supplied hash gzip'],disposition='No missing-path output was treated as source evidence; recoveries bound to original exact bytes.'),dict(kind='RANGE_ERROR',events=['Stat request through121 exceeded actual119','Fling request through472 exceeded actual470','UsageCalculations request through540 exceeded actual515'],disposition='IndexError preserved as a failed read, then corrected/eof complete finite unit reads supplied.'),dict(kind='BOOKKEEPING_ERROR',events=['Initial registry-name parser included ItemEffects namespace prefix and failed on SpeedCalc I'],disposition='Corrected to inspect arguments only. Final enumeration165 add+31 destinations/21 copy statements; semantic rules were already manually authored and did not derive from that parser.'),dict(kind='GIT_TRANSPORT',events=['git ls-remote exit128 could not read Username','gh auth status exit0 still reported GH_TOKEN invalid'],disposition='Business/auth success not inferred from exit0. Connected GitHub read succeeded. Publication uses nonforce branch Git-data update if CLI push remains unavailable; exact remote receipt separately records actual protocol.')]
dump('evidence/io-boundary.json',dict(schema='gr8-item-io-boundary/v1',failures=failures,published_io='Exact read ranges, payload identities and recovered object identities plus static logs; full private platform stdout/stderr stream is not exported and is not claimed remotely recovered.',metadata_clock='Actual command UTC retained in read-operations/preflight; first private tool-stream timestamp not available and not backfilled.',execution=dict(reference='NOT_EXECUTED',Ruby='NOT_EXECUTED',independent_behavior_model='NOT_EXECUTED',native='NOT_EXECUTED',game='NOT_EXECUTED',real_save='NOT_EXECUTED',fault_injection='NOT_EXECUTED'),tools_used='Python text/JSON/gzip parsing, hashes and Git only; no reference eval, Marshal load or production IO.'))

# Compress losslessly once, avoiding megabytes of repeated exact clause text in
# visible indexes. Decoding requires no execution of any reviewed code.
raw=(OUT/'evidence/semantic-atoms.json').read_bytes()
packed=gzip.compress(raw,mtime=0)
(OUT/'evidence/semantic-atoms.json.gz').write_bytes(packed)
store=dict(path='evidence/semantic-atoms.json.gz',encoding='gzip / UTF-8 JSON',compressed_bytes=len(packed),compressed_sha256=hashlib.sha256(packed).hexdigest(),decoded_path='semantic-atoms.json',decoded_bytes=len(raw),decoded_sha256=hashlib.sha256(raw).hexdigest(),decoded_git_blob=git(ROOT,'hash-object','--stdin',input=raw),recovery='python3 -c "import gzip,json,pathlib; x=json.loads(gzip.decompress(pathlib.Path(\'evidence/semantic-atoms.json.gz\').read_bytes())); print(json.dumps(x,ensure_ascii=False,indent=2))"',meaning_count=len(atoms),groups=len(groups),handler_bindings=196)
(OUT/'evidence/semantic-atoms.json').unlink()
dump('forward-mapping.json',dict(schema='gr8-item-forward/v1',complete_assertions_and_handler_joins=store,structure=dict(premises='/premises',manual_assertions='/assertions',manual_control_groups='/groups',complete_handlers='/handler_units'),source_to_spec='Each assertion has precise fixed source range, current operative body line and additional finite operative clauses; each handler has all local and required shared atom groups plus exact actual callers. Copy bindings retain resolved original atoms and current family.',assertion_count=len(atoms),handler_count=196,empty_families=['CriticalCalcFromTarget','TrappingByTarget'],unmapped_primary_handlers=0,unread_primary_source_ranges=[],qualification='Registry rows corroborate identity only. Decode the full store for semantic review; this index/hash/count is not reception.',execution='NOT_EXECUTED'))
dump('evidence/decoded-payload-binding.json',store)

progress=json.loads((OUT/'progress.json').read_text());progress.update(utc=now,state='LOCAL_STATIC_COMPLETED_PUBLICATION_PENDING',source_full_read=[1,1948],formal_full_read=['WP50-main:1-181','WP50-coverage:1-71'],shared_catalog_full_read=['CAT1:1-320','CAT2:1-349'],manual_assertions=len(atoms),manual_groups=len(groups),handler_pairs=196,primary_unread=0,necessary_gameplay_interfaces_unreceived=0,historical_qualifier_not_received=1,root_final_acceptance='PENDING',publication='PENDING',update_started=False)
dump('progress.json',progress)
dump('validation.json',dict(schema='gr8-item-validation/v1',utc=now,state='LOCAL_STATIC_CONSISTENCY_CHECKED_REMOTE_PUBLICATION_PENDING',input_hash_checks='All primary and shared readset identities match exact bytes/SHA256/blob at fixed B8/R.',manual_assertions=len(atoms),handler_units=196,source_registration_statements=186,direct=165,copy_statements=21,copy_destinations=31,families=32,empty_families=2,primary_source_unread=0,formal_unread=0,shared_catalog_unread=0,necessary_gameplay_interfaces_unreceived=0,old_qualifier_unreceived=1,independent_root_reception='PENDING',remote_readback='PENDING; successor publication receipt must bind exact frozen core, every changed file and decoded payload',tool_success_not_business_success=True,behavior_execution='NOT_EXECUTED',limits=['Target-host/media/game/save behavior not executed','Unbounded plugins not exhausted','Actual model/effort/tier/speed/Fast/platform task ID UNVERIFIED'],update_started=False))
dump('next-dispatch.json',dict(schema='gr8-item-next-dispatch/v1',task='external_item_atomic_completion',action='Main reviewer independently receives this complete frozen finite item report and its lossless assertion payload, resolves the two existing historical qualification rows only within historical owner authority, and records cumulative acceptance.',input=dict(contract=CONTRACT,B8=B8,R=R,report=f'{REPORT}/tasks/external_item_atomic_completion/'),required_read=['review.md','progress.json','identities.json','reading-ledger.json','forward-mapping.json','reverse-mapping.json','interfaces.json','proposals.json','validation.json','next-dispatch.json','evidence/semantic-atoms.json.gz','evidence/data-reception.json','evidence/old-evidence-recovery.json','evidence/peer-reception.json','evidence/catalog-reception.json','evidence/io-boundary.json','evidence/finite-body-reception.json','SHA256SUMS.json','publication-receipt.json when available'],acceptance=[f'All{len(atoms)} manually authored meanings, all165 direct handlers and31 copy destinations are actually received, including shared helper gates and complete caller/default/failed-prefix distinctions.','Primary two formal texts and two full catalogs retain current operative meanings and cross-domain boundaries.','Do not inherit old463/80/1479 counts as behavioral proof or overwrite original authors.','No new proposal is currently established. If root derives a candidate, give it a stable ID and send full eight-section contract to an actual different nonauthor counterreview context.','Only root can grant final global signoff. Historical status and model/runtime unknowns remain separate from personally unread source.'],new_required_ids=[],remediation_started=False,update_status='UPDATE_NOT_STARTED',spawned_here=0,write_set=f'{REPORT}/tasks/external_item_atomic_completion/',publishing='Only dedicated branch, ordinary nonforce update. No formal/source/main/tag writes or PR/merge.'))

review=f'''# 第八轮持物全量原子意义补全审查

本专属任务完成新的有限静态审读；主责源码未读 0、两份正式文本未读 0、两份共享目录未读 0，必要游戏行为接口未接收 0。新增提案 0，已裁决 required 0；这不构成全局 `NO_REQUIRED_UPDATE`。主审仍须独立接收本包，WP50:179/181 的旧限定通过/CLOSED 资格未被本任务重新批准。`UPDATE_NOT_STARTED`。

固定合同 `{CONTRACT}`，B8 `{B8}`（workspace `751dfde81048c81390f89a65ca1d1a565ba8e1ca` / formal `f292698cdd4a8e725525a9be6dc34b75faaf151e`），参考 R `{R}` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。云端实际路径为 `/workspace/pokemon-essentials-clean-room` 与 `/workspace/pokemon-essentials`；未冒称存在 Mac 准备目录。唯一写集为本目录，专用分支 `codex/r8-external-item-atomic-completion-20261016`。正文、source、main、tag、其它任务及历史原件只读。

## 新审读与真实意义分母

本上下文亲读 ItemEffects 全 1–1948 行、WP50 主稿全181行/覆盖附表全71行及两共享 catalog 全669行；逐段完整 prompt241行、skill51行、AGENTS297行和专用合同/readset均实际读。前序合并输出曾截断，不据其授信；完整窗口及补读范围在 reading-ledger。有限依赖读实际中央恢复/状态/阶级、消费/共生、实际每击/后段/排序/奖励/场地/换人/逃跑与 Item/Nature/Stat/编译/装载定义；没有把其它领域全文件加入新 primary。

冻结 32 族、165 直接处理器、21 复制语句/31 目的绑定、196（族，物品）配对、180 不同注册物品名。另手工拆出 **{len(atoms)} 个语义断言、{len(groups)} 个具名规则/控制组**。数量只是本任务可追溯分母：真正证据在完整处理器正文、每项手工意义、实际 caller、共享前提与 operative 正文，不以语句、分号、注册或文件/hash计数授予行为信用。

完整 `evidence/semantic-atoms.json.gz` 无损恢复所有断言、普通对照/最小分支、source范围、正文定位、共享前提、196处理器/copy及实际消费者。forward/reverse为双向可恢复入口；覆盖表只作身份旁证。注册外直接核心及精神香草后继门逐条有限接收另见 `evidence/finite-body-reception.json`，不以路由标签代替事实，也不纳入本文件处理器分母。共享组中 forced/HP门、代际整数分数、RIPEN、性质/原性格、中央查询/提交、默认 nil/false/0、记录顺序与异常已写前缀分别登记。所有行为执行 `NOT_EXECUTED`。

## 具体核对结果

- 五混乱果逐项原性格降低能力项与 helper 接合；世代≤6/7/≥8分别整除8/2/3，先整数再熟成翻倍。forced满HP可0回复仍混乱/真返回，未扩大为忽略所有资格。
- ORAN/SITRUS的false半血门与默认低HP/贪吃者门分开；BERRYJUICE仍须canHeal。STARF先抽后拒、MICLE原真才触发、LANSAT直接设2均保留实际异常方向。
- 状态果按真实异常/混乱，精神香草保留DisableMove；白香草直接负阶归0；LEPPA持久首空槽/强制首部分槽、同下标战斗PP直接写及两个非原子写点保留。
- 受击类型物、反伤果、帽/刺转移、弱点保单部分成功、允许倒下物品与普通能力门分开；减伤果计算标记与逐击消费、宝石计算标记/首击反馈/整招消费分开。
- EJECTPACK/按钮先消费后负选择；红牌先随机候选后消费/共生再吸盘或扎根；无实际换人或假返回不撤回已消费。SHELLBELL、LIFEORB和声音喷雾各自资格与后段强行门分别核。
- 奖励用持久当前物/还原记录fallback，无场上有效性门；种子无接地门，期限扩展保留实际有限来源门；source动态callback/反馈故障不保证事务。
- 当前默认数据180注册名中179有完整选定记录，STICK缺省无记录但有真实复制定义；Gen5/6/7备份有STICK，Gen8必要字段同当前。备份不自动递归装载，直接定义不因无默认caller免读。只接收相关字段/定义，不冒签全部3154旧数据记录。
- AI完整有限接口保留原 `/root/com_ai`、`/root/com_move` 实读者；真实callback、粗估替代、目标减伤果略过、GemConsumed清理与评分/消费分工分开，不声称查询全纯或真实效果已执行。

## 原证据、接收和未决范围

原 COM-ABILITY-ITEM 的2R/4F实读与原读者资格原样保留。源事实/双向大对象在固定提交已转无损gzip；本任务按原manifest精确恢复完整字节/结构并读取必要完整item事实，不把原 `ALL_CONCRETE`、463身份、80族、1479句段定位自动继承为本次意义批准。CORE tuple原.json实际上463个9字段NDJSON，全部数组和强制格式伴件实读；原单JSON解析失败不改写为成功。

五个必要有限游戏接口已经接收/实际补读（CORE、MOVE、AI、KERNEL、DATA），具名原读者与完整接收边界见 interfaces/peer-reception。主审本包独立接收仍待进行，旧 WP50:179/181 接受资格保持 `EXACT_OLD_QUALIFIER_NOT_RECEIVED`。这两项属于接收/资格待决，**不是宿主limit，也不是本任务可读primary未读**。非本域完整ABILITY、AI、PBS、UI等个人未读不归零、不接管、不冒签。

当前上下文可见逻辑入口为 `/root`（delegated external_item_atomic_completion），来自用户给出的父线程 `01a13f49-a154-7054-9b04-ce31f924d01c`；该值不是本任务新平台ID。一次实际代理状态检查只回显 `/root running`。请求gpt-6.1-sol/ultra/default普速/Fast off；实际model/effort/tier/speed/Fast/platform task ID各为 `UNVERIFIED`。按用户约束没有spawn，没有虚构不同审者或独立反证；新增发现0，因此不自造已通过反证的required。

## 执行与发布

参考/Ruby、独立行为模型、native、游戏、真实存档、故障注入均 `NOT_EXECUTED`、新运行0。Python只读文本/JSON/gzip恢复、Git/hash与有限常数推导是工具核验，exit0不证明业务成功。真实工具失败、截断及其补读、未导出完整私有I/O边界在 `evidence/io-boundary.json`；没有倒填最初不可见UTC或声称私有平台流已公开回读。

报告core先冻结，后继 `publication-receipt.json` 绑定准确core及逐文件完整远端回读。命令行Git远端认证当前失败（gh exit0仍报告token无效）；已连接GitHub读取成功。实际发布协议以回执为准，限专用分支非强制更新，不改main/tag、不建PR、不合并。SHAmanifest不含自身未来hash，最终发布commit/tree在外部最终回复给出，避免递归回执。
'''
(OUT/'review.md').write_text(review)
print('core files assembled',len(ids),'input identities',len(reverse),'reverse locators',len(raw),'decoded atom bytes')
