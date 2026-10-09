"""Independent Markdown inventory metadata extraction; no behavior evaluator."""
import collections
import hashlib
import json
import re
import subprocess
from pathlib import Path

BASE='1d06c45cc0a744fca181ac80ee573cc9ebb9b862'
CANDIDATE='8ddba850af71f24e7bd77a80b7605c456c31dc7a'
ROOT='review/remediation/20261003-prepare/batches/B12/'
OUT=Path(ROOT+'affected-candidate-review-1/B02')
NAMES={'A':'wp52-a-evaluation-coverage-and-data.md',
       'B':'wp52-b-effect-coverage.md','C':'wp52-c-item-control-coverage-and-data.md'}
FAMILIES={'F':'MoveFailureCheck','T':'MoveFailureAgainstTargetCheck','S':'MoveEffectScore',
          'G':'MoveEffectAgainstTargetScore','P':'MoveBasePower'}

def read(commit,path):
    return subprocess.check_output(['git','show',commit+':'+path]).decode()

def original_table(text,part):
    result=[]
    if part=='A': text=text.split('## 5.')[0]
    for line in text.splitlines():
        if not line.startswith('|'): continue
        cells=[x.strip() for x in line.split('|')[1:-1]]
        if part=='A' and len(cells)>=3 and cells[0] in ['GeneralMoveAgainstTargetScore','GeneralMoveScore','AbilityRanking']:
            source=re.search(r'←([A-Za-z][A-Za-z0-9_]*)',cells[2])
            result.append((cells[0],cells[1].strip('`'),source[1] if source else None))
            continue
        if part=='A' and len(cells)>=2 and re.fullmatch(r'`?[A-Za-z][A-Za-z0-9_]*`?',cells[0]):
            identity=cells[0].strip('`')
            for family,source in re.findall(r'(?:^|、)([FTSGP])(?::\d+)?(?:←([A-Za-z][A-Za-z0-9_]*))?',cells[1]):
                result.append((FAMILIES[family],identity,source or None))
        elif part!='A' and len(cells)>=3:
            m=re.fullmatch(r'([A-Za-z]+)\s*/\s*`([A-Za-z][A-Za-z0-9_]*)`',cells[1])
            if m:
                source_match=re.search(r'←([A-Za-z][A-Za-z0-9_]*)',cells[2])
                source=source_match[1] if source_match else None
                result.append((m[1],m[2],source))
    return result

def list_tokens(text,family):
    text=re.sub(r'（[^）]*）','',text)
    text=re.sub(r'\([^)]*\)','',text)
    text=text.rstrip('。')
    result=[]
    for group in re.split('[；;]',text):
        chunks=group.split('←',1)
        source=chunks[1].strip() if len(chunks)==2 else None
        for identity in re.split('[、,，]',chunks[0]):
            identity=identity.strip().strip('`')
            if re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*',identity): result.append((family,identity,source))
    return result

def generic_a(text):
    result=[]
    region=re.search(r'^## 3\..*?(?=^## 4\.)',text,re.M|re.S)[0]
    for line in region.splitlines():
        for prefix,family in [('GeneralMoveAgainstTargetScore：','GeneralMoveAgainstTargetScore'),
            ('GeneralMoveScore：','GeneralMoveScore'),('add：','AbilityRanking'),('copy：','AbilityRanking')]:
            if line.startswith(prefix): result+=list_tokens(line[len(prefix):],family)
    return result

def final_list(text,part):
    result=[]
    for line in text.splitlines():
        m=re.match(r'^(MoveFailureCheck|MoveFailureAgainstTargetCheck|MoveEffectScore|MoveEffectAgainstTargetScore|MoveBasePower)(?:（[^）]*）)?：(.*)',line)
        if m: result+=list_tokens(m[2],m[1])
        if part=='C' and line.startswith('直接登记（46）：'):
            result+=list_tokens(line.split('：',1)[1],'ItemRanking')
        if part=='C' and line.startswith('复制登记（7，均绑定成功）：'):
            result+=list_tokens(line.split('：',1)[1],'ItemRanking')
        if part=='C' and line.startswith('复制缺源（1）：'):
            m=re.search(r'(MoveEffectScore) / (\w+)←(\w+)',line)
            assert m
            result.append(m.groups())
    return result

results={}
for part,name in NAMES.items():
    old=read(BASE,'specs/combat/'+name)
    new=read(CANDIDATE,'deliverables/final-specification-set/combat-requirements/'+name)
    before=original_table(old,part)
    after=original_table(new,part) if part=='A' else final_list(new,part)
    if part=='A':
        before+=generic_a(old)
        after+=generic_a(new)
    literal_count=len(after)
    if part=='B':
        # The final list explicitly describes one final behavior for this duplicate.
        assert after.count(('MoveEffectScore','PowerHigherWithConsecutiveUse',None))==1
        after.append(('MoveEffectScore','PowerHigherWithConsecutiveUse',None))
    missing=list((collections.Counter(before)-collections.Counter(after)).elements())
    extra=list((collections.Counter(after)-collections.Counter(before)).elements())
    results[part]={'original_occurrences':len(before),'final_literal_occurrences':literal_count,
                  'final_audited_occurrences':len(after),'multiset_equal':not missing and not extra,
                  'missing':missing,'extra':extra,
                  'original_tuple_hash':hashlib.sha256(json.dumps(sorted(before,key=str),ensure_ascii=False).encode()).hexdigest(),
                  'final_tuple_hash':hashlib.sha256(json.dumps(sorted(after,key=str),ensure_ascii=False).encode()).hexdigest()}
report={'FIX_BASE':BASE,'reviewed_sha':CANDIDATE,'results':results,
    'method':'Extract all stage/identity/copy-source tuples from exact original and candidate Markdown, including A generic/AbilityRanking, B occurrence-only duplicate restoration, and C missing-source Sketch. This is inventory metadata, not behavioral execution.',
    'behavior_executions':0,'independent_full_quality_verdict':None}
(OUT/'shared-inventories.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
