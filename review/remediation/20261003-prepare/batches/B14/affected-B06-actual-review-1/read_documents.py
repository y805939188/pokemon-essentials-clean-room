"""New document bookkeeping only. Never execute historical programs or reference."""
import subprocess,json,hashlib,pathlib,re,sys,csv,io,functools
sys.dont_write_bytecode = True
D=pathlib.Path(__file__).parent
A='d48197f365c39925f795c1d325988c0d74e59979';P='1e6b11a47370f1c7c4659a32443fc1afda597bac';O='93e10babe0b9c9ef8b3f5277754541b447beeeb4';PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed'
B='review/remediation/20261003-prepare/batches/'
def show(sha,path):return subprocess.check_output(['git','show',sha+':'+path])
def build():
 docs=[]
 ids=['GIR-FD82-002','GIR-FD82-003','GIR-FD82-C003','GIR-FD82-C007']+['GIR-FD82-C%03d'%n for n in [86,87,88,89,91,92,93,94,95,97,98,99,100,101,102,103,104,105,106]]+['WP80-INTAKE-R01']
 owner=['GIR-FD82-A%03d'%n for n in range(32,39)]+['GIR-FD82-A059','GIR-FD82-C120']
 for sha,path,sel in [(O,'review/global-independent-review/2026-10-03-fd82a639/findings.json',ids+owner),(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json',ids+owner)]:docs.append([sha,path,sel])
 for path in ['stage-b-contract.md','batches/B14.md']:docs.append([PLAN,'review/remediation-20261003-prepare/'+path,None])
 for path in ['finding-registration.json','integration-manifest.json','downstream-handshake.json']:
  docs.append([P,B+'B06/integration-stage-1/'+path,None])
 docs.append([P,B+'B09/acceptance-stage-1/report-corrections-successor.json',None])
 rr='review/global-independent-review/2026-10-03-fd82a639/'
 docs.append([O,rr+'agents/B/X-B-C06-RECHECK/findings-review.json',None])
 docs.append([O,rr+'root/extension-adjudications.json',ids+owner])
 docs.append([O,rr+'root/adjudication-log.json',ids+owner])
 for g in json.loads((D/'predecessor-to-ACT-inventory.json').read_text())['groups']:
  path=g['header'].split(' b/',1)[1];docs.append([A,path,None])
 # Unique scalars are exact typed values; structural maps retain order/types via original bindings.
 vals={};catalog=[];docmeta=[]
 for di,(sha,path,sel) in enumerate(docs):
  raw=show(sha,path);dm={'commit':sha,'path':path,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'selection':sel,'format':path.rsplit('.',1)[-1]};docmeta.append(dm)
  nodes=[]
  def walk(x,loc):
   if isinstance(x,dict):
    nodes.append([loc,'object',list(x.keys())])
    for k,y in x.items():walk(y,loc+[k])
   elif isinstance(x,list):
    nodes.append([loc,'array',len(x)])
    for i,y in enumerate(x):walk(y,loc+[i])
   else:
    typ=type(x).__name__;key=(typ,json.dumps(x,ensure_ascii=False,separators=(',',':')))
    if key not in vals:
     vi=len(catalog);vals[key]=vi;catalog.append({'id':vi,'type':typ,'sha256':hashlib.sha256(key[1].encode()).hexdigest(),'first':[di,loc],'characters':len(x) if isinstance(x,str) else None,'class':'semantic' if isinstance(x,str) and not pure(x) else 'identity_or_numeric'})
    nodes.append([loc,typ,vals[key]])
  v=transform(raw,dm)
  walk(v,[])
  dm['nodes_file']='typed-map-%03d.json'%di
  (D/dm['nodes_file']).write_text(json.dumps(nodes,ensure_ascii=False,separators=(',',':'))+'\n')
 (D/'reading-documents.json').write_text(json.dumps(docmeta,indent=2)+'\n');(D/'reading-values.json').write_text(json.dumps(catalog,indent=2)+'\n')
 print('documents',len(docs),'exact typed values',len(catalog),'semantic values',sum(x['class']=='semantic' for x in catalog),'semantic characters',sum(x['characters'] or 0 for x in catalog if x['class']=='semantic'))
def pure(s):
 if not s:return True
 if re.fullmatch(r'[0-9a-f]{32,64}',s):return True
 if re.fullmatch(r'\$(?:\[[^\]]+\]|\.[A-Za-z0-9_-]+)*',s):return True
 if s.startswith('#/') and not any(c.isspace() for c in s):return True
 if re.fullmatch(r'[A-Za-z0-9_-]+(?:#\d+)?',s):return True
 if re.fullmatch(r'(?:\d+[-,:;.]?)+',s):return True
 if '/' in s and not any(c.isspace() for c in s) and not any('\u4e00'<=c<='\u9fff' for c in s):return True
 if s.startswith(('Data/Scripts/','PBS/','Text_english_core/')) and re.fullmatch(r'.*\.(rb|txt)(?::[0-9;,\-]+)?',s):return True
 return False

def transform(raw,dm):
 path=dm['path'];sel=dm['selection']
 if path.endswith('.json'):
  v=json.loads(raw)
  if sel:
   if isinstance(v,list):v=[[i,x] for i,x in enumerate(v) if isinstance(x,dict) and x.get('id') in sel]
   else:v=[[k,x] for k,x in v.items() if k in sel] if all(k in v for k in sel if k.startswith('GIR')) else [[k,x] for k,x in v.items() if any(i in json.dumps(x,ensure_ascii=False) for i in sel)]
  return v
 if path.endswith('.jsonl'):return [json.loads(l) for l in raw.decode().splitlines() if l]
 lines=raw.decode().splitlines(keepends=True)
 if dm['commit']==A and path in ['audit/source-traceability.md','deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md','planning/coverage.md','planning/feature-matrix.md','review/remediation/20261003-prepare/final-integration-review.md','review/remediation/20261003-prepare/historical-errata.md']:
  patch=subprocess.check_output(['git','diff','--no-ext-diff','--no-textconv','--no-renames','--no-color',P,A,'--',path]).decode().splitlines(keepends=True)
  lines=[l[1:] for l in patch if l[:1] in ['+','-',' '] and not l.startswith(('+++','---'))]
 if path.endswith('.tsv'):
  return [[parse_cell(c) for c in row] for row in csv.reader(lines,delimiter='\t')]
 if path.endswith(('.patch','.diff')):
  return [[l[:1],l[1:].rstrip('\r\n'),l[len(l.rstrip('\r\n')):]] if l[:1] in ['+','-',' '] and not l.startswith(('+++','---')) else [l.rstrip('\r\n'),l[len(l.rstrip('\r\n')):]] for l in lines]
 return [[l.rstrip('\r\n'),l[len(l.rstrip('\r\n')):]] for l in lines]
def parse_cell(s):
 try:return json.loads(s)
 except:return s

@functools.lru_cache(maxsize=32)
def document_value(di):
 dm=json.loads((D/'reading-documents.json').read_text())[di]
 return transform(show(dm['commit'],dm['path']),dm)
def selected_value(dm,loc):
 v=transform(show(dm['commit'],dm['path']),dm)
 for k in loc:v=v[k]
 return v
if __name__=='__main__':
 if sys.argv[1]=='build':build()
 elif sys.argv[1]=='read':
  docs=json.loads((D/'reading-documents.json').read_text());values=json.loads((D/'reading-values.json').read_text());start=int(sys.argv[2]);limit=int(sys.argv[3]);chars=0;end=start
  for x in values[start:]:
   end=x['id']+1
   if x['class']!='semantic':continue
   v=document_value(x['first'][0])
   for k in x['first'][1]:v=v[k]
   if 'segment' in x:v=v[x['segment'][0]:x['segment'][1]]
   line=str(x['id'])+' D'+str(x['first'][0])+' '+json.dumps(v,ensure_ascii=False)
   print(line);chars+=len(line)
   if chars>=limit:break
  print('EMITTED RANGE',start,end,'characters',chars)
