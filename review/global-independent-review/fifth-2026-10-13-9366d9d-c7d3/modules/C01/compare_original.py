import sys,json,difflib
from pathlib import Path
root=Path(__file__).resolve().parent
for r in json.loads(sys.argv[1]):
 a=Path(r['formal']).read_text().splitlines();b=Path(r['original']).read_text().splitlines();ops=[]
 print('ORIGINAL',r['original'],'FORMAL',r['formal'])
 for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
  ops.append({'type':tag,'formal':[i+1,j],'original':[k+1,l]})
  if tag=='equal':print('EXACT_EQUAL',i+1,j,'=>',k+1,l)
  elif tag in ('replace','insert'):
   print('ORIGINAL_DISTINCT')
   for n in range(k,l):print(str(n+1)+': '+b[n])
 with (root/'original-comparison-log.jsonl').open('a') as f:f.write(json.dumps(dict(r,opcodes=ops),ensure_ascii=False)+'\n')
