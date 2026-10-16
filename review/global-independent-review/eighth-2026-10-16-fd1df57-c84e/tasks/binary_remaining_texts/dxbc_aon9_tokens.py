"""Static Aon9 shader byte token decoder; no compiler, driver or GPU calls."""
import pathlib,json,re,struct,hashlib
P=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes()
h=(P/'d3d9types.h').read_text();body=h.split('typedef enum _D3DSHADER_INSTRUCTION_OPCODE_TYPE',1)[1].split('}',1)[0];ops={};v=-1
for name,value in re.findall(r'\b(D3DSIO_\w+)\s*(?:=\s*(0x[0-9a-fA-F]+|[0-9]+))?\s*,',body):
 v=int(value,0) if value else v+1;ops[v]=name[7:]
def reg(t,dest=False):
 assert t>>31==1 and not(t&8192),hex(t)
 typ=((t>>28)&7)|((t>>8)&24);s={0:'r',1:'v',2:'c',3:'t',4:'oRast',5:'oAttr',6:'oTex',8:'oColor',10:'s'}.get(typ,'type'+str(typ))+str(t&2047)
 if dest:s+='.'+''.join('xyzw'[i] for i in range(4) if t&(0x10000<<i))+' dstmod='+str((t>>20)&15)+' shift='+str((t>>24)&15)
 else:s+='.'+''.join('xyzw'[(t>>(16+2*i))&3] for i in range(4))+' srcmod='+str((t>>24)&15)
 return s
allrows=[];view=[]
for c in json.loads((P/'compiled-shader-container-structures.json').read_text())['containers']:
 a=next(x for x in c['chunks'] if x['tag']=='Aon9');s=a['payload_start'];raw=b[s:a['end']];w=list(struct.unpack('<'+'I'*(len(raw)//4),raw));assert w[0]==len(raw);off=w[3];size=w[2];assert off+size==len(raw) and off%4==0
 x=w[off//4:];assert x[0]==w[1] and x[-1]==65535;rows=[];i=1;view.append('CONTAINER %d Aon9 [%d,%d) header=%s'%(c['start'],s,a['end'],','.join('%08x'%v for v in w[:off//4])))
 while i<len(x):
  t=x[i];op=t&65535;name=ops[op];n=(t>>24)&15;assert i+n<len(x)
  arg=x[i+1:i+n+1];args=[]
  if name=='END':assert n==0 and i==len(x)-1
  elif name=='DEF':assert n==5;args=[reg(arg[0],True)]+[format(struct.unpack('<f',struct.pack('<I',v))[0],'.9g')+'[0x%08x]'%v for v in arg[1:]]
  elif name=='DCL':assert n==2;args=['declaration=0x%08x'%arg[0],reg(arg[1],True)]
  elif name in ('MOV','ADD','SUB','MUL','MAD','DP3','DP4','TEX','DP2ADD'):
   args=[reg(arg[0],True)]+[reg(v) for v in arg[1:]]
  else:raise ValueError((name,[hex(v) for v in arg]))
  row={'offset':s+off+i*4,'opcode':name,'opcode_controls':(t>>16)&255,'operands':args,'raw_tokens':['%08x'%v for v in x[i:i+n+1]]};rows.append(row);view.append('%d %s %s controls=0x%x'%(row['offset'],name,', '.join(args),row['opcode_controls']));i+=1+n
 allrows.append({'container_start':c['start'],'aon9_start':s,'aon9_end':a['end'],'header_words':['%08x'%v for v in w[:off//4]],'shader_start':s+off,'shader_bytes':size,'shader_sha256':hashlib.sha256(b[s+off:s+off+size]).hexdigest(),'instructions':rows,'qualification':'Aon9 initial fields structurally matched size/version/embedded shader bounds. Remaining header words preserved raw; translation-header semantic not fully proved.'})
(P/'compiled-shader-aon9-programs.json').write_text(json.dumps(allrows,indent=2)+'\n');(P/'compiled-shader-aon9-view.txt').write_text('\n'.join(view)+'\n');print(json.dumps({'containers':len(allrows),'instructions':sum(len(c['instructions']) for c in allrows),'view_lines':len(view)}))
