"""Decode fixed reference bytes as inert data; never launch a reference program."""
from pathlib import Path
import sys, subprocess, hashlib, json, argparse, zlib
T=Path(__file__).resolve().parent
sys.path.insert(0,str(T/'.work/packages'))
C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
ap=argparse.ArgumentParser();ap.add_argument('kind',choices=['cil','native','loader']);ap.add_argument('--method',type=int);a=ap.parse_args()
path={'cil':'animmaker.exe','native':'extendtext.exe','loader':'Data/Scripts.rxdata'}[a.kind]
b=subprocess.check_output(['git','show',C+':'+path],cwd='/workspace/pokemon-essentials')
receipt=dict(commit=C,path=path,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),behavior='NOT_EXECUTED',display_only=True)
if a.kind=='loader':
    # Exact frozen Marshal outer structure, with bounded zlib-only payload decoding.
    assert len(b)==594 and b[:4]==bytes.fromhex('04085b06')
    d=zlib.decompressobj();out=d.decompress(b[29:590],10000);out+=d.flush()
    assert d.eof and not d.unused_data and len(out)==1197
    receipt.update(compressed_range=[29,590],decoded_bytes=len(out),decoded_sha256=hashlib.sha256(out).hexdigest())
    print('OUTER',b[:29].hex(),b[590:].hex())
    print('\n'.join(f'{i}: {s}' for i,s in enumerate(out.decode().splitlines(),1)))
elif a.kind=='cil':
    import dnfile
    from dncil.cil.body.reader import read_method_body_from_bytes
    from dncil.clr.token import Token, StringToken
    p=dnfile.dnPE(data=b)
    owners={}
    for typ in p.net.mdtables.TypeDef.rows:
        for m in typ.MethodList:owners[m.row_index]=str(typ.TypeName)
    def resolve(tok):
        if isinstance(tok,StringToken):return repr(p.net.user_strings.get(tok.rid).value)
        if not isinstance(tok,Token):return str(tok) if tok is not None else ''
        row=p.net.mdtables.tables[tok.table].rows[tok.rid-1]
        if tok.table==6:return owners.get(tok.rid,'')+'::'+str(row.Name)+' sig='+row.Signature.value.hex()
        if tok.table==10:
            r=row.Class.row
            owner=('TypeSpec:'+r.Signature.value.hex()) if hasattr(r,'Signature') else str(getattr(r,'TypeNamespace',''))+'.'+str(getattr(r,'TypeName',getattr(r,'Name','?')))
            return owner+'::'+str(row.Name)+' sig='+row.Signature.value.hex()
        if tok.table in (1,2):return str(row.TypeNamespace)+'.'+str(row.TypeName)
        if tok.table==4:return str(row.Name)+' sig='+row.Signature.value.hex()
        if tok.table==17:return 'local_sig='+row.Signature.value.hex()
        return str(tok)
    methods=[]
    for i,m in enumerate(p.net.mdtables.MethodDef.rows,1):
        if not m.Rva:continue
        body=read_method_body_from_bytes(p.get_data(m.Rva))
        off=p.get_offset_from_rva(m.Rva)
        methods.append(dict(index=i,owner=owners.get(i),name=str(m.Name),rva=m.Rva,offset=off,size=body.size,code_size=body.code_size,sha256=hashlib.sha256(b[off:off+body.size]).hexdigest(),instructions=len(body.instructions),eh=[vars(e) for e in body.exception_handlers]))
        if a.method is not None and a.method!=i:continue
        print('METHOD',i,owners.get(i),str(m.Name),'offset',hex(off),'size',body.size,'code',body.code_size,'sig',m.Signature.value.hex())
        print('LOCALS',resolve(body.local_var_sig_tok))
        for ins in body.instructions:
            operand=resolve(ins.operand)
            if 'BrTarget' in ins.opcode.operand_type.name:operand=hex(ins.operand-body.header_size)
            print(f'{ins.offset-body.header_size:04x}: {ins.opcode.name:14} {operand}')
        for e in body.exception_handlers:print('EH',vars(e),'type',resolve(e.catch_type))
    receipt.update(methods=methods,displayed_method=a.method,method_count=len(methods))
else:
    import pefile
    from capstone import Cs,CS_ARCH_X86,CS_MODE_32
    p=pefile.PE(data=b);base=p.OPTIONAL_HEADER.ImageBase
    imports={base+v.address-base:str(v.name) for d in p.DIRECTORY_ENTRY_IMPORT for v in d.imports}
    print('IMPORTS',json.dumps(imports,sort_keys=True))
    for start,end in [(0x401219,0x401294),(0x40129c,0x4016cc)]:
        off=p.get_offset_from_rva(start-base);data=b[off:off+end-start]
        print('RANGE',hex(start),hex(end),'offset',off)
        for x in Cs(CS_ARCH_X86,CS_MODE_32).disasm(data,start):print(hex(x.address),x.mnemonic,x.op_str)
    print('DATA',repr(b[3072:3348]))
    receipt.update(virtual_ranges=[[0x401219,0x401294],[0x40129c,0x4016cc]],data_range=[3072,3348],imports=imports)
q=T/'binary-displays.json';s=json.loads(q.read_text()) if q.exists() else [];s.append(receipt);q.write_text(json.dumps(s,ensure_ascii=False,indent=2,default=str)+'\n')
