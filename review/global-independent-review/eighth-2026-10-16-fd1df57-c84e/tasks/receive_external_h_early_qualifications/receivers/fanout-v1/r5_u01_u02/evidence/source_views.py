"""Generate inert fixed-R continuous read ranges, extending overlapping method definitions."""
from pathlib import Path
import json,gzip,re,subprocess,hashlib,collections
W=Path(__file__).resolve().parents[1];T=W.parents[2];F=T/'delegation/fanout-v1';R=Path('/workspace/pokemon-essentials');C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
view=json.loads(gzip.decompress((F/'shards/r5_u01_u02/complete-records.json.gz').read_bytes()));sources=collections.defaultdict(list)
for o in view['owned_complete_objects']:
 if o.get('role')!='original_packet_finding':continue
 for kind in ['source_anchors','actual_source']:
  for a in o['expanded_complete_object'].get(kind,[]):
   p=a.get('path');rs=a.get('lines',a.get('range',a.get('ranges')))
   if p and rs:
    if isinstance(rs[0],int):rs=[rs]
    for lo,hi in rs:sources[p].append([lo,hi,o['primary_id']])
# Necessary missing definitions/callers identified from the complete contracts.
for p,rs,ids in [
 ('Data/Scripts/010_Data/001_GameData.rb',[(1,280)],['GR5-M01-021','GR5-JXN-001']),
 ('Data/Scripts/021_Compiler/001_Compiler.rb',[(105,181),(255,293),(384,482),(690,737),(824,834),(872,883),(990,1038)],['GR5-M01-001','GR5-M01-012','GR5-M01-023']),
 ('Data/Scripts/010_Data/002_PBS data/008_Species.rb',[(1,225),(277,327),(373,452)],['GR5-M01-004','GR5-M01-025','GR5-M01-026','GR5-M01-031']),
 ('Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',[(21,70),(283,370),(388,537),(791,928)],['GR5-M01-004','GR5-M01-025','GR5-M01-029']),
 ('Data/Scripts/010_Data/002_PBS data/021_PhoneMessage.rb',[(1,100)],['GR5-M01-023']),
 ('Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb',[(4,65),(174,283),(403,442),(688,727),(792,834)],['GR5-M01-017','GR5-M01-018','GR5-JXN-001']),
 ('Data/Scripts/001_Technical/003_Intl_Messages.rb',[(1,240),(291,471),(481,490),(511,611),(644,669),(752,784)],['GR5-M01-002','GR5-M01-003','GR5-M01-008','GR5-M01-009','GR5-JXN-001']),
 ('Data/Scripts/019_Utilities/001_Utilities.rb',[(1,60),(509,539)],['GR5-JXN-001','GR5-M02-001','GR5-M03-007']),
 ('Data/Scripts/003_Game processing/003_Interpreter.rb',[(1,424)],['GR5-M03-002','GR5-M03-003','GR5-M03-007','GR5-M03-008','GR5-M03-009','GR5-M03-010','GR5-M03-012']),
 ('Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb',[(1,60),(477,506),(577,727),(812,860)],['GR5-M03-013']),
]:
 for a,b in rs:
  for i in ids:sources[p].append([a,b,i])
out=W/'.local/source-pages';out.mkdir(exist_ok=True);records=[];pages=[];page='';pageparts=[]
for p,rs in sources.items():
 raw=subprocess.check_output(['git','-C',str(R),'show',C+':'+p]);lines=raw.decode().splitlines();oid=subprocess.check_output(['git','-C',str(R),'rev-parse',C+':'+p]).decode().strip();spans=[]
 for n,l in enumerate(lines,1):
  m=re.match(r'^(\s*)def\s',l)
  if m:
   indent=m.group(1)
   for j in range(n+1,len(lines)+1):
    if re.match('^'+re.escape(indent)+r'end\b',lines[j-1]):spans.append((n,j));break
 selected=set()
 for a,b,_ in rs:
  selected.update(range(a,min(b,len(lines))+1))
  for lo,hi in spans:
   if lo<=b and hi>=a:selected.update(range(lo,hi+1))
 ranges=[]
 for n in sorted(selected):
  if ranges and ranges[-1][1]==n-1:ranges[-1][1]=n
  else:ranges.append([n,n])
 records.append({'path':p,'commit':C,'git_blob':oid,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'requested_ranges':rs,'actual_ranges':ranges,'method_extension':'same-indentation def/end intervals; inspect boundaries in rendered text','source_static_only':True})
 for lo,hi in ranges:
  for start in range(lo,hi+1,120):
   end=min(start+119,hi);s=f'\nFILE {p} L{start}–{end} (continuous range {lo}–{hi})\n'+'\n'.join(f'{i}: {lines[i-1]}'for i in range(start,end+1))+'\n'
   if len(page)+len(s)>13000 and page:pages.append(page);page=''
   page+=s
if page:pages.append(page)
for i,s in enumerate(pages):(out/f'{i+1:02d}.txt').write_text(s)
(W/'.local/source-range-manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n');print({'files':len(records),'lines':sum(sum(b-a+1for a,b in r['actual_ranges'])for r in records),'pages':len(pages),'credit':0})
