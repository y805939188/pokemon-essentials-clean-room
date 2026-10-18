import pathlib,json,datetime,hashlib,subprocess
V=pathlib.Path(__file__).parent;NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
F=json.loads((V/'forward-mapping.json').read_text());REV=json.loads((V/'reverse-mapping.json').read_text())
assert len(F['atoms'])==1683
byid={x['id']:x for x in F['atoms']}
cases=[]
premise=('SOURCE_STATIC / DERIVED_VECTOR / NOT_EXECUTED. Fixed defaultR/B8, reached Safari action with valid globalPlayer/Storage/registry/onePokemon/positive totalHP and correctly typed integer factors, scene/messages/animations normally returning to each observation. '
         'RNG values are symbolic branch inputs, not sampled or simulated. Underlying positive-integer oldRand is assumed to return a legal0..upper−1 offset; percentage wording is conditional on ordinary integer uniformity, with no actual distribution/sequence guarantee. CurrentWP06§5.1.1 conditional native boundary retained. No unrelated callback changes fields. Rate-only cases stop before unrelated capture outcome math. '
         'Mode ball id is the complete SAFARIBALL record; ordinary/Ultra flag states are explicit supplied case premises, not proof that a particular default encounter contains an Ultra Beast. '
         'Rendering/native/frame/random distribution output and real battle execution remain unknown separately.')
def case(cid,line):
    z={'case':cid,'old_locator_id':f'F08-L{line:04}','line':line,'premise':premise,'children':[],'status':'FINITE_COMPLETE_STATIC_CASE_MEANINGS_RECONCILED','business':'NOT_EXECUTED'};cases.append(z);return z
def child(z,name,meaning,ids,proof):
    cid='FAC-SF-'+z['case']+'-'+name
    z['children'].append({'id':cid,'meaning':meaning,'source_assertion_ids':ids,'manual_static_justification':proof,'status':'FINITE_STATIC_CHILD_RECONCILED'})
    for aid in ids:
        assert aid in byid
        byid[aid].setdefault('formal_case_receivers',[]).append(cid)
    primary=ids[0];atom=byid[primary]
    REV['mappings'].append({'formal_clause':f"F08{z['case']}L{z['line']}:{name}",'formal_child_id':cid,'atomic_assertion':primary,'support_assertion_ids':ids,'meaning':meaning,'source':atom['source'],'source_unit':atom['unit_locator'],'premise':premise,'status':'FINITE_STATIC_CASE_CHILD_RECONCILED','pending_dependencies':[],'relation':'EXPLICIT_CASE_CHILD_WITH_ALL_NAMED_SUPPORT; source IDs reused, not newunique sourceassertions'})

z=case('SF07',17)
child(z,'joint-full','Party-full AND Storage-full makes the prethrow capacity gate true.',['FAC-A1654'],'Global helper uses logical AND; other capacities are not substituted.')
child(z,'message','True capacity gate requests the boxes-full rejection message.',['FAC-A1621'],'Message occurs in the full branch before next.')
child(z,'budget','Rejected Ball leaves its battle ballCount unchanged.',['FAC-A1621','FAC-A1622'],'next precedes decrement443.')
child(z,'no-round','Rejected Ball doesnot reach post-action factor clamp or round-end processing.',['FAC-A1621','FAC-A1630'],'next jumps to command selection436 before470.')
child(z,'no-random','Rejected Ball performs no capture or round-end random draw.',['FAC-A1621','FAC-A1624','FAC-A1632'],'No throwing call or escape branch is entered before next.')
child(z,'space','Once the joint-full predicate is false and Ball is chosen again, normal dependencies permit decrement, refresh and throw in that order.',['FAC-A1654','FAC-A1622','FAC-A1624'],'The conditional full branch is skipped; valid resolved SAFARIBALL id is truthy.')

z=case('SF09',19)
child(z,'bait-pass-catch','Initial Fc10,Fe10 with Bait r<90 yields Fc5.',['FAC-A1626'],'10 integer-divided by2 is5.')
child(z,'bait-pass-escape','The same successful Bait gate yields Fe5.',['FAC-A1626'],'Escape halves regardless of random result.')
child(z,'bait-fail-catch','Bait r≥90 preserves Fc10.',['FAC-A1626'],'Catch assignment condition fails.')
child(z,'bait-fail-escape','Bait r≥90 still yields Fe5.',['FAC-A1626'],'Unconditional escape-factor division remains.')
child(z,'rock-pass-catch','Rock r<90 yields Fc20.',['FAC-A1627'],'Catch factor always10×2=20.')
child(z,'rock-pass-escape','Rock r<90 yields Fe20.',['FAC-A1627'],'Conditional escape factor10×2=20.')
child(z,'rock-fail-catch','Rock r≥90 still yields Fc20.',['FAC-A1627'],'Catch doubling precedes conditional escape doubling.')
child(z,'rock-fail-escape','Rock r≥90 preserves Fe10.',['FAC-A1627'],'Conditional escape assignment fails.')
child(z,'catch-clamp','After each of these four branches Fc is clamped3..20.',['FAC-A1630'],'Each recognized action reaches470;5,10,20 all remain within interval.')
child(z,'escape-clamp','After each branch Fe is clamped2..20.',['FAC-A1630'],'5,10,20 are within escape interval; no clamp reverses those results.')

z=case('SF11',21)
child(z,'rate45','cr45 uses E125 and Fe9.',['FAC-A1612','FAC-A1620'],'1275×9=11475≤12500<12750=1275×10;9 passes2..20 clamp.')
child(z,'rate60','cr60 uses E100 and Fe7.',['FAC-A1613','FAC-A1620'],'1275×7=8925≤10000<10200=1275×8;7 passes clamp.')
child(z,'rate120','cr120 uses E75 and Fe5.',['FAC-A1614','FAC-A1620'],'1275×5=6375≤7500<7650=1275×6;5 passes clamp.')
child(z,'rate250','cr250 uses E50 and Fe3.',['FAC-A1615','FAC-A1620'],'1275×3=3825≤5000<5100=1275×4;3 passes clamp.')
child(z,'rate255','cr255 uses E25, integer quotient1, then Fe2.',['FAC-A1616','FAC-A1620'],'1275≤2500<2550; lower bound raises1 to2.')
child(z,'catch255','cr255 produces Fc20.',['FAC-A1619'],'255×100=25500=1275×20, exactly the upper factor bound.')
child(z,'catch25','cr25 has quotient1, then Fc3.',['FAC-A1619'],'1275≤2500<2550, lower bound raises1 to3.')
child(z,'partition45','Equality45 belongs to first interval≤45.',['FAC-A1612'],'First return uses≤45.')
child(z,'partition60','Equality60 belongs to second interval.',['FAC-A1613'],'Earlier≤45 already failed;≤60 succeeds.')
child(z,'partition120','Equality120 belongs to third interval.',['FAC-A1614'],'Earlier≤60 failed;≤120 succeeds.')
child(z,'partition250','Equality250 belongs to fourth interval.',['FAC-A1615'],'Earlier≤120 failed;≤250 succeeds.')
child(z,'partition-over250','Values above250 use the final E25 branch.',['FAC-A1616'],'All four early returns fail.')

z=case('SF12',22)
child(z,'factor3','Fc3 gives reconstructed rate38.',['FAC-A1623'],'3×1275=3825;3800≤3825<3900, integer÷100 is38.')
child(z,'factor20','Fc20 gives reconstructed rate255.',['FAC-A1623'],'20×1275=25500, integer÷100 is255.')
child(z,'random-bound','Bait and Rock each request random100 for their90 gate.',['FAC-A1626','FAC-A1627'],'Source request is100; symbolic domain is0..99 under the stated ordinaryrand integer contract, not an actual draw.')
child(z,'r89','Gate value89 satisfies the90 threshold.',['FAC-A1626','FAC-A1627'],'89<90.')
child(z,'r90','Gate value90 doesnot satisfy it.',['FAC-A1626','FAC-A1627'],'90<90 isfalse; no≤ comparison.')
child(z,'escape2','Fe2 uses escape threshold10.',['FAC-A1632'],'5×2=10.')
child(z,'escape-below','At Fe2, r9 escapes in the reached unresolved positive-ball round.',['FAC-A1632'],'9<10; its caller budget/decision gates retained in common premise.')
child(z,'escape-equal','At Fe2, r10 doesnot escape.',['FAC-A1632'],'10<10 isfalse; equals doesnot pass.')
child(z,'actual-safari','Both ordinary and Ultra variant cases actually throw the fixed Safari Ball.',['FAC-A1624'],'R01 resolves SAFARIBALL and supplies it as the thrown-ball argument; complete mode Item record received separately.')
child(z,'ordinary','For a target whose effective species lacks UltraBeast flag, the rate dispatcher reaches Safari1.5 modifier.',['FAC-A1660','FAC-A1655','FAC-A1656'],'NonUltra condition permits handler; actualballSAFARIBALL selects its complete1.5 callback.')
child(z,'bag-beast','Owning Beast Ball in Bag doesnot select its modifier for this throw.',['FAC-A1660','FAC-A1624'],'Capture gate checks thrown ball argument, not Bag ownership; the latter still matters separately for critical charm only.')
child(z,'ultra','For the explicitly configured Ultra target, fixed Safari Ball triggers pre-handler rate÷10.',['FAC-A1660'],'Ultra flag true and actual thrown ball!=BEASTBALL; integer input rate keeps integer division at this stage.')
child(z,'skip15','That Ultra variant skips Safari1.5 callback.',['FAC-A1660','FAC-A1656'],'Mutually exclusive if/else chooses division rather than rate dispatcher.')
child(z,'beast-reference','Beast Ball own Ultra5×/nonUltra÷10 behavior is forwarded to complete WP38 and its independently read handler; it is not applied to either fixed Safari throw.',['FAC-A1660'],'Complete handler180–187 read8004a6; wholecurrentWP38read a64a8e+c65c18. This is a reference disposition, not a new mode-ball behavior.')

R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';units=[]
for p,lo,hi,name in [
 ('Data/Scripts/001_Technical/002_RubyUtilities.rb',366,388,'Complete globalrand forwarding and Kernel author-parameter wrapper'),
 ('Data/Scripts/011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb',180,187,'Complete Beast Ball rate callback for forwarded reference'),
 ('Data/Scripts/010_Data/002_PBS data/008_Species.rb',263,265,'Complete Species flag predicate'),
 ('Data/Scripts/011_Battle/001_Battle/001_Battle.rb',658,675,'Complete ordinary seen/caught registrations'),
 ('Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',147,169,'Complete owned/set_shadow/owned-query methods'),
 ('Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',195,219,'Complete seen/form registration'),
 ('Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',222,228,'Complete last-seen registration'),
 ('Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',260,265,'Complete per-species caught counter'),
 ('Data/Scripts/015_Trainers and player/001_Trainer.rb',81,83,'Complete party-full predicate'),
 ('Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',20,32,'Complete box length/count/full predicates'),
 ('Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',132,146,'Complete storage box-count/capacity/full predicates'),
]:
    b=subprocess.check_output(['git','-C','/workspace/pokemon-essentials','show',R+':'+p]);identity={'repo':'/workspace/pokemon-essentials','commit':R,'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':subprocess.check_output(['git','-C','/workspace/pokemon-essentials','rev-parse',R+':'+p]).decode().strip()}
    units.append({'identity':identity,'range':[lo,hi],'name':name,'content':'\n'.join(b.decode().splitlines()[lo-1:hi]),'actual_reader':'/root/facility_atomic_completion_cloud','qualification':'Complete named units only; storage/Species/Dex wholeparent/sourceFULL not received.'})

formalpath='deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md';B='fd1df570cad987dc3852a3b958f03916e317f7fe';fb=subprocess.check_output(['git','-C','/workspace/pokemon-essentials-clean-room','show',B+':'+formalpath]);fid={'repo':'/workspace/pokemon-essentials-clean-room','commit':B,'path':formalpath,'bytes':len(fb),'sha256':hashlib.sha256(fb).hexdigest(),'blob':subprocess.check_output(['git','-C','/workspace/pokemon-essentials-clean-room','rev-parse',B+':'+formalpath]).decode().strip()};F['source_identities']['F15']=fid
packet={'schema':'facility-four-SF-catalog-rows-full-child-reception/v2','utc':NOW,'reader':'/root/facility_atomic_completion_cloud','cases':cases,'child_count':sum(len(z['children']) for z in cases),'complete_supplemental_units':units,'source_units_actual_reads':['92828d capacity+ordinaryDex methods','22a819 finiteDex methods','f073cd Speciesflag','8004a6 fullBeastcallback','acf3fd completeglobalrandwrapper366–388','earlier ownfullR01/02/Catch/Peer and151increment'],'formal_full_row_read':'2274b9 SF07/09/11/12 complete exact rows; WP53 all288 currentread; currentWP38 all146read','finite_Kernel_formal':{'identity':fid,'read_ranges':[[13,21],[109,133],[147,151],[189,194]],'actual_read':'d35a92','complete_random_author_dispatch_section':'\n'.join(fb.decode().splitlines()[120:133]),'qualification':'Complete necessary definition/author-dispatch/recording/scope paragraphs only, not wholeWP06. Given native legaloffset premise and no statistical/runtime proof.'},'complete_dependency_packet':'two-mode-item-records-consumers.v2.json complete2records/Itemderiveddefaultfacts; finite balls/source consumers in safari-contest-battle-atomic-increment.v2.json','qualification':'All four named row meanings and explicit branch/numeric/reference children reconciled within stated static premises. No gameplay/model/RNG execution. Every otherSFrow and all969baseline seed membership remain independently tracked; four closures do not imply wholeSafari/Dex/Storage/PBS acceptance. Native outputs remain separate unknown. Extra Dex units are finite newread for next natural SF21 unit, not closure by availability.','new_required':0,'new_optional':0,'new_contexts':0,'new_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
def dump(name,obj):(V/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
dump('sf07-09-11-12-full-child-reception.v2.json',packet);dump('forward-mapping.json',F)
REV['v2_new_exact_child_bindings']=len(REV['mappings'])-992;dump('reverse-mapping.json',REV)
N=json.loads((V/'next-dispatch.json').read_text());closing={z['old_locator_id'] for z in cases};before=len(N['unmet_formal_seed_structures']);N['unmet_formal_seed_structures']=[z for z in N['unmet_formal_seed_structures'] if z['old_locator_id'] not in closing];assert before-len(N['unmet_formal_seed_structures'])==4
for z in cases:
    N['closed_finite_formal_seed_structures'].append({'old_locator_id':z['old_locator_id'],'path':F['source_identities']['F08']['path'],'line':z['line'],'case':z['case'],'children':[c['id'] for c in z['children']],'status':'FINITE_STATIC_CHILD_RECEPTION_COMPLETE','external_catalog_primary':False,'receipt':'sf07-09-11-12-full-child-reception.v2.json'})
N['updated_utc']=NOW;N['new_manual_atomic_membership']=f"1683manual finite sourceassertions; {len(REV['mappings'])}reverse bindings=992historicalregion+{len(REV['mappings'])-992}explicitmanualchild/audit routes. True normalized overall denominatorOPEN. Original969unmet seed membership now965after four exactSFrow closures; immutableoriginalnavigation retained in v1."
for z in N['remaining_groups']:
    if z['id']=='FAC-OPEN-ATOMS':z['finish']='Manually normalize/exhaust source/formal compoundchildren;1683finiteassertions andcurrent2162routes not wholetrue denominator.965remaining seed structures/202external need exactchilddispositions; fourSF rows closed only within packetpremises.'
dump('next-dispatch.json',N)
P=json.loads((V/'progress.json').read_text());P.update(updated_utc=NOW,source_to_formal_bindings=len(REV['mappings']),finite_new_child_bindings=len(REV['mappings'])-992,original_formal_seed_locators_still_unexhausted=len(N['unmet_formal_seed_structures']),new_SF_exact_case_children=packet['child_count']);dump('progress.json',P)
D=json.loads((V/'atomic-denominator.json').read_text());D['updated_utc']=NOW;D['finite_reverse_bindings'].update(count=len(REV['mappings']),qualification=f"992historicalregionbindings+{len(REV['mappings'])-992}newexplicit source/audit/case-child routes, notglobalformaldenominator.");D['full_original_atomic_denominator']['unmet_original_paragraph_table_locators']=len(N['unmet_formal_seed_structures']);D['finite_SF_exact_case_children']={'rows':4,'children':packet['child_count'],'membership':'sf07-09-11-12-full-child-reception.v2.json','overlap':'Source1683assertion IDs reused, do not count42casechildren as42newsourceatoms.'};dump('atomic-denominator.json',D)
L=json.loads((V/'reading-ledger.json').read_text());L['updated_utc']=NOW;L.setdefault('v2_additional_source_reads',[]).append({'utc':NOW,'path':'sf07-09-11-12-full-child-reception.v2.json','complete_named_units':len(units),'actual_receipts':packet['source_units_actual_reads'],'qualification':'Only named finite storage/Dex/flag/ball/source units; no wholeotherdomainFULL. ExtraDexunitsdo notbyavailabilitycloseSF21.'});L['failures'].append({'receipt':'eb611f','meaning':'Metadata used wrong seed key id; recovered actual old_locator_id via92828d. No source/semantic/read credit from failed query.'});dump('reading-ledger.json',L)
print('casechildren',packet['child_count'],'reverse',len(REV['mappings']),'unmet',len(N['unmet_formal_seed_structures']))
b=(V/'sf07-09-11-12-full-child-reception.v2.json').read_bytes();print(len(b),hashlib.sha256(b).hexdigest())
