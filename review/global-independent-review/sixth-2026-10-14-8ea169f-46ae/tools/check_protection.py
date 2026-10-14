"""Read-only protection verification at a named report publication phase."""
import argparse,datetime,hashlib,json,pathlib,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1];REPO=ROOT.parents[2]
ap=argparse.ArgumentParser();ap.add_argument('label');a=ap.parse_args()
def git(*args,cwd=REPO):return subprocess.check_output(['git','--no-optional-locks',*args],cwd=cwd).decode().strip()
fixed=json.loads((ROOT/'control/session.json').read_text());base=fixed['main']
changed=[]
for file in ['inventory/protected-untracked.json']:
 for x in json.loads((ROOT/file).read_text()):
  p=REPO/x['path'];data=p.read_bytes() if p.exists() else b''
  if len(data)!=x['bytes'] or hashlib.sha256(data).hexdigest()!=x['sha256']:changed.append(x['path'])
for file in ['inventory/reference.json','inventory/formal131.json']:
 for x in json.loads((ROOT/file).read_text()):
  p=(REPO/'reference/pokemon-essentials'/x['path']) if 'reference.json' in file else REPO/x['path']
  data=p.read_bytes()
  if len(data)!=x['bytes'] or hashlib.sha256(data).hexdigest()!=x['sha256']:changed.append(str(p))
diff=git('diff','--name-only',base,'--','AGENTS.md','specs','planning','audit','deliverables','reference')
all_diff=git('diff','--name-only',base)
unexpected_tracked=[p for p in all_diff.splitlines() if not p.startswith(str(ROOT.relative_to(REPO))+'/')]
tag='refs/tags/delivery/fifth-round-closed-final-20261014'
out={'label':a.label,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'head':git('rev-parse','HEAD'),'branch':git('branch','--show-current'),'main':git('rev-parse','main'),
 'origin_main':git('rev-parse','origin/main'),'delivery':git('rev-parse',tag),'delivery_kind':git('cat-file','-t',tag),
 'formal_tree':git('rev-parse','HEAD:deliverables/final-specification-set'),
 'R_commit':git('rev-parse','HEAD',cwd=REPO/'reference/pokemon-essentials'),
 'R_tree':git('rev-parse','HEAD^{tree}',cwd=REPO/'reference/pokemon-essentials'),
 'R_status':git('status','--porcelain=v1',cwd=REPO/'reference/pokemon-essentials'),
 'protected_changed':changed,'protected_tracked_diff':diff.splitlines(),'unexpected_tracked_diff':unexpected_tracked,
 'original_62_checked':62,'reference_432_and_formal131_sha_checked':563,
 'incident_paths_current_absent':{p:not(REPO/p).exists() for p in ['build_review.py','forward-matrix.jsonl']},
 'no_claim_of_zero_historical_write_incidents':True,'update_started':False}
assert out['main']==out['origin_main']==out['delivery']==base
assert out['delivery_kind']=='commit' and out['formal_tree']==fixed['formal_tree']
assert out['R_commit']==fixed['reference_commit'] and out['R_tree']==fixed['reference_tree']
assert not changed and not diff and not unexpected_tracked and not out['R_status']
(ROOT/'control'/('protection-'+a.label+'.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False))
