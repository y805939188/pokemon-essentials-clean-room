"""Read-only, fixed-input review instrumentation. Does not execute reference code.

Inventory and relation results are evidence, never semantic PASS receipts.
Only files below this script's own directory may be written.
"""
from pathlib import Path
from collections import Counter, defaultdict
import csv, hashlib, json, re, subprocess, sys, datetime, gzip

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = Path(__file__).resolve().parent
REF = ROOT / 'reference/pokemon-essentials'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
MTREE = '6ab3429170d2762607fbc2237014c3a160449fa1'
RHEAD = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
RTREE = '7589c800b61ba13a13040ed0d686979b80a84fd0'
FTREE = '1046fbb657882e84b3dfc6d017943a9edf7782e5'
TEXT = {'Name','NamePlural','PortionName','PortionNamePlural','Description','Pokedex','Category','FormName'}
FAMILIES = {'pokemon','pokemon_forms','pokemon_metrics','moves','abilities','items','berry_plants','types','shadow_pokemon'}

def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b): return hashlib.sha256(b).hexdigest()
def save(name, obj):
    p = OUT / name
    assert p.resolve().is_relative_to(OUT)
    body=(json.dumps(obj, ensure_ascii=False, indent=2) + '\n').encode()
    if len(body)>5_000_000:
        packed=gzip.compress(body,mtime=0)
        (OUT/(name+'.gz')).write_bytes(packed)
        p.write_text(json.dumps({'artifact_encoding':'gzip_json','artifact':name+'.gz','uncompressed_bytes':len(body),'uncompressed_sha256':sha(body),'compressed_bytes':len(packed),'compressed_sha256':sha(packed),'semantic_status':'see records; compression does not change extent'},indent=2)+'\n')
    else:p.write_bytes(body)
def append(name, obj):
    with (OUT/name).open('a') as f: f.write(json.dumps(obj,ensure_ascii=False)+'\n')
def git(*args, cwd=ROOT):
    command=['git',*args]
    p=subprocess.run(command,cwd=cwd,capture_output=True,text=True,check=True)
    append('command-log.jsonl',{'time':now(),'command':command,'cwd':str(cwd),'exit_code':p.returncode,'stdout_sha256':sha(p.stdout.encode()),'kind':'fixed_input_read'})
    return p.stdout.strip()
def bind():
    expected=[('main_head',MAIN,git('rev-parse','HEAD')),('main_tree',MTREE,git('rev-parse','HEAD^{tree}')),('reference_head',RHEAD,git('rev-parse','HEAD',cwd=REF)),('reference_tree',RTREE,git('rev-parse','HEAD^{tree}',cwd=REF)),('formal_tree',FTREE,git('rev-parse','HEAD:deliverables/final-specification-set'))]
    assert all(x[1]==x[2] for x in expected), expected
    return {a:{'expected':b,'observed':c,'match':b==c} for a,b,c in expected}
def family(p):
    stem=p.stem
    return stem.replace('_shadow_pkmn','')
def is_text(fam,key): return key in TEXT and not (fam=='moves' and key=='Category')
def selected():
    return [p for p in sorted((REF/'PBS').rglob('*.txt')) if family(p) in FAMILIES]
def read_range(path, start, end):
    p=ROOT/path
    assert p.resolve().is_relative_to(ROOT)
    lines=p.read_text(encoding='utf-8-sig').splitlines()
    if end==0:end=len(lines)
    assert 1<=start<=end<=len(lines),(path,start,end,len(lines))
    append('reading-ledger.jsonl',{'time':now(),'path':path,'start_line':start,'end_line':end,'sha256':sha(p.read_bytes()),'mode':'model_visible_contiguous_read','semantic_status':'context_read_not_full_domain_approval'})
    print('\n'.join(f'{n}: {lines[n-1]}' for n in range(start,end+1)))
def inventory():
    binding=bind();files=[];records=[];seen={};field_values=defaultdict(Counter);anomalies=[]
    for p in selected():
        b=p.read_bytes();lines=b.decode('utf-8-sig').splitlines();rel=str(p.relative_to(ROOT));fam=family(p)
        blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        tracked=git('rev-parse',RHEAD+':'+str(p.relative_to(REF)),cwd=REF)
        assert blob==tracked,(p,blob,tracked)
        rs=[];cur=None
        for n,line in enumerate(lines,1):
            # This lexer intentionally preserves authored values. It does not
            # claim to duplicate the compiler's comment or CSV semantics.
            s=line.strip()
            if not s or s.startswith('#'):continue
            m=re.fullmatch(r'\[(.*)\]',s)
            if m:
                if cur:cur['end_line']=n-1
                cur={'path':rel,'profile':str(p.parent.relative_to(REF/'PBS')),'family':fam,'identity':m[1],'start_line':n,'end_line':len(lines),'fields':[],'structural_status':'inventoried','semantic_status':'not_fully_reviewed'};rs.append(cur);continue
            m=re.match(r'(\w+)\s*=\s*(.*)',s)
            if m and cur:
                k,v=m.groups();field_values[(fam,k)][v]+=1
                f={'key':k,'line':n,'value_sha256':sha(v.encode())}
                if is_text(fam,k):f.update(text_length=len(v),empty=not v)
                else:f['value']=v
                cur['fields'].append(f)
            else:anomalies.append({'path':rel,'line':n,'kind':'unexpected_lexical_row'})
        dup=[k for k,v in Counter(r['identity'] for r in rs).items() if v>1]
        files.append({'path':rel,'profile':str(p.parent.relative_to(REF/'PBS')),'family':fam,'bytes':len(b),'lines':len(lines),'sha256':sha(b),'git_blob':blob,'same_blob_as':seen.get(blob),'records':len(rs),'duplicate_authored_identities':dup,'semantic_status':'not_fully_reviewed'})
        seen.setdefault(blob,rel);records+=rs
        append('reading-ledger.jsonl',{'time':now(),'path':rel,'start_line':1,'end_line':len(lines),'sha256':sha(b),'mode':'deterministic_full_byte_and_record_inventory','semantic_status':'NOT_A_SEMANTIC_READ','record_count':len(rs)})
    save('input-binding.json',{'time':now(),'bindings':binding,'output_root':str(OUT),'runtime_metadata':{'actual_model':'UNVERIFIED','actual_reasoning_effort':'UNVERIFIED','service_tier':'UNVERIFIED','speed':'UNVERIFIED','runtime_uuid':'UNVERIFIED'},'execution':'No reference, compiler, game, save, or unknown historical script executed.'})
    save('file-inventory.json',files)
    with (OUT/'record-inventory.jsonl').open('w') as f:
        for r in records:f.write(json.dumps(r,ensure_ascii=False)+'\n')
    domains=[]
    for (fam,k),values in sorted(field_values.items()):
        numeric=[]
        for v in values:
            if re.fullmatch(r'-?\d+(?:\.\d+)?',v):numeric.append(float(v))
        row={'family':fam,'field':k,'occurrences':sum(values.values()),'distinct_authored_values':len(values),'numeric_min':min(numeric) if numeric else None,'numeric_max':max(numeric) if numeric else None}
        if is_text(fam,k):row['opaque_text_values']='withheld; hashes and lengths retained per record'
        else:row['values']=[{'value':v,'count':c} for v,c in sorted(values.items())]
        domains.append(row)
    save('field-value-domains.json',domains)
    save('lexical-anomalies.json',anomalies)
    print(json.dumps({'files':len(files),'unique_blobs':len(seen),'lines':sum(x['lines'] for x in files),'records':len(records),'field_domains':len(domains),'unexpected_rows':len(anomalies),'semantic_unread_records':len(records)},indent=2))
    for f in files:print(f['path'],f['records'],f['lines'],'duplicate_blob='+str(f['same_blob_as']))

if __name__=='__main__':
    append('command-log.jsonl',{'time':now(),'argv':sys.argv,'kind':'review_instrumentation','purpose':'read-only inventory / contiguous evidence read','script_sha256':sha(Path(__file__).read_bytes())})
    if sys.argv[1]=='inventory':inventory()
    elif sys.argv[1]=='read':read_range(sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))
    else:raise SystemExit('Unknown command')
