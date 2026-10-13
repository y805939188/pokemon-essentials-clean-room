"""Read-only reference text contexts; lexical navigation, never behavioral execution."""
import json,sys
from pathlib import Path
import review_state as s
ledger=s.read('configuration-consumer-ledger.json')
by={}
for d in ledger['definitions']:
 for x in d['occurrences']:
  if x['lexical_classification']=='candidate_code_requires_semantic_review':by.setdefault(x['path'],[]).append((x['line'],d['key']))
paths=sorted(by)
if len(sys.argv)==1:
 print('usage: config_contexts.py first_file last_file (1-based sorted active paths)');sys.exit()
first,last=map(int,sys.argv[1:3])
covered={e['path']:e.get('read_ranges',[]) for e in s.read('reading-coverage.json')['sources']}
for idx,p in enumerate(paths,1):
 if not first<=idx<=last:continue
 lines=(s.REF/p).read_text().splitlines(); hits=by[p]
 unread=sorted((n,k) for n,k in hits if not any(a<=n<=z for a,z in covered.get(p,[])))
 print('\nFILE',idx,p,'total',len(lines),'unread-setting-lines',len(unread))
 if not unread:print('already read contexts; no source repetition');continue
 windows=[]
 for n,k in unread:
  a=max(1,n-10);z=min(len(lines),n+12)
  if windows and a<=windows[-1][1]+1:windows[-1][1]=max(z,windows[-1][1])
  else:windows.append([a,z])
 # Sort and merge because occurrences were key-major.
 windows.sort();merged=[]
 for a,z in windows:
  if merged and a<=merged[-1][1]+1:merged[-1][1]=max(z,merged[-1][1])
  else:merged.append([a,z])
 for a,z in merged:
  print('RANGE',a,z,'KEYS',','.join(sorted({k for n,k in hits if a<=n<=z})))
  for no in range(a,z+1):print(f'{no:5} {lines[no-1]}')
