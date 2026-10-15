"""Recover complete public shell-result objects from this task only.

No reasoning/messages/account metadata are selected. Truncated JSON is retained
as a named original logging limitation, never reconstructed or executed.
"""
import datetime
import hashlib
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
LOG=Path('/Users/dingshinn/.codex/sessions/2026/10/14/rollout-2026-10-14T22-32-09-01a13d67-1bcb-72f2-8f3e-fcada717c8d4.jsonl')
raw=LOG.read_bytes(); calls={}; records=[]; unmatched=[]; decoder=json.JSONDecoder()
for line in raw.splitlines():
    try: v=json.loads(line)
    except ValueError: continue
    p=v.get('payload',{})
    if v.get('type')!='response_item': continue
    if p.get('type')=='custom_tool_call' and p.get('name') in ('exec','wait'):
        calls[p['call_id']]={'call_id':p['call_id'],'tool_call_utc':v.get('timestamp'),
                             'tool_name':p['name'],'input':p.get('input')}
    if p.get('type')!='custom_tool_call_output' or p.get('call_id') not in calls: continue
    results=[]; incomplete=0
    value=p.get('output'); texts=[x.get('text','') for x in value if isinstance(x,dict)] if isinstance(value,list) else [str(value)]
    for text in texts:
        for match in re.finditer(r'\{"chunk_id"\s*:',text):
            try: obj,end=decoder.raw_decode(text,match.start())
            except ValueError: incomplete+=1; continue
            if isinstance(obj,dict) and 'wall_time_seconds' in obj and ('exit_code' in obj or 'session_id' in obj):
                results.append(obj)
    if results:
        records.append({**calls[p['call_id']],'tool_output_utc':v.get('timestamp'),
                        'execution_results':results,'incomplete_result_objects':incomplete})
    elif incomplete:
        unmatched.append({'call_id':p['call_id'],'tool_output_utc':v.get('timestamp'),
                          'incomplete_result_objects':incomplete,'qualification':'Original tool JSON truncated; no synthetic reconstruction.'})
out={'schema':'r7.platform-command-recovery.final-prefix.v1','source_log':str(LOG),
     'read_prefix_bytes':len(raw),'prefix_sha256':hashlib.sha256(raw).hexdigest(),
     'recovered_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'records':records,'incomplete_original_results':unmatched,
     'scope':'Only complete public shell result objects in this task log prefix; no private reasoning, unrelated app outputs, user/account/auth/quota metadata. Exact underlying process UTC/separate streams absent in originals remain unknown. Later publication commands have separate new actual receipts.'}
path=ROOT/'execution/root-platform-command-recovery.final-prefix.json'
if path.exists(): raise FileExistsError('final prefix recovery must not overwrite')
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(path),'complete_command_records':len(records),'incomplete_originals':len(unmatched)}))
