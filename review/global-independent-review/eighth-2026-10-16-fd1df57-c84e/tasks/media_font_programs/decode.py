"""Read-only bounded font-data decoder; no font interpreter, rendering, or imports of font code."""
from pathlib import Path
import struct,json,hashlib,ast,datetime,sys
ROOT=Path(__file__).resolve().parent
INPUT=ROOT.parent/'binary_remaining_texts'/'embedded-font.ttf'
DATA=INPUT.read_bytes()
assert len(DATA)==350200 and hashlib.sha256(DATA).hexdigest()=='e5b0af421ea2bfbc1ac8d251d647268087ae82786234c57f757d1f0b90fa8b49'
def unpack(fmt,b,p):
    n=struct.calcsize('>'+fmt)
    assert 0<=p<=len(b)-n,(fmt,p,len(b))
    return struct.unpack_from('>'+fmt,b,p)
def u(b,p): return unpack('H',b,p)[0]
def s(b,p): return unpack('h',b,p)[0]
def ul(b,p): return unpack('I',b,p)[0]
def arr(b,p,n): return list(unpack(str(n)+'H',b,p)) if n else []
def save(n,v): (ROOT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def digest(b): return hashlib.sha256(b).hexdigest()
# Read instruction metadata as literal data, without importing or executing the dependency.
meta_path=Path('/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/fontTools/ttLib/tables/ttProgram.py')
node=ast.parse(meta_path.read_text())
meta={}
for item in node.body:
    if isinstance(item,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ['instructions','streamInstructions'] for t in item.targets):
        for op,name,bits,desc,pops,pushes in ast.literal_eval(item.value):
            for off in range(1<<bits): meta[op+off]=(name,off,bits,desc,pops,pushes)
def disasm(b):
    out=[];p=0
    while p<len(b):
        a=p;op=b[p];p+=1
        assert op in meta,('unknown opcode',a,op)
        name,flags,bits,desc,pops,pushes=meta[op];vals=[]
        if name.startswith('PUSH') or name.startswith('NPUSH'):
            if op in (64,65): n=b[p];p+=1
            else: n=(op&7)+1
            if name.endswith('W'): vals=list(unpack(str(n)+'h',b,p));p+=2*n
            else: assert p+n<=len(b);vals=list(b[p:p+n]);p+=n
        out.append({'pc':a,'end':p,'op':op,'name':name,'flags':flags if bits else None,'values':vals})
    return out
N=u(DATA,4);TABLES={}
for i in range(N):
    p=12+16*i;tag=DATA[p:p+4].decode('ascii');check,start,size=unpack('III',DATA,p+4)
    assert start+size<=len(DATA)
    TABLES[tag]={'offset':start,'length':size,'checksum':check,'sha256':digest(DATA[start:start+size])}
def table(tag):
    t=TABLES[tag];return DATA[t['offset']:t['offset']+t['length']]
head=table('head');hhea=table('hhea');maxp=table('maxp');count=u(maxp,4)
assert count==2587 and s(head,50)==1
loca=[ul(table('loca'),i*4) for i in range(count+1)]
assert loca==sorted(loca) and loca[-1]==len(table('glyf'))
hmetrics=u(hhea,34);hmtx=table('hmtx')
metrics=[list(unpack('Hh',hmtx,4*i)) for i in range(hmetrics)]
metrics += [[metrics[-1][0],s(hmtx,4*hmetrics+2*i)] for i in range(count-hmetrics)]
GLYPHS=[];PROGRAMS=[{'unit':'fpgm','offset':TABLES['fpgm']['offset'],'bytes':len(table('fpgm')),'sha256':digest(table('fpgm')),'code':disasm(table('fpgm'))},{'unit':'prep','offset':TABLES['prep']['offset'],'bytes':len(table('prep')),'sha256':digest(table('prep')),'code':disasm(table('prep'))}]
for gid in range(count):
    b=table('glyf')[loca[gid]:loca[gid+1]]
    g={'gid':gid,'range':[loca[gid],loca[gid+1]],'sha256':digest(b),'hmetric':metrics[gid]}
    if not b: g['kind']='empty';GLYPHS.append(g);continue
    contours,x0,y0,x1,y1=unpack('hhhhh',b,0);g.update(contours=contours,bbox=[x0,y0,x1,y1]);p=10
    if contours>=0:
        g['kind']='simple';ends=arr(b,p,contours);p+=contours*2
        assert ends==sorted(ends)
        n=ends[-1]+1 if ends else 0;g['endPoints']=ends
        inslen=u(b,p);p+=2;insstart=p;ins=b[p:p+inslen];p+=inslen
        flags=[]
        while len(flags)<n:
            f=b[p];p+=1;repeat=1
            if f&8: repeat+=b[p];p+=1
            flags += [f]*repeat
        assert len(flags)==n
        coords=[]
        for short,same in [(2,16),(4,32)]:
            v=0;vs=[]
            for f in flags:
                if f&short:
                    delta=b[p];p+=1
                    if not f&same: delta=-delta
                elif f&same: delta=0
                else: delta=s(b,p);p+=2
                v+=delta;vs.append(v)
            coords.append(vs)
        g['points']=[[x,y,f&1,bool(f&64)] for x,y,f in zip(*coords,flags)]
    else:
        assert contours==-1
        g['kind']='composite';cs=[]
        while True:
            flag,child=unpack('HH',b,p);p+=4;assert child<count
            words=bool(flag&1);xy=bool(flag&2)
            fmt=('hh' if xy else 'HH') if words else ('bb' if xy else 'BB')
            args=unpack(fmt,b,p);p+=struct.calcsize('>'+fmt)
            matrix=[]
            if flag&8: matrix=list(unpack('h',b,p));p+=2
            elif flag&64: matrix=list(unpack('hh',b,p));p+=4
            elif flag&128: matrix=list(unpack('hhhh',b,p));p+=8
            cs.append({'flags':flag,'child':child,'args':args,'args_kind':'translation_font_units' if xy else 'point_indices','matrix_F2Dot14':matrix})
            if not flag&32: break
        g['components']=cs;inslen=0;ins=b'';insstart=p
        if flag&256: inslen=u(b,p);p+=2;insstart=p;ins=b[p:p+inslen];p+=inslen
    assert p<=len(b) and len(b)-p<=3,(gid,p,len(b))
    g.update(instructionLength=inslen,instructionOffset=TABLES['glyf']['offset']+loca[gid]+insstart,padding=b[p:].hex())
    if inslen:
        PROGRAMS.append({'unit':f'g{gid}','offset':g['instructionOffset'],'bytes':inslen,'sha256':digest(ins),'code':disasm(ins)})
    GLYPHS.append(g)
# Full raw directory and numerical interpretation retained separately from reading credit.
HEAD={'version':ul(head,0),'fontRevision':ul(head,4),'checksumAdjustment':ul(head,8),'magic':ul(head,12),'flags':u(head,16),'unitsPerEm':u(head,18),'created':unpack('Q',head,20)[0],'modified':unpack('Q',head,28)[0],'bbox':list(unpack('hhhh',head,36)),'macStyle':u(head,44),'lowestRecPPEM':u(head,46),'fontDirectionHint':s(head,48),'indexToLocFormat':s(head,50),'glyphDataFormat':s(head,52)}
HHEA={'version':ul(hhea,0),'ascent':s(hhea,4),'descent':s(hhea,6),'lineGap':s(hhea,8),'advanceWidthMax':u(hhea,10),'minLSB':s(hhea,12),'minRSB':s(hhea,14),'xMaxExtent':s(hhea,16),'caretSlopeRise':s(hhea,18),'caretSlopeRun':s(hhea,20),'caretOffset':s(hhea,22),'reserved':arr(hhea,24,4),'metricDataFormat':s(hhea,32),'numberOfHMetrics':hmetrics}
MAXP=dict(zip(['version','numGlyphs','maxPoints','maxContours','maxCompositePoints','maxCompositeContours','maxZones','maxTwilightPoints','maxStorage','maxFunctionDefs','maxInstructionDefs','maxStackElements','maxSizeOfInstructions','maxComponentElements','maxComponentDepth'],[ul(maxp,0)]+arr(maxp,4,14)))
save('decoded-tables.json',{'tables':TABLES,'head':HEAD,'hhea':HHEA,'maxp':MAXP,'cvt':list(unpack(str(len(table('cvt '))//2)+'h',table('cvt '),0)),'loca':loca})
save('decoded-glyphs.json',GLYPHS);save('decoded-programs.json',PROGRAMS)
lines=[]
for prog in PROGRAMS:
    tokens=[]
    for ins in prog['code']:
        name=ins['name']
        if ins['values']: token=('W' if name.endswith('W') else 'B')+'('+','.join(map(str,ins['values']))+')'
        else: token=name+('['+format(ins['flags'],'b')+']' if ins['flags'] is not None else '')
        tokens.append(str(ins['pc'])+':'+token)
    lines.append(prog['unit']+' bytes='+str(prog['bytes'])+' '+' '.join(tokens))
(ROOT/'programs.compact.txt').write_text('\n'.join(lines)+'\n')
print(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tables':N,'glyphs':count,'kinds':{k:sum(g['kind']==k for g in GLYPHS) for k in ['empty','simple','composite']},'programs':len(PROGRAMS),'programBytes':sum(p['bytes'] for p in PROGRAMS),'opcodes':sum(len(p['code']) for p in PROGRAMS),'compactBytes':sum(map(len,lines))}))
