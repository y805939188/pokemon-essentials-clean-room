#!/usr/bin/env python3
"""Finite document/identity/regression checks; no reference or behavior execution."""
import collections
import datetime
import difflib
import hashlib
import json
import re
import subprocess
from pathlib import Path

E = Path(__file__).resolve().parent
ROOT = E.parents[4]
PREP = E.parents[2]
MIRROR = E.parent/'mirror'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
BASE = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
CONTRACT = json.loads((PREP/'contracts/R6-U06.json').read_text())
EXPECTED = {
    'demo-dx/wp73-a-content-editors.md': [('replace', 53, 53), ('replace', 71, 71), ('insert', 140, 139), ('insert', 204, 203)],
    'demo-dx/wp75-project-conversion-and-authoring-tools.md': [('replace', 241, 241), ('replace', 289, 289), ('replace', 392, 392)],
    'test-catalog/demo-dx-wp72-73-74-75-76-77.md': [('replace', 62, 62), ('replace', 66, 66), ('insert', 68, 67), ('replace', 94, 94), ('replace', 162, 162), ('replace', 175, 175)]
}
def git(*argv):
    return subprocess.check_output(['git', '-C', str(ROOT), *argv])
def identity(b):
    return dict(bytes=len(b), sha256=hashlib.sha256(b).hexdigest(),
                git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
checks = []
def checked(name, condition, detail=None):
    checks.append(dict(name=name, result='PASS' if condition else 'FAIL', detail=detail))
    assert condition, name

prompt = (PREP/'prompts/R6-U06-A.md').read_bytes()
checked('frozen full prompt identity', identity(prompt) == dict(bytes=224391, sha256='09ffb6d2e5bc0d41dd7cabeecc8c47af19dc1623d0553c678d77d25ffb7c478b', git_blob='bda5a95099421d783c245dfe6d65f260d68aa9d4'))
checked('entire JSON contract is literally embedded in fully read prompt', (PREP/'contracts/R6-U06.json').read_bytes() in prompt)
files = {}
hunks = []
for path in CONTRACT['candidate_formal_paths']:
    old = git('cat-file', 'blob', MAIN+':'+path)
    p = MIRROR/path
    new = p.read_bytes()
    checked('baseline mirror was fixed formal bytes: '+path, git('cat-file','blob',BASE+':'+str(p.relative_to(ROOT))) == old)
    checked('actual formal still fixed: '+path, (ROOT/path).read_bytes() == old)
    a, b = old.decode().splitlines(), new.decode().splitlines()
    diff = []
    for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
        if tag != 'equal':
            diff.append((tag,i+1,j))
            hunks.append(dict(path=path, tag=tag, baseline_lines=[i+1,j], candidate_lines=[k+1,l]))
    checked('only declared clause replacements/additions: '+path, diff == EXPECTED[path.removeprefix('deliverables/final-specification-set/')], diff)
    checked('UTF-8 newline and no source implementation fragments: '+path,
            new.endswith(b'\n') and '\r' not in new.decode() and not re.search(r'^\s*(def |class |module |import |from )', '\n'.join(b)))
    files[path] = dict(baseline=identity(old), candidate=identity(new), mode='100644', type='blob')

tcpath = 'deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md'
oldtc = git('cat-file','blob',MAIN+':'+tcpath).decode().splitlines()
newtc = (MIRROR/tcpath).read_text().splitlines()
rows = lambda lines: [x for x in lines if x.startswith('| ') and not x.startswith('| ---') and x.split('|')[1].strip() != 'ID']
rowkey = lambda line: line.split('|')[1].strip()
oldrows, newrows = rows(oldtc), rows(newtc)
newids = {'CE-TYPES-%02d'%i for i in range(1,7)}
checked('all prior table IDs/order/duplicate occurrences retained', [rowkey(x) for x in newrows if rowkey(x) not in newids] == [rowkey(x) for x in oldrows])
changedrows = {'CE-M15','CE-M19','WE-M20','CV-M11','CV-M24'}
checked('every other old table row remains byte-exact', [x for x in newrows if rowkey(x) not in newids|changedrows] == [x for x in oldrows if rowkey(x) not in changedrows])
checked('six finite new type rows, once each', all(sum(rowkey(x)==i for x in newrows)==1 for i in newids))
checked('B19-C016 and all B17/B19/B20/R5-U07 inherited vectors preserved', all(x in newrows for x in oldrows if rowkey(x).startswith(('B17-','B19-','B20-','U07-'))))
checked('metrics authoritative formal kept byte-exact', (ROOT/'deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md').read_bytes() == git('cat-file','blob',MAIN+':deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md'))

# New links are checked in their eventual formal location, including headings.
for path in CONTRACT['candidate_formal_paths']:
    newtext = (MIRROR/path).read_text()
    oldtext = git('cat-file','blob',MAIN+':'+path).decode()
    for dest in set(re.findall(r'\]\(([^)]+)\)',newtext)) - set(re.findall(r'\]\(([^)]+)\)',oldtext)):
        filename, _, fragment = dest.partition('#')
        target = (ROOT/path).parent/filename
        checked('new logical-formal link exists: '+dest, target.is_file())
        headings = []
        for line in target.read_text().splitlines():
            if line.startswith('#'):
                text = re.sub(r'[^\w\- ]','',line.lstrip('#').strip()).replace(' ','-').lower()
                headings.append(text)
        checked('new link heading exists: '+dest, not fragment or fragment in headings)

status = git('status','--porcelain','--untracked-files=all').decode().splitlines()
prefix = str(E.parent.relative_to(ROOT))+'/'
checked('all changed/untracked paths are in own exact write set', all(x[3:].startswith(prefix+'evidence/') or x[3:] in {str((MIRROR/p).relative_to(ROOT)) for p in CONTRACT['candidate_formal_paths']} for x in status),status)
checked('actual formal tree unchanged since preparation', not git('diff','--name-only',BASE,'--','deliverables/final-specification-set').strip())
checked('fixed main is ancestor of prepare', subprocess.run(['git','-C',str(ROOT),'merge-base','--is-ancestor',MAIN,BASE]).returncode == 0)

readings = [json.loads(x) for x in (E/'reading-scopes.jsonl').read_text().splitlines()]
covered = set()
for x in readings:
    if x['path'] == 'Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb':
        for a,b in x['ranges']: covered.update(range(a,b+1))
checked('MapsAndEvents full semantic read emission has no gaps', covered == set(range(1,1752)))
checked('required source contexts have emitted readings', set(CONTRACT['read_only_reference_paths']) <= {x['path'] for x in readings})

report = dict(evidence_level='TOOL_VALIDATION', utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              cwd=str(ROOT), result='PASS_FINITE_DOCUMENT_IDENTITY_SCOPE_CHECKS', checks=checks,
              changed_clause_spans=hunks, payloads=files,
              source_static_semantics='Separately assessed by author; string/diff checks are not semantic proof.',
              reference_execution=0, derived_vectors_executed=0, independent_behavior_model=0,
              native_host=0, Demo=0, real_save=0, independent_review='PENDING_NON_AUTHOR')
(E/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(result=report['result'], checks=len(checks), changed_clause_spans=hunks),ensure_ascii=False,indent=2))
