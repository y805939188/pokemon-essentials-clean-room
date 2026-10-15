"""Record actual public audit command I/O, PID, UTC and exit; no shell."""
import datetime, json, pathlib, subprocess, sys, time
out = pathlib.Path(__file__).parent / 'logs'
out.mkdir(exist_ok=True)
name, *argv = sys.argv[1:]
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
tick = time.monotonic()
with (out/(name+'.stdout')).open('xb') as stdout, (out/(name+'.stderr')).open('xb') as stderr:
    process = subprocess.Popen(argv, stdout=stdout, stderr=stderr)
    code = process.wait()
row = {'argv': argv, 'cwd': str(pathlib.Path.cwd()), 'start_utc': start, 'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'elapsed_seconds': time.monotonic()-tick, 'pid': process.pid, 'exit_code': code, 'stdout': 'logs/'+name+'.stdout', 'stderr': 'logs/'+name+'.stderr', 'qualification': 'Public audit subprocess only; PID is not model PID; no configuration certification.'}
(out/(name+'.json')).write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(row,ensure_ascii=False))
sys.exit(code)
