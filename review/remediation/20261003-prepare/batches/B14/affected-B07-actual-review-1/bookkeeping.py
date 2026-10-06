import subprocess,json,hashlib,pathlib,re,sys
D=pathlib.Path(__file__).parent
A='d48197f365c39925f795c1d325988c0d74e59979';O='93e10babe0b9c9ef8b3f5277754541b447beeeb4';P='41fffb540c6483f5296ea0d33b789b75180d27ed';B='1e6b11a47370f1c7c4659a32443fc1afda597bac'
def show(c,p):return subprocess.check_output(['git','show',c+':'+p])
def dump(p,x): (D/p).write_text(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
def build(name,inputs):
 values=[]; lookup={}; structures=[]
 def walk(x,loc):
  if isinstance(x,dict):return {'object':[[k,walk(v,loc+'/'+k)] for k,v in x.items()]}
  if isinstance(x,list):return {'array':[walk(v,loc+'/'+str(i)) for i,v in enumerate(x)]}
  t=type(x).__name__;val=json.dumps(x,ensure_ascii=False,separators=(',',':')); key=t+':'+val
  if key not in lookup:
   n=len(values);lookup[key]=n; values.append({'type':t,'value':x,'contexts':[]})
  n=lookup[key]; values[n]['contexts'].append(loc);return {'value':n}
 for c,p,sel in inputs:
  b=show(c,p);s=b.decode();x=json.loads(s) if p.endswith('.json') else s.splitlines(keepends=True)
  if sel is not None:
   if isinstance(x,list):x={z.get('id'):z for z in x if z.get('id') in sel}
   else:x={k:v for k,v in x.items() if k in sel}
  structures.append({'commit':c,'path':p,'selection':sel,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'structure':walk(x,c+':'+p)})
 dump(name+'-values.json',values);dump(name+'-structure.json',structures);print(name,'values',len(values),'inputs',len(inputs))
def display(name,a,b):
 v=json.loads((D/(name+'-values.json')).read_text());print('VALUES',name,a,b,'TOTAL',len(v))
 for n in range(a,min(b,len(v))):
  x=v[n];print(n,x['contexts'][0].split(':',1)[1],json.dumps(x['value'],ensure_ascii=False))
if __name__=='__main__':
 if sys.argv[1]=='view':display(sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))
def semview(name,start,budget=11000):
 v=json.loads((D/(name+'-values.json')).read_text());i=start;used=0
 while i<len(v):
  x=v[i];z=x['value'];t=json.dumps(z,ensure_ascii=False)
  pure=not isinstance(z,str) or bool(re.fullmatch(r'[0-9a-f]{40,64}|[A-Z0-9_./:+ -]{1,90}|[0-9;:,.+()\- ]+|(?:review|deliverables|specs|planning|audit|root|agents|Data|PBS)/[A-Za-z0-9_ ./()@:+\-]+\.(?:md|json|tsv|csv|rb|txt|dat|pdf|png|rxdata|jsonl)',z))
  if pure:i+=1;continue
  line=f"{i} {'/'.join(x['contexts'][0].split('/')[-3:])} {t}\n"
  if used and used+len(line)>budget:break
  print(line,end='');used+=len(line);i+=1
 print('NEXT',i,'TOTAL',len(v))
