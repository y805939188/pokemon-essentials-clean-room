import review_state as s
from pathlib import Path
import datetime

def upsert(filename,key,rows,id_key):
 d=s.read(filename)
 for row in rows:
  existing=next((i for i,x in enumerate(d[key]) if x.get(id_key)==row.get(id_key)),None)
  if existing is None:d[key].append(row)
  else:d[key][existing]=row
 s.write(filename,d)

def source(path, ranges, rules, extent='partial', pending=None):
 s.covered(path,ranges,rules)
 d=s.read('reading-coverage.json'); e=next(x for x in d['sources'] if x['path']==path)
 e['reading_extent']='full' if e.get('read_ranges')==[[1,e['line_count']]] else 'partial'
 e['review_extent']=extent
 if pending is not None:e['unreviewed_semantic_obligations']=pending
 s.write('reading-coverage.json',d)

def spec(path,ranges,rule):
 s.covered(path,ranges,[dict(lines=ranges[0],entry_or_rule=rule,comparison='Current B5 content reviewed for stated projection; status on individual mappings, not historical approval.')],'specifications')

def cap(id,path,ranges,fact,specs,status='partial',pending=None):
 row=dict(capability_id=id,source_anchors=[dict(path=path,version=s.R,lines=x) for x in ranges],spec_anchors=specs,status=status,evidence_level='static_semantic_comparison',comparison=fact,supported_boundary='supported_static for described source/data interface; no host/runtime execution' if status=='supported' else None,pending=pending or [])
 upsert('source-to-spec.json','capabilities',[row],'capability_id')

def progress(text,next_range):
 s.progress(next_range,text);d=s.read('progress.json');d['checkpoint_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();s.write('progress.json',d)
 with (s.OUT/'progress.md').open('a') as f:f.write('\n## '+d['checkpoint_at']+'\n\n'+text+'\n\n下一实际范围：'+next_range+'。complete=false；继续推进。\n')
