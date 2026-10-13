"""Review bookkeeping only. No reference code or behavioral model execution."""
import json,sys,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def read(n): return json.loads((ROOT/n).read_text())
def write(n,x): (ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n")
def complement(n,intervals):
 used=set()
 for a,b in intervals: used.update(range(a,b+1))
 spans=[];start=None
 for i in range(1,n+2):
  missing=i<=n and i not in used
  if missing and start is None:start=i
  elif not missing and start is not None:spans.append([start,i-1]);start=None
 return spans

def source(path,ranges):
 x=read('reading-coverage.json'); f=next(y for y in x['sources'] if y['path'].endswith(path))
 for v in ranges:
  a,b,entry,rules,specs,status=v
  f['semantic_ranges'].append({'lines':[a,b],'entries_and_rules':entry,'semantic_comparison':rules,'specification_anchors':specs,'capability_status':status,'evidence_level':'static_source_and_contract_comparison' if specs else 'static_source_only','supported_boundary':'supported_static: only the named rule, baseline, range and declared preconditions; no runtime or uninspected dependencies' if status=='supported' else None})
 f['unreviewed_ranges']=complement(f['line_count'],[z['lines'] for z in f['semantic_ranges']]);f['review_extent']='partial' if f['unreviewed_ranges'] else 'full';f['evidence_level']='static_semantic_review';f['review_extent_definition']='Full means every source line in this file has an explicit semantic disposition; it does not sign off all callers, dependencies or specification coverage.'
 for e in f['effect_entry_inventory']:
  hits=[z for z in f['semantic_ranges'] if z['lines'][0]<=e['line']<=z['lines'][1]]
  if hits:e.update(review_extent='full',semantic_comparison=hits[-1]['semantic_comparison'],specification_anchors=hits[-1]['specification_anchors'],capability_status=hits[-1]['capability_status'],evidence_level=hits[-1]['evidence_level'])
 write('reading-coverage.json',x)

def capability(cid,name,source_ranges,specs,rules,status='supported',unknowns=None):
 x=read('source-to-spec.json');x['capabilities'].append({'id':cid,'name':name,'capability_status':status,'evidence_level':'static_source_and_contract_comparison','supported_boundary':'supported_static: fixed R/B5 only; no execution; scope limited to stated rules and anchors' if status=='supported' else None,'source_anchors':source_ranges,'specification_anchors':specs,'rules_checked':rules,'unknowns':unknowns or [],'shared_contract_identity':cid,'consumer_projections':[]});write('source-to-spec.json',x)

def spec(path,a,b,result,sources,status='supported'):
 for name in ['reading-coverage.json','spec-to-source.json']:
  x=read(name);f=next(y for y in x['specifications'] if y['path'].endswith(path));f.setdefault('semantic_ranges',[]).append({'lines':[a,b],'comparison':result,'source_mappings':sources,'capability_status':status,'supported_boundary':'supported_static; no execution and no inference beyond named ranges' if status=='supported' else None});f['unreviewed_ranges']=complement(f['line_count'],[v['lines'] for v in f['semantic_ranges']]);f['review_extent']='partial' if f['unreviewed_ranges'] else 'full';f['evidence_level']='static_semantic_review'
  for u in f['units']:
   if a<=u['lines'][0] and u['lines'][1]<=b:u.update(review_extent='full',capability_status=status,source_mappings=sources,comparison=result)
  write(name,x)

def progress(text,next_range):
 x=read('progress.json');x['updated_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();x['last_completed_finite_range']=text;x['next_actual_range']=next_range;x['status']='in_progress';x['complete']=False;write('progress.json',x)
 (ROOT/'progress.md').write_text('# M08 进度\n\n状态：in_progress；不是 complete。实际模型参数 UNVERIFIED。仅静态语义审查。\n\n'+text+'\n\n下一实际范围：'+next_range+'\n\n逐段比较和未审区间见 reading-coverage.json。全表仅已记录语义范围可计审核，目录/自动命中不计。没有签署最终必修，没有引用历史 PASS 作为本轮证据。\n')
