"""R6 audit command capture. Never runs shell interpolation or edits inputs."""
import datetime, json, pathlib, subprocess, sys, time
root = pathlib.Path(__file__).resolve().parents[1]
task, label, *command = sys.argv[1:]
out = root / ('evidence' if task == 'R6-I' else 'tasks/' + task) / 'commands'
out.mkdir(parents=True, exist_ok=True)
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
prefix = out / (stamp + '-' + label)
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
t = time.monotonic()
try:
    p = subprocess.run(command, cwd=root.parents[2], capture_output=True, timeout=120)
    stdout, stderr, code = p.stdout, p.stderr, p.returncode
except subprocess.TimeoutExpired as e:
    stdout, stderr, code = e.stdout or b'', e.stderr or b'', None
    stderr += b'\nCAPTURE_TIMEOUT_120S\n'
prefix.with_suffix('.stdout').write_bytes(stdout)
prefix.with_suffix('.stderr').write_bytes(stderr)
record = {'argv': command, 'cwd': str(root.parents[2]), 'started_at': start,
          'ended_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'duration_seconds': time.monotonic()-t, 'exit_code': code,
          'stdout': str(prefix.with_suffix('.stdout').relative_to(root)),
          'stderr': str(prefix.with_suffix('.stderr').relative_to(root))}
prefix.with_suffix('.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
sys.stdout.buffer.write(stdout)
sys.stderr.buffer.write(stderr)
sys.exit(code if code is not None else 124)
