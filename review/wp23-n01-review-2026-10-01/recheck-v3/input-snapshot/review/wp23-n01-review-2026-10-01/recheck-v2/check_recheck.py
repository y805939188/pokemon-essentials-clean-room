"""Reviewer-owned N01 v2 identity/diff checks; never executes reference code."""
from pathlib import Path
import json,hashlib,re,subprocess
OUT=Path(__file__).resolve().parent
ROOT=OUT.parent.parent.parent
PREV=OUT.parent
DEL=ROOT/'review/wp23-n01-delivery-2026-10-01/revision-v2'
REF=ROOT/'reference/pokemon-essentials'
COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def ident(b):return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def put(n,v):(OUT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def rebuild(original, diff):
    """Reconstruct a single UTF-8 unified diff in memory, with exact context checks."""
    src = original.decode().splitlines(keepends=True)
    raw_lines = diff.decode().splitlines(keepends=True)
    lines = []
    for line in raw_lines:
        if line.startswith('\\ No newline at end of file'):
            assert lines and lines[-1].endswith('\n')
            lines[-1] = lines[-1][:-1]
        else:
            lines.append(line)
    result, cursor, i = [], 0, 0
    while i < len(lines):
        if not lines[i].startswith('@@ '):
            i += 1
            continue
        m = re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', lines[i])
        assert m
        start = int(m[1]) - 1 if int(m[1]) else 0
        assert start >= cursor
        result.extend(src[cursor:start])
        cursor = start
        old_count = new_count = 0
        i += 1
        while i < len(lines) and not lines[i].startswith('@@ '):
            line = lines[i]
            assert line[0] in ' +-'
            if line[0] in ' -':
                assert src[cursor] == line[1:], (cursor, repr(src[cursor]), repr(line))
                cursor += 1
                old_count += 1
            if line[0] in ' +':
                result.append(line[1:])
                new_count += 1
            i += 1
        assert old_count == int(m[2] or 1)
        assert new_count == int(m[4] or 1)
    result.extend(src[cursor:])
    return ''.join(result).encode()

def main():
    inputs=json.loads((OUT/'input-manifest.json').read_text())
    for row in inputs['inputs']:
        want={k:row[k] for k in ('sha256','bytes')}
        assert ident((ROOT/row['path']).read_bytes())==want
        assert ident((OUT/'input-snapshot'/row['path']).read_bytes())==want
    bindings=json.loads((DEL/'diff-bindings.json').read_text())['bindings'];results=[]
    for row in bindings:
        original=(PREV/'input-snapshot'/row['path']).read_bytes()
        assert ident(original)==row['from_snapshot']
        current=rebuild(original,(DEL/row['diff']).read_bytes())
        assert ident(current)==row['to_current']
        assert current==(ROOT/row['path']).read_bytes()
        results.append({'path':row['path'],'rebuild':'PASS','target':ident(current)})
    assert len(results)==9
    put('diff-checks.json',{'results':results})
    delivery_checks=json.loads((DEL.parent/'checks.json').read_text());sources=[]
    for row in delivery_checks['sources']:
        path=row['path'];b=(REF/path).read_bytes()
        assert ident(b)=={k:row[k] for k in ('sha256','bytes')}
        assert b==subprocess.check_output(['git','-C',str(REF),'show',COMMIT+':'+path])
        sources.append({'path':path,**ident(b),'pinned_blob_match':True})
    put('source-checks.json',{'reference_commit':COMMIT,'sources':sources})
    wp23=(ROOT/'specs/pokemon-rules/wp23-shadow-hyper-and-purification.md').read_text()
    ids=re.findall(r'^\| (W\d+) \|',wp23,re.M)
    assert ids==['W'+f'{i:02}' for i in range(1,47)]
    wp32path='specs/pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md'
    a=(PREV/'input-snapshot'/wp32path).read_text().splitlines();b=(ROOT/wp32path).read_text().splitlines()
    changed=[i+1 for i,(x,y) in enumerate(zip(a,b)) if x!=y]
    assert len(a)==len(b) and changed==[214]
    current_summary=ROOT/'review/wp22-wp23-wp32-delivery-2026-09-30/delivery-summary.md'
    section=current_summary.read_text().split('## 3.',1)[1].split('## 4.',1)[0]
    stale=[];checked=[]
    for line in section.splitlines():
        m=re.search(r'\[([^]]+)\]\(([^)]+)\).*?`([a-f0-9]{64})`，([\d,]+)字节',line)
        if not m:continue
        label,path,h,size=m.groups();actual=ident((current_summary.parent/path).read_bytes())
        row={'path':str((current_summary.parent/path).relative_to(ROOT)),'recorded':{'sha256':h,'bytes':int(size.replace(',',''))},'actual':actual}
        checked.append(row)
        if row['recorded']!=actual:stale.append(row)
    assert len(stale)==2
    put('current-summary-checks.json',{'checked':checked,'stale_current_references':stale})
    before={r['path']:r for r in json.loads((PREV/'input-manifest.json').read_text())['inputs']}
    history=[]
    history_section=(ROOT/'planning/review-manifest-2026-09-19.md').read_text().split('\n## 3.',1)[1].split('\n## 4.',1)[0]
    for line in history_section.splitlines():
        if not line.startswith('| `') or '第七十一轮' not in line or '留史' not in line:continue
        path=re.match(r'\| `([^`]+)`',line)[1]
        if path not in before:continue
        quoted=re.findall(r'`([a-f0-9]{64})`',line)
        sizes=re.findall(r'（([\d,]+)字节',line)
        if not quoted:continue
        assert quoted[0]==before[path]['sha256'],path
        if sizes:assert int(sizes[0].replace(',',''))==before[path]['bytes'],path
        if len(quoted)>1:
            assert quoted[-1]==ident((ROOT/path).read_bytes())['sha256'],path
        history.append(path)
    links=0
    for p in [ROOT/'specs/pokemon-rules/wp23-shadow-hyper-and-purification.md']:
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
            if '://' in target or target.startswith('#'):continue
            assert (p.parent/target.split('#')[0]).exists(),target
            links+=1
    for p in DEL.glob('*.json'):json.loads(p.read_text())
    status=subprocess.check_output(['git','-C',str(REF),'status','--porcelain'],text=True)
    head=subprocess.check_output(['git','-C',str(REF),'rev-parse','HEAD'],text=True).strip()
    assert head==COMMIT and status==''
    put('review-checks.json',{'date':'2026-10-01','decision':'REQUEST_CHANGES','current_manifest_rows':1015,'TSV_rows':919,'fixed_inputs_and_snapshots_unchanged':len(inputs['inputs']),'diff_reconstructions':9,'source_blob_matches':len(sources),'WP23_scenarios':len(ids),'WP32_only_changed_line':214,'round71_history_inputs_checked':len(history),'round71_paths':history,'current_summary_stale_reference_count':len(stale),'current_links_checked':links,'reference_head':head,'reference_status':status,'method':'Text/hash/JSON/diff checks and static source reading; no reference execution.'})
    print(json.dumps({'inputs':len(inputs['inputs']),'diffs':9,'sources':len(sources),'WP23_scenarios':46,'round71_history_inputs':len(history),'summary_stale_refs':2,'links':links}))
if __name__=='__main__':main()
