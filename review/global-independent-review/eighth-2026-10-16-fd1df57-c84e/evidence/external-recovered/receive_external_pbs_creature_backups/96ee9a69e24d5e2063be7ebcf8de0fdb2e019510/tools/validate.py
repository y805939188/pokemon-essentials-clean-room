"""Validate report integrity and honest incomplete status; no semantic or runtime credit."""
from pathlib import Path
import ast
import datetime
import hashlib
import json
import subprocess

T = Path(__file__).resolve().parents[1]
CONTRACT = '40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'

def main():
    checks = []
    def check(value, name):
        assert value, name
        checks.append(name)
    for p in T.rglob('*.json'):
        json.loads(p.read_text())
        checks.append('json:' + str(p.relative_to(T)))
    for p in (T / 'tools').glob('*.py'):
        ast.parse(p.read_text())
        checks.append('own-tool-syntax:' + p.name)
    frozen = json.loads((T/'frozen-denominator.json').read_text())
    ledger = json.loads((T/'reception-ledger.json').read_text())
    check({x['id'] for x in frozen['records']} == {x['id'] for x in ledger['records']}, 'record-ID-set')
    check(len(ledger['records']) == 6712, '6712-records')
    check(len(frozen['atoms']) == len(ledger['atoms']) == 212, '212-distinct-atom-population')
    unread = [x for x in ledger['records'] if x['literal_status'] == 'AVAILABLE_UNREAD_NOT_RECEIVED']
    check(len(unread) == 3940, '3940-available-unread-records')
    check(sum(x['field_count'] for x in unread) == 77195, '77195-unread-field-bindings')
    check(sum(x['omission_count'] for x in unread) == 72617, '72617-unreceived-omissions')
    check(ledger['status'] == 'INCOMPLETE' and not ledger['global_pass'], 'no-premature-completion')
    check(all(x['final_task_acceptance'] == 'OPEN_NOT_SIGNED' for x in ledger['records']), 'no-record-task-final-forgery')
    interface = json.loads((T/'interfaces.json').read_text())
    check(len(interface['interfaces']) == 12, '12-interfaces')
    check({x['id'] for x in interface['interfaces'] if x['status'] == 'FINITE_STATIC_INTERFACE_RECEIVED_FOR_ROOT'} == {'IF04','IF06'}, 'two-bounded-receipts')
    recovery = json.loads((T/'recovery.json').read_text())
    recovered = {str(p.relative_to(T/'recovered-target')) for p in (T/'recovered-target').rglob('*') if p.is_file()}
    check(recovered == {x['relative_to_target_task'] for x in recovery['files']}, '32-target-path-exact-collection')
    for row in recovery['files']:
        p = T/row['local_path']
        b = p.read_bytes()
        check(not p.is_symlink() and len(b) == row['bytes'] and hashlib.sha256(b).hexdigest() == row['sha256'], 'target-bytes:' + row['relative_to_target_task'])
    prefix = str(T.relative_to(Path.cwd())) + '/'
    changed = subprocess.check_output(['git','diff','--name-only',CONTRACT]).decode().splitlines()
    untracked = subprocess.check_output(['git','ls-files','--others','--exclude-standard']).decode().splitlines()
    check(all(p.startswith(prefix) for p in changed + untracked), 'exclusive-write-set')
    check(subprocess.check_output(['git','rev-parse','--abbrev-ref','HEAD']).decode().strip() == 'codex/r8-receive-pbs-creature-backups-20261016', 'dedicated-branch')
    result = dict(schema='r8-report-integrity-validation/v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  status='PASS_TOOL_INTEGRITY_ONLY',checks=checks,semantic_credit=0,behavior_execution='NOT_EXECUTED',task_status='INCOMPLETE')
    (T/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    payloads=[]
    for p in sorted(T.rglob('*')):
        if not p.is_file() or p == T / 'payload-manifest.json':
            continue
        check(not p.is_symlink(), 'no-symlink:' + str(p.relative_to(T)))
        b=p.read_bytes()
        payloads.append(dict(path=str(p.relative_to(T)),mode='100644',bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),
            blob=hashlib.sha1(('blob '+str(len(b))+'\0').encode()+b).hexdigest()))
    (T/'payload-manifest.json').write_text(json.dumps(dict(schema='r8-receiver-payload-manifest/v1',
        task_status='INCOMPLETE',excluded_self='Manifest identity bound externally by actual commit and complete remote tree receipt.',
        files=payloads,count=len(payloads),bytes=sum(x['bytes'] for x in payloads),semantic_credit=0),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],checks=len(result['checks']),payload_count=len(payloads),task_status='INCOMPLETE')))

if __name__ == '__main__':
    main()
