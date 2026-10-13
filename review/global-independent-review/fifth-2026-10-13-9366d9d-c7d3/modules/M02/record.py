from pathlib import Path
import json, hashlib
P=Path(__file__).parent
R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B='9366d9d17aaeac3b4414236468affa650fb3dd27'
RV='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
F='deliverables/final-specification-set/'
def mutate(name,key,entry,identity):
 p=P/(name+'.json'); d=json.loads(p.read_text()); a=d[key]
 a[:]=[x for x in a if x.get(identity)!=entry.get(identity)];a.append(entry)
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def source(path,segments,extent='partial',unreviewed=None,notes=''):
 p=R/path;n=len(p.read_text().splitlines())
 read=[]
 for lo,hi,entry,rules,mapping,result in segments:
  read.append({'lines':[lo,hi],'entries':entry,'semantic_rules':rules,'specification_mapping':mapping,'comparison_result':result})
 if unreviewed is None:
  covered=set(i for x in segments for i in range(x[0],x[1]+1)); missing=[i for i in range(1,n+1) if i not in covered];unreviewed=[]
  for i in missing:
   if unreviewed and unreviewed[-1][1]==i-1:unreviewed[-1][1]=i
   else:unreviewed.append([i,i])
 mutate('reading-coverage','sources',{'path':path,'version':RV,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'line_count':n,'review_extent':extent,'material_availability':'available_text','evidence_level':'static_semantic_comparison' if extent=='full' else 'static_partial_semantic_comparison','segments':read,'unreviewed_intervals':unreviewed,'notes':notes},'path')
def cap(cid,title,status,anchors,maps,comparison,unknowns=[]):
 mutate('source-to-spec','capabilities',{'id':cid,'title':title,'classification':'Generic Kernel','status':status,'support_boundary':'supported_static only; no runtime, real save, host or plugin-combination verification' if status=='supported' else 'static comparison only; incomplete or discrepancy as stated','source_anchors':anchors,'specification_anchors':maps,'comparison':comparison,'unknowns':unknowns},'id')
def spec(path,clauses,extent='full',unreviewed=[]):
 p=Path(path)
 mutate('spec-to-source','specifications',{'path':path,'version':B,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'review_extent':extent,'material_availability':'available_text','evidence_level':'static_semantic_comparison','clauses':[{'section_or_vector':sec,'lines':lines,'source_anchors':anchors,'result':result} for sec,lines,anchors,result in clauses],'effective_supplements':[],'unreviewed_intervals':unreviewed},'path')
def progress(done,next_range,pending):
 p=P/'progress.json';d=json.loads(p.read_text());d['completed_ranges']+=done;d['next_range']=next_range;d['not_reviewed']=pending;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 with (P/'progress.md').open('a') as f:f.write('\n## 检查点\n\n'+ '\n'.join('- '+s for s in done)+'\n\n下一范围：'+next_range+'。\n\n未审：'+'；'.join(pending)+'。\n')
def addsource(path,segments,notes=''):
 d=json.loads((P/'reading-coverage.json').read_text());old=next((x for x in d['sources'] if x['path']==path),None)
 rows=[]
 if old:
  rows=[(*x['lines'],x['entries'],x['semantic_rules'],x['specification_mapping'],x['comparison_result']) for x in old['segments']]
 source(path,rows+segments,'partial',notes=notes)
