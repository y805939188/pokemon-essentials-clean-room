import json,pathlib
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_04b.json').read_text())
d=base['source_dictionary']
def src(k,p,r,credit='FULL_FILE_READ'):
 d[k]={'path':p,'range':r,'actual_reader':'/root/core_atomic_reception','reading':credit}
src('bag','Data/Scripts/013_Items/008_PokemonBag.rb',[1,301])
src('itemdata','Data/Scripts/010_Data/002_PBS data/006_Item.rb',[1,270])
src('itemhandlers','Data/Scripts/013_Items/001_Item_Utilities.rb',[1,917])
src('battleitems','Data/Scripts/013_Items/003_Item_BattleEffects.rb',[1,712])
src('attack','Data/Scripts/011_Battle/001_Battle/010_Battle_AttackPhase.rb',[1,202])
src('eor','Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',[1,781])
src('potionpbs','PBS/items.txt',[2942,2950],'PARTIAL_FILE_COMPLETE_ONE_PBS_RECORD_READ; compiled artifact not executed')
src('targetresolve','Data/Scripts/011_Battle/002_Battler/008_Battler_UseMoveTargeting.rb',[1,203])
d['ui_targets']={'contribution':'ui67-complete-units.ndjson','receipt':'ui67-reception.v1.json','unit_ids':['UI67-U008','UI67-U009','UI67-U010'],'original_reader':'/root/ui_full','reading':'COMPLETE_ORIGINAL_FACT_OBJECTS_RECEIVED; U009-10 qualified by exact actual Battler-object argument, not integer adjacency proof'}
src('firsttarget','Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb',[333,382],'PARTIAL_FILE_COMPLETE_TARGET_TEXT_AND_INITIAL_TARGET_METHODS_READ')
rows=[]
def row(n,children,units,chain,**extra):
 rows.append(dict(number=n,children=children,source_units=units,chain=chain,**extra))
row(243,[
 'GameData::Item BattleUse schema maps0 unavailable,1 OnPokemon,2 OnMove,3 OnBattler,4 OnFoe,5 Direct; absent constructor value defaults0.',
 'Types1/2 dispatch to one party-Pokemon executor; selected move index remains choice[3] for PP handlers.',
 'Type3 targets current battler found by party index;4 calls ball executor;5 direct executor uses own battler when target index negative.'
],['itemdata','attack','items'],'Item schema/constructor battle_use→selection useType→choice target/move indices→AttackPhase case→distinct executors; not all target domains interchangeable.')
row(244,[
 'Scene battle Bag filter offers battle_use>0; this UI filter is separate from handler existence and execution behavior.',
 'Selection type1/2 rejects absent BattleUseOnPokemon handler before target helper; type3 rejects absent BattleUseOnBattler handler.',
 'Type4/5 have no parallel effect-handler-existence requirement in core selection; they still require a Pokemon and generic CanUse qualification.',
 'Type1/2 obtains party Pokemon and optional current battler; type3 requires found battler.pokemon; helper rejects nil/egg, Embargo and hyper-mode non-scent.',
 'Type4 rejects negative target, reads that battler Pokemon; type5 reads user battler Pokemon; all families reject missing Pokemon before generic qualification.',
 'Generic triggerCanUseInBattle defaults true only when its resolved direct/conditional handler is absent; unknown item is not thereby a lawful registered inventory item.',
 'Registration commits UseItem/item/target/move fields before consumption; normal registration returns true after consumption.',
 'consumed_after_use? requires non-important and consumable; player Bag.remove one false raises after choice writes; nonplayer owner list deletes first matching identity when a list exists.',
 'Ball classification is Item.is_poke_ball? (PokeBall or SnagBall flags); player command loop ends further action choices only after successful ball registration.',
 'Ball conditional CanUse handler separately requires firstAction, room, enabled balls, visible target, and opposing-count/snaggable trainer exception; occupancy and partial prefixes remain conditional.'
],['ui_command','command','items','itemdata','itemhandlers','event_dispatch','battleitems','bag'],'Actual scene yields selected item/useType→core existence/target/helper→resolved qualifier→choice writes→single inventory removal→ball all-action flag. Handler collection normalized lookup includes conditional predicates; no arbitrary unknown-ID authorization.')
row(245,[
 'pbItemMenu checks !internalBattle before scene menu; displays Items cannot be used here and returns false.',
 'This gate governs normal Bag command path; direct method invocation or another special battle controller is not certified by it.'
],['command'],'normal command Bag→internalBattle guard→message/false; no inventory registration on this reached refusal.')
row(246,[
 'Family1/2 executor announces item, resolves party Pokemon and optional battler, then calls CanUse with firstAction=true and showMessages=false.',
 'Family1/2 false qualification displays generic failure and refunds; it does not clear choice item identity.',
 'Family1/2 true qualification calls BattleUseOnPokemon then clears choice item identity on normal callback return, regardless callback return truthiness.',
 'Family3 executor resolves current battler; absent target displays not-where-usable then refunds retaining identity.',
 'Family3 existing target qualification false displays generic failure then refunds; true calls BattleUseOnBattler, clears identity, then calls target item-on-stat-drop hook.',
 'Family5 announces, resolves user/explicit target Pokemon, rechecks generic qualification; true triggers UseInBattle then clears identity; false refunds with identity retained.',
 'Family4 chooses user index only for negative index, triggers UseInBattle directly, then clears item identity; no generic execution recheck or automatic unsuccessful-capture refund.',
 'Refund skips nil/nonconsumable; player requires current Bag.can_add? before add, refusal raises; nonplayer pushes only if owner list exists.',
 'Nil/egg/Embargo/hyper-mode helper is called at normal selection branches1/2/3, not universally repeated by these execution wrappers.',
 'Effect callback failure before clear retains identity and any already-written effect prefix; family3 stat-drop callback failure occurs after identity clear. Ordinary false return alone does not cause generic refund.'
],['items','attack','itemhandlers','battleitems','bag','ability_item'],'selection-owned consumption→per-family qualifier and effect→normal clear OR refund with retained choice; announcements and effects precede later possible exceptions.')
row(247,[
 'Legal registered Direct5 item I with consumable true and no important/ball/snag flag, no direct/conditional qualification or effect handler, is a valid conditional input, not a claim every unknown ID works.',
 'Internal living normal player/Bag1 makes scene type filter pass; no type5 effect-existence gate and absent qualification defaults true.',
 'Normal registration consumes1→0 after storing identity; execution absent qualifier again defaults true, missing UseInBattle returns normally without effect, then identity clears; inventory stays0.',
 'Cleared identity prevents end cleanup refund on this vector; callback return nil does not turn it into qualification failure.',
 'Changing only family to1 with missing Pokemon handler rejects before registration; changing only to3 with missing battler handler likewise rejects; inventory remains1.'
],['itemdata','ui_command','command','items','itemhandlers','event_dispatch','bag','end'],'Legal configured Item record→no handlers matched→type5 bypasses existence gate→default true→consume→no-op trigger→clear;1/3 alternative fails preconsumption.',premise='Fixed ordinary valid registered item and Bag entry with precisely stated flags/handlers; no concurrent mutation, plugins or malformed target. Hypothetical legal configuration is source-static, NOT_EXECUTED; no claim current compiled dataset contains I.')
row(248,[
 'This formal paragraph explicitly limits ball coverage to command eligibility/registration; capture judgment/store semantics remain separately mapped to WP38.',
 'WP27 inventory and WP28 active-use references preserve per-family execution distinction; no blanket claim every execution path reruns each selection helper.'
],['command','items','battleitems'],'Formal scope boundary plus actual distinct per-family dispatch; does not grant whole referenced documents or capture backend acceptance.',open=['WP27/WP28/WP38 entire formal/source coverage remains separate; only bounded received CRE facts accepted.'])
row(249,[
 'Execution generic qualification failure families1/2/3/5 and missing target family3 refund without clearing choice item.',
 'Normal successful qualification/effect return clears item regardless callback truthiness; family3 later stat-drop check follows clear.',
 'Refund checks consumption and owner/current capacity, not prior-refund history; no once-only marker is written by refund.',
 'Normal end iterates battlers and cancels remaining choices: UseItem with retained item refunds again, then unregister Mega and clear choice.',
 'New command phase directly clears choices only for battlers whose commands can show, without refund call.',
 'Formal faint path directly clears battler choice without refund; later normal ending sees cleared identity.',
 'Capacity error stops before that add; previous inventory or HP changes are retained, and no outer rollback is inferred.'
],['items','command','end','b_change','bag'],'failed item refund leaves identity→either end cancel refund again or new-command/faint direct clear. Precise reached lifecycle decides multiplicity, not callback Boolean.')
row(250,[
 'Conditional ordinary internal wild2v1 no-partner state has two living player users and same able backup T missing1HP, no egg/Embargo/hyper gate; registered POTION record and exact handlers supplied.',
 'Both normal selections see injured T, qualify and consume one from initial2; after both registrations inventory0 and two independent item identities.',
 'First executor requalifies injured T, restores min(20,missing1), clears its identity on normal return.',
 'Second executor resolves same now-full T, CanUse POTION fails hp==totalhp, generic failure returns one item: inventory1 and second identity retained.',
 'One remaining ordinary wild foe poison status, statusCount0 and HP1, without healing/PoisonHeal/MagicGuard or interference, faints from reached normal end-of-round poison and yields win1.',
 'Normal ending cancel of surviving second user refunds retained item again and clears choice, inventory2.',
 'No intervening switch/faint/cancel/new command, no other inventory mutation, enough capacity on both returns and all messages/callbacks normal are necessary vector premises, not universal duplicate-refund behavior.'
],['potionpbs','itemdata','battleitems','itemhandlers','bag','items','command','end','eor','b_change'],'2 selections before execution→same object HP1 restore→second full-HP rejection/refund→poison final foe faint/win→normal ending second refund. Static conditional vector only; compiled data/runtime execution not claimed.',persistence='HP/inventory writes target actual party and global Bag references; whole-object save finite Kernel receipt applies only at its stated save gate. This vector and later reload NOT_EXECUTED.')
row(251,[
 'If foe instead survives with no other outcome, next command phase can-show user directly clears retained item identity; later ending does not return it again and inventory remains1 absent other mutations.',
 'If second user instead formally faints before ending, faint direct-clear removes identity; normal ending likewise leaves inventory1 absent other mutations.',
 'Normal cancellation of a registered, not-yet-executed consumable returns once then clears choice, so repeated normal cancel sees no original item.',
 'Player refund capacity refusal raises before current add; preceding first HP restoration/consumption/refund prefix is not rolled back; outer recovery remains unproved.',
 'Direct5 no-effect/qualification-true vector clears identity and inventory0; it differs from qualification-false retained identity and is preserved as correct prior contract.'
],['items','command','end','b_change','bag'],'Vary one reached lifecycle boundary of prior vector; clear-before-ending prevents repeat, failed add preserves earlier writes; no broad refund transaction guarantee.')
row(252,[
 'Formal explicitly labels duplicate-refund vectors NOT_EXECUTED and future compatibility choice outside this review.',
 'Cross-document synchronization to WP28/WP42 is a formal mapping requirement, not a demanded new refund API/data layout or game execution.'
],['items','command','end'],'Historical contract/scope qualification; source-static review does not set future user compatibility policy.',open=['Full WP28 clauses and global history synchronization remain independently scoped; no whole-document approval.'])
row(253,[
 'Fight selection registers chosen move first, then outside singleBattle calls pbChooseTarget with actual move.pbTarget(battler) data.',
 'Scene target negative result returns false; Fight callback next false continues move menu. Nonnegative registers target and succeeds.',
 'This selection target data can be dynamic move method output; static GameData default alone is not every effect override.'
],['command','movebase','ui_targets'],'move selected→pbTarget→scene target→negative retry/nonnegative register; no execution-neighbor revalidation implied by UI confirmation.')
row(254,[
 'pbMoveCanTarget? rejects target data num_targets==0 before type relations.',
 'NearAlly requires different same-side battler plus near; UserOrNearAlly allows own index or near same side.',
 'AllAllies excludes user and opposing; UserAndAllies includes same side including user.',
 'NearFoe/RandomNearFoe/AllNearFoes require opposing and near; Foe/AllFoes require opposing without near.',
 'NearOther/AllNearOthers require nonself and near; Other requires nonself without near.',
 'These use actual integer target indices in battle permission predicate; UI initial method passing a Battler object must be evaluated separately.'
],['query','priority','targetresolve','ui_targets'],'target data ID/num_targets→opposes?/nearBattlers?→execution target permission; each family relation differs, no inferred equivalence from menu text.')
row(255,[
 'NearAlly initial picker iterates live same-side Battler objects excluding self; calls nearBattlers?(b,idxBattler) with object b, not b.index.',
 'Core integer not-near pair table includes? with Battler object does not match integer entries under default objects; first live nonself ally is therefore chosen even if far by index table.',
 'In normal3v3 subsequent state user0 living, ally2 faint/no backup, ally4 living, initial index4; no live nonself ally only then fallback0; living2 appears first and becomes initial2.',
 'Target text uses genuine integer adjacency and leaves far4 nil (distinct from empty-name faint member); data-box/member selection can highlight4 while no target button is selected.',
 'USE returns current index4 without revalidation, core registers it; maintained live/layout execution rejects far4 and has no nearby living ally fallback in this vector.',
 'NearFoe initial scans direct-opposition order for living near; Foe scans same order living without near; other IDs initially self.',
 'This preserves precise current formal anomaly and genuine WP39 adjacency table; old UI compressed NearAlly description is qualified, not used to reverse correct formal.'
],['firsttarget','query','ui_targets','targetresolve','priority','command'],'UI initial object-argument anomaly→nil label/button versus selected member→USE rawindex registration→execution integer adjacency rejection; source identities and actual method scopes in UI67 reception.',open=['All native rendering/input execution and unrelated move effect target overrides remain NOT_EXECUTED/OPEN; exact finite source-derived vector only.'])
packet={'schema':'car-manually-authored-batch/v1','common_premise':'Fixed R ordinary valid default objects/registered records, no plugin/concurrent mutation; all actual consumers and callback gates explicitly named. Conditional legal vectors are static, not game execution.','common_cancel':'Only reached branch; selection cancellation and callback failure differ. Identity clearing/refund follows exact reached call order.','common_failure':'No transaction/ensure rollback; earlier choice/Bag/HP/messages/effect writes may remain after later error.','common_persistence':'Battle choices runtime; party Pokemon and Bag persistent object references, but full serialization/reload outside finite received Kernel fact remains OPEN and NOT_EXECUTED.','source_dictionary':d,'rows':rows}
(P/'manual_batch_05a.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children']) for x in rows)})
