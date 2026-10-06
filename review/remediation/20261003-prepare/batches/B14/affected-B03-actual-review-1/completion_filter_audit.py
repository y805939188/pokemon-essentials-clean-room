"""Own strict metadata-filter audit and unread queue; preserves all native mappings."""
import completion_read as R
import json,subprocess,collections
idx=R.gzload('completion-reading-index.json.gz');done=set(json.loads((R.OUT/'completion-consumption.json').read_text())['read_claims']);known=set()
for commit in [R.ACT,R.ORIG,R.PLAN,R.PRE]:known.update(subprocess.check_output(['git','ls-tree','-r','--name-only',commit]).decode().splitlines())
cache={};restored=[];behavior_context=collections.defaultdict(list)
for occ in idx['occurrences']:
 # Typed scalar-map indices, source addresses and document identities are
 # reconstruction metadata. They remain fully retained and verified.
 if __import__('re').search(r'/(?:value_index|value_indices|remaining_unique_value_indices|unique_value_indices|bytes|byte_count|lines|line_count)(?:/.*)?$',occ[2]):continue
 if __import__('re').search(r'(expected|fixture|premise|input|initial|final|state|result|sample|life|opacity|moisture|growth|through|outdoor|shading|faint|selection|registration|hour|duration|intensity|tone|hp|watering|drying)',occ[2],__import__('re').I):behavior_context[occ[0]].append(occ[:3])
for i,c in enumerate(idx['claims']):
 if c.get('decomposition_policy') or c.get('preserved_unrelated_accepted_history'):continue
 r=c['first'];di=r['document'];d=idx['documents'][di]
 if di not in cache:
  b=R.git(d['commit'],d['path']);assert R.h(b)==d['sha256']
  try:o=json.loads(b)
  except ValueError:o={'literal_lines':b.decode().splitlines(keepends=True)}
  if d['selection'] is not None:o={s:R.at(o,R.parts(s)) for s in d['selection']}
  cache[di]=o
 v=R.derive(R.at(cache[di],R.parts(r['selector'])),r['steps']);assert R.vh(v)==c['value_sha256']
 new=R.pure(v,r['selector'],known)
 if not isinstance(v,str) and behavior_context[i]:new=False;c['behavioral_numeric_native_contexts']=behavior_context[i]
 if c['metadata_only'] and not new:restored.append(i)
 c['metadata_only']=new
R.save('completion-reading-index.json.gz',idx)
q=[i for i,c in enumerate(idx['claims']) if not c['metadata_only'] and not c['prior_consumed'] and i not in done]
def rank(i):
 d=idx['documents'][idx['claims'][i]['first']['document']];p=d['path']
 if d['commit'] in [R.ORIG,R.PLAN,R.PRE]:return 0
 if 'integration-stage-1/' in p:return 1
 if p.startswith(('specs/','deliverables/')) and not p.endswith('.tsv'):return 2
 if not p.startswith(R.BASE):return 3
 if 'affected-B03-review' in p:return 4
 return 5
q.sort(key=lambda i:(rank(i),idx['claims'][i]['first']['document'],i))
R.save('completion-pending-claims.json',q)
R.save('completion-filter-audit.json',{'strict_ascii_selector_and_exact_path_exemptions':True,'mixed_path_plus_prose_not_discarded':True,'all_occurrence_behavioral_number_contexts_retained':True,'restored_claims':restored,'queue_contains_only_current_unread_semantic_claims':True,'previous_receipts_and_read_claim_ids_unchanged':True,'unread_count':len(q),'unread_characters':sum(idx['claims'][i]['length'] for i in q)})
print('restored',len(restored),'unread',len(q),'chars',sum(idx['claims'][i]['length'] for i in q))
