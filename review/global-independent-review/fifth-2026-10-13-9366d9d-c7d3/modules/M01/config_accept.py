import review_ops as o
s=o.s

def paths():
 d=s.read('configuration-consumer-ledger.json');return sorted({x['path'] for r in d['definitions'] for x in r['occurrences'] if x['lexical_classification']=='candidate_code_requires_semantic_review'})
def accept(rows):
 ps=paths();d=s.read('configuration-consumer-ledger.json')
 try:out=s.read('configuration-branch-reviews.json')
 except FileNotFoundError:out={'schema_version':'gr5.review.v1','module':'M01','source_baseline':s.R,'branches':[]}
 for fi,rs,meaning,projection in rows:
  p=ps[fi-1]; key=f'{p}:{rs}'
  relevant=[]
  for r in d['definitions']:
   for x in r['occurrences']:
    if x['path']==p and any(a<=x['line']<=z for a,z in rs):
     if x['lexical_classification']=='candidate_code_requires_semantic_review':
      x['semantic_review']='source_semantics_reviewed_contract_pending';x['rule_summary']=meaning;x['consumer_projection']=projection
      relevant.append({'key':r['key'],'line':x['line']})
  row={'id':key,'path':p,'source_version':s.R,'lines':rs,'setting_occurrences':relevant,'rule_summary':meaning,'consumer_projection':projection,'status':'partial','evidence_level':'static_source_semantics','pending':'Read/compare all current relevant domain clauses and any unique original/supplement rules; no support inferred from heading or lexical match.'}
  if not any(x['id']==key for x in out['branches']):out['branches'].append(row)
  o.source(p,rs,[{'lines':r,'entry_or_rule':'Configuration consumer branch','source_fact':meaning,'comparison':projection+'; current contract comparison pending per branch ledger.'} for r in rs])
 s.write('configuration-consumer-ledger.json',d);s.write('configuration-branch-reviews.json',out)
 print('Saved bounded branch reviews',len(rows),'total',len(out['branches']))
