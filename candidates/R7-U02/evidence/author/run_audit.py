"""Record public audit commands; never invoke restored reference programs."""
import base64
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    name, *argv = sys.argv[1:]
    if argv and argv[0] == '--':
        argv = argv[1:]
    assert name.replace('-', '').replace('_', '').isalnum() and argv
    directory = Path(__file__).resolve().parent / 'logs'
    directory.mkdir(exist_ok=True)
    receipt = directory / (name + '.json')
    assert not receipt.exists(), 'Never overwrite a previous command receipt'
    start = utc()
    process = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    def save_stream(suffix, data):
        encoded = any(line.endswith((b' ', b'\t')) for line in data.splitlines())
        filename = name + '.' + suffix + ('.base64' if encoded else '')
        (directory / filename).write_bytes(base64.b64encode(data) + b'\n' if encoded else data)
        return {'path': filename, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                'encoding': 'base64' if encoded else 'raw'}
    streams = {'stdout': save_stream('stdout', stdout), 'stderr': save_stream('stderr', stderr)}
    record = {
        'argv': argv, 'cwd': str(Path.cwd()), 'pid': process.pid,
        'start_utc': start, 'end_utc': utc(), 'exit_code': process.returncode,
        **streams,
        'qualification': 'Audit/tool I/O only; no behavior, reference, native, host, Demo, media, model, or save execution credit.'
    }
    receipt.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    sys.stdout.buffer.write(stdout)
    sys.stderr.buffer.write(stderr)
    print(json.dumps({'receipt': str(receipt), 'exit_code': process.returncode}))
    raise SystemExit(process.returncode)


if __name__ == '__main__':
    main()
