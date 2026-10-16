"""Record only the actual source units read in this context, with original I/O navigation."""
from pathlib import Path
import datetime,hashlib,json
P=Path(__file__).resolve().parent;R=Path('/workspace/pokemon-essentials');RR=P.parent.parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
lib=json.loads((RR/'tasks/coverage_acceptance_incremental/dispatch/kernel_atomic_reception.readset.json').read_text())['all_fixed_R432_F131_identity_library']
ledger=json.loads((P/'reading-ledger.json').read_text())
for path,ranges,full,units,evidence in [
 ('Data/Scripts/017_Minigames/005_Minigame_Lottery.rb',[[1,46]],True,['whole file all46 lines; date seed/reseed and lottery comparison/output'],['actual directtool92823d at tool clock09:50:37; command UTC not captured']),
 ('Data/Scripts/012_Overworld/005_Overworld_Fishing.rb',[[1,110]],True,['whole file all110 lines; begin/end, fishing, wait dots and input/deadline'],['io/time-fishing-complete-actual-clock-consumer.json','actual output b904e6']),
 ('Data/Scripts/018_Alternate battle modes/002_BugContest.rb',[[1,260],[279,360]],False,['BugContestState entire class4–226; TimerDisplay entire class230–259','state getter/inProgress/undecided/decided/startover and complete five event registrations279–359; following battle implementation not read'],['actual complete directtool d65c2e and473722; metadata discovery6613c4; command UTC not captured']),
 ('Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb',[[154,186]],False,['set_visitable_nodes154–164; generate_depth_first_maze166–173; recursively_connect_node175–184 complete'],['io/time-dungeon-complete-maze-random-sampling-methods.json','actual output653740']),
]:
 fixed=next(x for x in lib if x['repo']=='R' and x['path']==path);raw=(R/path).read_bytes()
 assert len(raw)==fixed['bytes'] and hashlib.sha256(raw).hexdigest()==fixed['sha256']
 x=next((x for x in ledger['records'] if x.get('repo')=='R' and x.get('path')==path),None)
 if not x:x={'repo':'R','path':path,'reader':'/root/kernel_atomic_reception'};ledger['records'].append(x)
 x['fixed_identity']=fixed;x['whole_file_read']=full or x.get('status')=='FULL_READ'
 x['status']='FULL_READ' if x['whole_file_read'] else 'PARTIAL_READ_COMPLETE_NAMED_UNITS'
 x['actual_read_ranges']=sorted(set(tuple(a) for a in x.get('actual_read_ranges',[]))|set(tuple(a) for a in ranges))
 x['complete_units']=sorted(set(x.get('complete_units',[])+units));x.setdefault('later_read_evidence',[]).extend(evidence)
ledger['updated_utc']=now
(P/'reading-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
(P/'time-actual-consumer-reading-addendum.v1.json').write_text(json.dumps({'recorded_utc':now,'reader':'/root/kernel_atomic_reception','actual_clock_after_direct_source_read':'2026-10-16 09:56:11 UTC','underlying_command_start_end_utc':'UNVERIFIED_NOT_CAPTURED; no backfill from later actual clock','actual_output_ids':['92823d','b904e6','d65c2e','473722','653740'],'facts':['Fishing timeout is gated by !FISHING_AUTO_HOOK; true removes deadline but still waits for USE/BACK. No new finding or whole-owner-contract adjudication from overview wording.','Contest expiry requires undecided and TIME_ALLOWED>0, compares uptime against captured timer_start; per-frame caller further defers messages/judging while forced route, interpreter or message window.','Contest pbStart stores uptime before party selection/contestant random loop and stats increment; failure keeps prefix. pbStartJudging sets decision1 before judge and transfer.','Contest pbEnd restores otherparty before nickname/store/place/wins and only later clears contest flags, sets lastContest wallclock and map refresh; no ensure/rollback.','Contest held-in-last24h is wallclock, expiration/display is uptime; negative or zero allowed duration prevents expiry (display subscription only suppresses ==0).','Lottery date seed followed by noargument srand does not restore prior global sequence.'],'whole_source_new_credit':['Lottery46','Fishing110'],'partial_only':['BugContest1–260/279–360','Dungeon154–186'],'target_business_execution':'NOT_EXECUTED','new_finding_context_vote_required':0},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':now,'own_nonPBS_FULL':sum(x.get('repo')=='R' and x.get('status')=='FULL_READ' and not x['path'].startswith('PBS/') for x in ledger['records'])}))
