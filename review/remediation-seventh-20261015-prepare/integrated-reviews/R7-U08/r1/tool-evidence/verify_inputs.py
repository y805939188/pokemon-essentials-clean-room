"""Identity, scope and document transport verification only; no behavior execution."""
import json,hashlib,subprocess,os,datetime
from pathlib import Path
ROOT=Path('/workspace/r7-ir-R7-U08');OUT=Path(__file__).parent
B='e646432c644dec04d306842cc5a559a29c718fbc';MI='45c80832a41c1b56dcd7e9d93497758cbb7721de';FI='13d76ba61838b13925ba9d41f58a6b047564d926';R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def git(*args,repo=None,missing=False):
 p=subprocess.run(['git',*(['-C',str(repo)] if repo else []),*args],capture_output=True)
 if p.returncode and not missing:raise RuntimeError(p.stderr.decode())
 return p.stdout
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def match(b,e):
 i=identity(b)
 for k in ['bytes','sha256','git_blob','git_blob_content_id']:
  if k in e:assert i['git_blob' if k=='git_blob_content_id' else k]==e[k],(k,e,i)
 return i
def show(c,p):return git('show',f'{c}:{p}')
def load(p):return json.loads(p.read_text())
checks={'schema':'r7.u08.independent-byte-scope-verification.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool_pid':os.getpid(),'semantic_PASS_from_tool':False}
checks['git_trees']={c:git('rev-parse',c+'^{tree}').decode().strip() for c in [B,MI,FI,'c64774c60d91e522cb515ef71e3e9d4ea6b4712c','d6e07340aa14eb8b45728020cad018a22d7559b2','d86d1db844c4f8ad0ed92b6a811b971e5057c967','aa369555b0e8b6c8b077f964b54ed63d3b924f26','84e2cca132ada38405657f19cbbd3d6891d4794f','44276c5ae69ef0970a98464a5a9e6ff7eb1c1f1c']}
assert checks['git_trees'][MI]=='6480ffe3df49bd9776c719f3c9be1c13618fdb0a'
assert checks['git_trees'][FI]=='6747a584b91c86acd4771c1a6dee93260602106f'
checks['reference_tree']=git('rev-parse',R+'^{tree}',repo=ROOT/'reference-meta.git').decode().strip();assert checks['reference_tree']=='7589c800b61ba13a13040ed0d686979b80a84fd0'
checks['plan_files']=[]
for name,dest in [('original','original'),('actual','actual-input')]:
 plan=ROOT/(name+'-plans')/'R7-U08.json';j=load(plan);rows=[]
 for row in j['artifacts']+j['evidence']+j['fixed_read_inputs']:
  b=(ROOT/dest/row['local_path']).read_bytes();i=match(b,row)
  if row in j['artifacts'] or row in j['fixed_read_inputs']:
   repo=ROOT/'reference-meta.git' if row['repository']=='Maruno17/pokemon-essentials' else None
   entry=git('ls-tree',row['commit'],'--',row['path'],repo=repo).decode().strip().split()
   assert entry[0:2]==['100644','blob'] and entry[2]==i['git_blob'],(row['path'],entry)
  rows.append({'local_path':row['local_path'],'commit':row['commit'],'repository':row['repository'],'remote_path':row['path'],**i,'result':'MATCH'})
 checks['plan_files'].append({'plan':str(plan),'plan_identity':identity(plan.read_bytes()),'count':len(rows),'bytes':sum(x['bytes'] for x in rows),'files':rows})
assert checks['plan_files'][0]['count']==39 and checks['plan_files'][1]['count']==204
p='review/remediation-seventh-20261015-prepare/integration/wave2/v1/integrated-input.json';frozen=show(FI,p);assert frozen==(ROOT/'bootstrap/integrated-input.json').read_bytes();fi=json.loads(frozen)
checks['FI_identity']=identity(frozen)
formal=[]
for row in fi['all_formal_file_identities']:
 p=row['path'];cur=show(MI,p);old=show(B,p);i=match(cur,row);match(old,row['base_B_identity']);assert (cur!=old)==row['changed_against_B'];formal.append({'path':p,**i,'changed_against_B':cur!=old})
assert len(formal)==131 and sum(x['changed_against_B'] for x in formal)==26
checks['formal_131']=formal;checks['formal_counts']={'all':131,'changed':26,'unchanged':105}
checks['formal_subtrees']={c:git('rev-parse',c+':deliverables/final-specification-set').decode().strip() for c in [B,MI]};assert checks['formal_subtrees'][B]=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c';assert checks['formal_subtrees'][MI]=='8403869aaeb4726518414b409b3808c3c0780e65'
checks['prior_five']=[]
for p in sorted((ROOT/'actual-input/prior-accepted/actual-at-accepted-MI').rglob('*.md')):
 rel=p.relative_to(ROOT/'actual-input/prior-accepted/actual-at-accepted-MI').as_posix();b=p.read_bytes();assert b==show(MI,rel)==show('b0eea808887a688d52d28390ac8886fed9c10bcf',rel);checks['prior_five'].append({'path':rel,**identity(b),'qualification':'EXACT_PRESERVATION_ONLY'})
assert len(checks['prior_five'])==5
journal=load(ROOT/'actual-input/integration/applied-clauses.json');admins={x['path']:x for x in journal['root_administrative_reception_adjustments']};checks['journal_files']=[];hunks=[]
for row in journal['files']:
 p=row['path'];base=show(B,p) if git('ls-tree',B,'--',p) else b'';match(base,row['baseline_identity']);lines=base.decode().splitlines(keepends=True);cursor=0;parts=[]
 for h in sorted(row['hunks'],key=lambda x:(x['base_line_indices_half_open'][0],x['batch_order'])):
  a,b=h['base_line_indices_half_open'];assert a>=cursor,(p,a,cursor);removed=''.join(lines[a:b]).encode();added=h['added_text'].encode();assert removed==h['removed_text'].encode();match(removed,h['removed_identity']);match(added,h['added_identity']);candidate=show(h['candidate_commit'],h['candidate_path']).decode().splitlines(keepends=True);ca,cb=h['candidate_line_indices_half_open'];assert ''.join(candidate[ca:cb]).encode()==added
  parts+=[''.join(lines[cursor:a]),h['added_text']];cursor=b
  actual=show(MI,p).decode().splitlines(keepends=True);fa,fb=h['actual_final_line_indices_half_open']
  # The explicitly authorized errata administrative rewrite changes two JSON
  # reception fields inside its candidate span. Verify its exact assembled
  # candidate first, then compare the permitted final JSON fields below.
  if p not in admins or 'added_text' in admins[p]:assert ''.join(actual[fa:fb]).encode()==added,(p,h['batch_id'],fa,fb)
  hunks.append({k:v for k,v in h.items() if k not in ['added_text','removed_text']})
 parts.append(''.join(lines[cursor:]));assembled=''.join(parts).encode();match(assembled,row['assembled_candidate_clauses_identity']);cur=show(MI,p);admin=admins.get(p)
 if not admin:assert cur==assembled
 elif 'added_text' in admin:assert cur==assembled+admin['added_text'].encode()
 else:
  a=json.loads(assembled);b=json.loads(cur)
  changes={k:[a.get(k),b.get(k)] for k in set(a)|set(b) if a.get(k)!=b.get(k)}
  assert set(changes)=={'status','reception'},changes
  assert changes['status']==['CANDIDATE_READY_NOT_REVIEWED','INTEGRATED_PENDING_INDEPENDENT_ACTUAL_REVIEW']
  assert {k for k in a['reception'] if a['reception'][k]!=b['reception'][k]}=={'candidate_review','shared_integration'}
  assert b['reception']['ACCEPTED'] is False and b['reception']['CLOSED'] is False
  checks['errata_admin_field_changes']=changes
 match(cur,admin['after_identity'] if admin else row['assembled_candidate_clauses_identity'])
 checks['journal_files'].append({'path':p,'contributors':row['contributors'],'hunks':len(row['hunks']),'assembled_identity':identity(assembled),'actual_identity':identity(cur),'result':('EXACT_CANDIDATE_ASSEMBLY_THEN_DECLARED_ADMIN_ADJUSTMENT_ONLY' if admin else 'ALL_CANDIDATE_SPANS_PRESERVED')})
checks['journal_hunks']=hunks;assert len(hunks)==56 and len(checks['journal_files'])==24
checks['same_boundary_insertions']=journal['same_boundary_insertions']
checks['root_admin_adjustments']=journal['root_administrative_reception_adjustments']
checks['U08_targets']=[x for x in checks['journal_files'] if 'R7-U08' in x['contributors']]
checks['U02_UI_receiver']={'path':'deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md','candidate':'84e2cca132ada38405657f19cbbd3d6891d4794f','approval':'44276c5ae69ef0970a98464a5a9e6ff7eb1c1f1c','hunk_present_once':True,'semantic_credit':'PRESERVATION_AND_COMPATIBILITY_WITH_U08_ONLY'}
checks['skill_search']={c:git('ls-tree','-r','--name-only',c,'--','.agents').decode().splitlines() for c in [B,MI,'c64774c60d91e522cb515ef71e3e9d4ea6b4712c']};assert not any(checks['skill_search'].values())
checks['source_settings']=identity((ROOT/'bootstrap/001_Settings.rb').read_bytes());entry=git('ls-tree',R,'--','Data/Scripts/001_Settings.rb',repo=ROOT/'reference-meta.git').decode();assert checks['source_settings']['git_blob'] in entry
checks['binding_spans']=[]
contract=load(ROOT/'original/dispatch/delegation/contracts/R7-U08.json');seen=set()
def walk(x):
 if isinstance(x,dict):
  if all(k in x for k in ['raw_member_byte_offsets','raw_member_sha256','input_sha256']):
   a,b=x['raw_member_byte_offsets'];key=(x['input_sha256'],a,b)
   if key not in seen:
    seen.add(key);p=ROOT/'original/evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs'/(x['input_sha256']+'.raw');d=p.read_bytes()[a:b];assert len(d)==x['raw_member_bytes'] and hashlib.sha256(d).hexdigest()==x['raw_member_sha256'];checks['binding_spans'].append({'input_sha256':key[0],'offsets':[a,b],'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'result':'MATCH'})
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(contract)
checks['status']='ALL_FIXED_BYTES_TREE_SPANS_AND_SCOPE_MATCH';(OUT/'input-byte-validation.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in checks.items() if k not in ['plan_files','formal_131','journal_files','journal_hunks','root_admin_adjustments','binding_spans']},ensure_ascii=False,indent=2));print('plan counts',[(x['count'],x['bytes']) for x in checks['plan_files']]);print('binding spans',len(checks['binding_spans']))
