#!/usr/bin/env python3
"""Independent fixed Git/document audit only. No reference behavior execution."""
import collections,csv,hashlib,io,json,re,subprocess
from pathlib import Path
P=Path('/workspace/pokemon-essentials-clean-room');R=Path('/workspace/reference-b03');D=Path(__file__).resolve().parent
I='e24f2ac6f43642ea0e68bd9aa21fb2c313d6ebdf';U='ae230e76e9c041f39c28948321d0960804c02388';B='9576f00e7d3aeb96f7ca8c42caccfba8f808505e';C='3c5728a47142c57abfdf3d55033768bc44a1f627';H='105a21a0bcba174d4c22a0e67231ed4f38c97693';R1='4706be652a4d9e70656d1e2db1cbc0be9a9194c6';R2='a69d6e057723cc8f8aec8cac0f868da4e456d0eb';G='93e10babe0b9c9ef8b3f5277754541b447beeeb4';PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed';S='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
AP='review/remediation/20261003-prepare/';ST=AP+'batches/B03/integration-stage-1/';RP1=AP+'batches/B03/review-round-1/';RP2=AP+'batches/B03/review-round-2/';AUTHOR=AP+'batches/B03/author';T='deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md'
checks=[]
def need(c,n):
 checks.append({'check':n,'pass':bool(c)})
 if not c:raise AssertionError(n)
def git(*args,repo=P):return subprocess.check_output(['git','-C',str(repo),*args])
def read(rev,p):return git('show',rev+':'+p)
def obj(rev,p):return json.loads(read(rev,p))
def sha(x):return hashlib.sha256(x).hexdigest()
def stable(x):return sha(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def identity(rev,p,repo=P):
 data=git('show',rev+':'+p,repo=repo)
 return {'commit':rev,'path':p,'git_blob':git('rev-parse',rev+':'+p,repo=repo).decode().strip(),'sha256':sha(data),'bytes':len(data)}
def tsv(rev,p):return list(csv.DictReader(io.StringIO(read(rev,p).decode()),delimiter='\t'))
def names(a,b):return git('diff','--name-only',a,b).decode().splitlines()
def diff(a,b):return git('diff','--binary','--full-index','--no-renames','--no-ext-diff','--no-textconv','--no-color',a,b)
def dump(name,x):(D/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
formal=[x['path'] for x in obj(R2,RP2+'input-identity-manifest.json')['formal_payload']]
public=['audit/source-traceability.md','deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md','planning/coverage.md','planning/feature-matrix.md',AP+'approval-ledger.tsv',AP+'traceability-successor.tsv',AP+'historical-errata.md',AP+'final-integration-review.md']
need(len(formal)==13 and len(public)==10,'13 formal and10 public exact scope')
source=[]
for rev,prefix in [(H,AUTHOR+'/'),(H,AUTHOR+'-v2/'),(H,AUTHOR+'-v3/'),(R1,RP1),(R2,RP2)]:
 paths=git('ls-tree','-r','--name-only',rev,'--',prefix).decode().splitlines()
 for p in paths:
  need(read(rev,p)==read(I,p),'immutable source byte preservation '+p)
  source.append(identity(rev,p))
need(len(source)==70,'43author plus27review original bytes preserved')
formal_records=[]
for p in formal:
 records={rev:identity(rev,p) for rev in [B,U,C,H,R2,I]}
 need(all(read(rev,p)==read(C,p) for rev in [H,R2,I]),'formal candidate/handoff/report/integration exact '+p)
 need(read(I,p)==(P/p).read_bytes(),'formal current workspace frozen '+p)
 formal_records.append({'path':p,'identities':records})
mgmt=git('ls-tree','-r','--name-only',I,'--',ST).decode().splitlines();need(len(mgmt)==14,'all14final integration materials')
up_paths=names(U,I);cand_paths=names(C,I)
need(set(up_paths)==set(formal+public+mgmt+[x['path'] for x in source]),'complete final107paths exact scope')
need(len(up_paths)==107 and len(cand_paths)==145,'final full diffs107/145 include all3evidence additions')
full_diffs={}
for label,base in [('accepted_upstream_to_actual',U),('candidate_to_actual',C)]:
 data=diff(base,I);full_diffs[label]={'base':base,'target':I,'bytes':len(data),'sha256':sha(data),'path_count':len(names(base,I)),'records':[{'status':line.split('\t')[0],'path':line.split('\t')[1],'new':identity(I,line.split('\t')[1])} for line in git('diff','--name-status',base,I).decode().splitlines()]}
merges=[('c3cd659295cd985489a524253535d8d4e9f70965',[U,R2]),('9316092c62eac8673c28f9a1f05800b2bcf34de6',['c3cd659295cd985489a524253535d8d4e9f70965',R1])]
for commit,parents in merges:need(git('show','-s','--format=%P',commit).decode().strip().split()==parents,'ordinary merge exact parents '+commit)
need(set(names(merges[0][0],merges[1][0]))=={x['path'] for x in source if x['commit']==R1},'second merge only12firstreport additions')
for rev in [B,U,C,H,R1,R2]:need(git('merge-base',rev,I).decode().strip()==rev,'reviewed/accepted ancestor '+rev)
freeze=obj(I,ST+'diff-and-freeze.json');payload=freeze['payload_commit']
need(git('rev-parse',I+'^').decode().strip()==payload,'finalevidenceonly exact parent')
need(set(names(payload,I))=={ST+p for p in ['upstream-to-payload.patch','candidate-to-payload.patch','diff-and-freeze.json']},'final commit only3new evidence files')
for r in freeze['full_payload_diffs']:
 data=diff(r['base_commit'],r['target_commit'])
 need(read(I,r['path'])==data and r['sha256']==sha(data) and r['bytes']==len(data),'full payload patch exact '+r['path'])
nested_diffcheck=subprocess.run(['git','-C',str(P),'diff','--check',U,I],capture_output=True,text=True)
need(nested_diffcheck.returncode in [0,2], 'full nestedpatch diffcheck observed status')
need(all(line.startswith(ST+'candidate-to-payload.patch:') or line.startswith(ST+'upstream-to-payload.patch:') for line in nested_diffcheck.stdout.splitlines() if ': trailing whitespace.' in line), 'full diffcheck warnings only two literal patch artifacts')
git('diff','--check',U,I,'--',':(exclude)*.patch',':(exclude)*.diff')
need(True,'formal/public/JSON/review non-patch whitespace check')
# Every inherited upstream path outside explicitly allowed modified paths is preserved.
up_tree=git('ls-tree','-r','--name-only',U).decode().splitlines();protected_paths=[p for p in up_tree if p not in formal+public]
need(all(p not in up_paths for p in protected_paths),'all prior B01/B02/B05/evidence/acceptance/PRE0/plan/other formal bytes preserved '+str(len(protected_paths)))
for prefix in [AP+'batches/B05/',AP+'batches/B02/',AP+'batches/B01/','review/remediation-20261003-prepare/']:
 need(not git('diff','--name-only',U,I,'--',prefix).strip(),'protected accepted directory '+prefix)
# Independent current/frozen identity verification of nested registrar objects.
identity_records=[]
def walk(v,where):
 if isinstance(v,dict):
  if {'path','git_blob','sha256','bytes'} <= set(v):
   rev=v.get('commit',I)
   if re.fullmatch(r'[0-9a-f]{40}',rev):
    got=identity(rev,v['path']);need(all(str(got[k])==str(v[k]) for k in ['git_blob','sha256','bytes']),'registrar identity '+where+' '+v['path']);identity_records.append({'where':where,**got})
  for k,w in v.items():walk(w,where+'/'+k)
 elif isinstance(v,list):
  for j,w in enumerate(v):walk(w,where+'/'+str(j))
for fn in ['integration-manifest.json','merge-and-dependency-impact.json','downstream-interface-investigation.json','accepted-primary-completion.json']:
 walk(obj(I,ST+fn),fn)
for row in tsv(I,ST+'current-hashes.tsv'):
 got=identity(row['binding'] if re.fullmatch(r'[0-9a-f]{40}',row['binding']) else I,row['path']);need(all(str(got[k])==row[k] for k in ['git_blob','sha256','bytes']),'current65hash '+row['path'])
# Canonical/approval/trace identities and exact old42 records.
original={x['id']:x for x in obj(G,'review/global-independent-review/2026-10-03-fd82a639/findings.json')};acc=obj(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
coverage={x['finding_id']:x for x in tsv(PLAN,'review/remediation-20261003-prepare/finding-coverage.tsv')};batches={x['id']:x for x in obj(PLAN,'review/remediation-20261003-prepare/batches.json')}
ledger_path=AP+'finding-ledger.tsv';need(read(U,ledger_path)==read(I,ledger_path),'canonical229ledger exact accepted bytes')
ledger=tsv(I,ledger_path);need(len(ledger)==229 and all(x['canonical_state']=='OPEN' for x in ledger),'229 canonical required OPEN and0CLOSED')
need(set(x['finding_id'] for x in ledger)=={k for k,v in original.items() if v['required_revision']},'canonical exact required originalID set')
for p in [AP+'approval-ledger.tsv',AP+'traceability-successor.tsv']:
 old,new=read(U,p),read(I,p);need(new.startswith(old),'old42contribution fullprefix '+p)
 rows=tsv(I,p);need(len(rows)==69 and all(x['canonical_state']=='OPEN' for x in rows),'69contributions OPEN '+p)
 need(len({(x['finding_id'],x['candidate_commit']) for x in rows})==69,'69 unique finding/candidatepairs '+p)
r2={x['id']:x for x in obj(R2,RP2+'finding-dispositions.json')['dispositions']};prior={x['id']:x for x in obj(R1,RP1+'finding-dispositions.json')['dispositions']};auth={x['id']:x for x in obj(H,AUTHOR+'-v3/finding-responses.json')}
registration=obj(I,ST+'finding-registration.json')['dispositions'];need(len(registration)==27 and sum(x['primary_in_B03'] for x in registration)==19,'27contributions and19primary exact')
need({x['id'] for x in registration}==set(batches['B03']['contribution_finding_ids']),'exact B03 canonicalcontribution IDs')
for row in registration:
 fid=row['id'];o=original[fid];a=acc[fid];r=r2[fid]
 need(row['original_complete_object_sha256']==stable(o) and row['acceptance_object_sha256']==stable(a),'complete original/acceptance binding '+fid)
 for k in ['current_qualifications','adjudication_precedence','effective_case_constraints']:
  need(row[k]==o.get(k),'effective original qualification '+fid+' '+k)
 need(row['minimum_revision']==o['minimum_revision'] and row['determinate_recheck']==o['determinate_recheck'] and row['acceptance_gate']==a['acceptance_gate'],'full effective gates retained '+fid)
 need(row['all_contributor_batches']==coverage[fid]['contributor_batches'].split(';'),'all approvedcontributors retained '+fid)
 need(set(row['other_batch_obligations'])==set(row['all_contributor_batches'])-{'B03'},'every otherbatch obligation retained '+fid)
 need(row['project_evidence']==r['project_evidence'] and row['static_test_evidence_not_executed']==r['test_evidence'] and row['reviewer_scoped_judgment']==r['independent_judgment'] and row['remaining_scope']==r['remaining_scope'],'current formal/test/judgment/scope exactR2 '+fid)
 need(row['author_v3_response_preserved']==auth[fid] and row['prior_candidate_verdict']==prior[fid]['verdict'],'author/priorreviewimmutable perID '+fid)
 need(row['priority']==o['priority'] and row['canonical_state']=='OPEN' and not row['canonical_edited'] and row['candidate_verdict']=='PASS_SCOPED','no severity/closure change '+fid)
 need(row['actual_integration_verdict']=='NOT_REVIEWED_PENDING_R_B03_ULTRA' and 'BLOCKED' in row['downstream_gate'],'frozenpending status not borrowedPASS '+fid)
 for path in [AP+'approval-ledger.tsv',AP+'traceability-successor.tsv']:
  line=next(x for x in tsv(I,path) if x['finding_id']==fid and x['candidate_commit']==C)
  need(line['candidate_review_commit']==R2,'public candidate report identity '+fid+path)
  if 'effective_priority' in line:need(line['effective_priority']==o['priority'],'trace priority '+fid)
obs=obj(I,ST+'review-observation-registration.json')['observations'];r1obs={x['id']:x for x in obj(R1,RP1+'finding-dispositions.json')['new_findings']};r2obs={x['id']:x for x in obj(R2,RP2+'finding-dispositions.json')['prior_observation_dispositions']}
need({x['observation_id'] for x in obs}==set(r1obs),'3P2 observation exactset')
for x in obs:
 fid=x['observation_id'];need(x['original_observation']==r1obs[fid] and x['repair_disposition_preserved']==r2obs[fid],'complete3P2original andrepair objects '+fid)
 need(x['priority']=='P2' and not x['closed'] and not x['original_229_ledger_mutated'],'3P2severity/no canonicalclosure '+fid)
# Static row bytes/counts and shared tail, no vector evaluation.
def byte_rows(data):return {m[1].decode():line for line in data.splitlines(keepends=True) if (m:=re.match(rb'^\| ((?:MP|MV|EV|FW|IM|MR|DG|RS|WT|FS)\d+) \|',line))}
old,new=byte_rows(read(B,T)),byte_rows(read(I,T));need(new==byte_rows(read(C,T)),'all311shared rows exactcandidate')
counts=dict(collections.Counter(re.sub(r'\d+$','',k) for k in new));need(counts=={'MP':27,'MV':77,'EV':39,'FW':7,'IM':41,'MR':17,'DG':43,'RS':20,'WT':25,'FS':15},'251B03+60protectedshared=311 static vectors')
tail=read(I,T).split(b'## H.',1)[1];need(tail==read(B,T).split(b'## H.',1)[1],'entire WP15/59/60tail exactbytes')
# Derive26primary classifications independently from canonical plan and exact accepted reports.
accepteds={'B01':('93d0714ddfdb4900e946c0acd1cc80cf6431f0a0','8a1fdfb2b582df4cefb408b56eea144a2e53dcfe','0a12de641542f9a59909d2a950c1de8df17ca09d'),'B02':('1b1e169faf273e89ad6b7f5e46fd7b60d87d3946','361e4e69126559c266a08fdf093082dbbcd83f8d',B),'B05':('cc085d618ce8b5ebda82c28a3a1ac9a09dda9a85','59b0451799cbfea41b12e2e1c3bb779420ed5ea9',U)}
accepted_rows=tsv(U,AP+'approval-ledger.tsv');review_by={}
for batch,(irev,rrev,acceptedrev) in accepteds.items():
 p=AP+'batches/'+batch+'/integration-review-1/finding-dispositions.json';rs=obj(rrev,p);rs=rs['dispositions'] if isinstance(rs,dict) else rs
 review_by[batch]={r['id']:r for r in rs}
 need(read(rrev,p)==read(I,p),'accepted reviewer bytes '+batch)
 need(git('merge-base',acceptedrev,I).decode().strip()==acceptedrev,'accepted successor ancestor '+batch)
 for fid in batches[batch]['primary_finding_ids']:
  need(fid in review_by[batch] and any(r['finding_id']==fid and r['integration_review_commit']==rrev and r['reviewed_integration_commit']==irev and r['integration_verdict']=='PASS_SCOPED' for r in accepted_rows),'accepted primary realI/report/registration '+fid)
primary={fid:batch for batch in accepteds for fid in batches[batch]['primary_finding_ids']};need(len(primary)==26,'canonical primaryunique7+9+10=26')
stat=obj(I,ST+'accepted-primary-completion.json');srows={r['id']:r for r in stat['rows']};need(set(srows)==set(primary),'stats exactcanonical26primary IDs')
stat_check=[]
for fid,batch in primary.items():
 row=srows[fid];o=original[fid];a=acc[fid];contributors=coverage[fid]['contributor_batches'].split(';')
 need(row['primary_owner']==batch and row['known_contributor_batches']==contributors,'statisticsowner/allcontributors '+fid)
 need(row['original_object_sha256']==stable(o) and row['acceptance_object_sha256']==stable(a),'statisticsfullbindings '+fid)
 for k,k2 in [('qualified_minimum_revision','minimum_revision'),('qualified_determinate_recheck','determinate_recheck'),('current_qualifications','current_qualifications'),('effective_case_constraints','effective_case_constraints')]:need(row[k]==o.get(k2),'statistics originaleffective field '+fid+k)
 need(row['owner_actual_review_disposition']==review_by[batch][fid],'stats exact independent actualdisposition '+fid)
 for record in row['accepted_contribution_records']:need(record in accepted_rows,'statistics prior accepted realrecord '+fid)
 global_batches=['B21'] if fid in ['WP80-B02-R02','GIR-FD82-A017'] else []
 missing=[b for b in contributors if b not in accepteds and b not in global_batches]
 category=2 if missing else 1
 need(row['classification']==category and row['global_aggregation_batches']==global_batches and row['missing_specific_batches']==missing,'independent classification specificobligations '+fid)
 need(row['canonical_state']=='OPEN' and not row['closure_performed'],'statistics notcanonicalclosure '+fid)
 stat_check.append({'id':fid,'owner':batch,'specific_revision_classification':category,'canonical_plan_contributor_batches':contributors,'pending_specific_batches':missing,'pending_global_aggregation_batches':global_batches,'strict_unaccepted_contributor_batches':[b for b in contributors if b not in accepteds],'original_object_sha256':stable(o),'acceptance_object_sha256':stable(a),'actual_review_commit':accepteds[batch][1]})
need(collections.Counter(r['specific_revision_classification'] for r in stat_check)=={1:25,2:1},'derived25specificsatisfied/1A024B07/0insufficient')
need(next(x for x in stat_check if x['pending_specific_batches'])['id']=='GIR-FD82-A024','A024 onlyspecific consumerpending')
# Compare independent counts to both published statistical formats.
for cat in [1,2,3]:
 ids=[r['id'] for r in stat_check if r['specific_revision_classification']==cat]
 need(stat['classification_summary'][str(cat)]['count']==len(ids) and set(stat['classification_summary'][str(cat)]['ids'])==set(ids),'statistical summary independently derived '+str(cat))
stat_tsv=tsv(I,ST+'accepted-primary-completion.tsv')
need(len(stat_tsv)==26 and {r['canonical_id'] for r in stat_tsv}==set(primary),'statistical TSV exact26IDs')
for r in stat_tsv:
 fid=r['canonical_id'];j=srows[fid]
 need(r['primary_owner']==j['primary_owner'] and int(r['classification'])==j['classification'] and r['known_contributors'].split(';')==j['known_contributor_batches'] and r['canonical_state']=='OPEN','statistical TSV classification/owner/contributors '+fid)
 need(r['reviewed_integration']==accepteds[primary[fid]][0] and r['actual_review_report']==accepteds[primary[fid]][1] and r['accepted_successor']==accepteds[primary[fid]][2],'statistical TSV exactI/report/acceptance identity '+fid)
for path in ['planning/coverage.md','planning/feature-matrix.md',AP+'historical-errata.md','audit/source-traceability.md']:
 old=read(U,path);new=read(I,path)
 need(new.endswith(old.split(b'\n',1)[1]),'new public layer preserves entire prior body suffix '+path)
need(read(I,AP+'final-integration-review.md').endswith(read(U,AP+'final-integration-review.md')),'central prior B01/B02/B05 entire handoff suffix immutable')
need(sha(read(I,T)[read(I,T).index(b'## H.'):])==obj(I,ST+'scope-counts.json')['shared_H_onward_sha256'],'sharedtail registrar includesHheader; matches exact protected bytes')
# Exact dependency crosssets and every downstream frozen input identity.
cross={'B04_write_to_B06_read':sorted(set(batches['B04']['write_paths'])&set(batches['B06']['read_paths'])),'B06_write_to_B04_read':sorted(set(batches['B06']['write_paths'])&set(batches['B04']['read_paths'])),'write_write':sorted(set(batches['B04']['write_paths'])&set(batches['B06']['write_paths'])),'shared_canonical_contributions':sorted(set(batches['B04']['contribution_finding_ids'])&set(batches['B06']['contribution_finding_ids']))}
need([len(cross[k]) for k in ['B04_write_to_B06_read','B06_write_to_B04_read','write_write']]==[4,1,0] and cross['shared_canonical_contributions']==['GIR-FD82-A059'],'independent4+1directed conflicts andA059sharedroot')
invest=obj(I,ST+'downstream-interface-investigation.json')
for k in cross:need(invest['exact_cross_sets'][k]==cross[k],'registeredexactcrossset '+k)
read_change=[p for p in batches['B06']['read_paths'] if p not in ['review/global-independent-review/2026-10-03-fd82a639/findings.json','review/global-independent-review/2026-10-03-fd82a639/root/remediation-index.tsv'] and read(U,p)!=read(I,p)]
need(read_change==[T],'B06exactstale read onlysharedenginecatalog')
for entry in invest['qualified_interface_findings']:
 fid=entry['interface']['id'];need(entry['original_binding']==stable(original[fid]) and entry['acceptance_binding']==stable(acc[fid]) and entry['effective_case_constraints']==original[fid].get('effective_case_constraints'),'A034/A059/C103full qualifiedbinding '+fid)
need(not invest['dispatch_performed'] and not invest['B06_unlock_performed'] and not invest['B04_unlock_performed'],'registrar didnot dispatch/unlock')
# Fixed reference and documented source hashes only; no Ruby execution.
need(git('rev-parse','HEAD',repo=R).decode().strip()==S and git('rev-parse','HEAD^{tree}',repo=R).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0','fixedreference exactSHA/tree')
need(not git('status','--porcelain',repo=R).strip(),'referenceclean')
for record in obj(R2,RP2+'source-reading-log.json')['fresh_round2_records']:
 got=identity(S,record['path'],repo=R);need(all(got[k]==record[k] for k in ['git_blob','sha256','bytes']),'R2 fixed literal sourcehash '+record['path'])
# New public relative links; do not run author scripts.
link_count=0
for path in public:
 txt=read(I,path).decode()
 for target in re.findall(r'\[[^\]]+\]\(([^)]+\.md|[^)]+\.json|[^)]+\.tsv)(?:#[^)]*)?\)',txt):
  if not re.match(r'[a-z]+:',target):
   # Historical links can predate removed snapshot files; review only newly added links.
   if target not in read(U,path).decode():need((P/path).parent.joinpath(target).resolve().is_file(),'newpublic relative link '+path+target);link_count+=1
validation={'result':'PASS_FIXED_IDENTITY_AND_DOCUMENT_AUDIT','reviewed_integration_commit':I,'reviewed_tree':git('rev-parse',I+'^{tree}').decode().strip(),'checks':checks,'check_count':len(checks),'formal_files':13,'immutable_source_paths':83,'old42public_contribution_records_preserved':True,'canonical229OPEN':True,'canonical_closed':0,'final_diff_path_counts':{'upstream':107,'candidate':145},'static_B03_vectors':251,'static_shared_other':60,'static_vectors_executed':0,'reference_execution':0,'runtime_observations':0,'proven_demo_chains':0,'new_public_links_checked':link_count,'actual_manual_semantic_review_separate':True,'capacity_failure_is_pass_evidence':False,'nested_patch_diffcheck':{'raw_returncode':nested_diffcheck.returncode,'raw_warning_count':nested_diffcheck.stdout.count(': trailing whitespace.'),'scope':'Two literal full-context frozenpatch artifacts only; exactdiff reconstruction verified; non-patch files pass separately'}}
dump('independent-validation.json',validation)
dump('complete-diff-manifest.json',{'reviewed_integration':I,'tree':validation['reviewed_tree'],'upstream':U,'candidate':C,'full_final_diffs':full_diffs,'formal_payload':formal_records,'immutable_author_and_report_sources':source,'all14integration_evidence':[identity(I,p) for p in mgmt],'registrar_identity_records_verified':identity_records,'preserved_upstream_path_count':len(protected_paths),'full_diff_method':'git diff --binary --full-index --no-renames --no-ext-diff --no-textconv --no-color; final actualcommit, not payloadonly'})
dump('primary-completion-review.json',{'reviewed_integration':I,'canonical_plan':PLAN,'original_report':G,'independent_specific_obligation_counts':{'satisfied_scoped':25,'missing_specific_consumer':1,'insufficient_evidence':0},'approved_unique_primary_count':26,'primary_counts':{'B01':7,'B02':9,'B05':10},'scope_interpretation':'25 means original item-specific revision and scoped actual acceptance, not all canonical contributor/final closure gates; B21 audit for WP80-B02-R02 andA017 stillpending','strict_all_contributor_acceptance_counts':{'all_contributor_batches_accepted':23,'still_has_unaccepted_contributor':3},'strict_pending_ids':['WP80-B02-R02','GIR-FD82-A017','GIR-FD82-A024'],'rows':stat_check,'canonical_closed':0,'reference_execution':0})
dump('dependency-identity-review.json',{'reviewed_integration':I,'exact_cross_sets':cross,'B06_plan_read_count':len(batches['B06']['read_paths']),'B04_plan_read_count':len(batches['B04']['read_paths']),'B06_changed_read_paths':read_change,'B06_new_read_identities':[identity(G if p.startswith('review/global-independent-review/') else I,p) for p in batches['B06']['read_paths']],'B06_write_input_identities':[identity(I,p) for p in batches['B06']['write_paths']],'B04_read_identities':[identity(G if p.startswith('review/global-independent-review/') else I,p) for p in batches['B04']['read_paths']],'B04_write_input_identities':[identity(I,p) for p in batches['B04']['write_paths']],'actual_dispatch_or_unlock_performed':False,'parallelism_verified':False,'reference_execution':0})
print(json.dumps({k:v for k,v in validation.items() if k!='checks'},ensure_ascii=False,indent=2))
