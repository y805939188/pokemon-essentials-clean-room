"""Apply explicitly reviewed continuation records, preserving all prior receipts."""
from pathlib import Path
import datetime,hashlib,json,subprocess
T=Path(__file__).resolve().parent
def read(p):return json.loads((T/p).read_text())
def save(p,v):(T/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def main():
    delta=read('additional-receptions.json');r=read('reception-ledger.json');have={x['id'] for x in r['fully_received_records']}
    r['fully_received_records'] += [x for x in delta['canonical_records'] if x['id'] not in have]
    have={x['id'] for x in r['fully_received_records']};r['necessary_unreceived_records']=[x for x in r['necessary_unreceived_records'] if x['id'] not in have]
    for row in r['original_nonmandatory']:
        for x in delta['legacy_records']:
            if row['kind']==x['kind'] and row['index']==x['index']:row.update(x)
    for row in r['purpose_payloads']:
        for f,scopes in delta['additional_purpose_scopes'].items():
            if row['file_index']==int(f):
                row['status']='PARTIAL' if row['status']=='OPEN_UNREAD' else row['status']
                row['actual_scopes']=list(dict.fromkeys(row['actual_scopes']+scopes))
    r['continued_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();save('reception-ledger.json',r)
    state=read('view-state.json');n=len(have);l=read('reading-ledger.json');l.update(exact_display_and_acknowledgments=state['acks'],canonical_groups_read=n*7,canonical_groups_remaining=(37-n)*7,canonical_records_complete=n,canonical_records_unreceived=37-n,original_proposal_and_counter_complete=n,C13_complete_group_aliases=n,original_nonmandatory_complete=sum(x['status'].startswith('RECEIVED') for x in r['original_nonmandatory']),original_nonmandatory_remaining=sum(x['status'].startswith('OPEN') for x in r['original_nonmandatory']),continued_utc=r['continued_utc'],additional_receipt='additional-receptions.json',new_behavior_runs=0);save('reading-ledger.json',l)
    f=read('frozen-denominator.json');f['canonical_received_ids']=[x['id'] for x in r['fully_received_records']];f['canonical_unreceived_ids']=[x['id'] for x in r['necessary_unreceived_records']];f['original_nonmandatory_objects']=r['original_nonmandatory'];f['continued_utc']=r['continued_utc'];save('frozen-denominator.json',f)
    p=read('progress.json');p.update(canonical_received=n,canonical_remaining=37-n,legacy_received=l['original_nonmandatory_complete'],legacy_remaining=l['original_nonmandatory_remaining'],continued_utc=r['continued_utc'],parent_parallel_contract='continuation-v2/manifest.json',parent_parallel_contract_commit='64cfde5aa3f6b25adc7291b2c2e880d87baf1ebd');save('progress.json',p)
    it=read('interfaces.json');ids={x['id'] for x in it['records']};it['records'] += [x for x in delta['interfaces'] if x['id'] not in ids];it['other_interfaces']='33 remaining canonical producer bodies and unreceived purpose interfaces remain OPEN in exact ledgers; no locator signoff.';save('interfaces.json',it)
    src=read('source-readings.json');seen={(x['commit'],x['path'],json.dumps(x['actual_read_ranges'])) for x in src['records']}
    for item in delta['source_readings']:
        repo=Path(item['repository']);b=subprocess.check_output(['git','-C',str(repo),'show',item['commit']+':'+item['path']]);assert b==(repo/item['path']).read_bytes();lines=b.splitlines(keepends=True);ranges=item['actual_read_ranges'] or [[1,len(lines)]];key=(item['commit'],item['path'],json.dumps(ranges))
        if key in seen:continue
        assert all(1<=a<=z<=len(lines) for a,z in ranges)
        src['records'].append(item|identity(b)|{'line_count':len(lines),'mode':'100644','actual_read_ranges':ranges,'full_file_read':ranges==[[1,len(lines)]],'range_identities':[{'range':x,**identity(b''.join(lines[x[0]-1:x[1]]))} for x in ranges],'recorded_after_read_utc':r['continued_utc'],'behavior':'NOT_EXECUTED','evidence':'Exact actual tool output in this context; immutable Git blob/ranges reproduce input.'});seen.add(key)
    src['continued_utc']=r['continued_utc'];save('source-readings.json',src)
    units=read('remaining-objects.exact.json');
    for u in units['objects']:u['fully_received']=u['id'] in have
    save('remaining-objects.exact.json',units)
    c=json.loads((T/'.work/originals/0').read_text());ch=json.loads((T/'.work/originals/15').read_text());eq=[]
    for i,x in enumerate(c['records']):
        if x['id'] in have:
            assert x['groups']==ch['records'][i]['groups'];eq.append({'id':x['id'],'full_groups_equal':True,'canonical_group_sha256':hashlib.sha256(json.dumps(x['groups'],sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest(),'C13_pointer':f'/records/{i}/groups','credit':'EXACT_ALIAS_TO_THIS_RECEIVER_COMPLETE_GROUP_READ'})
    save('c13-groups-equality.json',eq)
    print(json.dumps({'canonical_complete':n,'canonical_remaining':37-n,'legacy_complete':l['original_nonmandatory_complete'],'legacy_remaining':l['original_nonmandatory_remaining'],'status':'INCOMPLETE','UPDATE_NOT_STARTED':True},ensure_ascii=False))
if __name__=='__main__':main()
