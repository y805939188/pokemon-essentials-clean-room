import argparse, collections, hashlib, json, re, subprocess
from pathlib import Path

ap=argparse.ArgumentParser(description='New B16 incremental Git/JSON/byte metadata checks only; no source or behavior execution.')
ap.add_argument('--repo',default='/workspace/pokemon-essentials-clean-room')
ap.add_argument('--reference-git',default='/tmp/b16-reference.git')
ap.add_argument('--scratch-dir',default='/tmp/b16-affected-review-2')
args=ap.parse_args();REPO=args.repo;REF=args.reference_git;OUT=Path(args.scratch_dir);OUT.mkdir(parents=True,exist_ok=True)
OLD='ae223d7bfb9ff6ed8a1ac153debb986115345957'
NEW='356b46b320884e57e71a1cab8413e13594524a7d'
PUB='7585b16a65338392af8ff78e7d8a8cb23cd19901'
BASE='27185563f307e16d2612fa86e83b2c9bd772c79e'
REPORT1='6abb85d39993db446069e35880eb5de3b9295e4d'
REFERENCE='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
P='review/remediation/20261003-prepare/batches/B16/'
CP=P+'candidate-1/complete-after-R-B16-F01-and-C120-1/'
SP=P+'author-draft-1/original-sync-4/'
RP1=P+'affected-candidate-review-1/'
CAT='deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
FORMAL='deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md'
ORIGINAL='specs/ui/wp66-b-storage-and-pokedex-ui.md'

def git(*argv,repo=REPO):return subprocess.check_output(['git',*argv],cwd=repo)
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
cache={};identities={}
def read(commit,path,repo=REPO):
 key=(repo,commit,path)
 if key not in cache:cache[key]=git('show',commit+':'+path,repo=repo)
 return cache[key]
def ident(commit,path,repo=REPO):
 b=read(commit,path,repo)
 return dict(commit=commit,path=path,git_blob=git('rev-parse',commit+':'+path,repo=repo).decode().strip(),sha256=sha(b),bytes=len(b))
def verify(a):
 x=ident(a['commit'],a['path'])
 for k in ('git_blob','sha256','bytes'):
  if k in a:assert x[k]==a[k],(a,k)
 identities[(a['commit'],a['path'])]=x
 return x
def j(commit,path):return json.loads(read(commit,path))
def pointer(v,p):
 for t in p.split('/')[1:]:v=v[int(t)] if isinstance(v,list) else v[t.replace('~1','/').replace('~0','~')]
 return v
def tree(commit):
 d={}
 for r in git('ls-tree','-rz','--full-tree',commit).split(b'\0'):
  if r:
   h,p=r.split(b'\t',1);d[p.decode()]=h.decode().split(' ')
 return d

dispatch=j(PUB,SP+'incremental-review-dispatch.json')
manifest=j(NEW,CP+'manifest.json');author_protection=j(NEW,CP+'protection.json')
dm=j(PUB,SP+'complete-diff-manifest.json')
assert dispatch['OLD']==OLD and dispatch['NEW']==NEW and dispatch['formal_input']==BASE
assert git('rev-parse',NEW+'^{tree}').decode().strip()=='344b606d8368eb09dc9313e09fdda1fa227e6f39'
assert git('rev-parse',OLD+'^{tree}').decode().strip()=='7b3a16f86aea8438eceb007436687b72aced8e74'
assert git('rev-parse',REFERENCE+'^{tree}',repo=REF).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0'
for a in dispatch.values():
 if isinstance(a,dict) and {'commit','path','git_blob','sha256','bytes'} <= a.keys():verify(a)
oldproof=j(REPORT1,RP1+'B01/identity-and-preservation.json')
oldindex=j(REPORT1,RP1+'B01/review-index.json')
oldsource=j(REPORT1,RP1+'B01/source-reading-log.json')
oldcoverage=j(REPORT1,RP1+'B01/qualified-control-coverage.json')
oldproof_binding=ident(REPORT1,RP1+'B01/identity-and-preservation.json')
controls=j(dispatch['whole_original_approved_current_controls']['commit'],dispatch['whole_original_approved_current_controls']['path'])['controls']
effective=j(dispatch['whole_effective_constraints']['commit'],dispatch['whole_effective_constraints']['path'])['full_exact_values']
assert len(controls)==24 and sum(c['primary'] for c in controls)==20 and len(effective)==12
control_checks=[]
for c in controls:
 prior=next(x for x in oldproof['controls'] if x['id']==c['id'])
 assert sha(canonical(c['complete_current_control_fields']))==prior['current_control_sha256']
 assert c['whole_original_object_sha256']==prior['whole_original_object_sha256']
 assert c['whole_acceptance_object_sha256']==prior['whole_acceptance_object_sha256']
 cov=next(x for x in oldcoverage['controls'] if x['id']==c['id'])
 assert cov['complete_current_control_fields']==c['complete_current_control_fields']
 control_checks.append(dict(prior,version_match=True,scope='Unchanged complete original/approved/current qualified control accurately reused; not old PASS automatically carried forward'))
for e in effective:
 assert sha(canonical(e['aggregate']))==e['canonical_json_sha256']
 c=next(c for c in controls if c['id']==e['id'])
 assert c['complete_current_control_fields']['effective_case_constraints']==e['aggregate']
 assert next(x for x in oldproof['effective_case_constraints'] if x['id']==e['id'])['sha256']==e['canonical_json_sha256']

payloads=[]
assert len(manifest['outputs'])==11 and manifest['outputs']==dispatch['current_payload_outputs']
for o in manifest['outputs']:
 verify(o['FIX_BASE_before']);verify(o['reviewed_OLD_before'])
 after=verify(dict(o['after'],commit=NEW,path=o['path']))
 equal=read(OLD,o['path'])==read(NEW,o['path'])
 assert equal==o['unchanged_from_reviewed_OLD']
 payloads.append(dict(path=o['path'],kind=o['kind'],base=o['FIX_BASE_before'],old=o['reviewed_OLD_before'],new=after,byte_equal_OLD=equal))
assert sum(x['byte_equal_OLD'] for x in payloads)==8

streams=[]
for key,begin,fn in [('OLD_to_NEW',OLD,'OLD-to-NEW.diff'),('FIX_BASE_to_NEW',BASE,'FIX_BASE-to-NEW.diff')]:
 full=git('diff','--binary',begin,NEW) # no exclusions/pathspecs
 a=dm[key];assert len(full)==a['bytes'] and sha(full)==a['sha256']
 assert full==read(PUB,a['path'])
 (OUT/fn).write_bytes(full)
 inventory=[]
 for line in git('diff','--name-status','--no-renames',begin,NEW).decode().splitlines():
  status,path=line.split('\t',1);inventory.append(dict(status=status,path=path))
 assert [r['path'] for r in inventory]==a['changed_paths']
 assert len(re.findall(br'^diff --git ',full,re.M))==len(inventory)
 added_json_checks=[]
 for row in inventory:
  if row['status']=='A':
   assert row['path'].startswith(P)
   b=read(NEW,row['path'])
   if row['path'].endswith('.json'):
    obj=json.loads(b);added_json_checks.append(dict(path=row['path'],sha256=sha(b),bytes=len(b),parsed=True,top_level_fields=list(obj) if isinstance(obj,dict) else None))
 streams.append(dict(begin=begin,end=NEW,bytes=len(full),sha256=sha(full),inventory=inventory,
  path_count=len(inventory),publication_copy_exact=True,unfiltered=True,added_JSON_metadata_read=added_json_checks))
ot,nt,bt=tree(OLD),tree(NEW),tree(BASE)
assert not (ot.keys()-nt.keys()) and not (bt.keys()-nt.keys())
changed=[p for p in ot if nt[p]!=ot[p]]
assert changed==[CAT,FORMAL,ORIGINAL] # Git tree lexical order
assert author_protection['OLD_existing_path_count']==len(ot)==36417
assert author_protection['all_other_OLD_existing_paths_preserved']==len(ot)-len(changed)==36414
oldprotected={p:v for p,v in ot.items() if p not in changed}
assert all(nt[p]==v for p,v in oldprotected.items())
permitted={p['path'] for p in payloads}
baseprotected={p:v for p,v in bt.items() if p not in permitted}
assert all(nt[p]==v for p,v in baseprotected.items()) and len(baseprotected)==36339
assert {r['path'] for r in streams[0]['inventory'] if r['status']!='A'}==set(changed)
assert {r['path'] for r in streams[1]['inventory'] if r['status']!='A'}==permitted

# Exact single-line replacements, not an execution of the original patch/program.
line_changes=[]
for path in changed:
 before=read(OLD,path).splitlines(keepends=True);after=read(NEW,path).splitlines(keepends=True)
 assert len(before)==len(after)
 where=[i for i,(b,a) in enumerate(zip(before,after)) if b!=a]
 assert len(where)==1
 i=where[0];line_changes.append(dict(path=path,line=i+1,before=before[i].decode().rstrip('\n'),after=after[i].decode().rstrip('\n')))
oldtext=read(OLD,CAT);newtext=read(NEW,CAT)
oldpart='上限50对照实际20来源30目标50'.encode();newpart='上限50对照实际20来源26目标50'.encode()
assert oldtext.count(oldpart)==1 and oldtext.replace(oldpart,newpart)==newtext
for path in (FORMAL,ORIGINAL):assert next(x for x in line_changes if x['path']==path)['line']==217
fragment=lambda path:read(NEW,path).decode().splitlines()[216].split('另有查看盒子的背景刷新写入：',1)[1]
assert fragment(FORMAL)==fragment(ORIGINAL)

scope=j(dispatch['scope4_receipt']['commit'],dispatch['scope4_receipt']['path'])
assert scope['grant_file_count']==scope['grant_control_count']==scope['grant_replacement_count']==1
grant=scope['granted_files'][0];assert grant['path']==ORIGINAL and grant['qualified_ids']==['GIR-FD82-C120']
for k in ('current_before','before_artifact','whole_combined_patch','complete_proposed_after'):verify(grant[k])
b,a=grant['current_before'],grant['complete_proposed_after']
assert read(OLD,ORIGINAL)==read(b['commit'],b['path'])
assert read(NEW,ORIGINAL)==read(a['commit'],a['path'])
scope3=j(dispatch['scope3_receipt']['commit'],dispatch['scope3_receipt']['path'])
for s in scope3['granted_files']:
 path=s['path'];oldafter=s['complete_proposed_after']
 assert read(OLD,path)==read(oldafter['commit'],oldafter['path'])
 if path!=ORIGINAL:assert read(NEW,path)==read(OLD,path)
patch=read(grant['whole_combined_patch']['commit'],grant['whole_combined_patch']['path']).decode().splitlines()
deletes=[x[1:] for x in patch if x.startswith('-') and not x.startswith('---')]
adds=[x[1:] for x in patch if x.startswith('+') and not x.startswith('+++')]
assert len(deletes)==len(adds)==1
change=next(x for x in line_changes if x['path']==ORIGINAL)
assert deletes==[change['before']] and adds==[change['after']]
assert sum(x.startswith('@@ ') for x in patch)==1

def catalog_rows(data):
 sec='';occ=collections.Counter();res=[]
 for b in data.splitlines(keepends=True):
  s=b.decode()
  if s.startswith('## '):sec=s.rstrip('\r\n')
  m=re.match(r'^\|\s*([A-Za-z][A-Za-z0-9_-]*\d[a-z]?)\s*\|',s)
  if m:code=m[1];occ[(sec,code)]+=1;res.append(((sec,code,occ[(sec,code)]),b))
 return res
br,ors,nr=[catalog_rows(read(c,CAT)) for c in (BASE,OLD,NEW)]
assert len(br)==460 and len(ors)==len(nr)==484
assert [k for k,b in ors]==[k for k,b in nr]
assert [k for k,b in br]==[k for k,b in nr if k in dict(br)]
assert [k[1] for (k,b),(nk,nb) in zip(ors,nr) if b!=nb]==['B16-C003']
edits=[k for k,b in br if dict(nr)[k]!=b];assert len(edits)==9
assert [k[1] for k in edits]==[x['id'] for x in oldproof['catalog']['edits']]
assert all(dict(nr)[k]==dict(ors)[k] for k,b in br)

receipt=oldproof['accepted_receipts']['binding'];verify(receipt)
assert read(NEW,receipt['path'])==read(BASE,receipt['path'])
receipts=j(NEW,receipt['path'])['accepted_contribution_receipts']
assert len(receipts)==240 and sha(canonical(receipts))==oldproof['accepted_receipts']['records_sha256']
owner_inputs=[]
for row in oldproof['owner_input_identities']:
 current=[]
 for a in row['inputs']:
  path=a['before']['path'];assert ident(BASE,path)==a['before']
  current.append(dict(role=a['role'],path=path,base=a['before'],old=ident(OLD,path),new=ident(NEW,path),byte_equal_OLD=read(OLD,path)==read(NEW,path)))
 owner_inputs.append(dict(owner=row['owner'],shared_control_IDs=row['shared_control_IDs'],inputs=current))

trace=j(NEW,manifest['traceability']);assert len(trace['rows'])==24
for i,row in enumerate(trace['rows']):
 a=row['full_qualified_original_approved_current_control'];assert pointer(j(a['commit'],a['path']),a['pointer'])==controls[i]
fc=j(NEW,SP+'finding-completion.json')
assert trace['correction_context']['corrected_catalog_trace']['full_static_row']==next(x for x in line_changes if x['path']==CAT)['after']
assert fc['R-B16-F01']['current_catalog']['row']==next(x for x in line_changes if x['path']==CAT)['after']
for k,path in [('sanitized_clause',FORMAL),('original_clause',ORIGINAL)]:
 assert fc['B16-AFFECTED-C120-1'][k]['text']==next(x for x in line_changes if x['path']==path)['after']
 assert ident(NEW,path)['git_blob']==fc['B16-AFFECTED-C120-1'][k]['after']['git_blob']

fresh=[('Data/Scripts/016_UI/005_UI_Party.rb',1254,1294,'MILKDRINK/SOFTBOILED caller: fixed cost before capped recipient restore'),
 ('Data/Scripts/013_Items/001_Item_Utilities.rb',333,338,'Recipient-only capped write and actual gain return'),
 ('Data/Scripts/016_UI/017_UI_PokemonStorage.rb',378,397,'C120 display-read/legacy/cache/fallback ordering'),
 ('Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',101,106,'Actual availability including negative integer condition')]
source_checks=[]
for path,start,end,purpose in fresh:
 b=read(REFERENCE,path,REF);x=ident(REFERENCE,path,REF)
 span='\n'.join(b.decode().splitlines()[start-1:end])+'\n'
 source_checks.append(dict(x,lines=f'{start}–{end}',range_sha256=sha(span.encode()),purpose=purpose,mode='FRESH_BOUNDED_STATIC_TEXT_ONLY',execution=0))
for a in oldsource['fresh_bounded_source_reads']:
 x=ident(REFERENCE,a['path'],REF)
 assert all(x[k]==a[k] for k in ('git_blob','sha256','bytes'))

result=dict(role='B16_AFFECTED_INCREMENTAL_CANDIDATE_METADATA_ONLY',OLD=OLD,NEW=NEW,NEW_tree='344b606d8368eb09dc9313e09fdda1fa227e6f39',FIX_BASE=BASE,publication=PUB,
 shared_validation_once=True,identity_result='PASS_METADATA_NOT_QUALITY_OR_RUNTIME_PASS',
 entry_bindings=list(identities.values()),dispatch=ident(PUB,SP+'incremental-review-dispatch.json'),prior_shared_proof=oldproof_binding,
 prior_affected_index=ident(REPORT1,RP1+'B01/review-index.json'),source_limits=dispatch['source_limits'],controls=control_checks,
 effective_constraints=[dict(id=x['id'],sha256=x['canonical_json_sha256'],exact_prior_equal=True) for x in effective],
 contribution_count=24,primary_count=20,payloads=payloads,line_changes=line_changes,full_unfiltered_streams=streams,
 protection=dict(OLD_existing_paths=len(ot),changed_existing_paths=changed,other_OLD_paths_mode_type_blob_equal=len(oldprotected),
  OLD_protected_projection_sha256=sha(canonical(oldprotected)),BASE_protected_paths_mode_type_blob_equal=len(baseprotected),
  base_projection_sha256=sha(canonical(baseprotected)),deleted_OLD_or_BASE_paths=0,unchanged_other_payloads=8,
  author_protection_independently_matches=True),
 scope4=dict(binding=dispatch['scope4_receipt'],one_file=ORIGINAL,one_clause='§8.5 item5',
  exact_before=grant['current_before'],exact_patch=grant['whole_combined_patch'],exact_after=grant['complete_proposed_after'],
  actual_NEW_full_after_equal=True,single_line_single_hunk_equal=True,other_four_scope3_original_afters_equal=True,
  application_count='Author records 1; independent bytes prove the exact single replacement, no historical program rerun',quality_permission_only=True),
 catalog=dict(BASE_old_rows=460,OLD_rows=484,NEW_rows=484,OLD_to_NEW_only_edited_row='B16-C003',
  OLD_to_NEW_other_483_rows_equal=True,all_460_old_BASE_rows_identical_to_OLD=True,old_order_multiplicity_equal=True,
  protected_BASE_rows=451,assigned_BASE_edits=9,new_rows_from_BASE=24,executed_rows=0),
 accepted_receipts=dict(binding=receipt,count=240,records_sha256=sha(canonical(receipts)),BASE_NEW_full_bytes_equal=True,
  canonical_OPEN=229,canonical_CLOSED=0,per_batch=dict(sorted(collections.Counter(x['batch'] for x in receipts).items()))),
 owner_input_identities=owner_inputs,source_static_supplement=source_checks,
 prior_source_and_control_provenance='Fixed report1 evidence reused only for unchanged premises/bytes; fresh static milk/fallback checks judge current changes. No old reviewer/author script run.',
 prohibited_execution_count=0,quality_verdict='Separate independent owner reports; author claims and scope permission are not quality PASS')
(OUT/'independent-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(result='PASS',payloads=11,unchanged_payloads=8,existing_line_changes=3,
 OLD_paths=len(ot),protected_OLD_paths=len(oldprotected),protected_BASE_paths=len(baseprotected),controls=24,primary=20,effective=12,receipts=240,
 stream_bytes=[s['bytes'] for s in streams],stream_paths=[s['path_count'] for s in streams],catalog_OTHER_OLD_rows_equal=483)))
