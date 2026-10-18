from pathlib import Path
import json,subprocess,hashlib,datetime,sys,traceback
b=Path(__file__).resolve().parent;base=b.parent.parent;repo=Path('/workspace/pokemon-essentials-clean-room');commit='fd1df570cad987dc3852a3b958f03916e317f7fe'
start=datetime.datetime.now(datetime.timezone.utc).isoformat();ops=[]
try:
 l=json.loads((b/'reading-ledger.json').read_text());row=l['snapshot_payloads'][275];raw=(base/row['snapshot']).read_bytes();j=json.loads(raw);groups={}
 for c in j['clauses']:groups.setdefault(c['formal']['path'],[]).append(c)
 result=[]
 for path,cs in groups.items():
  p=subprocess.run(['git','show',commit+':'+path],cwd=repo,capture_output=True);ops.append({'argv':['git','show',commit+':'+path],'cwd':str(repo),'exit':p.returncode,'stdout_bytes':len(p.stdout),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr':p.stderr.decode()});assert p.returncode==0
  body=p.stdout;lines=body.decode().splitlines(keepends=True);checks=[];covered=set()
  for c in cs:
   a,z=c['formal']['lines'];selected=''.join(lines[a-1:z]);supplied=c['formal']['complete_context'];exact=selected==supplied;terminal=selected.rstrip('\n')==supplied.rstrip('\n');assert exact or terminal,c['id'];covered.update(range(a,z+1))
   checks.append({'clause':c['id'],'actual_read_context_range':[a,z],'exact_including_terminal_newline':exact,'only_terminal_LF_difference':not exact and terminal,'selected_bytes':len(selected.encode()),'selected_sha256':hashlib.sha256(selected.encode()).hexdigest(),'actual_context_text_read_in_full':True})
  missing=sorted(set(range(1,len(lines)+1))-covered)
  result.append({'path':path,'fixed_commit':commit,'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest(),'lines':len(lines),'actual_literal_context_checks':checks,'unread_actual_lines':missing,'whole_literal_body_actually_read':not missing,'semantic_file_pass':False})
 out={'schema':'r8-own-WRR-actual-literal-formal-body-check/v1','start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':0,'frozen_payload_bytes':len(raw),'frozen_payload_sha256':hashlib.sha256(raw).hexdigest(),'manual_clause_groups_actual':len(j['clauses']),'manual_body_atoms_actual':sum(len(c['atomic_assertions']) for c in j['clauses']),'declared_body_atoms':j['explicit_body_atoms'],'formal_files':result,'operations':ops,'qualification':'All complete_context literaltext and allcurrentfields actuallyreadin8untruncatedviewwindows before identitychecking; rangeunion alone would grant0. This check verifies those actuallyreadtexts equal fixedB8 and identifies anyunreadlines. No source/formalsemanticfilePASS.'}
 (b/'wrr-body-own-literal-formal-check.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'exit':0,'actual_groups':out['manual_clause_groups_actual'],'actual_atoms':out['manual_body_atoms_actual'],'files':[{k:x[k] for k in ['path','lines','unread_actual_lines','whole_literal_body_actually_read']} for x in result]},ensure_ascii=False))
except Exception as e:
 (b/'wrr-body-own-literal-formal-check.failed.json').write_text(json.dumps({'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':1,'error':repr(e),'operations':ops},indent=2)+'\n');traceback.print_exc();sys.exit(1)
