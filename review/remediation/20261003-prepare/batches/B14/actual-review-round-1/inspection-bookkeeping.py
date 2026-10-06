"""New read-only document bookkeeping. Never executes inspected programs."""
import sys, json, subprocess, hashlib, pathlib, datetime
OUT = pathlib.Path(__file__).parent
ACT = 'd48197f365c39925f795c1d325988c0d74e59979'
ORIG = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
OP = 'review/global-independent-review/2026-10-03-fd82a639/findings.json'
AP = 'review/remediation-20261003-prepare/finding-acceptance.json'
BASE = 'review/remediation/20261003-prepare/batches/B14/'
def git(args, repo=None):
    return subprocess.check_output(['git'] + (['-C', repo] if repo else []) + args)
def get(c, p, repo=None):
    return git(['show', c + ':' + p], repo)
def journal(rec):
    rec['recorded_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with (OUT / 'display-events.jsonl').open('a') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
def display(c, p, start, end, repo=None):
    b = get(c, p, repo)
    lines = b.decode().splitlines(keepends=True)
    for n in range(start, min(end, len(lines)) + 1):
        print(str(n) + ': ' + lines[n-1], end='' if lines[n-1].endswith('\n') else '\n')
    journal({'kind':'literal_lines_displayed', 'repository':'reference' if repo else 'project', 'commit':c,'path':p,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'total_lines':len(lines),'start':start,'end':min(end,len(lines)),'semantic_credit':'Only untruncated output actually inspected; final reading log states limits'})
def controls():
    ids = json.loads(get(ACT,BASE+'candidate-1/contributions.json'))
    ids = [r['id'] for r in ids['contributions']]
    originals = json.loads(get(ORIG,OP)); accepted = json.loads(get(PLAN,AP))
    seen = {}; locs = {}; seq = []
    def render(x, path, binding):
        if isinstance(x, dict):
            return '{'+','.join(json.dumps(k,ensure_ascii=False)+':'+render(v,path+'/'+k.replace('~','~0').replace('/','~1'),binding) for k,v in x.items())+'}'
        if isinstance(x,list):
            return '['+','.join(render(v,path+'/'+str(i),binding) for i,v in enumerate(x))+']'
        raw=json.dumps(x,ensure_ascii=False,separators=(',',':'))
        if isinstance(x,str) and len(x)>80:
            if raw in seen:
                key=seen[raw]; locs[key]['occurrences'].append({'binding':binding,'selector':path});return '{"exact_value_reuse":"'+key+'"}'
            key='V'+str(len(seen)+1);seen[raw]=key
            locs[key]={'sha256':hashlib.sha256(raw.encode()).hexdigest(),'first_binding':binding,'first_selector':path,'occurrences':[{'binding':binding,'selector':path}]}
            return '{"first_exact_value":"'+key+'","value":'+raw+'}'
        return raw
    for id in ids:
        i=next(i for i,r in enumerate(originals) if r['id']==id)
        seq.append('ORIGINAL '+id+' '+str(i)+'\n'+render(originals[i],'/'+str(i),'ORIGINAL')+'\n')
        seq.append('ACCEPTANCE '+id+'\n'+render(accepted[id],'/'+id,'ACCEPTANCE')+'\n')
    text=''.join(seq)
    meta={'objects':48,'IDs':ids,'original_binding':{'commit':ORIG,'path':OP},'acceptance_binding':{'commit':PLAN,'path':AP},'policy':'All keys, array order, short scalars and first long values displayed; exact repeated long values refer to first value. Fixed objects retain original structure and every unique value; mappings are reversible through pinned selectors. Hash/parse preparation is not semantic reading.','rendered_characters':len(text),'rendered_sha256':hashlib.sha256(text.encode()).hexdigest(),'values':locs}
    return text,meta
if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='read':display(sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5]))
    elif mode=='source':display(sys.argv[3],sys.argv[4],int(sys.argv[5]),int(sys.argv[6]),sys.argv[2])
    elif mode in ['control-stats','control-page']:
        stream,meta=controls()
        if mode=='control-stats':
            (OUT/'control-dedup-map.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
            print(meta['rendered_characters'],len(meta['values']),meta['IDs'])
        else:
            start,end=int(sys.argv[2]),int(sys.argv[3]);print(stream[start:end]);journal({'kind':'lossless_control_characters_displayed','stream_sha256':meta['rendered_sha256'],'start_inclusive':start,'end_exclusive':min(end,len(stream)),'total':len(stream),'credit':'No semantic credit for truncated outputs'})
