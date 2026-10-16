from pathlib import Path
import json,hashlib,subprocess,datetime
o=Path(__file__).resolve().parent;ident=json.loads((o/'identities.json').read_text());primary={str(Path(x['repo'])/x['path']) for x in ident['files']}
rows={}
for p in sorted((o/'io').glob('*.json')):
 r=json.loads(p.read_text());path=r.get('path')
 if not path or path in primary:continue
 if path not in rows:rows[path]={'path':path,'io_records':[],'successful_intervals':[],'failed_reads':[]}
 x=rows[path];x['io_records'].append('io/'+p.name)
 if r['exit_code']==0:x['successful_intervals'].append([r['start_line'],r['end_line']])
 else:x['failed_reads'].append({'io':'io/'+p.name,'exit_code':r['exit_code'],'stderr':r['stderr'],'start_utc':r['start_utc'],'end_utc':r['end_utc']})
for path,x in rows.items():
 pp=Path(path)
 if not pp.exists():x['status']='FAILED_FILENAME_READ_PRESERVED_NO_SOURCE_CREDIT';continue
 raw=pp.read_bytes();x.update({'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'lines':len(raw.decode().splitlines())});merged=[]
 for a,b in sorted(x['successful_intervals']):
  if merged and a<=merged[-1][1]+1:merged[-1][1]=max(b,merged[-1][1])
  else:merged.append([a,b])
 x['read_intervals']=merged;x['read_lines']=sum(b-a+1 for a,b in merged);x['status']='FULL_SUPPLEMENTARY_FILE_ACTUALLY_READ' if x['read_lines']==x['lines'] else 'PARTIAL_FILE_ACTUAL_COMPLETE_RELATED_UNITS_READ';x['qualification']='Only named finite structures/facts in interfaces.json received. Full code file reading alone does not accept every external domain.'
 repo='/workspace/pokemon-essentials' if path.startswith('/workspace/pokemon-essentials/') else '/workspace/pokemon-essentials-clean-room'
 commit=ident['R_commit'] if repo.endswith('/pokemon-essentials') else ident['B8_commit'];rel=str(pp.relative_to(repo));r=subprocess.run(['git','-C',repo,'ls-tree',commit,'--',rel],capture_output=True,text=True);record=r.stdout.strip()
 x.update({'repo':repo,'commit':commit,'relative_path':rel,'tree':ident['R_tree'] if repo.endswith('/pokemon-essentials') else ident['B8_workspace_tree'],'git_ls_tree_stdout':r.stdout,'git_ls_tree_stderr':r.stderr,'git_ls_tree_exit_code':r.returncode})
 blob=record.split()[2] if record else None;x['git_blob']=blob
 calc=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest();x['actual_blob']=calc;x['identity_matches_frozen']=blob==calc
payload={'schema':'gr8-com-ai-supplementary-reading/v1','reviewer':'/root/com_ai','updated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'records':list(rows.values()),'qualification':'Supplementary finite interfaces only; not added to20R9formal primary denominator. Each actual text interval has originalstdout/stderr/exit/UTC inio. Wrongfilename failures do not grant credit.','business_execution':'NOT_EXECUTED'}
(o/'supplementary-read-ledger.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'supplementary_paths':len(rows),'existing_paths':sum(Path(p).exists() for p in rows),'identity_conflicts':[x['path'] for x in rows.values() if x.get('identity_matches_frozen') is False]}))
