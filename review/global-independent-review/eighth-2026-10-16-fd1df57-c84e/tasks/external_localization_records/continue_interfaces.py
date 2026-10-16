"""Serialize manually reviewed finite interface facts; no source/game execution."""
import json, hashlib, subprocess
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
BASE = ROOT / 'evidence/continuation'
REC = BASE / 'received'
SPEC = ROOT.parents[4]
REF = Path('/workspace/pokemon-essentials')
B = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PEER = '6c31240ade5c761b1f405958583a81ed140d4682'
REPORT = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/'
NOW = datetime.now(timezone.utc).isoformat()

def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])
def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
def get(path): return json.loads(path.read_text())
def identity(repo, commit, path):
    d = git(repo, 'show', commit + ':' + path)
    return dict(repo=str(repo), commit=commit, path=path,
                blob=git(repo, 'rev-parse', commit+':'+path).decode().strip(),
                bytes=len(d), sha256=hashlib.sha256(d).hexdigest(), lines=len(d.splitlines()))
def merge(ranges):
    out=[]
    for a,b in sorted(ranges):
        if out and a <= out[-1][1]+1: out[-1][1]=max(out[-1][1], b)
        else: out.append([a,b])
    return out
def complement(ranges,n):
    seen={i for a,b in ranges for i in range(a,b+1)}; out=[]
    for i in range(1,n+1):
        if i in seen: continue
        if out and i==out[-1][1]+1: out[-1][1]=i
        else: out.append([i,i])
    return out

# Preserve exact published peer bytes, including EOF; no receipt is inferred from fetching.
cached = {
 'media-messages.json':'resource_media_serialized_cloud/messages-body-reception.json',
 'media-encoding.json':'resource_media_serialized_cloud/serialized-encoding-closure-contribution.json',
 'media-data-getters.json':'resource_media_serialized_cloud/data-getter-source-contribution.json',
 'media-progress.json':'resource_media_serialized_cloud/progress.json',
 'kernel-report.md':'kernel_review/report.md',
 'media-kernel-core.json':'resource_media_serialized_cloud/kernel-core-additional-receptions.json',
 'media-ui-text.json':'resource_media_serialized_cloud/ui-text-consumers-reception.json',
 'kernel-fact-matrix.json':'kernel_review/file-unit-fact-consumer-spec-matrix.json'
}
fetched=get(BASE/'fetched-peer-manifest.json')
for name,short in cached.items():
    p=REPORT+'tasks/'+short
    d=git(SPEC,'show',PEER+':'+p); (REC/name).write_bytes(d)
    fetched.append(dict(commit=PEER,path=p,blob=git(SPEC,'rev-parse',PEER+':'+p).decode().strip(),bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),local='received/'+name,actual_content_read=False))

scope = {
 'media-messages.json':'Entire file: all bucket spans, 10697-pair attestation, five unequal pairs, object links and qualifications. Actual source reader /root/resource_media_serialized_cloud.',
 'media-encoding.json':'Entire file: exact messages/Scripts.rxdata tags, E metadata, raw UTF8 versus compressed bytes, safe decoding qualification. Source reader /root/resource_media_serialized_cloud.',
 'media-data-getters.json':'Entire file: MED-DATA01–09, all eight complete source identity objects, premises and exclusions. Actual source reader /root/resource_media_serialized_cloud.',
 'media-progress.json':'Entire file, lifecycle only; no behavioral credit.',
 'kernel-report.md':'Entire report, finite-source scope and explicit remaining gaps; no global PASS received.',
 'media-kernel-core.json':'Entire kernel section (15 complete producers + 3 common contracts), entire core F01–F04 with F02 reread after truncated output, all qualifications. No whole-source personal credit transfer.',
 'kernel-fact-matrix.json':'Only complete KER-F102–125 objects, including reread F112–114. Other 111 rows NOT_RECEIVED by this reviewer.',
 'media-ui-text.json':'All 36 complete semantic unit objects own7/wp66_29, shared qualifications and parent reception; five primary identity rows. The 28 administrative dependency identity rows are only bound mechanically; the oversized display was truncated there. Not whole administrative-container FULL_READ.',
 'resource_media_serialized_cloud--kernel-core-additional-binding-receptions.json':'Entire file. Exact Trainer_LoadAndNew producer identity and complete pbConvertTrainerData62–68; priority supplement and F02 tail exclusion preserved.',
 'resource_media_serialized_cloud--ui-dex-name-consumer-reception.json':'Entire file: 7 complete units/24 facts, five exact source identities, original author /root/ui_wp66 and receiving /root/ui_full attribution; no source FULL transfer.',
 'resource_media_serialized_cloud--media-consumer-receptions.json':'Only complete UI17-U026–U030, shared ui qualification/exclusion, and top-level kernel/source navigation; unprinted/truncated remaining units NOT_RECEIVED.',
 'ui_full--kernel-consumers-interface.v2.json':'Only complete UI17-U034–036, UI65-U004/U020/U021, UI67-U010; complete traces KC002/KC032–035 and common credit/premise/open/correction. Other units NOT_RECEIVED.',
 'pbs_battle--review.md':'Entire report: exact reader/path distinctions, 21-primary record attestation and pending external scope. This is not reception of every raw PBS field value.',
 'pbs_creature_facility--review.md':'Entire report, useful bounded TrainerType/display observations only; no full facility semantic acceptance or new PBS whole-file credit.',
 'pbs_battle--field-contracts.json':'Entire field-contract file. Localization name/description/portion/plural and identity-to-display interfaces received; record values not replaced by their hashes.',
 'ui_full--review.md':'Entire report, original readers and qualifications retained; no global UI approval.',
 'ui_minigames--review.md':'Entire report, original minigames reader and history-open qualifications retained; not independent counterreview of ELR001.',
 'history_current--report.md':'Entire report, bounded current/history qualification and incomplete work retained.',
 'h_r7_final_receptions--report.md':'Entire report, exact 243-payload/27-ID/13-batch historical scope attestation; raw 243 payloads NOT personally read or fully received here.',
 'external_h_r6_effective_contracts--report.md':'Entire report at 38e78d, explicitly incomplete; no full R6 effective-contract reception.',
 'external_h_c2_current_records--report.md':'Entire report at 3fdc7f, explicitly incomplete; no full 37-record/canonical reception.',
 'resource_media_serialized_cloud--static-recovery-001--current-serialized--Main.rb':'Entire derived49-line program personally read; not executed; binary structure/decode provenance received from media reader.',
 'resource_media_serialized_cloud--static-recovery-001--current-serialized--Main.identity.json':'Entire identity object read, compressed/decoded identities retained.'
}
for a in fetched:
    name=Path(a['local']).name
    a['semantic_read_scope']=scope.get(name,'NOT_READ; fetched only; no semantic reception')
    a['personal_source_full_credit_transferred']=False
    a['actual_content_read']=name in scope and ('Entire file' in scope[name] or 'Entire report' in scope[name] or 'Entire field-contract' in scope[name] or 'Entire derived' in scope[name] or 'Entire identity' in scope[name])
put(BASE/'fetched-peer-manifest.json',fetched)

imgs=get(BASE/'image-unit-inventory.json')
image_meanings=[
 'Translate only bg/memo basenames then concatenate GRAPHICS_DIRECTORY through Cache. Tiles/cursor stay fixed; actual scene/pixels unexecuted.',
 'Reel image fullpath translated at each constructor; source H later participates in reel geometry/timing. Prior whole456-line reading retained.',
 'Payout win/bonus/lose identities translated only at their success/replay/loss branch; fixed lights/numbers independent. Prior whole-file reading.',
 'Start insert fullpath translated after earlier scene/reel construction; partial initialization not rolled back. Prior whole-file reading.',
 'Main stop/insert/press paths translate at their reached betting/spin/prompt stage; input/credit write order unchanged. Prior whole-file reading.',
 'Back card loads type sheet only for nonnil type; fixed opponent back excluded when noback; strict Type lookup after load.',
 'Owner0 delegates back; other owners select fixed player/opponent back; translated type sheet independent of Species icon and fixed numbers.',
 'Safari databox fullpath translated before its dimensions allocate contents; no host bitmap-success claim.',
 'SideSize1 normal player/foe pair versus thin pair; both array elements translated before parity selection; replace old wrapper before geometry changes.',
 'Level overlay identity translated separately from numeric level drawing.',
 'NONE suppresses status image; badly poisoned selects last status row, otherwise strict icon_position; negative suppresses image.',
 'Graphical Command only loads translated cursor_command; fixed overlay_command independent; text mode creates command window instead.',
 'Graphical Fight only loads translated fight/type/Mega/shift sheets; fixed overlay independent; dimensions feed buttons. Text mode takes separate path.',
 'Naming creates fixed tabs/background/subject first, then translated overlay_controls; subject-specific branches do not translate all naming graphics.',
 'Naming mode icon fullpath translated for draw-list load, slice x=mode*60 and width60; destination changes independently.',
 'Relearner resolves every candidate name first, then translated type sheet, then initial draw. Empty list failure not converted into safe cancel.',
 'Visible candidate names/types/PP separately consumed; type sheet through draw list; strict selected move description queried after other drawing data.',
 'Bag register fullpath only important item plus registered/canRegister branch; row0/row24 distinguish; register icon suppresses quantity.',
 'Storage held member wins selection; no member returns; non-egg gates level/ability/item/type images; translated types use current icon positions.',
 'Summary loads translated types before initial page, retains party reference; fixed marking/background resources stay independent.',
 'Forget scene loads translated type sheet before first selected move; no guarantee zero-move scene reaches input.',
 'Summary egg redirects before non-egg resources; fainted/status/Pokerus determine translated statuses row; names and held-item labels separate.',
 'Summary move rows translate type-sheet identity only for existing moves; display_type(member), name, PP and nil slots are independent.',
 'Selection four or four+new rows translate types; per-member type source and page geometry preserved; fixed detail backgrounds independent.',
 'Trainer Card resolves translated female card before female gate, fallback translated card; female background separate raw resolution.',
 'Jukebox loads translated fullpath background before header and supplied command window; no audio execution implied.',
 'Dex menu translated bg_menu independent of separately translated SEEN/OBTAINED labels and command contents.',
 'Party panel fixed rounded/rectangular variants; three translated HP backgrounds via Changeling, translated statuses via AnimatedBitmap; no all-resource claim.',
 'Party egg suppresses level overlay; translated overlay_lv distinct from numeric level.',
 'Full dex startup translates icon_types; fixed Area/TownMap/arrow resources depend on separate metadata; first draw reached only after earlier dependencies.',
 'Brief dex independent numbering construction, translated icon_types before first Info draw; national/regional gates retained.',
 'Dex Info bg_info always; overlay_info only brief; owned gates category, dex text, footprint/types; unowned placeholders. Actual US units independent.',
 'Area bg_area translated; map/nest square construction uses separate raw data; region and species localized text consumed at end.',
 'Forms bg_forms translated; form label selected from existing available gender/form tuples, species name independent.',
 'Dex main translates icon_types/icon_hw/icon_searchslider only; other sliders/shape/search backgrounds fixed.',
 'Controls seven fullpath identities translated independently of labels and fixed bg; later picture selection uses screen number.'
]
for a,meaning in zip(imgs,image_meanings):
    a['status']='PERSONALLY_COMPLETE_METHOD_READ' if a['id'] not in ['ELR-IMG-02','ELR-IMG-03','ELR-IMG-04','ELR-IMG-05'] else 'ALREADY_PERSONALLY_FULL_FILE_READ'
    a['actual_reader']='external_localization_records /root'
    a['meaning']=meaning
    a['premise']='Fixed R/no overrides/concurrent mutation; valid named receiver objects and prior normal calls; source requests only, failures retain actual prefix.'
    a['execution']='NOT_EXECUTED'
put(BASE/'image-unit-inventory.json',imgs)

# Exact ranges actually displayed/read; overlap merges only track personal reading, never peer FULL.
own=[(a['path'],a['range']) for a in imgs if a['id'] not in ['ELR-IMG-02','ELR-IMG-03','ELR-IMG-04','ELR-IMG-05']]
own += [(p,[a,b]) for p,a,b in [
 ('Data/Scripts/007_Objects and windows/010_DrawText.rb',1130,1151),
 ('Data/Scripts/007_Objects and windows/007_BitmapSprite.rb',210,243),
 ('Data/Scripts/009_Scenes/002_EventScene.rb',97,137),
 ('Data/Scripts/016_UI/001_Non-interactive UI/002_UI_Controls.rb',43,83),
 ('Data/Scripts/007_Objects and windows/011_Messages.rb',239,274),
 ('Data/Scripts/003_Game processing/001_StartGame.rb',67,126),
 ('Data/Scripts/002_Save data/001_SaveData.rb',1,82),
 ('Data/Scripts/002_Save data/004_Game_SaveValues.rb',1,127),
 ('Data/Scripts/012_Overworld/001_Overworld.rb',650,750),
 ('Data/Scripts/002_Save data/002_SaveData_Value.rb',1,284),
 ('Data/Scripts/001_Technical/002_Files/001_FileTests.rb',112,151),
 ('Data/Scripts/004_Game classes/004_Game_Map.rb',98,108),
 ('Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb',119,138),
 ('Data/Scripts/001_Technical/002_RubyUtilities.rb',1,42)]]
rows=[]
for path in dict.fromkeys(p for p,_ in own):
    ranges=merge([r for p,r in own if p==path]); ident=identity(REF,R,path)
    raw=git(REF,'show',R+':'+path).decode().splitlines(); view=BASE/'own-source-views'/ (hashlib.sha256(path.encode()).hexdigest()[:16]+'.txt')
    view.parent.mkdir(parents=True,exist_ok=True)
    view.write_text('\n'.join(f'{n}: {raw[n-1]}' for a,b in ranges for n in range(a,b+1))+'\n')
    rows.append(dict(identity=ident,ranges=ranges,personal_reader='external_localization_records /root',status='ACTUALLY_READ',view=str(view.relative_to(ROOT)),exact_per_read_utc='UNVERIFIED_NOT_BACKFILLED',whole_file_read=ranges==[[1,len(raw)]],qualification='Some displayed neighboring tails are partial definitions; only complete named units support their stated facts.'))
formal='deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md'
rows.append(dict(identity=identity(SPEC,B,formal),ranges=[[98,124]],status='ACTUALLY_READ',personal_reader='external_localization_records /root',whole_file_read=False,exact_per_read_utc='UNVERIFIED_NOT_BACKFILLED'))
put(BASE/'own-reading-ledger.json',dict(schema='gr8-elr-continuation-own-reading/v1',created_utc=NOW,source_rows=rows,image_complete_methods=36,image_existing_whole_file_methods=4,image_new_complete_method_ranges=32,image_new_method_lines=1363,derived_Main='received/resource_media_serialized_cloud--static-recovery-001--current-serialized--Main.rb: all49 lines actually read, decoded source view; no personal decoder/loader execution',limits='limit-records.json all14 complete records and all metadata actually read; original older limit payload not yet recovered/read',io='Actual platform output chunks include 5bac70,9a02c7,db59f0,5330a7,1cbf1d,80898a,bc50f6,07865e,86dedd,95c566,81a82e. This is a retrospective source-view archive, not a claim to reproduce original complete stdout/stderr/UTC.',technical_failures='Two oversized range iterators raised IndexError before yielding the body; corrected clipped output read. Wrong guessed map/formal/old-limit paths and schema-key probes failed and were not credited. Oversized peer displays truncated; complete relevant units reread or explicitly excluded. Exec-server disconnection/recovery timeout occurred, then pwd succeeded; no approval rejection.',business_execution_count=0))

ledger=get(ROOT/'reading-ledger.json')
old=ledger['dependency_file_range_summary']
scope_by_suffix={
 '001_Compiler.rb':('kernel_review; developer_full','Only preprocessing/tokenizer/compile/default-message persistence interface necessary here; full source attested by kernel_atomic reception. Other compiler rules stay primary-owned.'),
 '002_Compiler_CompilePBS.rb':('kernel_review; developer_full','All15 message producers + common driver contract received with exact source identity; unrelated domain validators remain primary-owned, not self full read.'),
 'wp15-resource-matching-and-audio.md':('world_resources_rendering; kernel_review','Actual image resolution and ordinary/prefixed wrapper paths needed and personally read; remaining audio/native/material contracts stay original primary.'),
 '003_Type.rb':('kernel_review; resource_media_serialized_cloud','Name-domain/getter contract received MED-DATA03; remaining type mechanics/asset policies not own localization primary.'),
 '005_Move.rb':('kernel_review; pbs_battle','Name/description domains and disabled display overrides received MED-DATA05; effect mechanics outside this task.'),
 '006_Item.rb':('kernel_review; creature_b; pbs_battle','Five text getters/raw constructor defaults received MED-DATA06; item effects, held use and prices remain original primary.'),
 '008_Species.rb':('kernel_review; creature domain','Four localized getters/form fallback received MED-DATA07; full species mechanics outside own primary.'),
 '014_TrainerType.rb':('kernel_review; UI; pbs_creature_current_cloud','Localized real name plus independent graphic identities received MED-DATA09/UI67-U021; not whole trainers population.'),
 '002_Debug_MenuCommands.rb':('developer_full','Translation extract/import menu1423–1480 personally read; other debug command bodies unrelated to own finite localization contract.'),
 '001_Settings.rb':('kernel_review','LANGUAGES declaration415–430 personally read; current boot/language consumers read/received. Other settings not necessary to this finite text-record contract.'),
 '013_UI_Load.rb':('ui_full; kernel_review','Complete language branch personally read; complete load-screen source contribution UI65-U004 and kernel facts received. Other load UI remains primary-owned.'),
 'generic-kernel-wp05-06-07-08-09-10.md':('kernel_review','All LZ01–41 and related local rows personally read; remaining nonlocalization catalog rows are other domains.'),
 '007_BitmapSprite.rb':('ui_full','IconSprite and entire Changeling class personally read. Remaining generic sprite definitions not needed beyond accepted UI source contracts.'),
 '001_RPG_Cache.rb':('ui_full; world_resources_rendering','Complete cache load entrance1–76 personally read; later specialized RPG resource wrappers outside image identity lookup claim.'),
 '001_FileTests.rb':('kernel_review; world_resources_rendering','pbResolveBitmap119–135/pbBitmapName139–142 personally read, earlier filesystem helpers1–69 retained. Remaining audio/archive/path abilities primary-owned.'),
 '001_Utilities.rb':('kernel_review; developer_full','Language chooser603–624 personally read; unrelated helpers1–602 not necessary here.'),
 '015_UI_Options.rb':('ui_full; kernel_review','PokemonSystem default language field1–36 personally read; exact full-screen option/language consumers received finite UI/kernel facts. Other option controls original primary.')
}
oldrows=[]
for a in old:
    if not a['unread_ranges']:continue
    path=a['identity'][2:];extra=[v['ranges'] for v in rows if v['identity']['path']==path and v['identity']['commit']==(R if a['identity'].startswith('R:') else B)]
    merged=merge(a['read_ranges']+[r for z in extra for r in z]);remain=complement(merged,a['total_lines'])
    suffix=path.rsplit('/',1)[-1];owner,need=scope_by_suffix.get(suffix,('kernel_review','Now personally complete; no residual.'))
    oldrows.append(dict(identity=a['identity'],total_lines=a['total_lines'],previous_unread_ranges=a['unread_ranges'],previous_unread_lines=a['unread_lines'],current_personal_read_ranges=merged,current_personal_unread_ranges=remain,current_personal_unread_lines=sum(b-a+1 for a,b in remain),frozen_or_named_primary_owner=owner,necessary_scope_disposition=need,peer_full_not_converted_to_personal=True))

frozen={}
for task in ['pbs_battle','pbs_world','pbs_creature_current_cloud.complete','pbs_creature_backups']:
    path=REPORT+'delegation/readsets/'+task+'.json';x=json.loads(git(SPEC,'show',PEER+':'+path))
    for a in x['reference']:frozen[a['path']]=dict(task=x['primary_task'],readset_path=path,readset_commit=PEER,readset_blob=git(SPEC,'rev-parse',PEER+':'+path).decode().strip(),source_identity={k:a[k] for k in ['commit','path','git_blob','bytes','sha256']})
pbs=[]
for a in get(ROOT/'evidence/pbs-dependencies.inventory-only.json'):
    path=a['identity'][2:];owner=frozen[path];name=path.rsplit('/',1)[-1]
    fields= ['SectionName','Name']
    if 'pokemon' in name:fields+=['FormName','Category','Pokedex','base/form identity and explicit omission/inheritance; no move/stat/rule body credit']
    elif name.startswith('items'):fields+=['NamePlural','PortionName','PortionNamePlural','Description']
    elif name.startswith(('moves','abilities','ribbons')):fields+=['Description']
    pbs.append(dict(path=path,owner=owner,necessary_localization_field_scope=fields,necessary_interface='raw field/default → real_* constructor → set/addMessagesAsHash domain → selected language getter → scoped UI; exact corpus/body values already personally read in 18 primary files and received binary corpus, not proof every PBS record equals one corpus pair',record_body_personally_read=False,record_body_fully_received=False,status='PRIMARY_RECORD_BODY_ROUTED_NOT_RECEIVED',available_named_read_attestation='pbs_battle exact report/field-contract received' if owner['task']=='pbs_battle' else 'NOT_RECEIVED for complete original record body; frozen assignment is not actual reading',activation='Top-level PBS/*.txt discovery only; backup subdirectories require explicit replacement/selection, not auto recursive activation'))
put(BASE/'unread-scope-routing.json',dict(schema='gr8-elr-bounded-dependency-routing/v1',created_utc=NOW,old_personal_partial_file_denominator=18,old_personal_unread_lines=6782,current_personal_unread_lines_in_same_18=sum(a['current_personal_unread_lines'] for a in oldrows),old_partial_files=oldrows,pbs_files=35,pbs_personal_full=0,pbs_record_body_fully_received=0,pbs=pbs,qualification='This routes readable other-primary content, not a material/host limit or an assignment/attestation-as-PASS substitution. Scope does not expand into re-auditing all PBS mechanics. Root must receive original primary record bodies for global closure.'))

facts=[
 dict(id='ELR-C01',interface='ELR-I01',meaning='Current game→core→original hash return, empty hit, key-only normalization versus raw translated body, sequential placeholder substitution; no default-baseline runtime fallback.',support=['own complete Intl823/WP08','kernel KER-F102–112','media messages/encoding full scoped receipt'],formal='WP08§3–6; LZ01–41'),
 dict(id='ELR-C02',interface='ELR-I02',meaning='All15 compiler message collectors and extra TrainerType producer, set/add distinction, registry-before-text-before-save prefixes, default/core exclusion, sequential nontransactional persistence; cached default load does not reload current language.',support=['media-kernel-core.json#/kernel','additional-binding packages0','own Compiler selected whole units'],formal='WP08§6 / WP04; complete other-domain clause acceptance remains primary-owned'),
 dict(id='ELR-C03',interface='ELR-I03',meaning='Eight data sources/9 facts preserve identity versus raw/localized names, constructors and nil/empty field defaults; 35 PBS file bodies routed to exact frozen owners. No claim corpus pair counts equal registered records or all PBS semantics.',support=['media-data-getters.json','pbs_battle--field-contracts.json','unread-scope-routing.json'],formal='WP08§3.2/§6 and original data/UI primary contracts'),
 dict(id='ELR-C04',interface='ELR-I04',meaning='Exact messages963270-byte corpus has31 buckets,18 nonempty hash buckets and10697 pairs matching own18 primary read, including exactly same5 unequal key/body rows; 178 links to Strings, raw UTF8/E metadata kept. Scripts594 bytes decodeMain1197 bytes49 lines; decoding never executes it. messages_game.dat ABSENT at fixedR.',support=['media-messages.json','media-encoding.json','Main identity and complete derived source read'],formal='WP08§3/§6; L10/L14 execution qualifications'),
 dict(id='ELR-C05',interface='ELR-I05',meaning='All63 previously located explicit graph-image calls now have36 personally complete caller-method bodies (4 already inside Slot full file). Fullpath translations differ from Voltorb basename composition; no universal all-images translation or fallback-on-load-error.',support=['image-unit-inventory.json complete36','own wrappers/DrawImagePositions/Changeling/EventScene bridge','UI36 complete semantic units and named4-family package'],formal='WP08§5.1.1/WP15§3.2/§5; WP65/66/67/69 existing finite UI contracts; proposedSlot omission remains independently undecided'),
 dict(id='ELR-C06',interface='ELR-I06',meaning='MapMetadata.name mutates selected returned string via gsub!, including translated/original/basic shared material; simple map-name wrapper fallback differs from generic message copied-input processing. Language directdump bypasses Game.save; ordinary save serializes PokemonSystem in registration order and only rescues IO/SystemCall. ItemBall adds before success prompt, ReceiveItem prompts before add, BuyPrize adds before pocket prompt; formatting/host errors retain reached prefix.',support=['own SaveData82/Value284/SaveValues127, StartGame126 nowfull','own MapMetadata121–126/Messages245–262/Game_Map103–105','own Overworld656–750','received UI17U026–030/U034–036, UI65U004'],formal='WP08§4/§5.2 / WP11§5.3.1 (personally fullsection) / finite WP17 and WP65 primary receipts'),
 dict(id='ELR-C07',interface='ELR-I07',meaning='Current R6 L01–L14 complete records read. Exact history reviewers report their full versus incomplete scopes; no oldPASS transfer. R7 37 title/canonical/alias projection is navigation only; original37 complete contracts and R6 effective56 not fully received here. Slot canonical/extension decision remains root/history pending.',support=['limit-records.json','history_current, h_r7_final_receptions, external_h_* exact published reports','37-title-projection.json'],formal='Global contract historical qualification; no historical CLOSED reopening or runtime claim')
]
put(BASE/'peer-reception.json',dict(schema='gr8-elr-finite-interface-reception/v1',created_utc=NOW,receiver='external_localization_records /root',peer_commit=PEER,source_credit='All original source FULL/actual reader identities preserved; own source reading only in own-reading-ledger. Receiving an already shared contribution adds no independent source vote.',facts=facts,manifest='fetched-peer-manifest.json',global_pass_received=False,root_acceptance='NOT_RECEIVED',business_execution='NOT_EXECUTED'))

interfaces=get(ROOT/'interfaces.json');interfaces.update(schema='gr8-external-localization-interfaces/v2',updated_utc=NOW,received=5,partially_received=2,not_received=0,incoming_denominator=7,qualification='received counts COMPLETE_FINITE only; two PARTIAL_FINITE carry explicit readable body/canonical debts. Root acceptance of outgoing contribution is a distinct denominator.')
for a,f in zip(interfaces['interfaces'],facts):
    a['continuation_fact']=f['id'];a['continuation_evidence']='evidence/continuation/peer-reception.json'
    a['status']='COMPLETE_FINITE_RECEIVED'
    a['pending']='Root cumulative reception/independent decision; no whole cross-domain/runtime approval.'
    a['local_evidence']=f['meaning']
interfaces['interfaces'][2].update(status='PARTIAL_FINITE_FIELD_CONTRACT_RECEIVED_RECORD_BODIES_ROUTED',pending='All35 raw PBS bodies remain personally UNREAD / complete-body NOT_RECEIVED. Necessary field interfaces received; exact frozen primary owners, fields, identities and activation premises in unread-scope-routing.json. Global record-body reception belongs root/primary owners.')
interfaces['interfaces'][6].update(status='PARTIAL_FINITE_QUALIFICATION_RECEIVED_DEDUP_UNVERIFIED',pending='Original older limit payload, all R6 effective56/R7 complete37 canonical contracts and their full evidence not received here; named historical primary readers retain responsibility. ELR001 canonical/alias/extension classification and strongest coverage rebuttal require root/history independent reception.')
interfaces['outgoing_primary_files']['parent_message_status']='SUBMITTED_TO_ROOT per continuation request; no explicit acceptance receipt supplied'
put(ROOT/'interfaces.json',interfaces)

p=get(ROOT/'proposals.json');q=p['proposals'][0]
q['continuation']=dict(updated_utc=NOW,full_evidence='evidence/continuation/peer-reception.json',counterexample_scope='Ordinary finite selected-language fixture, not repositorydefault language or existing asset claim.',strongest_counterargument='WP08§5.1 and generic _INTL already define lookup for arbitrary strings. If root judges §5.1.1 table illustrative rather than exhaustive or another primary contract already covers Slot, this is optional navigation/alias/no-required rather than a new mandatory behavioral gap. Own rebuttal is not independent counterreview.',canonical_status='UNVERIFIED: title/alias navigation plus limited history reports do not prove full-history negative; may be extension of older language-resource root, root decides.',independent_counterreview='NOT_RECEIVED')
q['normal_cancel_failure_partial']['empty_translation']='Empty hit into IconSprite.setBitmap clears it. For direct reel AnimatedBitmap.new(""): current String#last returns "", split gives empty array, pop makes filename nil and filename[regex] fails before GifBitmap rescue. This is SOURCE_STATIC/DERIVED_VECTOR, NOT_EXECUTED; frozen/default String utility premise retained.'
q['source']['string_last']={'identity':'R:Data/Scripts/001_Technical/002_RubyUtilities.rb','lines':[24,31]}
q['history']['reason']='R6 currentL01–L14 read, exact incomplete/complete history reviewer reports and R7 title/canonical/alias projection received; full original canonical contracts not received. Do not infer a new canonical root from no title match.'
q['negative_evidence']['remaining']='Finite complete36 resource caller methods now read and original UI source facts received. Full broader formal and original R6/R7 canonical roots are still not fully received; no full-global negative claim.'
put(ROOT/'proposals.json',p)

ledger['continuation']={'updated_utc':NOW,'own_ranges':'evidence/continuation/own-reading-ledger.json','peers':'evidence/continuation/peer-reception.json','exact_residual':'evidence/continuation/unread-scope-routing.json','old_18_partial_personal_unread_now':sum(a['current_personal_unread_lines'] for a in oldrows),'primary_read_counts_unchanged':True}
put(ROOT/'reading-ledger.json',ledger)
ids=get(ROOT/'identities.json');ids['continuation']={'own': [a['identity'] for a in rows], 'peers':'evidence/continuation/fetched-peer-manifest.json','same_frozen_inputs':True};put(ROOT/'identities.json',ids)
fw=get(ROOT/'forward-mapping.json');fw['continuation_finite_interfaces']=facts;put(ROOT/'forward-mapping.json',fw)
rv=get(ROOT/'reverse-mapping.json');rv['continuation_finite_interfaces']=[{'fact':a['id'],'formal':a['formal'],'support':a['support'],'qualification':'Only explicit finite assertion; not full formal-primary atom acceptance.'} for a in facts];put(ROOT/'reverse-mapping.json',rv)
pr=get(ROOT/'progress.json');pr.update(updated_utc=NOW,ended_utc=NOW,process_status='COMPLETED_WITH_EXPLICIT_RECEPTION_GAPS',semantic_status='PRIMARY_FULL_READ_AND_SEVEN_SCOPED_INTERFACES_RECONCILED_FIVE_COMPLETE_TWO_PARTIAL',incoming_interfaces_not_received=0,incoming_interfaces_fully_received=5,incoming_interfaces_partially_received=2,unread_lines_in_original_partial_dependencies=sum(a['current_personal_unread_lines'] for a in oldrows),additional_unread_pbs_files=35,publication_status='CONTINUATION_READY_FOR_NORMAL_COMMIT_PUSH_AND_FULL_REMOTE_READBACK',blockers=['ELR-I03 complete PBS record-body reception35 remains root/original primary scope; not a host/material limit.','ELR-I07 full original historical/canonical reception and ELR001 independent classification pending root/history.','Outgoing18 primary files submitted to root, explicit final acceptance receipt not supplied; counterreview1 NOT_RECEIVED.'])
pr['continuation'].update(completed_utc=NOW,environment_transport='exec server disconnected/recovery timed out, subsequently recovered; no persistent permission blocker',own_new_image_method_reads=32,own_new_image_method_lines=1363,original_6782_current_personal_unread=6655,business_executions=0)
put(ROOT/'progress.json',pr)

# Exact finite history navigation; projections are explicitly not full contract reads.
p='review/global-independent-review/seventh-2026-10-14-e646432-7a91/findings.json';x=json.loads(git(SPEC,'show',B+':'+p))
put(BASE/'37-title-projection.json',{'identity':identity(SPEC,B,p),'scope':'Only all37 title/canonical/alias/root-cause navigation fields actually read; original proposal/verdict bodies UNREAD except explicitly existing receipts, no negative proof.','rows':[dict(id=a['id'],title=a.get('original_proposal',a).get('title',a.get('original_proposal',a).get('subject')),canonical=a.get('canonical_id'),aliases=a.get('aliases'),root=a.get('root_cause_key')) for a in x['records']]})
print(json.dumps({'spec':str(SPEC),'personal_rows':len(rows),'old_partial_unread':sum(a['current_personal_unread_lines'] for a in oldrows),'pbs':len(pbs),'peer_snapshots':len(fetched),'facts':len(facts)}))
