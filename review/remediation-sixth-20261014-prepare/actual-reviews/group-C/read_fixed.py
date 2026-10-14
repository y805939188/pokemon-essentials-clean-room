"""Bounded fixed-blob reads; logs are evidence of reading, not semantic verdicts."""
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path('/workspace/r6-actual-c')
OUT = pathlib.Path(__file__).parent
ACT = '86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
PRIOR_ACT = '9d5b4e99b617828690e6529b77a1e555d7c9eb1b'
PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
BASE = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'


def git(*args, reference=False):
    argv = ['git', '--git-dir=/tmp/r6-u07-reference.git'] if reference else ['git', '-C', str(ROOT)]
    return subprocess.check_output(argv + list(args))


def payload(role, path):
    commit = {'actual':ACT, 'prior_actual':PRIOR_ACT, 'prepare':PREP, 'baseline':BASE, 'reference':REF}.get(role,role)
    b = git('show',commit+':'+path,reference=role=='reference')
    return commit,b


def read(role, path, start, end, mode='lines'):
    commit,b = payload(role,path)
    s = b.decode()
    if mode == 'json':
        s = json.dumps(json.loads(s),ensure_ascii=False,separators=(',',':'))
    if mode == 'json-dedup':
        original = json.loads(s)
        counts = {}
        def key(v):
            return json.dumps(v,ensure_ascii=False,separators=(',',':'),sort_keys=True)
        def count(v):
            k=key(v)
            if isinstance(v,(dict,list,str)) and len(k)>=100:
                counts[k]=counts.get(k,0)+1
            if isinstance(v,dict):
                for x in v.values(): count(x)
            elif isinstance(v,list):
                for x in v: count(x)
        count(original)
        ids={}; definitions={}
        def encode(v):
            k=key(v)
            if counts.get(k,0)>1:
                if k in ids:return {'$exact_ref':ids[k]}
                ident='D'+str(len(ids));ids[k]=ident
                encoded=children(v)
                return {'$exact_def':ident,'value':encoded}
            return children(v)
        def children(v):
            if isinstance(v,dict):return {k:encode(x) for k,x in v.items()}
            if isinstance(v,list):return [encode(x) for x in v]
            return v
        encoded=encode(original)
        def decode(v):
            if isinstance(v,dict) and '$exact_ref' in v:return definitions[v['$exact_ref']]
            if isinstance(v,dict) and '$exact_def' in v:
                result=decode(v['value']);definitions[v['$exact_def']]=result;return result
            if isinstance(v,dict):return {k:decode(x) for k,x in v.items()}
            if isinstance(v,list):return [decode(x) for x in v]
            return v
        assert decode(encoded)==original
        s=json.dumps(encoded,ensure_ascii=False,separators=(',',':'))
    total = len(s) if mode != 'lines' else len(s.splitlines())
    end = min(end,total)
    row = {'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'role':role,'commit':commit,'path':path,'bytes':len(b),
           'sha256':hashlib.sha256(b).hexdigest(),
           'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),
           'mode':mode,'total_units':total,'span':[start,end],
           'coordinate_rule':'lines are1-based inclusive; text/json chars0-based half-open',
           'normalization':('Full JSON exact-value dedup: first occurrence printed as $exact_def with complete value; repeats reference that identical value by $exact_ref; recursive reconstruction asserted equal to entire original. All original keys/values retained or exactly referenced.' if mode=='json-dedup' else 'JSON parsed and losslessly printed compactly; all keys and values retained' if mode=='json' else 'none'),
           'execution':'TOOL_READ_ONLY', 'reference_execution':0}
    with (OUT/'read-journal.jsonl').open('a') as f:
        f.write(json.dumps(row,ensure_ascii=False)+'\n')
    print(json.dumps(row,ensure_ascii=False))
    if mode=='lines':
        for i in range(start-1,end):
            print(str(i+1)+': '+s.splitlines()[i])
    else:
        print(s[start:end])


if __name__=='__main__':
    read(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),sys.argv[5] if len(sys.argv)>5 else 'lines')
