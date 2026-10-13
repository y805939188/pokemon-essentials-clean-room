from pathlib import Path
import json,re,collections
P=Path(__file__).parent
names=['reading-coverage','source-to-spec','spec-to-source','findings','shared-interfaces','progress']
D={x:json.loads((P/(x+'.json')).read_text()) for x in names}
checks=[]
def check(name,ok,detail=None):checks.append({'check':name,'passed':bool(ok),'detail':detail})
for n,d in D.items():check(n+' schema_version',d.get('schema_version')=='gr5.review.v1')
req='id title module severity disposition status reviewer category source_baseline specification_baseline source_anchors spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change affected_files shared_contracts acceptance_criteria dependencies related_capabilities related_findings root_cause_group priority batch_owner history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution'.split()
f=D['findings']['findings'];check('five candidate IDs unique',len(f)==5 and len({x['id'] for x in f})==5)
for x in f:
 check(x['id']+' required fields',set(req)<=x.keys(),sorted(set(req)-x.keys()))
 check(x['id']+' candidate only',x['status']=='candidate_pending_independent_counterevidence' and x['review_resolution']['final_required_revision_signed'] is False)
 check(x['id']+' severity/disposition',x['severity'] in ['P1','P2','P3'] and x['disposition'] in ['required','optional','no_required_revision','unresolved'])
 check(x['id']+' no must-execute action',x['acceptance_criteria']['must_execute']==[])
# Correct the per-capability review label to the required enum, retaining its scoped boundary.
p=P/'source-to-spec.json'
for x in D['source-to-spec']['capabilities']:
 if x.get('review_extent')=='full_for_named_capability_scope':x['review_extent']='full';x['review_extent_boundary']='named capability and source ranges only'
p.write_text(json.dumps(D['source-to-spec'],ensure_ascii=False,indent=2)+'\n')
capids={x['id'] for x in D['source-to-spec']['capabilities']}
check('all candidate capabilities resolve',all(set(x['related_capabilities'])<=capids for x in f))
si=D['shared-interfaces']['interfaces'];allsi={v for x in si for v in [x['id']]+x.get('aliases',[])}
check('shared IDs and aliases unique',len(allsi)==sum(1+len(x.get('aliases',[])) for x in si))
check('all finding shared contracts resolve',all(set(x['shared_contracts'])<=allsi for x in f))
coverage=D['reading-coverage']['sources'];check('source paths unique',len(coverage)==len({x['path'] for x in coverage}))
allowed={'full','partial','inventory_only','unread','unreadable'}
check('source review_extent enum',all(x['review_extent'] in allowed for x in coverage))
check('source exact versions',all(x['version']=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' and len(x.get('sha256',''))==64 for x in coverage))
primary=[x for x in coverage if x.get('review_scope_kind') in ['primary','primary_mixed_file']]
check('primary source semantic completion',len(primary)==26 and all(x['semantic_comparison_complete_for_owned_ranges'] for x in primary))
R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
uncov=[]
for x in primary:
 covered={i for s in x['segments'] for i in range(s['lines'][0],s['lines'][1]+1)}
 lines=(R/x['path']).read_text().splitlines()
 for a,b in x['owned_ranges']:
  for i in range(a,b+1):
   if i not in covered and lines[i-1].strip() and not lines[i-1].lstrip().startswith('#'):uncov.append((x['path'],i))
check('primary meaningful owned lines accounted for',not uncov,uncov)
specs=D['spec-to-source']['specifications'];formal=[x for x in specs if x['path'].startswith('deliverables/final-specification-set/generic-kernel/') and x['review_extent']=='full']
check('seven primary formal specs mapped',len(formal)==7)
for x in formal:
 lines=Path(x['path']).read_text().splitlines();covered={i for c in x['clauses'] for i in range(c['lines'][0],c['lines'][1]+1)}
 gaps=[i for i,t in enumerate(lines,1) if t.strip() and not re.fullmatch(r'[| :\-]+',t) and i not in covered]
 check(Path(x['path']).name+' every meaningful line mapped',not gaps,gaps)
t=next(x for x in specs if x['path'].endswith('test-catalog/generic-kernel-wp05-06-07-08-09-10.md'))
check('shared catalog is partial and excludes WP08',t['review_extent']=='partial' and t['unreviewed_intervals']==[[110,154]] and all(not c['section_or_vector'].startswith('LZ') for c in t['clauses']))
cnt=collections.Counter(re.match(r'[A-Z]+',c['section_or_vector'])[0] for c in t['clauses'])
check('110 assigned vectors accounted for',len(t['clauses'])==110 and len({x['section_or_vector'] for x in t['clauses']})==110,dict(cnt))
st=next(x for x in formal if x['path'].endswith('wp06-stats-directory.md'));fields=[c for c in st['clauses'] if c['unit_kind']=='table_row' and re.match(r'\| [a-z_]+ \|',c['current_unit'])]
check('74 stats field rows unique',len(fields)==74 and len({x['section_or_vector'] for x in fields})==74)
check('all primary units carry source anchors',all(c['source_anchors'] for x in formal for c in x['clauses']))
check('all supported capabilities explicitly static',all('supported_static' in x['support_boundary'] for x in D['source-to-spec']['capabilities'] if x['status']=='supported'))
result={'schema_version':'gr5.review.v1','kind':'artifact_integrity_checks_only','reference_or_behavior_execution':False,'checks':checks,'passed':all(x['passed'] for x in checks),'counts':{'source_paths':len(coverage),'primary_source_paths':len(primary),'formal_primary_specs':len(formal),'assigned_test_vectors':len(t['clauses']),'stats_fields':len(fields),'capabilities':len(capids),'shared_canonical_contracts':len(si),'candidates':len(f)},'note':'These checks validate record integrity and accounting, not source semantics or executed behavior. Source semantics were read and compared before artifact generation.'}
(P/'artifact-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'counts':result['counts'],'failed':[x for x in checks if not x['passed']]},ensure_ascii=False,indent=2))
