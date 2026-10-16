import datetime,hashlib,json,pathlib,subprocess
P=pathlib.Path(__file__).resolve().parent
selected_path=P/'battler-finite-selected-input.v1.json'
raw=selected_path.read_bytes(); selected=json.loads(raw)
ledger=json.loads((P/'reading-ledger.json').read_text())
records=[]
def record(ident,meaning,premise,units,formal,remaining):
 records.append(dict(id=ident,status='RECEIVED_FINITE_WITH_EXPLICIT_PREMISES',received_original_complete_object=next(x for x in selected['selected_complete_facts']if x['complete_object']['id']==ident),accepted_meaning=meaning,premise=premise,own_complete_necessary_definitions=units,current_formal_comparison=formal,cancel_failure_partial_prefix='Actual reached callbacks/scene/diagnostic/array/setter operations may fail after prior writes. No transaction, implicit finally, universal termination or runtime execution is inferred.',remaining_exact=remaining))
record('RX-CORE-SET',
 ['Constructor creates one shared field, two side objects, runtime choices/result and party-indexed restore/recycle/Belch/Bond/corrosion/used arrays; allBattlers returns only nonnil currently living actors.',
  'Side parity alone does not mean player-owned: owner mapping/party-start segments matter. LastInTeam considers current owner segment and able Pokemon, maximizing current partyOrder.',
  'Global ability query returns the first effective bearer object or nil. Effective-weather suppression is queried separately from field.weather storage.'],
 ['Fixed constructor/owner/current-party data, valid active-ability predicates, no arbitrary external mutation. Defaultparty/side-size defects already root-qualified are not erased.'],
 ['E036 whole867 previously actually read: initialize98–174, owner mapping/segment methods, LastInTeam418–429, allBattlers448–450, global queries487–498; Battler abilityActive/hasActiveAbility/effectiveWeather own whole777/476; constructor callbacks and nil/native failure remain their own gates.'],
 ['WP39§2 distinguishes participant/side/owner/partner identities and temporary context; WP41 replacement-message and Illusion contracts use current order. Existing COM002/003 and all qualified correct ranges remain.'],
 ['Every field/ability-specific downstream handler and all species-form behavior are not granted by a constructor/query fact.'])
record('RX-CORE-SWAP',
 ['Opposing order/near selection depends on declared side sizes. Swap rejects missing actor/opposite side/different current owner; then swaps actor objects and indices, choice slots and sprites.',
  'Ten live-recipient pointer effects are remapped; LeechSeed is excluded because it targets a position, PerishSongUser need not change side. Counter damage amount is not a pointer and is not changed by that loop.'],
 ['Valid current indices/owners and normal scene return; selection CanShift and low-level executor remain separate predicates.'],
 ['E036 own whole867: complete Swap602–635, complete opposing-order and near methods previously read; UseMove ProcessTurn5–56/Begin/Cancel for actual acting-cost consumer. Fresh captured602–648 confirms complete Swap and following context.'],
 ['WP41§6 and WP40 Shift preserve the exact ten effects/two exceptions and acting-cost boundary; source fact does not create a new defect.'],
 ['Arbitrary scene exception/saved actor aliases/plugin pointer effects remain OPEN outside this exact list.'])
record('RX-CORE-ENTRY',
 ['Entry resets events only unless skip flag, sorts cached speed, filters actual entrants/liveness, then participation/message/position effects/hazards/faint branch/form/Primal/continual/entry ability/primordial/item/status cure.',
  'Its final scan is per member itemOnStatDropped first, then abilitiesOnDamageTaken, stopping at first truthy within this scan. Recursive entry may run more scans; not a global one-trigger guarantee.'],
 ['Current cached priority entry exists, live entrant and each callback-specific active/faint/suppression condition; complete localbreak versus recursion distinction.'],
 ['E039 own whole469: complete Entry316–374, participation376–383/message385–391, complete position394–423; AbilityAndItem own whole476 and previously actual complete default exit handlers; Priority own279.'],
 ['WP41§4.2 item-before-ability per-member ordering and recursive replacement preserve correct scope. GR8-COM-008 only fixed-summary order phrase remains the independently accepted separate issue.'],
 ['Remaining exact concrete entry/hazard/form/ability/item handler consumers retain their individual OPEN obligations.'])
record('RX-CORE-ROUNDS',
 ['Priority entries store speed/tie/brackets. Full recalculation redraws tie ordering/rebuilds brackets; incremental refresh rereads eligible speed/move-priority changes and preserves prior tie/bracket states.',
  'Truant alternates action permission at its own gate; Stall registered priority bracket differs. These identities are not interchangeable.'],
 ['Valid nonnil actor/choice/handler results; full versus incremental configuration gates and TrickRoom comparison have their actual scopes.'],
 ['E017 own whole279, complete CalculatePriority136–262/Priority264–278 and helpers; SuccessChecks own595 Truant gate; AbilityEffects own3208 concrete PriorityBracketChange STALL registration.'],
 ['WP40§6 full/incremental order contract retained. Existing COM001 precisely corrects WP40:257 Truant example to Stall; no new root/count or reopening correct WP48.'],
 ['All ability/item ordering families and malformed callback return totality remain independently scoped.'])
record('RX-CORE-LOG',
 ['PBDebug.logonerr uses bare rescue for ordinary errors. If all diagnostic log/backtrace/print/flush operations return normally there is no explicit rethrow; wrapper return lets the caller continue.',
  'Diagnostic failure, nonordinary exception and outside-wrapper failure differ. No completion stamp or rollback is synthesized.'],
 ['Exception reaches this wrapper; diagnostic functions themselves must return for the no-rethrow continuation. No debuglog file/game/input was executed.'],
 ['E175 complete logonerr4–17/flush19–24 freshly read; own full77 previously actual. ProcessTurn5–56 and BattleLoop322–347 actual caller definitions, Errors full94 previously actual for diagnostic formatter.'],
 ['WP40§5.2.3 and WP42§3/§8 explicitly separate diagnostic return, lastRoundMoved write and conditional same-round reselection. Current correct paragraphs are retained.'],
 ['All host/UI/input exception collections and global progress/termination are not certified.'])
record('RX-CLAUSES',
 ['Loaded sleep/freeze/Yawn wrappers test their rule and current party status before base predicate; status census skips nil/egg, does not add a fainted filter.',
  'Dedicated wrappers are not automatically called by every direct status setter/transfer. Clauses EOR wrapper calls base then zero-decision suddenDeath; it does not write moldBreaker=false.'],
 ['Loaded aliases at fixed source, exact requested status and current party; generic setter/transfer must follow its actual independent call path.'],
 ['E024 own whole306, fresh complete40–101 wrappers/status census; Statuses own575 and Battler status setter own777; whole EOR781.'],
 ['WP40 clause forward and WP42 ordinaryEOR/loaded wrapper contract retain these limited effects; no new finding from a possible extra clause vector. ECB001 existing NO_REQUIRED scope preserved.'],
 ['All status transfer producers/dedicated callbacks outside adopted facts remain OPEN, not automatically approved.'])
record('RX-CORE-EOR',
 ['Master EOR597–780 captures speed order and sequentially dispatches stage consumers. Octolock calls central Def/SpDef decrease with nil source; current state is reread under its own gates.',
  'Explicit positive-result exits may skip tail; only reached current living actors get listed tail resets. No moldBreaker reset occurs in this complete master.'],
 ['Default ordinary master plus separately loaded clause wrapper, valid cached objects and exact local handler conditions; no intervening writer when deriving the already bounded ECB001 vector.'],
 ['E026 complete597–780 previously whole781 actually read and independently fresh full master in completed Q2 counter. StatStages full387, UseMove full762, clause wrapper full306 bound to exact ECB001 fact package.'],
 ['Whole WP42 was previously read; fresh§5 lines97–154 correctly specifies cached sequence/source-free central decreases/early exits/exhaustive bounded tail. Existing ECB001 independent NO_REQUIRED counter remains valid, with source trace accepted.'],
 ['All concrete stage handler families and whole callback totality remain independently OPEN.'])
record('RX-CORE-ATTACK',
 ['AttackPhase consumes choices in Call/switch/items/Mega/move stages; MoveNext/regular/Quash passes reselect only eligible live unmoved current move/Shift choices with positive-result checks.',
  'Ordinary ProcessTurn normal diagnostic return then Judge/optional priority update is separate from action lastMoveFailed and lastRoundMoved writes. Failures can bypass common tail; no generic finally or equal failure assignment.'],
 ['Exact current choices/effects/liveness, existing config, diagnostic completion and actual stamp positions; no scheduler progress guarantee for arbitrary mutations/errors.'],
 ['E018 own whole202; fresh complete attack176–201/move scheduling102–171; UseMove5–56 and full762 previously actual.'],
 ['WP40§5.2/§5.2.3 and WP42:39/41 preserve exact caller checkpoints and conditional reselection; no extra compulsory fixture is justified by the interface fact.'],
 ['All nested Instruct/Dancer/move-family outcomes outside named complete bindings retain independent scope.'])
record('RX-PEER',
 ['Constructor uses Peer.new, distinct from unused NullPeer methods. Normal Peer leave skips missing Pokemon, gets leaving-form result, applies truthy differing form, caps HP to totalhp, then invokes change hook.',
  'Peer itself does not universally unmega/unprimal. Caller Faint/capture/outer cleanup have separate explicit operations and different endBattle/used arguments. Ruby form0 truthiness is preserved.'],
 ['Current Pokemon/form setter and MultipleForms callback conditions; ordinary leaving versus faint/capture/end arguments kept distinct.'],
 ['E078 own whole77; fresh complete leave53–59. Constructor98–174, Faint64–99, normalEnd405–512, Catch271 own FULL, BURMY178–200 partial complete registration.'],
 ['WP41:109 keeps ordinary switch/Primal distinction; WP42 normal cleanup and WP39 outer cleanup are separate. Existing mandatory F054 animation-only and audio channel corrections remain authoritative.'],
 ['All other MultipleForms callbacks/native save reload remain OPEN outside selected CTF/CAA contributions.'])

verified=[]
for ident in selected['selected_complete_parent_identities']:
 raw_source=subprocess.check_output(['git','-C',ident['repo'],'show',ident['commit']+':'+ident['path']])
 assert len(raw_source)==ident['bytes'] and hashlib.sha256(raw_source).hexdigest()==ident['sha256']
 assert subprocess.check_output(['git','-C',ident['repo'],'rev-parse',ident['commit']+':'+ident['path']],text=True).strip()==ident['blob']
 prior=[x for x in ledger['entries']if x.get('path')==ident['path']and x.get('status')=='FULL_READ']
 assert prior
 verified.append({'identity':ident,'identity_match':True,'own_preexisting_actual_full_read_ledger_records':prior,'new_FULL_credit':0})
out=dict(schema='r8-core-external-battler-nine-finite-reception-v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),reader='/root/core_atomic_reception',source_original_reader=selected['envelope']['source_actual_reader'],parent=selected['parent'],selected_snapshot={'path':str(selected_path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'actual_read_scope':'All418lines/envelope/ninecompletefacts/eightcompleteidentities in two untruncated bounded captured views1–220/219–418'},records=records,exact_parent_verification=verified,actual_source_IO='P/io/read-*.json retains actual selected/necessary source and current formal outputs with realUTC/stdout/stderr/exit. Early whole-read timestamps stay NOT_CAPTURED as original ledger, never reconstructed. Mechanical identity verification is not semantic reading.',original_parent_claims_not_adopted='Other15 fact objects and whole810 external manual atoms/full1.79MB mapping are not adopted by this receipt. RX-HANDLER not in assigned nine: preserve root explicit empty-subclass qualification; no invented registry/string normalization.',whole_CORE='INCOMPLETE_NO_GLOBAL_PASS',all_callbacks=False,new_context=0,new_vote=0,new_required=0,new_optional=0,business_execution='NOT_EXECUTED',UPDATE_NOT_STARTED=True)
target=P/'battler-finite-reception.v1.json';encoded=(json.dumps(out,ensure_ascii=False,indent=2)+'\n').encode();target.write_bytes(encoded)
print(json.dumps(dict(path=str(target),bytes=len(encoded),sha256=hashlib.sha256(encoded).hexdigest(),facts=len(records),identities=len(verified),utc=out['utc'])))
