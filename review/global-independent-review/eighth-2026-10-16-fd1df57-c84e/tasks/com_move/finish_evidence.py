from pathlib import Path
import json, datetime, hashlib, re, subprocess

P=Path(__file__).resolve().parent
W=P.parents[3]
R=Path('/workspace/pokemon-essentials')
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(n,x): (P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
D=json.loads((P/'dependency-facts.json').read_text())
def dep(k,path,intervals,facts,scope='RELEVANT_COMPLETE_UNITS_READ'):
 D[k]={'path':path,'intervals':intervals,'status':scope,'reviewer':'/root/com_move','facts':facts}
dep('AbilitySpeedWeight','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',[[1,365]],[
 'Registry families and wrappers were read through SpeedCalc and WeightCalc. A nil handler return alone invokes the supplied fallback; false and zero are retained.',
 'Chlorophyll/Sand Rush/Slush Rush/Swift Swim double in their matching effective weather. Quick Feet uses viewed status and multiplies speed by 1.5; Slow Start positive halves; Surge Surfer doubles under Electric Terrain without grounding; Unburden needs its marker and current empty item.',
 'Heavy Metal doubles weight; Light Metal takes integer half and clamps to one. The Battler consumer applies ability unless moldBreaker, then item independently.'
])
dep('AbilityStatuses','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',[[411,818]],[
 'Comatose on KOMALA supplies viewed Sleep/any-status and non-ignorable general status immunity even when the ordinary active-ability query would fail. Shields Down immunity requires MINIOR and form below seven.',
 'Ordinary self and ally immunity entries were read individually: Flower Veil requires Grass, Immunity/Pastel Veil poison, Insomnia/Sweet Veil/Vital Spirit sleep, Leaf Guard sunny weather, Limber paralysis, Magma Armor frozen, Water Veil/Water Bubble burn. Ally wrappers preserve their separate activation gates.',
 'Synchronize requires a different source and handles only poison/burn/paralysis, queries the source via synchronization eligibility and submits with no original source; current poison count selects toxic. No recursive source is supplied.',
 'Matching status cures use raw state. Oblivious also clears Attract and generation-six Taunt; Own Tempo clears confusion. Big Pecks covers Defense, Hyper Cutter Attack, Keen Eye Accuracy, Clear Body/White Smoke all ordinary lowering, Grass Flower Veil and ally Flower Veil have their own gates. Full Metal Body is non-ignorable but its active check can still fail under Gastro Acid.',
 'Stat-gain handler family is empty. Competitive and Defiant request two stages only for an opposing or absent source after a loss; this is a reaction after an actual stage write, not a qualification replacement.'
])
dep('AbilityAccuracy','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',[[1040,1193]],[
 'Aerilate/Galvanize/Pixilate/Refrigerate convert Normal only when the destination type exists, then set powerBoost. Liquid Voice changes sound moves to Water; Normalize requires registered Normal and grants powerBoost only in generation seven or later.',
 'User accuracy modifiers: Compound Eyes 1.3; Hustle physical 0.8; Keen Eye clears positive evasion in generation six; No Guard base accuracy zero; Unaware clears damaging target evasion; Victory Star multiplies 1.1 for user and ally independently.',
 'Target modifiers: Lightning Rod electric and Storm Drain water set accuracy zero, No Guard zero, Sand Veil/Snow Cloak multiply evasion 1.25 in matching weather, Tangled Feet halves accuracy while confused, Unaware clears damaging user accuracy stage, Wonder Skin opposing status caps positive base accuracy above fifty to fifty. Caller skips target layer under moldBreaker.'
])
dep('AbilityCritical','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',[[1630,1656]],[
 'Merciless returns ninety-nine for a viewed poisoned target; Super Luck adds one. Target Battle Armor/Shell Armor return negative one. Their ordering in Move calculations lets the target veto precede late always-critical requests unless target layer is skipped.'
])
dep('AbilityInnards','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',[[1853,1891]],[
 'Innards Out requires a fainted target and non-dummy source, then source indirect-damage eligibility; it uses target damageState.hpLost and immediately runs the source HP-item check. It may run while target HP is zero before formal faint handling.',
 'Iron Barbs/Rough Skin require actual contact, source indirect-damage and contact-effect permission; request integer source maxHP/8 and invoke HP-item checks.'
])
dep('ItemStatuses','Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb',[[1,630]],[
 'Registry wrappers preserve nonnil results. Choice Scarf speed 1.5; Iron Ball/Macho Brace/six Power items half; Quick Powder untransformed Ditto doubles; Float Stone integer half clamped to one.',
 'All sixteen HPHeal handlers were read. Confusion berries map Figy attack/Iapapa defense/Mago speed/Aguav special defense/Wiki special attack nature dislikes. Stat berries map Liechi attack/Ganlon defense/Salac speed/Petaya special attack/Apicot special defense. Forced and normal gates differ.',
 'Berry Juice twenty uses half threshold unless forced but always canHeal. Lansat needs pinch unless forced and FocusEnergy below two. Micle rejects when its marker is false and keeps it true on success. Oran ten and Sitrus floor(maxHP/4) use canHeal and the false half-HP helper; Ripen doubles the integer request. Starf builds its legal five-stat pool and samples before calling the low-HP helper.',
 'Aspear/Cheri/Chesto/Pecha/Rawst ordinary matching status cures require berry consumption permission; forced skips that permission. Lum handles raw status and confusion together; Persim confusion only. Mental Herb clears Attract/Taunt/Encore+ID/Torment/Disable counter/Heal Block but leaves DisableMove identity.',
 'Eject Pack checks Sky Drop, opposing survivors, full canSwitchOut, backup and lowered flag, then consumes before a cancellable switch selection; round-end entry leaves first and waits for replacement. Consumption survives a negative selection.'
])
dep('ItemHit','Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb',[[1269,1695]],[
 'Absorb Bulb water special attack, Cell Battery electric attack, Luminous Moss water special defense, Snowball ice attack each query and request one. Air Balloon removal is nonrecoverable and can use Symbiosis. Enigma checks nonsubstitute, no form absorption, super-effective and then healing helper.',
 'Jaboca physical and Rowap special require target berry permission and source indirect eligibility, request integer source maxHP/8, double for target Ripen, damage source and immediately check its HP items. Target ordinary successful-trigger suffix consumes the reactive berry. Kee physical/Maranga special call positive berry handlers.',
 'Rocky Helmet needs actual contact, contact permission and indirect eligibility, then maxHP/6. Sticky Barb requires contact, source alive and empty, then transfers current item and may update matching initial records in wild cases. Weakness Policy requires no form absorption, super-effectiveness and at least one of Attack/Special Attack can rise; it requests two for each legal stat then consumes.',
 'Positive Enigma canHeal then quarter; Kee/Maranga query one stage, Ripen doubles. Normal entries check canConsumeBerry, forced entries can bypass it.',
 'Eject Button needs empty switched set, surviving opponents and backup, consumes before choice and does not call full canSwitchOut. Red Card samples source backup first, consumes, then tests Suction Cups/Ingrain; refusals retain consumption. Successful replacement clears source choice/moldBreaker and records switched seat.',
 'Life Orb needs damaging move, hits positive, source indirect eligibility and one affected nonsubstitute target, then integer maxHP/10. Shell Bell needs canHeal and positive sum of totalHPLost, then integer sum/8. Throat Spray needs both parties alive, sound move, positive hits and a legal special-attack rise; damaging classification is not required.',
 'Leppa selects persistent empty-PP slot first, or forced partial slot, restores ten/Ripen twenty clipped, then directly writes the same-index Battler slot even if Transform changed identity. White Herb resets only negative seven-stage entries to zero and sets the raised flag, preserving positive values.'
])
dep('EOR','Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',[[1,781]],[
 'Full phase ordering and early decisions were read. Future Sight constructs a new dummy first; that initialization can clear live cross-seat references before binding an off-field legal source. A present same-side party identity reuses its actual battler. Counter reaching zero is not a guarantee that delayed attack reaches every later cleanup.',
 'Wish decrements at its position and uses the saved amount and current canHeal. Sea of Fire can decrement once in damage and again in later side-duration loop. All Aqua Ring entries precede all Ingrain, then Leech Seed.',
 'Poison runs for all affected battlers before burn; toxic positive statusCount increments Toxic up to sixteen before Poison Heal/Magic Guard/no-heal checks. Ordinary poison does not increment. Burn takes integer H/16 current or H/8 old, then Heatproof half rounded; shared HP writer enforces eligible minimum one.',
 'Nightmare clears if not viewed asleep before quarter damage; Curse quarter damage. Trapping decrements first, returns without damage at zero, and uses generation-six H/8 or Binding Band H/6 versus old H/16 or H/8. Existing trapped source and move references have separate clearing rules.',
 'Timer helper only processes live battlers with positive counters and calls expiry only on a positive-to-zero transition. DisableMove clears at that expiry; counter already zero after Mental Herb never reaches it. Missing Encore move clears pair; zero PP can zero count while leaving identity. Yawn decrements then invokes its dedicated sleep query.',
 'Perish Song decrements each live counter, deals all remaining HP at zero, checks items/faint, then judges if all zero events have one source side; positive decision returns. Individual-timer, EXP and switching boundaries can stop later EOR phases.',
 'Field counters and terrain expiry use stored state and current defaults; natural Magic Room expiry triggers item checks. Affection cure (enabled/internal/player/level>=4/nonMega) draws and cures at r>=80 before later poison/burn. Octolock asks Defense then Special Defense lowering with no source and checks stat-loss items.',
 'Tail only visits live battlers; charge/hyper/laser/throat counters decrement; LockOn target clears only when its positive timer reaches zero. Counter/Mirror target records reset, damage/history and temporary flags clear, lastRoundMoveFailed copies current. Side Echoed Voice counter resets only when unused, field IonDeluge false, FairyLock decrements and both fusion markers false.'
], 'FULL_READ_DEPENDENCY')
dep('DebugStats','Data/Scripts/020_Debug/003_Debug menus/005_Debug_BattlePkmnCommands.rb',[[178,243]],[
 'set_stat_values snapshots the five getters once, displays cached entries, allows one through 9999 and writes only the selected same-named raw field while updating only that cached slot. Reset invokes pbUpdate and resnapshots all. Wonder Room getters and raw defense writer names thus produce TD22/23 different current-menu and reopened displays.'
])
dep('BattleSettings','Data/Scripts/002_BattleSettings.rb',[[1,140]],[
 'Full battle settings were read: split category, more type effects and immunity switches, critical ratios, paralysis/burn generation-derived policies and affinity defaults are inputs. Global Settings actual generation is eight at 001_Settings.rb lines 7–17; old branches are conditional alternatives, not simultaneously enabled.'
], 'FULL_READ_DEPENDENCY')
dep('TypePBS','PBS/types.txt',[[1,129]],[
 'All nineteen default entries read, including eighteen ordinary plus pseudo QMARKS. Icon order and complete weaknesses/resistances/immunities were compared to type calculations and TD vectors; the full actual records are in read I/O. Hidden Power excludes pseudo/NORMAL/SHADOW and uses remaining seventeen ordered icons.'
], 'FULL_READ_DEPENDENCY')
dep('FlingPBS','PBS/items.txt',[],[
 'Read every one of 578 item identities and its complete Fling/Flags projection; compared all group membership and numeric Fling powers to the formal complete table. This grants relevant-field credit, not unrelated item names/prices/descriptions or every PBS field. Natural Gift fields are separately received from the child complete relevant-record projection.'
], 'ALL_RELEVANT_FIELDS_READ')
child=Path('subreviews/attributes_calling')
for k,name in [('R008-sub','008_MoveEffects_MoveAttributes.rb'),('R012-sub','012_MoveEffects_ChangeMoveEffect.rb')]:
 dep(k,'Data/Scripts/011_Battle/003_Move/'+name,[[1,1620 if k=='R008-sub' else 1330]],[
  'Actual full source read by /root/com_move/attributes_calling, received by /root/com_move by reading all 125 manual unit facts and the complete main-clause breakdown. Each concrete class has qualification/value/write/consumer facts in the child forward mapping; complete compound assertions and actual vectors in child reverse mapping.',
  'Full source rather than name inventory was read; 93 structures in 008 and 32 in 012. Parent finite acceptance retains current predicates and earlier gates, including later Clauses alias behavior and per-hit resource rereads.'
 ],'FULL_READ_BY_NAMED_SUBREVIEW_RECEIVED')
 D[k]['reviewer']='/root/com_move/attributes_calling';D[k]['accepted_by']='/root/com_move';D[k]['evidence']=[str(child/'unit-facts.tsv'),str(child/'main-breakdown.tsv'),str(child/'forward-mapping.json'),str(child/'reverse-mapping.json')]
for k,name,n,scope in [('BattlerUse','007_Battler_UseMove.rb',762,'Use shell; history/PP; distinct special and accuracy flags; Charge action-end and normal Instruct reentry'),('BattlerTarget','008_Battler_UseMoveTargeting.rb',203,'Actual target construction, default User empty set, late Curse rebuild without redirect, redirect order and dynamic target category'),('BattlerSuccess','009_Battler_UseMoveSuccessChecks.rb',595,'Use qualification and target/hit gates, status early returns, reflection/protection, actual type immunity; no universal bypass'),('BattlerTrigger-sub','010_Battler_UseMoveTriggerEffects.rb',218,'Hit records and reaction order, Innards/Jaboca/HP items, target primary effects, Beak Blast nil move-context failure; outer move effects by actual entry')]:
 dep(k,'Data/Scripts/011_Battle/002_Battler/'+name,[[1,n]],[scope,'Full source actually read by the named child; finite source behavior received through its complete caller facts, reverse assertions and vector derivations. Whole Battler formal-domain reverse acceptance is not implied.'],'FULL_READ_BY_NAMED_SUBREVIEW_RECEIVED')
 D[k]['reviewer']='/root/com_move/attributes_calling';D[k]['accepted_by']='/root/com_move'
for k,path,n,f in [('MoveData','Data/Scripts/010_Data/002_PBS data/005_Move.rb',408,'Defaults None type/category2/power0/accuracy100/PP5/TargetNone/priority0/functionNone/flags[]/chance0. GameData display returns actual registered data; dynamic proposed algorithms in comment blocks do not execute. Battle::Move display has the separately read AuraWheel MORPEKO/TransformSpecies exception.'),('TypeData','Data/Scripts/010_Data/002_PBS data/003_Type.rb',141,'Default icon zero/pseudo false; type effectiveness checks weakness then resistance then immunity. Full enum/schemas/default and export were read; existing default records—not arbitrary future content—supply the current table.')]:
 dep(k,path,[[1,n]],[f],'FULL_READ_BY_NAMED_SUBREVIEW_RECEIVED');D[k]['reviewer']='/root/com_move/attributes_calling';D[k]['accepted_by']='/root/com_move'
core=json.loads((P/'io/core-facts-01.json').read_text())
# Core facts were actually read in two continuous batches; keep their original
# native schema and bind finite received facts without granting full CORE scope.
for key in ['CORE-F019','CORE-F030','CORE-F031','CORE-F032','CORE-F034','CORE-F043']:
 D[key]={'status':'FINITE_SOURCE_FACT_RECEIVED','producer':'/root/combat_review','receiver':'/root/com_move','evidence':['../combat_review/source-to-spec.json','io/core-facts-01.json','io/core-facts-02.json'],'fact_id':key[5:],'boundary':'Only this named source fact and its actual conditions; no acceptance of all CORE reverse rows.'}
save('dependency-facts.json',D)
print('dependency fact groups',len(D))
