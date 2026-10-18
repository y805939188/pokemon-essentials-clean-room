"""Bounded data-only decoder for this font's complete OpenType layouts and legacy kerning."""
from pathlib import Path
import json,struct,hashlib
ROOT=Path(__file__).resolve().parent
D=(ROOT.parent/'binary_remaining_texts'/'embedded-font.ttf').read_bytes()
T=json.loads((ROOT/'decoded-tables.json').read_text())['tables']
RAW=[]
ACTIVE=None
def u(b,p): assert 0<=p<=len(b)-2;return struct.unpack_from('>H',b,p)[0]
def s(b,p): assert 0<=p<=len(b)-2;return struct.unpack_from('>h',b,p)[0]
def a(b,p,n): return [u(b,p+2*i) for i in range(n)]
def raw(tag): t=T[tag];return D[t['offset']:t['offset']+t['length']]
def cov(b,p):
 f=u(b,p);n=u(b,p+2)
 if f==1:
  values=a(b,p+4,n);RAW.append({'table':ACTIVE,'kind':'Coverage','offset':p,'format':f,'count':n,'glyphs':values});return values
 assert f==2
 out=[];ranges=[]
 for i in range(n):
  start,end,idx=a(b,p+4+6*i,3);assert idx==len(out);ranges.append([start,end,idx]);out+=list(range(start,end+1))
 RAW.append({'table':ACTIVE,'kind':'Coverage','offset':p,'format':f,'count':n,'ranges':ranges})
 return out
def cls(b,p):
 if not p:return []
 f=u(b,p)
 if f==1:
  start,n=a(b,p+2,2);values=[u(b,p+6+2*i) for i in range(n)];RAW.append({'table':ACTIVE,'kind':'ClassDef','offset':p,'format':f,'start':start,'count':n,'values':values});return [[start+i,v] for i,v in enumerate(values)]
 assert f==2
 values=[a(b,p+4+6*i,3) for i in range(u(b,p+2))];RAW.append({'table':ACTIVE,'kind':'ClassDef','offset':p,'format':f,'count':len(values),'ranges':values});return values
def anchor(b,p):
 if not p:return None
 f=u(b,p);out={'format':f,'xy':[s(b,p+2),s(b,p+4)]}
 if f==2:out['point']=u(b,p+6)
 if f==3:
  out['devices']=[device(b,p+u(b,p+k)) if u(b,p+k) else None for k in (6,8)]
 assert f in (1,2,3);return out
def device(b,p):
 first,last,fmt=a(b,p,3)
 assert fmt in (1,2,3)
 bits=1<<fmt;num=(last-first+1)*bits;words=a(b,p+6,(num+15)//16)
 return {'start':first,'end':last,'format':fmt,'packed':words}
def value(b,p,fmt,base):
 vals={}
 for k,name in enumerate(['xPlacement','yPlacement','xAdvance','yAdvance','xPlaDevice','yPlaDevice','xAdvDevice','yAdvDevice']):
  if fmt&(1<<k):
   v=s(b,p) if k<4 else u(b,p);p+=2
   vals[name]=v if k<4 or not v else device(b,base+v)
 assert not fmt&0xff00
 return vals,p
def layout(tag):
 global ACTIVE
 ACTIVE=tag
 b=raw(tag);assert a(b,0,2)==[1,0]
 script,feature,lookup=a(b,4,3);out={'header':[1,0,script,feature,lookup],'scripts':[],'features':[],'lookups':[]}
 for i in range(u(b,script)):
  p=script+2+6*i;name=b[p:p+4].decode('ascii');q=script+u(b,p+4);default=u(b,q);langs=[]
  for lang,off in ([('default',default)] if default else [])+[(b[q+4+6*j:q+8+6*j].decode('ascii'),u(b,q+8+6*j)) for j in range(u(b,q+2))]:
   z=q+off;assert u(b,z)==0;langs.append({'lang':lang,'requiredFeature':u(b,z+2),'features':a(b,z+6,u(b,z+4))})
  out['scripts'].append({'script':name,'langs':langs})
 for i in range(u(b,feature)):
  p=feature+2+6*i;name=b[p:p+4].decode('ascii');q=feature+u(b,p+4);assert u(b,q)==0
  out['features'].append({'tag':name,'lookups':a(b,q+4,u(b,q+2))})
 for i in range(u(b,lookup)):
  p=lookup+u(b,lookup+2+2*i);typ,flag,n=a(b,p,3);subs=[]
  assert not flag&16
  for j in range(n):
   q=p+u(b,p+6+2*j);fmt=u(b,q);r={'offset':q,'format':fmt}
   if (tag=='GPOS' and typ==8) or (tag=='GSUB' and typ==6):
    assert fmt==3;z=q+2
    for field in ['backtrack','input','lookahead']:
     nc=u(b,z);z+=2;r[field]=[cov(b,q+v) for v in a(b,z,nc)];z+=2*nc
    nr=u(b,z);z+=2;r['apply']=[a(b,z+4*k,2) for k in range(nr)]
   else:
    coverage=cov(b,q+u(b,q+2));r['coverage']=coverage
    if tag=='GSUB' and typ==1:
     assert fmt==1;r['delta']=s(b,q+4);r['mapping']=[[g,(g+s(b,q+4))&65535] for g in coverage]
    elif tag=='GSUB' and typ==4:
     assert fmt==1 and u(b,q+4)==len(coverage);r['ligatures']=[]
     for g,off in zip(coverage,a(b,q+6,len(coverage))):
      z=q+off
      for lo in a(b,z+2,u(b,z)):
       v=z+lo;result,nc=a(b,v,2);r['ligatures'].append({'input':[g]+a(b,v+4,nc-1),'output':result})
    elif tag=='GPOS' and typ==1:
     vf=u(b,q+4);r['valueFormat']=vf;r['values']=[];z=q+6
     if fmt==1:
      v,z=value(b,z,vf,q);r['values']=[v]
     else:
      assert fmt==2;nv=u(b,z);z+=2;assert nv==len(coverage)
      for k in range(nv):v,z=value(b,z,vf,q);r['values'].append(v)
    elif tag=='GPOS' and typ==2:
     assert fmt==1;vf1,vf2,nset=a(b,q+4,3);assert nset==len(coverage)
     r['valueFormats']=[vf1,vf2];r['pairs']=[]
     for first,off in zip(coverage,a(b,q+10,nset)):
      z=q+off;np=u(b,z);z+=2
      for k in range(np):
       second=u(b,z);z+=2;v1,z=value(b,z,vf1,q);v2,z=value(b,z,vf2,q)
       r['pairs'].append([first,second,v1,v2])
    elif tag=='GPOS' and typ==4:
     assert fmt==1;basecov=cov(b,q+u(b,q+4));nc,mo,bo=a(b,q+6,3);mp=q+mo;bp=q+bo
     assert u(b,mp)==len(coverage) and u(b,bp)==len(basecov)
     r['classCount']=nc;r['marks']=[];r['bases']=[]
     for k,g in enumerate(coverage):
      c,off=a(b,mp+2+4*k,2);assert c<nc;r['marks'].append([g,c,anchor(b,mp+off) if off else None])
     for k,g in enumerate(basecov):r['bases'].append([g,[anchor(b,bp+off) if off else None for off in a(b,bp+2+2*nc*k,nc)]])
    else:raise AssertionError((tag,typ,fmt))
   subs.append(r)
  out['lookups'].append({'index':i,'type':typ,'flag':flag,'subtables':subs})
 return out
OUT={tag:layout(tag) for tag in ['GSUB','GPOS']}
ACTIVE='GDEF'
b=raw('GDEF');assert a(b,0,2)==[1,0];gclass,attach,caret,mclass=a(b,4,4);assert attach==0
lig=[]
if caret:
 cc=cov(b,caret+u(b,caret));assert len(cc)==u(b,caret+2)
 for gid,off in zip(cc,a(b,caret+4,len(cc))):
  q=caret+off;vals=[]
  for co in a(b,q+2,u(b,q)):
   z=q+co;fmt=u(b,z);assert fmt in (1,2,3)
   vals.append({'format':fmt,'value':s(b,z+2) if fmt!=2 else u(b,z+2),'device':device(b,z+u(b,z+4)) if fmt==3 and u(b,z+4) else None})
  lig.append([gid,vals])
OUT['GDEF']={'version':[1,0],'offsets':[gclass,attach,caret,mclass],'glyphClassDef':cls(b,gclass),'attachList':[],'ligCaretList':lig,'markAttachClassDef':cls(b,mclass)}
b=raw('kern');version,n=a(b,0,2);assert version==0;p=4;subs=[]
for i in range(n):
 v,length,coverage,np,search,entry,shift=a(b,p,7);assert v==0 and coverage>>8==0
 pairs=[[u(b,p+14+6*j),u(b,p+16+6*j),s(b,p+18+6*j)] for j in range(np)]
 assert length==14+6*np;subs.append({'offset':p,'length':length,'coverage':coverage,'nPairs':np,'searchRange':search,'entrySelector':entry,'rangeShift':shift,'pairs':pairs});p+=length
assert p==len(b);OUT['kern']={'version':version,'subtables':subs}
(ROOT/'decoded-layout.json').write_text(json.dumps(OUT,ensure_ascii=False,indent=2)+'\n')
(ROOT/'raw-layout-structures.json').write_text(json.dumps(RAW,indent=2)+'\n')
(ROOT/'raw-layout-structures.read.txt').write_text('\n'.join(json.dumps(x,separators=(',',':')) for x in RAW)+'\n')
lines=[]
for tag,lay in OUT.items():
 if tag in ('GDEF','kern'):lines.append(tag+' '+json.dumps(lay,separators=(',',':')));continue
 lines.append(tag+' header/scripts/features '+json.dumps({k:v for k,v in lay.items() if k!='lookups'},separators=(',',':')))
 for lookup in lay['lookups']:
  lines.append(tag+' lookup '+json.dumps({k:v for k,v in lookup.items() if k!='subtables'},separators=(',',':')))
  for sub in lookup['subtables']:lines.append(json.dumps(sub,separators=(',',':')))
(ROOT/'layout.compact.txt').write_text('\n'.join(lines)+'\n')
print(json.dumps({'lookups':{t:len(OUT[t]['lookups']) for t in ['GSUB','GPOS']},'kernPairs':sum(s['nPairs'] for s in subs),'layoutBytes':(ROOT/'layout.compact.txt').stat().st_size}))
