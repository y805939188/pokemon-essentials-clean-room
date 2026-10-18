import json,pathlib,subprocess,hashlib,datetime
V=pathlib.Path(__file__).resolve().parent;R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
F=json.loads((V/'forward-mapping.json').read_text());REV=json.loads((V/'reverse-mapping.json').read_text());assert len(F['atoms'])==1906
rows=[]
def a(unit,meaning,receiver,source='R20'):rows.append((source,unit,meaning,receiver))
for unit,meaning,receiver in [
 ('globals1–7','Loading this generator file replaces four speciesfact hashes and legalMoves with fresh hashes, legalMovesLevel0 and tmMovesnil; no percall reset of the four species caches.','F12§9.1L236–241:cache-initialization'),
 ('pbBaseStatTotal9–14','Direct BST helper resolves Species.get and sums every value in its base_stats hash; it doesnot selectively iterate the six mainstats here.','F12§5.2L78:raw-BST-source'),
 ('baseStatTotal16–19','BST memoization uses original caller key and recomputes only a false/nil stored value; zero is truthy and remains cached.','F12§9.1:BST-cache-key-and-truthiness'),
 ('babySpecies21–24','Baby species memoizes Species.get(species).get_baby_species under original input key, not the returned baby ID.','F12§9.1:baby-cache'),
 ('minimumLevel26–29','Minimum level memoizes Species.get(species).minimum_level under original input key.','F12§9.1:minimum-cache'),
 ('evolutions31–34','Evolution cache receives get_evolutions(true), including its exact producer semantics and returned array reference.','F12§9.1:evolutions-cache'),
 ('globals1–34','These caches do not automatically invalidate on species registry mutation or form-data recompilation; false/nil values retry while empty arrays remain cached.','F12§9.1/§10:cache-lifecycle-boundary'),
 ('RandomMove40–44','Sketch replacement snapshots Move.keys once per helper call and repeatedly samples a key then resolves Move.get.','F12§5.6L103:Sketch-global-key-sampling'),
 ('RandomMove45','Replacement rejects exactly function codes Struggle and ReplaceMoveWithTargetLastMoveUsed, without a species legal-move restriction.','F12§5.6L103:Sketch-exclusions'),
 ('RandomMove46–48','First accepted replacement returns canonical data.id; absent accepted candidates can loop without a retry cap, while registry lookup failures propagate.','F12§5.6L103/§10:Sketch-return-and-nontermination'),
 ('LegalMoves50–55','Legal-move building first performs Species.get, allocates moves[], then has a nil guard; strict get failures occur before that guard.','F12§5.5L96:lookup-before-nil-guard'),
 ('LegalMoves55','Level-up entries are processed in authored order and add with base2 only when learnlevel≤maxlevel.','F12§5.5L96:levelup-source-order'),
 ('LegalMoves56–59','First false/nil tmMoves initializes an empty global array before iterating every current Item record; every is_machine? item appends its move without dedup here.','F12§5.5L96/§9.1:machine-cache-build'),
 ('LegalMoves56–59','Failure during Item.each can leave the alreadytruthy partial tmMoves cache; no ensure clears it for a subsequent call.','F12§10:machine-cache-failure-prefix'),
 ('LegalMoves60','Tutor entries are processed after level-up and add with base0 only if the global machine-move array includes the move.','F12§5.5L96:tutor-machine-intersection'),
 ('LegalMoves61–62','Egg entries come from resolved babySpecies species record, in that record order, with base2; no level filter applies to egg entries.','F12§5.5L96:baby-egg-source'),
 ('LegalMoves63–66','Pruning comparison movedatas is a fresh array containing one [moveID,datareference] per pre-prune weighted occurrence.','F12§5.5L98:comparison-snapshot'),
 ('LegalMoves68–72','DeleteAll repeatedly uses Array.delete to remove every occurrence of the requested move ID from the live moves array.','F12§5.5L98:delete-all-copies'),
 ('LegalMoves73–75','Outer pruning iteration traverses the mutating live moves array; inner movedatas retains its initial entries, so deletions can shift later outer iteration and comparisons remain available after deletion.','F12§5.5L98:live-outer-snapshot-inner'),
 ('LegalMoves78–80','First pruning branch: actoraccuracy0 plus targetfunctionNone, sameType, actorpower≥targetpower removes all target copies.','F12§5.5L98:always-hit-prune'),
 ('LegalMoves78–80','Always-hit pruning has no identity exclusion: an accuracy0/None actor can delete all its own copies when its own snapshot pair is reached.','F12§5.5L98:self-deletion'),
 ('LegalMoves83–85','Only if earlier branch fails, equalfunction and bothpower0 with strictly greater actoraccuracy removes the target status move.','F12§5.5L98:status-accuracy-prune'),
 ('LegalMoves87–88','Next priority branch actorBadPoisonTarget removes targetPoisonTarget; the condition itself doesnot test type/power/accuracy.','F12§5.5L98:toxic-poison-prune'),
 ('LegalMoves93–98','Last pruning branch requires samefunction, nonzeroactorpower, sameType and an actorPP gate in addition to strength.','F12§5.5L98:damaging-prune-conjunction'),
 ('LegalMoves95','Actor PP gate is actorPP15 OR actorPP10 OR actorPP==targetPP; targetPP10/15 alone is insufficient.','F12§5.5L98:actor-PP-direction'),
 ('LegalMoves96–97','Strength gate is strictly greater actorpower OR equalpower with strictly greater actoraccuracy; meeting the PP gate alone doesnot delete.','F12§5.5L98:strength-gate'),
 ('LegalMoves78–99','The four branches are ordered if/elsif alternatives for each pair; no ideal unordered dominance-set calculation replaces their mutations.','F12§5.5L98:ordered-pruning-branches'),
 ('LegalMoves102','The live weighted remaining array is returned without a final dedup, sort, padding, or check for an empty result.','F12§5.5L98–99:weighted-pruning-return'),
 ('addMove105–107','A move is resolved first; if its canonical ID already occurs, this entire later add returns without adding further sourceweight.','F12§5.5L96:first-positive-source-wins'),
 ('addMove108','BUBBLE and BUBBLEBEAM return before any weight calculation or insertion, for every source.','F12§5.5L97:two-exclusions'),
 ('addMove109','Initial copy count is base+1.','F12§5.5L97:default-weight'),
 ('addMove110','None function with power≤40 replaces count with base.','F12§5.5L97:weak-None-weight'),
 ('addMove111–113','Power≤30 OR GROWL/TAILWHIP/LEER replaces count with base; this rule follows the prior assignment.','F12§5.5L97:weak-or-named-weight'),
 ('addMove114–117','Power≥60 OR REFLECT/LIGHTSCREEN/SAFEGUARD/SUBSTITUTE/FAKEOUT replaces count with base+2.','F12§5.5L97:strong-or-defense-weight'),
 ('addMove118','Power≥80 AND NORMAL type replaces count with base+3 after the base+2 rule.','F12§5.5L97:normal-strong-weight'),
 ('addMove119–122','PROTECT/DETECT/TOXIC/AERIALACE/WILLOWISP/SPORE/THUNDERWAVE/HYPNOSIS/CONFUSERAY/ENDURE/SWORDSDANCE finally replace count with base+3.','F12§5.5L97:high-value-final-weight'),
 ('addMove123','Insertion appends canonical data.id count times; zero-copy sources leave no membership, so a later source may still add that move.','F12§5.5L96–97:zero-copy-doesnot-lock-membership'),
 ('hasMorePowerful128–130','Candidate power0 immediately returnsfalse; it is not compared as a weaker attack.','F12§5.6L105:status-power-exemption'),
 ('hasMorePowerful131–138','For a nonzero-power candidate, any nonnil list member with sameType and strictly greater power returns true, irrespective of category/function/PP/accuracy.','F12§5.6L105:strict-same-type-power'),
 ('hasMorePowerful131–138','Nil list slots are skipped; no qualifying stronger move returnsfalse.','F12§5.6L105:nil-and-negative-case'),
 ('Candidate144–150','Candidate outeriteration starts−1 and increments at loopentry, so first outerattempt is even0; suggestedLevel is read again per outerattempt.','F12§5.1–5.2L69,73–75:first-parity-and-level'),
 ('Candidate151–156','Per outerattempt it snapshots all Species.keys and retries sampling until Species.get(key).form==0; there is no max retry count or prebuilt base-only array here.','F12§5.2L73:form-zero-only'),
 ('Candidate157–159','After a form0 candidate it draws rand20, reads memoizedBST, then rejects if level<minimumLevel; the RNG/BST effects precede that rejection.','F12§5.2L74–78:minimum-gate-prefix'),
 ('Candidate160–162','Even outerattempt rejects r<16&&BST<400 and then rejects r<13&&BST<500, using the same r.','F12§5.2L75:even-conjunctions'),
 ('Candidate163–165','Odd outerattempt rejects BST>400, then r<10&&babySpecies!=species.','F12§5.2L76:odd-conjunctions'),
 ('Candidate167','Both parities reject r<10&&babySpecies==species after parity-specific gates.','F12§5.2L77:common-baby-gate'),
 ('Candidate168','Both parities then reject r<7&&evolutions(species).length>0.','F12§5.2L77:common-evolvable-gate'),
 ('Candidate152–170','Rejected species restart the inner species selection without incrementing outeriteration; final legality/empty-move rejection later starts a new outerattempt and changes parity.','F12§5.1–5.2:retry-level-distinction'),
 ('Candidate171–172','Initial EV list visits each mainstat once and appends its ID when rand100<50; there are six draws and no duplicates at this initial stage.','F12§5.3L82:initial-six-independent-draws'),
 ('Candidate174–177','Nature keys snapshot once per outerattempt; each nature retry samples and resolves a current Nature record.','F12§5.3L83:nature-registry-draw'),
 ('Candidate178–179','LAX, GENTLE, or empty stat_changes use only the rand20<19 rejection branch, bypassing the raised/lowered-emphasis checks.','F12§5.3L83:neutral-and-two-named-branch'),
 ('Candidate181–187','For other natures, raised/lowered flags are determined only by changes whose stat appears in the current initial EV list and by the signs of their changes.','F12§5.3L83:emphasis-flags'),
 ('Candidate188','The modified-nature branch draws rand10 before testing !raised_emphasis and rejects only when draw<6 AND no raised emphasis; it consumes this draw even if raised_emphasis istrue.','F12§5.3L83:nature-raised-draw-order'),
 ('Candidate189','Only if the prior gate didnot continue, it draws another rand10 before testing lowered_emphasis and rejects when draw<9 AND lowered emphasis.','F12§5.3L83:nature-lowered-draw-order'),
 ('Candidate175–192','Nature retry has no cap and doesnot resample species or the EV list; emphasis consistency is probabilistic, not a hard equality requirement.','F12§5.3L83:nature-retry-scope'),
 ('Candidate193–195','A changed level replaces the entire global legalMoves hash before assigning legalMovesLevel; an unchanged level retains all per-species arrays.','F12§5.5L99/§9.1:level-wide-cache-invalidation'),
 ('Candidate195','Only a false/nil species entry rebuilds via pbGetLegalMoves2; a cached empty array is truthy and remains cached.','F12§5.5L99:empty-list-cache-hit'),
 ('Candidate193–195','A builder failure after legalMovesLevel assignment leaves the newlevel/globalhash prefix; no transactional restoration of the previouslevel cache.','F12§10:legal-cache-failure-prefix'),
 ('Candidate196–206','The candidate item array preserves the exact41 literal entries and order shown in WP76§5.4; LEFTOVERS is also one of these entries.','F12§5.4L88:literal41-item-input'),
 ('Candidate210–213','Each item retry first draws rand40; zero chooses LEFTOVERS and breaks the item loop without the case gates.','F12§5.4L88:early-leftovers-gate'),
 ('Candidate214–215','Otherwise it draws an index into the full41-entry array; a nil sampled entry would retry. No global Item.exists? filtering occurs here.','F12§5.4L88,92:item-table-and-no-prefilter'),
 ('Candidate217–218','LIGHTBALL retries unless species==PIKACHU.','F12§5.4L89:LIGHTBALL-gate'),
 ('Candidate219–220','SHEDSHELL retries unless species is FORRETRESS or SKARMORY.','F12§5.4L89:SHEDSHELL-gate'),
 ('Candidate221–222','SOULDEW retries unless species is LATIOS or LATIAS.','F12§5.4L89:SOULDEW-gate'),
 ('Candidate223–224','FOCUSSASH retries only when BST>450 AND rand10<8; the random draw is skipped if BST≤450. This is the separate non-species gate.','F12§5.4L89:FOCUSSASH-numeric-gate'),
 ('Candidate225–226','ADAMANTORB retries unless species==DIALGA.','F12§5.4L89:ADAMANTORB-gate'),
 ('Candidate227–228','PASSHOBERRY retries unless species==STEELIX.','F12§5.4L89:PASSHOBERRY-gate'),
 ('Candidate229–230','BABIRIBERRY retries unless species==TYRANITAR.','F12§5.4L89:BABIRIBERRY-gate'),
 ('Candidate231–232','HABANBERRY retries unless species==GARCHOMP.','F12§5.4L89:HABANBERRY-gate'),
 ('Candidate233–234','OCCABERRY retries unless species==METAGROSS.','F12§5.4L89:OCCABERRY-gate'),
 ('Candidate235–236','CHOPLEBERRY retries unless species==UMBREON.','F12§5.4L89:CHOPLEBERRY-gate'),
 ('Candidate237–238','YACHEBERRY retries unless species is TORTERRA, GLISCOR, or DRAGONAIR.','F12§5.4L89:YACHEBERRY-gate'),
 ('Candidate239–240','SHUCABERRY retries unless species==HEATRAN.','F12§5.4L89:SHUCABERRY-gate'),
 ('Candidate241–242','DEEPSEATOOTH retries unless species==CLAMPERL.','F12§5.4L89:DEEPSEATOOTH-gate'),
 ('Candidate243–244','THICKCLUB retries unless species is CUBONE or MAROWAK.','F12§5.4L89:THICKCLUB-gate'),
 ('Candidate245–246','LIECHIBERRY only when ATTACK is absent draws rand100 and appends ATTACK on<50; an existing ATTACK entry causes neither append nor this draw.','F12§5.4L90:Liechi-nonduplicate-shortcircuit'),
 ('Candidate247–248','SALACBERRY uses the corresponding absentSPEED/<50 append and skips draw when already present.','F12§5.4L90:Salac-nonduplicate-shortcircuit'),
 ('Candidate249–250','PETAYABERRY uses absentSPECIAL_ATTACK/<50 append and skips draw when already present.','F12§5.4L90:Petaya-nonduplicate-shortcircuit'),
 ('Candidate252–253','Any accepted item case exits the inner item loop without resampling nature/species; item-loop rejection itself has no retry cap.','F12§5.4L88–90:item-retry-scope'),
 ('Candidate254–255','If level<10 and ORANBERRY is registered, a new rand40 draw of0 OR currentSITRUSBERRY replaces item with ORANBERRY; the draw is evaluated first even for currentSITRUSBERRY.','F12§5.4L91:low-level-berry-replacement'),
 ('Candidate256–257','Else if level>20 and SITRUSBERRY is registered, symmetric rand40==0 OR currentORANBERRY replaces with SITRUSBERRY; no such replacement at levels10..20.','F12§5.4L91:high-level-berry-replacement'),
 ('Candidate259–263','Local moves aliases the cached array. If its firstentry isSKETCH, local sketchtrue and four calls replace cache positions0..3 in order.','F12§5.6L103:shared-Sketch-write'),
 ('Candidate261–264','Four Sketch writes extend an array shorterthan4 and preserve any tail beyondindex3; replacements may duplicate eachother and are not deduplicated at assignment time.','F12§5.6L103:Sketch-extension-tail-and-duplicates'),
 ('Candidate261–264','An exception in a later Sketch replacement preserves earlier cache writes; no array clone/rollback protects the shared cache.','F12§10:Sketch-failure-prefix'),
 ('Candidate260–265','Subsequent samelevel/samespecies sampling sees the mutated cache, usually with noSKETCH atindex0; sketchflag startsfalse each attempt. A levelchange independently clears this cache.','F12§5.6L103:Sketch-persistence'),
 ('Candidate265','Empty legalMoves immediately continues outergeneration after nature/item work; no TACKLE rescue is reached through this empty-array branch.','F12§5.6L104:empty-outer-retry'),
 ('Candidate266–268','Fewerthan4unique IDs adopts a new union-deduplicated array in originalfirst-occurrenceorder, with no padding; source inner empty→TACKLE line is guarded by the earlieremptycontinue.','F12§5.6L104:small-unique-list'),
 ('Candidate266–338','The fewerthan4unique path skips combination/stat-emphasis/totalpower/acceptedEV/SILKSCARF gates inside the else block, but still reaches final item-move checks.','F12§5.6L104:small-list-gate-scope'),
 ('Candidate271–276','The ≥4unique path resolves each of REST/SPITUP/SWALLOW/STOCKPILE/SNORE/SLEEPTALK to its ID ifregistered, else nil before combo retries.','F12§5.6L106:optional-combination-ID-resolution'),
 ('Candidate277–283','Each combination retry clears newmoves, then repeatedly draws weighted listindices until four distinct nonnil entries; no retry cap.','F12§5.6L105:weighted-distinct-four'),
 ('Candidate280–282','Each candidate draw then always draws rand100 first; only<50 AND hasMorePowerfulMove skips it. Nil is excluded and duplicate IDs are not appended.','F12§5.6L105:stronger-skip-draw-prefix'),
 ('Candidate284–287','SPITUP orSWALLOW withoutSTOCKPILE rejects unless local sketchflag.','F12§5.6L106:stockpile-forward-pair'),
 ('Candidate288–291','STOCKPILE without bothSPITUPandSWALLOW rejects unless local sketchflag.','F12§5.6L106:stockpile-reverse-pair'),
 ('Candidate292–295','SLEEPTALK withoutREST rejects unless (sketch OR availablelist lacksREST) AND its own rand100<20; noexception draw if that prerequisitefails.','F12§5.6L106:sleeptalk-independent-gate'),
 ('Candidate296–299','SNORE withoutREST has a separate identical exceptiondraw/gate, evaluated only if earlierSLEEPTALK gate allowed continuation. Both canrequiretwo draws.','F12§5.6L106:snore-independent-gate'),
 ('Candidate300–310','Power sum and physical/special/Normal flags ignore everypower0 move. Damaging entries contribute rawpower and category0/1 flags, with Normal determined by rawdata.type.','F12§5.6L107–109:raw-power-and-category-flags'),
 ('Candidate312–315','No physical flag plusATTACK inEV causes rand100<80 combinationretry; thedraw is skipped if either antecedentfails.','F12§5.6L107:attack-emphasis-retry'),
 ('Candidate316–319','Only after that gate, no specialflag plusSPECIAL_ATTACK inEV has its own rand100<80 retry.','F12§5.6L107:special-emphasis-retry'),
 ('Candidate320–322','One new rand10 value is reused for both power gates: r>6&&totalpower>180, then r>8&&totalpower>140; they are not independent draws.','F12§5.6L108:shared-power-draw'),
 ('Candidate323','Only totalpower0 draws rand100 and retries on<95 after earlier gates.','F12§5.6L108:zero-power-retry'),
 ('Candidate326–328','Accepted physical-only combination independently appends ATTACK onrand100<80, then deletes everySPECIAL_ATTACK entry on a separate<80draw. Append doesnot dedup.','F12§5.6L109:physical-EV-append-and-delete'),
 ('Candidate330–332','Accepted special-only combination independently deletes allATTACK on<80, then appendsSPECIAL_ATTACK on a separate<80draw, allowing duplicates.','F12§5.6L109:special-EV-delete-and-append'),
 ('Candidate334','In this ≥4unique accepted path, SILKSCARF becomesLEFTOVERS if no damagingNormal move; a Normal status move doesnot set hasNormal.','F12§5.6L109:SilkScarf-damaging-Normal-gate'),
 ('Candidate335–337','After accepted adjustments local moves becomes newmoves and the combination loop breaks; repeated combination failures do not roll back earlier species/nature/item selection.','F12§5.6L104–109:combination-loop-boundary'),
 ('Candidate339–341','Final LIGHTCLAY becomesLEFTOVERS if moves contain neitherLIGHTSCREENnorREFLECT.','F12§5.6L110:LightClay-final-check'),
 ('Candidate342–345','Final BLACKSLUDGE resolves base speciesrecord.types and becomesLEFTOVERS ifPOISON absent; it doesnot invoke activeBattler orPokemon form/type modifiers here.','F12§5.6L110:BlackSludge-base-data-check'),
 ('Candidate346','Final HEATROCK becomesLEFTOVERS ifSUNNYDAY absent.','F12§5.6L110:HeatRock-final-check'),
 ('Candidate347–349','Final DAMPROCK becomesLEFTOVERS ifRAINDANCE absent.','F12§5.6L110:DampRock-final-check'),
 ('Candidate350–352','IfREST present, a rand100<33 replaces anycurrentitem withLUMBERRY, then a separate rand100<25 replaces anyresult withCHESTOBERRY. Both draws occur in that order.','F12§5.6L110:REST-two-overwriting-draws'),
 ('Candidate354','PBPokemon intermediate receives species,item,nature,thefirstfour move slots and the entire current EV list including repeats.','F12§5.7L114:intermediate-record-inputs'),
 ('Candidate355','Intermediate creates at suggestedlevel with IV31 and suppliedtrainer; its exact creator normalization/ownership/EV behavior is separately received, not reimplemented here.','F12§5.7L114:individual-producer-handoff'),
 ('Candidate356–359','Only rules.ruleset.isPokemonValid?(pkmn) true exits the outerloop and returns thisPokemon; failure restarts outergeneration with updatedparity and retainedglobalcaches.','F12§5.1L69/§5.7:single-member-final-exit'),
 ('Candidate144–359','There is no rescue, retrybudget, UIcancel check or progresscallback in this entire candidatebuilder; thrown failures propagate with cacheprefixes while unsatisfiable rejection paths may run indefinitely.','F12§5.1L69/§10L256–257:candidate-progress-and-failure-boundary'),
]:a(unit,meaning,receiver)
for unit,meaning,receiver,source in [
 ('Natureconstructor15–19','Nature constructor storesid/rawname/stat_changes with Unnamed/[]fallback; stat_changes array is returned directly byattr_reader.','F12§5.3L83:nature-record-contract','GEN-NATURE'),
 ('Nature25registrations29–176','Default25 registrations are ordered and have five emptychange neutralnatures HARDY/DOCILE/SERIOUS/BASHFUL/QUIRKY; LAX/GENTLE instead have realopposing±10changes but are separatelynamed bygenerator.','F12§5.3L83:default-nature-inputs','GEN-NATURE'),
 ('Speciesreaders3–42/schema52–111/initialize175–221','Species moves/tutor_moves/egg_moves are direct arrays defaulting[]; types defaultsNORMAL; form defaults0; schema uses level+Move pairs forMoves andMove enums forTutor/Egg. ActualPBS value/compile qualification remains separate.','F12§5.2/§5.5:species-field-producer','GEN-SPECIES-FIELDS'),
 ('Moveconstructor41–57','Move raw fields defaultcategory2/power0/accuracy100/PP5/typeNONE/functionNone; generator directlyreads these raw fields. Zero numeric values aretruthy.','F12§5.5–5.6:raw-move-fields','GEN-MOVEDATA'),
 ('Movephysical80–90','Generator category0/1 tests do not call Move.physical?/special? and therefore do not apply their Settings.MOVE_CATEGORY_PER_MOVE/type-category branch.','F12§5.6L107:raw-category-vs-dynamic-consumer','GEN-MOVEDATA'),
]:a(unit,meaning,receiver,source)
# Explicit manual assertions above. The following performs identity/serialization/membership bookkeeping only.
def blob(path):return subprocess.check_output(['git','show',R+':'+path],cwd='/workspace/pokemon-essentials')
def sid(path):
 b=blob(path);return {'repo':'/workspace/pokemon-essentials','commit':R,'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':subprocess.check_output(['git','rev-parse',R+':'+path],cwd='/workspace/pokemon-essentials',text=True).strip()}
ns='Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb';ss='Data/Scripts/010_Data/002_PBS data/008_Species.rb';ms='Data/Scripts/010_Data/002_PBS data/005_Move.rb'
F['source_identities']['GEN-NATURE']=sid(ns);F['source_identities']['GEN-SPECIES-FIELDS']=sid(ss)
assert F['source_identities']['GEN-MOVEDATA']['sha256']==sid(ms)['sha256']
units=[]
for key,path,ranges,receipt in [('GEN-NATURE',ns,[(1,len(blob(ns).splitlines()))],'67aa6d'),('GEN-SPECIES-FIELDS',ss,[(3,50),(52,111),(175,221)],'255fe4/c6b2b2/d2ce8c'),('GEN-MOVEDATA',ms,[(1,len(blob(ms).splitlines()))],'c45b39')]:
 for lo,hi in ranges:units.append({'identity':F['source_identities'][key],'range':[lo,hi],'content':''.join(blob(path).decode().splitlines(keepends=True)[lo-1:hi]),'actual_full_unit_read':receipt,'qualification':'Complete named sourceunit actuallyread; whole sourcefileFULL onlyNature/Move text, finiteSpeciesunits only. No completePBS registry value/compile/runtime transfer.'})
premise=('FixeddefaultR/B8 withoutlater overrides; normal registeredvalid species/move/item/nature objects andnumeric arrays; calledregistry/individual/rules/IO primitives return normally to eachobservation unless a failureprefixexplicit. '
 'Uniformprobability labels are conditional on ordinarylegaluniformunderlyingoffsets, not measured native distributions. rand/Array.sample implementation is not executed; source callorder is stated. '
 'CRE-A7facts54units/full72TrainerType and all1600/1888literalreceptions retain ownboundedpremises, do not supply453species649classes2732provenance/proofqualification. '
 'Helpers audited independentofordinarycallers; noautomaticfuturepublicAPI/tests/compatibilitymandate.')
new=[]
for num,(source,unit,meaning,receiver) in enumerate(rows,1907):
 atom={'id':f'FAC-A{num:04}','source':source,'unit_locator':unit,'assertion':meaning,'formal_receivers':[receiver],'premise':premise,'pending_dependencies':[],'status':'BOUNDED_SOURCE_FACT_AND_EXPLICIT_FORMAL_CHILD_OR_AUDIT_SCOPE_ROUTING','evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED','reader':'/root/facility_atomic_completion_cloud'};new.append(atom);REV['mappings'].append({'formal_clause':receiver,'atomic_assertion':atom['id'],'meaning':meaning,'source':source,'source_unit':unit,'premise':premise,'status':atom['status'],'pending_dependencies':[],'relation':'EXPLICIT_NAMED_CANDIDATE_BUILDER_CHILD_OR_AUDIT_SCOPE'})
F['atoms'].extend(new);F['bounded_denominator']=len(F['atoms']);F.setdefault('v2_increments',[]).append({'path':'generator-candidate-legalmove-atomic-increment.v2.json','count':len(new),'ids':[new[0]['id'],new[-1]['id']],'utc':NOW});REV['true_bounded_assertions']=len(F['atoms']);REV['v2_new_exact_child_bindings']=len(REV['mappings'])-992
packet={'schema':'facility-generator-candidate-legalmove-manual-meaning-increment/v2','utc':NOW,'reader':'/root/facility_atomic_completion_cloud','explicit_source_assertions':new,'source_identities':{k:F['source_identities'][k] for k in ['R20','R19','GEN-NATURE','GEN-SPECIES-FIELDS','GEN-MOVEDATA','F12']},'complete_supplemental_units':units,'actual_source_reads':['eddebb R20L1–180 fullyvisiblebeforelatermissingF13KeyError; noR20truncation','a7db80 R20L181–359','67aa6d wholeNature25registrationfile','255fe4/c6b2b2/d2ce8c Speciesneededcompleteunits','c45b39 wholeMove source includingdormantcommentbodies'],'actual_formal_reads':['eddebb WP76L63–113','a7db80 WP76L112–124','priorwholeWP76all279'],'qualification':'Manuallyauthoredfinite facts, some mechanical antecedents aggregated; notfullnormalized originaldenominator. CurrentWP76 alreadycorrectlyretains sourcecache/pruning/selfdeletion/shortlist/duplicateEV branches. Native randomness, eventualtermination/quality/fullcompile/defaultprimaryinputproof notexecuted or asserted.','OPEN':['Complete453species649classes2732provenance/normalization andfiniteeligibilityproofinput premises','41candidateItemrecords/allmachineItementries andallMoveprimaryfacts beyondalreadyactualreceivedneededunits; noeffectscontractinferred fromlabels','R21allocation/currentCompilerwriter/parser/datalist normalization andallGN/B17/formalchildreception','964remaining formal seedstructures/202external joins; no fullSF/RC/PA/QC/WSclosure'],'new_required':0,'new_optional':0,'new_contexts':0,'new_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
def dump(n,d):(V/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
dump('generator-candidate-legalmove-atomic-increment.v2.json',packet);dump('forward-mapping.json',F);dump('reverse-mapping.json',REV)
p=json.loads((V/'progress.json').read_text());p.update(updated_utc=NOW,manually_authored_finite_source_assertions=len(F['atoms']),source_to_formal_bindings=len(REV['mappings']),finite_new_child_bindings=len(REV['mappings'])-992,state='RUNNING_R21_WRITER_PRIMARY_TRAIT_AND_CATALOG_TAILS');dump('progress.json',p)
d=json.loads((V/'atomic-denominator.json').read_text());d['updated_utc']=NOW;d['manual_bounded_source_assertions'].update(count=len(F['atoms']),id_end=new[-1]['id']);d['finite_reverse_bindings'].update(count=len(REV['mappings']),qualification=f"992historicalregionbindings+{len(REV['mappings'])-992}explicit source/audit/casechildroutes, notfullformaldenominator.");d['finite_generator_candidate_legalmoves']={'source_assertions':len(new),'membership':'generator-candidate-legalmove-atomic-increment.v2.json','qualification':packet['qualification']};dump('atomic-denominator.json',d)
l=json.loads((V/'reading-ledger.json').read_text());l['updated_utc']=NOW;l['v2_additional_source_reads'].append({'utc':NOW,'packet':'generator-candidate-legalmove-atomic-increment.v2.json','actual_reads':packet['actual_source_reads'],'qualification':'WholeNature/Move source text ownactualread; onlySpeciescompletefiniteunits. NoPBSvalueproof/fullproducerdomain transfer.'});dump('reading-ledger.json',l)
b=(V/'generator-candidate-legalmove-atomic-increment.v2.json').read_bytes();print('new',len(new),'range',new[0]['id'],new[-1]['id'],'total',len(F['atoms']),'routes',len(REV['mappings']),'bytes',len(b),'sha',hashlib.sha256(b).hexdigest());print('naturelines',len(blob(ns).splitlines()),'movelines',len(blob(ms).splitlines()))
