"""Continuation document-only reader; no inspected program is executed."""
import json,re,hashlib,pathlib,sys,gzip
from audit_documents import corpus,ROOT,ACT,OUT,mechanical
from read_documents import record
def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def pure_identity(v,contexts):
    if not isinstance(v,str):return True
    if re.fullmatch(r'[0-9a-f]{7,64}|[0-9]+(?:\.[0-9]+)?|[0-9;,\-–— ]+',v):return True
    if re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*:(?:[0-9]+|[0-9a-f]{7,64})',v):return True
    if re.fullmatch(r'[A-Z][A-Z0-9_-]*[0-9][A-Z0-9_-]*',v):return True
    if '\n' not in v and not re.search(r'\s',v) and '/' in v:
        if re.fullmatch(r'[A-Za-z0-9_./:#~%+=,@*\[\]<>|?\-]+',v) and re.match(r'^(?:[0-9a-f]{8,40}|GIR-FD82-[A-Z0-9]+|WP[0-9]+-[A-Z0-9_-]+|report|plan|finding|acceptance|review|reference|specs|deliverables|Data|PBS|formal_diff|text:review|original|approved)/',v):return True
        if re.fullmatch(r'[A-Za-z0-9_./:#~%+=,@*\[\]<>|?\-]+',v) and (re.match(r'^[0-9a-f]{8,40}:',v) or re.search(r'\.(?:jsonl?|md|rb|tsv|py|txt)(?:[#:/]|$)',v) or re.fullmatch(r'B[0-9]{2}/[A-Z][A-Z0-9_-]*',v)):return True
        if v.startswith('/') and re.fullmatch(r'[A-Za-z0-9_./:#~%+=,@*\[\]<>|?\-]+',v):return True
        if re.match(r'^(?:[0-9a-f]{8,40}:)?(?:review|specs|planning|audit|deliverables|reference|Data|PBS|Graphics|Audio)/',v) and re.search(r'\.(?:md|jsonl?|tsv|csv|rb|txt|patch|diff|py|gz|dat)(?::[0-9,;–\-]+|#[^\s]*)?$',v):return True
    if re.fullmatch(r'[AMD]\t[^\n]+\.(?:md|jsonl?|tsv|patch|py|txt)',v):return True
    if re.fullmatch(r'[^\t\n]+\t[0-9a-f]{40}\t[0-9a-f]{64}\t[0-9]+\tINTENDED_G_SNAPSHOT_AWAIT_EXTERNAL_ACT',v):return True
    if re.fullmatch(r':[0-9]{6} [0-9]{6} [0-9a-f]{40} [0-9a-f]{40} [AMD]\t[^\n]+',v):return True
    if v.startswith(('diff --git ','index ','--- a/','+++ b/','--- /dev/null','new file mode ')):return True
    if re.fullmatch(r'@@ -[0-9,]+ \+[0-9,]+ @@',v):return True
    # Paths with spaces are pure only when the file suffix/optional locator ends the string.
    if re.match(r'^(?:[0-9a-f]{8,40}[:/])?(?:review|specs|planning|audit|deliverables|reference|Data|PBS|Graphics|Audio|agents|root)/',v):
        if re.search(r'\.(?:md|jsonl?|tsv|csv|rb|txt|patch|diff|py|gz|dat)(?::[0-9,;–\-]+|#[^\s]*)?$',v) and '\n' not in v:return True
    # A structural-node child-name is a schema key, with every original context retained.
    if all(re.search(r'/(?:structures|container_type_length_map)/\d+/children/\d+$',c) for c in contexts):return True
    return False
def load():
    cache=OUT/'continuation-transient-corpus.json.gz'
    if cache.exists():
        with gzip.open(cache,'rt') as f:vals,occ,struct,ids=json.load(f)
    else:
        vals,occ,struct,ids=corpus()
        with gzip.open(cache,'wt',compresslevel=3) as f:json.dump([vals,occ,struct,ids],f,ensure_ascii=False,separators=(',',':'))
    events=[json.loads(l) for l in (OUT/'delivery-log.jsonl').read_text().splitlines()]
    confirmed=set()
    for e in events:
        if e.get('kind')=='audit_group_semantic_delivery' and e.get('pattern') in ['/B14/integration-stage-1/','affected-B02-actual-review-1/reading-log.json']:
            confirmed.update(e['value_hashes'])
        if e.get('kind')=='continuation_semantic_confirmed':confirmed.update(e['value_hashes'])
    # Complete, untruncated literal bodies are exact-value semantic reuse, never quality transfer.
    completed={e['commit']+':'+e['path'] for e in events if e.get('kind')=='line_delivery' and e.get('range_inclusive')==[1,e.get('total_lines')]}
    for i,v in enumerate(vals):
        if any(c.split('#')[0] in completed for c in occ[i]):confirmed.add(digest(v))
    remaining=[i for i,v in enumerate(vals) if not pure_identity(v,occ[i]) and digest(v) not in confirmed]
    mixed=[i for i,v in enumerate(vals) if isinstance(v,str) and mechanical(v) and not pure_identity(v,occ[i])]
    return vals,occ,struct,ids,remaining,mixed,confirmed
if __name__=='__main__':
    vals,occ,struct,ids,left,mixed,confirmed=load();mode=sys.argv[1]
    print('Unconfirmed real semantic strings',len(left),'bytes',sum(len(vals[i].encode()) for i in left),'mixed strings restored',len(mixed))
    if mode=='confirm':
        events=[json.loads(l) for l in (OUT/'delivery-log.jsonl').read_text().splitlines()]
        e=next(e for e in reversed(events) if e.get('kind')=='continuation_semantic_delivered' and (len(sys.argv)<3 or len(e['indices'])==int(sys.argv[2])))
        record({'kind':'continuation_semantic_confirmed','value_hashes':e['value_hashes'],'indices':e['indices'],'basis':'All exact displayed values consumed without truncation; every native context retained in audit map.'})
        print('Confirmed',len(e['indices']))
    elif mode=='read':
        a,b=map(int,sys.argv[2:4])
        for n in range(a,min(b,len(left))):
            i=left[n];print('N'+str(n),'V'+str(i),json.dumps(vals[i],ensure_ascii=False))
        record({'kind':'continuation_semantic_delivered','slice':[a,min(b,len(left))],'indices':left[a:b],'value_hashes':[digest(vals[i]) for i in left[a:b]],'requires_confirmation':True,'classifier':'pure_identity_v3; no mixed prose prefix discard'})
    elif mode=='inventory':
        data={'version':4,'exact_corpus_values':len(vals),'semantic_indices':[i for i,v in enumerate(vals) if not pure_identity(v,occ[i])],'unconfirmed':left,'mixed_strings_restored':mixed,'confirmed_hashes':sorted(confirmed),'classification_rule':'Complete context/type/structure preservation; pure identities/schema nodes verified mechanically; mixed path/selector prose remains semantic.'}
        (OUT/'continuation-semantic-index.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
        for i in mixed[:15]:print('MIXED',i,json.dumps(vals[i],ensure_ascii=False))
