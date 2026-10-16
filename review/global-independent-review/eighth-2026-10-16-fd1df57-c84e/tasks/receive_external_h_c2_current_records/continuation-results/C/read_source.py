"""Display immutable source or formal ranges; persist identities, never execute source."""
from pathlib import Path
import argparse, hashlib, json, subprocess, datetime
T=Path(__file__).resolve().parent
B='fd1df570cad987dc3852a3b958f03916e317f7fe'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def read(label,kind,path,ranges):
    repo='/workspace/pokemon-essentials' if kind=='R' else '/workspace/pokemon-essentials-clean-room'
    c=R if kind=='R' else B
    raw=subprocess.check_output(['git','-C',repo,'show',c+':'+path]);lines=raw.decode().splitlines(keepends=True)
    print('FIXED READ',label,kind,c,path,identity(raw), 'lines',len(lines))
    for start,end in ranges:
        assert 1<=start<=end<=len(lines),(label,start,end,len(lines))
        print('RANGE',start,end)
        print(''.join(f'{n+1}: {lines[n]}' for n in range(start-1,end)),end='')
    fp=T/'source-readings.json';d=json.loads(fp.read_text()) if fp.exists() else []
    d.append({'label':label,'repository':kind,'commit':c,'path':path,'file_identity':identity(raw),'ranges':ranges,'total_lines':len(lines),'range_identities':[identity(''.join(lines[a-1:b]).encode()) for a,b in ranges],'displayed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'DISPLAYED_PENDING_ACK','behavior':'NOT_EXECUTED'})
    fp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def ack(label,note):
    fp=T/'source-readings.json';d=json.loads(fp.read_text());r=next(r for r in d if r['label']==label);r['status']='ACTUAL_READ';r['note']=note;fp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('label');ap.add_argument('kind');ap.add_argument('path');ap.add_argument('ranges');a=ap.parse_args();read(a.label,a.kind,a.path,json.loads(a.ranges))
