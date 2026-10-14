"""Validate only this batch's fixed material identities; never run the reference."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
PREP = ROOT / 'review/remediation-sixth-20261014-prepare'
C = json.loads((PREP / 'contracts/R6-U14.json').read_text())
INDEX = json.loads((PREP / 'inputs/frozen-inputs.json').read_text())
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)
def identity(ref, path):
    data = git('show', ref + ':' + path)
    entry = git('ls-tree', ref, '--', path).decode().strip().split()
    return dict(commit=ref, path=path, bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob=git('rev-parse', ref + ':' + path).decode().strip(), mode=entry[0], object_type=entry[1])
rows=[]
for kind, paths, ref, records in [
    ('reference', C['read_only_reference_paths'], C['frozen_reference'], INDEX['source_materials']),
    ('formal', C['candidate_formal_paths'], C['frozen_main'], INDEX['formal_materials'])]:
    bypath={x['path']:x for x in records}
    for path in paths:
        got=identity(ref,path)
        expected=bypath[path]
        checks={k:got[k]==expected[k] for k in ['bytes','sha256','git_blob','mode']}
        assert all(checks.values()), (path, checks)
        if kind=='formal':
            mirror=PREP/'candidates/R6-U14/mirror'/path
            assert mirror.read_bytes()==git('show',ref+':'+path),path
        rows.append(dict(role=kind,**got,expected_material_type=expected.get('type', 'text/formal_markdown'),checks=checks))
prompt=PREP/'prompts/R6-U14-A.md'
p=prompt.read_text()
embedded=p.split('## 本批确定合同（含原证据、反例、验收、同步和实际路径）\n\n```json\n',1)[1].split('\n```',1)[0]+'\n'
assert embedded.encode()==(PREP/'contracts/R6-U14.json').read_bytes()
assert prompt.stat().st_size==350085
assert hashlib.sha256(prompt.read_bytes()).hexdigest()=='9e6b3d0b26724332cb0b87b45d68f9ee4b408e99e79690b8482be24a4f05c4f3'
trees={r:git('rev-parse',r+'^{tree}').decode().strip() for r in [C['frozen_main'],C['frozen_reference'],'469a268b92daed7b4d28d7fd0da75520cbb7228f']}
assert trees[C['frozen_reference']]==INDEX['reference_tree']
assert git('rev-parse',C['frozen_main']+':deliverables/final-specification-set').decode().strip()==INDEX['formal_tree']
result=dict(batch=C['id'],utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),cwd=str(ROOT),
            fixed_prepare='469a268b92daed7b4d28d7fd0da75520cbb7228f',trees=trees,
            prompt=identity('469a268b92daed7b4d28d7fd0da75520cbb7228f',str(prompt.relative_to(ROOT))),
            embedded_contract_exact_byte_equal=True,material_identities=rows,
            model_requested=C['author'],effective_configuration='UNVERIFIED: no effective echo in available task context; no CLI or extra agent launched',
            current_instruction_override='User authorizes this live cloud author, specifies branch and forbids repeated configuration probing; historical NOT_STARTED fields not rewritten',
            prompt_semantic_read_ranges=[[1,230],[231,870],[871,1390],[1391,1920],[1921,2480],[2481,3030],[3031,3630],[3631,4200],[4201,4720],[4721,5200],[5201,5770],[5771,6334]],
            prompt_read_note='All ranges displayed and inspected. Initial oversized contract display truncated and was not counted; full byte-identical embedded contract was read in these ranges. Initial tool calls did not capture per-process UTC/stdout/stderr into files; platform tool transcript preserves outputs. These missing metadata are not backfilled.',
            reference_mapping='Fixed reference fetched into this repository object database; no reference checkout or edits',
            status='INPUT_IDENTITY_CHECK_PASS_ONLY; no semantic or runtime PASS implied')
(OUT/'input-snapshot.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=result['status'],materials=len(rows),prompt_bytes=350085),ensure_ascii=False))
