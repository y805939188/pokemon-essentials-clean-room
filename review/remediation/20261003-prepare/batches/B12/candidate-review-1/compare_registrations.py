"""Text catalog comparison; does not execute or translate reference behavior."""
import collections
import json
import pathlib
import re
import subprocess

C = "8ddba850af71f24e7bd77a80b7605c456c31dc7a"
ROOT = pathlib.Path("review/remediation/20261003-prepare/batches/B12/candidate-review-1")
FILES = {"A":"wp52-a-evaluation-coverage-and-data.md", "B":"wp52-b-effect-coverage.md", "C":"wp52-c-item-control-coverage-and-data.md"}
FAMILIES = {"F":"MoveFailureCheck", "T":"MoveFailureAgainstTargetCheck", "S":"MoveEffectScore", "G":"MoveEffectAgainstTargetScore", "P":"MoveBasePower"}

def read(path):
    return subprocess.check_output(["git", "show", C + ":" + path]).decode()

def original(group, text):
    rows=[]
    for line in text.splitlines():
        if group=="A" and line.startswith("## 4."): break
        if group!="A" and line.startswith("## 3."): break
        cells=[x.strip() for x in line.split("|")[1:-1]]
        if not cells:continue
        if group=="A" and re.fullmatch(r"`[A-Za-z0-9_]+`", cells[0]):
            name=cells[0].strip("`")
            for f,source in re.findall(r"([FTSGP]):\d+(?:←([A-Za-z0-9_]+))?",cells[1]):rows.append((FAMILIES[f],name,source or None))
        elif group=="A" and len(cells)>2 and cells[0] in ["GeneralMoveScore","GeneralMoveAgainstTargetScore","AbilityRanking"]:
            rows.append((cells[0],cells[1].strip("`"),re.match(r"[A-Za-z0-9_]+",cells[2].split("←")[1])[0] if "←" in cells[2] else None))
        elif group!="A" and len(cells)>2:
            m=re.fullmatch(r"([A-Za-z]+) / `([A-Za-z0-9_]+)`",cells[1])
            if m:rows.append((m[1],m[2],re.match(r"[A-Za-z0-9_]+",cells[2].split("←")[1])[0] if "←" in cells[2] else None))
    return rows

def names(text):
    return re.findall(r"[A-Za-z][A-Za-z0-9_]*",text)

def final(group,text):
    rows=[]
    for line in text.splitlines():
        if group=="A" and line.startswith("## 4."):break
        if group!="A" and line.startswith("## 3."):break
        if group=="A" and line.startswith("| "):
            cells=[x.strip() for x in line.split("|")[1:-1]]
            if len(cells)>1 and re.fullmatch(r"[A-Za-z0-9_]+",cells[0]):
                for f,source in re.findall(r"([FTSGP])(?:←([A-Za-z0-9_]+))?",cells[1]):rows.append((FAMILIES[f],cells[0],source or None))
        m=re.match(r"(Move[A-Za-z]+|GeneralMove[A-Za-z]+)(?:（[^）]*）)?：(.+)",line)
        if m:
            body=re.sub(r"（[^）]*）","",m[2])
            for entry in re.split(r"[；;]",body):
                source=None
                if "←" in entry:
                    dest,source=entry.split("←",1);source=names(source)[0]
                else:dest=entry
                rows.extend((m[1],n,source) for n in names(dest))
        if group=="A" and line.startswith("add："):rows.extend(("AbilityRanking",n,None) for n in names(line.split("：",1)[1]))
        if group=="A" and line.startswith("copy："):
            for entry in line[5:].split("；"):
                dest,source=entry.split("←");rows.extend(("AbilityRanking",n,names(source)[0]) for n in names(dest))
        if group=="C" and line.startswith("直接登记（"):
            rows.extend(("ItemRanking",n,None) for n in names(line.split("：",1)[1]))
        if group=="C" and line.startswith("复制登记（"):
            for dest,source in re.findall(r"([A-Z]+)←([A-Z]+)",line):rows.append(("ItemRanking",dest,source))
        if group=="C" and line.startswith("复制缺源（"):
            f,d,s=re.search(r"(Move[A-Za-z]+) / ([A-Za-z]+)←([A-Za-z]+)",line).groups();rows.append((f,d,s))
    return rows

report={}
for group,name in FILES.items():
    a=original(group,read("specs/combat/"+name));b=final(group,read("deliverables/final-specification-set/combat-requirements/"+name))
    # B's body lists the final effective consecutive-use score once; original
    # occurrence provenance retains both adds. Keep this adjustment visible.
    normalized=list(b)
    adjustment=[]
    if group=="B":
        t=("MoveEffectScore","PowerHigherWithConsecutiveUse",None)
        if a.count(t)==2 and b.count(t)==1:
            normalized.append(t);adjustment.append(dict(tuple=t,reason="Original has two add occurrences; final effective behavior is listed once. §1 and independent duplicate audit preserve overwrite metadata; not two effective scores."))
    ca,cb=collections.Counter(a),collections.Counter(normalized)
    report[group]=dict(original_count=len(a),final_literal_count=len(b),final_occurrence_count_after_explicit_duplicate_accounting=len(normalized),missing=list((ca-cb).elements()),extra=list((cb-ca).elements()),equal=ca==cb,explicit_adjustment=adjustment,original_tuples=a,final_literal_tuples=b)
(ROOT/"registration-comparison.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
for g,x in report.items():print(g,{k:x[k] for k in x if 'tuples' not in k})
