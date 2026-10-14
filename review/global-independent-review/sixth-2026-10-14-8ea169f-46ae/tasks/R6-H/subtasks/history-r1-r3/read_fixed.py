"""Independent read-only git-object range reader. No reference programs execute.
Inputs: explicit approved fixed revision, object path, inclusive line bounds.
Output: numbered range stdout, same range log, nonsemantic reading ledger entry.
This helper does not declare semantic completion; reviewer annotates separately.
"""
import sys, subprocess, pathlib, json, hashlib, datetime
BASE = pathlib.Path(__file__).resolve().parent
ALLOWED = {'8ea169fbd0f33f378b5d732fd6bea59e854e04a6','b67f542b47ad33ac23053a21f62748077c167a23','f49d870c6fd616ab6736754a218a4553b5acac7f','13fddb0a217b36974c75657aa68da0caf104ee48','7533e516bd6e2a34ebeb68af28617c854ac17d50','044c3483229e7e76bedf1fc244fc84d274bf059c','debf59f3c5370df253706969fd4dd1c103300bf2','1eda123e3bcd4b1aa99e2ba57c6de02d56414716','b1589101dd8afc37afa4fa83d0d2159079483066'}
rev, path, first, last = sys.argv[1:]
assert rev in ALLOWED and not path.startswith('/') and '..' not in path.split('/')
first, last = int(first), int(last)
assert 1 <= first <= last
proc = subprocess.run(['git','show',f'{rev}:{path}'],capture_output=True,check=True)
data = proc.stdout
lines = data.decode('utf-8').splitlines()
last = min(last,len(lines))
assert first <= last
output = '\n'.join(f'{n}: {lines[n-1]}' for n in range(first,last+1))+'\n'
key = hashlib.sha256(f'{rev}:{path}'.encode()).hexdigest()[:12]
log = BASE/f'read-{key}-{first}-{last}.log'
log.write_text(output)
entry = {'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'revision':rev,'path':path,'range':[first,last],'total_lines':len(lines),'sha256':hashlib.sha256(data).hexdigest(),'mode':'actual_range_read','semantic_review':'pending','log':log.name}
with (BASE/'reading-ledger.jsonl').open('a') as f: f.write(json.dumps(entry,ensure_ascii=False)+'\n')
print(f'OBJECT {rev}:{path} lines {first}-{last}/{len(lines)} sha256 {entry["sha256"]}')
print(output,end='')
