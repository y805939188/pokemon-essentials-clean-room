"""Record exact fresh original-comparison evidence; no semantic verdict from text equality."""
from current_evidence import *
formal_paths=subprocess.check_output(['git','-C',str(ROOT),'ls-tree','-r','--name-only',B,'deliverables/final-specification-set']).decode().splitlines()
byname={Path(p).name:p for p in formal_paths if '/test-catalog/' not in p}
byname['wp16-pre-battle-transitions-appendix.md']='deliverables/final-specification-set/engine-overworld/wp16-pre-battle-transitions.md'
out=[]
reviewed_modules={'M01','M02','M03','M04','M05','M06','M07','M08','M09','M10','M11','M12B','C00'}
def add(module,name,pointer,record,original=None,formal=None,extent=None):
 p=HERE.parent/module/name;raw=p.read_bytes();original=original or record.get('path',record.get('original'))
 if not original or not original.startswith('specs/'):return
 formal=formal or record.get('formal',record.get('formal_path',record.get('current_counterpart',record.get('current_successor',record.get('comparison_target'))))) or byname.get(Path(original).name)
 ext=extent or record.get('review_extent') or ('full' if record.get('range_review_complete') or record.get('full_read_lines') else 'partial')
 comparisons={k:v for k,v in record.items() if k in ['semantic_ranges','semantic_segments','judgment','special_dispositions','distinct_checks','comparison','unique_fact_assessment','specific_dispositions','unique_fact_dispositions','substantive_unique_loss_conclusion','semantic_disposition','unique_fact_disposition','result','method','unreviewed_comparison_ranges','semantic_compared_ranges','physical_read_ranges_new','qualified_exact_reuse','comparisons']}
 if not comparisons and record.get('sections'):comparisons={'section_results':[{'lines':s.get('lines'),'comparison_result':s.get('comparison_result'),'section':s.get('section')} for s in record['sections']]}
 if not comparisons and record.get('clauses'):comparisons={'clause_result_classes':list(dict.fromkeys(str(s.get('result')) for s in record['clauses']))}
 out.append({'id':module+'-ORIGINAL-'+Path(original).stem,'original':original,'original_version':B,'current_formal':formal,'primary_reviewer':module,'primary_review_extent':ext,'REG_review_extent':'fresh_detailed_comparison_evidence_review; direct original reads separately logged in REG reading-coverage','material_availability':'available_text','evidence_level':'PRIMARY_ORIGINAL_CURRENT_STATIC_COMPARISON','primary_evidence':{'path':str(p.relative_to(ROOT)),'file_sha256':digest(raw),'pointer':pointer,'record_sha256':digest(record)},'comparison_fields':comparisons,'REG_comparison_fields_reviewed':module in reviewed_modules,'status':'supported' if ext=='full' and module in reviewed_modules else 'not_reviewed','boundary':'Only original-to-current fact disposition; no transfer of old approval or arbitrary architecture. Unfinished primary ranges remain not_reviewed.'})
# M01 primary originals only, foreign projections belong their domain reviewer.
m='M01';name='reading-coverage.json';d=json.loads((HERE.parent/m/name).read_text())
for i,r in enumerate(d['specifications']):
 if r.get('path','').startswith('specs/kernel/'):add(m,name,f'/specifications/{i}',r)
# M02 per-clause companion comparisons, including stats qualified unknown writers.
m='M02';name='spec-to-source.json';d=json.loads((HERE.parent/m/name).read_text())
for i,r in enumerate(d['specifications']):
 if r['path'].startswith('specs/'):add(m,name,f'/specifications/{i}',r)
for m,name,key in [('M03','spec-to-source.json','original_draft_review'),('M04','original-reconciliation.json','originals'),('M07','spec-to-source.json','original_draft_checks'),('M08','original-comparison.json','files'),('M09','spec-to-source.json','original_draft_disposition'),('M10','spec-to-source.json','original_comparison'),('M11','original-range-comparison.json','records'),('M12B','original-comparison.json','records')]:
 p=HERE.parent/m/name
 if not p.exists():continue
 d=json.loads(p.read_text())
 for i,r in enumerate(d[key]):add(m,name,f'/{key}/{i}',r,extent='full' if m=='M03' else None)
m='M05';name='spec-to-source.json';d=json.loads((HERE.parent/m/name).read_text())
for i,r in enumerate(d['specifications']):
 if r['path'].startswith('specs/'):
  ranges=[s['lines'] for s in r.get('sections',[])];covered={x for a,b in ranges for x in range(a,b+1)};n=r.get('line_count',len(lines(r['path'])));ext='full' if all(i in covered for i in range(1,n+1)) else 'partial'
  add(m,name,f'/specifications/{i}',r,extent=ext)
m='M06';name='spec-to-source.json';d=json.loads((HERE.parent/m/name).read_text())
for i,r in enumerate(d['specifications']):
 if r.get('original_comparison'):add(m,name,f'/specifications/{i}/original_comparison',r['original_comparison'],formal=r['path'],extent='full')
m='C00';name='reading-coverage.json';dd=json.loads((HERE.parent/m/name).read_text())
for i,r in enumerate(dd['records']):
 if r.get('path')=='specs/demo/wp01-baseline-and-evidence-scope.md':add(m,name,f'/records/{i}',r,formal='deliverables/final-specification-set/scope-statement.md')
save('original-comparison-joins.json',{**BASE,'complete':all(r['status']!='not_reviewed' for r in out),'method':'Read actual fresh per-range/difference dispositions and current receiver references. Exact text-match indexes are addresses only. Formal B5 governs superseded old statements; retired administrative histories retain fixed qualification.','records':out,'pending':[{'path':r['original'],'primary_evidence':r['primary_evidence'],'status':'not_reviewed','reason':'Original comparison ranges not fully closed in available primary artifact; material is available.'} for r in out if r['status']=='not_reviewed']})
print('Original comparison records',len(out),'pending',[(r['primary_reviewer'],r['original']) for r in out if r['status']=='not_reviewed'])
