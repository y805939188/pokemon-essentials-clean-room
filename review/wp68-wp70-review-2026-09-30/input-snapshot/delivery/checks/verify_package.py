"""Own text/identity checker only; never loads or executes reference programs."""
from pathlib import Path
import sys,json,hashlib,re,subprocess,datetime
ROOT=Path('/Users/dingshinn/Desktop/pokemon-spec-parallel-minigames')
REF=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PACKAGES={'WP68':['specs/ui/wp68-duel.md','specs/creature-rpg/wp68-triple-triad.md'],'WP69':['specs/ui/wp69-slot-machine.md','specs/pokemon-rules/wp69-voltorb-flip.md','specs/ui/wp69-slot-reels.md','specs/pokemon-rules/wp69-voltorb-layouts.md'],'WP70':['specs/pokemon-rules/wp70-lottery.md','specs/ui/wp70-mining.md','specs/ui/wp70-mining-data.md']}
def identity(p):
 b=p.read_bytes(); return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def check_inputs():
 m=json.loads((ROOT/'delivery/input-manifest.json').read_text()); count=0
 for key in ['frozen_inputs','review_authority','handoff_inputs']:
  for e in m[key]:
   for p in [e.get('frozen_source_path',e.get('path')),e['local_copy_path']]:
    assert identity(Path(p))=={k:e[k] for k in ['sha256','bytes']},p
   count+=1
 return count
pkg=sys.argv[1]; assert pkg in PACKAGES
out=ROOT/f'delivery/checks/{pkg.lower()}-fixed.json'; assert not out.exists(),'Do not silently replace a fixed package record'
assert subprocess.check_output(['git','-C',str(REF),'rev-parse','HEAD'],text=True).strip()==COMMIT
files=[]
for name in PACKAGES[pkg]:
 p=ROOT/name; s=p.read_text(); assert 'ReviewPending' in s
 links=[]
 for dest in re.findall(r'\]\(([^)]+)\)',s):
  if '://' in dest: continue
  target=(p.parent/dest.split('#')[0]).resolve(); assert target.exists(),(name,dest)
  links.append({'target':dest,'exists_locally':True})
 scenarios=re.findall(r'^\| ([DTVSLM]\d{2}) \|',s,re.M)
 assert len(scenarios)==len(set(scenarios)),name
 files.append({'path':name,**identity(p),'scenarios':scenarios,'links':links})
result={'package':pkg,'status':'ReviewPending','fixed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':COMMIT,'input_identities_rechecked':check_inputs(),'files':files,'checks':{'new_draft_links':'all relative links resolve locally; reference audit paths use explicit main-workspace mapping','scenario_ids':'unique within activity','manual_semantic_review':'definition, consumer, data, UI, state/return/commit boundaries compared; not external review','runtime':'not executed'}}
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'package':pkg,'files':len(files),'scenario_counts':[len(e['scenarios']) for e in files]},ensure_ascii=False))
