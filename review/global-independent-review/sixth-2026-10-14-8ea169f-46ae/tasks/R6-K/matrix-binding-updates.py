# Explicit consumer joins from receipts actually read in this review turn.
# This does not give K source-reading or execution credit for another reviewer.
O=json.loads((P/'received-O-cross-interface.json').read_text())
C=json.loads((P/'received-C-cross-interface.json').read_text())
of={x['id']:x for x in O['facts']}
cf={x['domain']:x for x in C['facts']}
ui={x['id']:x for x in json.loads((P/'imported-ui-root-facts.json').read_text())}

def join(doc, first, status, explanation, oids=(), cdomains=(), uids=(), extra=()):
    unit=next(x for x in UNITS if x['formal_path']==SPEC[doc]['path'] and x['start_line']==first)
    r=[]; bindings=[]
    for oid in oids:
        f=of[oid]
        bindings.append({'owner':'R6-O','receipt':'received-O-cross-interface.json','id':oid,'new_fact':f['fact'],'source_read_credit_to_K':0})
        for s in f['source']:r.append(f"{s['path']}:{s['lines'][0]}:{s['lines'][1]}")
    for dom in cdomains:
        f=cf[dom]
        for n,sf in enumerate(f['facts'],1):
            s=sf['source'];r.append(f"{s['path']}:{s['start']}:{s['end']}")
            bindings.append({'owner':'R6-C','receipt':'received-C-cross-interface.json','id':f'{dom}-{n}','new_fact':sf['behavior'],'consumer':sf['consumer'],'source_read_credit_to_K':0})
    for uid in uids:
        f=ui[uid]
        # Individual method ranges are retained in imported-ui-root-facts.json;
        # the enclosing full-class unit is not substituted for K source reading.
        for a,b,_ in f['unit_ranges']:r.append(f"{f['source_path']}:{a}:{b}")
        bindings.append({'owner':'R6-UI/root','receipt':'imported-ui-root-facts.json','id':uid,'new_fact':f['facts'],'source_read_credit_to_K':0})
    r.extend(extra)
    rr=refs(*r)
    for s in rr:
        if s not in unit['necessary_consumer_refs']:unit['necessary_consumer_refs'].append(s)
    unit['previous_binding_status']=unit['status'];unit['status']=status
    unit['new_fact']+=' Current consumer join: '+explanation
    unit['consumer_receipts']=bindings
    unit['evidence']='SOURCE_STATIC_WITH_SEPARATELY_IMPORTED_CURRENT_CONSUMERS'
    unit['does_not_certify_native_execution']=True

join('wp06-time-random-steps-stats.md',1,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'O exact world clock/daynight/tonecache joins K stats and both phone timers. Integer division and actual-second update gates retained.',oids=('O-K-TIME',))
join('wp06-time-random-steps-stats.md',82,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'Normal31-bit step writes precede two notification families; forced/interpreter branch precedes increment. Named counter units and partial callback prefixes remain distinct.',oids=('O-K-STEP31',))
join('wp09-save-startup-continue.md',83,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'Full three25/25/24-line raw switch/variable/selfswitch receipts confirm values0/false/nil and slot5000/5001; convenience refresh belongs owned helper.',oids=('O-K-RAW-SWITCH-VARIABLE',))
join('wp09-save-startup-continue.md',95,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'Fresh LoadScreen228–355 parsed-data validity/backup/menu/language paths join owned StartGame126. Native IO/maps and error presentation still UNKNOWN.',uids=('UI-FACT-0021','UI-FACT-0022'))
join('wp09-save-startup-continue.md',121,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'Owned entire StartGame126 supplies save prewrites and IO-only countrollback; UI save/backup wrappers are separately bound. No file atomicity or host-run guarantee.',uids=('UI-FACT-0021','UI-FACT-0023','UI-FACT-0024'),extra=('reference/pokemon-essentials/Data/Scripts/003_Game processing/001_StartGame.rb:99:126',))
join('wp08-localization.md',1,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'UI Load language switch mutates options and directly writes nonempty parsed save-data; author translation export target remains separate.',uids=('UI-FACT-0022','UI-FACT-0090'))
join('wp10-migration-failure-recovery.md',101,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'Berry constructor initializes all fields and moisture100; own conversion1–420 applies the6/7/8-slot selective legacy writes and retains unassigneddefaults. Constructor does not itself parseold arrays.',oids=('O-K-BERRY-CONSTRUCTOR',))
join('wp10-migration-failure-recovery.md',211,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'Fresh Load recursion/deletion and emergency scene/save order join owned StartGame/Errors/Main. Recovery world notification projection imported, file state/native exit remain unexecuted.',oids=('O-K-STEP31',),uids=('UI-FACT-0021','UI-FACT-0023'),extra=('reference/pokemon-essentials/Data/Scripts/003_Game processing/001_StartGame.rb:1:126',))
join('wp20-hp-status-moves-helditem.md',162,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'C PPwrite104–124 guards realMove ID andTransform; ordinary use source beforePP and item PP helper match. No general after-failure refund guarantee.',cdomains=('WP20',))
join('wp20-hp-status-moves-helditem.md',192,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'C mutable initial/recycle/consumption and terminal item restore join O partner concatenation and captureplayerlist replacement. Old participant list and shiftedinitial can alias incorrectly exactly as scoped.',oids=('O-K-PARTNER',),cdomains=('WP20','WP32'))
join('wp24-player-trainers-partners.md',136,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'C award/loss sources352–404 use actual clamped money differences; own NPC load/default behavior unchanged.',cdomains=('WP24',))
join('wp24-player-trainers-partners.md',200,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'O registration resolver→vehiclecancel→trainerload→callback→owner/stat→storedtuple ordering and same-creature participant concatenation; world partnerheal/unforms precede endnotify.',oids=('O-K-PARTNER','O-K-BEGIN-END-EVOLUTION'))
join('wp36-wild-encounters-and-modifiers.md',100,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'O full469 encounter selector and modifiers73 source receipts bind deepcopied snapshots, chance/accumulator/grace/double/preference/generation and active wrapper. Ownbalanced math and source type/config are retained.',oids=('O-K-EN-SNAPSHOT-PROBABILITY','O-K-EN-GENERATION-WRAPPER','O-K-TIME','O-K-STEP31'))
join('wp32-contextual-trade-and-post-battle-evolution.md',1,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'O current walltime/worldweather inputs join owned entire676 evolutionmethod table; short-circuit and check-time reading, notbattle snapshot, remain source static.',oids=('O-K-TIME','O-K-ROAM-RADAR-BOUNDARY'))
join('wp32-contextual-trade-and-post-battle-evolution.md',34,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'C hitmessage/lossrecord/faint/capture source and O begin/end notifications bind full index scope, ordinarystartguards, XP-beforeworldscan, captureleftshift versus partner mergedinitial, levelup-first scan, clear-after-normalreturn and failureprefix.',oids=('O-K-BEGIN-END-EVOLUTION','O-K-PARTNER'),cdomains=('WP32',))
join('wp32-contextual-trade-and-post-battle-evolution.md',110,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'Wholeparty Event入口 is in owned Evolution647–652, snapshots able_party then loops; singlecheck/scene returnhit versus commitcancel is owned+UI evolution source. No consumed-eventID or retry/Kpersist invention.',uids=('UI-FACT-0047',),extra=('007_Evolution.rb:647:676','001_Pokemon.rb:1047:1059'))
join('wp35-eggs-and-hatching.md',67,'SOURCE_STATIC_OWN_NECESSARY_CONSUMER_SUPPORTED',
     'K additionally fresh-full-read Hatch268: normalstep decrements before dynamic nonEgg scan, clips0 before submit; submit stats/owner/time/firstmoves doesnotsetsteps orguardegg. Animationtrue makesfallbackunreachable, formreads beforestandardDex flags and naming. No host/media executed.',extra=('reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb:1:268',))
join('wp23-shadow-hyper-and-purification.md',86,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'K newly read completePurifyScreen348–628: caller passes screen self to owned purification, no pbUpdate wrapper in that class; levelhelper windowcallback is reached beforeexactfinalExp/store/centerclear. Relic screen hasempty pbUpdate. UI full1308 class/context receipt imported separately.',uids=('UI-FACT-0038',),extra=('reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:348:628','002_ShadowPokemon_Other.rb:106:135'))
join('wp23-shadow-hyper-and-purification.md',130,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED_WITH_STORAGE_SELECTOR_DEPENDENCY_PENDING',
     'UI full1308 math/list/tempo/Lugia/flow and own completeScreen348–628 bind place/noegg, rawShadowequality, uncheckedwithdraw andstore/clear order. Storage mode1 actualnegative-position selection propagation still requires its owncurrentselectorreceipt, so not silently closed.',uids=('UI-FACT-0035','UI-FACT-0036','UI-FACT-0037','UI-FACT-0038','UI-FACT-0040','UI-FACT-0041'),extra=('reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:348:628',))
join('wp64-mail-and-mystery-gift.md',84,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'UI fresh Gift428 source field/queue/codec/authoring groups0042/0043/0077 bind owned HTTP and acquisition/storage/ownercontracts. DuplicateonlineIDs and sourcealiascancel remain limited to their callers. No network/unknownpayloadexecution.',uids=('UI-FACT-0042','UI-FACT-0043','UI-FACT-0077'))
join('wp30-growth-learning-and-friendship.md',126,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'UI evolution195–250 success after cancellable animation joins owned candy/level/experience helpers; choosingcancel versus animationcancel remain distinct.',uids=('UI-FACT-0047',))
join('wp31-basic-evolution.md',156,'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
     'UI actualevolution84–134/195–250 andduplicate5–20 sourceunits join owned species/cache/postaction/items guards; prefixstat/message/postaction/species/Dex/learn andcancellableboundaries intact.',uids=('UI-FACT-0047',))

# These unresolved compound units now have new input but retain specific gaps.
join('wp28-item-use-and-training.md',112,'CURRENT_C_CONSUMER_SUPPORTED_DX_WRITER_PENDING',
     'C itemregistration/refundresidue and cancel/clear/faint/normalterminal consumers are confirmed. PBS enum/Consumable rewrite remainsDX primary; nohandler return-basedrefund invented.',cdomains=('WP28',))
join('wp22-mega-and-primal-reversion.md',37,'CURRENT_C_O_SUPPORTED_FACILITY_RESTORE_BINDING_PENDING',
     'C Megaquotas/registercancel/Primalexecution andfaintdirectunmake plusO worldexplicitunmake/partnerheal are joined. Bareterminalonlycallspeer generalleave/endBattle andrestoresitem, not directspecialunmake. Facility counterpart stillF pending.',oids=('O-K-BEGIN-END-EVOLUTION',),cdomains=('WP22',))
join('wp30-growth-learning-and-friendship.md',79,'CURRENT_C_CORE_GROWTH_SUPPORTED_HELD_MODIFIER_BINDING_PENDING',
     'C coregrowth5–270 supplies eligibility, sequentialfloor, Shadowstaging andlevel/move timings. Heldmodifiers/EOR effectimplementations needtheirprimaryownerreceipt, notonly dispatch existence.',cdomains=('WP30',))

join('wp26-acquisition-gifts-and-script-trade.md',93,'SOURCE_STATIC_OWN_NECESSARY_CONSUMER_SUPPORTED',
     'K additionally full-read Trading243. Statistics precede targetresolution; receivedexistingobject owner/name/provenance mutate beforepresentation. Trade165 reads receivedownpredicate againstoldsender andunconditionallycannotcancel; outerpartyreplacement islast. Dex condition cancallendonceinside thenagainoutside; secondviewportdispose mayfailbeforesecondcheck, hostunknown.',extra=('reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb:1:243',))
join('wp32-contextual-trade-and-post-battle-evolution.md',98,'SOURCE_STATIC_OWN_NECESSARY_CONSUMER_SUPPORTED',
     'Own full Trading243 binds receivedobject predicates andtwo cleanupcalls. First End157–169 disposesbeforechecking; nestedend208 plusouter240 canredisposeviewport beforesecondcheck. No host permit ordouble-evolution guarantee; finalpartywrite242 afterouterendnormalreturn.',extra=('reference/pokemon-essentials/Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb:1:243',))

factory=tuple('reference/pokemon-essentials/Data/Scripts/018_Alternate battle modes/001_Battle Frontier/'+n+f':{a}:{b}' for n,a,b in [
 ('001_Challenge_BattleChallenge.rb',368,427),('002_Challenge_Data.rb',201,218),
 ('003_Challenge_ChooseFoes.rb',88,164),('005_UI_BattleSwap.rb',1,247)])
join('wp57-factory-rentals-and-swaps.md',1,'CURRENT_IMPORTED_F_FACTORY_CONSUMER_JOIN_SUPPORTED',
     'Current F tenfactreceipt binds inclusive-scaled candidates, low/high IV threshold, blanktrainer defaultowner, rentconfirmcount+submit, swapcancelstillunconditionalsubmit, oldfoe same-reference snapshot andsceneend-before-slotassignment. Candidateerror/retry noensure retains temporaryrulescount; nativeUI/RNGnotexecuted.',extra=factory)
u=next(x for x in UNITS if x['formal_path']==SPEC['wp57-factory-rentals-and-swaps.md']['path'] and x['start_line']==1)
u['consumer_receipts'].append({'owner':'R6-F','receipt':'imported-F-factory-stat-restore-facts.json','ids':['F-A08','F-A09','F-B04','F-C03','F-U01','F-U02','F-U03','F-U04'],'source_read_credit_to_K':0})
join('wp22-mega-and-primal-reversion.md',37,'CURRENT_STATIC_C_O_F_CONSUMER_JOIN_SUPPORTED',
     'Fresh F-E02 organizedbattle wrapper restores both positional oldEXP, heals eachmember, explicitly unMega/unPrimal, thenitem restore after normalbattle. This closesFacilitycontrast only; interruptednormal tail isnotpromised.',extra=('reference/pokemon-essentials/Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb:40:144',))
u=next(x for x in UNITS if x['formal_path']==SPEC['wp22-mega-and-primal-reversion.md']['path'] and x['start_line']==37)
u['consumer_receipts'].append({'owner':'R6-F','receipt':'imported-F-factory-stat-restore-facts.json','id':'F-E02','source_read_credit_to_K':0})

# Bag and BP authored fact-group receipts (all listed groups actually read).
bagall=json.loads((P/'imported-ui-party-storage-bag-facts.json').read_text())
bag={x['id']:x for x in bagall if (x.get('id') or '').startswith('BAG-FACT-')}
bag.update({x['id']:x for x in json.loads((P/'imported-ui-BP-facts.json').read_text())})
def bagjoin(doc, first, ids, status, text):
    u=next(x for x in UNITS if x['formal_path']==SPEC[doc]['path'] and x['start_line']==first)
    for i in ids:
        f=bag[i];s=f['source'];a,b=s['lines'];ref=refs(f"{s['path']}:{a}:{b}")[0]
        if ref not in u['necessary_consumer_refs']:u['necessary_consumer_refs'].append(ref)
        u.setdefault('consumer_receipts',[]).append({'owner':'R6-UI/bag','receipt':'imported-ui-BP-facts.json' if int(i[-3:])>=37 else 'imported-ui-party-storage-bag-facts.json','id':i,'new_fact':f['fact'],'source_read_credit_to_K':0})
    u['previous_binding_status']=u['status'];u['status']=status;u['new_fact']+=' Current UI bag/BP join: '+text
bagjoin('wp29-shops-and-exchanges.md',1,tuple(f'BAG-FACT-{i:03d}' for i in [24,26,30,31,33,34,35,36,37,39,42,45,46]),
        'CURRENT_IMPORTED_UI_SUPPORTED_WITH_GREETING_PROPOSAL_ROOT_PENDING',
        'Money/BP full transactions andhalfdisplay match the ownedcontainer/resources. BP providedgreeting onlyonecustom replacesbothdefaults; WP29:88 compoundwelcomeclaim belongs alreadyreported GR6-UI-BAG-001, importedexistingproposal not a new K rootcause. Preservetwofarewells/normalpricesclear; failureskeep reachedprefix.')
bagjoin('wp29-shops-and-exchanges.md',110,('BAG-FACT-024','BAG-FACT-034','BAG-FACT-035','BAG-FACT-036','BAG-FACT-037','BAG-FACT-045'),
        'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
        'Itemdefaultprices andpositive/zerooverride predicate joins actualUIreaders; eventoverride writer itself remains explicit formalinput, with upperbound assumptions not propagated tocontenttext.')
bagjoin('wp27-bag-and-item-storage.md',113,('BAG-FACT-011','BAG-FACT-012','BAG-FACT-013','BAG-FACT-014'),
        'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
        'Temporary bagchooser restores browsing onlynormalend, PC transfer capacityprobe→checkeddelete→checkedadd→refresh→message; ordinaryquantity andimportantwholeactualstack differ fromdisplay1. No confirmation isadded todeposit/withdraw.')
bagjoin('wp27-bag-and-item-storage.md',157,('BAG-FACT-002','BAG-FACT-009'),
        'CURRENT_STATIC_CONSUMER_JOIN_SUPPORTED',
        'Actualimportanticon andcommandconstruction keep directregister versuseligibility; quickfieldcollection helperowned. Legacyregistered fields remain correctlymigrated, noK001spillover.')

DX={x['id']:x for x in json.loads((P/'received-DX-compiler-facts.json').read_text())}
def dxjoin(doc,first,ids,text):
    u=next(x for x in UNITS if x['formal_path']==SPEC[doc]['path'] and x['start_line']==first)
    for i in ids:
        f=DX[i];s=f['source'];r=refs(f"{s['path']}:{s['start_line']}:{s['end_line']}")[0]
        if r not in u['necessary_consumer_refs']:u['necessary_consumer_refs'].append(r)
        u.setdefault('consumer_receipts',[]).append({'owner':'R6-DX/compiler','receipt':'received-DX-compiler-facts.json','id':i,'new_fact':f['fact'],'qualification':f['assessment'],'source_read_credit_to_K':0})
    u['previous_binding_status']=u['status'];u['status']='CURRENT_IMPORTED_DX_STATIC_CONSUMER_JOIN_SUPPORTED'
    u['new_fact']+=' Current DX join: '+text
dxjoin('wp02-rule-configuration-and-data-variants.md',213,['FACT-018','FACT-019','FACT-021'],'Discovery top-level exactbase/underscore suffix versus fixed facilitymaster andstartup-onlypreflight; legalbackup existence never active/compatibility proof.')
dxjoin('wp03-content-identity-and-schema.md',118,['FACT-002','FACT-003','FACT-008','FACT-011','FACT-013','FACT-014','FACT-022','FACT-025','FACT-030','FACT-031','FACT-038','FACT-040','FACT-044','FACT-053'],'Actual parser/producers/writers bind strict atoms, exactinlineenums, optional groups andsix-stat column mapping; ordinary repeated properties versus singularEvolutionappend and class exceptions retain scoped fail-before-register/partialprefix.')
dxjoin('wp28-item-use-and-training.md',112,['FACT-028','FACT-048'],'Item constructor Consumable false override retains explicitfalse; generic falseomission rule doesnot overwriteordinarynonconsumable semantics. Battledebit/refund sourceC alreadybound separately.')
dxjoin('wp33-daycare-and-breeding-session.md',1,['FACT-057','FACT-066'],'Map/event old-call replacements preserve exact recognized35text pairs and entry syntax; own/O session/generator facts retain caller versusmacro distinctions.')
dxjoin('wp36-wild-encounters-and-modifiers.md',1,['FACT-008','FACT-036','FACT-052'],'Encounter headers/chances permissiveintegerprefix, strictslots/merge/sort/repeatedtype replacement andwriterzero/nonpositive omissions are source-bound; O deepcopied currentmap snapshot doesnotrefresh merelyfromcompile.')
dxjoin('wp31-basic-evolution.md',1,['FACT-030','FACT-031','FACT-049'],'Base/form forwardevolution inputs and reverseprefermatchingform thenbasefirstfound bind author merge andruntimefamily/extraction; extraction canmutate numeric nestedparams, KL29 preserved.')
dxjoin('wp37-roaming-and-poke-radar.md',134,['FACT-057','FACT-066'],'Persistent migrations andorderednotificationsowned; currentDebug branch sourceO/R6-DX finaldomain fullreview exists, no passivecompiledsave orUI proof.')
for u in UNITS:
 if u['formal_path'].endswith('test-catalog/generic-kernel-wp02-03-04.md') and u['start_line']>=37:
  u['status']='DERIVED_VECTOR_CURRENT_DX_PRODUCER_WRITER_BOUND'
  u['consumer_receipts']=[{'owner':'R6-DX/compiler','receipt':'received-DX-compiler-facts.json','ids':list(DX),'source_read_credit_to_K':0,'scope':'All70current factgroups read; vectors remain unexecuted.'}]

join('wp02-rule-configuration-and-data-variants.md',173,'SOURCE_STATIC_OWN_NECESSARY_CONSUMER_SUPPORTED',
     'K additionally full-read BattleSettings140, all30constants/generation expressions anddefaults; thirty declarations/26displayrows notthirtyindependent activatedfeatures.',extra=('reference/pokemon-essentials/Data/Scripts/002_BattleSettings.rb:1:140',))
join('wp30-growth-learning-and-friendship.md',79,'SOURCE_STATIC_OWN_HELD_MODIFIERS_WITH_CURRENT_C_CONSUMERS_SUPPORTED',
     'K complete ItemEffects dispatcher1–215 plusLuckyEgg and7EVcallbacks1696–1746 read: expinteger3/2, allMacho yields×2, exactsixPowerstat +8/+4. Expabsent−1 versusEVabsentfalse andC current/initial fallback areexplicit; no activeheld-use orconsumption guardis invented here.',extra=('reference/pokemon-essentials/Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb:1:215','reference/pokemon-essentials/Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb:1696:1746'))
join('wp23-shadow-hyper-and-purification.md',130,'SOURCE_STATIC_OWN_SELECTOR_WITH_CURRENT_UI_MODEL_SUPPORTED',
     'Own completeStoragechoose1964–2021 joins owncontainernegativeaddressing andUI mode1 input912–937: mappedempty skipsouterloop; nonemptySelectreturnsrawnegativeposition. Ownscreenplace/replacerawshadoweq andunconditionalpost-storeclear alreadyread; finiteUI modelmath andsamelevel/crosslevel failures separatelybound.',extra=('reference/pokemon-essentials/Data/Scripts/016_UI/017_UI_PokemonStorage.rb:1964:2021','reference/pokemon-essentials/Data/Scripts/016_UI/017_UI_PokemonStorage.rb:912:937'))

def imported_manual(doc,first,status,text,source_refs,receipt,ids):
    u=next(x for x in UNITS if x['formal_path']==SPEC[doc]['path'] and x['start_line']==first)
    for s in refs(*source_refs):
        if s not in u['necessary_consumer_refs']:u['necessary_consumer_refs'].append(s)
    u['previous_binding_status']=u['status'];u['status']=status;u['new_fact']+=' Exact current imported interface: '+text
    u.setdefault('consumer_receipts',[]).append({'receipt':receipt,'ids':ids,'source_read_credit_to_K':0,'own_reference_execution_credit':0})

part='reference/pokemon-essentials/Data/Scripts/016_UI/005_UI_Party.rb'
sto='reference/pokemon-essentials/Data/Scripts/016_UI/017_UI_PokemonStorage.rb'
relearn='reference/pokemon-essentials/Data/Scripts/016_UI/022_UI_MoveRelearner.rb'
imported_manual('wp25-party-and-storage.md',121,'CURRENT_IMPORTED_UI_GUARD_CONSUMER_JOIN_SUPPORTED',
 'UI store/hold/place/swap/release guards andpreserveRaroundhealing, plusmode1 selector andcurrentbox cancellation areexactlybounded; no guardisadded tolowlevelcontainer.',
 (f'{sto}:1689:1881',f'{sto}:1964:2021'), 'imported-ui-storage-required-facts.json',['UI-ST-S-1689','UI-ST-S-1724','UI-ST-S-1770','UI-ST-S-1784','UI-ST-S-1813','UI-ST-S-1845','UI-ST-S-0912'])
imported_manual('wp28-item-use-and-training.md',1,'CURRENT_IMPORTED_UI_SELECTION_CONSUMER_JOIN_SUPPORTED',
 'Party itemfilter/normalBag commands andtemporarychooser restore join owneditemhandlers; ordinarynonEggfilter includesfainted andonSuccess/cancel remainslastpath.',
 (f'{part}:704:744',f'{part}:1394:1420','reference/pokemon-essentials/Data/Scripts/016_UI/007_UI_Bag.rb:458:601'), 'imported-ui-party-storage-bag-facts.json',['R6-UI-party-P017','R6-UI-party-P040','BAG-FACT-009','BAG-FACT-011'])
imported_manual('wp28-item-use-and-training.md',321,'CURRENT_IMPORTED_UI_REENTRY_CONSUMER_JOIN_SUPPORTED',
 'Currentparty permitsstoragebridge, SPECIAL targetselector retains sourceobject; FLYcancel reopenswithoutbridge. UI panels read dynamicform at refresh before outeronSet, ownHOOPA/fullfusion handlersbind result. BoxLink permanentgates do not guarantee every reopenedscene permission.',
 (f'{part}:474:527',f'{part}:745:800',f'{part}:1204:1213',f'{part}:1288:1313',f'{part}:1394:1407'), 'imported-ui-party-storage-bag-facts.json',['R6-UI-party-P011','R6-UI-party-P018','R6-UI-party-P032','R6-UI-party-P034','R6-UI-party-P040'])
imported_manual('wp30-growth-learning-and-friendship.md',154,'CURRENT_IMPORTED_UI_C_LEARN_CONSUMER_JOIN_SUPPORTED',
 'UI emptyrelearn initialstrictdetail precedesinput, candidate nonoverlappingfirst-recordorder andoutercancel/retry cycles areactual; C battlelearn andownedgenerallearn shareforget UIbutnotcommit/PP semantics.',
 (f'{relearn}:1:199','reference/pokemon-essentials/Data/Scripts/016_UI/006_UI_Summary.rb:1355:1367'), 'imported-ui-trade-relearn-facts.json',['R6-UI-party-R002','R6-UI-party-R003','R6-UI-party-R005','R6-UI-party-R006','R6-UI-party-R007'])
imported_manual('wp64-mail-and-mystery-gift.md',56,'CURRENT_IMPORTED_UI_PC_MAIL_CONSUMER_JOIN_SUPPORTED',
 'Actualmailboxgiver926–957 attaches aftermessage thenreads mismatchedmail nil beforehelditem; sourcegetterselfclears. Ownedgiving/takepartialprefixes preserved, normalreadalreadyconsumes storedsnapshot.',
 (f'{part}:926:957','reference/pokemon-essentials/Data/Scripts/016_UI/019_UI_PC.rb:58:105'), 'imported-ui-party-storage-bag-facts.json',['R6-UI-party-P023','R6-UI-party-P038','R6-UI-party-P041','R6-UI-party-P042'])

# Final exact intersections. Unknown host/data activation is a named boundary,
# not an unreviewed source dependency and not a runtime PASS.
extraC=json.loads((P/'received-C-final-addendum.json').read_text())['source_facts']
def cj(doc,first,indices,text):
    ss=tuple(f"{extraC[i]['path']}:{extraC[i]['start']}:{extraC[i]['end']}" for i in indices)
    imported_manual(doc,first,'CURRENT_IMPORTED_C_EXACT_CONSUMER_JOIN_SUPPORTED',text,ss,'received-C-final-addendum.json',indices)
cj('wp21-dynamic-forms-and-display.md',236,[5,6,7,8],
   'Current C exactchange/form-familyguard156–296/Transform297–325/entry274–375/Peer39–59 bind eachstarting/entering/leavingEOR/status/move callback. Marking/ribbonUI currentSummary/Storagefacts are separatelyread, not a new mutable-field or host guarantee.')
cj('wp23-shadow-hyper-and-purification.md',60,[0,1,2,3,4],
   'Call actualShadow+effectiveHyper clearsstoredflag thenheartcall; normalcompletion afterXP/Arena andnonNonechoice triggersHyper beforeEndTurn. Obedienceearlyinternal/ownership/continuation guards precedeORHyper; EOR earlierH/24 no indirect-immunity query, later10%selfEffects andform703 are distinct. OwnShadowoverride supplies truebinding, not corestub.')
cj('wp23-shadow-hyper-and-purification.md',1,[1,5,6,7,8],
   'Current C entry/form/Transform are joined; own ShadowOther413–460 savesstart-heart perpartyindex andendreads it. ExactC catch35–80 shifts L0/K/D/initial only, not heart array; fixedpartial/capture scopes preserved.')
join('wp06-time-random-steps-stats.md',135,'SOURCE_STATIC_OWN_NECESSARY_RANDOM_CONSUMER_SUPPORTED',
     'Fresh complete generate428–450 establishesseedpriority/clear/srand beforeusable-sizegate. Fresh recorder129–133 andplayback188–192 append/reuseorder withoutrequested-bound requery; no originalmethod ordeserializationexecution, globalunrecordedrandom remainsunknown.',extra=('reference/pokemon-essentials/Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb:428:450','reference/pokemon-essentials/Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb:129:133','reference/pokemon-essentials/Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb:147:192'))
join('wp37-roaming-and-poke-radar.md',81,'SOURCE_STATIC_OWN_BICYCLE_WITH_CURRENT_O_RADAR_SUPPORTED',
     'Fresh entireMount600–609 confirmsalready-ridingearlyreturn; newbike writesstate/stat/vehicle/audio beforecancel. Normalcompletedmount immediatelyclearschain, mediainterruption doesnotguaranteecancel. OwnRadar full267 suppliesall7internalcancels andbattery/statnonclear.',extra=('reference/pokemon-essentials/Data/Scripts/004_Game classes/008_Game_Player.rb:587:616',))
join('wp35-eggs-and-hatching.md',1,'SOURCE_STATIC_OWN_EGG_SUMMARY_WITH_CURRENT_DX_EDITOR_SUPPORTED',
     'Fresh complete drawPageOneEgg481–540 confirmsfourorderedthresholdintervals. OwnedSpecies455 suppliesHatchSteps schema/default; DX completepropertyeditor/Debug traceonhatchcounter iscurrentdelegatedsource, onlylayer-specificpositive/editorlimits claimed.',extra=('reference/pokemon-essentials/Data/Scripts/016_UI/006_UI_Summary.rb:481:540',))
u=next(x for x in UNITS if x['formal_path']==SPEC['wp06-stats-directory.md']['path'] and x['start_line']==1)
u['status']='NAMED_STATS_DIRECTORY_SCOPE_WITH_CURRENT_WRITER_INTERFACES'
u['new_fact']+=' Full74 declaration/default/read-query catalog verified in ownStats200. The actualdirectory names knownwriterfamilies andexplicitly retains source-unknown entries; no exhaustive/all-caller claim is added. C money/XP/items andO step/phone/daycare writerreceipts plusUI shops/gifts/hatch are bound elsewhere in namedunits andcrosscatalog. Unlocatedeventwriters remain namedunknown, not asserted absent.'
u['consumer_receipts']=[{'receipt':'received-C-cross-interface.json','domains':['WP24','WP28','WP30'],'source_read_credit_to_K':0},{'receipt':'received-O-cross-interface.json','ids':['O-K-STEP31','O-K-DAYCARE-BRIDGE'],'source_read_credit_to_K':0}]
u=next(x for x in UNITS if x['formal_path']==SPEC['wp29-shops-and-exchanges.md']['path'] and x['start_line']==1)
u['status']='IMPORTED_EXISTING_UI_GREETING_PROPOSAL_ROOT_ADJUDICATION_RESERVED'
u['root_adjudication_required_for_existing_foreign_proposal']='GR6-UI-BAG-001';u['consumer_dependency_pending']=False

# Complete finite literal tables: current D author-field rules + newly read
# actual table-comparison receipt, with a separate own142 primitive comparison.
lit=json.loads((P/'finite-data-validation.json').read_text())
assert all(x.get('match') is not False and ('matches' not in x or x['matches']==1) for x in lit['checks'])
data_rows=json.loads((P/'received-D-shadow153-comparison.json').read_text())
assert len(data_rows)==153 and all(all(v for k,v in x.items() if k.startswith('matches_')) for x in data_rows)
def datajoin(doc,first,text,refs0=()):
    u=next(x for x in UNITS if x['formal_path']==SPEC[doc]['path'] and x['start_line']==first)
    u['previous_binding_status']=u['status'];u['status']='CURRENT_D_AUTHOR_RULES_WITH_FINITE_LITERAL_COMPARISON_SUPPORTED'
    u['new_fact']+=' Current finite data binding: '+text
    u['consumer_receipts']=[{'owner':'R6-D/pbs-bulk','receipt':'field-semantic-rules.json / record-author-scope-coverage.json','scope':'116 author rules, not everydownstream effect or manual transcriptionof206649 lines','source_read_credit_to_K':0},{'receipt':'finite-data-validation.json','evidence':'TOOL_VALIDATION_LITERAL_DATA_ONLY','scope':'48Mega/47stones/ring/orbflags,57contextrows/35counts,153Shadow comparisons; no referencefunctionexecution/source-readcredit'}]
    for s in refs(*refs0):
        if s not in u['source_refs']:u['source_refs'].append(s)
datajoin('wp22-transformation-data.md',1,'All48 printedtargettuples/requirements/Unmega defaults/MegaMessage and47stoneflags/ring/orbnonMega flagsmatchactualcurrentrecords. Independentliteralparser initialplural-only andlast-singular losseswere invalidtooloutputs, preservedandrepaired, never sourcefindings.')
datajoin('wp22-transformation-data.md',69,'METAGROSS sourceMega95/base80 is among48checkedrows; ownstatformula140→155 andHP70→85/reverse remain derivedmath, notreferenceexecution.')
datajoin('wp32-context-inputs-and-scenarios.md',1,'All35 printedmethodcounts matchrawcurrentbase/form Evolution rows withrepeatedsingular retained; existence of registeredmethodsource676 separatelyowned.')
datajoin('wp32-context-inputs-and-scenarios.md',47,'All57 printedsource/target/method/parameter rows eachhaveexactmatching currentPBSline. Sixmapflag/weather cases arecurrentDsemanticnotes item10 plusliteralmetadata relations; thisdoesnot proveevents/maps orweatheractivation.')
datajoin('wp23-shadow-data-and-vectors.md',61,'All153 D literalrowsactuallyreceived/read:131 gauge+orderedmoves,18 SHADOW effectIDs,4itemuses/prices/noFlags. Optionaldata isnotinstalled orcompiled; SHADOWSHED unmatchedRemoveAllScreens remains a namedfunctiondispatch boundary.')
datajoin('wp23-shadow-hyper-and-purification.md',112,'Currentfouroptionalitems noScentflag/uses/prices bind ownedScent/TimeFlute entrygates; successfulhandlerdoesnot prove normalHyper canenteritsince ordinaryflag gateblocks.')
datajoin('wp21-dynamic-forms-and-display.md',1,'Ownentire792 formregistry isexacttriggerdata; D author-field rule/effectivebase inheritance/presence isconditionedonvalidcontent. Fixedliteralfieldtuples and mediaexistence aredifferentdomains; no otherwise-unprovedmap/clock/assetresult inferred.')
u=next(x for x in UNITS if x['formal_path']==SPEC['wp19-attributes-ability-and-stats.md']['path'] and x['start_line']==117)
u['status']='CURRENT_F_TEMPLATE_EV_WITH_D_AUTHOR_RULES_SUPPORTED';u['new_fact']+=' CurrentF B201–218 directEV dividebyemphasiscount andemptytrainer arebound; D all2770templaterecords have1–6 distinctrecognizedeffortatoms. Double255/twoefforts, four127sum508 andordinarycultivationcaps remain separate; rawruntime storage isnotnormalized.'
u['necessary_consumer_refs'].extend(refs('reference/pokemon-essentials/Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb:201:218'))
u['consumer_receipts']=[{'receipt':'imported-F-factory-stat-restore-facts.json','id':'F-B04','source_read_credit_to_K':0},{'owner':'R6-D','receipt':'semantic-notes.md / facility-effort-move-domains.json','scope':'2770 literaltemplates anddistincteffortatom counts only; no generated/runtime approval','source_read_credit_to_K':0}]
u=next(x for x in UNITS if x['formal_path']==SPEC['wp23-shadow-data-and-vectors.md']['path'] and x['start_line']==37)
u['status']='CURRENT_UI_MODEL_OWN_PURIFY_HELPERS_DERIVED_VECTORS_BOUND';u['new_fact']+=' CurrentUI model52–284/Screen348–628 andowncompletepurification/levelhelper bindflow/tempo/Lugia/callbackfailure. Vectorsremainunexecutedandpredicated; source/privateclock/graphics unknowns retained.'
u['necessary_consumer_refs'].extend(refs('reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:52:284','reference/pokemon-essentials/Data/Scripts/016_UI/023_UI_PurifyChamber.rb:348:628'))
u=next(x for x in UNITS if x['formal_path']==SPEC['wp37-roaming-and-poke-radar.md']['path'] and x['start_line']==1)
u['status']='CURRENT_O_C_CORE_ROAM_WITH_NAMED_EFFECT_INTERFACE_SUPPORTED';u['new_fact']+=' CurrentO fullRoam228+wrapper creation andC terminalPeer/effects dispatch bind persistentparticipant andnotificationreceiver. OrdinaryNaturalCure andendRegenerator exception followcurrentAbilityeffectowner; no fixedHP/status/frozenitem guarantee. Nilrouteversusempty[] andpost-extra finalcandidate interpretation retained.'
u['consumer_receipts']=[{'receipt':'received-O-cross-interface.json','ids':['O-K-ROAM','O-K-EN-GENERATION-WRAPPER'],'source_read_credit_to_K':0},{'receipt':'received-C-final-addendum.json','id':8,'source_read_credit_to_K':0}]

# Recompute catalog inherited qualifications after all final joins.
byid={x['id']:x for x in UNITS}
for u in UNITS:
 if u.get('primary_unit_ids'):u['parent_binding_statuses']={i:byid[i]['status'] for i in u['primary_unit_ids']}

# Catalog rows keep the actual limitations of their newly joined parent units.
byid={x['id']:x for x in UNITS}
for u in UNITS:
    if u.get('primary_unit_ids'):
        u['parent_binding_statuses']={i:byid[i]['status'] for i in u['primary_unit_ids']}

# Final freshly read roam effect callbacks/debug commands, preserving native uncertainty.
join('wp37-roaming-and-poke-radar.md',1,'CURRENT_O_C_CORE_ROAM_WITH_OWN_EFFECT_CALLBACKS_SUPPORTED','Fresh complete NaturalCure3098–3103 clearsstatus evenendbattle; Regenerator3105–3111 explicitlyskipsendbattle. TerminalC504 effectiveabilitydispatch endbattletrue beforePeerleave suppliesexactconsumer, not a genericstatuspreservation claim.',extra=('reference/pokemon-essentials/Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb:3098:3111','reference/pokemon-essentials/Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb:499:511'))
join('wp37-roaming-and-poke-radar.md',134,'SOURCE_STATIC_OWN_DEBUG_WITH_CURRENT_NOTIFICATION_PERSISTENCE_JOIN_SUPPORTED','Fresh entirepbDebugRoamers461–548 establishesallRM28 subcases; parentDX exactmethodreceipt confirmscurrentreview. Nativewindow/input/audio may interruptprefixes, nohostobservation.',extra=('reference/pokemon-essentials/Data/Scripts/020_Debug/003_Debug menus/003_Debug_MenuExtraCode.rb:461:548',))
for cu in UNITS:
 if cu.get('primary_unit_ids'):
  cu['parent_binding_statuses']={i:byid[i]['status'] for i in cu['primary_unit_ids']}
  cu['necessary_consumer_refs']=list({(r['path'],r['start_line'],r['end_line']):r for i in cu['primary_unit_ids'] for r in byid[i]['necessary_consumer_refs']}.values())
