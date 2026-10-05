"""B09 document/identity bookkeeping only. Never loads or executes reference code.

The formal authoring script is a draft step; this script reads the current final
files, including the bounded refinements recorded in formal-change-log.json.
"""
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[6]
BASE = '407536adb682a04161d3e9c82f153a62b1becd97'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
HISTORY = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
OUT = pathlib.Path(__file__).resolve().parent
CONTRACT = ROOT / 'review/remediation/20261003-prepare/batches/B08/acceptance-stage-1/B09-downstream-contract.json'
SOURCE = pathlib.Path('/workspace/b09-reference')

def git(*args, cwd=ROOT):
    return subprocess.check_output(['git', *args], cwd=cwd)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def identity(path, commit=None, cwd=ROOT):
    raw = git('show', commit + ':' + path, cwd=cwd) if commit else (cwd / path).read_bytes()
    blob = git('rev-parse', commit + ':' + path, cwd=cwd).decode().strip() if commit else git('hash-object', path, cwd=cwd).decode().strip()
    return dict(path=path, commit=commit, git_blob=blob, sha256=sha(raw), bytes=len(raw))

def lines_with(path, text):
    return [i for i, line in enumerate((ROOT / path).read_text().splitlines(), 1) if text in line]

c = json.loads(CONTRACT.read_text())
formal = c['allowed_formal_write_paths']
original = [p['original_path'] for p in c['potential_original_sync_contract']]
ledger = json.loads((OUT / 'formal-change-log.json').read_text())
proposal = json.loads((OUT.parent / 'scope-proposal-1/original-sync-proposal.json').read_text())
bounded = json.loads((OUT / 'bounded-reader-log.json').read_text())
bounded_by_path = {r['path']: r for r in bounded}
combat = 'deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md'
capture = 'deliverables/final-specification-set/test-catalog/pokemon-rules-wp31-32-37-38.md'

# Entire authoritative controls remain in the fixed contract; we expose all
# currently effective qualifications, roots and registered extension reviews.
case_map = {
    '003': [], '005': ['CM-31'], 'A047': ['G11', 'G12'],
    'A049': ['G13', 'G10'], 'A059': ['BC-23', 'BC-24', 'BC-25'],
    'B001': ['CM-30', 'CM-15', 'CM-16'], 'B002': ['BC-19', 'BC-20'],
    'B003': ['BC-21'], 'B005': ['CP01', 'CP24', 'BC-12', 'CM-05', 'CM-08', 'CM-12', 'SW-09'],
    'B006': ['CM-02', 'CM-33'], 'B007': ['CP10', 'CP23'],
    'B008': ['CM-32', 'CM-19', 'CM-20'], 'B009': ['BC-22'],
    'B011': ['R04'], 'B012': ['SW-28'], 'B013': ['CP20', 'CP21', 'CP22', 'E14', 'CX40', 'CX41', 'CX42'],
    'B014': ['SW-29'], 'B015': ['R10'], 'B025': ['R11', 'R08'], 'D018': ['R09']
}
notes = {
    '003': 'B09 only: WP39 battle roles/participants/partner/initialization and WP40 choices/ordering. Necessary shared identities, seats, nine layouts, input syntax, failure side effects and effective priorities retained. Other registered extensions remain assigned to their owners.',
    '005': 'Normal 3v3 later state: 2 fainted/no reserve, 4 living; no candidate text for 4, member/data-box highlight possible, button unselected, USE still registers 4; unchanged layout execution rejects distant 4. 2 living and no living nonself ally contrasts kept; B033 separate.',
    'A047': 'WP30 accepted integer contract consumed in final WP42; five originals retain correct A047 material. No new correction of a correct original. Floors of individual shares, early zero, integer division by5, sequential multipliers and prior EV writes are separate.',
    'A049': 'WP42 original correct single-creature forget summary preserved; final WP42 clarifies 4 old + 1 new move, slot/-1, no party-selection layer. General teaching PP retention remains separate.',
    'A059': 'Six independent selection entries, Intro memory, normal consumers, nil/empty distinction, presets, direct FromType with no fixed ordinary consumer, skip/override/normal return boundaries. Correct WP24/PT41–63/WP15/WP16/K29 retained; NA successor proposal only.',
    'B001': 'Before-PP rejection clears recent-used move/type for ordinary and special calls; only regular move/target pair retained by special. Special accuracy/Struggle differences and unrelated PP rows retained.',
    'B002': 'First failure for existing NPC all-fainted nonempty party and sparse earlier owner segment is specified without normalizing absent counts; generated input versus existing object separated; earlier record/rule-clear commits not rolled back.',
    'B003': 'All14 exact clause literals retained; three consumer-only names have no fixed facility setter. sleep is not sleepclause. SkillSwap common target gate preserved; WP47-B local row cannot override it.',
    'B005': 'All five root incomplete-premise rows plus SW09 extension receive qualified forward/reverse outcomes; no default enemy count creates a partner, no absence of ring creates Primal eligibility.',
    'B006': 'ANY false/FOREIGN true defaults independent of generation; threshold and configured own/foreign contrasts supplied.',
    'B007': 'Heavy Ball reads effective current battle weight in0.1kg, not base weight; temporary, ability suppression and item-validity pipeline retained; old/new thresholds remain.',
    'B008': 'Valid authored Direct5 consumable only: normal menu default eligibility, registration deduction, no effect/no refund. Families1/2 and3 existence gates distinct; unknown items excluded.',
    'B009': 'Event-touch trigger2, all other trainer candidate gates, unique-other candidate and input capacity constraints preserved; render priority not used as trigger type. No actual map/Demo proof.',
    'B011': 'Perish faint handling already clears Flinch before phase14 early return; Reflect1 and EOR flag can remain; normal tail contrast retained.',
    'B012': 'Manual Shift clears Fury Cutter/multiturn, not Counter damage; Counter target remaps independently and ordinary EOR tail later clears it.',
    'B013': 'Primary qualified double-wild partner case requires no KnockOff. Shared boxed identity and shifted six-player records write through old merged participants, including arbitrary middle member. No-partner aligned case, legitimate temporary KnockOff Shadow-Snag route, permanent consumption and WP32 current-item timing kept.',
    'B014': 'Damaging pivot uses actual successful-hit count; Ice Face0 HP loss with1 successful hit can pivot subject to all remaining gates. Intermediate damage1 is not HP loss1.',
    'B015': 'Off-field available future-source initialization clears current living members\' cross-relations to saved seat before data read; current occupant need not switch. Source still on-field contrast and future-position early failures kept.',
    'B025': 'Checkpoint takes passed/saved Perish source; ordinary selfKO draw separately uses last move user with unchanged direction. Full noninternal Lapras/Growl four-round fixture and last-mover contrast retained.',
    'D018': 'Full collect-then-execute rule includes both sides, global near-pair break retaining earlier plans, owner filter, established endpoints, double-side multi-plan skip, triple continuation and no post-first-move near recheck. Manual Shift cost and full entry are excluded.'
}

dispositions = []
for control in c['contribution_controls']:
    fid = control['id']; short = fid.removeprefix('GIR-FD82-')
    obj = control['complete_original_object']
    accepted = control['complete_approved_acceptance']
    edits = [r for r in ledger['changes'] if fid in r['finding_ids']]
    orig_edits = [dict(path=f['path'], clause=r['clause']) for f in proposal['files'] for r in f['clauses'] if fid in r['finding_ids']]
    extensions = [dict(report=e.get('report'), raw_id=e.get('raw_id'), root_review=e.get('root_review'), local_disposition='B09 local clause/identity only; owner allocation and pending controls below govern other loci') for e in obj.get('extensions', [])]
    dispositions.append(dict(
        id=fid, primary=control['primary'], primary_owner=control['primary_owner'],
        author_disposition='COMPLETE_LOCAL_CANDIDATE_PENDING_INDEPENDENT_REVIEW',
        canonical_state='OPEN', canonical_closed=False, source_control=dict(
            contract_identity=identity(str(CONTRACT.relative_to(ROOT)), BASE),
            complete_original_object_sha256=control['original_complete_object_sha256'],
            complete_approved_acceptance_sha256=control['acceptance_object_sha256'],
            current_qualifications=obj.get('current_qualifications'),
            effective_case_constraints=obj.get('effective_case_constraints'),
            root_adjudications=obj.get('root_adjudications', []),
            extensions=extensions,
            minimum_revision=accepted.get('minimum_revision'),
            determinate_recheck=accepted.get('determinate_recheck'),
            acceptance_gate=accepted.get('acceptance_gate')),
        local_reason=notes[short], final_changes=[dict(path=e['path'],clause=e['clause']) for e in edits],
        exact_authorized_original_changes=orig_edits, static_case_ids=case_map[short],
        accepted_other_contributors_at_fixed_receipts=control['accepted_other_contributors_at_fixed_receipts'],
        other_contributors_pending=control['other_contributors_pending'],
        no_other_contributor_approval=True))
assert len(dispositions) == 20 and sum(r['primary'] for r in dispositions) == 13
dump('contribution-dispositions.json', dict(count=20, primary_count=13, canonical_required_OPEN=229, canonical_CLOSED=0, dispositions=dispositions, author_self_check_is_approval=False))

# Catalog text is the design; parsing identifiers is not a behavioral execution.
rows = {}
for path in [combat, capture]:
    for n, line in enumerate((ROOT/path).read_text().splitlines(),1):
        if line.startswith('| '):
            cells=line.split('|')
            cid=cells[1].strip()
            if re.match(r'^(BC-|CM-|SW-|G|R|E|CP|CX)\d',cid):
                rows[cid]=dict(path=path,line=n,input_and_premises=cells[2].strip(),static_expected=cells[3].strip(),executed=False)
selected=sorted({cid for ids in case_map.values() for cid in ids})
assert all(cid in rows for cid in selected)
extras = [
    dict(id='B09-ARCH-EQUIVALENCE',finding_ids=['GIR-FD82-003'],premises='Independent representation can use keyed action records and ordering values instead of four/five choice slots or seven-item entries, while maintaining same seats, shared creature identities and isolated battle/persistent states.',expected='All final behavior clauses remain satisfiable; source object-wrapping/tuple layout is unnecessary. Reverse: dropping shared boxed identity would lose CP21/CX40 and is forbidden.',executed=False),
    dict(id='B09-CLAUSE-SKILLSWAP',finding_ids=['GIR-FD82-B003'],premises='Loaded clause consumer; living opposite U/T, distinct valid exchangeable abilities, no substitute/bounce or unrelated failure; normal SkillSwap target path reached. Compare skillswapclause true/false.',expected='True rejects at common target gate, abilities unchanged. False reaches normal exchange and swaps abilities. Local WP47-B row is not an exemption; B11/B13 still own their material.',executed=False),
    dict(id='B09-CLAUSE-SLEEP',finding_ids=['GIR-FD82-B003'],premises='Living target currently no status, otherwise sleep-permitted; living non-egg teammate truly asleep; enemy-origin sleep. Compare only sleep=true versus only sleepclause=true with loaded consumer.',expected='sleep alone does not activate the clause. sleepclause rejects at added sleep gate before ordinary downstream checks; self-origin reverse follows separate modifiedsleep clause rules, no renamed literals.',executed=False),
    dict(id='B09-OBEDIENCE-SEQUENCE',finding_ids=['GIR-FD82-B005','GIR-FD82-B006'],premises='CM-02 high-level foreign ordinary player; prior non-obedience gates pass, a>=40 and b>=40; current level60, L40, c20; no status/Hyper. Fix final r0, canSleep true/false; r20, canSleep true.',expected='r0/canSleep true self-sleeps before self-harm. r0/canSleep false self-harms; r20 self-harms. PP not deducted at this preceding gate. Defaults do not cause own members to enter this high-level path.',executed=False),
    dict(id='B09-OPPONENT-REPLACEMENT',finding_ids=['GIR-FD82-B005'],premises='SW-09 all qualified gates pass. Independently negate internalBattle, switchStyle, player side size1, live player, no prior replacement, legal player reserve, no Outrage, or opponent fainted with legal reserve.',expected='Each missing required gate removes voluntary player prompt. When only switchStyle=false, opponent automatic replacement remains; no guarantee of a successful replacement when its own reserve is removed.',executed=False),
    dict(id='B09-EXP-INTEGER-STAGES',finding_ids=['GIR-FD82-A047'],premises='Valid participant/shared integer allocation and no unrelated multipliers. a7, participant count2, sharer count2, member has both roles, sharing on; separate authored a1/two participants zero-share input; separate scaled factor test G11. For downstream multipliers, enter charm stage with integer13, no foreign multiplier, valid EXPCHARM in bag, valid current LUCKYEGG, no additional item modifier, internal nonMega member with affection>=4 and affection effects enabled, ample experience room.',expected='Combined shares floor(7/4)+floor(7/4)=2, not floor(7/2)=3. Zero share exits before trainer/scale/+1 while prior EV survives. G11 yields13. Sequential charm13→19, LuckyEgg19→28, affection28→33; combined real multiplier would wrongly give35. Current item has result so restored item not additionally applied; removing all three multipliers keeps13.',executed=False),
    dict(id='B09-FORGET-CANCEL',finding_ids=['GIR-FD82-A049'],premises='G13 normal summary opened for one creature; first select HM slot0 with debug false, then nonHM1; independently BACK or fifth/new item then Give-up Yes/No; caller scene/assets otherwise work.',expected='HM refusal stays selection; old slot1 returns1; BACK/fifth returns-1. Give-up Yes keeps old moves and prior growth; No returns to same single-creature summary. Debug true permits HM selection. General machine old-PP preservation is not battle replacement.',executed=False),
    dict(id='B09-AUDIO-MATRIX',finding_ids=['GIR-FD82-A059'],premises='Valid metadata/type/audio conversion with no plugin interception. For each of six WP39§7.5 entries vary independent preset X, matching map M, global G; ordinary ordered trainer fields [A,B]/[A,nil]/[nil,nil]/[A,actually stored empty]. Direct same empty type tested separately.',expected='Each matching nonempty preset wins independently. Ordinary trainers B/A/M/G/default according to stated gates; stored trailing empty overwrites A then falls backM. Direct empty produces empty request, with no located ordinary fixed Scripts caller. Wild battle/victory/capture defaults Battle wild/Battle victory/Battle capture success; trainer battle/victory defaults Battle trainer/Battle victory. Selection does not clear presets or prove media output.',executed=False),
    dict(id='B09-AUDIO-MEMORY-CONSUMERS',finding_ids=['GIR-FD82-A059'],premises='Valid nonempty IntroI with existing memoryR/r, absent memory plus queuedQ/timer, absent memory/no timer plus current music positionp/failed position query; empty Intro contrast. Normal core, admission skip, handled override, normal return and post-state playback failure separated.',expected='ExistingR/r preserved including queued timer; queue first cancels timer then remembersQ/0, otherwise current/p or0. Empty Intro no request/state change. Normal core uses transition wrapper; wild success only without opposing trainer uses captureME and existing3.5s wait. Skip/override do not gain skipped core consumers. Normal return clears memory/presets; failure does not promise rollback or audio restoration.',executed=False),
    dict(id='B09-HEAVYBALL-ITEM-VALIDITY',finding_ids=['GIR-FD82-B007'],premises='Current form weight1180, delta0, no weight ability; FLOATSTONE active versus item-invalid due to Embargo/MagicRoom/KLUTZ, otherwise normal CP23 conditions. Separate active LIGHTMETAL with mode-break false/true.',expected='Active stone produces590 and new HeavyBall rate25/x8; invalid stone keeps1180 and rate45/x15. Ability suppression skips ability stage but does not independently suppress an otherwise-valid item stage. Unit remains0.1kg; no300kg→300 confusion.',executed=False),
    dict(id='B09-SHIFT-REMAP',finding_ids=['GIR-FD82-B012'],premises='SW-28 manual0/2 same-owner shift with pre-existing Counter damage20; enemy living counter target points0. Other current relations target2. No tail yet.',expected='Damage20 remains; pointers0/2 remap separately; user FuryCutter/multiturn clears and user acted. Same successful position exchange at automatic phase23 preserves manual action-cost boundary; normal tail independently clears Counter fields.',executed=False),
    dict(id='B09-CAPTURE-TEMPORARY-REMOVAL',finding_ids=['GIR-FD82-B013'],premises='Authored legal Shadow trainer Snag capture route, player SnagMachine true, no participating partner, full player party and box space; enemy non-lethally KnockOff-removes valid ordinary heldX from outgoing player member, restoredX retained, both stay alive; later capture last valid Shadow target using Snag-capable ball, receive/send that member. X is not a permanent-consumption example; no extra held-item callbacks.',expected='At send-box same identity has current empty; no-partner synchronized participants exclude it from final loop, so box stays empty. Retain member reverse restoresX at normal end. Permanent consumption with restored record empty stays empty both ways. Primary partner case remains CP21/CX40 without requiring KnockOff or friendly AI attacking own side.',executed=False),
    dict(id='B09-CAPTURE-MIDDLE-WORLD',finding_ids=['GIR-FD82-B013'],premises='CP22 same-identity storage, actual participating partner, only outgoing positionk changes; normal terminal restore before outside partner heal and world achievement/pickup callbacks. No extra party/items callbacks before restore.',expected='Earlier identities unchanged; outgoing oldk receives old(k+1) restore item, each following old member gets successor record, oldlast gets empty. Current-player world consumers read their actual item after this restore, not own historical initial item. Merely registered/nonparticipating partner stays aligned; WP32 already-correct timing and CX40–42 kept.',executed=False),
    dict(id='B09-PIVOT-REMAINDER',finding_ids=['GIR-FD82-B014'],premises='SW-29 IceFace absorbs one successful physical hit with HP loss0. Independently remove legal U reserve, faint U through other effect, exhaust opposing party, switch all original targets already, or make hit miss.',expected='Only complete remaining gates permit pivot. Successful-hit1 alone does not bypass other gates; miss0 rejects. Mode-break true skips valid IceFace ability where applicable and changes absorption outcome, not success-count definition.',executed=False),
    dict(id='B09-FUTURE-SOURCE-CLEANUP',finding_ids=['GIR-FD82-B015'],premises='R10 current target living; saved source off-field but reserve alive. Distinguish target absent/fainted at expiration, source still on-field, off-field source unavailable. No extra data callbacks.',expected='Only reached off-field available initialization produces extra cleanup of current living members pointing at saved seat before data read/attack. On-field reverse does not newly clear. Earlier helper returns can retain auxiliary source/move records per WP45; empty/fainted target does not establish cleanup execution.',executed=False),
    dict(id='B09-PERISH-CHECKPOINT-SIDES',finding_ids=['GIR-FD82-B025','GIR-FD82-B011'],premises='R11 noninternal qualified four-round Lapras input; saved singer side is fixed while final Growl mover changes. Independently swap singer to opponent with same source-side consistency; separately call ordinary both-party-empty selfKO draw with last-user unknown/player/opponent.',expected='Player saved singer gives checkpoint2 regardless of final mover; opponent saved singer gives checkpoint1. Normal last-user selfKO directions unknown5/player1/opponent2 unchanged. Perish formal faint clears Flinch before phase14, later Reflect/EOR tail can be skipped; checkpoint intermediate value is not universally final.',executed=False),
    dict(id='B09-AUTO-PREPLAN-REVERSES',finding_ids=['GIR-FD82-D018'],premises='R09 complete established endpoints, live0/1 only. Compare3v3 vs3v2, player three owners versus single owner, initial near pair. Direct malformed endpoint fixture clearly separate from normal initialized layout; stage23 reached/earlier decision positive contrast.',expected='3v3 ends2/3 despite first move creating near pair; 3v2 ends2/1 because total-plan2 skips double-side item; ownership reverse ends0/3. Initial near pair produces no plans. Missing endpoint rejects that exchange/no message, not other plans. Stage23 not reached implies no adjustment guarantee.',executed=False),
    dict(id='B09-AUTO-EARLIER-PLAN-RETAINED',finding_ids=['GIR-FD82-D018'],premises='Normal1v3 four established seats0/1/3/5, one owner each; only0/5 living, center3 fainted/no reserve, stage23 reached. Side0 size1 skipped, side1 has no near pair. Independently change opponent living5 to living3.',expected='First input plans5↔3 then succeeds, ending0/3. Second already-near input terminates collection with empty plan. Collection rule for encountering a near pair does not erase earlier recorded candidates; no supported normal reciprocal-neighbor example claims earlier plans where symmetry makes them impossible.',executed=False)
]
dump('static-cases.json',dict(status='STATIC_DESIGNS_ONLY',executed=0,runtime_observations=0,proven_Demo_chains=0, catalog_cases=[dict(id=k,**rows[k]) for k in selected], supplemental_designs=extras, old_ids_preserved=True, reference_simulator_used=False))

# Keep inherited named limitations as exact data, not paraphrased away.
dump('source-limits.json',dict(contract_source_limits=c['source_limits'],configuration=c['configuration'],own_limits='Unlisted reference paths/ranges unread. No reference game, compiler, converter, generator, deserializer, historical verifier or behavior simulator executed. PBS samples only stated ranges. Entire actual maps/events/media/fonts/soundfont/host configuration/binaries/backups/gen remain unread/unverified; dynamic dispatch/plugin combinations and real Demo chains not exhausted.',reference_execution=0,behavior_vectors_executed=0,runtime_observations=0,proven_Demo_chains=0,own_identity_bookkeeping='Executed own Python/Git text and hash bookkeeping only; not behavioral vectors or observations.'))
prior=json.loads((OUT.parent/'scope-proposal-1/source-reading-log.json').read_text())
additional = {
 'Data/Scripts/019_Utilities/003_Utilities_BattleAudio.rb': [[1,149]],
 'Data/Scripts/010_Data/002_PBS data/014_TrainerType.rb': [[18,32],[101,116]],
 'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb': [[171,207],[388,401],[493,545]],
 'Data/Scripts/012_Overworld/002_Battle triggering/002_Overworld_BattleIntroAnim.rb': [[67,81],[125,144]],
 'Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb': [[405,431]],
 'Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb': [[337,355]],
 'Data/Scripts/003_Game processing/003_Interpreter.rb': [[418,442]],
 'Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb': [[112,178]],
 'Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb': [[78,118],[539,596]],
 'Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb': [[16,110],[477,514]],
 'Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb': [[1,271]],
 'Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb': [[262,442],[447,469]],
 'Data/Scripts/011_Battle/004_Scene/005_Battle_Scene_Menus.rb': [[515,545]],
 'Data/Scripts/016_UI/006_UI_Summary.rb': [[1232,1280],[1352,1367]],
 'Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb': [[15,79]],
 'PBS/pokemon.txt': [[237,257],[3453,3480],[22519,22545]]
}
new_reads=[]
for p, ranges in additional.items():
    obj=identity(p,REF,SOURCE);count=len((SOURCE/p).read_text().splitlines())
    ranges=[[a,min(b,count)] for a,b in ranges]
    new_reads.append(dict(**obj,displayed_text_ranges=ranges,mode='read-only text; full-file identity is not full semantic coverage',full_file_semantic_read_claimed=False))
search=git('grep','-n','-E','pbGetTrainerBattleBGMFromType|pbGetWildBattleBGM|pbGetTrainerBattleBGM|pbGetWildVictoryBGM|pbGetTrainerVictoryBGM|pbGetWildCaptureME|pbPlayTrainerIntroME', REF, '--','Data/Scripts',cwd=SOURCE).decode()
dump('source-reading-log.json',dict(reference_commit=REF,reference_tree=git('rev-parse',REF+'^{tree}',cwd=SOURCE).decode().strip(),reference_clean=git('status','--porcelain=v1','--untracked-files=all',cwd=SOURCE).decode()=='',proposal_source_reads_reused=prior,additional_source_reads=new_reads, fixed_script_audio_search=dict(pattern='listed selection families; all fixed Data/Scripts tracked text',sha256=sha(search.encode()),matches=search.splitlines(),FromType='definition only; dynamic and plugin consumers unknown'),source_limits_file='source-limits.json',reference_execution=0,behavior_vectors_executed=0,runtime_observations=0,proven_Demo_chains=0))

coverage=[]
for frozen in c['planned_reads']:
    p=frozen['path'];commit=frozen.get('commit',BASE);before=identity(p,commit)
    assert all(before[k]==frozen[k] for k in ['git_blob','sha256','bytes']), p
    current=identity(p,commit) if commit==HISTORY else identity(p)
    if p in formal:scope=dict(mode='own final clause/body and full normative diff review',changes=[e['clause'] for e in ledger['changes'] if e['path']==p])
    elif p in original:scope=dict(mode='own original context and exact approved30-clause before/after verification',proposal='scope-proposal-1/original-sync-proposal.json; original-application.json')
    elif p.endswith('findings.json'):scope=dict(mode='all20 assigned complete effective control objects via fixed contract; raw historical bulk not claimed full semantic reread',ids=c['contribution_finding_ids'])
    elif p.endswith('remediation-index.tsv'):scope=dict(mode='all20 assigned rows/control binding; unrelated rows not semantically reviewed')
    elif p.endswith('source-judgments.json'):scope=dict(mode='row287 BattleAudio full row; remaining file identity only',full_file_semantic_read=False)
    elif p=='AGENTS.md':scope=dict(mode='complete instructions read')
    else:scope=bounded_by_path[p]
    coverage.append(dict(path=p,frozen_input=before,current_refreeze=current,changed=before['sha256']!=current['sha256'],semantic_scope=scope,unread_limits='Unlisted clauses/ranges and unrelated historical reports not semantically claimed; hashes are identity evidence only.'))
dump('read-coverage.json',dict(planned_count=62,bindings_checked=62,semantic_full_all62_claimed=False,readers=coverage,contract=identity(str(CONTRACT.relative_to(ROOT)),BASE),source_limits_file='source-limits.json',additional_reader_ranges='bounded-reader-log.json; reverse-impact.json exact clauses',reference_static_only=True))

# Whole-file locks protect unrelated owners and the exact old ID sequence.
checks=[]
for path,marker in [(combat,'## W：'),(capture,'## CP：')]:
    old=git('show',BASE+':'+path).decode();now=(ROOT/path).read_text()
    protected_old=old.split(marker,1)[1] if path==combat else old.split(marker,1)[0]
    protected_new=now.split(marker,1)[1] if path==combat else now.split(marker,1)[0]
    assert protected_old==protected_new,path
    pattern=r'^\| ([A-Z]+-?\d+b?) \|'
    a=re.findall(pattern,old,re.M);b=re.findall(pattern,now,re.M)
    assert len(a)==len(set(a)) and len(b)==len(set(b)),path
    assert [x for x in b if x in a]==a,path
    checks.append(dict(path=path,whole_file_lock='B09 isolated sole writer; not cross-container lease attestation',protected_region=('all WP45 W/T/F/S/H/P/C sections' if path==combat else 'all pre-CP BE/CX/RM sections'),protected_sha256=sha(protected_old.encode()),protected_bytes=len(protected_old.encode()),protected_identical=True,old_id_count=len(a),current_id_count=len(b),new_ids=[x for x in b if x not in a],old_order_multiplicity_preserved=True))
dump('whole-catalog-lock-check.json',dict(locks=checks,B09_before_B14=True,B14_read_only_preflight_commit='2a496b76e9b18efde71a273fcf33245927e68020',B14_preflight_accepted=False,no_B14_rules_adopted=True,serialization_contract=c['B09_B14_operational_serialization']))

# The normative patch is complete for all12 allowed formal/original files.
patch=git('diff','--binary',BASE,'--',*formal,*original)
(OUT/'formal-and-approved-originals.patch').write_bytes(patch)
dump('normative-identities.json',dict(baseline_commit=BASE,formal_count=7,approved_original_count=5,files=[dict(before=identity(p,BASE),after=identity(p)) for p in formal+original],complete_normative_diff=dict(path='formal-and-approved-originals.patch',sha256=sha(patch),bytes=len(patch)),not_full_candidate_evidence_diff=True))

print(json.dumps(dict(contributions=20,primary=13,read_bindings=62,source_additional_paths=len(new_reads),catalog_design_rows=len(selected),supplemental_designs=len(extras),new_catalog_ids=sum(len(x['new_ids']) for x in checks),formal_files=7,exact_approved_originals=5),ensure_ascii=False))

prefix='deliverables/final-specification-set/'
def owner_clause(path, first, last):
    p=prefix+path
    old=git('show',BASE+':'+p).decode().splitlines(keepends=True)
    now=(ROOT/p).read_text().splitlines(keepends=True)
    before=''.join(old[first-1:last]);after=''.join(now[first-1:last])
    assert before==after,p
    return dict(path=p,before_identity=identity(p,BASE),current_refreeze=identity(p),lines=[first,last],before_text=before,after_text=after,byte_identical=True)

premises={
 'B04': [
   dict(interface='Six audio requests and Intro memory → WP15 playback → WP16 transition',disposition='AFFECTED_CALLER_DOCUMENTATION_REQUIRES_REVIEW',changed_paths=[formal[0]],controls=['GIR-FD82-A059','GIR-FD82-003'],before='WP39 core transitions and cleanup existed but lacked complete selection/preset/empty/Intro request contract.',after='WP39§7.5 consumes already accepted WP24§5.4; ordinary wild/trainer transition category and normal-return boundary preserved. Skip/override branches do not gain ordinary consumers.',static=['BC-23','BC-24','BC-25','B09-AUDIO-MATRIX','B09-AUDIO-MEMORY-CONSUMERS'],not_affected_subscope='WP15 parsing, volume scaling, default music override, paused position, queued timing and media limits: exact owner clauses unchanged; new selection description does not change these stages.'),
   dict(interface='Command registration/execution and growth summary → common message/input/audio primitives',disposition='AFFECTED_READER_PREMISES_REQUIRE_REVIEW',changed_paths=[formal[0],formal[1]],controls=['GIR-FD82-005','GIR-FD82-B001','GIR-FD82-B002','GIR-FD82-B008','GIR-FD82-B005'],before='WP39/40 had structural choice requirements, broad item handler gate, incomplete qualifications and wrong recent-used history.',after='Independent roles, first-failure ordering, Direct5 no-effect deduction, NearAlly anomaly and complete conditional prompts; no new generic input/message or actual audio/output guarantee.',static=['CM-30','CM-31','CM-32','SW-09'],not_affected_subscope='Only common presentation/selection/registration boundaries assessed. Specialized WP67 target/partner/capture business is B17/B09 scope and is not reapproved under old B04 two-caller receipts.'),
   dict(interface='B04 accepted35/23 and prior bounded reverse receipts',disposition='PRESERVE_FIXED_HISTORY_NO_PASS_TRANSFER',changed_paths=[formal[0],formal[1]],controls=['GIR-FD82-A059'],before='Prior accepted B04 and subsequent bounded reviews apply to their exact versions/scopes.',after='New separate R-B04 candidate and actual review must bind current changed readers and unchanged relevant owner clauses. No claim of new full partner/capture/audio/UI approval.',static=['B09-AUDIO-MATRIX'],not_affected_subscope='Other B04 domains are outside this bounded review request, not newly reviewed or closed.')
 ],
 'B07': [
   dict(interface='WP40 item selection/registration/dispatch → accepted WP28',disposition='AFFECTED_CALLER_REQUIRES_REVIEW',changed_paths=[formal[1]],controls=['GIR-FD82-B008','GIR-FD82-003'],before='WP40 claimed all families required an effect handler.',after='Families1/2 and3 existence checks, families4/5 distinct, valid Direct5 default-eligibility/no-effect/no-refund agrees with unchanged WP28§3.5/§6.',static=['CM-32','CM-19','CM-20'],not_affected_subscope='WP28 effect-return refund semantics, inventory deduction and original clauses unchanged; cannot infer safety for an unregistered item.'),
   dict(interface='WP42 growth and full-slot learning → accepted WP30 and growth catalog',disposition='AFFECTED_CALLER_REQUIRES_REVIEW',changed_paths=[formal[3]],controls=['GIR-FD82-A047','GIR-FD82-A049'],before='WP42 relied on WP30 formula/summary contract but did not expose precise truncation/early-zero and single-creature 4+1 distinction.',after='Explicit integer stage/EV ordering and single-creature summary consume accepted WP30; correct originals remain byte-preserved at A047/A049 clauses. General machine PP-preservation separate.',static=['G11','G12','G13','B09-EXP-INTEGER-STAGES','B09-FORGET-CANCEL'],not_affected_subscope='WP30§4.2/§6 and GR51 remain unchanged; B16 A048 empty relearner and C003 A23/A31/A33 are still pending owners, not covered by this caller reconciliation.'),
   dict(interface='WP38/WP42 capture restoration → accepted WP32 current-item timing/CX40–42',disposition='AFFECTED_SHARED_CATALOG_AND_DATA_PREMISE_REQUIRES_REVIEW',changed_paths=[formal[3],formal[4],capture],controls=['GIR-FD82-B013'],before='CP20 and capture prose unconditionally excluded boxed member from restoration while accepted CX40–42 already had qualified partner mismatch.',after='CP20 qualified no-partner path plus CP21/22 and E14 preserve exact accepted same-identity and shifted-record anomaly. Current-player world consumer after restoration reads changed actual items.',static=['CP20','CP21','CP22','E14','CX40','CX41','CX42'],not_affected_subscope='BE/CX/RM whole protected region byte-identical, including CX40–42. Correct WP32 timing remains; this is changed input data, not a new WP32 error.')
 ],
 'B08': [
   dict(interface='WP39 public wild wrapper/core generation and override → WP36/WP37',disposition='AFFECTED_READER_REQUIRES_REVIEW',changed_paths=[formal[0]],controls=['GIR-FD82-003','GIR-FD82-A059','GIR-FD82-B002'],before='Accepted B08 depends on public temporary generation before override, persistent roamer generation/reuse, actual object versus notification identity, skip and normal-return cleanup.',after='All ordinary wrapper/core generation, shared object input, override ordering and temporary-versus-persistent notification premises remain in WP39§3.1/§3.4. New audio request documentation consumes separate roamer preset without adding skipped ordinary-wrapper post-hook. NPC first-failure correction is separately qualified.',static=['BC-01','BC-02','BC-03','BC-07','BC-08','RM34','RM35','RM36'],not_affected_subscope='RM34/35/36 exact rows and WP36§7/WP37§5.1 unchanged. Counts concern generation stage, not final virus distribution. No acceptance transfer; current caller checks required.'),
   dict(interface='WP40 item/command gating → radar/partner conditions',disposition='AFFECTED_READER_REQUIRES_REVIEW',changed_paths=[formal[1]],controls=['GIR-FD82-B008','GIR-FD82-005','GIR-FD82-B005'],before='Radar has separate field/bag qualification and later candidate partner guard; command family statements must not overwrite them.',after='Direct5 is a valid authored battle-item path; radar is important field item with own qualification, no default-family inference. NearAlly/partner BC12 changes do not move radar partner guard to startup permission.',static=['CM-32','CM-31','BC-12','RM37'],not_affected_subscope='WP37§6.1 and RM37 remain unchanged. Normal roam/radar candidate selection requires no partner and forced single, so no default actual partner merged restore example is imported into normal roamer path.'),
   dict(interface='Shared pokemon catalog CP changes with protected RM/BE/CX',disposition='AFFECTED_WHOLE_FILE_REQUIRES_REVIEW',changed_paths=[capture],controls=['GIR-FD82-B013','GIR-FD82-B007','GIR-FD82-B005'],before='Shared accepted file carries entire BE/CX/RM/CP owner populations and unique IDs.',after='Only CP01/10/20 revised and CP21–24 appended; pre-CP region unchanged byte-for-byte. Capture current weight and partner-dependent restoration must be reviewed with earlier B08 roamer restrictions, not treated as catalog-wide prior PASS.',static=['CP01','CP10','CP20','CP21','CP22','CP23','CP24','RM34','RM35','RM36','RM37'],not_affected_subscope='Protected unchanged RM/BE/CX rows retain all qualifiers/limits. New CP rows do not modify ordinary field permission, temporary candidate identity, persistent selection/association or RM30/RM32 first failure.')
 ]
}
owners={
 'B04': [owner_clause('engine-overworld/wp15-resource-matching-and-audio.md',100,138),owner_clause('engine-overworld/wp16-pre-battle-transitions.md',1,42),owner_clause('engine-overworld/wp16-pre-battle-transitions.md',99,111),owner_clause('test-catalog/engine-overworld-wp11-15-59-60.md',399,401),owner_clause('creature-rpg/wp24-player-trainers-partners.md',167,205)],
 'B07': [owner_clause('creature-rpg/wp28-item-use-and-training.md',94,103),owner_clause('creature-rpg/wp30-growth-learning-and-friendship.md',80,115),owner_clause('creature-rpg/wp30-growth-learning-and-friendship.md',150,168),owner_clause('test-catalog/creature-rpg-wp27-28-29-30-33.md',193,197),owner_clause('test-catalog/pokemon-rules-wp31-32-37-38.md',92,94),owner_clause('pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md',20,30),owner_clause('pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md',61,90)],
 'B08': [owner_clause('creature-rpg/wp36-wild-encounters-and-modifiers.md',207,226),owner_clause('pokemon-rules/wp37-roaming-and-poke-radar.md',60,89),owner_clause('test-catalog/pokemon-rules-wp31-32-37-38.md',129,135)]
}
reverse=[]
for gate in c['accepted_reverse_review_gates']:
    batch=gate['accepted_batch']
    paths=list(dict.fromkeys([r['path'] for r in gate['changed_planned_reverse_readers']]+gate['shared_accepted_formal_paths']))
    assert all(p in formal for p in paths)
    changed=[dict(path=p,before=identity(p,BASE),after=identity(p),full_before_after_clauses=[e for e in ledger['changes'] if e['path']==p]) for p in paths]
    manifest_path=f'review/remediation/20261003-prepare/batches/{batch}/acceptance-stage-1/acceptance-manifest.json'
    history=json.loads((ROOT/manifest_path).read_text())
    fixed_acceptance=dict(identity=identity(manifest_path,BASE),reviewed_integration_commit=history['reviewed_integration_commit'],accepted_contributions=history['accepted_original_contributions'],accepted_primary=history['accepted_'+batch+'_primary_contributions'],historical_receipts=c['current_B08_actual_review_receipts'])
    package=dict(batch=batch,author_impact_disposition='AFFECTED_SEPARATE_INDEPENDENT_CANDIDATE_AND_ACTUAL_REQUIRED',author_approval=False,candidate_binding='Exact final candidate freeze-envelope SHA delivered by ordinary push/readback; payload SHA and evidence-only envelope delta must both be reviewed',gate=gate,fixed_acceptance=fixed_acceptance,changed_readers=changed,all62_current_refreeze='read-coverage.json',whole_catalog_guard='whole-catalog-lock-check.json',untouched_owner_clauses=owners[batch],reader_caller_data_condition_analysis=premises[batch],qualified_controls='contribution-dispositions.json fixed contract full root/extension qualifications',static_designs='static-cases.json',complete_normative_diff='formal-and-approved-originals.patch',complete_unfiltered_diff='freeze-envelope/full-predecessor-to-payload.patch plus payload-to-final-envelope delta; final SHA and full-diff hash in pushed handoff',independent_review=dict(requested_model='gpt-6.1-sol',reasoning='Ultra',speed='Standard(default)',effective_configuration='UNVERIFIED under approved Plan A',candidate_required=True,actual_required=True,actual_requirement='A-REG exact integration SHA: full predecessor-to-actual and candidate-to-actual public/management/source deltas; refreeze stale current reader identities and scope; no automatic prior PASS'),closure='No canonical/root/global closure, author self-check is not approval')
    dump('affected-'+batch+'-review-request.json',package)
    reverse.append(package)

other_reader_impacts=[
 dict(owner='B10',control_ids=['GIR-FD82-B015','GIR-FD82-003'],paths=[prefix+'combat-requirements/wp45-weather-terrain-side-and-position-effects.md',prefix+'pokemon-rules/wp46-damage-multihit-and-healing.md'],disposition='AFFECTED_PENDING_OWNER',reason='Future-source helper relation cleanup must accompany existing auxiliary-record early-return limits; own catalog W/T/F/S/H/P/C remains protected.'),
 dict(owner='B11',control_ids=['GIR-FD82-B003','GIR-FD82-B007','GIR-FD82-B014'],paths=[prefix+'combat-requirements/wp47-b-switching-control-and-item-changes.md',prefix+'pokemon-rules/wp48-ability-calculation-modifiers.md',prefix+'pokemon-rules/wp50-held-item-triggers-and-consumption.md'],disposition='AFFECTED_PENDING_OWNER',reason='SkillSwap common clause cannot be bypassed by local row; effective weight and success-count inputs consume unchanged weight/pivot facts, with full owner reviews still pending. No global ability/item reapproval.'),
 dict(owner='B13',control_ids=['GIR-FD82-B003','GIR-FD82-B025','GIR-FD82-003'],paths=[prefix+'combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md',prefix+'combat-requirements/wp54-entry-rules-and-cup-data.md',prefix+'combat-requirements/wp56-palace-and-arena-variants.md',prefix+'combat-requirements/wp58-battle-recording-and-playback.md'],disposition='AFFECTED_PENDING_OWNER',reason='Checkpoint saved source must not be described as last mover; selfKO direction already correct and stays. Exact literals/no-setter facts align with B09; architecture/history and full facility/recording scope remain B13.'),
 dict(owner='B17',control_ids=['GIR-FD82-005','GIR-FD82-A059','GIR-FD82-D018','GIR-FD82-003'],paths=[prefix+'user-interface/wp67-a-battle-interaction-and-presentation.md'],disposition='AFFECTED_PENDING_OWNER',reason='Existing NearAlly adjacent-first UI text conflicts with fixed anomaly; round-end only3-seat description cannot replace full WP42 planning. Request selection vs playback3.5s timing and architectural scope must remain separate; no unauthorized edit to UI.'),
 dict(owner='B14',control_ids=['GIR-FD82-003'],paths=[prefix+'combat-requirements/wp52-a-evaluation-coverage-and-data.md',prefix+'combat-requirements/wp52-b-effect-coverage.md',prefix+'combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md',prefix+'combat-requirements/wp52-c-items-calling-and-control-evaluation.md'],disposition='SERIALIZATION_BLOCKED_UNTIL_ACCEPTED_B09',reason='Changed actual weight, hit-count/target/round planning premises need fresh72 reads/6 writes and semantic dependency assessment. Prior fixed-input read-only preflight2a496b7 is not an accepted upstream or source of unapproved rules.'),
 dict(owner='B15/B16/B19/B20/B21',control_ids=['GIR-FD82-003'],paths=[prefix+'engine-overworld/wp59-world-time-weather-field-moves.md',prefix+'pokemon-rules/wp60-berry-plants.md',prefix+'user-interface/wp63-pokegear-map-music-and-phone.md',prefix+'user-interface/wp65-title-load-options-pause-and-pc.md',prefix+'user-interface/wp66-a-party-and-summary-ui.md',prefix+'demo-dx/wp72-debug-contexts-and-controls.md',prefix+'demo-dx/wp73-a-content-editors.md',prefix+'demo-dx/wp73-b-world-editors.md',prefix+'demo-dx/wp74-battle-animation-authoring-and-exchange.md'],disposition='BOUNDED_READ_ONLY_OWNER_RESIDUALS_PRESERVED',reason='All11 registered003 extension reviews read and retained; B09 does not edit their architectural/compatibility clauses. Debug normal-entry side effects and specialized UI/workflow statements remain owned. Other controls outside B09 are not closed.'),
 dict(owner='B06',control_ids=['GIR-FD82-A059','GIR-FD82-B013'],paths=[prefix+'creature-rpg/wp24-player-trainers-partners.md'],disposition='NOT_AFFECTED_ONLY_NAMED_UNCHANGED_SELECTION_CLAUSES',reason='WP24§5.4 six requests/Intro/PT41–63 match final WP39§7.5; no owner byte changes. Partner merge behavior retained in WP39; this does not newly approve full WP24 partner/radar scope.'),
 dict(owner='B15',control_ids=['GIR-FD82-B013'],paths=[prefix+'pokemon-rules/wp61-field-passive-effects-and-blackout.md'],disposition='NOT_AFFECTED_ONLY_NAMED_INPUT_TIMING',reason='No fail-return flow, canLose or world passive timing changed. B013 can change actual held-item values after restore, and caller premise is explicitly recorded; world consumer still reads actual current values. No full world package reapproval.')
]
dump('reverse-impact.json',dict(status='AUTHOR_ANALYSIS_NOT_APPROVAL',all62_refreeze='read-coverage.json',required_affected_reviews=reverse,other_readers=other_reader_impacts,existing_cross_owner_residuals=c['existing_cross_owner_residuals'],global_and_domain_residuals=c['global_and_domain_residuals'],B09_B14_serialization=c['B09_B14_operational_serialization'],no_NOT_AFFECTED_whole_batch_claim=True))

judgment='review/wp79-coverage-review-2026-10-03/revision-v6/source-judgments.json'
old_judgment=json.loads((ROOT/judgment).read_text())['rows'][286]
dump('registry-change-proposals.json',dict(status='PROPOSED_ONLY_NOT_APPLIED',sole_public_writer='A-REG',public_paths_modified=[],canonical_required_OPEN=229,canonical_CLOSED=0,new_canonical_ids=0,new_AX=0,contributions=[dict(id=x['id'],primary=x['primary'],suggested_state='AUTHOR_CANDIDATE_PENDING_R_B09_AND_AFFECTED_REVIEWS',final_clauses=x['final_changes'],canonical_state='OPEN',other_contributors_pending=x['other_contributors_pending']) for x in dispositions],coverage_successor=dict(finding_id='GIR-FD82-A059',before=dict(identity=identity(judgment,BASE),row_number_1_based=287,row=old_judgment),proposed_after=dict(path='019_Utilities/003_Utilities_BattleAudio.rb',judgment='B09 candidate concrete request-selection coverage pending independent review/integration',carrier='WP24§5.4 + WP39§7.5; WP15 playback; WP16 transition; WP67-A capture wait',cases=['PT41–63 unchanged','BC-23','BC-24','BC-25','B09-AUDIO-MATRIX','B09-AUDIO-MEMORY-CONSUMERS'],remaining='B17/B21 and full source/registry acceptance gates remain; actual media and dynamic/FromType consumer unknown'),rule='Immutable old row/report is not overwritten; A-REG writes a version-bound successor after required review.'),successor_traceability=dict(normative='normative-identities.json / formal-and-approved-originals.patch',source='source-reading-log.json',controls='contribution-dispositions.json',designs='static-cases.json',review_gates=c['candidate_and_actual_gates']),downstream='B14 remains formally blocked until accepted B09-C and successor72-read/6-write refreeze',counts_rule='24 new catalog IDs are static designs only; zero accepted B09 contributions until required independent candidate/actual gates and parent C. No accepted denominator update by author.'))

dump('candidate-review-request.json',dict(role='R-B09',status='REVIEW_REQUIRED_NOT_DISPATCHED_BY_AUTHOR',binding='Exact ordinary-pushed/readback final freeze-envelope SHA in parent handoff',requested_model='gpt-6.1-sol',requested_reasoning='Ultra',requested_speed='Standard(default)',effective='UNVERIFIED; approved Plan A; no quota/auth/configuration probes',baseline=BASE,previous_scope_checkpoint='de11c8a712b3fbce5c1e11756919536c4739e2a5',contribution_count=20,primary_count=13,formal_count=7,approved_originals=5,required_inputs=['complete fixed B09-downstream-contract.json; all complete effective current roots/qualifications/cases/extensions', 'original-scope-approval.json; all five approved patch hashes/before/after and full30-clause proposal', 'all7 final bodies and2 whole catalogs; normative-identities.json and71-clause ledger', 'all20 contribution dispositions and43 linked catalog design rows +18 supplemental qualified designs', 'all62 read bindings/refreeze, bounded reader clauses and source limits; no hashes treated as semantic coverage', 'separate affected-B04/B07/B08 review requests including untouched owner clauses', 'full unfiltered407536a-to-payload patch and evidence-only payload-to-final envelope diff'],required_actual='Separate R-B09 exact A-REG integration SHA Ultra/Standard, plus separately scoped B04/B07/B08 actual review; full predecessor-to-actual and candidate-to-actual public/management/source deltas.',no_closure=True,author_self_check_is_approval=False))

dump('reader-clause-supplement.json',dict(mode='additional bounded exact owner/caller clauses read for reverse premises',clauses=owners,other_current_reads=[dict(path=prefix+'pokemon-rules/wp48-ability-calculation-modifiers.md',lines=[17,45],role='weight suppression pipeline'),dict(path=prefix+'pokemon-rules/wp50-held-item-triggers-and-consumption.md',lines=[9,42],role='item validity / weight'),dict(path=prefix+'user-interface/wp67-a-battle-interaction-and-presentation.md',lines=[92,105],role='NearAlly affected UI residual'),dict(path=judgment,row=287,role='specific NA successor proposal')],full_other_owner_approval=False))

# Read-only extra reader discovery: exact proposed changes, never applied.
# This is propagation of existing B013, not a new canonical finding or an
# expansion of the five approved originals. Parent/AREG must decide its scope.
import difflib
residuals=[]
for p in ['specs/creature-rpg/wp20-hp-status-moves-helditem.md',prefix+'creature-rpg/wp20-hp-status-moves-helditem.md']:
    before=git('show',BASE+':'+p).decode()
    assert (ROOT/p).read_text()==before,p
    old_lines=before.splitlines(keepends=True)
    edits=[];new_lines=[]
    for n,line in enumerate(old_lines,1):
        if ('战斗结束时' in line and '对仍在队伍中的成员执行' in line):
            after='- 正常战斗终局按玩家侧参与集合及届时同索引还原记录写回持有物；无伙伴实际参战且参与集合与当前玩家队伍同步时，以下逐成员对照成立。伙伴实际参战而满队接收移出旧成员时，身份与记录可错配，完整映射沿 WP38/WP42。\n'
        elif line.startswith('- 特殊路径（静态登记，未穷尽）：'):
            after='- 满队捕获转送旧成员至盒子：先按当前持物送盒，再从玩家当前队伍删除并左移玩家记录；无伙伴实际参战且参与集合同步时，该旧成员退出正常终局还原。伙伴实际参战的旧合并参与集合仍可保留其共享身份，终局按已移位记录写回，故盒中旧成员和留队成员都可能被写错物品。仅登记伙伴而未参与不构成此反例；完整限定输入及反向对照沿 WP38/WP42 的 CP20–22、E14／CX40–42，不以普通永久消耗冒充暂时打落前提。\n'
        else:after=line
        if after!=line:edits.append(dict(finding_id='GIR-FD82-B013',path=p,clause='§6.4',before_lines=[n,n],before_text=line,intended_after_text=after))
        new_lines.append(after)
    assert len(edits)==2,p
    proposed=''.join(new_lines).encode()
    diff=''.join(difflib.unified_diff(old_lines,new_lines,fromfile='a/'+p,tofile='b/'+p)).encode()
    name=('original' if p.startswith('specs/') else 'final')+'-WP20-unapplied.patch'
    (OUT/name).write_bytes(diff)
    blob=hashlib.sha1(b'blob '+str(len(proposed)).encode()+b'\0'+proposed).hexdigest()
    residuals.append(dict(path=p,before=identity(p,BASE),current_unmodified=identity(p),clause_changes=edits,intended_after=dict(git_blob=blob,sha256=sha(proposed),bytes=len(proposed)),full_diff=dict(path=name,sha256=sha(diff),bytes=len(diff)),applied=False,authorized=False))
dump('out-of-scope-reader-proposal.json',dict(status='PENDING_PARENT_SCOPE_DISPOSITION_NOT_APPLIED',id='GIR-FD82-B013',new_root=False,current_B09_allowed_paths_unchanged=True,reason='Extra WP20 reader still unconditionally excludes outgoing boxed party member. Existing B013 extension and qualified CP21/CX40 static evidence contradict it; current B09 contract allocates no WP20 writes. This does not alter the complete approved five-original patches.',requested_scope='Parent decide exact WP20 original/final two-clause synchronization or assign scoped downstream/AREG resolution before global dependency acceptance. No author application before explicit scope authorization.',files=residuals,source_evidence=[dict(commit=REF,path='Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',lines=[171,207],role='partner merged ordered participants; exact proposal source log governs surrounding ranges'),dict(commit=REF,path='Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb',lines=[15,79],role='same-identity box handoff, delete/shift/append'),dict(commit=REF,path='Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb',lines=[477,514],role='normal end loops original participants with shifted records')],static=['CP21','CP22','E14','CX40','CX41','CX42'],review_requirement='Include this exact unchanged extra reader residual in R-B07 affected review and parent scope assessment; do not treat accepted B07 context as approval of these WP20 bytes. No canonical closure.'))
coverage_doc=json.loads((OUT/'read-coverage.json').read_text())
coverage_doc['additional_unplanned_readers']=[dict(path=x['path'],identity=x['current_unmodified'],semantic_scope='§6.4 only, exact before clauses in out-of-scope-reader-proposal.json; not full file') for x in residuals]+[dict(path=prefix+'pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md',identity=identity(prefix+'pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md'),semantic_scope='§2 inputs/§4 timeline/§5 movement; lines20–30/61–90; exact unchanged clauses in affected-B07-review-request.json')]
dump('read-coverage.json',coverage_doc)
for name in ['reverse-impact.json','affected-B07-review-request.json','registry-change-proposals.json','candidate-review-request.json']:
    doc=json.loads((OUT/name).read_text())
    doc['unapplied_extra_reader_scope_proposal']='out-of-scope-reader-proposal.json; exact original/final WP20 before/diff/intended-after, existing B013 propagation, pending parent disposition'
    dump(name,doc)
