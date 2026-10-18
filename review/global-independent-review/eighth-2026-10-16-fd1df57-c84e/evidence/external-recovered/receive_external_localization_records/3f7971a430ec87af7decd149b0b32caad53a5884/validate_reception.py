"""Check the finite handoff's identities/arithmetic; never execute reference behavior."""
from pathlib import Path
from collections import Counter
import datetime
import hashlib
import json
import subprocess

T = Path(__file__).resolve().parent
ROOT = T.parents[4]
PREFIX = str(T.relative_to(ROOT)) + '/'
READY = 'READY_FOR_ROOT_TASK_FINAL_ACCEPTANCE'
def read(name): return json.loads((T/name).read_text())
def sha(data): return hashlib.sha256(data).hexdigest()
def paths(*args):
    return [p.decode() for p in subprocess.check_output(['git',*args,'-z'],cwd=ROOT).split(b'\0') if p]

def main():
    f=read('frozen-denominator.json'); r=read('reading-ledger.json')
    q=read('reception-ledger.json'); i=read('interfaces.json'); p=read('proposal-counters.json')
    assert q['status']==r['status']==i['status']==READY and q['full_task_final_ready']
    assert q['root_final_signed'] is False and p['root_task_final_signed'] is False
    assert r['independence']['different'] and p['actual_receiver_differs_from_author']
    assert r['actual_context']!=r['original_author_context']
    assert r['independence']['self_spawn']==0 and p['counts']['self_spawn_contexts']==0
    assert len(f['primary_objects'])==10715
    assert sum(x['literal_read_here'] for x in f['primary_objects'])==442
    own=r['literal_record_reads']; own_ids={x['id'] for x in own}
    assert len(own)==len(own_ids)==433 and r['counts']['literal_fields_read']==866
    named=read('continuation/received-parts/parent-acceptance.json')
    named_ids={x['id'] for x in named['records']}
    assert len(named_ids)==len(named['records'])==10264 and not own_ids&named_ids
    all_ids={x['id'] for x in f['primary_objects'] if x['kind']=='record'}
    assert own_ids|named_ids==all_ids and len(all_ids)==10697
    assert Counter(x['part'] for x in named['records'])=={'records_a':2756,'records_b':1620,'records_c':1061,'records_d_recovery':4827}
    assert len(named['receipts'])==4 and all(x['interfaces_final'] for x in named['records'])
    assert all(x['parent_literal_reread'] is False for x in named['records'])
    assert len({x['reader_context'] for x in named['receipts']})==4
    assert all(x['reader_context']!=r['original_author_context'] for x in named['receipts'])
    assert named['received_fields']==20528 and named['distinct_primary_fields_with_parent']==21394
    assert not named['remaining_necessary_record_ids'] and named['root_final_signed'] is False
    d=read('continuation/received-parts/recovery-D-validation.json')
    assert d['record_id_order_exact'] and d['batch_contiguous_records']==4827
    assert d['all_literal_view_raw_key_value_bindings_exact'] and d['original_unit_forward_fact_fields_exact']
    assert d['union_parent433_named10264_exact10697'] and d['A_B_C_unchanged_receipts_reused']
    assert d['receipt']['actual_write_scope_only_new_eight_paths']
    assert d['receipt']['definition_extent_correction']['complete_generic_method']==[4,68]
    assert r['counts']['primary_distinct_pairs_actually_read_or_received']==10697
    assert r['counts']['primary_distinct_fields_actually_read_or_received']==21394
    assert r['counts']['primary_files_with_complete_literal_reader_coverage']==18
    assert r['counts']['primary_pairs_still_unreceived']==0
    assert r['counts']['headers_read']==9 and r['counts']['headers_read_or_received']==18
    assert len([x for x in f['primary_objects'] if x['kind']=='header'])==18
    assert all(x['full_chain_reception'].startswith('COMPLETE') for x in f['primary_objects'])
    assert q['necessary_unread']==q['necessary_unreceived']==0
    assert not any(q['remaining_exact_objects'].values())
    assert len(f['image_methods'])==len(q['image_callers'])==36
    assert sum(len(x['matched_lines']) for x in f['image_methods'])==63
    assert len(f['pbs35'])==35 and len(f['fact_groups'])==18
    assert len(i['interfaces'])==i['complete']==7 and i['partial']==i['not_received']==0
    assert all(x['receiver_finite_reception_complete'] and not x['necessary_unreceived'] and not x['full_final_acceptance'] and not x['root_final_signed'] for x in i['interfaces'])
    assert all((T/e.split('#')[0]).is_file() for x in i['interfaces'] for e in x['evidence'])
    assert len(f['reverse125'])==125 and sum(x['subassertion_count'] for x in f['reverse125'])==398
    assert len(f['tests41'])==41
    links=read('continuation/links-and-reverse-validation.json')
    assert links['object_links']==178 and links['reverse125']['clauses']==125 and links['reverse125']['subassertions']==398
    assert links['behavior_execution']=='NOT_EXECUTED'
    pbs=read('continuation/pbs-field-binding/actual-reader-bindings.json')
    assert len(pbs['rows'])==11647 and pbs['empty_s_fields']==[]
    assert pbs['counts']=={'new_literal_occurrences':150,'absent':3330,'corpus_literals_resolved':8167}
    assert not any(x['status'].startswith('PENDING') for x in pbs['rows'])
    assert pbs['generation_reading_credit']==0 and q['pbs_literal_reader_binding']['corpus_literal_slots_pending_D']==0
    provider=read('continuation/pbs-field-binding/provider-comparison.json')
    assert provider['provided_records']==2339 and provider['all_35_raw_field_projection_records']==13051
    assert provider['whole_PBS_records_read'] is False
    generation=read('continuation/pbs-field-binding/generation.json')
    assert generation['raw_literal_matching_is_reading'] is False and generation['source_FULL'] is False
    assert generation['warnings']==0 and generation['unique_necessary_records']==3324
    purpose=read('continuation/target-payload-purpose.json')
    assert len(purpose['entries'])==213 and not any(x.get('necessary_pending_reader_ids') for x in purpose['entries'])
    assert {x['path'] for x in purpose['entries']}=={x['path'] for x in r['target_file_states']}
    views=read('continuation/target-view-reuse.json')
    assert len(views['source_views'])==105 and len(views['corpus_views'])==38
    assert all(not x['pending_reader_ids'] and x['all_raw_fields_exact'] and x['headers_exact'] for x in views['corpus_views'])
    assert {v for x in views['corpus_views'] for v in x['record_ids']}==all_ids
    count=total=0
    for row in read('evidence/target-recovery.json')['files']:
        data=(T/row['local_path']).read_bytes()
        assert len(data)==row['bytes'] and sha(data)==row['sha256']
        count+=1; total+=len(data)
    assert count==213 and total==18637972
    originals=T/'evidence/recovered-target/evidence/contracts'
    for name in ['AGENTS.md','eighth-global-review-prompt.md','review-SKILL.md']:
        assert (originals/name).read_bytes()==(T/'evidence/contract'/name).read_bytes()
    corpus={p.stem:p.read_text(encoding='utf-8-sig').splitlines() for p in (T/'evidence/primary-reference').glob('*.txt')}
    assert len(corpus)==18 and sum((len(v)-4)//2 for v in corpus.values())==10697
    for x in own:
        n=x['record']; assert [x['raw_key'],x['raw_value']]==corpus[x['domain']][2*n+2:2*n+4]
    source_rows=read('continuation/direct-source-reception-2.json')['rows']
    for row in source_rows:
        data=(T/row['local_path']).read_bytes()
        assert len(data)==row['bytes'] and sha(data)==row['sha256']
        assert all(1<=a<=b<=len(data.decode('utf-8-sig').splitlines()) for a,b in row['actual_read_ranges'])
    assert p['counts']['new_required_roots']==p['counts']['new_optional']==p['counts']['new_policy']==p['counts']['new_no_required']==p['counts']['new_votes']==0
    assert p['business_execution']=='NOT_EXECUTED' and p['UPDATE_NOT_STARTED']
    changed=set(paths('diff','--name-only','40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'))
    staged=set(paths('diff','--cached','--name-only'))
    untracked=set(paths('ls-files','--others','--exclude-standard'))
    assert all(x.startswith(PREFIX) for x in changed|staged|untracked), sorted((changed|staged|untracked)-{x for x in changed|staged|untracked if x.startswith(PREFIX)})
    json_count=0
    for path in T.rglob('*.json'):
        json.loads(path.read_text()); json_count+=1
    out={'schema':'gr8-elr-mechanical-package-validation/v3','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'result':'PASS_MECHANICAL_ONLY','source_semantic_credit':0,'business_execution':'NOT_EXECUTED',
        'task_status':READY,'target_identity_files':213,'target_identity_bytes':18637972,
        'parent_personal_literal_records':433,'parent_personal_literal_fields':866,'personal_headers':9,
        'named_reader_records_received':10264,'named_reader_fields_received':20528,'logical_reader_groups':4,
        'distinct_pairs_read_or_received':10697,'distinct_fields_read_or_received':21394,'headers_read_or_received':18,
        'records_still_unreceived':0,'PBS_necessary_slots':11647,'PBS_slot_split':[8167,150,3330],'PBS_pending_slots':0,
        'complete_image_methods':36,'image_calls':63,'source_views_bound':105,'corpus_views_bound':38,
        'reverse_clauses':125,'reverse_subassertions':398,'objectlinks':178,
        'finite_interfaces_complete':7,'root_global_final_signed':False,'new_required_roots':0,'new_independent_votes':0,
        'all_changed_staged_untracked_in_write_set':True,'JSON_files_parsed':json_count,'UPDATE_NOT_STARTED':True}
    (T/'evidence/package-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False))
if __name__=='__main__': main()
