#!/usr/bin/env python3
"""This new report's identity and consistency; no reference behavior execution."""
import hashlib,json,pathlib,re,subprocess
D=pathlib.Path(__file__).resolve().parent
P=next(x for x in D.parents if (x/'.git').exists())
C='af39efbf32549be964cb083bd49bed6d1d5c0d2a';C1='47f7514765f8569ae9172bb06a2cd615e2b83b8a';B='1e6b11a47370f1c7c4659a32443fc1afda597bac';S='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
checks=[]
def need(v,label):
 checks.append({'check':label,'pass':bool(v)})
 if not v:raise AssertionError(label)
def read(p):return json.loads((D/p).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args,repo=P):return subprocess.check_output(['git',*args],cwd=repo)
need(git('rev-parse','HEAD').decode().strip()==C,'exact candidate2 before report commit')
need(git('branch','--show-current').decode().strip()=='remediation/20261003-prepare/review-B14-affected-B03-2','prescribed review branch')
m=read('input-identity-manifest.json');first=read('independent-first-judgment.json');final=read('independent-final-judgment.json');f=read('findings.json');dis=read('affected-dispositions.json');v=read('independent-validation.json');receipt=read('execution-request-receipt.json');comparison=read('author-comparison.json');source=read('source-reading-log.json');checkpoint=read('recovery-checkpoint.json')
need(sha(D/'independent-first-judgment.json')==final['first_judgment_sha256']==comparison['independent_first_judgment']['sha256']==checkpoint['independent_first_judgment_sha256'],'first judgment preserved after author comparison/recovery')
need(first['verdict']==final['verdict']==f['verdict']==dis['verdict']==comparison['final_verdict']=='PASS_SCOPED','consistent bounded candidate verdict')
need(all(x['reviewed_candidate']==C for x in [m,first,final,f,dis,v,comparison]),'exact candidate binding across reports')
need([(x['path_count'],x['bytes'],x['sha256']) for x in m['complete_unfiltered_deltas']]==[(46,690132,'64fa7af7383bbc0ab03e56eadff84d1b79a8854463b0d99dce3c38a139099af9'),(22,135924,'cc70984763bc52d8825cea6d394171a1cb1dcc3051a26903488de1aec44558a3')],'both complete unfiltered diff identities')
need(m['candidate1']==C1 and m['accepted_predecessor']==B,'candidate1 and accepted predecessor identity')
need([(x['id'],x['original_severity'],x['successor_disposition']) for x in f['round1_finding_dispositions']]==[('B14-AFFECTED-B03-001','P2','PASS_SCOPED'),('R-B14-1-001','P3','PASS_SCOPED'),('B14-B04-R1-01','P2','PASS_SCOPED')],'all three findings and exact original severity retained')
need(all(x['original_verdict']=='REQUEST_CHANGES' for x in f['round1_finding_dispositions']) and f['original_report_verdicts_rewritten'] is False,'original three round1 verdicts immutable')
need(f['new_findings']==final['new_findings']==comparison['new_findings']==[],'no new scoped finding hidden in summary')
for item in f['round1_finding_dispositions']:
 need(all(item.get(k) for k in ['positive','counterexample','consumer_contrast','scope','remaining','acceptance_assessment']),'explicit case/reverse/remaining/acceptance '+item['id'])
 for evidence in item['project_evidence']+item['reference_evidence']:
  reference=evidence['repository']=='reference';repo=pathlib.Path('/workspace/reference-b03') if reference else P;rev=S if reference else C
  raw=git('show',rev+':'+evidence['path'],repo=repo)
  need(evidence['commit']==rev and evidence['sha256']==hashlib.sha256(raw).hexdigest() and evidence['bytes']==len(raw),'fixed exact case evidence '+item['id']+' '+evidence['path'])
  need(all(1<=int(x)<=len(raw.decode().splitlines()) for x in re.findall(r'\d+',evidence['lines'])),'only actual source/project line locations '+item['id']+' '+evidence['path'])
expected=['GIR-FD82-002','GIR-FD82-C003','GIR-FD82-C007','GIR-FD82-C094','GIR-FD82-C095','WP80-INTAKE-R01']
need([x['id'] for x in dis['original_control_dispositions']]==expected,'all six original affected controls retained')
control={x['id']:x['complete_contract_control'] for x in read('qualified-control-bindings.json')}
for item in dis['original_control_dispositions']:
 need(item['whole_original_object_sha256']==control[item['id']]['whole_original_object_sha256'] and item['whole_acceptance_object_sha256']==control[item['id']]['whole_acceptance_object_sha256'],'whole qualified object binding '+item['id'])
 need(item['disposition']=='PASS_SCOPED' and item['canonical_state']=='OPEN' and item['remaining'] and item['acceptance'],'scoped pass with remaining/acceptance '+item['id'])
need(v['check_count']==final['independent_metadata_checks']==1411 and v['semantic_verdict_separate'],'metadata1411 checks distinct from semantic review')
need([(x['raw_returncode'],x['raw_warnings'],x['nonpatch_returncode']) for x in v['raw_whitespace_checks']]==[(2,80,0),(2,23,0)],'raw patch warning scope accurate')
cat=read('catalog-preservation.json')
need(cat['B03_rows_preserved']==251 and cat['B04_R_rows_preserved']==28 and sum(x['versions']['candidate2'] for x in cat['catalogs'])==505,'protected owner/static505 inventory')
need(receipt['reference_game_ruby_compiler_converter_generator_deserializer_solver_emulator_execution']==receipt['reference_helpers_or_historical_verifiers_executed']==receipt['behavior_simulation']==receipt['static_design_execution']==0,'no reference/helper/old verifier/behavior execution')
need(receipt['configuration_probes']==receipt['quota_probes']==receipt['quota_checks']==receipt['child_tasks']==0,'no probes/children')
need(receipt['requested_model']=='gpt-6.1-sol' and receipt['requested_reasoning']=='Ultra' and receipt['requested_speed']=='inherited Standard(default)' and receipt['effective_model_reasoning_speed']=='UNVERIFIED','requested settings accurate and effective unverified')
need(all(x['canonical_open']==229 and x['canonical_closed']==0 for x in [first,final,f,dis,receipt]),'canonical229OPEN/0CLOSED')
need(all(x['actual_integration_checked'] is False for x in [first,final,f,dis,receipt,m]),'actual gate not prepaid')
need(len(source['literal_reads'])==20 and source['fixed_commit']==S,'fresh scoped source identity records')
for entry in source['literal_reads']:
 raw=git('show',S+':'+entry['path'],repo=pathlib.Path('/workspace/reference-b03'))
 need(entry['sha256']==hashlib.sha256(raw).hexdigest() and entry['bytes']==len(raw),'source reading fixed bytes '+entry['path'])
for p in D.glob('*.json'):json.loads(p.read_text())
need(True,'all new JSON parses')
for p in D.glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if target.startswith('https://'):need('/blob/'+C+'/' in target or '/blob/'+S+'/' in target,'external evidence fixed candidate/reference '+p.name)
  else:need((p.parent/target.split('#',1)[0]).is_file(),'relative review link '+target)
text=(D/'report.md').read_text()
need(all(x in text for x in ['PASS_SCOPED','实际integration','80/23','REQUEST_CHANGES','24 贡献/19 主责','未执行','UNVERIFIED']),'self-contained scope/gates/execution/warnings in report')
files=[{'path':p.relative_to(P).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(D.iterdir()) if p.is_file() and p.name!='review-document-validation.json']
out={'result':'PASS_NEW_REVIEW_DOCUMENT_IDENTITY_CONSISTENCY_ONLY','semantic_verdict':'PASS_SCOPED','reviewed_candidate':C,'checks_count':len(checks),'checks':checks,'new_document_inventory_excluding_this_result':files,'reference_behavior_execution':0,'actual_integration_checked':False,'self_result_hash_included':False}
(D/'review-document-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':out['result'],'checks':len(checks),'bound_documents':len(files),'semantic_verdict':out['semantic_verdict']}))
