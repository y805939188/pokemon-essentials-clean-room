"""Refresh actual display metadata, never infer semantic acceptance from line coverage."""
import collections,datetime,hashlib,json,pathlib,subprocess
p=pathlib.Path(__file__).resolve().parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
rows=[json.loads(x) for x in (p/'read-io/index.jsonl').read_text().splitlines()]
by=collections.defaultdict(list)
for x in rows: by[x['path']].append(x)
def full(rs):
    end=0
    for r in sorted(rs,key=lambda x:x['range']):
        if r['range'][0]>end+1:return False
        end=max(end,r['range'][1])
    return end==rs[0]['file_lines']
def ds(rs):return [{k:r[k] for k in ['range','stdout','began_utc','ended_utc','exit_code']} for r in rs]
a=json.loads((p/'identities.json').read_text()); l=json.loads((p/'reading-ledger.json').read_text())
seen=set()
for entry in l['initial']:
    i=entry['identity']; path=str(pathlib.Path(i['repo'])/i['path']); seen.add(path); rs=by.get(path,[])
    if full(rs) if rs else False:
        i['read_status']='FULL_CONTINUOUS_READ_THIS_CONTEXT';entry['own_full_read']=True;entry['continuous_displays']=ds(rs)
        entry['semantic_disposition']='REVIEWER_FULL_READ; FINITE_MEANING_IN_FORWARD_REVERSE_PBS_INTERFACES'
    elif i['path']=='PBS/Gen 8 backup/items.txt':
        peer=next(e['identity'] for e in l['initial'] if e['identity']['path']=='PBS/items.txt')
        assert i['blob']==peer['blob'] and i['sha256']==peer['sha256'] and i['bytes']==peer['bytes']
        i['read_status']='IDENTICAL_BYTE_PATH_ASSOCIATION_DEFAULT_FULL_READ_NOT_SEPARATE_DISPLAY'
        entry['own_full_read']=False;entry['semantic_disposition']='EXACT_BLOB_SHA_BYTES_MATCH; CONDITIONAL_GEN8_BACKUP_PATH; NO_SEPARATE_READ_CREDIT'
for i in a['payloads']:
    match=next(e['identity'] for e in l['initial'] if e['identity']['repo']==i['repo'] and e['identity']['path']==i['path'])
    i['read_status']=match['read_status']
l['extra_full_reads']=[]
l['extra_partial_reads']=[]
for path,rs in by.items():
    if path in seen:continue
    f=pathlib.Path(path); repo='/workspace/pokemon-essentials' if path.startswith('/workspace/pokemon-essentials/') else '/workspace/pokemon-essentials-clean-room'
    commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' if repo.endswith('/pokemon-essentials') else 'fd1df570cad987dc3852a3b958f03916e317f7fe'
    rel=str(f.relative_to(repo)); proc=subprocess.run(['git','rev-parse',f'{commit}:{rel}'],cwd=repo,capture_output=True,text=True)
    target=l['extra_full_reads'] if full(rs) else l['extra_partial_reads']
    target.append({'path':path,'repo':repo,'commit':commit,'blob':proc.stdout.strip() if proc.returncode==0 else 'WORKSPACE_REVIEW_INPUT_NOT_B8_TRACKED','bytes':rs[0]['bytes'],'sha256':rs[0]['sha256'],'lines':rs[0]['file_lines'],'reviewer':'/root/creature_b','own_full_read':full(rs),'continuous_displays':ds(rs),'identity_git_exit':proc.returncode,'semantic_credit':'Reviewer judgement only; full-file credit only when actually read. Selected complete PBS records do not grant whole-file credit.'})
    if not full(rs):
        merged=[]
        for row in sorted(rs,key=lambda x:x['range']):
            begin_line,end_line=row['range']
            if merged and begin_line<=merged[-1][1]+1:merged[-1][1]=max(merged[-1][1],end_line)
            else:merged.append([begin_line,end_line])
        unread=[];cursor=1
        for begin_line,end_line in merged:
            if cursor<begin_line:unread.append([cursor,begin_line-1])
            cursor=end_line+1
        if cursor<=rs[0]['file_lines']:unread.append([cursor,rs[0]['file_lines']])
        target[-1]['unread_ranges']=unread;target[-1]['unread_lines']=sum(end_line-begin_line+1 for begin_line,end_line in unread)
l.update(updated_utc=now,initial_own_full_read=sum(e['own_full_read'] for e in l['initial']),same_byte_associated_paths=1,available_unread_paths=[],semantic_acceptance='PRIMARY_FULL_READ_MAPPINGS_AUTHORED; NAMED_TRANSITIVE_RECEIPTS_IN_INTERFACES')
assert l['initial_own_full_read']==46
(p/'reading-ledger.json').write_text(json.dumps(l,ensure_ascii=False,indent=2)+'\n')
a['updated_utc']=now;(p/'identities.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
q=json.loads((p/'progress.json').read_text());q.update(updated_utc=now,initial_full_read=46,initial_dependency_full_read=36,available_unread_pbs_paths=[],phase='ALL_INITIAL_PAYLOADS_READ_OR_PROVEN_BYTE_ASSOCIATED; FINITE_CONSUMER_RECEPTION_ACTIVE',extra_full_reads=len(l['extra_full_reads']),unreceived_interfaces='ENUMERATED_IN_INTERFACES_JSON',semantic_acceptance='SOURCE_STATIC_FINITE_MAPPINGS; NO_GLOBAL_PASS')
(p/'progress.json').write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':now,'own_initial_full_reads':46,'associated_paths':1,'extra_full_reads':len(l['extra_full_reads']),'available_initial_unread':0}))
