"""Inert, bounds-checked reader for the exact Ruby 3.1 YARB containers.

No target runtime, object constructors, eval, dynamic linking, or C execution.
The opcode names/types/lengths come from the target DLL's raw PE data.
Format reference: fixed official compile.c and Typemap, read before authoring.
"""
from pathlib import Path
import json, struct, hashlib, collections

ROOT=Path(__file__).resolve().parent
B=Path('/workspace/pokemon-essentials/x64-msvcrt-ruby310.dll').read_bytes()
S=json.loads((ROOT/'x64-msvcrt-ruby310.dll.coff-symbols.json').read_text())
SY={s['name']:s for s in S if 'raw' in s}
def cstr(b,p):
    return b[p:b.index(0,p)].decode('ascii')
def table(name): return SY[name]['raw']
OPS=[]
for i in range(202):
    no=struct.unpack_from('<H',B,table('rb_vm_insn_name_offset')+2*i)[0]
    to=struct.unpack_from('<H',B,table('rb_vm_insn_op_offset')+2*i)[0]
    name=cstr(B,table('rb_vm_insn_name_base')+no)
    types=cstr(B,table('rb_vm_insn_op_base')+to)
    length=B[table('rb_vm_insn_len_info')+i]
    assert length==len(types)+1,(i,name,types,length)
    assert set(types)<=set('CHKAISTOVLFNR')
    OPS.append(dict(index=i,name=name,types=types,length=length))
assert OPS[-1]['name']=='trace_putobject_INT2FIX_1_'
FIELDS='type iseq_size bytecode_offset bytecode_size param_flags param_size param_lead_num param_opt_num param_rest_start param_post_start param_post_num param_block_start param_opt_table_offset param_keyword_offset location_pathobj_index location_base_label_index location_label_index location_first_lineno location_node_id location_code_location_beg_pos_lineno location_code_location_beg_pos_column location_code_location_end_pos_lineno location_code_location_end_pos_column insns_info_body_offset insns_info_positions_offset insns_info_size local_table_offset catch_table_size catch_table_offset parent_iseq_index local_iseq_index mandatory_only_iseq_index ci_entries_offset outer_variables_offset variable_flip_count local_table_size is_size ci_size stack_max catch_except_p builtin_inline_p'.split()
RELATIVE=set('bytecode_offset param_opt_table_offset insns_info_body_offset insns_info_positions_offset local_table_offset catch_table_offset ci_entries_offset outer_variables_offset'.split())
SIGN32=set('param_rest_start param_block_start parent_iseq_index local_iseq_index mandatory_only_iseq_index'.split())
def signed(x,bits=64):
    x&=(1<<bits)-1
    return x-(1<<bits) if x>>(bits-1) else x

class Read:
    def __init__(self,b):self.b=b;self.ranges=[]
    def raw(self,p,n,kind):
        assert p>=0 and n>=0 and p+n<=len(self.b),(p,n,len(self.b),kind)
        self.ranges.append((p,p+n,kind));return self.b[p:p+n]
    def small(self,p):
        c=self.raw(p,1,'small-prefix')[0]
        n=1 if c&1 else 9 if c==0 else (c&-c).bit_length()
        raw=self.raw(p,n,'small-value');v=c>>n
        for x in raw[1:]:v=(v<<8)|x
        return v,p+n
    def many(self,p,n):
        result=[]
        for i in range(n):v,p=self.small(p);result.append(v)
        return result,p
    def unpack(self,p,fmt,kind):return struct.unpack(fmt,self.raw(p,struct.calcsize(fmt),kind))

RESULT=[]
for sy in S:
    start=sy.get('raw')
    if start is None or not sy['name'].endswith('_bin') or B[start:start+4]!=b'YARB':continue
    h=struct.unpack_from('<9I',B,start);assert h[1:3]==(3,1) and h[4]==0
    b=B[start:start+h[3]];r=Read(b)
    r.raw(0,36,'header');platform=cstr(b,36);assert platform=='x64-mingw32';r.raw(36,len(platform)+1,'platform')
    ise_offsets=r.unpack(h[7],'<'+h[5]*'I','iseq-index')
    obj_offsets=r.unpack(h[8],'<'+h[6]*'I','object-index')
    objects=[]
    for oi,off in enumerate(obj_offsets):
        flag=r.raw(off,1,'object-flags')[0];typ=flag&31;p=off+1
        o=dict(index=oi,offset=off,type=typ,special=bool(flag&32),frozen=bool(flag&64),internal=bool(flag&128))
        if flag&32:
            v,p=r.small(p)
            o['value']=('nil' if typ==17 else 'true' if typ==18 else 'false' if typ==19 else 'undef' if typ==22 else signed(v)>>1 if v&1 else {'raw_value':v})
            o['raw_value']=v
        elif typ in (5,20):
            enc,p=r.small(p);n,p=r.small(p);raw=r.raw(p,n,'string-or-symbol');p+=n
            o.update(encoding_index=enc,text=raw.decode('utf-8'),raw_hex=raw.hex())
        elif typ==7:
            n,p=r.small(p);items,p=r.many(p,n);assert all(v<len(obj_offsets) for v in items)
            o['items']=items
        elif typ==4:
            p=(p+7)//8*8;o['value']=r.unpack(p,'<d','float')[0];p+=8
        else:raise AssertionError(('unsupported-object-type',sy['name'],oi,typ))
        o['end_exclusive']=p;objects.append(o)
    def obj(n):
        assert n<len(objects),n
        o=objects[n]
        return o.get('text',o.get('value',{'array':o.get('items')}))
    iseqs=[]
    for ii,off in enumerate(ise_offsets):
        vs,end=r.many(off,len(FIELDS));f=dict(zip(FIELDS,vs))
        for k in RELATIVE:f[k]=(off-f[k])&0xffffffff
        for k in SIGN32:f[k]=signed(f[k],32)
        ci=[];p=f['ci_entries_offset']
        for j in range(f['ci_size']):
            mid,p=r.small(p)
            if mid==(1<<64)-1:ci.append(None);continue
            vals,p=r.many(p,3);flag,argc,nkw=vals;kw,p=r.many(p,nkw)
            ci.append(dict(method=obj(mid),method_object=mid,flags=flag,argc=argc,keywords=[obj(k) for k in kw]))
        p=f['outer_variables_offset'];n,p=r.small(p);outer,p=r.many(p,n*2)
        local=r.unpack(f['local_table_offset'],'<'+f['local_table_size']*'Q','local-table') if f['local_table_size'] else ()
        opt=r.unpack(f['param_opt_table_offset'],'<'+(f['param_opt_num']+1)*'Q','optional-jumps') if f['param_opt_num'] else ()
        keyword=None
        if f['param_keyword_offset']:
            kn,req,bits,rest,tableptr,dvptr=r.unpack(f['param_keyword_offset'],'<iiiiQQ','keyword-structure')
            kt=r.unpack(tableptr,'<'+kn*'Q','keyword-ids') if kn else ()
            dv=r.unpack(dvptr,'<'+(kn-req)*'Q','keyword-defaults') if kn>req else ()
            keyword=dict(num=kn,required=req,bits_start=bits,rest_start=rest,keys=[obj(k) for k in kt],defaults=[obj(k) for k in dv])
        catches=[];p=f['catch_table_offset']
        for j in range(f['catch_table_size']):
            vals,p=r.many(p,6);v=dict(zip(('iseq','type','start','end','cont','sp'),vals));v['iseq']=signed(v['iseq'],32);catches.append(v)
        info=[];p=f['insns_info_body_offset']
        for j in range(f['insns_info_size']):
            vals,p=r.many(p,3);info.append(dict(line=vals[0],node=signed(vals[1],32),events=vals[2]))
        positions=[];p=f['insns_info_positions_offset'];last=0
        for j in range(f['insns_info_size']):v,p=r.small(p);last+=v;positions.append(last)
        code=[];pc=0;p=f['bytecode_offset'];cidx=0
        while pc<f['iseq_size']:
            begin=p;opcode,p=r.small(p);assert opcode<len(OPS),opcode;op=OPS[opcode];args=[]
            for typ in op['types']:
                if typ=='C':
                    assert cidx<len(ci);args.append(dict(type=typ,value=ci[cidx],call_data_index=cidx));cidx+=1
                elif typ=='R':
                    ix,p=r.small(p);ln,p=r.small(p);name=r.raw(p,ln,'builtin-name').decode();p+=ln;args.append(dict(type=typ,index=ix,name=name))
                else:
                    v,p=r.small(p);value=obj(v) if typ in 'VIH' else signed(v,32) if typ=='S' else signed(v) if typ=='O' else v
                    args.append(dict(type=typ,value=value,raw_value=v))
            code.append(dict(pc=pc,raw_start=begin,raw_end=p,opcode=opcode,name=op['name'],operands=args));pc+=op['length']
        assert pc==f['iseq_size'] and p==f['bytecode_offset']+f['bytecode_size'],(sy['name'],ii,pc,p,f)
        # Callsites are consumed in bytecode order; all except optional NULL entries must be visited.
        assert cidx==len(ci),(sy['name'],ii,cidx,len(ci))
        iseqs.append(dict(index=ii,body_offset=off,body_end=end,fields=f,label=obj(f['location_label_index']),
                          path=obj(f['location_pathobj_index']),locals=[obj(k) for k in local],optional_jumps=opt,
                          keyword=keyword,catch_table=catches,call_data=ci,outer_variables=outer,
                          instruction_info=info,instruction_positions=positions,code=code))
    ranges=sorted((a,e) for a,e,k in r.ranges if e>a);merged=[]
    for a,e in ranges:
        if merged and a<=merged[-1][1]:merged[-1][1]=max(e,merged[-1][1])
        else:merged.append([a,e])
    holes=[];p=0
    for a,e in merged:
        if p<a:holes.append(dict(start=p,end=a,hex=b[p:a].hex()))
        p=e
    if p<len(b):holes.append(dict(start=p,end=len(b),hex=b[p:].hex()))
    assert all(set(bytes.fromhex(hole['hex']))<={0} for hole in holes),(sy['name'],holes)
    RESULT.append(dict(name=sy['name'],start=start,end_exclusive=start+len(b),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),
                       coff_symbol=sy,header_words=h,platform=platform,objects=objects,iseqs=iseqs,
                       parsed_byte_ranges=merged,zero_padding=holes))
assert len(RESULT)==16
(ROOT/'yarb-decoded.json').write_text(json.dumps(RESULT,ensure_ascii=False,indent=2)+'\n')
(ROOT/'yarb-opcodes.json').write_text(json.dumps(OPS,ensure_ascii=False,indent=2)+'\n')
lines=[]
for unit in RESULT:
    lines.append('UNIT '+unit['name']+' '+str(unit['start'])+' '+str(unit['end_exclusive']))
    for o in unit['objects']:lines.append('OBJ '+str(o['index'])+' '+str(o))
    for q in unit['iseqs']:
        lines.append('ISEQ '+str(q['index'])+' '+str(q['label'])+' line='+str(q['fields']['location_first_lineno'])+' locals='+str(q['locals'])+' kw='+str(q['keyword'])+' opt='+str(q['optional_jumps'])+' catches='+str(q['catch_table']))
        for ins in q['code']:lines.append(str(ins['pc'])+' '+ins['name']+' '+str(ins['operands']))
(ROOT/'yarb-full-view.txt').write_text('\n'.join(lines)+'\n')
print(json.dumps(dict(containers=len(RESULT),bytes=sum(x['bytes'] for x in RESULT),iseqs=sum(len(x['iseqs']) for x in RESULT),objects=sum(len(x['objects']) for x in RESULT),instructions=sum(len(q['code']) for x in RESULT for q in x['iseqs']),all_nonpadding_bytes_parsed=True)))
