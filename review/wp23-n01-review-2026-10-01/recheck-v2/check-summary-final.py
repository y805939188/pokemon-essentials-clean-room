"""Read-only final-state check. Run AFTER all upstream JSON writes; never edits files."""
from pathlib import Path
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
DIR=ROOT/'review/wp22-wp23-wp32-delivery-2026-09-30'
summary=(DIR/'delivery-summary.md').read_text()
results=[]
for name in ['self-checks.json','boundary-checks.json']:
    matches=[]
    for line in summary.splitlines():
        m=re.search(r'\['+re.escape(name)+r'\]\('+re.escape(name)+r'\).*?`([a-f0-9]{64})`，([\d,]+)字节',line)
        if m:matches.append(m)
    data=(DIR/name).read_bytes()
    actual={'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
    recorded=None if len(matches)!=1 else {'sha256':matches[0][1],'bytes':int(matches[0][2].replace(',',''))}
    results.append({'path':str((DIR/name).relative_to(ROOT)),'recorded':recorded,'actual':actual,'match':recorded==actual})
print(json.dumps({'read_only':True,'rows':results,'all_match':all(r['match'] for r in results)},ensure_ascii=False,indent=2))
sys.exit(0 if all(r['match'] for r in results) else 1)
