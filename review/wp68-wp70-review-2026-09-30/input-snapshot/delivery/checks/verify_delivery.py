"""Static text, JSON, hash, literal-data checks. No gameplay or reference execution."""
from pathlib import Path
import json,hashlib,re,subprocess
ROOT=Path('/Users/dingshinn/Desktop/pokemon-spec-parallel-minigames')
def identity(p):
 b=p.read_bytes();return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
inputs=json.loads((ROOT/'delivery/input-manifest.json').read_text())
ref=Path(inputs['reference_read_only']);commit=inputs['reference_commit']
contexts=[]
for group in ['frozen_inputs','review_authority','handoff_inputs']:
 for e in inputs[group]:
  expected={k:e[k] for k in ['sha256','bytes']}
  for path in [e.get('frozen_source_path',e.get('path')),e['local_copy_path']]:assert identity(Path(path))==expected,path
  contexts.append(Path(e['local_copy_path']).relative_to(ROOT).as_posix())
assert identity(Path(inputs['live_instructions']['path']))=={k:inputs['live_instructions'][k] for k in ['sha256','bytes']}
assert subprocess.check_output(['git','-C',str(ref),'rev-parse','HEAD'],text=True).strip()==commit
assert subprocess.check_output(['git','-C',str(ref),'status','--porcelain'],text=True)==''
source=json.loads((ROOT/'delivery/evidence/source-manifest.json').read_text())
sources={e['path']:e for e in source['entries']}
for name,e in sources.items():
 assert identity(ref/name)=={k:e[k] for k in ['sha256','bytes']}
 assert (ref/name).read_bytes()==subprocess.check_output(['git','-C',str(ref),'show',commit+':'+name])
new=[];scenario_count=0;link_count=0;fixed_times=[]
for package in ['wp68','wp69','wp70']:
 fixed=json.loads((ROOT/f'delivery/checks/{package}-fixed.json').read_text());fixed_times.append(fixed['fixed_at'])
 for e in fixed['files']:
  p=ROOT/e['path'];assert identity(p)=={k:e[k] for k in ['sha256','bytes']}
  text=p.read_text();assert 'ReviewPending' in text and '```' not in text
  scenarios=re.findall(r'^\| ([DTVSLM]\d{2}) \|',text,re.M);assert scenarios==e['scenarios'];scenario_count+=len(scenarios)
  for dest in re.findall(r'\]\(([^)]+)\)',text):assert (p.parent/dest).resolve().is_file();link_count+=1
  new.append(e['path'])
assert fixed_times==sorted(fixed_times)
assert len(new)==9 and scenario_count==108 and link_count==43
# Compare ordered data tables with fixed source numeric literals, without eval.
slot=(ref/'Data/Scripts/017_Minigames/003_Minigame_SlotMachine.rb').read_text()
reels=[[int(n) for n in s.split(', ')] for s in re.findall(r'\[([0-7](?:, [0-7]){21})\]',slot)]
labels=['樱桃','小磁怪','大舌贝','皮卡丘','可达鸭','红7','蓝7','重玩']
slotrows=re.findall(r'^\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$',(ROOT/'specs/ui/wp69-slot-reels.md').read_text(),re.M)
assert len(slotrows)==22
for i,a,b,c in slotrows:assert [a,b,c]==[labels[r[int(i)]] for r in reels]
vf=(ref/'Data/Scripts/017_Minigames/004_Minigame_VoltorbFlip.rb').read_text().split('  def update')[0]
vfsource=[tuple(map(int,row)) for row in re.findall(r'\[(\d+), (\d+), (\d+), (\d+), (\d+)\]',vf)]
vfrows=[tuple(map(int,row)) for row in re.findall(r'^\| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$',(ROOT/'specs/pokemon-rules/wp69-voltorb-layouts.md').read_text(),re.M)]
assert len(vfrows)==len(vfsource)==75
for row,src in zip(vfrows,vfsource):
 lev,idx,v,t,h,one,f,g,prize=row;assert (v,t,h,f,g)==src and one+v+t+h==25 and prize==2**t*3**h
mining=(ref/'Data/Scripts/017_Minigames/006_Minigame_Mining.rb').read_text()
msource=re.findall(r'\[:([A-Z0-9]+), (\d+), (\d+), (\d+), (\d+), (\d+), \[([01, ]+)\]\]',mining)
md=(ROOT/'specs/ui/wp70-mining-data.md').read_text()
mrows=re.findall(r'^\| (\d+) \| ([A-Z0-9]+) \| (\d+) \| (\d+)×(\d+) \| (\d+) \| `([#./]+)` \|$',md,re.M)
assert len(msource)==len(mrows)==61
for row,src in zip(mrows,msource):
 idx,name,weight,w,h,occupied,mask=row;sn,sw,gx,gy,swidth,sheight,pattern=src
 vals=[int(x) for x in pattern.split(', ')];assert (name,weight,w,h)==(sn,sw,swidth,sheight)
 assert mask.replace('/','')==''.join('#' if x else '.' for x in vals) and int(occupied)==sum(vals)
 assert len(mask.split('/'))==int(h) and all(len(r)==int(w) for r in mask.split('/'))
isource=re.findall(r'\[(\d+), (\d+), (\d+), (\d+), \[([01, ]+)\]\]',mining.split('  IRON = [')[1].split('  def update')[0])
irows=re.findall(r'^\| (\d+) \| (\d+)×(\d+) \| (\d+) \| `([#./]+)` \|$',md,re.M)
assert len(isource)==len(irows)==13
for row,src in zip(irows,isource):
 idx,w,h,n,mask=row;gx,gy,sw,sh,pat=src; vals=[int(x) for x in pat.split(', ')];assert (w,h)==(sw,sh) and int(n)==sum(vals)
 assert mask.replace('/','')==''.join('#' if x else '.' for x in vals)
# Independent fixed arithmetic (not a behavioral engine or input simulator).
assert 2026*512+9*32+30==1037630
assert 7%65536==7 and 65543%65536==7
assert (9+9+16+16+32)*4*14//10==459
assert (400+200)*10*40//10==24000
assert 2**7*3**3==3456
assert [144-36,36-9,9-1,1]==[108,27,8,1]
assert [36,81-36,121-81,144-121]==[36,45,40,23]
# JSON and exact output scopes; context JSON must parse too.
json_paths=list(ROOT.rglob('*.json'))
for p in json_paths:json.loads(p.read_text())
proposal_path=ROOT/'delivery/integration-proposal.json'
proposal_checks='not yet present during preparation'
if proposal_path.exists():
 proposal=json.loads(proposal_path.read_text());targets=[];allowed=[]
 for e in proposal['new_artifacts']:
  assert identity(Path(e['local_absolute_path']))=={k:e[k] for k in ['sha256','bytes']}
  targets.append(e['suggested_main_relative_path']);allowed.append(e['local_relative_path'])
 assert len(allowed)==len(set(allowed)) and len(targets)==len(set(targets))
 assert set(allowed)==set(proposal['allowed_import_whitelist'])
 assert not (set(allowed)&set(contexts))
 assert set(new).issubset(allowed)
 assert all(t.startswith('specs/') or t.startswith('review/wp68-wp69-wp70-parallel-b-2026-09-30/') for t in targets)
 proposal_checks='identities, exact whitelist, excluded contexts, unique targets passed'
print(json.dumps({'status':'static-checks-passed-not-external-review','context_copies_checked':len(contexts),'source_records':len(source['entries']),'distinct_sources':len(sources),'new_spec_files':len(new),'scenario_count':scenario_count,'relative_links':link_count,'json_files_parsed':len(json_paths),'ordered_data_rows':{'slot':22,'voltorb':75,'mining_items':61,'mining_iron':13},'package_fixed_time_order':fixed_times,'integration_proposal':proposal_checks},ensure_ascii=False,indent=2))
