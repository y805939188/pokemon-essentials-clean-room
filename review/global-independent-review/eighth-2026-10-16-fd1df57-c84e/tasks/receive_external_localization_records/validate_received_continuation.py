#!/usr/bin/env python3
"""Parent-authored byte/structure checks; never executes recovered programs or Ruby."""
import collections
import hashlib
import json
from pathlib import Path
import subprocess
import sys

T = Path(__file__).resolve().parent

def load(p):
    return json.loads((T / p).read_text())

def save(p, data):
    (T / p).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def sha(b):
    return hashlib.sha256(b).hexdigest()

def git(*args, reference=False):
    return subprocess.check_output(['git'] + (['--git-dir=/tmp/r8-elr-reception-reference.git'] if reference else []) + list(args))

def records():
    original = load('evidence/recovered-target/reading-ledger.json')
    units = {u['id']: u for u in original['units']}
    forward = load('evidence/recovered-target/forward-mapping.json')
    fmap = {u['unit']: u for u in forward['records']}
    groups = {g['domain']: g for g in forward['fact_groups']}
    accepted = []
    receipts = []
    contexts = {'records_a': '01a14489-ff6c-768f-a559-703851d89034', 'records_b': '01a1448a-24b4-73d7-aa11-96a1ddb0400a',
                'records_c': '01a1448d-21a1-710d-806a-eb8cc5fe2022'}
    pure = {'id', 'identity', 'lines', 'record', 'key_sha256', 'translation_sha256'}
    for part in contexts:
        prefix = 'continuation/received-parts/' + part + '/'
        manifest = load(prefix + 'parent-retrieval-identity.json')
        for f in manifest['files']:
            b = (T / f['local']).read_bytes()
            assert len(b) == f['bytes'] and sha(b) == f['sha256']
            assert git('show', manifest['commit'] + ':' + f['path']) == b
        contract = load('continuation/contracts/readsets/' + part + '.complete.json')
        semantics = load('continuation/contracts/readsets/' + part + '.original-semantic-fields.json')
        identity = load('continuation/contracts/readsets/' + part + '.identity-only-index.json')['rows']
        rec = load(prefix + 'reception-ledger.json')['records']
        reading = load(prefix + 'reading-ledger.json')['records']
        assert [x['id'] for x in rec] == [x['id'] for x in reading] == contract['record_ids'] == [x['id'] for x in identity]
        bindings = rec if part == 'records_a' else (reading if part == 'records_c' else load(prefix + 'mechanical-record-bindings.json')['rows'])
        assert len(bindings) == len(rec)
        for fact in semantics['fact_groups']:
            assert fact == groups[fact['domain']]
        for i, (r, read, ident, bind) in enumerate(zip(rec, reading, identity, bindings)):
            domain = r.get('domain', r.get('domain_contract'))
            u = units[r['id']]
            assert {k: u[k] for k in pure} == ident
            template = semantics['templates'][domain]
            assert {k: v for k, v in u.items() if k not in pure} == template['complete_original_unit_semantic_fields']
            assert {k: v for k, v in fmap[r['id']].items() if k != 'unit'} == template['complete_original_forward_fields']
            raw = (T / 'evidence/primary-reference' / (domain + '.txt')).read_text(encoding='utf-8-sig').splitlines()
            a, z = u['lines']
            key, value = raw[a - 1], raw[z - 1]
            literal = bind['raw_key_and_translation_equal_literal'] if part == 'records_a' else (bind['full_literal_value'] if part == 'records_c' else bind['literal'])
            assert key == value == literal
            assert sha(key.encode()) == u['key_sha256'] and sha(value.encode()) == u['translation_sha256']
            if part != 'records_c': assert read['literal_read_here'] is True
            if part == 'records_a':
                assert r['source'] == ident and r['necessary_local_unread'] == []
                assert r['profile'] == 'semantic-profiles.json#/domains/' + r['domain']
                assert r['original_semantics'].endswith('#/templates/' + r['domain'])
            elif part == 'records_b':
                assert bind['id'] == r['id'] and r['finite_unresolved'] == []
                assert r['literal_binding']['binding_row'] == i
                assert r['complete_meaning_template'] == r['domain']
            else:
                assert read['physical_lines'] == u['lines'] and read['two_field_sha256'] == u['key_sha256']
                assert r['record_ref'] == 'reading-ledger.json#/records/' + str(i)
                assert r['read_witness'] == read['witness'] and r['decision'] == 'FINITE_CHECKED'
            accepted.append({'id': r['id'], 'domain': domain, 'reader_context': contexts[part], 'part': part,
                             'reader_record': i, 'parent_literal_reread': False,
                             'reception': 'RECEIVED_FINITE_RECORD_SEMANTICS_FROM_NAMED_NONAUTHOR_READER',
                             'interfaces_final': False})
        receipts.append({'part': part, 'commit': manifest['commit'], 'checkout_tree': manifest['checkout_tree'],
                         'task_tree': manifest['task_tree'], 'files_retrieved_and_bound': len(manifest['files']),
                         'records': len(rec), 'fields': 2 * len(rec), 'reader_context': contexts[part],
                         'semantic_material_actually_received': ['complete original templates/fact groups', 'complete worker semantics/profiles',
                             'necessary finite definitions', 'finite vectors', 'reverse clauses', 'withdrawal/counters', 'report and ledger business fields'],
                         'mechanical_checks': 'all IDs/order/literals/source positions/original semantic fields/fact groups match fixed inputs',
                         'excluded': 'No worker scripts executed; no duplicate literal reading; no parent/global final signature transferred'})
    assert len({r['id'] for r in accepted}) == len(accepted) == 5437
    save('continuation/received-parts/parent-acceptance.json', {
        'schema': 'gr8-elr-parent-part-reception/v1', 'actual_context': '01a14465-d18e-725b-b69c-2e6f52300005',
        'receipts': receipts, 'records': accepted, 'received_pairs': len(accepted), 'received_fields': len(accepted) * 2,
        'new_proposals': 0, 'new_independent_required_votes': 0,
        'worker_proposal_qualification': 'A double-directory prefix suspicion withdrawn before proposal; no formal required finding.',
        'C_identity_qualification': 'Actual independent dispatch context supplied by coordinator; worker authoritative self UUID remains UNVERIFIED. No added vote.',
        'C_topic_notes': 'Secondary nonauthoritative locator glosses not adopted as independent business assertions; exact full values remain original reader credit.',
        'parent_seven_interfaces_complete': False, 'root_final_signed': False,
        'semantic_credit_from_mechanical_checks': 0, 'behavior_execution': 'NOT_EXECUTED', 'UPDATE_NOT_STARTED': True})
    return receipts

def receive_recovery_d():
    """Receive only the new D evidence; reuse the already accepted A/B/C receipt."""
    part = 'records_d_recovery'
    prefix = 'continuation/received-parts/' + part + '/'
    manifest = load(prefix + 'parent-retrieval-identity.json')
    assert manifest['commit'] == '477fb3ce438fe5462ee6901908cccc59977d4ba1'
    for f in manifest['files']:
        b = (T / f['local']).read_bytes()
        assert len(b) == f['bytes'] and sha(b) == f['sha256']
        assert git('show', manifest['commit'] + ':' + f['path']) == b
    assert len(manifest['files']) == 8 and sum(f['bytes'] for f in manifest['files']) == 696469
    source_prefix = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/recovery_elr_d/'
    changed = [p.decode() for p in git('diff-tree','--no-commit-id','--name-only','-r','-z',
        'd14a4bf68776ac7aacf54065c28ed982a054c8a8',manifest['commit']).split(b'\0') if p]
    assert len(changed) == 8 and all(p.startswith(source_prefix) for p in changed)
    identity_checks = load(prefix + 'input-identity.json')['checks']
    for item in identity_checks:
        ref = item['commit'] == '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
        data = git('show', item['commit'] + ':' + item['path'], reference=ref)
        desc = git('ls-tree',item['commit'],'--',item['path'],reference=ref).decode().split('\t')[0].split()
        assert len(data) == item['bytes'] and sha(data) == item['sha256']
        assert desc[0] == item['mode'] and desc[2] == item['blob']
    frozen = load('continuation/contracts/readsets/records_d.complete.json')
    supplied = load(prefix + 'frozen-denominator.json')
    assert supplied['record_ids'] == frozen['record_ids'] and supplied['ordered_runs'] == frozen['ordered_runs']
    assert supplied['count'] == 4827 and supplied['fields'] == 9654
    context = supplied['context']['actual_platform_context_id']
    assert context == '01a144fc-df1d-7133-97ce-5d218016402d'
    assert context not in supplied['context']['author_contexts_excluded']
    rec = load(prefix + 'reception-ledger.json')
    reading = load(prefix + 'reading-ledger.json')
    assert reading['literal_read'] == rec['received_pairs'] == 4827 and reading['unread'] == rec['unread'] == 0
    rows = rec['rows']; batches = reading['batches']
    assert [r[0] for r in rows] == frozen['record_ids'] and len(batches) == 14
    previous = 0
    for batch in batches:
        first,last = batch['ordinal_range']
        assert first == previous + 1 and rows[first-1][0] == batch['first'] and rows[last-1][0] == batch['last']
        assert rows[first-1][1] == batch['view_lines'][0] and rows[last-1][1] == batch['view_lines'][1]
        assert batch['credit'] == 'complete displayed literals actually read; each equals both raw fields'
        previous = last
    assert previous == 4827
    index = load('continuation/contracts/readsets/records_d.identity-only-index.json')['rows']
    semantics = load('continuation/contracts/readsets/records_d.original-semantic-fields.json')
    original = load('evidence/recovered-target/reading-ledger.json')
    units = {u['id']:u for u in original['units']}
    forward = load('evidence/recovered-target/forward-mapping.json')
    fm = {u['unit']:u for u in forward['records']}
    groups = {g['domain']:g for g in forward['fact_groups']}
    for fact in semantics['fact_groups']: assert fact == groups[fact['domain']]
    view = (T/'continuation/contracts/views/records_d.records.view.txt').read_text().splitlines()
    pure = {'id','identity','lines','record','key_sha256','translation_sha256'}
    raw = {d:(T/'evidence/primary-reference'/(d+'.txt')).read_text(encoding='utf-8-sig').splitlines() for d in rec['domain_contracts']}
    old = load('continuation/received-parts/parent-acceptance.json')
    accepted = [r for r in old['records'] if r['part'] != part]
    assert len(accepted) == 5437
    own_ids = {r['id'] for r in load('reading-ledger.json')['literal_record_reads']}
    assert not own_ids & set(frozen['record_ids']) and not {r['id'] for r in accepted} & set(frozen['record_ids'])
    for i,(row,ident) in enumerate(zip(rows,index)):
        rid,line,physical,index_n,batch_n,domain,disposition = row
        u = units[rid]; n = u['record']
        assert {k:u[k] for k in pure} == ident and index_n == i+1 and physical == u['lines']
        assert domain in rec['domain_contracts'] and rid == 'ELR-'+domain+'-'+str(n).zfill(4)
        assert 1 <= batch_n <= 14 and disposition == 'RECEIVED_LOCALIZATION_DATA'
        first,last = batches[batch_n-1]['ordinal_range']; assert first <= i+1 <= last
        marker,literal = view[line-1].split(' = ',1)
        value = json.loads(literal)
        assert marker == 'R'+str(n) and value == raw[domain][2*n+2] == raw[domain][2*n+3]
        assert sha(value.encode()) == u['key_sha256'] == u['translation_sha256']
        assert {k:v for k,v in u.items() if k not in pure} == semantics['templates'][domain]['complete_original_unit_semantic_fields']
        assert {k:v for k,v in fm[rid].items() if k!='unit'} == semantics['templates'][domain]['complete_original_forward_fields']
        accepted.append({'id':rid,'domain':domain,'reader_context':context,'part':part,'reader_record':i,
            'reader_batch':batch_n,'parent_literal_reread':False,
            'reception':'RECEIVED_FINITE_RECORD_SEMANTICS_FROM_NAMED_NONAUTHOR_READER','interfaces_final':False})
    assert len(accepted) == len({r['id'] for r in accepted}) == 10264
    assert own_ids | {r['id'] for r in accepted} == {u['id'] for u in original['units'] if 'record' in u}
    receipts = [r for r in old['receipts'] if r['part'] != part]
    receipt = {'part':part,'logical_part':'records_d','commit':manifest['commit'],'checkout_tree':manifest['checkout_tree'],
        'task_tree':manifest['task_tree'],'files_retrieved_and_bound':8,'bytes':696469,'records':4827,'fields':9654,
        'reader_context':context,'source_prefix':source_prefix,'actual_write_scope_only_new_eight_paths':True,
        'semantic_material_actually_received':['complete report common/four-domain meanings','all14 actual reading batches and failure qualifications',
            'all12 necessary-definition receipts plus parent completion correction','complete finite vectors and strongest no-required/reverse clauses',
            'all four original full semantic templates/fact groups','all domain contracts and row dispositions','interfaces/proposal/identity/publication qualifications'],
        'parent_literal_reread':False,'generation_reading_credit':0,
        'definition_extent_correction':{'source':'Compiler_CompilePBS.rb','D_ledger_range':[1,64],
            'complete_generic_method':[4,68],'completion_reader':'01a14465-d18e-725b-b69c-2e6f52300005',
            'prior_actual_reading':'continuation/reading-and-reception.addendum.json source range1–108; not retroactive D credit'},
        'excluded':'No global/root final signature, no source behavior execution or independent ELR001 vote'}
    receipts.append(receipt)
    old.update(records=accepted,receipts=receipts,received_pairs=10264,received_fields=20528,
        parent_seven_interfaces_complete=False,root_final_signed=False,
        D_recovery_qualification='One logical D scope; new recovery actual reader replaces unreceived original D. Later original results dedup by exact stable ID; conflicting ID freezes for root, no extra denominator/vote.')
    save('continuation/received-parts/parent-acceptance.json',old)
    save('continuation/received-parts/recovery-D-validation.json',{'receipt':receipt,'input_identity_checks':len(identity_checks),
        'record_id_order_exact':True,'batch_contiguous_records':4827,'all_literal_view_raw_key_value_bindings_exact':True,
        'original_unit_forward_fact_fields_exact':True,'union_parent433_named10264_exact10697':True,
        'A_B_C_unchanged_receipts_reused':True,'semantic_credit_from_tool':0,'behavior_execution':'NOT_EXECUTED'})
    return receipt

def pbs():
    packet = load('evidence/pbs-current/localization-field-contribution.v1.json')
    sources = load('continuation/pbs-field-binding/sources-and-order.json')
    rows = load('continuation/pbs-field-binding/raw-required-fields-and-positions.json')
    bypath = {p['path']: [r for r in rows if r['path_index'] == p['index']] for p in sources}
    checked = []
    for p in packet['own_six_paths']:
        family = packet['family_contracts'][p['family']]
        fields = family['field_order']
        rawrows = bypath[p['path']]
        assert len(rawrows) == len(p['records'])
        for ordinal, (source, r) in enumerate(zip(rawrows, p['records']), 1):
            assert ordinal == r[0] and source['header'] == r[1]
            assert [source['fields'].get(f) for f in fields] == r[4]
            assert r[2][0] <= source['start'] <= r[2][1]
            for value in source['fields'].values(): assert r[2][0] <= value[0] <= r[2][1]
            if p['family'] == 'species' and 'forms' in p['path']:
                name, number = r[1].split(',')
                assert r[3] == [name, int(number)]
            elif p['family'] == 'species':
                assert r[3] == [r[1], 0]
            else:
                assert r[3] == r[1]
            for f, ref in zip(fields, r[5]):
                actual = source['fields'].get(f)
                is_form = p['family'] == 'species' and 'forms' in p['path']
                if is_form and (f == 'Name' or (actual is None and f in ['Category','Pokedex'])):
                    expected_ref = ['BASE', r[3][0], f]
                elif actual is not None:
                    expected_ref = ['RAW', fields.index(f)]
                else:
                    expected_ref = ['DEFAULT', family['base_missing'][fields.index(f)]]
                assert ref == expected_ref
                if ref[0] == 'RAW': assert ref[1] == fields.index(f) and actual is not None
                elif ref[0] == 'DEFAULT':
                    assert actual is None and ref[1] == family['base_missing'][fields.index(f)]
                elif ref[0] == 'BASE':
                    assert p['family'] == 'species' and 'forms' in p['path'] and actual is None
                    assert ref[1] == r[3][0] and ref[2] == f
                    base = next(b for b in bypath['PBS/pokemon.txt'] if b['header'] == ref[1])
                    assert f in base['fields'] or f in fields
                else: raise AssertionError(ref)
        checked.append({'path': p['path'], 'records': len(rawrows), 'raw_fields_positions_and_effective_references_match': True})
    for p in packet['additional_two_complete_prior_receptions']:
        rawrows = bypath[p['path']]
        assert len(rawrows) == len(p['records'])
        for ordinal, (source, r) in enumerate(zip(rawrows, p['records']), 1):
            assert ordinal == r[0] and source['header'] == r[1]
            assert [source['fields'][f][1] for f in ['Name', 'Description']] == r[3]
            assert r[2][0] <= source['start'] <= r[2][1]
            assert all(r[2][0] <= source['fields'][f][0] <= r[2][1] for f in ['Name','Description'])
        checked.append({'path': p['path'], 'records': len(rawrows), 'all_name_description_values_match': True})
    save('continuation/pbs-field-binding/provider-comparison.json', {
        'scope': 'Eight provided finite localization projections; remaining27 receive only own required-field projection, not full PBS records.',
        'paths': checked, 'provided_records': sum(p['records'] for p in checked),
        'all_35_raw_field_projection_records': len(rows), 'whole_PBS_records_read': False,
        'corpus_dictionary_references': 'Exact string aliases only; runtime domains determined by family/field/producer. C/D literal reader receipt still pending.',
        'generation_semantic_credit': 0, 'source_behavior_execution': 'NOT_EXECUTED'})
    return checked

def compact(data, pos):
    n = data[pos]; pos += 1
    n = n if n < 128 else n - 256
    if n == 0: return 0, pos
    if n > 4: return n - 5, pos
    if n < -4: return n + 5, pos
    count = abs(n)
    v = int.from_bytes(data[pos:pos + count], 'little', signed=False)
    if n < 0: v -= 1 << (count * 8)
    return v, pos + count

def links_and_reverse():
    packet = load('continuation/received/objectlinks.json')
    b = git('show', '8c5911e:' + packet['source']['path'], reference=True)
    assert len(b) == packet['source']['bytes'] and sha(b) == packet['source']['sha256']
    for n, r in enumerate(packet['links']):
        a, z = r['source_span']; ta, tz = r['target_span']
        assert n == r['link'] and b[a:z].hex() == r['original_hex'] and b[a] == 64
        index, end = compact(b, a + 1)
        assert index == r['target_object'] and end == z and ta < a
        assert r['target_type'] == '"' and b[ta] == 34
        size, start = compact(b, ta + 1)
        assert start + size == tz and b[start:tz].decode('utf-8') == r['entire_target_text']
    reverse = load('evidence/recovered-target/reverse-mapping.json')
    formal = (T / 'evidence/necessary-source/F-wp08-localization.md').read_text().splitlines()
    groups = collections.defaultdict(list)
    sub = 0
    for row in reverse['wp08_clause_records']:
        assert row['text'] == formal[row['lines'][0] - 1].strip()
        for atom in row['subassertions']:
            assert atom['assertion'] in row['text'] or atom['assertion'] in row['text'].replace('**', '')
            sub += 1
        k = row['status']
        groups[k].append(row['id'])
    save('continuation/links-and-reverse-validation.json', {
        'messages_source': packet['source'], 'object_links': len(packet['links']),
        'link_checks': ['all exact source bytes match', 'compact integer target indices match', 'all targets earlier string spans',
                        'all 178 complete target texts match raw bytes'],
        'object_links_actual_read': 'All178 text rows c0522a; envelopes9900cc. No Marshal.load or recovered parser execution.',
        'reverse125': {'clauses': len(reverse['wp08_clause_records']), 'subassertions': sub, 'lossless_status_groups': dict(groups),
                       'actual_read_chunks': ['cbe51e', 'e2c3f3', '10aaf8'],
                       'qualification': 'Each complete clause and its finite premises received; contains no whole test-catalogue or entire-system acceptance.'},
        'semantic_credit_from_tool': 0, 'behavior_execution': 'NOT_EXECUTED', 'UPDATE_NOT_STARTED': True})
    return len(packet['links']), len(reverse['wp08_clause_records']), sub

if __name__ == '__main__':
    if sys.argv[1:] == ['--receive-recovery-D']:
        result = {'recovery_D':receive_recovery_d()}
    else:
        result = {'parts':load('continuation/received-parts/parent-acceptance.json')['receipts'], 'pbs': pbs(), 'links_reverse': links_and_reverse()}
    print(json.dumps(result, ensure_ascii=False, indent=2))
