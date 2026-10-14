from pathlib import Path
import json,datetime,hashlib,collections
out=Path('review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-O');base=out.parent/'R6-F';now=datetime.datetime.now(datetime.timezone.utc).isoformat();rows=[json.loads(x) for x in (out/'reverse-matrix.jsonl').read_text().splitlines()]
fm=json.loads((base/'reverse-matrix.json').read_text());saf=json.loads((base/'safari/reverse-matrix.json').read_text())['rows'];sfacts={x['unit_id']:x for x in json.loads((base/'safari/forward-matrix.json').read_text())['units']};rootfacts={}
for x in json.loads((base/'forward-matrix.json').read_text()):rootfacts.setdefault(x.get('fact_id'),x)
receipts=[]
for r in rows:
 p=r['formal'];a,z=r['lines'];c=None;source_rows=[];fact_ids=[];clear=None
 if p.endswith('creature-rpg-wp35-36-57-64-68.md') and 74<=a<=90:
  c=next((x for x in fm if x.get('formal_path')==p and x.get('start_line')==a),None)
  if c:source_rows=c['source_locations'];fact_ids=c['human_fact_ids'];clear='C Factory';fact_text=[rootfacts[x]['fact'] if x in rootfacts else 'actual complete source range binding (F-C04 second half independently read by O)' for x in fact_ids]
 if p.endswith('pokemon-rules-wp53-60-61-62-69-70.md') and 11<=a<=45:
  c=next((x for x in saf if x.get('formal_path')==p and x.get('line')==a),None)
  if c:source_rows=c['sources'];fact_ids=c['source_units'];clear='C Safari/contest';fact_text=[sfacts[x]['fact'] for x in fact_ids if x in sfacts]
 if not c:continue
 receipt={'block':r['id'],'formal':p,'lines':[a,z],'primary':'R6-F current real independent reviewer','primary_source_full_read_credit':'R6-F only; O no wholefile credit','primary_row':c,'fact_ids':fact_ids,'facts':fact_text,'new_O_consumer_assessment':'Own whole catalog alreadyread; actual currentF facts considered with its explicit input/partialcancel/host boundaries. F final findings still root classified.'}
 receipts.append(receipt);r.setdefault('interface_bindings',[]).append('R6-F-current-'+r['id'])
 for x in source_rows:
  path=x['path'];path=path if path.startswith('reference/') else 'reference/pokemon-essentials/'+path
  r['evidence'].append({'path':path,'lines':[x['start_line'],x['end_line']],'fact':'Current F '+','.join(fact_ids)+': '+'; '.join(fact_text),'grade':'SOURCE_STATIC_IMPORTED_CURRENT_COMPLETED_PRIMARY','owner':'R6-F actual current report/matrices, not ownfullread'})
 r['pending_bindings']=[x for x in r.get('pending_bindings',[]) if x!=clear]
 if r['status'] in ['LOCAL_FACTS_CHECKED_FOREIGN_CONSUMER_BINDING_PENDING','FOREIGN_PRIMARY_PENDING_CURRENT_BINDING'] and not r['pending_bindings']:r['status']='CURRENT_PRIMARY_STATIC_BINDING_RECEIVED'
 if p.endswith('pokemon-rules-wp53-60-61-62-69-70.md') and a==11:
  r['status']='CONTRADICTION_PROPOSED_EXTERNAL_ROOT_DECISION';r['proposal_ids'].append('GR6-F-009 exact in-mode unsavableSF01claim; final root-I pending')
 if p.endswith('pokemon-rules-wp53-60-61-62-69-70.md') and a==40:
  r['proposal_ids'].append('GR6-F-009 newQuitGame save contrast needed; existing dedicatedSave hidden/afternormalEndsave/no migration remain correct')
(out/'received-F-interface.json').write_text(json.dumps({'at':now,'primary_status':json.loads((base/'task-status.json').read_text()),'receipt_count':len(receipts),'receipts':receipts,'artifacts':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [base/'report.md',base/'task-status.json',base/'forward-matrix.json',base/'reverse-matrix.json',base/'safari/forward-matrix.json',base/'safari/reverse-matrix.json']],'credit':'This is crossdomain current evidence receipt; O ownreadingledger does not claim primary files fullread.'},ensure_ascii=False,indent=2)+'\n')
(out/'reverse-matrix.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
with (out/'command-log.jsonl').open('a') as log:log.write(json.dumps({'at':now,'command':'Read current R6-F report/status/crossinterfaces + compact everyFC/SF primaryfact and reverse binding; import-F-interface.py','result':'52 current block bindings consumed; firstwide output truncated and compactrecovered; inline navigation SyntaxErrorand74 didnotread/modifythenrepaired. No ownwholefilecredit, no imported executioncredit.'},ensure_ascii=False)+'\n')
print(json.dumps({'received':len(receipts),'statuses':dict(collections.Counter(r['status'] for r in rows))},ensure_ascii=False))
