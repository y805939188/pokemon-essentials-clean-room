"""Static structure only; does not execute, import, or translate reference code."""
import pathlib,re,json,csv,hashlib
root=pathlib.Path(__file__).resolve().parent
src=pathlib.Path('reference/pokemon-essentials/Data/Scripts/011_Battle')
files=sorted((src/'006_AI MoveEffects').glob('00[123]*.rb'))
files += [src/'005_AI/008_AI_Utilities.rb']
rows=[]
for p in files:
 text=p.read_text()
 matches=list(re.finditer(r'^Battle::AI::Handlers::(\w+)\.(add|copy)\((.*?)\)',text,re.M|re.S))
 for i,m in enumerate(matches):
  family,op,args=m.groups()
  if p.name.startswith('008_') and family!='AbilityRanking': continue
  if op=='add':
   k=re.match(r'\s*(?:"([^"]+)"|:(\w+))',args); keys=[k[1] or k[2]]
  else: keys=[a or b for a,b in re.findall(r'"([^"]+)"|:(\w+)',args)]
  line=text.count('\n',0,m.start())+1
  last=text.count('\n',0,matches[i+1].start()) if i+1<len(matches) else len(text.splitlines())
  for k in (keys[1:] if op=='copy' else keys):
   rows.append({'path':str(p),'line':line,'unit_end_before_next_registration':last,'family':family,'operation':op,'key':k,'copy_source':keys[0] if op=='copy' else '', 'evidence':'STRUCTURAL_ONLY_NOT_SEMANTIC_PASS'})
with (root/'inventory-registrations.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(root/'inventory-summary.json').write_text(json.dumps({'files':{str(p):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'lines':len(p.read_text().splitlines())} for p in files},'registration_occurrences':len(rows),'by_file':{p.name:sum(r['path']==str(p) for r in rows) for p in files},'stage':'STRUCTURAL_ONLY'},indent=2))
print(json.dumps({'occurrences':len(rows),'effects':len(set(r['key'] for r in rows)),'by_file':{p.name:sum(r['path']==str(p) for r in rows) for p in files}},indent=2))
for p in files:
 print('\n'+p.name)
 for key in dict.fromkeys(r['key'] for r in rows if r['path']==str(p)):
  units=[r for r in rows if r['key']==key and r['path']==str(p)]
  print(key+' '+','.join(r['family']+':'+str(r['line']) for r in units))
