from pathlib import Path
import json, hashlib, datetime
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[4]
REF=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
B='9366d9d17aaeac3b4414236468affa650fb3dd27'
def load(name): return json.loads((ROOT/(name+'.json')).read_text())
def save(name,data): (ROOT/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def source(path,segments,role='primary'):
    d=load('reading-coverage'); records=d['sources']; q=next((x for x in records if x['path']==path),None)
    txt=(REF/path).read_bytes(); total=len(txt.splitlines())
    if q is None:
        q={'path':path,'version':R,'sha256':hashlib.sha256(txt).hexdigest(),'line_count':total,'role':role,'material_availability':'available','evidence_level':'static_semantic_review','semantic_segments':[]};records.append(q)
    for x in segments:
        a,b,entry,rules,targets,result=x
        q['semantic_segments'].append({'lines':[a,b],'entries':entry,'rules_reviewed':rules,'spec_targets':targets,'comparison_result':result,'execution_status':'not_executed'})
    read=set()
    for x in q['semantic_segments']: read.update(range(x['lines'][0],x['lines'][1]+1))
    missing=[n for n in range(1,total+1) if n not in read]; intervals=[]
    for n in missing:
        if intervals and intervals[-1][1]+1==n: intervals[-1][1]=n
        else: intervals.append([n,n])
    q['unreviewed_intervals']=intervals;q['review_extent']='full' if not intervals else 'partial';save('reading-coverage',d)
def capability(id,title,status,source_anchors,spec_anchors,result,shared=None):
    d=load('source-to-spec');q={'id':id,'title':title,'status':status,'evidence_level':'supported_static' if status=='supported' else 'static_semantic_review','support_boundary':'Fixed R source and B5 text only; no reference, model, host or demo execution.','source_anchors':source_anchors,'spec_anchors':spec_anchors,'comparison_result':result,'shared_contract':shared}; d['capabilities']=[x for x in d['capabilities'] if x['id']!=id]+[q];save('source-to-spec',d)
def spec(path,segments,kind='formal'):
    d=load('spec-to-source');q=next((x for x in d['specifications'] if x['path']==path),None)
    if q is None: q={'path':path,'version':B,'kind':kind,'material_availability':'available','sections':[],'effective_supplements':[]};d['specifications'].append(q)
    for a,b,section,anchors,result in segments:q['sections'].append({'lines':[a,b],'section':section,'source_anchors':anchors,'comparison_result':result,'evidence_level':'static_semantic_review'})
    save('spec-to-source',d)
def checkpoint(done,next_ranges):
    d=load('progress');d['completed_ranges']+=done;d['next_actual_ranges']=next_ranges;d['complete']=False;d['updated_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();save('progress',d)
    (ROOT/'progress.md').write_text('# M05 进度\n\ncomplete: false；模型实际参数 UNVERIFIED；仅静态审查。\n\n已完成有限语义范围：\n'+''.join('- '+x+'\n' for x in d['completed_ranges'])+'\n下一实际范围：\n'+''.join('- '+x+'\n' for x in next_ranges))
