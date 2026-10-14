from pathlib import Path
import json,urllib.request,hashlib,subprocess
P=Path('review/remediation-sixth-20261014-prepare');E=P/'candidates/R6-U01/evidence';T=Path('/tmp/r6-u01-context');C='c0ff33024aea424c68d29f9778fe7c8e807d21e8';R='review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3'
ident=lambda b:{'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
ref=json.loads((T/'historical-u03-projections.json').read_text());known={x['identity']['path']:x['identity'] for n in ref for x in n['exact_required_history_readset']};receipt=[];projection={}
for path,row in known.items():
 out=T/Path(path).name
 if out.exists():b=out.read_bytes()
 else:b=urllib.request.urlopen('https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+C+'/'+path,timeout=30).read();out.write_bytes(b)
 assert all(ident(b)[k]==row[k] for k in ident(b));j=json.loads(b);receipt.append({'commit':C,'path':path,**ident(b),'mode':'100644','type':'blob','scope':'Fixed historical payload validated; semantic scope projected below, not whole-report reading'})
 print(Path(path).name,'keys',list(j.keys()))
 if 'legacy' in path:
  projection['controls']=[x for x in j['controls'] if x.get('id') in ['GIR-FD82-A021','GIR-FD82-A022','GIR-FD82-A026','GIR-FD82-A033','GIR-FD82-A053']]
  projection['contributions']=[x for x in j['contributions'] if x.get('record_key') in ['B05/GIR-FD82-A021','B05/GIR-FD82-A022','B05/GIR-FD82-A026','B06/GIR-FD82-A033','B07/GIR-FD82-A026','B08/GIR-FD82-A053']]
 else:projection['GR4']=[x for x in j['records'] if x.get('id')=='GR4-M04-001']
 for section in projection:
  print(section,[(x.get('id',x.get('record_key')),list(x)[:16],len(json.dumps(x))) for x in projection[section]])
# Store complete qualification projections separately from nested supporting archives.
(T/'historical-qualified-records.json').write_text(json.dumps(projection,ensure_ascii=False,indent=2)+'\n')
close='review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-closure-candidate/closure-candidate.json';b=subprocess.check_output(['git','show','13fddb0a217b36974c75657aa68da0caf104ee48:'+close]);j=json.loads(b)
chosen=[x for x in j['records'] if x.get('id',x.get('finding_id')) in ['GR5-M01-006','GR5-M04-002','GR5-M03-001','GR5-M03-003']]
print('closing selected',[(x.get('id',x.get('finding_id')),list(x),len(json.dumps(x))) for x in chosen]);print('recordfirstkeys',list(j['records'][0]))
(T/'fifth-selected-closure.json').write_text(json.dumps({'records':chosen,'scope_qualification':j['scope_qualification'],'excluded_from_closing':j['excluded_from_closing'],'history_preserved':j['history_preserved'],'execution':j['execution']},ensure_ascii=False,indent=2)+'\n')
receipt.append({'commit':'13fddb0a217b36974c75657aa68da0caf104ee48','path':close,**ident(b),'scope':'Only selected exact records and closure boundary; remaining92 not rereviewed'})
(E/'history-input-identities.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
