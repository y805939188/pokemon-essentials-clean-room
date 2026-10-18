"""Static token navigation. No GPU/API/compiler invocation or shader execution."""
import pathlib,json,struct,re,hashlib
P=pathlib.Path(__file__).resolve().parent
h=(P/'d3d12TokenizedProgramFormat.hpp').read_text()
body=h.split('typedef enum D3D10_SB_OPCODE_TYPE {',1)[1].split('}',1)[0]
names=re.findall(r'^\s*(D3D\w+_SB_OPCODE_\w+)\s*,',body,re.M)
def operand(w,i):
 start=i;t=w[i];i+=1;typ=(t>>12)&255;comp=t&3;sel=(t>>2)&3
 ext=[];z=t
 while z>>31:z=w[i];ext.append(z);i+=1
 dims=(t>>20)&3;idx=[]
 for d in range(dims):
  rep=(t>>(22+3*d))&7
  assert rep==0,('unimplemented relative index',hex(t))
  idx.append(w[i]);i+=1
 if typ in (4,5):
  n={0:0,1:1,2:4}[comp]*(2 if typ==5 else 1)
  val=w[i:i+n];i+=n
  s='l('+','.join(format(struct.unpack('<f',struct.pack('<I',x))[0],'.9g')+'[0x%08x]'%x for x in val)+')'
 else:
  s={0:'r',1:'v',2:'o',6:'s',7:'t',8:'cb'}.get(typ,'type'+str(typ))+''.join('['+str(x)+']' for x in idx)
  if comp==2:
   if sel==0:s+='.'+''.join('xyzw'[k] for k in range(4) if t&(16<<k))
   elif sel==1:s+='.'+''.join('xyzw'[(t>>(4+2*k))&3] for k in range(4))
   elif sel==2:s+='.'+'xyzw'[(t>>4)&3]
   else:raise ValueError('undefined selection')
 for e in ext:
  assert e&63==1
  mod=(e>>6)&255
  s={0:lambda x:x,1:lambda x:'-'+x,2:lambda x:'abs('+x+')',3:lambda x:'-abs('+x+')'}[mod](s)
 return s,i,{'start_word':start,'end_word':i,'tokens':['%08x'%x for x in w[start:i]]}
allrows=[];lines=[]
for f in sorted((P/'compiled-shader-objects').glob('*.dxbc'),key=lambda f:int(f.stem)):
 b=f.read_bytes();n=struct.unpack_from('<I',b,28)[0];chunks=[]
 for off in struct.unpack_from('<'+'I'*n,b,32):
  size=struct.unpack_from('<I',b,off+4)[0]
  if b[off:off+4]==b'SHDR':sh=b[off+8:off+8+size];shoff=int(f.stem)+off+8
 w=list(struct.unpack('<'+'I'*(len(sh)//4),sh));assert w[1]==len(w);i=2;rows=[]
 lines.append('CONTAINER '+f.stem+' VERSION 0x%08x WORDS %d'%(w[0],len(w)))
 while i<len(w):
  t=w[i];op=t&2047;length=(t>>24)&127;name=names[op].split('_OPCODE_',1)[1];assert length and i+length<=len(w)
  raw=w[i:i+length];j=i+1;extensions=[];z=t
  while z>>31:z=w[j];extensions.append(z);j+=1
  args=[];parsed=[]
  if name=='DCL_TEMPS':args=[str(w[j])];j+=1
  elif name=='DCL_RESOURCE':
   a,j,p=operand(w,j);args=[a,'return-types=0x%08x'%w[j],'dimension='+str((t>>11)&31)];parsed=[p];j+=1
  elif name in ('DCL_INPUT_SIV','DCL_OUTPUT_SIV','DCL_INPUT_SGV','DCL_OUTPUT_SGV','DCL_INPUT_PS_SIV','DCL_INPUT_PS_SGV'):
   a,j,p=operand(w,j);args=[a,'system-value='+str(w[j])];parsed=[p];j+=1
  elif name in ('DCL_INPUT','DCL_OUTPUT','DCL_INPUT_PS','DCL_SAMPLER','DCL_CONSTANT_BUFFER'):
   a,j,p=operand(w,j);args=[a];parsed=[p]
  elif name in ('MOV','ADD','MUL','MAD','DP2','DP3','DP4','SAMPLE','RET'):
   while j<i+length:a,j,p=operand(w,j);args.append(a);parsed.append(p)
  else:raise ValueError(('unsupported opcode',name,raw))
  assert j==i+length,(f.name,name,j,i+length)
  r={'offset':shoff+4*i,'word':i,'length':length,'opcode':name,'controls':(t>>11)&8191,'extensions':extensions,'operands':args,'operand_tokens':parsed,'raw_tokens':['%08x'%x for x in raw]};rows.append(r)
  lines.append('%d %s %s controls=0x%x ext=%s'%(r['offset'],name,', '.join(args),r['controls'],','.join('%08x'%x for x in extensions)))
  i+=length
 allrows.append({'container':f.name,'source_start':int(f.stem),'SHDR_start':shoff,'version':w[0],'length':len(sh),'sha256':hashlib.sha256(sh).hexdigest(),'instructions':rows})
(P/'compiled-shader-token-programs.json').write_text(json.dumps(allrows,indent=2)+'\n')
(P/'compiled-shader-token-view.txt').write_text('\n'.join(lines)+'\n')
print(json.dumps({'containers':len(allrows),'instructions':sum(len(r['instructions']) for r in allrows),'view_lines':len(lines)}))
