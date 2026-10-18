"""Mechanical identity/accounting checks, explicitly not behavioral tests."""
from pathlib import Path
import collections, datetime, gzip, hashlib, json, re, subprocess
O=Path(__file__).resolve().parent
P=O.parent/'preflight_resources'
sha=lambda b:hashlib.sha256(b).hexdigest()
counts=collections.Counter();seen={};lines=collections.defaultdict(list)
with gzip.open(O/'full-disposition-ledger.jsonl.gz','rt') as f:
 for l in f:
  r=json.loads(l);rid=r['candidate_id'];assert rid not in seen
  seen[rid]=r;counts[r['semantic_status']]+=1;lines[r['path']].append(r['inventory_line'])
assert len(seen)==260161
summary=json.loads((O/'disposition-summary.json').read_text())
assert dict(counts)==summary['status_counts']
for seq in lines.values():assert seq==list(range(1,len(seq)+1))
unread={}
with gzip.open(O/'remaining-unread.jsonl.gz','rt') as f:
 for l in f:
  r=json.loads(l);assert r['semantic_status']=='UNREAD' and r=={k:v for k,v in seen[r['candidate_id']].items() if k!='additional_content_inspection'}
  unread[r['candidate_id']]=r
assert set(unread)=={k for k,v in seen.items() if v['semantic_status']=='UNREAD'}
assert len(unread)==57948
ctrl=json.loads((P/'handoff/controller-readset.json').read_text());pos=ctrl['offset']
for r in ctrl['rows']:
 assert r['start']==pos;pos=r['end_exclusive']
assert pos==ctrl['end_exclusive'] and len(ctrl['rows'])==1678
orders={}
for l in (O/'controller-order-view.txt').read_text().splitlines():
 a,b=l.split(' ',1);orders[int(a)]=b.split(',')
patterns={}
for l in (O/'controller-pattern-view.txt').read_text().splitlines()[1:]:
 m=re.fullmatch(r'P(\d+) order=(\d+) base=(None|\d+) (.*)',l);assert m
 p,order=int(m[1]),int(m[2]);v={} if m[3]=='None' else patterns[int(m[3])][0].copy()
 for delta in m[4].split(','):
  if not delta:continue
  k,x=delta.split('=',1)
  if x=='<ABSENT>':del v[k]
  else:v[k]=x
 assert set(v)==set(orders[order]);patterns[p]=(v,order)
assert len(patterns)==790 and len(orders)==122
record_count=0
for r in ctrl['rows']:
 if r['kind']!='mapping':continue
 v,order=patterns[r['pattern_group']]
 assert [[k,v[k]] for k in orders[order]]==r['mapping'];record_count+=1
assert record_count==1666
names={};covered={}
for l in (O/'controller-name-view.txt').read_text().splitlines():
 n,refs=l.split(' | ',1);assert n not in names;names[n]=refs
 for pair in refs.split(','):
  line,pattern=map(int,pair.split(':'));assert line not in covered;covered[line]=(n,pattern)
assert len(names)==806 and len(covered)==1666
for r in ctrl['rows']:
 if r['kind']=='mapping':assert covered[r['line']]==(r['name'],r['pattern_group'])
ids=json.loads((O/'identities.json').read_text())['identities'];unique=set()
for r in ids:
 data=Path(r['path']).read_bytes() if 'repo' not in r else (Path(r['repo'])/r['path']).read_bytes()
 assert len(data)==r['bytes'] and sha(data)==r['sha256']
 key=(r.get('repo'),r.get('commit'),r['path']);assert key not in unique;unique.add(key)
 if 'repo' in r:
  old=subprocess.run(['git','-C',r['repo'],'show',r['commit']+':'+r['path']],check=True,capture_output=True).stdout
  assert data==old
for p in O.glob('*.json'):json.loads(p.read_text())
props=json.loads((O/'proposals.json').read_text());assert len(props['records'])==4 and len({r['id'] for r in props['records']})==4
assert props['independently_accepted']==0 and props['required_accepted']==0
result=dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),kind='TOOL_VALIDATION',status='MECHANICAL_CHECKS_PASS',finite_candidates=len(seen),status_counts=dict(counts),unread=len(unread),controller=dict(rows=1678,records=record_count,patterns=len(patterns),orders=len(orders),names=len(names)),identities=len(ids),semantic_review='INCOMPLETE;57948UNREAD;no independent counterreview yet',behavior_vectors='NOT_EXECUTED',update_status='UPDATE_NOT_STARTED')
(O/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
