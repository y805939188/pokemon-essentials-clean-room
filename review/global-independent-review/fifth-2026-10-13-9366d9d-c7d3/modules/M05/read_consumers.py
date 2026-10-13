from pathlib import Path
import json,sys
p=Path(__file__).resolve().parent;r=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
d=json.loads((p/'consumer-read-plan.json').read_text())
for idx in map(int,sys.argv[1].split(',')):
 x=d['files'][idx];ls=(r/x['path']).read_text().splitlines();print('\nSOURCE',idx,x['path'])
 for q in ([{'lines':a,'entries':['complete registration block']} for a in x.get('registration_full_ranges',[])] if len(sys.argv)>2 and sys.argv[2]=='reg' else x['ranges']):
  a,b=q['lines'];print('RANGE',a,b,'ENTRY','; '.join(q['entries']))
  for n in range(a,b+1):print(f'{n:5} {ls[n-1]}')
