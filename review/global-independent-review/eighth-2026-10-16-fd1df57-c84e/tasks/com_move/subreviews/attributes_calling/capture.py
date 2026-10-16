"""Static evidence capture only; does not import or run reference Ruby."""
from pathlib import Path
import datetime, hashlib, json, subprocess, sys
ROOT = Path(__file__).resolve().parent
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z')
def capture(name, args, cwd='/workspace/pokemon-essentials-clean-room'):
    requested_name=name
    suffix=1
    while (ROOT/'evidence'/f'{name}.stdout').exists() or (ROOT/'evidence'/f'{name}.stderr').exists():
        suffix+=1
        name=f'{requested_name}-{suffix:03d}'
    start=utc()
    p=subprocess.run(args,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    end=utc()
    (ROOT/'evidence'/f'{name}.stdout').write_bytes(p.stdout)
    (ROOT/'evidence'/f'{name}.stderr').write_bytes(p.stderr)
    row={'id':name,'argv':args,'cwd':cwd,'start_utc':start,'end_utc':end,'exit':p.returncode,
         'stdout':f'evidence/{name}.stdout','stderr':f'evidence/{name}.stderr','kind':'TOOL_VALIDATION',
         'business_behavior':'NOT_EXECUTED','stdout_bytes':len(p.stdout),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest()}
    with (ROOT/'evidence'/'commands.jsonl').open('a') as f: f.write(json.dumps(row,ensure_ascii=False)+'\n')
    return p
if __name__=='__main__':
    p=capture(sys.argv[1],sys.argv[2:])
    sys.stdout.buffer.write(p.stdout)
    sys.stderr.buffer.write(p.stderr)
    sys.exit(p.returncode)
