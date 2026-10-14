"""Read fixed Git text as evidence; never execute reference content."""
import datetime, hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = ROOT / 'review/remediation-sixth-20261014-prepare/reviews/R6-U10-R'
ref, path = sys.argv[1:3]
begin = int(sys.argv[3]) if len(sys.argv) > 3 else 1
end = int(sys.argv[4]) if len(sys.argv) > 4 else None
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
argv = ['git', 'show', ref + ':' + path]
p = subprocess.run(argv, cwd=ROOT, capture_output=True)
if p.returncode:
    sys.stderr.buffer.write(p.stderr)
    sys.exit(p.returncode)
data = p.stdout
lines = data.decode('utf-8').splitlines()
end = len(lines) if end is None else min(end, len(lines))
delivered = '\n'.join(f'{i+1}: {line}' for i, line in enumerate(lines[begin-1:end], begin-1)) + '\n'
blob = subprocess.check_output(['git', 'rev-parse', ref + ':' + path], cwd=ROOT, text=True).strip()
row = dict(reviewer='/root', cwd=str(ROOT), argv=argv, request_argv=sys.argv, started_utc=started,
           ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), exit_code=p.returncode,
           stderr=p.stderr.decode(), ref=ref, path=path, git_blob=blob, bytes=len(data),
           sha256=hashlib.sha256(data).hexdigest(), physical_lines=len(lines), start_line=begin,
           end_line=end, delivered_stdout_bytes=len(delivered.encode()),
           delivered_stdout_sha256=hashlib.sha256(delivered.encode()).hexdigest(),
           evidence_level='SOURCE_STATIC_READ_DELIVERY_NOT_BEHAVIOR_EXECUTION',
           semantic_read_credit='ONLY_IF_TOOL_OUTPUT_UNTRUNCATED_AND_CONSUMED',
           platform_uuid='UNVERIFIED')
with (OUT / 'primary-read-delivery.jsonl').open('a') as f:
    f.write(json.dumps(row, ensure_ascii=False) + '\n')
print(json.dumps({k:row[k] for k in ['ref','path','git_blob','bytes','sha256','physical_lines','start_line','end_line']},ensure_ascii=False))
print(delivered, end='')
