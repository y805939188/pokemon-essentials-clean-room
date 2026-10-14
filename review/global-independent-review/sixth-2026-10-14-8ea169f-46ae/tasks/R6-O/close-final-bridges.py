from pathlib import Path
import json
import datetime
import hashlib
import collections
out = Path('review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-O')
inv = json.loads((out / 'inventory.json').read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
prefix = 'reference/pokemon-essentials/Data/Scripts/'
def e(path, start, end, fact):
    return {'path': prefix + path, 'lines': [start, end], 'fact': fact, 'grade': 'SOURCE_STATIC_NEW_OWN_NECESSARY_JOIN', 'owner': 'R6-O'}
mail = [
    e('013_Items/006_Item_Mail.rb', 1, 125, 'Full125 newread: mail primitive attribute tuples snapshot party k+2/k+1/actualrecipient, no live member references; write only after nonemptytext, emptycancel createsnone; mailbox cap10; reading requests saved tuples.'),
    e('013_Items/001_Item_Utilities.rb', 781, 853, 'Give/take complete helper read: egg guard, remove oldmail first; swap newitemremove then olditemadd, cancelled mail returnsnewitem but olditemadd notretracted; bagcapacity first evenPC intent; mailbox/remove/helditem clearing partial prefixes.'),
    e('014_Pokemon/001_Pokemon.rb', 586, 599, 'Mail setter validates record type only; getter clears unmatched mail and returnsnil.'),
    e('016_UI/019_UI_PC.rb', 58, 104, 'PC senderlist/read/movetobag/give complete caller; successful add before message/delete; canceled choices donottransfer.'),
    e('016_UI/005_UI_Party.rb', 938, 956, 'PC Give prompt beforetemporary mail attach then getter reads mail.item; validemptyheld recipient clears unmatched mail thennil.itemfails before heldwrite/delete/normalend. Existing mail/item andegg guards rejectearlier.')
]
gift = [
    e('016_UI/024_UI_MysteryGift.rb', 1, 428, 'Full428 new read: create/edit sourceobtain_text writebeforelatercancel, sessionEdit/Delete notmasterwrite, Receive shares creature; download filters onlyinitialqueue so duplicatepayloadIDs survive, animation/messages precedequeue; unclaimedfirstmatch delivery mutatescreature PID/stats/time/source beforecapacity, successmessage then[id], itemprecheck/add/message/[id], nonempty decodeerror outward; no codec/network execution.'),
    e('001_Technical/002_Files/003_HTTP_Utilities.rb', 1, 83, 'Full83: HTTPLite transportexception empty, Hash non200 empty, nonHash returnraw; wrappercatch does notcover laternonemptygift decode. No networkcalled.'),
    e('019_Utilities/002_Utilities_Pokemon.rb', 1, 292, 'Full292 newread: capacitybeforeconstruct in obtainhelpers; silentadd explicitseen/owned plusconditionalform, silentparty onlyform+owned; nicknameandstore repeatsseen/owned; gift capacity failure preserves earliergiftobjectprefix; egg constructorcan formregister butwrapperno directseenegg. Balancedlevel mean/stdevweights andsizeformula also read, native0.')
]
subscriber = [
    e('013_Items/002_Item_Effects.rb', 147, 166, 'Repelplayerstep afterDayCare: positivecounter/nonice then−1; expiredflaggeditems controls message orconfirm/filterbag/use; no globalcounterbyitself.'),
    e('013_Items/005_Item_PokeRadar.rb', 239, 267, 'Radarplayerstep batterypositive andnochain decrement; badland/rustle terrain cancels; enteredmap alwayscancel.'),
    e('014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb', 441, 460, 'Shadowplayerstep ablearray, nonzeroheartgauge counter256 andreadymove updates; chamber update aftermemberloop byexistence, no positivegauge/member gate.'),
    e('016_UI/001_Non-interactive UI/003_UI_EggHatching.rb', 252, 268, 'Hatchplayerstep perparty sequential: positiveegg−1 before scan currentnonEggParty; first FasterEggHatching reducesoneextra/break, selfnewlynoneggeligible; clamp0 thenhatch; no crosspartyparallel.'),
    e('013_Items/004_Item_Phone.rb', 543, 560, 'Phoneframe afterworldcue beforelatecontest: busy menu/battle/message/forcing/interpreter pausesboth clocks; readywallsecond loop thenincomingdelta loop.'),
    e('003_Game processing/005_Event_Handlers.rb', 67, 95, 'Named ordered handler collection dispatch; fixed registeredsource sequence plus callbackguards, not blanket effect guarantee.')
]
heal_debug = [
    e('015_Trainers and player/001_Trainer.rb', 155, 171, 'heal_party eachmember calls individualheal; completeheal coverage staysindividualegg guard/PPall/readyevo clear, coreown268–306.'),
    e('014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb', 178, 264, 'Copy/move/movecaught/store complete methods read: configuredboxheal saves/readyevo thenheal/restores it; directheal does notrestore. StoreCaught canheal beforefailure, statedvectorhasvalidspace. No new fullStoragefile claim.'),
    e('020_Debug/003_Debug menus/007_Debug_PokemonCommands.rb', 113, 147, 'CompletePokérus menu callback: randomgive calls existing curedguard; make noninfectious onlypositiveword preservesstrain/zeroeslowtime; clearword0; three actions no directarbitrarystrain/daysinput.'),
    e('014_Pokemon/001_Pokemon.rb', 786, 832, 'Corevirus complete methods ownread: stages/validstrain/default0random, curedregrant reject beforestat, resettime recuresactive, loweronlystage1, curelowtime0.')
]
C = json.loads((out.parent / 'R6-C/cross-interface-O.json').read_text())
K = json.loads((out.parent / 'R6-K/named-review-units.json').read_text())
ku = [x for x in K if x['id'] in ['K-U109', 'K-U110', 'K-U111', 'K-U112']]
rows = [json.loads(line) for line in (out / 'reverse-matrix.jsonl').read_text().splitlines()]
receipts = []
for row in rows:
    pending = row.get('pending_bindings', [])
    if not pending:
        continue
    completed = []
    for label in pending:
        evidence = None
        judgement = ''
        if label == 'K trainer/item matching exactfiles':
            evidence = [e('011_Battle/004_Scene/002_Scene_Initialize.rb', 94, 151, 'Actual backdrop complete method ownjoin alreadyclosed O-J-BATTLE-BACKDROP; this oldtrainer/item broadlabel notapplicable to86heading/88backdropclause.')]
            judgement = 'Existing old sectionwide pending narrowed to actual backdrop source, no new missing consumer.'
        elif label == 'K/C/UI foreign registered subscribers':
            evidence = subscriber
            judgement = 'Fixed source registration order freshly reconnected; O ownworld/DayCare/Safari F/currentUI plusHash dispatch, no pluginmodified order claim.'
        elif label == 'C battle Pokérus source snapshot binding':
            evidence = [e('012_Overworld/001_Overworld.rb', 20, 34, 'Interpretation query actualguard and frame update alreadyownwholeworld750'), e('012_Overworld/007_Overworld_DayCare.rb', 239, 255, 'Breeding source probability normalcurrent field'), e('012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb', 428, 429, 'Wild source probability')]
            if row['lines'][0] == 113:
                evidence += heal_debug[-2:]
            judgement = 'Battle snapshot exact111 alreadyC-bound; other109/110/112/113/114 are wild/breeding/daily/debug/query clauses andmustnot inherit broadC pending.'
        elif label == 'K heal/storage/debug direct consumers' or label == 'K/C storage/debug/virus consumer':
            evidence = heal_debug + subscriber
            judgement = 'Necessary fullmethods/callbacks new ownread, K source fullprimary received; sourcefield defaults/persistence alreadyowned. Sourcegetter/eventcaller coverage not fullnative/game validation.'
        elif label == 'K/UI mail/gift consumers':
            evidence = mail if row['lines'][0] <= 108 else gift
            judgement = 'Current K mail/schema getter full88source proof received plus owncomplete necessary mail/helpers/PCGive andfullGift428/HTTP83/PokemonUtilities292; exactsharedcatalog normal/cancel/error/prefix cases compared.'
        elif label == 'K/UI storage/mail consumer':
            evidence = mail + [e('016_UI/017_UI_PokemonStorage.rb', 1, 2022, 'Actualcompleted R6-UI source32/own wholeStorage2022 received, conditional summaryGive index/heldcaller facts in current forward records; no O wholeStorage claim')]
            evidence[-1]['grade'] = 'SOURCE_STATIC_IMPORTED_CURRENT_COMPLETED_PRIMARY'
            evidence[-1]['owner'] = 'R6-UI'
            judgement = 'Mail tuple actualrecipient independent ofparty membership. Existing k callers andholding index retained bycompletedUIprimary, no wholeO Storage credit.'
        if evidence is None:
            continue
        row['evidence'] += evidence
        completed.append(label)
        receipts.append({'block': row['id'], 'label': label, 'judgement': judgement, 'evidence': evidence})
    row['pending_bindings'] = [label for label in pending if label not in completed]
    if row['status'] in ['LOCAL_FACTS_CHECKED_FOREIGN_CONSUMER_BINDING_PENDING', 'FOREIGN_PRIMARY_PENDING_CURRENT_BINDING'] and not row['pending_bindings']:
        row['status'] = 'FINAL_CURRENT_STATIC_INTERFACE_BOUND'
(out / 'reverse-matrix.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows))
receipt = {
    'at': now, 'receipts': receipts, 'K_current_units': ku,
    'K_read_status': json.loads((out.parent / 'R6-K/task-status.json').read_text()),
    'C_current_interface': C,
    'primary_credit': 'K actual88source/43formal newread0unread, UIactual32source/9formal+catalog; their ongoing foreign proof does not prevent their own sourcefacts here. O independently complete necessary functions/callbacks/fullfiles as recorded.',
    'artifacts': [{'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in [out.parent / 'R6-K/named-review-units.json', out.parent / 'R6-K/forward-source-matrix.jsonl', out.parent / 'R6-K/task-status.json', out.parent / 'R6-C/cross-interface-O.json']],
    'runtime': 'No executions for these final bridges; source0native/UI/network/save. SeparateOprobes actual3success22vectors2failed.'
}
(out / 'received-K-final-bridges.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
# Count exact newreading separately from peer imports; inventory UI Gift is now also ownfullread.
with (out / 'reading-ledger.jsonl').open('a') as log:
    for source in mail + gift + subscriber + heal_debug:
        path = source['path']; a, z = source['lines']
        full = a == 1 and z == len(Path(path).read_text().splitlines())
        log.write(json.dumps({'at': now, 'kind': 'source' if path == inv['sources'][99]['path'] else 'source_external_join', 'path': path, 'start': a, 'end': z, 'complete_unit': full, 'summary': source['fact'], 'semantic_judgement': 'Fresh exact/full necessary source reading; allsharedowncatalog evaluated under its stated limits; no wholefile claimfrompartial', 'execution': 'NOT_EXECUTED'}, ensure_ascii=False) + '\n')
with (out / 'command-log.jsonl').open('a') as log:
    log.write(json.dumps({'at': now, 'command': 'FullGift428/HTTP83/Mail125/PokemonUtilities292 + listed necessarymethod/callback reads and close-final-bridges.py', 'result': 'Old broadpending labels replaced by exact new evidence/currentprimaryreceipts, not parserautoPASS; failedguessedStoragepath no read credit then corrected.'}, ensure_ascii=False) + '\n')
forward = [json.loads(line) for line in (out / 'forward-matrix.jsonl').read_text().splitlines()]
for row in forward:
    if row['source'] == inv['sources'][99]['path']:
        row.update(own_read=True, status='FULLTEXT_SOURCE_STATIC_FACTS_MAPPED', named_fact=gift[0]['fact'], consumers=[{'formal': inv['formal'][18]['path'], 'lines': [109, 128], 'clause': 'MG14–MG32 and currentsharedprefixes'}])
(out / 'forward-matrix.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in forward))
assert not any(row.get('pending_bindings') for row in rows), [(row['id'], row.get('pending_bindings')) for row in rows if row.get('pending_bindings')]
print(json.dumps({'bridge_records': len(receipts), 'pending': 0, 'statuses': dict(collections.Counter(row['status'] for row in rows))}, ensure_ascii=False))
