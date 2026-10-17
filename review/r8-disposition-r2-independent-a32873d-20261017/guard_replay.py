#!/usr/bin/env python3
"""Replay actual pending-U04 prepare/refusal on the review-owned clean fixture."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;E=OUT/'evidence'
fixture=Path(json.loads((E/'tool-replay-summary.json').read_bytes())['fixture']);src=fixture/'planning/implementation-routing/r8-20261017';script=src/'revisions/r2/tools/backfill-accepted-sources.py'
def hashes():return {n:hashlib.sha256((src/n).read_bytes()).hexdigest()for n in ['routing-manifest.json','section-coverage.json','accepted-source-updates.json']}
initial=hashes();records=[]
for command,exit_code in [('prepare',0),('apply',1)]:
 argv=[sys.executable,str(script),command,'--snapshot','0eee6d141f33758eda34bd8ebad94a3e2b617f5a'];start=datetime.datetime.now(datetime.timezone.utc).isoformat();before=hashes();p=subprocess.run(argv,cwd=fixture,capture_output=True,text=True);after=hashes()
 records.append({'argv':argv,'cwd':str(fixture),'started_utc':start,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'expected_exit_code':exit_code,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'core_hashes_before':before,'core_hashes_after':after})
 assert p.returncode==exit_code and before==after==initial
 if command=='apply':assert 'formal changes lack ACCEPTED receipts'in p.stderr
prepared=json.loads((src/'revisions/r2/tools/prepared-source-backfill.json').read_bytes())
assert len(prepared['unaccepted_changed_formal_paths'])==6 and len(prepared['unresolved_new_headings'])==10 and prepared['current_headings_observed']==2704 and len(prepared['current_locators'])==736
(E/'independent-prepare-apply-refusal.json').write_text(json.dumps({'candidate':'a32873d2860b15d9f5e27727db8f131f4ec433b6','fixture':str(fixture),'tool_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),'commands':records,'core_unchanged':True,'unaccepted_paths':prepared['unaccepted_changed_formal_paths'],'pending_new_headings':prepared['unresolved_new_headings'],'prepared_locators':736,'headings_observed_not_applied':2704,'actual_snapshot_still_908':json.loads((src/'routing-manifest.json').read_bytes())['current_snapshot']['commit'],'future5_and_real_cumulative_full_coverage':'NOT_EXECUTED_AWAITING_U04','qualification':'Exact author code, isolated clone only. Expected refusal proves current U04 gate, not general soundness or future full application acceptance.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'prepare':0,'apply_expected_refusal':1,'core_unchanged':True,'pending_paths':6,'pending_headings':10,'prepared_locators':736}))
