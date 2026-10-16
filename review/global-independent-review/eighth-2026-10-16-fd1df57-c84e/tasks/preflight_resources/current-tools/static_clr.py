"""Target-specific ECMA-335 static metadata/CIL reader; unknown opcodes fail closed."""
from static_pe import PE
import struct,json,sys
p=PE('/workspace/pokemon-essentials/animmaker.exe');h=p.clrhead();streams=h['streams'];counts=h['counts'];rows={}
# All present tables in this file have 2-byte heap/table/coded indices (counts < coded thresholds).
assert h['heap_sizes']==0 and max(counts.values())<1024
schemas={0:('Module','H H H H H'),1:('TypeRef','H H H'),2:('TypeDef','I H H H H H'),4:('Field','H H H'),6:('MethodDef','I H H H H H'),8:('Param','H H H'),9:('InterfaceImpl','H H'),10:('MemberRef','H H H'),12:('CustomAttribute','H H H'),17:('StandAloneSig','H'),21:('PropertyMap','H H'),23:('Property','H H H'),24:('MethodSemantics','H H H'),27:('TypeSpec','H'),32:('Assembly','I H H H H I H H H'),35:('AssemblyRef','H H H H I H H H H')}
a=h['data_offset'];spans={}
for tab,n in counts.items():
 name,fmt=schemas[tab];fmt='<'+fmt.replace(' ','');sz=struct.calcsize(fmt);spans[tab]=(a,a+n*sz);rows[tab]=[struct.unpack_from(fmt,p.b,a+i*sz) for i in range(n)];a+=n*sz
assert a<=streams['#~'][0]+streams['#~'][1]
def string(i):return p.z(streams['#Strings'][0]+i)
def compressed(o):
 v=p.u(o,1)
 if v<128:return v,1
 if v<192:return ((v&63)<<8)|p.u(o+1,1),2
 return ((v&31)<<24)|int.from_bytes(p.b[o+1:o+4],'big'),4
def blob(i):
 a=streams['#Blob'][0]+i;n,k=compressed(a);return p.b[a+k:a+k+n].hex()
def us(i):
 a=streams['#US'][0]+i;n,k=compressed(a);return p.b[a+k:a+k+n-1].decode('utf-16le')
def typeref(i):
 if i==0:return 'nil'
 r=rows[1][i-1];return string(r[2])+'.'+string(r[1])
def memberparent(i):
 tag=i&7;v=i>>3
 if tag==1:return typeref(v)
 if tag==0:return string(rows[2][v-1][1])
 if tag==4:return 'TypeSpec('+blob(rows[27][v-1][0])+')'
 return str((tag,v))
def token(v):
 t=v>>24;i=v&0xffffff
 if t==0x70:return repr(us(i))
 if t==10:
  r=rows[t][i-1];return memberparent(r[0])+'.'+string(r[1])+' sig='+blob(r[2])
 if t==6:return string(rows[t][i-1][3])
 if t==4:return string(rows[t][i-1][1])
 if t==1:return typeref(i)
 if t==2:return string(rows[t][i-1][1])
 if t==27:return 'TypeSpec '+blob(rows[t][i-1][0])
 return f'token {v:#x}'
ops={}
def seq(start,names,kind=''):
 for i,n in enumerate(names.split()):ops[start+i]=(n,kind)
seq(0,'nop break ldarg.0 ldarg.1 ldarg.2 ldarg.3 ldloc.0 ldloc.1 ldloc.2 ldloc.3 stloc.0 stloc.1 stloc.2 stloc.3')
seq(0x0e,'ldarg.s ldarga.s starg.s ldloc.s ldloca.s stloc.s','B')
seq(0x14,'ldnull ldc.i4.m1 ldc.i4.0 ldc.i4.1 ldc.i4.2 ldc.i4.3 ldc.i4.4 ldc.i4.5 ldc.i4.6 ldc.i4.7 ldc.i4.8')
ops.update({0x1f:('ldc.i4.s','b'),0x20:('ldc.i4','i'),0x21:('ldc.i8','q'),0x22:('ldc.r4','f'),0x23:('ldc.r8','d'),0x25:('dup',''),0x26:('pop',''),0x27:('jmp','t'),0x28:('call','t'),0x29:('calli','t'),0x2a:('ret','')})
seq(0x2b,'br.s brfalse.s brtrue.s beq.s bge.s bgt.s ble.s blt.s bne.un.s bge.un.s bgt.un.s ble.un.s blt.un.s','r1')
seq(0x38,'br brfalse brtrue beq bge bgt ble blt bne.un bge.un bgt.un ble.un blt.un','r4')
ops[0x45]=('switch','switch')
seq(0x46,'ldind.i1 ldind.u1 ldind.i2 ldind.u2 ldind.i4 ldind.u4 ldind.i8 ldind.i ldind.r4 ldind.r8 ldind.ref stind.ref stind.i1 stind.i2 stind.i4 stind.i8 stind.r4 stind.r8 add sub mul div div.un rem rem.un and or xor shl shr shr.un neg not conv.i1 conv.i2 conv.i4 conv.i8 conv.r4 conv.r8 conv.u4 conv.u8')
seq(0x6f,'callvirt cpobj ldobj ldstr newobj castclass isinst','t');ops[0x76]=('conv.r.un','');ops[0x79]=('unbox','t');ops[0x7a]=('throw','');seq(0x7b,'ldfld ldflda stfld ldsfld ldsflda stsfld stobj','t')
seq(0x8c,'box newarr','t');ops[0x8e]=('ldlen','');ops[0x8f]=('ldelema','t');seq(0x90,'ldelem.i1 ldelem.u1 ldelem.i2 ldelem.u2 ldelem.i4 ldelem.u4 ldelem.i8 ldelem.i ldelem.r4 ldelem.r8 ldelem.ref stelem.i stelem.i1 stelem.i2 stelem.i4 stelem.i8 stelem.r4 stelem.r8 stelem.ref');seq(0xa3,'ldelem stelem unbox.any','t');ops[0xd0]=('ldtoken','t');ops[0xd1]=('conv.u2','');ops[0xd2]=('conv.u1','');ops[0xd3]=('conv.i','');ops[0xdc]=('endfinally','');ops[0xdd]=('leave','r4');ops[0xde]=('leave.s','r1');ops[0xe0]=('conv.u','');seq(0xfe00,'arglist ceq cgt cgt.un clt clt.un');seq(0xfe06,'ldftn ldvirtftn','t');seq(0xfe09,'ldarg ldarga starg ldloc ldloca stloc','H');ops[0xfe11]=('endfilter','');ops[0xfe15]=('initobj','t');ops[0xfe16]=('constrained.','t');ops[0xfe1a]=('rethrow','')
def method(i):
 r=rows[6][i-1];off=p.off(r[0]);flags=p.u(off,1)
 if flags&3==2:hs=1;sz=flags>>2;local=0;fl=2;stack=8
 else:fl=p.u(off,2);hs=(fl>>12)*4;stack=p.u(off+2,2);sz=p.u(off+4,4);local=p.u(off+8,4)
 st=off+hs;end=st+sz;res=[];a=st
 while a<end:
  old=a;o=p.u(a,1);a+=1
  if o==0xfe:o=(o<<8)|p.u(a,1);a+=1
  if o not in ops:raise ValueError(f'unknown {o:#x} at {a-1:#x} method {i}')
  name,k=ops[o];v=''
  if k in ['r1','r4']:
   n=int(k[-1]);v=int.from_bytes(p.b[a:a+n],'little',signed=True);a+=n;v=f'IL_{a-st+v:04x}'
  elif k=='switch':
   n=p.u(a,4);a+=4;base=a+n*4;v=[base-st+int.from_bytes(p.b[a+4*j:a+4*j+4],'little',signed=True) for j in range(n)];a=base
  elif k:
   fmt='I' if k=='t' else k;n=struct.calcsize('<'+fmt);v=struct.unpack_from('<'+fmt,p.b,a)[0];a+=n
   if k=='t':v=f'{v:#010x} '+token(v)
  res.append(f'{old:#06x} IL_{old-st:04x} {name} {v}')
 assert a==end
 eh=[]
 if fl&8:
  a=(end+3)&~3
  while True:
   kind=p.u(a,1);fat=bool(kind&64);size=p.u(a+1,3) if fat else p.u(a+1,1);cs=24 if fat else 12
   for q in range(a+4,a+size,cs):
    vals=struct.unpack_from('<6I' if fat else '<H H B H B I',p.b,q);eh.append({'offset':q,'fields':vals,'catch':token(vals[-1]) if vals[0]==0 else None})
   if not kind&128:break
   a=(a+size+3)&~3
 return {'id':i,'name':string(r[3]),'signature':blob(r[4]),'file_range':[off,end],'header_bytes':p.b[off:st].hex(),'stack':stack,'local_signature':blob(rows[17][(local&0xffffff)-1][0]) if local else None,'cil':res,'exception_sections':eh}
if __name__=='__main__':
 if len(sys.argv)>1 and sys.argv[1]=='meta':
  print(json.dumps(h,indent=2));print('TABLES')
  for t,rs in rows.items():
   print('TABLE',t,schemas[t][0],'RANGE',spans[t])
   for i,r in enumerate(rs,1):
    extra=''
    if t==1:extra=typeref(i)
    if t==2:extra=string(r[2])+'.'+string(r[1])
    if t in [4,6,10]:extra=token((t<<24)|i)
    if t==8:extra=string(r[2])
    if t in [17,27]:extra=blob(r[0])
    if t==23:extra=string(r[1])+' sig='+blob(r[2])
    if t==32:extra=string(r[7])+' '+string(r[8])
    if t==35:extra=string(r[6])+' '+string(r[7])
    print(i,r,extra)
 else:
  ids=range(1,16) if len(sys.argv)==1 else [int(x) for x in sys.argv[1:]]
  for i in ids:
   m=method(i);cil=m.pop('cil');print(json.dumps(m,ensure_ascii=False));print('\n'.join(cil))
