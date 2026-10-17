#!/usr/bin/env python3
"""Static document validator probes; output and mutation fixtures are isolated."""
from pathlib import Path
import copy,datetime,hashlib,importlib.util,json,shutil,subprocess,sys,tempfile
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent; ROOT=OUT.parents[1]
SRC=ROOT/'planning/implementation-routing/r8-20261017'; E=OUT/'evidence'
def save(n,v):(E/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def digest(b):return hashlib.sha256(b).hexdigest()
m=json.loads((SRC/'routing-manifest.json').read_text());c=json.loads((SRC/'section-coverage.json').read_text())
spec=importlib.util.spec_from_file_location('review_fixed_candidate',SRC/'routing.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
start=datetime.datetime.now(datetime.timezone.utc).isoformat();cases=[]
with tempfile.TemporaryDirectory(prefix='r1-document-tools-') as tmp:
 isolated=Path(tmp);shutil.copyfile(SRC/'routing-manifest.schema.json',isolated/'routing-manifest.schema.json');mod.HERE=isolated
 assert mod.DATA_HOME==SRC
 baseline=mod.errors(m,c);assert not baseline,baseline
 nine=mod.self_test(m,c)
 def check(name,fn,expected):
  mm=copy.deepcopy(m);cc=copy.deepcopy(c);fn(mm,cc)
  try:errors=mod.errors(mm,cc);result={'case':name,'expected':expected,'rejected':bool(errors),'errors':errors}
  except Exception as exc:result={'case':name,'expected':expected,'rejected':True,'exception':str(exc)}
  result['expectation_met']=result['rejected'] if expected=='REJECT' else not result['rejected'];cases.append(result)
 check('missing name',lambda m,c:m['features'][0].pop('name'),'REJECT')
 check('invalid source anchor',lambda m,c:m['features'][0]['source'].update(anchor='missing-anchor'),'REJECT')
 check('unknown route',lambda m,c:m['features'][0]['future_plan'].update(destination='unknown'),'REJECT')
 check('empty coverage mapping replaced by ALL_FORMAL_FEATURES',lambda m,c:c['sections'][60].update(feature_refs=[],coverage_scope='ALL_FORMAL_FEATURES'),'REJECT')
 check('arbitrary existing but unrelated feature coverage',lambda m,c:c['sections'][60].update(feature_refs=[m['features'][-1]['feature_id']]),'MANUAL_SEMANTIC_GATE')
 check('stale coverage title level line_end',lambda m,c:c['sections'][60].update(title='wrong',level=6,line_end=999999),'REJECT')
 check('false current feature snapshot and path',lambda m,c:m['features'][0]['current_applicability'].update(snapshot_commit='0'*40,document='missing.md'),'REJECT')
 check('false declared source formal tree',lambda m,c:m['source_baseline'].update(formal_tree='0'*40),'REJECT')
 check('false source git blob',lambda m,c:m['features'][0]['source'].update(file_git_blob='0'*40),'REJECT')
 check('empty planned collaborators',lambda m,c:m['features'][0]['future_plan'].update(partners=[]),'REJECT')
 check('drop known R8-U06 batch binding',lambda m,c:m['features'][0]['upstream'].update(batches=[],required_ids=[]),'REJECT')
 check('invalid dependency WP',lambda m,c:m['features'][0]['dependencies'].update(wp_refs=['WP999']),'REJECT')
 check('unbound accepted event bypasses gate',lambda m,c:(m['features'][0]['upstream'].update(accepted_events=['invented'],status='已校准'),m['features'][0]['current_applicability'].update(status='已校准')),'REJECT')
 check('invented target evidence structure',lambda m,c:m['features'][0]['destination_verification'].update(status='已验证',evidence=[{'kind':'TARGET_BEHAVIOR_PROTOTYPE','ref':'not-an-evidence','target_commit':'0'*40,'scope':'all','result':'PASS'}]),'MANUAL_AUTHENTICITY_GATE')
 mod.render(m,c)
 rendered=[]
 for p in sorted(isolated.rglob('*')):
  if not p.is_file() or p.name in ['routing-manifest.schema.json','validator-negative-checks.json']:continue
  rel=p.relative_to(isolated);rendered.append({'path':str(rel),'bytes':p.stat().st_size,'sha256':digest(p.read_bytes()),'equal_fixed_candidate':p.read_bytes()==(SRC/rel).read_bytes()})
 assert len(rendered)==11 and all(x['equal_fixed_candidate']for x in rendered)
 fresh=mod.check_generated(m,c);probe=isolated/'views/creature-rpg.md';probe.write_bytes(probe.read_bytes()+b'\nSTALE PROBE\n');stale=mod.check_generated(m,c)
 assert fresh['result']=='PASS_GENERATED_FRESHNESS'and stale['result']=='FAIL'
 try:mod.seed();seed={'refused':False}
 except ValueError as exc:seed={'refused':True,'message':str(exc)}
 assert seed['refused']
 views=[]
 for path in sorted((SRC/'views').glob('*.md')):
  lines=path.read_text().splitlines()
  for number,line in enumerate(lines,1):
   if not line.startswith('| FR-'):continue
   fid=line.split(' / ',1)[0].lstrip('| ');f=next(x for x in m['features']if x['feature_id']==fid)
   children=f['functional_scope']['excluded_child_refs'];missing=[x for x in children if x not in line]
   views.append({'feature_id':fid,'view':str(path.relative_to(ROOT)),'line':number,'excluded_children':children,'missing_child_ids_in_whole_row':missing})
 assert len(views)==736 and len({x['feature_id']for x in views})==736
 save('view-projection.json',{'rows':views,'active_rows':len(views),'missing_child_navigation_rows':[x for x in views if x['missing_child_ids_in_whole_row']],'scope':'All rows projected against candidate IDs; domain reviewers inspect classification semantics. Missing navigation is distinct from byte freshness.'})
 save('independent-tool-replay.json',{'started_utc':start,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'baseline_errors':baseline,'nine_negative_cases':nine,'previous_fourteen_cases_replayed':cases,'rendered_files':rendered,'freshness':fresh,'stale_probe':stale,'seed':seed,'all_structural_expectations_met':all(x['expectation_met']for x in cases),'mutation_boundary':'Only in-memory manifest copies and temporary review-owned output tree. DATA_HOME and Git fixed inputs unchanged. No Ruby/game/framework/business execution.'})
 print(json.dumps({'negative9':nine['all_rejected'],'fourteen_rejected':sum(x['rejected']for x in cases),'expectations_met':all(x['expectation_met']for x in cases),'rendered':len(rendered),'view_missing_rows':sum(bool(x['missing_child_ids_in_whole_row'])for x in views)},ensure_ascii=False))
