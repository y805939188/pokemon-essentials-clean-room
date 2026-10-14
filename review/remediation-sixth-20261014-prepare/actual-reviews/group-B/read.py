"""Read immutable review inputs; this is evidence tooling, not a behavior model."""
import datetime, hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OWN = ROOT / 'review/remediation-sixth-20261014-prepare/actual-reviews/group-B'
def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])
def read(repo, commit, path, start=1, end=None, json_key=None, exclude=None):
    begin = stamp()
    payload = git(repo, 'show', commit + ':' + path)
    lines = payload.decode('utf-8-sig').splitlines()
    stop = len(lines) if end is None else min(end, len(lines))
    assert 1 <= start <= stop <= len(lines)
    if json_key is not None:
        value = json.loads(payload)
        for key in json_key.split('/') if json_key else []:
            value = value[int(key)] if isinstance(value, list) else value[key]
        if exclude:
            value = {k:v for k,v in value.items() if k not in exclude.split(',')}
        shown = json.dumps(value, ensure_ascii=False, separators=(',', ':'))
    else:
        shown = '\n'.join(f'{i + 1}: {line}' for i, line in enumerate(lines) if start <= i + 1 <= stop)
    row = dict(repository=str(repo), commit=commit, tree=git(repo, 'rev-parse', commit+'^{tree}').decode().strip(), path=path,
               bytes=len(payload), sha256=hashlib.sha256(payload).hexdigest(), git_blob=hashlib.sha1(b'blob '+str(len(payload)).encode()+b'\0'+payload).hexdigest(),
               total_lines=len(lines), start=start, end=stop, json_key=json_key, excluded_keys=exclude, utc_start=begin, utc_end=stamp(), cwd=str(ROOT),
               argv=['git','-C',str(repo),'show',commit+':'+path], exit=0, stderr='', displayed_sha256=hashlib.sha256(shown.encode()).hexdigest(),
               evidence_level='READING_ONLY_NOT_BEHAVIOR_EXECUTION')
    with (OWN / 'reading-ledger.jsonl').open('a') as f:
        f.write(json.dumps(row, ensure_ascii=False)+'\n')
    print(json.dumps(row, ensure_ascii=False))
    print(shown)
if __name__ == '__main__':
    repo, commit, path = sys.argv[1:4]
    if len(sys.argv)>4 and sys.argv[4]=='--json-key':
        read(repo, commit, path, json_key=sys.argv[5], exclude=sys.argv[6] if len(sys.argv)>6 else None)
    else:
        read(repo, commit, path, int(sys.argv[4]) if len(sys.argv)>4 else 1, int(sys.argv[5]) if len(sys.argv)>5 else None)
