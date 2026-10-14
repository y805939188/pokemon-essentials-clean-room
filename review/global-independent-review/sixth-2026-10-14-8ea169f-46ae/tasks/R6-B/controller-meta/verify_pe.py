"""Independent bounded PE metadata validation; never loads reference binaries.

Inputs are three fixed read-only reference files and the current review's JSON.
Outputs stay in this script's directory. Structure validation is not behavior.
"""
from pathlib import Path
import collections
import hashlib
import json
import struct

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]
REF = ROOT / 'reference/pokemon-essentials'
AUDIT = OUT.parents[2] / 'evidence/resource-parser/binary-interface-audit.json'


def parse(name):
    b = (REF / name).read_bytes()
    def u16(p): return struct.unpack_from('<H', b, p)[0]
    def u32(p): return struct.unpack_from('<I', b, p)[0]
    def u64(p): return struct.unpack_from('<Q', b, p)[0]
    def cstr(p):
        end = b.index(0, p)
        return b[p:end].decode('ascii', errors='replace')
    pe = u32(60)
    assert b[:2] == b'MZ' and b[pe:pe+4] == b'PE\0\0'
    machine, nsec, stamp, syms, nsyms, osize, flags = struct.unpack_from('<HHIIIHH', b, pe+4)
    opt = pe+24
    assert u16(opt) == 0x20b
    ndirs = u32(opt+108)
    dirs = [struct.unpack_from('<II', b, opt+112+i*8) for i in range(ndirs)]
    secs = []
    for i in range(nsec):
        p = opt+osize+i*40
        nm = b[p:p+8].split(b'\0')[0].decode('ascii')
        vs, va, sz, raw = struct.unpack_from('<IIII', b, p+8)
        resolved=cstr(syms+nsyms*18+int(nm[1:])) if nm.startswith('/') and nm[1:].isdigit() else nm
        secs.append({'raw_name':nm,'name':resolved,'virtual_size':vs,'rva':va,'size':sz,'offset':raw,'flags':u32(p+36)})
    def at(rva):
        for s in secs:
            if s['rva'] <= rva < s['rva']+max(s['virtual_size'],s['size']):
                off = s['offset']+rva-s['rva']
                assert rva-s['rva'] < s['size'] and off < len(b)
                return off
        assert 0 <= rva < min(s['offset'] for s in secs if s['offset'])
        return rva
    imports = []
    if dirs[1][0]:
        p = at(dirs[1][0])
        while any(b[p:p+20]):
            ilt, ts, fw, dn, iat = struct.unpack_from('<IIIII', b, p)
            dll = cstr(at(dn));q=at(ilt or iat);entries=[];idx=0
            while u64(q+8*idx):
                value=u64(q+8*idx)
                if value >> 63: ent={'ordinal':value & 0xffff,'iat_rva':iat+8*idx}
                else:
                    t=at(value);ent={'name':cstr(t+2),'hint':u16(t),'iat_rva':iat+8*idx}
                entries.append(ent);idx+=1
            imports.append({'dll':dll,'symbols':entries});p+=20
    exports=[]
    if dirs[0][0]:
        p=at(dirs[0][0]);base,nfunc,nnames,fa,na,oa=struct.unpack_from('<IIIIII',b,p+16)
        names={u16(at(oa)+2*i):cstr(at(u32(at(na)+4*i))) for i in range(nnames)}
        for i in range(nfunc):
            rva=u32(at(fa)+4*i)
            if rva:
                exports.append({'ordinal':base+i,'name':names.get(i),'rva':rva,'forwarder':cstr(at(rva)) if dirs[0][0]<=rva<sum(dirs[0]) else None})
    coff=[];i=0;strstart=syms+nsyms*18
    while syms and i<nsyms:
        p=syms+i*18;z,no=struct.unpack_from('<II',b,p)
        nm=cstr(strstart+no) if z==0 else b[p:p+8].split(b'\0')[0].decode('ascii',errors='replace')
        value,sec,typ,storage,aux=struct.unpack_from('<IhHBB',b,p+8)
        assert i+aux<nsyms
        coff.append({'index':i,'name':nm,'value':value,'section_number':sec,'type':typ,'storage_class':storage,'auxiliary_count':aux})
        i+=1+aux
    assert i==nsyms
    counts=collections.Counter((x['section_number'],x['type'],x['storage_class'],x['auxiliary_count']) for x in coff)
    return {'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'machine':machine,'PE32_plus':True,'entry_rva':u32(opt+16),'image_base':u64(opt+24),'coff_symbol_count':nsyms,'coff_nonaux_count':len(coff),'coff_aux_count':nsyms-len(coff),'coff_category_counts':[{'section_number':k[0],'type':k[1],'storage_class':k[2],'auxiliary_count':k[3],'count':v} for k,v in sorted(counts.items())],'sections':secs,'directories':[{'index':i,'address':a,'size':sz} for i,(a,sz) in enumerate(dirs)],'imports':imports,'exports':exports,'coff_symbols':coff,'debug_directory_absent':not dirs[6][0],'certificate_directory_absent':not dirs[4][0],'managed_cli_directory_absent':not dirs[14][0],'evidence_level':'STRUCTURE_VALIDATION_ONLY','executed_reference':False}


audit=json.loads(AUDIT.read_text())
results=[]
for name in ['Game.exe','x64-msvcrt-ruby310.dll','zlib1.dll']:
    record=parse(name);original=next(x for x in audit['records'] if x['path']==name)
    compared=['bytes','sha256','machine','PE32_plus','entry_rva','image_base','coff_symbol_count','directories','imports','exports']
    checks={k:record[k]==original[k] for k in compared}
    checks['all_coff_core_fields']=all({k:x[k] for k in record['coff_symbols'][i]}==record['coff_symbols'][i] for i,x in enumerate(original['coff_symbols'])) and len(record['coff_symbols'])==len(original['coff_symbols'])
    checks['all_section_core_fields']=all({k:x[k] for k in ['name','virtual_size','rva','size','offset','flags']}=={k:y[k] for k in ['name','virtual_size','rva','size','offset','flags']} for x,y in zip(record['sections'],original['sections'])) and len(record['sections'])==len(original['sections'])
    b=(REF/name).read_bytes()
    pe=struct.unpack_from('<I',b,60)[0]
    symoffset=struct.unpack_from('<I',b,pe+12)[0]
    checks['all_coff_aux_payload_hashes']=all(hashlib.sha256(b[symoffset+(x['index']+1)*18:symoffset+(x['index']+1+x['auxiliary_count'])*18]).hexdigest()==x['aux_sha256'] for x in original['coff_symbols'] if x['auxiliary_count'])
    checks['all_section_payload_hashes']=all(hashlib.sha256(b[x['offset']:x['offset']+x['size']]).hexdigest()==x['sha256'] for x in original['sections'])
    checks['all_resource_payload_hashes']=all(hashlib.sha256(b[x['offset']:x['offset']+x['size']]).hexdigest()==x['sha256'] for x in original['resources'])
    checks['all_selected_strings_match_source_bytes']=all(b[x['offset']:x['offset']+len(x['text'].encode(x['encoding']))]==x['text'].encode(x['encoding']) for x in original['string_scan']['selected'])
    record['checks_against_new_root_evidence']=checks
    record['root_resource_count']=len(original['resources'])
    record['root_selected_string_count']=len(original['string_scan']['selected'])
    (OUT/(name+'.independent-structure.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    summary={k:record[k] for k in ['path','bytes','sha256','coff_symbol_count','coff_nonaux_count','coff_aux_count','checks_against_new_root_evidence']}
    summary.update(import_groups=len(record['imports']),imports=sum(len(x['symbols']) for x in record['imports']),exports=len(record['exports']))
    results.append(summary)
(OUT/'independent-pe-checks.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results,ensure_ascii=False,indent=2))
