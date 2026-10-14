import json,collections,itertools,datetime
from pathlib import Path
b=Path(__file__).parent;p=json.loads((b/'handoff__batch-assignment.json').read_text());dg=json.loads((b/'handoff__dependency-graph.json').read_text());fg=json.loads((b/'handoff__file-conflict-graph.json').read_text());issues=[];expected={}
for a,c in itertools.combinations(p['batches'],2):
 paths=sorted(set(a['candidate_formal_paths'])&set(c['candidate_formal_paths']))
 if paths:expected[(a['id'],c['id'])]=paths
actual={tuple(sorted([x['from'],x['to']])):sorted(x['paths'])for x in fg['edges']}
for pair,paths in expected.items():
 if actual.get(pair)!=paths:issues.append({'type':'FILE_CONFLICT_INCIDENCE_MISMATCH','pair':pair,'expected':paths,'actual':actual.get(pair)})
for pair,paths in actual.items():
 if pair not in expected:issues.append({'type':'SPURIOUS_FILE_CONFLICT','pair':pair,'paths':paths})
# No author dependency cycle; verify normal staged DAG including receivers.
edge=dg['edges'];nodes=set();adj=collections.defaultdict(set);indeg=collections.Counter()
for e in edge:
 a=e['from'];c=e['to'];nodes.update([a,c])
 if c not in adj[a]:adj[a].add(c);indeg[c]+=1
queue=collections.deque(n for n in nodes if indeg[n]==0);ordered=[]
while queue:
 n=queue.popleft();ordered.append(n)
 for c in adj[n]:
  indeg[c]-=1
  if indeg[c]==0:queue.append(c)
if len(ordered)!=len(nodes):issues.append({'type':'DEPENDENCY_CYCLE','remaining':[n for n in nodes if indeg[n]>0]})
roles=[]
receivers=collections.defaultdict(list)
for q in p['batches']:
 a=q['author']['logical_id'];r=q['reviewer']['logical_id'];roles += [a,r]
 if a==r:issues.append({'type':'AUTHOR_REVIEWER_NOT_SEPARATE','batch':q['id']})
 if not any(e['from']==a and e['to']==r and e['kind']=='candidate_review'for e in edge):issues.append({'type':'MISSING_CANDIDATE_REVIEW_EDGE','batch':q['id']})
 if not any(e['from']==r and e['to']=='R6-I'and e['kind']=='candidate_acceptance'for e in edge):issues.append({'type':'MISSING_INTEGRATION_ACCEPTANCE_EDGE','batch':q['id']})
 if q['blocking_author_dependencies']:issues.append({'type':'AUTHOR_BLOCKING_REQUIRES_MANUAL_REVIEW','batch':q['id'],'deps':q['blocking_author_dependencies']})
 if not q['candidate_only_write_directory'].endswith(q['id']+'/'):issues.append({'type':'CANDIDATE_DIR_NONUNIQUE','batch':q['id']})
 if 'NOT_STARTED'not in q['state']:issues.append({'type':'STATE_REQUIRES_MANUAL_CONFIRMATION','batch':q['id'],'state':q['state']})
 contracts={v['id']:v for v in q['scope_contracts']}
 if set(contracts)!=set(q['required_ids']):issues.append({'type':'SCOPE_IDS_NOT_EXACT_REQUIRED','batch':q['id']})
 for v in contracts.values():
  if v['identity_and_verdict']['classification']!='required':issues.append({'type':'NONREQUIRED_IN_SCOPE','batch':q['id'],'id':v['id']})
 for path in q['candidate_formal_paths']:receivers[path].append(q['id'])
assert len(roles)==len(set(roles))
expectedreceivers={path:sorted(ids)for path,ids in receivers.items()}
for name,actualreceivers in [('batch.shared_receivers',p['shared_receivers']),('conflict.file_receivers',fg['file_receivers'])]:
 if {path:sorted(ids)for path,ids in actualreceivers.items()}!=expectedreceivers:issues.append({'type':'RECEIVER_INCIDENCE_NOT_EXACT','field':name})
if set(p['formal_file_solewriter'])!=set(expectedreceivers) or set(p['formal_file_solewriter'].values())!={'R6-I'}:issues.append({'type':'SOLEWRITER_PATH_OR_ACTOR_MISMATCH'})
summary={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'expected_conflict_pairs':len(expected),'actual_conflict_pairs':len(actual),'dependency_nodes':len(nodes),'dependency_edges':len(edge),'dag_topological_nodes':len(ordered),'separate_logical_author_reviewer_roles':len(roles),'candidate_formal_paths':len(expectedreceivers),'scope_contract_ids_exact_required':not any(v['type']=='SCOPE_IDS_NOT_EXACT_REQUIRED'for v in issues),'receiver_incidence_exact':not any(v['type']=='RECEIVER_INCIDENCE_NOT_EXACT'for v in issues),'solewriter_all_exact_paths':'R6-I'if not any(v['type']=='SOLEWRITER_PATH_OR_ACTOR_MISMATCH'for v in issues)else'ISSUE','issues':issues,'status':'STRUCTURAL_GRAPH_CHECK_NOT_REVIEW_AUTHORIZATION_OR_SEMANTIC_PASS'}
(b/'graph-validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');print(json.dumps(summary,ensure_ascii=False,indent=2))
