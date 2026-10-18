from pathlib import Path
import json, datetime, subprocess, hashlib
B=Path(__file__).resolve().parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
ledger=json.loads((B/'reading-ledger.json').read_text());e=ledger['snapshot_payloads'][258]
gen=json.loads((B/'world-terrain-reverse-current-columnar-generation.json').read_text())
proof={'schema':'gr8-world-terrain-reverse-current-field-reception/v1','utc':now,
 'auditor':'/root/coverage_acceptance_incremental',
 'source':{k:e[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},
 'complete_current_json_fields_read':True,'view':gen,
 'actual_receipts':[f'world-terrain-reverse-current-{i:02d}.receipt.json' for i in range(1,7)],
 'continuous_view_lines':[[1,400],[401,800],[801,1200],[1201,1600],[1601,2000],[2001,2329]],
 'current_subassertion_fields':265,
 'ledger_qualification':'Allterrainreverse complete clauseobjects265assertionfields read;18terrainroles/allpassabilityreceivers/motion/vehicles/callers/defaults/prefix fields. Genericpremise/status/sourceID notindependentwhole source/formal/consumerproof.',
 'bounded_qualifications':[
 'All18terrain roles read;Mappriority0tileevent exception beforeplayer/nonplayerterrain;characterbothend/collision/playerboundarybeforedebug;followeractual vsstrict preserveexactreceiver.',
 'Cardinalencounterflag beforepermission,ledge attemptendsbothresults;directzerojump bypassesflag/landing butgeneralstep;diagonalprepermissionfacing/fixedLorder/noordinarydistance;zerobumpcreation vsqualifiedcompletion/consumerfailures separate.',
 'Running surf/dive/bike shoesexceptions/walkonly/walkorrunonly;forcedroute vsice/waterfall automove;eventoriginalanchor/rangefilterleft-right-down-up/oneuniformdraw/no collisionprecheck/retry/UDLRdefaults allread.',
 'Surfprecommit/count/basebeforejump/norollback;qualifiedstepmap/player/base/endingcleanup;201keep-water/defaultclearwater neithercleartemporaries;waterfallthroughcleanupdistinctice. Host/runtime results separate.',
 'WORLD003requestonly !moving not !jumping;newUSE/ACTION/SPECIAL/F9 firstdetectedbranch andexistingmenu/debug/shortcut/interactdifferentgates;routeWAITpossible;earlierCutSceneSPECIALseparate. NoentireUIapproval.',
 'All source/premise/status/clauses/foreignfield/defaultqualifications actually read;265manualprovideratoms notfinaluniqueglobaldenominator. No newfinding/vote/sourceorformal全文credit/wholefilePASS.'
 ],
 'transport_failure':{'cell':'734','failure':'CreateProcess Rejected: Failed to create unified exec process: exec-server transport disconnected',
 'original_failure_utc':'UNVERIFIED_NO_EXACT_CLOCK_CAPTURE','underlying_process_created':'NO_CONFIRMED_PROCESS;toolrejectedcreation',
 'underlying_exit':None,'safe_recovery':'pwdexit0;read-onlycheckproofabsentandprogress/ledger247/42confirmed before this new recording process.'},
 'source_full_increment':0,'formal_full_increment':0,'wholefile_semantic_increment':0,
 'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
name='world-terrain-complete-current-field-reception.json'
assert not (B/name).exists()
(B/name).write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
a=['python',str(B/'record_current_field_reception.py'),'258',name,'world_terrain_complete_current_field_reception']
s=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(a,capture_output=True);t=datetime.datetime.now(datetime.timezone.utc).isoformat()
(B/'world-terrain-reception-record.stdout.txt').write_bytes(r.stdout)
(B/'world-terrain-reception-record.stderr.txt').write_bytes(r.stderr)
(B/'world-terrain-reception-record-execution.json').write_text(json.dumps({'argv':a,'start_utc':s,'end_utc':t,'exit':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr).hexdigest(),'business':'NOT_EXECUTED'},indent=2)+'\n')
print(r.stdout.decode());print(r.stderr.decode());print('EXIT',r.returncode)
if r.returncode==0:
 with (B/'review.md').open('a') as f:f.write('\n\n### '+now+'：地形/移动/载具逆向当前字段全接收\n\n原258/150204B/2c8ec8…全2329行视图6连续窗实际全读，265子断言和原source/premise/status字段全接收；18地形/各receiver/运动开始完成/载具及请求门、外域OPEN保留。首次记录调用因exec-server transport disconnected在CreateProcess被拒，未确认进程/无底层exit，核proof不存在及旧247/42后另受控记录。当前248/41、未收106120006B；Rfull1/Ffull0/wholefilesemantic0不变。业务NOT_EXECUTED，UPDATE_NOT_STARTED。\n')
