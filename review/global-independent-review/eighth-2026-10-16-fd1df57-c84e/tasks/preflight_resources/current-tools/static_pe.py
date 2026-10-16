"""Bounded static PE reader. Reads bytes only; never loads target libraries."""
import pathlib,struct,json,sys,hashlib
class PE:
 def __init__(self,p):
  self.p=pathlib.Path(p);self.b=self.p.read_bytes();b=self.b
  self.pe=self.u(0x3c,4);assert b[:2]==b'MZ' and b[self.pe:self.pe+4]==b'PE\0\0'
  self.c=self.pe+4;self.n=self.u(self.c+2,2);self.oz=self.u(self.c+16,2);self.o=self.c+20;self.magic=self.u(self.o,2);self.w=8 if self.magic==0x20b else 4;self.base=self.u(self.o+(24 if self.w==8 else 28),self.w);self.dd=self.o+(112 if self.w==8 else 96);self.sections=[]
  for i in range(self.n):
   s=self.o+self.oz+i*40;n=b[s:s+8].split(b'\0')[0].decode();vsize,rva,size,off=struct.unpack_from('<4I',b,s+8);self.sections.append(dict(name=n,header=[s,s+40],rva=rva,virtual_size=vsize,raw_size=size,offset=off,flags=self.u(s+36,4)))
 def u(self,o,n):return int.from_bytes(self.b[o:o+n],'little')
 def off(self,r):
  for s in self.sections:
   if s['rva']<=r<s['rva']+max(s['virtual_size'],s['raw_size']):return r-s['rva']+s['offset']
  if r<self.u(self.o+60,4):return r
  raise ValueError(hex(r))
 def z(self,o):return self.b[o:self.b.index(0,o)].decode('utf-8',errors='replace')
 def structure(self):
  bounds={0,len(self.b),0x40,self.pe,self.pe+4,self.c+20,self.o+self.oz,self.o+self.oz+40*self.n,self.u(self.o+60,4)}
  for s in self.sections:bounds.update([s['offset'],s['offset']+s['raw_size']])
  bs=sorted(x for x in bounds if 0<=x<=len(self.b));regions=[]
  for a,b in zip(bs,bs[1:]):
   labels=[s['name'] for s in self.sections if s['offset']<=a<b<=s['offset']+s['raw_size']];regions.append({'start':a,'end_exclusive':b,'kind':labels or ['headers_stub_gap_or_overlay'],'sha256':hashlib.sha256(self.b[a:b]).hexdigest(),'semantic_status':'UNREAD'})
  dirs=[dict(index=i,rva=self.u(self.dd+8*i,4),size=self.u(self.dd+8*i+4,4)) for i in range(self.u(self.dd-4,4))]
  fields={'dos_signature':self.b[:2].hex(),'pe_offset':self.pe,'machine':hex(self.u(self.c,2)),'sections_count':self.n,'timestamp':self.u(self.c+4,4),'symbol_table_offset':self.u(self.c+8,4),'symbol_count':self.u(self.c+12,4),'optional_size':self.oz,'coff_flags':hex(self.u(self.c+18,2)),'optional_magic':hex(self.magic),'entry_rva':hex(self.u(self.o+16,4)),'image_base':hex(self.base),'section_alignment':self.u(self.o+32,4),'file_alignment':self.u(self.o+36,4),'size_image':self.u(self.o+56,4),'size_headers':self.u(self.o+60,4),'checksum':self.u(self.o+64,4),'subsystem':self.u(self.o+68,2),'dll_flags':hex(self.u(self.o+70,2))}
  imports=[]
  if dirs[1]['rva']:
   o=self.off(dirs[1]['rva'])
   while self.u(o,4) or self.u(o+12,4):
    ilt=self.u(o,4) or self.u(o+16,4);iat=self.u(o+16,4);dll=self.z(self.off(self.u(o+12,4)));ts=[];t=self.off(ilt);i=0
    while self.u(t+i*self.w,self.w):
     v=self.u(t+i*self.w,self.w);ts.append({'iat_rva':iat+i*self.w,'name':f'ordinal:{v&65535}' if v>>(self.w*8-1) else self.z(self.off(v)+2)});i+=1
    imports.append({'dll':dll,'entries':ts});o+=20
  return {'path':str(self.p),'bytes':len(self.b),'fields':fields,'directories':dirs,'sections':self.sections,'continuous_partition':regions,'imports':imports,'qualification':'STRUCTURE_ONLY; neither strings nor imports prove host behavior'}
 def clrhead(self):
  r=self.u(self.dd+14*8,4)
  if not r:return None
  c=self.off(r);m=self.off(self.u(c+8,4));vlen=self.u(m+12,4);a=(m+16+vlen+3)&~3;streams={};n=self.u(a+2,2);a+=4
  for i in range(n):
   off,sz=struct.unpack_from('<II',self.b,a);name=self.z(a+8);streams[name]=(m+off,sz);a=(a+8+len(name)+1+3)&~3
  t,sz=streams.get('#~',streams.get('#-'));valid=self.u(t+8,8);counts={};a=t+24
  for i in range(64):
   if valid>>i&1:counts[i]=self.u(a,4);a+=4
  return {'clr_offset':c,'metadata_offset':m,'metadata_size':self.u(c+12,4),'flags':self.u(c+16,4),'entry_token':hex(self.u(c+20,4)),'version':self.b[m+16:m+16+vlen].decode(errors='replace'),'streams':streams,'tables_offset':t,'data_offset':a,'heap_sizes':self.u(t+6,1),'counts':counts}
if __name__=='__main__':
 for p in sys.argv[1:]:
  pe=PE(p);print(json.dumps({'pe':pe.structure(),'clr':pe.clrhead()},ensure_ascii=False,indent=2))
