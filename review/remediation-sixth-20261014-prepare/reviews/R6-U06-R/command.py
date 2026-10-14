import sys, json, subprocess, datetime
from pathlib import Path
root = Path(__file__).resolve().parent
label, *argv = sys.argv[1:]
assert '/' not in label and not (root / (label + '.json')).exists(), 'Use a fresh label; preserve attempts.'
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
p = subprocess.run(argv, capture_output=True)
(root / (label + '.stdout')).write_bytes(p.stdout)
(root / (label + '.stderr')).write_bytes(p.stderr)
record = dict(argv=argv, cwd=str(Path.cwd()), start_utc=start,
              end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), exit_code=p.returncode,
              stdout=label + '.stdout', stderr=label + '.stderr')
(root / (label + '.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, ensure_ascii=False))
print(p.stdout.decode(errors='replace')); print(p.stderr.decode(errors='replace'), file=sys.stderr)
sys.exit(p.returncode)
