"""Independent static audit views; never a behavior simulator or reading certificate."""
import json, pathlib, subprocess, re, sys, hashlib, collections
from review_bookkeeping import document, get, ROOT, event, artifact_bytes
def replay(r,cache):
    o=r['occurrences'][0];k=(o['commit'],o['path'])
    if k not in cache:cache[k]=document(get(*k),o['path'])
    v=cache[k]
    for s in o['selector']:v=v[s]
    return v,o
if sys.argv[1]=='prepare':
    m=json.loads(artifact_bytes('audit-map.json'));inv=json.loads((ROOT/'stream-inventory.json').read_text())['predecessor']['inventory'];allowed={};cache={}
    for r in inv:
        ranges=[]
        for h in r['hunks']:
            x=re.search(r'\+(\d+)(?:,(\d+))?',h);a=int(x[1]);n=int(x[2] or 1);ranges.append((a-1,a+n-1))
        allowed[r['path']]=ranges
    primary={r['sha256'] for r in json.loads((ROOT/'primary-map.json').read_text())['values']}
    queue=[];mechanical=[];counts=collections.Counter()
    for i,r in enumerate(m['values']):
        v,o=replay(r,cache);p=o['path'];s=o['selector'];reason=None
        if r['sha256'] in primary:reason='EXACT_TYPED_PRIMARY_REUSE'
        elif not isinstance(v,str):reason='TYPED_STRUCTURAL_SCALAR'
        elif '/B14/' not in p and s and s[0]=='lines' and not any(a<=s[1]<b for a,b in allowed[p]):reason='UNCHANGED_PREFIX_OUTSIDE_UNFILTERED_HUNKS'
        elif p.endswith('.tsv') and s and s[0]=='rows' and p.endswith(('approval-ledger.tsv','traceability-successor.tsv')) and s[1]<170:reason='UNCHANGED_ACCEPTED_PREFIX_BYTE_VERIFIED'
        elif not re.search('[\u4e00-\u9fff]',v):
            if re.fullmatch(r'[A-Za-z0-9_.:/#@~+\[\]$\"\x27-]+',v) or re.fullmatch(r'[\d\W]*',v):reason='PURE_IDENTIFIER_OR_LAYOUT'
            elif '\n' not in v and re.fullmatch(r"[^;\n]*\.(?:json|md|diff|rb|tsv|patch|py|txt)(?:[/#:]|$)[A-Za-z0-9_./~#:$\[\]\"' -]*",v):reason='PURE_LOCATOR'
            elif str(s[-1]) in ['pointer','first','at','unique_value_id','mapped_value_id','value_id','selector'] and re.fullmatch(r'[A-Za-z0-9_./~:#$\[\]\" -]+',v) and '/' in v:reason='PURE_GENERATED_SELECTOR'
        if reason:mechanical.append({'value':i,'reason':reason});counts[reason]+=1
        else:queue.append(i);counts['SEMANTIC_VALUES']+=1;counts['SEMANTIC_CHARS']+=len(v)
    result={'queue':queue,'mechanical_or_reuse':mechanical,'counts':dict(counts),'policy':'All changed/new audit prose remains in semantic queue. Pure identities/typed nodes reconstructed from complete fixed objects; no mixed path-plus-prose suppression. Public unchanged prefixes preserve exact bytes and roles. Exact typed primary reuse binds every original occurrence and structure, contingent on completed primary supplements.'}
    (ROOT/'audit-semantic-plan.json').write_text(json.dumps(result,indent=2)+'\n');print(counts)
elif sys.argv[1]=='consume':
    m=json.loads(artifact_bytes('audit-map.json'));q=json.loads((ROOT/'audit-semantic-plan.json').read_text())['queue'];start=int(sys.argv[2]);offset=int(sys.argv[3]) if len(sys.argv)>3 else 0;cache={};budget=int(sys.argv[4]) if len(sys.argv)>4 else 7500;used=0;pos=start;read=[];context=None
    estimated_tokens=0
    while pos<len(q) and used<budget and estimated_tokens<5200:
        i=q[pos];v,o=replay(m['values'][i],cache);left=v[offset:];take=min(len(left),budget-used);fragment=left[:take]
        overhead=60+len(json.dumps(o['selector'],ensure_ascii=False))*0.45
        remaining=max(100,5200-estimated_tokens-overhead)
        while take>100 and (len(re.findall('[\u4e00-\u9fff]',fragment))*1.7+(len(fragment)-len(re.findall('[\u4e00-\u9fff]',fragment)))*0.32)>remaining:
            take=max(100,int(take*0.8));fragment=left[:take]
        if o['path']!=context:print('CONTEXT',o['path']);context=o['path']
        print('VALUE',i,'QUEUE',pos,'SELECTOR',json.dumps(o['selector'],ensure_ascii=False,separators=(',',':')),'CHARS',offset,offset+take,'OF',len(v));print(fragment)
        read.append({'value':i,'characters':[offset,offset+take],'length':len(v)});used+=take;offset+=take
        cjk=len(re.findall('[\u4e00-\u9fff]',fragment));estimated_tokens+=overhead+cjk*1.7+(len(fragment)-cjk)*0.32
        if offset==len(v):pos+=1;offset=0
        else:break
    print('NEXT',pos,offset,'TOTAL',len(q));event({'mode':'semantic-fragments-delivered','queue':'audit-semantic-plan.json','start':[start,int(sys.argv[3]) if len(sys.argv)>3 else 0],'next':[pos,offset],'fragments':read,'not_a_reading_certificate':True})
