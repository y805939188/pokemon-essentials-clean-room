"""Read-only literal comparisons for already freshly read formal finite tables.

Only plain fields in these fixed data records are used. No reference callback,
compiler, evaluator, deserializer, game or independent gameplay model is run.
R6-D author-field semantics remain a separately imported prerequisite.
"""
from pathlib import Path
import json,re,csv,datetime,hashlib
P=Path(__file__).parent
R=Path('reference/pokemon-essentials/PBS')
def records(name):
    path=R/name;out={};cur=None
    for n,line in enumerate(path.read_text().splitlines(),1):
        s=line.strip()
        if not s or s.startswith('#'):continue
        m=re.fullmatch(r'\[([^\]]+)\]',s)
        if m:
            cur={'path':str(path),'identity':m[1],'start_line':n,'end_line':n,'fields':{},'field_lines':{}}
            out[m[1]]=cur
        elif cur and '=' in s:
            k,v=s.split('=',1);k=k.strip();v=v.strip();cur['fields'][k]=v;cur['field_lines'][k]=n;cur['end_line']=n
            if k in ['Evolution','Evolutions']:cur.setdefault('evolution_rows',[]).append({'line':n,'value':v,'key':k})
    return out
base=records('pokemon.txt');forms=records('pokemon_forms.txt');items=records('items.txt');moves=records('moves.txt')
checks=[];bindings=[]
doc=Path('deliverables/final-specification-set/pokemon-rules/wp22-transformation-data.md')
for n,line in enumerate(doc.read_text().splitlines(),1):
    if not 11<=n<=58:continue
    cols=[x.strip() for x in line.split('|')[1:-1]]
    species,form,req,stats=cols;d=forms[species+','+form];f=d['fields']
    values=[int(x) for x in next(csv.reader([f['BaseStats']]))]
    expected=[int(x) for x in stats.split('／')]
    kind,target=req.split(' ',1);key='MegaStone' if kind=='石' else 'MegaMove'
    ok=(values==expected and f.get(key)==target and int(f.get('UnmegaForm','0'))==0 and int(f.get('MegaMessage','0'))==(1 if species=='RAYQUAZA' else 0))
    checks.append({'table':'Mega48','formal_line':n,'identity':d['identity'],'reference_record':{k:d[k] for k in ['path','start_line','end_line']},'expected':expected,'actual':values,'requirement_field':key,'actual_requirement':f.get(key),'match':ok,'base_hp':int(base[species]['fields']['BaseStats'].split(',')[0])})
stones={x['fields']['MegaStone'] for x in forms.values() if 'MegaStone' in x['fields']}
flagged={k for k,v in items.items() if 'MegaStone' in v['fields'].get('Flags','').split(',')}
checks.append({'table':'47stones_and_ring','stone_sets_equal':stones==flagged,'stone_count':len(stones),'flagged_count':len(flagged),'rings':[k for k,v in items.items() if 'MegaRing' in v['fields'].get('Flags','').split(',')],'orb_flags':{k:items[k]['fields'].get('Flags','') for k in ['BLUEORB','REDORB']}})
doc=Path('deliverables/final-specification-set/pokemon-rules/wp32-context-inputs-and-scenarios.md')
methodcounts={};evo=[]
for ident,rec in {**base,**forms}.items():
    for row in rec.get('evolution_rows',[]):
        a=next(csv.reader([row['value']])) if row['value'] else []
        for i in range(0,len(a),3):
            if i+1>=len(a):continue
            target,method=a[i:i+2];param=a[i+2] if i+2<len(a) else ''
            evo.append((ident,target,method,param,{**rec,'evolution_line':row['line']}))
            methodcounts[method]=methodcounts.get(method,0)+1
for n,line in enumerate(doc.read_text().splitlines(),1):
    if not 53<=n<=109:continue
    a=[x.strip() for x in line.split('|')[1:-1]]
    ident,target,method,param=a;param='' if param=='无' else param
    hit=[x for x in evo if x[:4]==(ident,target,method,param)]
    checks.append({'table':'Context57','formal_line':n,'expected':[ident,target,method,param],'matches':len(hit),'source_refs':[{'path':x[4]['path'],'line':x[4]['evolution_line'],'record_start':x[4]['start_line'],'record_end':x[4]['end_line']} for x in hit]})
for n,line in enumerate(doc.read_text().splitlines(),1):
    if not 9<=n<=43:continue
    a=[x.strip() for x in line.split('|')[1:-1]]
    method,expected=a[0],int(a[1]);checks.append({'table':'Context35counts','formal_line':n,'method':method,'expected':expected,'actual':methodcounts.get(method,0),'match':expected==methodcounts.get(method,0)})
rows=json.loads((P.parent/'R6-D/pbs-bulk/shadow-formal-table-comparison.json').read_text())
checks.append({'table':'OptionalShadow153','records':len(rows),'all_literal_checks_true':all(all(v for k,v in x.items() if k.startswith('matches_')) for x in rows),'scope':'Separate D literal table comparisons and field semantics; does not enable backups or execute effects.'})
result={'evidence':'TOOL_VALIDATION_LITERAL_DATA_ONLY','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reference_functions_executed':0,'runtime_compile':0,'gameplay_model':0,'native_host':0,'no_source_read_credit_from_parser':True,'checks':checks}
(P/'finite-data-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
bad=[x for x in checks if x.get('match') is False or ('matches' in x and x['matches']!=1)]
print(json.dumps({'checks':len(checks),'mismatches':bad,'mega_records':sum(x.get('table')=='Mega48' for x in checks),'context_records':sum(x.get('table')=='Context57' for x in checks),'context_counts':sum(x.get('table')=='Context35counts' for x in checks),'stone_set':next(x for x in checks if x.get('table')=='47stones_and_ring'),'execution':'NO_REFERENCE_FUNCTION_OR_HOST'},ensure_ascii=False))
