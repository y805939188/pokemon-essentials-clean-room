#!/usr/bin/env python3
"""Retain all original183 obligations; distinguish expansions and retired history."""
from pathlib import Path
import hashlib,json,subprocess
O=Path(__file__).resolve().parent;R=O.parents[1];S='planning/implementation-routing/r8-20261017/'
C='7ed3e0554ac24339a7e61cab152f628037111644';I='d62b41f4d620e50bb04c80a7505374bd284d8210'
def blob(c,p):return subprocess.check_output(['git','show',c+':'+p],cwd=R)
a=json.loads(blob(I,S+'routing-manifest.json'));m=json.loads(blob(C,S+'routing-manifest.json'));active={x['feature_id']:x for x in m['features']};retired={x['feature_id']:x for x in m['retired_features']};docs={x['document_id']:x for x in m['documents']};metadata={x['metadata_id']:x for x in m['metadata_records']};rows=[]
for f in a['features']:
 if not f['upstream']['batches']:continue
 fid=f['feature_id'];old=f['upstream'];cur=(active|retired)[fid];up=cur['upstream']
 assert old['binding_basis']==up['binding_basis'] and old['authority']==up['authority']
 assert set(old['batches'])<=set(up['batches']) and set(old['required_ids'])<=set(up['required_ids'])
 exact=all(old[k]==up[k]for k in ['binding_basis','batches','required_ids','authority'])
 row={'feature_id':fid,'original_binding':old,'current_binding':up,'original_obligations_retained':True,'binding_identity_exactly_equal':exact,'current_state':'active'if fid in active else'retired'}
 if fid in active:
  assert up['status']=='已回填ACCEPTED源规格；去向待独立复审' and up['accepted_events']
  row['current_disposition']='ACCEPTED_SOURCE_BOUND_TARGET_REVIEW_SEPARATE'
 else:
  assert up==old and cur['retirement']['metadata_record_id']in metadata
  d=docs[cur['document_id']];assert d['upstream']['status']=='已回填ACCEPTED源规格；去向待独立复审' and d['upstream']['accepted_events']
  assert d['current_applicability']['snapshot_commit']=='5f87743293290de2e219ecdd6c19e88280f60c9a'
  row.update(current_disposition='HISTORICAL_RETIRED_PENDING_LABEL_PRESERVED_CURRENT_DOCUMENT_ACCEPTED',retirement=cur['retirement'],current_document_upstream=d['upstream'],current_document_applicability=d['current_applicability'])
 rows.append(row)
assert len(rows)==183 and sum(not x['binding_identity_exactly_equal']for x in rows)==8 and sum(x['current_state']=='retired'for x in rows)==3
out={'original':I,'candidate':C,'count':183,'all_original_obligations_retained':True,'exact_binding_identity_fields':175,'expanded_with_original_subset_retained':8,'active_original_rows_currently_bound':180,'retired_complete_history_with_current_document_bound':3,'rows':rows,'qualification':'230 current active binding rows pending0/partial0 does not rewrite the three complete retired original objects or imply CLOSED.'}
(O/'evidence/original183-bindings.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='rows'}))
