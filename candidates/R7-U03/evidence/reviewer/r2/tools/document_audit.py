"""Bounded document preservation/link checks; no behavior-vector execution."""
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess

OUT=Path(__file__).resolve().parents[1]
REPO=OUT.parents[4]
INPUT=Path('/workspace/r7-review-input/R7-U03-r2-11bff8e7912a98de09691ad7d7b7a2d3194e2757/candidate/candidates/R7-U03')
FROZEN=Path('/workspace/r7-review-bootstrap/R7-U03-r2/mirror-diffs.patch')
B='e646432c644dec04d306842cc5a559a29c718fbc'
FILES=sorted((INPUT/'deliverables/final-specification-set').rglob('*.md'))
historical={'engine-overworld-wp11-15-59-60.md':['MV04','MV18','MV19','MV24','MR02','MR17','R5-DI01','R5-DI02','R5-DI03'],
            'pokemon-rules-wp53-60-61-62-69-70.md':['FP01','FP02','FP05','FP24','FP25','FP33','PD24','PD25','R4-PD02','R6-PD01','R6-PD02','R6-PD03'],
            'engine-overworld-wp16.md':['WR16','GR3-CAM06','GR3-CAM07','GR3-CAM08','GR3-CAM12','GR3-CAM15','GR3-CAM16','GR3-CAM17']}
preserved=[];links=[];vectors=[];patch=[]
for p in FILES:
    rel=p.relative_to(INPUT).as_posix();new=p.read_text()
    old=subprocess.check_output(['git','-C',str(REPO),'show',B+':'+rel]).decode()
    before=old.splitlines(keepends=True);after=new.splitlines(keepends=True)
    patch.extend(difflib.unified_diff(before,after,fromfile='a/'+rel,tofile='b/'+rel))
    for id in historical.get(p.name,[]):
        a=next(x for x in before if x.startswith('| '+id+' |'))
        assert a in after,id
        preserved.append(dict(path=rel,id=id,bytes=len(a.encode()),sha256=hashlib.sha256(a.encode()).hexdigest(),exact_original_row_retained=True,behavior_execution='NOT_EXECUTED'))
    for line in after:
        if re.match(r'\| R7-(BP|FP|CAM)\d{2} \|',line):
            assert '| NOT_EXECUTED |' in line
            vectors.append(dict(path=rel,id=line.split('|')[1].strip(),execution='NOT_EXECUTED'))
    for kind,a,b,c,d in difflib.SequenceMatcher(None,before,after,autojunk=False).get_opcodes():
        if kind=='equal':continue
        for line in after[c:d]:
            for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',line):
                target=link.split('#')[0]
                if not target or '://' in target:continue
                at=(p.parent/target).resolve()
                within=at.is_relative_to(INPUT)
                logical=at.relative_to(INPUT).as_posix() if within else None
                exists=at.is_file() or (logical is not None and (REPO/logical).is_file())
                assert exists,(rel,link)
                links.append(dict(path=rel,target=link,resolves_in_candidate_or_fixed_B=True))
assert len(vectors)==20
assert ''.join(patch).encode()==FROZEN.read_bytes(),'frozen diff mismatch'
result=dict(stage='TOOL_VALIDATION',mirror_diff_rebuilt_from_actual_B_and_candidate_matches_frozen_patch=True,
            historical_rows=preserved,historical_rows_verified=len(preserved),new_behavior_vectors=vectors,
            changed_clause_links=links,changed_clause_links_verified=len(links),
            qualification='Document membership and preservation only. Paper semantic assessment is in report/per-id; no vector or source executed.')
(OUT/'document-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(historical_rows=len(preserved),new_unexecuted_vectors=len(vectors),changed_clause_links=len(links),frozen_patch_matches=True,stage='TOOL_VALIDATION')))
