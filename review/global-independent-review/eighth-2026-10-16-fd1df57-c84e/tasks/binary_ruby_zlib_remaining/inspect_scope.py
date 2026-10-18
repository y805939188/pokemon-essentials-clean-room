"""Read-only PE/string scope inspection; writes only beside this file.

Does not load target binaries, interpret Ruby, or grant semantic reading credit.
"""
from pathlib import Path
import bisect, collections, datetime, gzip, hashlib, json, struct, subprocess

OUT = Path(__file__).resolve().parent
TASKS = OUT.parent
INPUT = TASKS / 'binary_remaining_texts/ruby-zlib-subtask'
REFERENCE = Path('/workspace/pokemon-essentials')
REPO = TASKS.parents[3]
sha = lambda b: hashlib.sha256(b).hexdigest()
def save(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
def rows(name):
    return [json.loads(x) for x in gzip.decompress((INPUT / name).read_bytes()).splitlines()]

manifest = json.loads((INPUT / 'manifest.json').read_text())
identities = []
for entry in manifest['files']:
    data = (INPUT / entry['path']).read_bytes()
    assert len(data) == entry['bytes'] and sha(data) == entry['sha256']
    row = dict(entry, verified=True)
    if 'decoded' in entry:
        decoded = gzip.decompress(data)
        assert len(decoded) == entry['decoded']['bytes']
        assert sha(decoded) == entry['decoded']['sha256']
        assert len(decoded.splitlines()) == entry['decoded']['lines']
    identities.append(row)
unread = rows('unread.jsonl.gz')
readset = rows('readset.jsonl.gz')
refs = {x['candidate_id']: r for r in readset for x in r['refs']}
assert len(unread) == len(refs) == 20907
assert {x['candidate_id'] for x in unread} == set(refs)
assert len(readset) == 13574
assert sha(('\n'.join(sorted(refs)) + '\n').encode()) == manifest['candidate_set_sha256']
old = json.loads((TASKS / 'preflight_resources/current-programs-v2/inventory.json').read_text())
old += json.loads((TASKS / 'binary_controller_strings_review/new-program-inventory.json').read_text())
details = []
all_candidates = []
cstrings = {}
for path in manifest['scope_paths']:
    b = (REFERENCE / path).read_bytes()
    source_blob = subprocess.check_output(['git', '-C', str(REFERENCE), 'rev-parse', 'HEAD:' + path]).decode().strip()
    assert b == subprocess.check_output(['git', '-C', str(REFERENCE), 'show', 'HEAD:' + path])
    pe = struct.unpack_from('<I', b, 0x3c)[0]
    assert b[pe:pe+4] == b'PE\0\0'
    machine, ns, stamp, symoff, nsyms, optsize, flags = struct.unpack_from('<HHIIIHH', b, pe+4)
    imagebase = struct.unpack_from('<Q', b, pe+24+24)[0]
    sections = []
    for i in range(ns):
        at = pe+24+optsize+40*i
        name = b[at:at+8].rstrip(b'\0').decode()
        vs, va, size, raw = struct.unpack_from('<IIII', b, at+8)
        sections.append(dict(index=i+1, name=name, virtual_size=vs, rva=va, raw=raw, size=size))
    def raw_for_rva(rva):
        for s in sections:
            if s['rva'] <= rva < s['rva']+s['size']:
                return s['raw']+rva-s['rva']
    symbols=[]
    strings=symoff+18*nsyms
    stringsize=struct.unpack_from('<I',b,strings)[0]
    assert strings+stringsize<=len(b)
    i=0
    while i<nsyms:
        at=symoff+18*i
        namebytes=b[at:at+8]
        if namebytes[:4]==b'\0'*4:
            noff=struct.unpack_from('<I',namebytes,4)[0]
            pos=strings+noff
            name=b[pos:b.index(0,pos)].decode('utf-8','backslashreplace')
        else: name=namebytes.rstrip(b'\0').decode('utf-8','backslashreplace')
        value,section,typ,storage,aux=struct.unpack_from('<IhHBB',b,at+8)
        sy=dict(index=i,record_offset=at,name=name,value=value,section=section,type=typ,storage=storage,aux=aux)
        if 0<section<=len(sections):
            s=sections[section-1]; sy['raw']=s['raw']+value; sy['rva']=s['rva']+value
        symbols.append(sy); i+=1+aux
    symbols.sort(key=lambda s:(s.get('raw',len(b)+1),s['index']))
    data_symbols=[s for s in symbols if s.get('section')==3 and not s['name'].startswith('.')]
    positions=[s['raw'] for s in data_symbols]
    block=[]
    for x in unread:
        if x['path']!=path: continue
        raw=b[x['start']:x['end_exclusive']]
        assert sha(raw)==x['sha256'] and len(raw)==x['bytes']
        expected=refs[x['candidate_id']]['text']
        encoding='utf-16le' if x['encoding'] in ('utf16le','utf-16-le-ascii-subset') else x['encoding']
        assert raw.decode(encoding)==expected,(x['candidate_id'],encoding)
        j=bisect.bisect_right(positions,x['start'])-1
        owner=data_symbols[j] if j>=0 else None
        prev=b.rfind(b'\0',0,x['start'])+1
        end=b.find(b'\0',x['end_exclusive'])
        if end<0: end=len(b)
        contiguous=b[prev:end]
        printable=all(c in (9,10,13) or 32<=c<=126 for c in contiguous)
        cover=[s['id'] for s in old if s['path']==path and s['start']<=x['start'] and x['end_exclusive']<=s['end_exclusive']]
        rr=dict(x,read_id=refs[x['candidate_id']]['read_id'],view_line=readset.index(refs[x['candidate_id']])+1,
                nearest_coff_symbol=owner,cstring_start=prev,cstring_end=end,cstring_printable=printable,
                prior_program_identity_cover=cover)
        block.append(rr)
        if printable and (b'\n' in contiguous or b'\r' in contiguous):
            key=(path,prev,end)
            cstrings[key]=dict(path=path,start=prev,end_exclusive=end,bytes=len(contiguous),sha256=sha(contiguous),
                              text=contiguous.decode(),candidate_ids=[])
    for x in block:
        key=(path,x['cstring_start'],x['cstring_end'])
        if key in cstrings: cstrings[key]['candidate_ids'].append(x['candidate_id'])
    all_candidates.extend(block)
    yarbs=[]
    pos=0
    while True:
        pos=b.find(b'YARB',pos)
        if pos<0: break
        header=struct.unpack_from('<9I',b,pos)
        sy=[s for s in data_symbols if s['raw']<=pos]
        yarbs.append(dict(start=pos,header_words=header,nearest_coff_symbol=sy[-1] if sy else None))
        pos+=4
    details.append(dict(path=path,bytes=len(b),sha256=sha(b),git_blob=source_blob,
                        image_base=imagebase,pe_offset=pe,sections=sections,symbol_table=dict(offset=symoff,count=nsyms,string_offset=strings,string_bytes=stringsize),
                        yarb_headers=yarbs))
    save(path+'.coff-symbols.json',symbols)
save('identities.json',dict(schema='gr8.ruby-zlib.identities/v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                         contracts_and_containers=identities,reference_commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
                         reference_tree='7589c800b61ba13a13040ed0d686979b80a84fd0',
                         b8_commit='fd1df570cad987dc3852a3b958f03916e317f7fe',b8_tree='751dfde81048c81390f89a65ca1d1a565ba8e1ca',
                         formal_tree='f292698cdd4a8e725525a9be6dc34b75faaf151e',sources=details,
                         candidate_set_sha256=manifest['candidate_set_sha256'],all_raw_candidates_verified=20907))
serialized=('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in all_candidates)+'\n').encode()
(OUT/'candidate-contexts.jsonl.gz').write_bytes(gzip.compress(serialized,mtime=0))
save('complete-cstrings.json',list(cstrings.values()))
print(json.dumps(dict(occurrences=len(all_candidates),distinct=len(readset),cstring_units=len(cstrings),
                      cstring_candidate_count=sum(len(x['candidate_ids']) for x in cstrings.values()),
                      prior_program_identity_covered=sum(bool(x['prior_program_identity_cover']) for x in all_candidates),
                      text_bytes=sum(len(r['text'].encode()) for r in readset),yarb_headers=[x['yarb_headers'] for x in details]),ensure_ascii=False))
