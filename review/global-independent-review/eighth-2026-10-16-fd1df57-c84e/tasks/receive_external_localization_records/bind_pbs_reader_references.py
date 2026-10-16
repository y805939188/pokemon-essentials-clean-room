"""Resolve exact literal aliases to actual named readers; generation is not reading."""
from pathlib import Path
import collections
import json

T = Path(__file__).resolve().parent
def load(p): return json.loads((T / p).read_text())
named = load('continuation/received-parts/parent-acceptance.json')['records']
previous_path = T/'continuation/pbs-field-binding/actual-reader-bindings.json'
previous = {(r['unit'],r['field']):r for r in json.loads(previous_path.read_text())['rows']} if previous_path.exists() else {}
readers = {r['id']: {'context':r['reader_context'],'part':r['part']} for r in named}
for r in load('reading-ledger.json')['literal_record_reads']:
    readers[r['id']] = {'context':'01a14465-d18e-725b-b69c-2e6f52300005','part':'parent_actual_literal_read'}
raw = {}
for p in (T / 'evidence/primary-reference').glob('*.txt'):
    raw[p.stem] = p.read_text(encoding='utf-8-sig').splitlines()
pool = collections.defaultdict(list)
for rid in sorted(readers):
    domain, number = rid[4:].rsplit('-',1); n = int(number)
    for field, pos in [('key',2*n+2),('value',2*n+3)]:
        pool[raw[domain][pos]].append({'record_id':rid,'field':field,**readers[rid]})
result = []; counts = collections.Counter()
for r in load('continuation/pbs-field-binding/unique-necessary-records.json'):
    for field, ref in r['fields'].items():
        out = {'unit':r['id'],'family':r['family'],'field':field,'original_literal_reference':ref}
        if ref is None:
            out['status']='ABSENCE_CONTEXT_ACTUALLY_READ'; counts['absent']+=1
        elif 'NEW_LITERAL' in ref:
            out.update(status='ACTUALLY_READ_NEW_LITERAL',reader_context='01a14465-d18e-725b-b69c-2e6f52300005',literal_id=ref['NEW_LITERAL'])
            assert ref['NEW_LITERAL'] in load('continuation/pbs-field-binding/new-literals.json')
            counts['new_literal_occurrences']+=1
        else:
            domain,n,which=ref['CORPUS_EXACT_LITERAL']; value=raw[domain][2*n+2+(which=='value')]
            candidates=pool.get(value,[])
            if candidates:
                old=previous.get((r['id'],field),{}).get('actual_literal_reader')
                if old:
                    rid=old['record_id']; dom,num=rid[4:].rsplit('-',1); number=int(num)
                    assert rid in readers and raw[dom][2*number+2+(old['field']=='value')]==value
                    assert old['context']==readers[rid]['context'] and old['part']==readers[rid]['part']
                out.update(status='EXACT_LITERAL_BOUND_TO_ACTUAL_RECEIVED_READER',actual_literal_reader=old or candidates[0])
                counts['corpus_literals_resolved']+=1
            else:
                out['status']='PENDING_D_ACTUAL_LITERAL_RECEPTION';counts['corpus_literals_pending_D']+=1
        result.append(out)
empty_s=[]
for r in load('continuation/pbs-field-binding/raw-required-fields-and-positions.json'):
    for field, pair in r['fields'].items():
        if field not in {'Description','Pokedex','FormName'} and pair[1]=='':
            empty_s.append({'path_index':r['path_index'],'unit':r['unit'],'field':field,'line':pair[0]})
out={'schema':'gr8-elr-pbs-exact-literal-reader-bindings/v1','rows':result,'counts':dict(counts),'empty_s_fields':empty_s,
     'qualification':'Every unit/header/field-reference/context and all149 new literal definitions actually read separately. Equality binds only the complete literal value; runtime domain/producer/getter/default/premise comes from the PBS family contract. No new record reading, source vote, gameplay or complete PBS-body acceptance.',
     'generation_reading_credit':0,'behavior_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
(T/'continuation/pbs-field-binding/actual-reader-bindings.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'counts':dict(counts),'empty_s_fields':len(empty_s),'generation_reading_credit':0}))
