"""Own exact reuse-span correction; keeps earlier annotations and reopens any unsupported value."""
import completion_read as R
import json
idx=R.gzload('completion-reading-index.json.gz');claims=idx['claims'];done=set(json.loads((R.OUT/'completion-consumption.json').read_text())['read_claims']);cache={};vals={};changes=[];reopened=[]
def value(n):
 if n in vals:return vals[n]
 c=claims[n];r=c['first'];di=r['document'];d=idx['documents'][di]
 if di not in cache:
  b=R.git(d['commit'],d['path']);assert R.h(b)==d['sha256']
  try:o=json.loads(b)
  except ValueError:o={'literal_lines':b.decode().splitlines(keepends=True)}
  if d['selection'] is not None:o={s:R.at(o,R.parts(s)) for s in d['selection']}
  cache[di]=o
 v=R.derive(R.at(cache[di],R.parts(r['selector'])),r['steps']);assert R.vh(v)==c['value_sha256'];vals[n]=v;return v
for n,c in enumerate(claims):
 p=c['prior_consumed']
 if not p or p.get('kind')!='exact_body_substring_already_consumed':continue
 parent=p['parent_claim'];v=value(n);body=value(parent);a,z=p['exact_span']
 if type(v)==str and type(body)==str and body[a:z]==v:continue
 assert parent in done or claims[parent]['prior_consumed']
 start=body.find(v) if type(body)==str and type(v)==str else -1
 old=json.loads(json.dumps(p));c['earlier_reuse_annotation']=old
 if start>=0:
  c['prior_consumed']={**p,'exact_span':[start,start+len(v)],'correction':'Child partition inherited whole-parent span; corrected against exact genuinely consumed parent body, with native type/hash/context unchanged.'};changes.append({'claim':n,'earlier':old,'corrected':c['prior_consumed']})
 else:
  c['prior_consumed']=None;reopened.append(n);changes.append({'claim':n,'earlier':old,'corrected':None,'required':'Supplement exact native value before final disposition.'})
R.save('completion-reuse-span-correction.json',{'cause':'Earlier exact table/sentence partitions copied a whole-parent substring annotation onto child spans without adjusting offsets. Native values/order/contexts remained intact.','changes':changes,'unsupported_reopened_claims':reopened,'not_ACT_payload_defect':True,'first_receipt_and_preliminary_snapshots_unchanged':True})
R.save('completion-reading-index.json.gz',idx);q=json.loads((R.OUT/'completion-pending-claims.json').read_text());present=set(q);q.extend(n for n in reopened if n not in done and n not in present);R.save('completion-pending-claims.json',q);print('corrected exact spans',len(changes)-len(reopened),'reopened',len(reopened),'queue',len(q))
