"""Metadata/integrity checks only. Does not execute reference, game or a model."""
from pathlib import Path
import datetime, hashlib, json, subprocess
T=Path(__file__).resolve().parent; RR=T.parent.parent
R=Path('/workspace/pokemon-essentials'); C=Path('/workspace/pokemon-essentials-clean-room')
RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'; BC='fd1df570cad987dc3852a3b958f03916e317f7fe'
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return json.loads((T/p).read_text())
def write(p,x):(T/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(b):return hashlib.sha256(b).hexdigest()
errors=[];checks=[]
jsonpaths=[p for p in T.rglob('*.json') if p.name!='delivery-manifest.current.json']
for p in jsonpaths:
 try:json.loads(p.read_text())
 except Exception as e:errors.append({'path':str(p),'error':str(e)})
ident=read('identities.json')
for row in ident['payloads']:
 p=Path(row['repo'])/row['path'];b=p.read_bytes()
 if len(b)!=row['bytes'] or sha(b)!=row['sha256']:errors.append({'initial_identity':str(p),'issue':'byte/SHA mismatch'})
 repo=R if str(p).startswith(str(R)+'/') else C;commit=RC if repo==R else BC
 proc=subprocess.run(['git','cat-file','blob',f'{commit}:{p.relative_to(repo)}'],cwd=repo,capture_output=True)
 if proc.returncode or proc.stdout!=b:errors.append({'frozen_identity':str(p),'exit':proc.returncode,'issue':'fixed blob not exact'})
ledger=read('continuation-reading-ledger.current.json')
for rel in ledger['new_own_complete_R_files']:
 p=R/rel;b=p.read_bytes();proc=subprocess.run(['git','cat-file','blob',f'{RC}:{rel}'],cwd=R,capture_output=True)
 if proc.returncode or proc.stdout!=b:errors.append({'newR':rel,'issue':'fixed blob not exact','exit':proc.returncode})
 rows=[x for x in ledger['read_identity_groups'] if x['identity']['path']==str(p) and x['identity']['sha256']==sha(b)]
 if len(rows)!=1 or not rows[0]['display_full_for_exact_bytes']:errors.append({'newR':rel,'issue':'missing exact full display'})
for fact in read('dependency-semantic-facts.json')['facts']:
 p=R/fact['source']
 if not p.exists():errors.append({'fact':fact['id'],'issue':'nonexistent source'})
 elif not(1<=fact['lines'][0]<=fact['lines'][1]<=len(p.read_text(encoding='utf-8-sig').splitlines())):errors.append({'fact':fact['id'],'issue':'invalid source range'})
current=read('necessary-reception.current.json')
for row in current['complete_operative_artifact_receptions']:
 p=Path(row['path']);p=p if p.is_absolute() else RR/p;b=p.read_bytes()
 if len(b)!=row['bytes'] or sha(b)!=row['sha256']:errors.append({'received':str(p),'issue':'operative changed since actual reception'})
cor=read('final-evidence-corrections.current.json')
for x in cor['complete_source_units']:
 p=Path(x['identity']['path']);p=p if p.is_absolute() else RR/p
 a,b=x['complete_unit_range'];actual=''.join(p.read_text(encoding='utf-8-sig').splitlines(keepends=True)[a-1:b])
 if actual!=x['complete_text']:errors.append({'correction_unit':x['id'],'issue':'source text differs'})
for x in cor['actual_complete_mandatory_companions']:
 p=Path(x['path']);p=p if p.is_absolute() else RR/p;b=p.read_bytes()
 if len(b)!=x['bytes'] or sha(b)!=x['sha256']:errors.append({'mandatory':str(p),'issue':'byte identity differs'})
interfaces=read('interfaces.json');remaining=read('remaining.json');prior=read('prior-delivery.v1.json')
assert len(interfaces['interfaces'])==20 and interfaces['finite_accepted']==20 and interfaces['open_actual_receipt']==0
assert prior['complete_prior_objects']['interfaces.json']['finite_accepted']==15
assert prior['complete_prior_objects']['interfaces.json']['open_actual_receipt']==5
ids={x['id'] for x in current['manual_finite_units']}
for x in current['former_five_interfaces']:
 for i in x['units']:
  if i not in ids:errors.append({'interface':x['id'],'unresolved_finite_unit':i})
assert len(current['former_five_interfaces'])==5
assert not remaining['necessary_available_unread'] and not remaining['necessary_consumer_unreceived']
assert len(read('dependency-semantic-facts.json')['facts'])==42
assert len(read('forward-mapping.json')['facts'])==50
assert len(read('reverse-mapping.json')['groups'])==47
assert len(read('vector-mapping.json')['vectors'])==125
assert read('progress.json')['initial_dependency_full_read']==36
assert read('progress.json')['initial_dependency_byte_associated']==1
head=subprocess.run(['git','rev-parse','HEAD'],cwd=R,capture_output=True,text=True)
formal=subprocess.run(['git','rev-parse',f'{BC}:deliverables/final-specification-set'],cwd=C,capture_output=True,text=True)
validation={'schema':'gr8-creb-current-static-integrity-validation/v1','utc':utc,'metadata_only':True,
 'JSON_documents_parsed':len(jsonpaths),'initial_payloads_fixed_blob_checked':len(ident['payloads']),
 'new_same_context_full_R_fixed_blob_and_displays_checked':len(ledger['new_own_complete_R_files']),
 'complete_operative_receipt_bindings_checked':len(current['complete_operative_artifact_receptions']),
 'complete_correction_source_units_checked':len(cor['complete_source_units']),
 'original_fact_group_vector_denominators':[50,42,47,125],
 'original_interface_snapshot':[15,5],'current_necessary_interfaces':[20,0],
 'reference_head':head.stdout.strip(),'reference_head_exit':head.returncode,
 'fixed_formal_tree':formal.stdout.strip(),'fixed_formal_tree_exit':formal.returncode,
 'errors':errors,'result':'PASS_METADATA_IDENTITY_ONLY' if not errors else 'FAIL_METADATA',
 'semantic_credit':'No semantic credit from this script, counts, ranges, parsing, hashes or byte equality. Manually authored finite conclusions are separate.',
 'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','new_contexts':0,'new_votes':0}
write('validation.current.json',validation)
assert not errors,errors
files=[]
for p in sorted(T.rglob('*')):
 if not p.is_file() or p.name=='delivery-manifest.current.json':continue
 b=p.read_bytes();files.append({'path':str(p.relative_to(T)),'bytes':len(b),'sha256':sha(b),'mode':oct(p.stat().st_mode&0o777)})
write('delivery-manifest.current.json',{'schema':'gr8-creb-current-exact-delivery-manifest/v1','utc':utc,
 'root':str(T),'files':files,'file_count':len(files),'total_bytes':sum(x['bytes'] for x in files),
 'exclusions':['delivery-manifest.current.json (self-binding impossible; parent receives its bytes/SHA separately)'],
 'required_current':['review.md','progress.json','identities.json','reading-ledger.json','forward-mapping.json','reverse-mapping.json','interfaces.json','proposals.json','remaining.json','necessary-reception.current.json','final-evidence-corrections.current.json','continuation-reading-ledger.current.json','validation.current.json'],
 'identity_not_semantic_credit':True,'all_business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'})
manifest=(T/'delivery-manifest.current.json').read_bytes()
print(json.dumps({'utc':utc,'errors':len(errors),'files':len(files),'bytes':sum(x['bytes'] for x in files),
 'manifest_bytes':len(manifest),'manifest_sha256':sha(manifest),'validation_exit':0,'business':'NOT_EXECUTED'}))
