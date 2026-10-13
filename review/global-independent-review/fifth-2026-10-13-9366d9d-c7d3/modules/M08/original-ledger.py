"""Original/current review bookkeeping only; no source or behavior execution."""
import json,hashlib,datetime,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
GCV=ROOT.parent/'GCV/effective-corpus-gap-register.json'
def read(n):return json.loads((ROOT/n).read_text())
def write(n,v):(ROOT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def points(rs):return {n for a,b in rs for n in range(a,b+1)}
def spans(nums):
 out=[]
 for n in sorted(set(nums)):
  if out and out[-1][1]+1==n:out[-1][1]=n
  else:out.append([n,n])
 return out

def initialize():
 g=next(v for v in json.loads(GCV.read_text())['confirmed_gap_groups'] if v['id']=='GCV-E001')
 prior=read('reading-coverage.json');rev=read('spec-to-source.json');src=read('source-to-spec.json')
 x={'schema_version':'gr5.review.v1','module':'M08','task_kind':'bounded_original_comparison_GCV_E001','source_baseline':prior['source_baseline'],'specification_baseline':prior['specification_baseline'],'model_request':prior['model_request'],'execution_status':'NOT_EXECUTED','complete':False,'gcv_input':{'path':str(GCV),'sha256':hashlib.sha256(GCV.read_bytes()).hexdigest(),'record_id':'GCV-E001'},'preserved_denominators':{'primary_source_files':28,'primary_source_lines':21586,'formal_specification_files':len(rev['specifications']),'formal_clause_rows':sum(len(f['clause_mappings']) for f in rev['specifications']),'canonical_rule_records':len(src['capabilities']),'capability_id_set_sha256':hashlib.sha256('\n'.join(sorted(c['id'] for c in src['capabilities'])).encode()).hexdigest()},'navigation_counts_only':{'original_files':14,'original_lines':3854,'qualified_exact_reuse_lines':935,'unclosed_original_lines':2919,'not_feature_or_semantic_coverage_counts':True},'prior_actual_read_audit':{'full_original_reading_claimed':False,'WP48_WP50_rosters':'data-audit.json#/roster_text_crosschecks records exact identity/registration projection only; source-locus and clause-column facts still require comparison','WP44_122_125':'findings.json original link is navigation-only; not promoted to full-row reading','other_originals':'Prior current/source completion never substitutes for original unique-fact disposition'},'files':[],'new_findings':[],'prior_findings_preserved':['GR5-M08-001','GR5-M08-002','GR5-M08-003']}
 for i,f in enumerate(g['files']):
  old=Path(f['path']).read_bytes().splitlines(keepends=True);np=f['qualified_reuse']['formal_path'];new=Path(np).read_bytes().splitlines(keepends=True)
  pairs=[]
  for j,pair in enumerate(f['qualified_reuse']['pairs']):
   a,b=pair['original_lines'];c,d=pair['formal_lines'];v=b''.join(old[a-1:b]);w=b''.join(new[c-1:d]);assert v==w,(f['path'],pair);assert hashlib.sha256(v).hexdigest()==pair['sha256']
   spec=next(s for s in rev['specifications'] if s['path']==np)
   ids=[q['source_anchor_group_ref'] for q in spec['clause_mappings'] if c<=q['lines'][0]<=d]
   pairs.append({**pair,'formal_comparison_group_refs':list(dict.fromkeys(ids)),'comparison':'Exact same bytes qualified against the previously fully read/current-semantic-reviewed range; headers/layout only do not become behavior rules.'})
  exact=points([q['original_lines'] for q in pairs]);remaining=points(f['remaining_comparison_ranges']);assert exact|remaining==set(range(1,f['line_count']+1)) and not exact&remaining
  x['files'].append({'id':'ORIG-'+str(i+1).zfill(2),'path':f['path'],'version':f['version'],'line_count':f['line_count'],'sha256':f['sha256'],'formal_path':np,'formal_version':f['version'],'formal_sha256':f['qualified_reuse']['formal_sha256'],'material_availability':'available','review_extent':'partial','physical_read_ranges_new':[],'semantic_compared_ranges':spans(exact),'qualified_exact_reuse':pairs,'prior_literal_projections':f['qualified_literal_comparisons'],'unreviewed_comparison_ranges':f['remaining_comparison_ranges'],'comparisons':[]})
 write('original-comparison.json',x)

def show(index,start=1,end=99999):
 x=read('original-comparison.json');f=x['files'][index];ls=Path(f['path']).read_text().splitlines();missing=points(f['unreviewed_comparison_ranges'])
 print(f['id'],f['path'],'range',start,end)
 for n in range(start,min(end,len(ls))+1):
  if n in missing:print(str(n)+'\t'+ls[n-1])
 print('END RANGE')

def compare(index,start,end,category,summary,receivers=None,details=None):
 x=read('original-comparison.json');f=x['files'][index];missing=points(f['unreviewed_comparison_ranges']);actual=sorted(n for n in range(start,end+1) if n in missing)
 if not actual:raise ValueError('Range already closed or exact-reused')
 allowed={'received','sanitized_source_or_implementation_exclusion','historical_or_superseded','mixed_received_and_sanitized','unreceived_correct_fact','existing_confirmed_gap','metadata_or_layout'}
 assert category in allowed
 cid=f['id']+'-C'+str(len(f['comparisons'])+1).zfill(3)
 record={'id':cid,'original_ranges':spans(actual),'physical_read_mode':'actual_text_read_this_followup','disposition':category,'comparison':summary,'current_receivers':receivers or [],'evidence_level':'original_and_current_static_semantic_comparison','execution_status':'NOT_EXECUTED','additional_details':details or []}
 f['comparisons'].append(record);f['physical_read_ranges_new']=spans(points(f['physical_read_ranges_new'])|set(actual));f['semantic_compared_ranges']=spans(points(f['semantic_compared_ranges'])|set(actual));f['unreviewed_comparison_ranges']=spans(missing-set(actual));f['review_extent']='full' if not f['unreviewed_comparison_ranges'] else 'partial';write('original-comparison.json',x)

def receiver(index,a,b,kind='body'):
 f=read('original-comparison.json')['files'][index];return {'path':f['formal_path'],'version':f['formal_version'],'lines':[a,b],'kind':kind}
def test(path,a,b):return {'path':'deliverables/final-specification-set/test-catalog/'+path,'version':read('original-comparison.json')['specification_baseline']['commit'],'lines':[a,b],'kind':'vectors_and_common_fixture'}

def named_transfer(index,start,end,summary,existing_gap_names=None):
    """Index table rows only AFTER they were substantively read and compared."""
    f=read('original-comparison.json')['files'][index]
    old=Path(f['path']).read_text().splitlines();new=Path(f['formal_path']).read_text().splitlines()
    for n in range(start,end+1):
        if n not in points(read('original-comparison.json')['files'][index]['unreviewed_comparison_ranges']):continue
        names=re.findall(r'`([A-Za-z][A-Za-z0-9_]*)`',old[n-1])
        if not names:raise ValueError('No explicit identity on original line '+str(n))
        hits=[i for i,l in enumerate(new,1) if any(re.search(r'(?<![A-Za-z0-9_])'+re.escape(k)+r'(?![A-Za-z0-9_])',l) for k in names)]
        if not hits:raise ValueError('No current literal anchor '+str(n)+' '+str(names))
        gap=bool(set(names)&set(existing_gap_names or []))
        compare(index,n,n,'existing_confirmed_gap' if gap else 'mixed_received_and_sanitized',summary,
                [receiver(index,i,i,'table_or_named_clause') for i in hits],['Identities: '+', '.join(names),'Literal lookup indexes the completed substantive comparison; it is not its proof.'])
