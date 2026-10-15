# Local byte-loader adaptation of fully read R7-C06 inspection tool. No target execution.
"""Independent bounded PE/CLR byte decoder, inspection only; never loads target."""
import pathlib, subprocess, struct, json, hashlib, sys
ROOT=pathlib.Path.cwd()
b=pathlib.Path('/workspace/r7-context/R7-U10-reviewer/inputs/reference/animmaker.exe').read_bytes()
def u(o,n=4): return int.from_bytes(b[o:o+n],'little')
p=u(60); opt=p+24; n=u(p+6,2); sh=opt+u(p+20,2)
sections=[]
for i in range(n):
 s=sh+i*40; sections.append((b[s:s+8].rstrip(b'\0').decode(),u(s+12),u(s+16),u(s+20),u(s+8)))
def off(r):
 for name,va,sz,raw,vs in sections:
  if va<=r<va+max(sz,vs): return raw+r-va
 raise ValueError(hex(r))
clr=off(u(opt+96+14*8)); meta=off(u(clr+8)); vl=u(meta+12); pos=meta+16+vl; pos=(pos+3)&~3; ns=u(pos+2,2);pos+=4;streams={}
for i in range(ns):
 rel=u(pos);sz=u(pos+4); end=b.index(0,pos+8); name=b[pos+8:end].decode();streams[name]=(meta+rel,sz);pos=(end+4)&~3
tab=streams['#~'][0]; heap=b[tab+6]; valid=u(tab+8,8); pos=tab+24;counts={}
for i in range(64):
 if valid>>i&1: counts[i]=u(pos);pos+=4
def idx(t): return 4 if counts.get(t,0)>=65536 else 2
def cod(bits,ts): return 4 if max([counts.get(t,0) for t in ts]) >= (1<<(16-bits)) else 2
S=4 if heap&1 else 2; G=4 if heap&2 else 2; B=4 if heap&4 else 2
C={'ResolutionScope':cod(2,[0,26,35,1]),'TypeDefOrRef':cod(2,[2,1,27]),'MemberRefParent':cod(3,[2,1,26,6,27]),'HasConstant':cod(2,[4,8,23]),'HasCustomAttribute':cod(5,[6,4,1,2,8,9,10,0,14,23,20,17,26,27,32,35,38,39,40,42,44,43]),'CustomAttributeType':cod(3,[6,10]),'HasFieldMarshal':cod(1,[4,8]),'HasDeclSecurity':cod(2,[2,6,32])}
schemas={0:[2,S,G,G,G],1:[C['ResolutionScope'],S,S],2:[4,S,S,C['TypeDefOrRef'],idx(4),idx(6)],3:[idx(4)],4:[2,S,B],5:[idx(6)],6:[4,2,2,S,B,idx(8)],7:[idx(8)],8:[2,2,S],9:[idx(2),C['TypeDefOrRef']],10:[C['MemberRefParent'],S,B],11:[2,C['HasConstant'],B],12:[C['HasCustomAttribute'],C['CustomAttributeType'],B],13:[C['HasFieldMarshal'],B],14:[2,C['HasDeclSecurity'],B],15:[2,4,idx(2)],16:[4,idx(4)],17:[B]}
tables={}
for t in range(18):
 if t not in counts: continue
 schema=schemas[t]; rows=[]
 for i in range(counts[t]):
  vals=[]
  for sz in schema: vals.append(u(pos,sz));pos+=sz
  rows.append(vals)
 tables[t]=rows
def string(i):
 o=streams['#Strings'][0]+i;return b[o:b.index(0,o)].decode()
def compressed(o):
 v=b[o]
 if v<128:return v,1
 if v<192:return ((v&63)<<8)|b[o+1],2
 return ((v&31)<<24)|(b[o+1]<<16)|(b[o+2]<<8)|b[o+3],4
def blob(i):
 o=streams['#Blob'][0]+i;sz,k=compressed(o);return b[o+k:o+k+sz].hex()
types={i+1:string(r[2])+'.'+string(r[1]) for i,r in enumerate(tables[1])}
names={}
for i,r in enumerate(tables[6]):names[0x06000001+i]=string(r[3])
for i,r in enumerate(tables.get(4,[])):names[0x04000001+i]=string(r[1])
for i,r in enumerate(tables.get(10,[])):
 parent,na,si=r;tag=parent&7;rid=parent>>3; pn=types.get(rid,'?') if tag==1 else ('TypeDef'+str(rid) if tag==0 else '?')
 names[0x0a000001+i]=pn+'::'+string(na)+' sig='+blob(si)
def token(v):
 if v>>24==0x70:
  o=streams['#US'][0]+(v&0xffffff);sz,k=compressed(o);return repr(b[o+k:o+k+sz-1].decode('utf-16le'))
 return names.get(v,hex(v))
# Only standard CIL opcode decoding, no target evaluation or behavioral model.
ops={}
def add(code,name,form=''):ops[code]=(name,form)
for code,name in enumerate(['nop','break','ldarg.0','ldarg.1','ldarg.2','ldarg.3','ldloc.0','ldloc.1','ldloc.2','ldloc.3','stloc.0','stloc.1','stloc.2','stloc.3']):add(code,name)
for code,name in [(14,'ldarg.s'),(15,'ldarga.s'),(16,'starg.s'),(17,'ldloc.s'),(18,'ldloca.s'),(19,'stloc.s')]:add(code,name,'U1')
add(20,'ldnull')
for code in range(21,31):add(code,'ldc.i4.'+str(code-22))
for code,name,form in [(31,'ldc.i4.s','I1'),(32,'ldc.i4','I4'),(33,'ldc.i8','I8'),(34,'ldc.r4','F4'),(35,'ldc.r8','F8'),(37,'dup',''),(38,'pop',''),(39,'jmp','T'),(40,'call','T'),(41,'calli','T'),(42,'ret','')]:add(code,name,form)
branches=['br','brfalse','brtrue','beq','bge','bgt','ble','blt','bne.un','bge.un','bgt.un','ble.un','blt.un']
for i,name in enumerate(branches):add(43+i,name+'.s','R1');add(56+i,name,'R4')
add(69,'switch','SW')
for code,name in [(88,'add'),(89,'sub'),(90,'mul'),(91,'div'),(92,'div.un'),(93,'rem'),(94,'rem.un'),(95,'and'),(96,'or'),(97,'xor'),(98,'shl'),(99,'shr'),(100,'shr.un'),(101,'neg'),(102,'not'),(103,'conv.i1'),(104,'conv.i2'),(105,'conv.i4'),(106,'conv.i8'),(107,'conv.r4'),(108,'conv.r8'),(109,'conv.u4'),(110,'conv.u8')]:add(code,name)
for code,name in [(111,'callvirt'),(112,'cpobj'),(113,'ldobj'),(114,'ldstr'),(115,'newobj'),(116,'castclass'),(117,'isinst'),(121,'unbox'),(123,'ldfld'),(124,'ldflda'),(125,'stfld'),(126,'ldsfld'),(127,'ldsflda'),(128,'stsfld'),(129,'stobj'),(140,'box'),(141,'newarr'),(143,'ldelema'),(163,'ldelem'),(164,'stelem'),(165,'unbox.any'),(208,'ldtoken')]:add(code,name,'T')
add(122,'throw');add(142,'ldlen')
for code,name in [(144,'ldelem.i1'),(145,'ldelem.u1'),(146,'ldelem.i2'),(147,'ldelem.u2'),(148,'ldelem.i4'),(149,'ldelem.u4'),(150,'ldelem.i8'),(151,'ldelem.i'),(152,'ldelem.r4'),(153,'ldelem.r8'),(154,'ldelem.ref'),(155,'stelem.i'),(156,'stelem.i1'),(157,'stelem.i2'),(158,'stelem.i4'),(159,'stelem.i8'),(160,'stelem.r4'),(161,'stelem.r8'),(162,'stelem.ref'),(211,'conv.i'),(220,'endfinally')]:add(code,name)
add(221,'leave','R4');add(222,'leave.s','R1')
for code,name in [(0xfe01,'ceq'),(0xfe02,'cgt'),(0xfe03,'cgt.un'),(0xfe04,'clt'),(0xfe05,'clt.un'),(0xfe1a,'rethrow')]:add(code,name)
for code,name in [(0xfe06,'ldftn'),(0xfe07,'ldvirtftn'),(0xfe15,'initobj'),(0xfe16,'constrained.')]:add(code,name,'T')
print('IDENTITY',len(b),hashlib.sha256(b).hexdigest(),'SECTIONS',sections,'STREAMS',streams,'COUNTS',counts)
print('TYPES',types)
print('TOKENS',json.dumps({hex(k):v for k,v in names.items()},ensure_ascii=False))
selection={int(x,0) for x in sys.argv[1:]} if len(sys.argv)>1 else set(range(1,len(tables[6])+1))
for rid,r in enumerate(tables[6],1):
 if rid not in selection:continue
 o=off(r[0]);h=b[o]; flags=0;ls=0
 if h&3==2: sz=h>>2;hs=1
 else: flags=u(o,2);hs=(flags>>12)*4;sz=u(o+4);ls=u(o+8)
 st=o+hs;end=st+sz;q=st;starts=set();targets=[]
 print(f'METHOD {rid} {names[0x06000000+rid]} RVA={r[0]:x} FILE=[{o},{end}) HEADER={hs} CODE={sz} FLAGS={flags:x} LOCALS={ls:x} SIG={blob(r[4])}')
 while q<end:
  at=q;starts.add(at-st);code=b[q];q+=1
  if code==254:code=0xfe00|b[q];q+=1
  if code not in ops: raise ValueError(f'unknown opcode {code:x} at {at:x}')
  name,f=ops[code];v=''
  if f=='T':x=u(q);q+=4;v=f'{x:08x} '+token(x)
  elif f in ('U1','I1','I4','I8','F4','F8','R1','R4'):
   szf={'U1':1,'I1':1,'I4':4,'I8':8,'F4':4,'F8':8,'R1':1,'R4':4}[f]
   x=struct.unpack('<'+{'U1':'B','I1':'b','I4':'i','I8':'q','F4':'f','F8':'d','R1':'b','R4':'i'}[f],b[q:q+szf])[0];q+=szf
   if f.startswith('R'):x=q-st+x;targets.append(x);v=f'IL_{x:04x}'
   else:v=str(x)
  elif f=='SW':
   count=u(q);q+=4;dest=q+4*count;vv=[]
   for j in range(count):vv.append(dest-st+struct.unpack('<i',b[q:q+4])[0]);q+=4
   targets.extend(vv);v=str(vv)
  print(f'  file {at:04x} IL_{at-st:04x} {name} {v}')
 assert q==end and all(t in starts or t==end-st for t in targets)
 print('BRANCH_TARGETS_VALID',len(targets))
 if flags&8:
  eh=(end+3)&~3;kind=b[eh];size=u(eh+1,3) if kind&64 else b[eh+1];print('EH_SECTION',eh,kind,size,b[eh:eh+size].hex())
  step=24 if kind&64 else 12
  for z in range(eh+4,eh+size,step):
   vals=struct.unpack('<IIIIII' if kind&64 else '<HHBHBI',b[z:z+step]);print('EH_CLAUSE',vals,token(vals[-1]))
