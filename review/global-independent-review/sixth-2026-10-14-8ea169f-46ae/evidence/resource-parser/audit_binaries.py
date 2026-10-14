"""Bounded PE/CLI metadata reader. Never maps, loads or executes an input.

No external dependency; writes sanitized interface data, not disassembled source.
--inspect-il N prints decoded instructions transiently for human static review.
"""
from audit_resources import ROOT, OUT, PIN, Reader, require, sha, save
import collections
import json
import re
import struct
import sys
import uuid

class PE(Reader):
    def __init__(self,b):
        super().__init__(b)
        require(self.span(0,2)==b'MZ','DOS signature')
        pe=self.unpack('<I',60)[0];require(self.span(pe,4)==b'PE\0\0','PE signature')
        self.machine,ns,stamp,sym,nsym,optlen,flags=self.unpack('<HHIIIHH',pe+4)
        self.symoff,self.nsym=sym,nsym
        self.strbase=sym+18*nsym if sym else 0
        self.strsize=self.unpack('<I',self.strbase)[0] if sym else 0
        if sym:self.span(self.strbase,self.strsize)
        opt=pe+24;magic=self.unpack('<H',opt)[0];require(magic in (0x10b,0x20b),'optional magic')
        self.wide=magic==0x20b; self.imagebase=self.unpack('<Q' if self.wide else '<I',opt+(24 if self.wide else 28))[0]
        self.entry=self.unpack('<I',opt+16)[0];self.headers=self.unpack('<I',opt+60)[0]
        nd=self.unpack('<I',opt+(108 if self.wide else 92))[0];require(nd<=16,'directory count')
        ds=opt+(112 if self.wide else 96);require(ds+nd*8<=opt+optlen,'directory beyond optional header')
        self.dirs=[self.unpack('<II',ds+8*i) for i in range(nd)]+[(0,0)]*(16-nd)
        self.sections=[]
        for i in range(ns):
            p=opt+optlen+i*40; nm,vs,va,sz,off,rel,ln,nrel,nln,fl=self.unpack('<8sIIIIIIHHI',p)
            self.span(off,sz)
            name=nm.rstrip(b'\0').decode('ascii','replace')
            if name.startswith('/') and name[1:].isdigit():name=self.coff_string(int(name[1:]))
            self.sections.append({'name':name,'virtual_size':vs,'rva':va,'size':sz,'offset':off,'flags':fl,'sha256':sha(self.span(off,sz))})
        self.meta={'machine':self.machine,'PE32_plus':self.wide,'entry_rva':self.entry,'image_base':self.imagebase,
            'sections':self.sections,'directories':[{'index':i,'address':v[0],'size':v[1]} for i,v in enumerate(self.dirs)],'coff_symbol_count':nsym}
    def coff_string(self,ix):
        require(4<=ix<self.strsize,'COFF string index');return self.cstr(self.strbase+ix,self.strsize-ix)
    def coff_symbols(self):
        out=[];i=0
        while i<self.nsym:
            p=self.symoff+18*i;nm,value,section,typ,storage,aux=self.unpack('<8sIhHBB',p)
            name=self.coff_string(int.from_bytes(nm[4:],'little')) if nm[:4]==b'\0'*4 else nm.rstrip(b'\0').decode('ascii','replace')
            require(i+1+aux<=self.nsym,'COFF aux count');ab=self.span(p+18,18*aux)
            row={'index':i,'name':name,'section_number':section,'section_name':self.sections[section-1]['name'] if section>0 and section<=len(self.sections) else None,
                'value':value,'type':typ,'storage_class':storage,'auxiliary_count':aux}
            if aux:
                row['aux_sha256']=sha(ab)
                if storage==103:row['file_name']=ab.rstrip(b'\0').decode('utf8','replace')
                elif storage==3 and aux==1:row['section_aux_fields']=list(struct.unpack('<IHHIHB3s',ab))[:-1]
                else:row['aux_data_hex']=ab.hex()
            out.append(row);i+=1+aux
        return out
    def offset(self,rva,size=1):
        if rva<self.headers:
            self.span(rva,size);return rva
        match=[s for s in self.sections if s['rva']<=rva and rva+size<=s['rva']+s['size']]
        require(len(match)==1,'unmapped/ambiguous RVA')
        return match[0]['offset']+rva-match[0]['rva']
    def cstr(self,off,limit=65536):
        require(0<=off<len(self.b),'bad string offset');end=self.b.find(b'\0',off,min(len(self.b),off+limit))
        require(end>=0,'unterminated string');return self.b[off:end].decode('utf8','replace')
    def imports(self):
        r,n=self.dirs[1];out=[]
        if not r:return out
        start=self.offset(r,n)
        for p in range(start,start+n-19,20):
            lookup,time,fwd,name,iat=self.unpack('<IIIII',p)
            if not any((lookup,time,fwd,name,iat)):break
            dll=self.cstr(self.offset(name));items=[];w=8 if self.wide else 4;f='<Q' if self.wide else '<I'
            table=self.offset(lookup or iat)
            for ix in range(65536):
                v=self.unpack(f,table+w*ix)[0]
                if not v:break
                entry={'iat_rva':iat+w*ix}
                if v & (1<<(w*8-1)):entry['ordinal']=v&65535
                else:
                    at=self.offset(v,2);entry.update(hint=self.unpack('<H',at)[0],name=self.cstr(at+2))
                items.append(entry)
            else:raise ValueError('import cap')
            out.append({'dll':dll,'symbols':items})
        return out
    def exports(self):
        r,n=self.dirs[0]
        if not r:return []
        p=self.offset(r,40);_,_,_,_,name,base,nfunc,nnames,func,nm,ordr=self.unpack('<IIHHIIIIIII',p)
        require(nfunc<100000 and nnames<=nfunc,'export count');names={}
        for i in range(nnames):
            ix=self.unpack('<H',self.offset(ordr+2*i,2))[0];require(ix<nfunc,'export ordinal')
            names[ix]=self.cstr(self.offset(self.unpack('<I',self.offset(nm+4*i,4))[0]))
        out=[]
        for i in range(nfunc):
            va=self.unpack('<I',self.offset(func+4*i,4))[0]
            if not va:continue
            out.append({'ordinal':base+i,'name':names.get(i),'rva':va,'forwarder':self.cstr(self.offset(va)) if r<=va<r+n else None})
        return out
    def resources(self):
        r,n=self.dirs[2];out=[]
        if not r:return out
        base=self.offset(r,n);seen=set()
        def walk(rel,path,depth):
            require(depth<=5 and rel not in seen,'resource cycle/depth');seen.add(rel)
            require(rel+16<=n,'resource directory bounds');at=base+rel
            nn,ni=self.unpack('<HH',at+12);require(rel+16+8*(nn+ni)<=n,'resource entries bounds')
            for j in range(nn+ni):
                key,ptr=self.unpack('<II',at+16+8*j)
                if key & 0x80000000:
                    ka=key&0x7fffffff;require(ka+2<=n,'resource name');ln=self.unpack('<H',base+ka)[0]
                    require(ka+2+ln*2<=n,'resource name length');key=self.span(base+ka+2,ln*2).decode('utf-16-le')
                if ptr & 0x80000000:walk(ptr&0x7fffffff,path+[key],depth+1)
                else:
                    require(ptr+16<=n,'resource leaf');va,sz,cp,_=self.unpack('<IIII',base+ptr);o=self.offset(va,sz);raw=self.span(o,sz)
                    row={'path':path+[key],'offset':o,'size':sz,'codepage':cp,'sha256':sha(raw)}
                    if path and path[0]==16:row['version']=version_resource(raw)
                    elif path and path[0]==24:
                        text=raw.rstrip(b'\0').decode('utf8','replace')
                        row['manifest_properties']={k:re.search(r'<'+k+r'\b[^>]*>([^<]+)</'+k+'>',text).group(1).strip() for k in ('dpiAware','dpiAwareness') if re.search(r'<'+k+r'\b[^>]*>([^<]+)</'+k+'>',text)}
                    elif path and path[0]==14:
                        rr=Reader(raw);reserved,typ,count=rr.unpack('<HHH',0);require(reserved==0 and typ==1 and 6+count*14==len(raw),'icon group')
                        row['icon_group']=[dict(zip(('width_byte','height_byte','color_count','reserved','planes','bpp','bytes','resource_id'),rr.unpack('<BBBBHHIH',6+14*i))) for i in range(count)]
                    elif path and path[0]==3 and raw[:4]==b'\x28\0\0\0':
                        rr=Reader(raw);size,w,h,planes,bpp,compression,imagesize,xppm,yppm,colors,important=rr.unpack('<IiiHHIIiiII',0)
                        row['icon_DIB']={'width':w,'height_including_mask':h,'planes':planes,'bits_per_pixel':bpp,'compression':compression,'image_size_field':imagesize,'palette_entries':colors}
                    elif path and path[0]==6:
                        ss=[];q=0
                        for k in range(16):
                            length=struct.unpack_from('<H',raw,q)[0];q+=2;ss.append(raw[q:q+2*length].decode('utf-16-le'));q+=2*length
                        row['string_table']=ss
                    else:row['content_review']='resource descriptor only; icon/image payload outside additional interface scope'
                    out.append(row)
        walk(0,[],0);return out
    def debug(self):
        r,n=self.dirs[6];out=[]
        if not r:return out
        require(n%28==0,'debug size')
        for i in range(n//28):
            _,ts,maj,mi,typ,sz,va,ptr=self.unpack('<IIHHIIII',self.offset(r+28*i,28));raw=self.span(ptr,sz)
            row={'type':typ,'size':sz,'offset':ptr,'sha256':sha(raw)}
            if typ==2 and raw[:4]==b'RSDS':row.update(format='RSDS',age=struct.unpack_from('<I',raw,20)[0],pdb_path=raw[24:].rstrip(b'\0').decode('utf8','replace'))
            out.append(row)
        return out

def version_resource(b):
    rd=Reader(b)
    def walk(p,end,depth):
        require(depth<=8,'version depth');ln,vln,typ=rd.unpack('<HHH',p);require(ln>=6 and p+ln<=end,'version bounds')
        q=p+6;key=[]
        while q+2<=p+ln:
            v=rd.unpack('<H',q)[0];q+=2
            if not v:break
            key.append(v)
        name=''.join(chr(c) for c in key);q=(q+3)&~3;vs=vln*2 if typ==1 else vln
        value=rd.span(q,vs) if vs else b'';require(q+vs<=p+ln,'version value')
        obj={'key':name}
        if typ==1:obj['value']=value.decode('utf-16-le').rstrip('\0')
        elif name=='VS_VERSION_INFO' and vs==52:obj['fixed_info_dwords']=list(struct.unpack('<13I',value))
        elif value:obj['value_hex']=value.hex()
        q=(q+vs+3)&~3;children=[]
        while q+6<=p+ln:
            cl=rd.unpack('<H',q)[0]
            if not cl:break
            children.append(walk(q,p+ln,depth+1));q=(q+cl+3)&~3
        if children:obj['children']=children
        return obj
    return walk(0,len(b),0)

def scan_strings(pe):
    # All bytes scanned; candidate strings are data. Native program snippets are
    # counted/hashed, never reproduced. Only short relevant interface labels kept.
    categories=collections.Counter();selected=[];pool=0
    patterns=[('soundfont_midi',r'(?i)soundfont|fluidsynth|\bmidi|synth\.'),
        ('audio_interface',r'(?i)^(?:bgm|bgs|me|se)_(?:play|stop|fade|pos)|^(?:BGMTrackCount|SESourceCount|Audio)$'),
        ('fonts',r'(?i)font|freetype'),('editor_windows',r'(?i)^(?:Batch Text Entry|Comment|Show Text|EDIT|Script|#32770|RPG Maker XP|Afx:|RPGXP-ExpandText-.*)$'),
        ('version',r'(?i)^(?:ruby [0-9]|zlib version|FluidSynth runtime|mkxp-z)')]
    for enc,pattern in [('ascii',rb'[\x20-\x7e]{4,}'),('utf-16-le',rb'(?:[\x20-\x7e]\x00){4,}')]:
        for m in re.finditer(pattern,pe.b):
            s=m.group().decode(enc);pool+=1
            if len(s)>200 or '\n' in s or s!=s.lstrip() or re.search(r'\b(?:def|class|module|uniform|varying)\s|[{};]|bitmap\.|</|<script',s):
                categories['long_or_code_like_not_reproduced']+=1;continue
            cat=next((c for c,p in patterns if re.search(p,s)),None)
            if cat:
                categories[cat]+=1;selected.append({'offset':m.start(),'encoding':enc,'category':cat,'text':s,
                    'evidence':'present_literal_only_not_reachability_or_behavior'})
            else:categories['other_strings_including_symbols_and_incidental_bytes']+=1
    return {'all_file_bytes_scanned':len(pe.b),'candidate_count':pool,'categories':dict(categories),'selected':selected,
        'not_claimed':'Unselected string candidates were not individually interpreted; selected literals do not prove their code path is reachable.'}

def embedded_readable_inventory(pe):
    blocks=[];controllers=[]
    for m in re.finditer(rb'[\x09\x0a\x0d\x20-\x7e]{500,}',pe.b):
        raw=m.group()
        if b'\n' not in raw:continue
        text=raw.decode('ascii');row={'offset':m.start(),'size':len(raw),'sha256':sha(raw),'lines':text.count('\n')}
        if raw.startswith(b'# Game Controller DB'):
            row['kind']='embedded_controller_mapping_data'
            for ln,line in enumerate(text.splitlines(),1):
                if not line or line.startswith('#'):continue
                fields=line.split(',');require(len(fields)>=3,'controller row')
                require(re.fullmatch('[0-9a-fA-F]{32}',fields[0]) is not None or fields[0]=='xinput','controller GUID')
                pairs=[]
                for f in fields[2:]:
                    if not f:continue
                    require(':' in f,'controller mapping');k,v=f.split(':',1);pairs.append({'control':k,'binding':v})
                controllers.append({'line':ln,'guid':fields[0],'name':fields[1],'mapping':pairs,'consumer':'embedded SDL mapping table; selected runtime backend unproved'})
            row['review']='all rows decoded as controller identifiers/bindings; activation and physical input unknown'
        elif 'module RPG' in text:
            row['kind']='embedded_RPG_compatibility_text'
            declarations=re.findall(r'^\s*(?:module|class|def)\s+([^\s(;]+)',text,re.M)
            row['declaration_count']=len(declarations)
            row['audio_interface_names']=sorted({v for v in declarations if v in ('AudioFile','BGM','BGS','ME','SE')})
            row['review']='interface inventory only; text is readable, not opaque machine code; binding/version selection not proven'
        elif re.search(r'\b(?:uniform|varying)\s',text):
            row['kind']='embedded_shader_text'
            row['input_names']=re.findall(r'\b(?:uniform|varying)\s+(?:(?:lowp|mediump|highp)\s+)?\w+\s+(\w+)',text)
            row['review']='shader input interface inventory; arithmetic/compiled shader paths not fully semantically reviewed'
        elif '<?xml' in text:
            row['kind']='manifest_text';row['review']='properties decoded in resource directory'
        else:
            row['kind']='other_printable_multiline_data';row['review']='structural inventory only; not represented as machine-code opacity'
        blocks.append(row)
    return {'blocks':blocks,'controller_records':controllers,'full_embedded_behavior_review':False}

def safe_literal(s):
    if len(s)>200 or '<animations>' in s:
        return {'characters':len(s),'sha256_utf8':sha(s.encode()),'meaning':'embedded usage/example text, read for context; source-like text omitted'}
    return s

# Metadata column definitions from ECMA-335 II.22/II.24. No runtime reflection.
CODED={'ResolutionScope':(2,[0,26,35,1]),'TypeDefOrRef':(2,[2,1,27]),
    'MemberRefParent':(3,[2,1,26,6,27]),'HasCustomAttribute':(5,[6,4,1,2,8,9,10,0,14,23,20,17,26,27,32,35,38,39,40,42,44,43]),
    'CustomAttributeType':(3,[None,None,6,10,None]),'HasSemantics':(1,[20,23])}
SCHEMA={0:('Module',[('Generation','u2'),('Name','s'),('Mvid','g'),('EncId','g'),('EncBaseId','g')]),
 1:('TypeRef',[('Scope','cResolutionScope'),('Name','s'),('Namespace','s')]),
 2:('TypeDef',[('Flags','u4'),('Name','s'),('Namespace','s'),('Extends','cTypeDefOrRef'),('FieldList','t4'),('MethodList','t6')]),
 4:('Field',[('Flags','u2'),('Name','s'),('Signature','b')]),
 6:('MethodDef',[('RVA','u4'),('ImplFlags','u2'),('Flags','u2'),('Name','s'),('Signature','b'),('ParamList','t8')]),
 8:('Param',[('Flags','u2'),('Sequence','u2'),('Name','s')]),
 9:('InterfaceImpl',[('Class','t2'),('Interface','cTypeDefOrRef')]),
 10:('MemberRef',[('Class','cMemberRefParent'),('Name','s'),('Signature','b')]),
 12:('CustomAttribute',[('Parent','cHasCustomAttribute'),('Type','cCustomAttributeType'),('Value','b')]),
 17:('StandAloneSig',[('Signature','b')]),
 21:('PropertyMap',[('Parent','t2'),('PropertyList','t23')]),
 23:('Property',[('Flags','u2'),('Name','s'),('Type','b')]),
 24:('MethodSemantics',[('Semantics','u2'),('Method','t6'),('Association','cHasSemantics')]),
 27:('TypeSpec',[('Signature','b')]),
 32:('Assembly',[('HashAlgId','u4'),('Major','u2'),('Minor','u2'),('Build','u2'),('Revision','u2'),('Flags','u4'),('PublicKey','b'),('Name','s'),('Culture','s')]),
 35:('AssemblyRef',[('Major','u2'),('Minor','u2'),('Build','u2'),('Revision','u2'),('Flags','u4'),('PublicKeyOrToken','b'),('Name','s'),('Culture','s'),('HashValue','b')])}

def compressed(rd,p):
    v=rd.span(p,1)[0]
    if v<128:return v,p+1
    if v<192:return ((v&63)<<8)|rd.span(p+1,1)[0],p+2
    require(v<224,'invalid compressed integer')
    return ((v&31)<<24)|int.from_bytes(rd.span(p+1,3),'big'),p+4

class CLI:
    def __init__(self,pe):
        self.pe=pe;r,n=pe.dirs[14];require(r and n>=72,'no CLI')
        p=pe.offset(r,72);cb,major,minor,mrva,msz,flags,entry=pe.unpack('<IHHIIII',p)
        self.header={'runtime':[major,minor],'flags':flags,'entry_token':entry,'metadata_size':msz}
        self.md=Reader(pe.span(pe.offset(mrva,msz),msz));rd=self.md;require(rd.span(0,4)==b'BSJB','metadata signature')
        vl=rd.unpack('<I',12)[0];self.header['version']=rd.span(16,vl).rstrip(b'\0').decode('ascii')
        p=16+vl;_,ns=rd.unpack('<HH',p);p+=4;self.streams={}
        for i in range(ns):
            o,z=rd.unpack('<II',p);q=p+8;end=rd.b.find(b'\0',q,q+32);require(end>=0,'stream name')
            name=rd.span(q,end-q).decode('ascii');require(name not in self.streams,'duplicate stream')
            self.streams[name]={'offset':o,'size':z,'sha256':sha(rd.span(o,z))};p=(end+4)&~3
        tr=self.stream('#~');reserved,major,minor,hsize,res=tr.unpack('<IBBBB',0);valid,sortedmask=tr.unpack('<QQ',8);q=24
        self.counts={}
        for i in range(64):
            if valid&(1<<i):self.counts[i]=tr.unpack('<I',q)[0];q+=4
        self.tables={};self.blobrefs=collections.defaultdict(list)
        def width(t):
            if t in ('u2','u4'):return int(t[1:])
            if t in ('s','g','b'):return 4 if hsize & {'s':1,'g':2,'b':4}[t] else 2
            if t.startswith('t'):return 4 if self.counts.get(int(t[1:]),0)>=65536 else 2
            bits,ids=CODED[t[1:]];return 4 if max(self.counts.get(i,0) for i in ids if i is not None)>=(1<<(16-bits)) else 2
        for tid,n in self.counts.items():
            require(tid in SCHEMA,f'unsupported metadata table {tid}')
            name,cols=SCHEMA[tid];rows=[]
            for ix in range(1,n+1):
                row={'token':(tid<<24)|ix,'row':ix}
                for cn,ct in cols:
                    w=width(ct);v=int.from_bytes(tr.span(q,w),'little');q+=w;row[cn]=v
                    if ct=='s':row[cn]=self.string(v)
                    elif ct=='b':self.blobrefs[v].append(f'{name}:{ix}:{cn}')
                    elif ct.startswith('c'):
                        bits,ids=CODED[ct[1:]];tag=v&((1<<bits)-1);rid=v>>bits
                        require(not v or tag<len(ids) and ids[tag] is not None and rid<=self.counts.get(ids[tag],0),'coded index')
                        row[cn+'_token']=(ids[tag]<<24)|rid if v else 0
                rows.append(row)
            self.tables[tid]=rows
        require(q<=len(tr.b) and not any(tr.b[q:]),'unparsed metadata table bytes')
        self.tables_consumed=q
        for i,t in enumerate(self.tables[2]):
            nxt=self.tables[2][i+1] if i+1<len(self.tables[2]) else {'MethodList':len(self.tables[6])+1,'FieldList':len(self.tables[4])+1}
            for key,tid in [('MethodList',6),('FieldList',4)]:
                for r in self.tables[tid][t[key]-1:nxt[key]-1]:r['declaring_type']=t['Name']
        self.by_token={r['token']:r for rows in self.tables.values() for r in rows}
    def stream(self,n):
        s=self.streams[n];return Reader(self.md.span(s['offset'],s['size']))
    def string(self,ix):
        rd=self.stream('#Strings');end=rd.b.find(b'\0',ix);require(end>=ix,'string heap');return rd.span(ix,end-ix).decode('utf8')
    def blob(self,ix):
        if not ix:return b''
        rd=self.stream('#Blob');n,p=compressed(rd,ix);return rd.span(p,n)
    def label(self,token):
        if token>>24==0x70:
            rd=self.stream('#US');n,p=compressed(rd,token&0xffffff);raw=rd.span(p,n);return raw[:-1].decode('utf-16-le') if n else ''
        if not token:return 'nil'
        r=self.by_token.get(token);require(r is not None,f'unknown token {token:x}')
        tid=token>>24
        if tid in (1,2):return (r.get('Namespace','')+'.'+r['Name']).lstrip('.')
        if tid in (4,6):return r.get('declaring_type','')+'::'+r['Name']
        if tid==10:return self.label(r['Class_token'])+'::'+r['Name']
        if tid==27:return self.signature(r['Signature'],'type')
        return SCHEMA[tid][0]+':'+str(token&0xffffff)
    def signature(self,ix,kind=None):
        rd=Reader(self.blob(ix));p=0
        def number():
            nonlocal p
            v,p=compressed(rd,p);return v
        def typ():
            nonlocal p
            t=number();base={1:'void',2:'bool',3:'char',4:'i1',5:'u1',6:'i2',7:'u2',8:'i4',9:'u4',10:'i8',11:'u8',12:'r4',13:'r8',14:'string',22:'typedref',24:'native_int',25:'native_uint',28:'object'}
            if t in base:return base[t]
            if t in (15,16,29,69):return {15:'pointer',16:'byref',29:'array',69:'pinned'}[t]+'<'+str(typ())+'>'
            if t in (17,18):
                coded=number();return self.label(([2,1,27][coded&3]<<24)|(coded>>2))
            if t in (19,30):return ('T' if t==19 else 'M')+str(number())
            if t==21:
                head=typ();n=number();return str(head)+'<'+','.join(str(typ()) for _ in range(n))+'>'
            if t in (31,32):
                modifier=number();return f'modifier({modifier}) '+str(typ())
            raise ValueError(f'unsupported signature type {t}')
        if kind=='type':result=typ()
        else:
            call=number()
            if call==6:result={'field':typ()}
            elif call==7:result={'locals':[typ() for _ in range(number())]}
            else:
                generic=number() if call&16 else 0;count=number();ret=typ();args=[typ() for _ in range(count)]
                result={'calling_convention':call,'generic_parameters':generic,'return':ret,'args':args}
        require(p==len(rd.b),'unconsumed signature bytes');return result
    def ledger(self):
        blobrows=[]
        for ix,uses in sorted(self.blobrefs.items()):
            row={'offset':ix,'consumers':uses,'sha256':sha(self.blob(ix)),'bytes':len(self.blob(ix))}
            if ix and any(u.endswith(':Signature') or u.startswith('Property:') for u in uses):
                row['decoded']=self.signature(ix,'type' if uses[0].startswith('TypeSpec:') else None)
            else:row['data_hex']=self.blob(ix).hex()
            blobrows.append(row)
        strings=[];rd=self.stream('#Strings');p=1
        while p<len(rd.b):
            end=rd.b.find(b'\0',p);require(end>=0,'strings tail');s=rd.b[p:end].decode('utf8')
            if s:strings.append({'offset':p,'value':s})
            p=end+1
        us=[];rd=self.stream('#US');p=1
        while p<len(rd.b):
            at=p;n,p=compressed(rd,p)
            if n:
                raw=rd.span(p,n);us.append({'offset':at,'value':safe_literal(raw[:-1].decode('utf-16-le')),'terminal_flag':raw[-1]});p+=n
        rd=self.stream('#Blob');p=1;all_blobs=[]
        while p<len(rd.b):
            at=p;n,p=compressed(rd,p);raw=rd.span(p,n);p+=n
            all_blobs.append({'offset':at,'size':n,'sha256':sha(raw),'consumers':self.blobrefs.get(at,[]),'padding':n==0})
        for r in self.tables[12]:
            r['attribute_constructor']=self.label(r['Type_token']);raw=self.blob(r['Value'])
            if 'DebuggableAttribute' in r['attribute_constructor']:
                r['decoded_value']={'prolog':int.from_bytes(raw[:2],'little'),'flags':int.from_bytes(raw[2:6],'little'),'named_count':int.from_bytes(raw[6:8],'little')}
            elif 'CompilationRelaxationsAttribute' in r['attribute_constructor']:
                require(len(raw)==8,'compilation attribute length')
                r['decoded_value']={'prolog':int.from_bytes(raw[:2],'little'),'relaxations_flags':int.from_bytes(raw[2:6],'little'),'named_count':int.from_bytes(raw[6:8],'little')}
            elif 'RuntimeCompatibilityAttribute' in r['attribute_constructor']:
                r['decoded_value']={'prolog':int.from_bytes(raw[:2],'little'),'named_count':int.from_bytes(raw[2:4],'little'),'named_boolean_property':'WrapNonExceptionThrows','value':bool(raw[-1])}
        bodies=[]
        for m in self.tables[6]:
            body=decode_body(self,m);m['signature_decoded']=self.signature(m['Signature']);bodies.append(body)
        return {'header':self.header,'streams':self.streams,'table_counts':{SCHEMA[k][0]:v for k,v in self.counts.items()},
            'tables':{SCHEMA[k][0]:v for k,v in self.tables.items()},'strings':strings,'user_strings':us,'blobs':blobrows,'all_blob_heap_records':all_blobs,
            'GUIDs':[str(uuid.UUID(bytes_le=self.stream('#GUID').span(i,16))) for i in range(0,self.stream('#GUID').b.__len__(),16)],'methods':bodies}

# ECMA CIL opcode identities and operand widths, no execution engine.
OPS={}
def op(code,name,operand=''):OPS[code]=(name,operand)
for i,n in enumerate('nop break ldarg.0 ldarg.1 ldarg.2 ldarg.3 ldloc.0 ldloc.1 ldloc.2 ldloc.3 stloc.0 stloc.1 stloc.2 stloc.3'.split()):op(i,n)
for i,n in enumerate('ldarg.s ldarga.s starg.s ldloc.s ldloca.s stloc.s'.split(),14):op(i,n,'B')
for i,n in enumerate('ldnull ldc.i4.m1 ldc.i4.0 ldc.i4.1 ldc.i4.2 ldc.i4.3 ldc.i4.4 ldc.i4.5 ldc.i4.6 ldc.i4.7 ldc.i4.8'.split(),20):op(i,n)
for code,name,operand in [(31,'ldc.i4.s','b'),(32,'ldc.i4','i'),(33,'ldc.i8','q'),(34,'ldc.r4','f'),(35,'ldc.r8','d'),(37,'dup',''),(38,'pop',''),(39,'jmp','T'),(40,'call','T'),(41,'calli','T'),(42,'ret','')]:op(code,name,operand)
branches='br brfalse brtrue beq bge bgt ble blt bne.un bge.un bgt.un ble.un blt.un'.split()
for i,n in enumerate(branches):op(43+i,n+'.s','r1');op(56+i,n,'r4')
op(69,'switch','switch')
for i,n in enumerate('ldind.i1 ldind.u1 ldind.i2 ldind.u2 ldind.i4 ldind.u4 ldind.i8 ldind.i ldind.r4 ldind.r8 ldind.ref stind.ref stind.i1 stind.i2 stind.i4 stind.i8 stind.r4 stind.r8 add sub mul div div.un rem rem.un and or xor shl shr shr.un neg not conv.i1 conv.i2 conv.i4 conv.i8 conv.r4 conv.r8 conv.u4 conv.u8'.split(),70):op(i,n)
for code,name in {0x6f:'callvirt',0x70:'cpobj',0x71:'ldobj',0x72:'ldstr',0x73:'newobj',0x74:'castclass',0x75:'isinst',0x79:'unbox',0x7b:'ldfld',0x7c:'ldflda',0x7d:'stfld',0x7e:'ldsfld',0x7f:'ldsflda',0x80:'stsfld',0x81:'stobj',0x8c:'box',0x8d:'newarr',0x8f:'ldelema',0xa3:'ldelem',0xa4:'stelem',0xa5:'unbox.any',0xc2:'refanyval',0xc6:'mkrefany',0xd0:'ldtoken'}.items():op(code,name,'T')
op(0x76,'conv.r.un');op(0x7a,'throw');op(0x8e,'ldlen')
for i,n in enumerate('ldelem.i1 ldelem.u1 ldelem.i2 ldelem.u2 ldelem.i4 ldelem.u4 ldelem.i8 ldelem.i ldelem.r4 ldelem.r8 ldelem.ref stelem.i stelem.i1 stelem.i2 stelem.i4 stelem.i8 stelem.r4 stelem.r8 stelem.ref'.split(),0x90):op(i,n)
for c,n in {0xd1:'conv.u2',0xd2:'conv.u1',0xd3:'conv.i',0xd4:'conv.ovf.i',0xd5:'conv.ovf.u',0xd6:'add.ovf',0xd7:'add.ovf.un',0xd8:'mul.ovf',0xd9:'mul.ovf.un',0xda:'sub.ovf',0xdb:'sub.ovf.un',0xdc:'endfinally',0xdf:'stind.i',0xe0:'conv.u'}.items():op(c,n)
op(0xdd,'leave','r4');op(0xde,'leave.s','r1')
for i,n in enumerate('arglist ceq cgt cgt.un clt clt.un'.split()):op(0xfe00+i,n)
op(0xfe06,'ldftn','T');op(0xfe07,'ldvirtftn','T')
for i,n in enumerate('ldarg ldarga starg ldloc ldloca stloc'.split(),9):op(0xfe00+i,n,'H')
for c,n in {0xfe0f:'localloc',0xfe11:'endfilter',0xfe13:'volatile.',0xfe14:'tail.',0xfe17:'cpblk',0xfe18:'initblk',0xfe1a:'rethrow',0xfe1d:'refanytype',0xfe1e:'readonly.'}.items():op(c,n)
op(0xfe12,'unaligned.','B');op(0xfe15,'initobj','T');op(0xfe16,'constrained.','T');op(0xfe1c,'sizeof','T')

def decode_body(cli,m,inspect=False):
    pe=cli.pe;p=pe.offset(m['RVA']);first=pe.span(p,1)[0];sections=[]
    if first&3==2:hs=1;sz=first>>2;maxstack=8;localsig=0;flags=2
    else:
        flags,maxstack,sz,localsig=pe.unpack('<HHII',p);hs=(flags>>12)*4;require(flags&3==3 and hs>=12,'fat method header')
    code=Reader(pe.span(p+hs,sz));q=0;instructions=[];starts=[]
    while q<sz:
        at=q;v=code.span(q,1)[0];q+=1
        if v==254:v=(v<<8)|code.span(q,1)[0];q+=1
        require(v in OPS,f'unknown opcode {v:x} at method {m["row"]}:{at:x}')
        name,typ=OPS[v];operand=None;label=None
        if typ=='T':operand=code.unpack('<I',q)[0];q+=4;label=cli.label(operand)
        elif typ in ('r1','r4'):
            d=code.unpack('<b' if typ=='r1' else '<i',q)[0];q+=int(typ[1:]);operand=q+d
        elif typ=='switch':
            count=code.unpack('<I',q)[0];q+=4;require(count<=sz//4,'switch count');base=q+4*count
            operand=[base+code.unpack('<i',q+4*i)[0] for i in range(count)];q=base
        elif typ:operand=code.unpack('<'+typ,q)[0];q+=struct.calcsize('<'+typ)
        starts.append(at);instructions.append({'offset':at,'op':name,'operand':operand,'label':label,'operand_kind':typ})
    require(q==sz,'method byte accounting')
    for ins in instructions:
        targets=ins['operand'] if ins['operand_kind']=='switch' else [ins['operand']] if ins['operand_kind'].startswith('r') else []
        require(all(t in starts for t in targets),'branch target not instruction')
    if flags&8:
        a=(p+hs+sz+3)&~3
        while True:
            k=pe.span(a,1)[0];fat=bool(k&64);n=int.from_bytes(pe.span(a+1,3),'little') if fat else pe.span(a+1,1)[0]
            require(k&1 and n>=4 and (n-4)%(24 if fat else 12)==0,'method extra section')
            for j in range((n-4)//(24 if fat else 12)):
                v=pe.unpack('<IIIIII' if fat else '<HHBHBI',a+4+j*(24 if fat else 12))
                fl,ts,tl,hs2,hl,tok=v
                require(ts in starts and hs2 in starts and ts+tl<=sz and hs2+hl<=sz,'EH bounds')
                sections.append({'flags':fl,'try':[ts,ts+tl],'handler':[hs2,hs2+hl],'catch_type':cli.label(tok) if fl==0 else None,'filter_offset':tok if fl==1 else None})
            a=(a+n+3)&~3
            if not k&128:break
    if inspect:
        print(json.dumps({'method':m,'locals':cli.signature(cli.by_token[localsig]['Signature']) if localsig else [],'exceptions':sections},ensure_ascii=False))
        for ins in instructions:print(f'{ins["offset"]:04x} {ins["op"]} {ins["label"] if ins["label"] is not None else ins["operand"] if ins["operand"] is not None else ""}')
    calls=[{'il_offset':x['offset'],'operation':x['op'],'target':x['label']} for x in instructions if x['op'] in ('call','callvirt','newobj','ldftn')]
    return {'method_token':m['token'],'name':cli.label(m['token']),'file_offset':p,'code_size':sz,'sha256':sha(code.b),
        'instruction_count':len(instructions),'op_histogram':dict(collections.Counter(x['op'] for x in instructions)),
        'all_instruction_bytes_decoded':True,'branches_valid':True,'exception_clauses':sections,'calls':calls,
        'string_references':[{'il_offset':x['offset'],'value':safe_literal(x['label'])} for x in instructions if x['op']=='ldstr'],
        'locals':cli.signature(cli.by_token[localsig]['Signature']) if localsig else [],'max_stack_header':maxstack,
        'not_claimed':'No execution, stack-verification proof, framework dependency implementation or rendering result.'}

def main():
    if len(sys.argv)==3 and sys.argv[1]=='--inspect-il':
        cli=CLI(PE((ROOT/'animmaker.exe').read_bytes()));decode_body(cli,cli.tables[6][int(sys.argv[2])-1],True);return
    results=[]
    for name in ('Game.exe','animmaker.exe','extendtext.exe','x64-msvcrt-ruby310.dll','zlib1.dll'):
        data=(ROOT/name).read_bytes();pe=PE(data)
        row={'path':name,'bytes':len(data),'sha256':sha(data),**pe.meta,'imports':pe.imports(),'exports':pe.exports(),'coff_symbols':pe.coff_symbols(),
            'resources':pe.resources(),'debug_records':pe.debug(),'string_scan':scan_strings(pe),'embedded_readable':embedded_readable_inventory(pe)}
        if pe.dirs[14][0]:
            cli=CLI(pe);row['CLI']=cli.ledger()
        results.append(row)
    save('binary-interface-audit.json',{'records':results,'execution_status':'DATA_ONLY_NO_REFERENCE_LOADING'})
    print(json.dumps([{'path':x['path'],'imports':sum(len(d['symbols']) for d in x['imports']),'exports':len(x['exports']),
        'resources':len(x['resources']),'selected_strings':len(x['string_scan']['selected']),'CLI_methods':len(x.get('CLI',{}).get('methods',[]))} for x in results]))

if __name__=='__main__':main()
