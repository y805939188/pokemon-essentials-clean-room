"""Create reversible, exact-value review views. Generation grants no reading credit."""
from pathlib import Path
import hashlib
import json

P = Path(__file__).resolve().parent
def enc(x):
    return json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
def digest(x):
    return hashlib.sha256(enc(x).encode()).hexdigest()
original = {i: json.loads((P/'originals'/str(i)).read_text()) for i in range(25) if i not in (2,9)}
delegated = {}
for i in (0,1,15,16,18):
    for n,x in enumerate(original[i]['records']):
        delegated[digest(x)] = f'file{i}#/records/{n}'
        if i in (0,15):
            delegated[digest(x['groups'])] = f'file{i}#/records/{n}/groups'
def delegate_children(x,ptr):
    if isinstance(x,(dict,list)) and len(enc(x))>180:
        delegated.setdefault(digest(x),ptr)
    if isinstance(x,dict):
        for k,v in x.items():delegate_children(v,ptr+'/'+k)
    elif isinstance(x,list):
        for k,v in enumerate(x):delegate_children(v,ptr+'/'+str(k))
for i in (0,1,15,18):
    for n,x in enumerate(original[i]['records']): delegate_children(x,f'file{i}#/records/{n}')
prior = {}
for i in (2,3,4,7,8,17,23,24):
    data = (P/'originals'/str(i)).read_text()
    if i==2: continue
    x=json.loads(data)
    prior[digest(x)] = f'file{i}#'
    if i==24:
        for n,row in enumerate(x['records']): prior[digest(row)] = f'file24#/records/{n}'
legacy = original[6]
for kind,rows in legacy.items():
    if not isinstance(rows,list): continue
    for n,x in enumerate(rows):
        if kind=='optional' and n in (1,7):
            prior[digest(x)]=f'file6#/{kind}/{n}'
        else:
            prior[digest(x)]=f'file6#/{kind}/{n} (D text already displayed; fact joins separate)'
        if isinstance(x,dict) and 'original_full_proposal' in x:
            prior[digest(x['original_full_proposal'])] = f'file6#/{kind}/{n}/original_full_proposal (text association only)'

# These fields carry identities, locations or transport coordinates. Every other
# field remains in the view, including all purpose, status and qualification text.
IDENTITY = {'path','original_path','logical_path','transport_path','payload','pointer',
 'fact_id','id','original_id','task','owner','source','locations','range','lines',
 'source_or_necessary_consumer_paths','bytes','sha256','git_blob','git_blob_content_id',
 'transport_bytes','transport_sha256','transport_git_blob_content_id','mode','commit',
 'tree','workspace_tree','repository','repository_id','identity_id','text_sha256',
 'original_index','base_fact_links','current_authored_fact_scope_indices',
 'original_unmapped_registration_ranges','authored_scope_indices','primary',
 'identity','public_projection_identity','public_projection_path','retained_events',
 'excluded_event_counts'}
IDENTITY |= {'successor_id','successor_pointer','evidence','source_fact_ids'}
IDENTITY |= {'canonical_R6_id','successor_path','current_fact_reference','current_clause_reference',
 'case_reference','parent_and_scope_reference','original_contract','original_pointer',
 'current_historical_top_reception_indices'}
STRATA = {
 (20,'/facts'), (21,'/records'), (22,'/units'),
 (10,'/coverage_and_qualification_sections/source_inventory'),
 (10,'/coverage_and_qualification_sections/formal_inventory'),
 (10,'/coverage_and_qualification_sections/supplement_inventory'),
 (10,'/coverage_and_qualification_sections/source_units/units'),
 (10,'/coverage_and_qualification_sections/formal_units/units'),
 (10,'/all_core_logical_payloads/logical_files'),
 (10,'/all_core_logical_payloads/compressed_objects'),
 (10,'/all_core_logical_payloads/local_only_platform_streams'),
 (10,'/coverage_and_qualification_sections/c13_identity_index/identities'),
 (11,'/all_handoff_members'), (11,'/all_C1_report_members'), (18,'/inputs'),
 (5,'/current56/records'), (19,'/derived_323')}
associations=[]; inventories=[]; seen={}
def typed_values(x):
    if isinstance(x,dict):return {k:typed_values(v) for k,v in x.items() if k not in IDENTITY}
    if isinstance(x,list):return [typed_values(v) for v in x]
    return x
def walk(x,fi,ptr=''):
    address=f'file{fi}#{ptr}'
    h=digest(x)
    if h in prior:
        associations.append({'at':address,'exact_value_as':prior[h],'sha256':h,'credit':'DEPENDENCY_TEXT_ONLY'})
        return {'$prior_exact':prior[h]}
    if h in delegated:
        associations.append({'at':address,'exact_value_as':delegated[h],'sha256':h,'credit':'OPEN_OTHER_RECEIVER'})
        return {'$delegated_open':delegated[h]}
    if (fi,ptr) in STRATA:
        groups={}
        for n,row in enumerate(x):
            assert isinstance(row,dict)
            business=typed_values(row)
            s=enc(business)
            groups.setdefault(s,{'values':business,'rows':[]})['rows'].append(n)
        inventories.append({'at':address,'rows':len(x),'row_keysets':sorted({tuple(sorted(r)) for r in x}),
          'sha256':h,'identity_fields':sorted(IDENTITY & {k for row in x for k in row}),
          'groups':[{'values':g['values'],'row_indices':g['rows']} for g in groups.values()],
          'target_body_credit':0})
        return {'$typed_index':address,'rows':len(x),'all_row_keysets':inventories[-1]['row_keysets'],
          'identity_fields':inventories[-1]['identity_fields'],
          'all_distinct_nonidentity_values':[walk(g['values'],fi,ptr+'/@group/'+str(n)) for n,g in enumerate(groups.values())],
          'target_body_credit':0}
    # Long exact duplicate values retain their complete pointer and identity.
    if len(enc(x))>60 and h in seen:
        associations.append({'at':address,'exact_value_as':seen[h],'sha256':h,'credit':'SAME_VALUE_DISPLAY_DEPENDENCY'})
        return {'$same_value':seen[h]}
    if len(enc(x))>60:seen[h]=address
    if isinstance(x,dict):return {k:walk(v,fi,ptr+'/'+k) for k,v in x.items()}
    if isinstance(x,list):return [walk(v,fi,ptr+'/'+str(n)) for n,v in enumerate(x)]
    return x

for i in (0,1,15,18,16,5,19,20,21,22,12,13,14,11,10):
    x=walk(original[i],i)
    data=json.dumps(x,ensure_ascii=False,indent=2)+'\n'
    (P/'views'/f'scope-{i}.json').write_text(data)
    print(i,len(data.encode()),len(data.splitlines()))
(P/'scope-associations.json').write_text(json.dumps(associations,ensure_ascii=False,indent=2)+'\n')
(P/'private/typed-index-inventory.json').write_text(json.dumps(inventories,ensure_ascii=False,indent=2)+'\n')
print('ASSOCIATIONS',len(associations),'TYPED ARRAYS',len(inventories))
