import datetime, hashlib, json, re, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=Path('/workspace/r7-ir-R7-U02')
MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
B='e646432c644dec04d306842cc5a559a29c718fbc'
refs={}
contract=json.loads((BASE/'original/dispatch/delegation/contracts/R7-U02.json').read_bytes())
def walk(x):
    if isinstance(x,dict):
        if all(k in x for k in ['input_sha256','json_pointer','raw_member_byte_offsets','raw_member_sha256']):
            refs[(x['input_sha256'],x['json_pointer'])]=x
        for v in x.values():walk(v)
    elif isinstance(x,list):
        for v in x:walk(v)
walk(contract)
raw={hashlib.sha256(p.read_bytes()).hexdigest():p for p in (BASE/'original/evidence').rglob('*.raw')}
checks=[]
for (sha,pointer),r in refs.items():
    if sha not in raw:continue
    data=raw[sha].read_bytes();a,b=r['raw_member_byte_offsets'];fragment=data[a:b]
    assert hashlib.sha256(fragment).hexdigest()==r['raw_member_sha256']
    value=json.loads(data)
    for token in pointer.lstrip('/').split('/'):
        token=token.replace('~1','/').replace('~0','~')
        value=value[int(token)] if isinstance(value,list) else value[token]
    assert json.loads(fragment)==value
    canonical=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    assert hashlib.sha256(canonical).hexdigest()==r['canonical_sha256'],pointer
    checks.append(dict(input_sha256=sha,pointer=pointer,offsets=[a,b],raw_member_sha256=r['raw_member_sha256'],canonical_sha256=r['canonical_sha256']))
assert len(checks)>=18
links=[]
for p in ('audit/source-traceability.md','planning/feature-matrix.md'):
    data=subprocess.check_output(['git','show',MI+':'+p]).decode()
    tail=data[data.index('## 第七轮累计整合的当前接收状态'):]
    target=re.search(r'\]\(([^)]+)\)',tail).group(1)
    import posixpath
    resolved=posixpath.normpath(posixpath.join(posixpath.dirname(p),target))
    assert resolved=='review/remediation-seventh-20261015-prepare/integration/wave2/v1/public-reception.json'
    subprocess.check_output(['git','cat-file','-e',MI+':'+resolved])
    links.append(dict(from_path=p,relative_target=target,resolved_path=resolved,commit=MI))
j=json.loads((BASE/'actual-input/integration/applied-clauses.json').read_bytes())
r=json.loads(subprocess.check_output(['git','show',MI+':review/remediation-seventh-20261015-prepare/integration/wave2/v1/public-reception.json']))
# Confirm all source bindings against the freeze rather than current branch tips.
f=json.loads(subprocess.check_output(['git','show','13d76ba61838b13925ba9d41f58a6b047564d926:review/remediation-seventh-20261015-prepare/integration/wave2/v1/integrated-input.json']))
err=json.loads(subprocess.check_output(['git','show',MI+':review/remediation-seventh-20261015-prepare/current-navigation-errata.json']))
assert err['current_label']=='WP72 §5.3／WP27' and err['reception']['ACCEPTED'] is False
assert err['reception']['CLOSED'] is False
original=subprocess.check_output(['git','show',B+':'+err['frozen_original']['path']])
assert hashlib.sha256(original).hexdigest()==err['frozen_original']['sha256']
assert json.loads(original)['items'][42]['actual_clause_label']==err['old_label']
clause=subprocess.check_output(['git','show',B+':'+err['current_clause']['path']])
line=clause.splitlines(keepends=True)[123]
assert hashlib.sha256(line).hexdigest()==err['current_clause']['rule_line_identity_including_LF']['sha256']
(ROOT/'bindings-and-links.json').write_text(json.dumps(dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),raw_member_checks=checks,current_pointer_links=links,errata=dict(status=err['status'],frozen_old_label=err['old_label'],current_label=err['current_label'],historical_payload_unchanged=True,ACCEPTED=False,CLOSED=False),qualification='TOOL_VALIDATION; semantic conclusions recorded separately'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(raw_members=len(checks),current_links=len(links),errata_historical_pointer=True)))
