# Historical manual authoring transcript only. Frozen JSON includes subsequent explicit corrections; do not rerun over the final evidence.
"""One further manually authored finite batch; not a behavior model."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
f = json.loads((ROOT/'forward-mapping.json').read_text())
r = json.loads((ROOT/'reverse-mapping.json').read_text())
assert len(f['atoms']) == 458

def group(source, unit, formal, assertions, joins=()):
    for text in assertions:
        a = dict(id='FAC-A%04d' % (len(f['atoms'])+1),source=source,unit_locator=unit,
                 assertion=text,formal_receivers=formal,
                 premise='Fixed default R/B8; nonnegative normal session counters; valid ordinary rules/data/UI dependencies through this observation point; no override. Finite static source agreement, not runtime or all-PBS-row qualification.',
                 pending_dependencies=list(joins),status='LOCAL_FACT_WITH_NAMED_JOIN_OPEN' if joins else 'BOUNDED_SOURCE_AND_FORMAL_RECONCILED',
                 evidence='SOURCE_STATIC',execution='NOT_EXECUTED',reader='/root/facility_atomic_completion_cloud')
        f['atoms'].append(a)
        for v in formal:
            r['mappings'].append(dict(formal_clause=v,atomic_assertion=a['id'],meaning=text,source=source,source_unit=unit,premise=a['premise'],status=a['status'],pending_dependencies=list(joins),relation='AUTHOR_SELECTED_RECEIVER_REGION; complete per-compound-child reverse signoff remains OPEN'))

group('R09','pbBattleFactoryPokemon', ['F03 §2.6','F09 WP57 §2.1–§2.3'],[
 'Factory group is the minimum of win_count integer-divided by seven and seven.',
 'Open selection is used exactly when suggested level equals GrowthRate.max_level.',
 'Ordinary group zero selects unscaled endpoints zero and173.',
 'Ordinary group one selects unscaled endpoints174 and272.',
 'Ordinary group two selects unscaled endpoints273 and371.',
 'Ordinary group three selects unscaled endpoints372 and491.',
 'Ordinary group four selects unscaled endpoints492 and610.',
 'Ordinary group five selects unscaled endpoints611 and729.',
 'Ordinary group six selects unscaled endpoints730 and849.',
 'Ordinary group seven selects unscaled endpoints372 and881.',
 'Open group zero selects unscaled endpoints372 and491.',
 'Open group one selects unscaled endpoints492 and610.',
 'Open group two selects unscaled endpoints611 and729.',
 'Open group three selects unscaled endpoints730 and849.',
 'Open groups four through seven each select unscaled endpoints372 and881.',
 'Each endpoint is separately multiplied by actual pool length and integer-divided by881.',
 'The lower IV comes from [3,6,9,12,15,21,31,31] at the group index.',
 'The upper IV comes from the next group index capped at seven.',
 'The initial lower-IV count is six.',
 'Swap count15 changes the lower-IV threshold to five.',
 'Swap count22 changes the lower-IV threshold to four.',
 'Swap count29 changes the lower-IV threshold to three.',
 'Swap count36 changes the lower-IV threshold to two.',
 'Swap count43 and above changes the lower-IV threshold to one.',
 'The generator saves both original ruleset length bounds before temporary mutation.',
 'An empty exclusion list temporarily sets the ruleset exact number to six.',
 'A nonempty exclusion list temporarily sets exact number to old maximum plus exclusions length.',
 'An empty exclusion list generates six new Pokemon in each attempt.',
 'A nonempty exclusion list generates old maximum new Pokemon in each attempt.',
 'Sampling includes both scaled endpoints.',
 'An endpoint of881 scales to actual pool length N, so sampling that endpoint returns no template and fails at createPokemon.',
 'A zero-length pool scales both endpoints to zero, so the random bound is one and creation receives no template.',
 'Within an attempt, prior sampled templates are not removed or rejected before construction.',
 'Batch position before append determines whether the lower or upper IV is used.',
 'Each Factory candidate is created at suggested level with a nil trainer argument.',
 'Whole-attempt validation receives a fresh array concatenating the new party and exclusions.',
 'A failed validation retries after clearing the new party.',
 'The retry loop has no iteration limit.',
 'The original ruleset bounds are restored only after successful validation.',
 'A creation exception or nonterminating validation loop does not execute the normal bounds-restoration tail.'
])
group('R07','BattleFactoryData.pbPrepareRentals/pbPrepareSwaps/pbChooseRentals/pbChooseSwaps', ['F09 WP57 §2.5/§3/§4/§5'],[
 'Initial preparation generates six rental candidates before obtaining opponent candidates.',
 'Initial opponent generation uses the entire rental-candidate collection as exclusions.',
 'The opponent party is a sample of three from the returned opponent candidates.',
 'Opponent display name and trainer type come from the selected trainer record.',
 'Opponent win and lose texts use the corresponding frontier message dictionaries.',
 'Preparing a swap saves the previous opponent party reference before replacing the opponent object.',
 'Preparing a swap concatenates current rentals and the previous opponent party as exclusions.',
 'Rental confirmation stores the returned collection before asking the active session to add a swap.',
 'Rental confirmation submits that same returned collection to the session setParty operation.',
 'A completed swap asks the session to add a swap only when the UI returned true.',
 'The swap wrapper calls setParty regardless of whether the UI returned true or false.',
 'The swap wrapper returns the UI Boolean only after the fade block completes.'
])
group('R11','BattleSwapScene rent/swap/commands/selection', ['F09 WP57 §3/§4'],[
 'Rental mode uses the RENTAL POKéMON title and initially empty choices.',
 'Rental rows show species name followed by species category and Pokemon label.',
 'Selected rental indices receive the red text tag.',
 'The rental helper prompt distinguishes zero, one and at least two selected entries.',
 'The rental caller passes canCancel false, so the scene Back input does not return a cancellation.',
 'The swap first screen lists current Pokemon plus a final CANCEL entry.',
 'The swap second screen lists new Pokemon, PKMN FOR SWAP and CANCEL in that order.',
 'The swap second-screen extra row returns minus two, which requests the first screen.',
 'Back or the final cancel entry returns minus one when cancellation is permitted.',
 'Summary returns its current index to the scene list without replacing any rental slot.'
])
group('R11','BattleSwapScreen.pbStartRent', ['F09 WP57 §3'],[
 'Rental item commands are SUMMARY, RENT or DESELECT according to membership, and OTHERS.',
 'SUMMARY opens a summary view without selecting the entry.',
 'DESELECT deletes the chosen index and redraws choices.',
 'RENT appends the chosen index and redraws choices.',
 'Reaching three selected entries asks for confirmation.',
 'Refusing the three-member confirmation deletes the just-added third entry.',
 'Accepting the confirmation creates a new return array containing the selected original Pokemon references in chosen order.',
 'OTHERS has no matching action branch.',
 'The normal rental selection loop has no cancel return and ends only on accepted three-member confirmation.'
])
group('R11','BattleSwapScreen.pbStartSwap', ['F09 WP57 §4/§5'],[
 'The first-screen Pokemon submenu offers SUMMARY, SWAP and RECHOOSE.',
 'RECHOOSE has no dedicated case action and returns to the first-screen loop.',
 'SWAP saves the selected current slot before entering the second-screen loop.',
 'Refusing an offered replacement keeps the second-screen loop active.',
 'Accepting a replacement first ends the scene, then assigns the original newPokemon object into the selected current slot.',
 'This assignment neither clones Pokemon fields nor rewrites their Owner records.',
 'Successful assignment returns true.',
 'The second-screen extra row resets the first-screen list and breaks only the inner loop.',
 'Either cancel route asks Quit swapping before returning false.',
 'Refusing that quit confirmation stays in its current first or second screen.',
 'Accepted cancellation ends the scene without replacing a slot and returns false.'
])

f['bounded_denominator']=len(f['atoms'])
r['true_bounded_assertions']=len(f['atoms'])
(ROOT/'forward-mapping.json').write_text(json.dumps(f,ensure_ascii=False,indent=2)+'\n')
(ROOT/'reverse-mapping.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(len(f['atoms']),'manual finite assertions',len(r['mappings']),'region bindings; original exhaustive denominator OPEN')
