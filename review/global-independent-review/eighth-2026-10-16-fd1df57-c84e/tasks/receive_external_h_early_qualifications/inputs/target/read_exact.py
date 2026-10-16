"""Read-only evidence presentation with local receipts; never executes evidence."""
from pathlib import Path
import argparse, datetime, hashlib, json

TASK = Path(__file__).resolve().parent
REC = TASK / 'recovered-early-history'

def ident(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(b)}\0'.encode() + b).hexdigest()}

def main():
    a = argparse.ArgumentParser()
    a.add_argument('path')
    a.add_argument('--pointer', default='')
    a.add_argument('--start', type=int, default=1)
    a.add_argument('--end', type=int)
    a.add_argument('--name', required=True)
    args = a.parse_args()
    rel = Path(args.path)
    assert not rel.is_absolute() and '..' not in rel.parts
    assert args.start >= 1
    assert all(c.isalnum() or c in '-_' for c in args.name)
    source = TASK / rel
    b = source.read_bytes()
    if args.pointer:
        obj = json.loads(b)
        for field in args.pointer.lstrip('/').split('/'):
            field = field.replace('~1', '/').replace('~0', '~')
            obj = obj[int(field)] if isinstance(obj, list) else obj[field]
        shown = json.dumps(obj, ensure_ascii=False, indent=2) + '\n'
    else:
        shown = b.decode()
    lines = shown.splitlines(keepends=True)
    end = args.end or len(lines)
    assert end <= len(lines)
    out = ''.join(lines[args.start-1:end])
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    record = {'reader': 'external-H-EARLY-QUALIFICATIONS/root', 'utc': now,
              'source_task_path': str(rel), 'identity': ident(b),
              'pointer': args.pointer, 'presentation': 'exact UTF8' if not args.pointer else 'lossless JSON pointer, pretty printed',
              'lines': [args.start, end], 'presentation_total_lines': len(lines),
              'scope': 'only presented pointer/lines, no credit for unpresented siblings',
              'output_identity': ident(out.encode()), 'execution': 'TOOL_VALIDATION_ONLY',
              'semantic_status': 'PRESENTED_PENDING_READER_ACK', 'restored_code_executed': False}
    log = TASK / 'read-logs'
    log.mkdir(exist_ok=True)
    (log / (args.name + '.stdout')).write_text(out)
    (log / (args.name + '.receipt.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(record, ensure_ascii=False))
    print(out, end='')

if __name__ == '__main__':
    main()
