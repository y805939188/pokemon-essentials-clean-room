"""Explicit reader acknowledgement followed by exact next chunk presentation."""
from pathlib import Path
import argparse,datetime,json,subprocess,sys
p=Path(__file__).resolve().parent
a=argparse.ArgumentParser();a.add_argument('--ack',type=int);a.add_argument('--read',type=int,required=True);q=a.parse_args()
f=p/'semantic-atlas/manifest.json';x=json.loads(f.read_text())
if q.ack:
 r=x['chunks'][q.ack-1]
 r.update(status='ACTUALLY_READ',reader='external-H-EARLY-QUALIFICATIONS/root',acknowledged_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 f.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
name=x['chunks'][q.read-1]['file']
subprocess.run([sys.executable,str(p/'read_exact.py'),'semantic-atlas/'+name,'--name',f'atlas-{q.read:03d}'],check=True)
