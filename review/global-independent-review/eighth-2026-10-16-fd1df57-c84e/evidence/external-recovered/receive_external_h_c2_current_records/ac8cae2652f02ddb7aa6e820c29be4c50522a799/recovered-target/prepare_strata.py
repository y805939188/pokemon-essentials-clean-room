"""Prepare exact purpose strata; inventories confer no target-body credit."""
from pathlib import Path
import json, re, hashlib
import semantic_reader as sr

T = Path(__file__).parent
W = T / '.publication-work' / 'strata'
W.mkdir(parents=True, exist_ok=True)
state = json.loads(sr.STATE.read_text())
manifest = sr.load_doc(10)
inventory = []

def typed(value, anchor, purpose, fields):
    """All rows retained; exact shared qualifier values factored without prose."""
    groups = {}
    for n, row in enumerate(value):
        semantics = {k: row[k] for k in fields if k in row}
        key = sr.digest(semantics)
        groups.setdefault(key, {'exact_values': semantics, 'row_indices': []})['row_indices'].append(n)
    for group in groups.values():
        runs=[]
        for n in group.pop('row_indices'):
            if runs and n==runs[-1][1]+1:runs[-1][1]=n
            else:runs.append([n,n])
        group['original_row_pointer_prefix']=anchor+'/'
        group['complete_inclusive_index_runs']=runs
    out = W / (hashlib.sha256(anchor.encode()).hexdigest() + '.json')
    out.write_text(json.dumps(value, ensure_ascii=False, separators=(',', ':')))
    receipt = {'anchor': anchor, 'purpose': purpose, 'rows': len(value),
               'all_row_keysets': sorted({tuple(sorted(x)) for x in value}),
               'original_array_sha256': sr.digest(value), 'inventory_path': str(out),
               'body_reading_credit': 0, 'groups': list(groups.values())}
    inventory.append(receipt)
    # Group memberships are typed locators, never facts or bodies.
    return {'typed_index': len(inventory)-1, 'purpose': purpose, 'rows': len(value),
            'exact_shared_values': [x['exact_values'] for x in groups.values()]}

fact = sr.load_doc(20)
fact['facts'] = typed(fact['facts'], 'file20#/facts',
    'HISTORICAL_SOURCE_FACT_POINTER_PURPOSE_INDEX; target objects and source bodies not approved', ['scope'])
clause = sr.load_doc(21)
overrides = [r['exact_reception_override'] for r in clause['records'] if 'exact_reception_override' in r]
clause['records'] = typed(clause['records'], 'file21#/records',
    'HISTORICAL_AUTHORED_CLAUSE_LOCATION_INDEX; target assertions are not embedded or newly read', ['facts_and_premise_consumer', 'qualification'])
clause['exact_override_purpose_stratum'] = typed(overrides, 'file21#/exact_override_purpose_stratum',
    'HISTORICAL_EXACT_RECEPTION_POINTER_AND_STATUS_INDEX; no successor-body reading credit', ['disposition', 'evidence', 'owner'])
program = sr.load_doc(22)
program['units'] = typed(program['units'], 'file22#/units',
    'HISTORICAL_PROGRAM_LOCATION_AND_BOUNDED_READ_STATUS_INDEX; no program body included or execution credit',
    ['kind', 'status', 'premise', 'source_fact_ids', 'evidence'])

coverage = manifest['coverage_and_qualification_sections']
for key, fields in [
    ('source_inventory', ['reading_status', 'evidence_level', 'current_review']),
    ('formal_inventory', ['reading_status', 'evidence_level', 'current_review']),
    ('supplement_inventory', ['reading_status', 'evidence_level', 'current_review']),
    ('source_units', ['qualification', 'reception']),
    ('formal_units', ['qualification', 'reception', 'structure_type']),
]:
    obj = coverage[key]
    arrkey = next(k for k,v in obj.items() if isinstance(v,list) and v and isinstance(v[0],dict)) if isinstance(obj,dict) else None
    arr = obj[arrkey] if arrkey else obj
    converted = typed(arr, 'file10#/coverage_and_qualification_sections/' + key + ('/' + arrkey if arrkey else ''),
         'HISTORICAL_COVERAGE_LOCATION_PURPOSE_INDEX; original status generation preserved, no source or formal-body approval', fields)
    if arrkey: obj[arrkey] = converted
    else: coverage[key] = converted

coverage['source_facts'] = fact
coverage['clause_subassertions'] = clause
coverage['finite_programs'] = program
for key in ('all_core_logical_payloads',):
    obj = manifest[key]
    for k,v in list(obj.items()):
        if isinstance(v,list) and v and isinstance(v[0],dict):
            obj[k] = typed(v, 'file10#/' + key + '/' + k,
                'TRANSPORT_IDENTITY_INDEX_ONLY; no semantic payload or target-body reading credit',
                ['purpose', 'reading_scope_authority', 'transport_reading_status', 'content_blob_qualification', 'payload_type', 'encoding'])

ident = coverage['c13_identity_index']
ident['identities'] = typed(ident['identities'], 'file10#/coverage_and_qualification_sections/c13_identity_index/identities',
    'FIXED_INPUT_IDENTITY_INDEX_ONLY; no source reading or Git membership approval', ['repository_id', 'evidence_level'])

binding = sr.load_doc(11)
for k in ('all_handoff_members', 'all_C1_report_members'):
    binding[k] = typed(binding[k], 'file11#/' + k,
        'PUBLICATION_PATH_MODE_BYTE_SHA_BLOB_IDENTITY_INDEX_ONLY; no body semantics or this-task remote readback claim', [])

for label, value, anchor in [('source_pointer_purposes',fact,'file20#'), ('clause_pointer_purposes',clause,'file21#'),
                              ('program_pointer_purposes',program,'file22#'), ('manifest_strata',manifest,'file10#'),
                              ('binding_strata',binding,'file11#')]:
    text=json.dumps(sr.render(value,anchor,state,{}),ensure_ascii=False,separators=(',',':'))
    parts=[text[j:j+16000] for j in range(0,len(text),16000)] or ['']
    for j,s in enumerate(parts):(W/f'{label}.{j}.txt').write_text(s)
    print(label,len(text),len(parts))
    (W/f'{label}.identity.json').write_text(json.dumps({'anchor':anchor,'display_sha256':hashlib.sha256(text.encode()).hexdigest(),
        'parts':len(parts),'purpose':'EXACT_SHARED_QUALIFIERS_AND_ACKNOWLEDGED_DUPLICATES; typed pointer inventories no target-body credit'},ensure_ascii=False,indent=2))
(T/'typed-purpose-strata.json').write_text(json.dumps({'schema':'r8.external-h-c2.exact-purpose-strata.v1',
    'rule':'All indexed rows retained and keysets checked. Shared qualifier values are exact, not summaries. Target objects and bodies are not read by indexing them.',
    'strata':inventory},ensure_ascii=False,indent=2)+'\n')
sr.STATE.write_text(json.dumps(state,ensure_ascii=False,indent=1)+'\n')
