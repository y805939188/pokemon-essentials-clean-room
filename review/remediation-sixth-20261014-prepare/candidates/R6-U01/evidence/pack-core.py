from pathlib import Path
import json,hashlib,datetime,subprocess,shutil
P=Path('review/remediation-sixth-20261014-prepare');B=P/'candidates/R6-U01';E=B/'evidence';now=datetime.datetime.now(datetime.timezone.utc).isoformat()
ident=lambda b:{'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
rows=[json.loads(x) for x in (E/'commands.jsonl').read_text().splitlines()];logs=E/'logs';logs.mkdir(exist_ok=True)
for n,r in enumerate(rows,1):
 for kind in ['stdout','stderr']:
  old=Path(r[kind+'_path']);dst=logs/f'{n:04d}.{kind}';dst.write_bytes(old.read_bytes());assert ident(dst.read_bytes())==r[kind+'_identity'];r[kind+'_scratch_path']=str(old);r[kind+'_path']=str(dst)
(E/'commands.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
patch=subprocess.check_output(['git','diff','469a268b92daed7b4d28d7fd0da75520cbb7228f','--',str(B/'mirror')]);(E/'integration-deltas.patch').write_bytes(patch)
protect=subprocess.check_output(['git','diff','--name-only','469a268b92daed7b4d28d7fd0da75520cbb7228f']).decode().splitlines();assert all(x.startswith(str(B)+'/') for x in protect)
refs={}
for ref in ['refs/heads/main','refs/tags/delivery/fifth-round-closed-final-20261014']:
 r=subprocess.run(['git','rev-parse','--verify',ref],capture_output=True,text=True);refs[ref]={'present':r.returncode==0,'value':r.stdout.strip() if r.returncode==0 else None}
(E/'freeze-receipt.json').write_text(json.dumps({'utc':now,'candidate_state':'AUTHOR_COMPLETE_STATIC_CANDIDATE_READY','branch':subprocess.check_output(['git','branch','--show-current']).decode().strip(),'starting_prepare':'469a268b92daed7b4d28d7fd0da75520cbb7228f','core_commit':'Bound externally after actual commit; no self identity claim','protected_ref_snapshot':refs,'source_modification':False,'actual_formal_diff':subprocess.check_output(['git','diff','--name-only','8ea169fbd0f33f378b5d732fd6bea59e854e04a6','--','deliverables/final-specification-set']).decode().splitlines(),'changed_mirror_paths':protect,'logs':'All available instrumented actual stdout/stderr archived verbatim; early/root and missing-ruby-wrapper UTC not retroactively reconstructed.','independent_candidate_PASS':'PENDING','integrated_PASS':'PENDING','formal_acceptance':'NOT_GRANTED','CLOSED':'NOT_REGISTERED'},ensure_ascii=False,indent=2)+'\n')
items=[]
for p in sorted(B.rglob('*')):
 if p.is_file() and p.name!='core-manifest.json':items.append({'path':str(p),'mode':'100644','type':'blob',**ident(p.read_bytes())})
(E/'core-manifest.json').write_text(json.dumps({'schema':'R6-U01-author-finite-core-v1','utc':now,'excluded_self':[str(E/'core-manifest.json')],'items':items,'whole_tree':'Bound externally to actual core commit/tree; manifest does not recursively hash itself.','candidate_identity_scope':'Seven corrected formal mirrors plus two unchanged baseline mirrors; evidence covers only GR6-K-001/002/003.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'packaged_items_excluding_manifest':len(items),'total_bytes':sum(x['bytes'] for x in items),'instrumented_command_receipts':len(rows),'changed_mirrors':len(protect),'protected_refs':refs},ensure_ascii=False))
