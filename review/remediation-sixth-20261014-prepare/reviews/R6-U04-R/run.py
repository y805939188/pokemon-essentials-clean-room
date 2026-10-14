"""Capture exact finite verification processes and ordinary publication operations."""
import datetime, json, pathlib, subprocess, sys
OWN = pathlib.Path(__file__).resolve().parent
name, argv = sys.argv[1], sys.argv[2:]
begin = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = subprocess.run(argv, capture_output=True)
finish = datetime.datetime.now(datetime.timezone.utc).isoformat()
logs = OWN / 'processes'
logs.mkdir(exist_ok=True)
prefix = logs / name
assert not prefix.with_suffix('.json').exists(), 'Do not overwrite attempts'
prefix.with_suffix('.stdout').write_bytes(result.stdout)
prefix.with_suffix('.stderr').write_bytes(result.stderr)
record = dict(argv=argv, cwd=str(pathlib.Path.cwd()), utc_start=begin, utc_end=finish, exit=result.returncode,
              stdout=str(prefix.with_suffix('.stdout').relative_to(OWN)), stderr=str(prefix.with_suffix('.stderr').relative_to(OWN)))
prefix.with_suffix('.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(record, ensure_ascii=False))
sys.stdout.write(result.stdout.decode(errors='replace'))
sys.stderr.write(result.stderr.decode(errors='replace'))
sys.exit(result.returncode)
