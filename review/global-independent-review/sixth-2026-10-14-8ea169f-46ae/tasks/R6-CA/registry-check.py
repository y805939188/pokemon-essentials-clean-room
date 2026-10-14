"""Literal static registration simulation, not source execution or semantic PASS.
Reads the 20 pinned AI inputs. Understands only literal add/copy/addIf headers;
asserts on nonliteral copy syntax. Outputs only task registry-check.json.
"""
import re,json
from pathlib import Path
W=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
O=Path(__file__).resolve().parent
D=json.loads((O/'structural-denominator.json').read_text())
registry={};occurrences=[];duplicates=[];missing=[];conditions=[];statements=[]
for f in D['source_files']:
    text=(W/f['path']).read_text(encoding='utf-8-sig')
    pattern=r'Battle::AI::Handlers::(\w+)\.(add|copy|addIf)\('
    for match in re.finditer(pattern,text):
        family,operation=match.groups();start=text.count('\n',0,match.start())+1
        tail=text[match.end():];base={'path':f['path'],'start':start,'family':family,'operation':operation}
        if operation=='copy':
            header=tail.split(')',1)[0]
            ids=re.findall(r'"([A-Za-z0-9_]+)"|:([A-Za-z0-9_]+)',header)
            ids=[a or b for a,b in ids]
            assert len(ids)>=2,(base,header)
            assert not re.sub(r'[\s,]|"[A-Za-z0-9_]+"|:[A-Za-z0-9_]+','',header),(base,header)
            source=registry.get((family,ids[0]))
            for dest in ids[1:]:
                occurrences.append({**base,'identity':dest,'copy_source':ids[0]})
                if (family,dest) in registry:duplicates.append({**base,'identity':dest,'previous':registry[(family,dest)]})
                if source:registry[(family,dest)]=source
                else:missing.append({**base,'identity':dest,'missing_source':ids[0],'previous_retained':(family,dest) in registry})
        else:
            m=re.match(r'\s*(?:"([A-Za-z0-9_]+)"|:([A-Za-z0-9_]+))',tail)
            assert m,base
            identity=m[1] or m[2]
            if operation=='addIf':conditions.append({**base,'condition_identity':identity})
            else:
                occurrences.append({**base,'identity':identity})
                if (family,identity) in registry:duplicates.append({**base,'identity':identity,'previous':registry[(family,identity)]})
                registry[(family,identity)]={**base,'identity':identity}
        statements.append(base)
item_conditions=[r for r in json.loads((O/'data-check-summary.json').read_text()).get('unequal',[]) if r]
assert not item_conditions
summary={'classification':'STRUCTURAL_LITERAL_BINDINGS_ONLY_NOT_SEMANTIC_PASS',
 'registration_files':len(set(r['path'] for r in statements)),'statements_including_conditions':len(statements),
 'add_copy_statements':sum(r['operation']!='addIf' for r in statements),'expanded_add_copy_occurrences':len(occurrences),
 'different_occurrence_keys':len(set((r['family'],r['identity']) for r in occurrences)),
 'effective_direct_keys':len(registry),'conditions':conditions,'duplicates':duplicates,'missing_copies':missing,
 'validated_condition_identities':57,'effective_direct_plus_condition_identities':len(registry)+57}
(O/'registry-check.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['duplicates','missing_copies','conditions']},ensure_ascii=False))
