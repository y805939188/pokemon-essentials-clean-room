"""Validate read union and pinned blobs; writes only task-owned audit artifacts."""
from pathlib import Path
import json,csv,hashlib,subprocess,datetime
R=Path(__file__).resolve().parent
source=Path('reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects')
owned=sorted(source.glob('00[123]*.rb'))
formal=Path('deliverables/final-specification-set')
owned += sorted((formal/'combat-requirements').glob('wp52-[abc]-*.md'))
owned += [formal/'test-catalog/combat-requirements-wp49-51-52.md']
ledger=[json.loads(x) for x in (R/'reading-ledger.jsonl').read_text().splitlines() if x]
checks=[]
for p in owned:
 raw=p.read_bytes(); lines=raw.decode().splitlines();seen=set()
 for e in ledger:
  if e.get('path')==str(p) and e.get('stage')=='continuous_range_output':seen.update(range(e['start'],e['end']+1))
 gaps=sorted(set(range(1,len(lines)+1))-seen)
 if str(p).startswith('reference/'):
  repo='reference/pokemon-essentials';ref='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+str(p.relative_to(repo))
 else:repo='.';ref='8ea169fbd0f33f378b5d732fd6bea59e854e04a6:'+str(p)
 blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
 expected=subprocess.run(['git','-C',repo,'rev-parse',ref],capture_output=True,text=True,check=True).stdout.strip()
 checks.append({'path':str(p),'lines':len(lines),'read_lines':len(seen),'unread':gaps,'pinned_blob':expected,'actual_blob':blob,'pinned_match':blob==expected})
 assert not gaps,(p,gaps)
 assert blob==expected,(p,blob,expected)
(R/'coverage-proof.json').write_text(json.dumps({'read_unread0_is_not_automatic_semantic_pass':True,'checks':checks,'total_owned_read_lines':sum(x['lines'] for x in checks),'unread_owned_lines':sum(len(x['unread']) for x in checks)},indent=2))
print(json.dumps({'files':len(checks),'lines':sum(x['lines'] for x in checks),'unread':0,'all_pinned_blobs_match':True}))
