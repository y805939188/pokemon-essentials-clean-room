"""Reviewer-owned v3 targeted-review text/hash checks; no reference execution."""
from pathlib import Path
import hashlib,json,re,subprocess
OUT=Path(__file__).resolve().parent
PREV=OUT.parent/'recheck-v2'
ROOT=OUT.parent.parent.parent
DELIVERY=ROOT/'review/wp66bc-wp71-delivery-2026-09-30'
REV=DELIVERY/'revision-v3'
REF=ROOT/'reference/pokemon-essentials'
COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def ident(b): return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def put(name,data): (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def rebuild(original, diff):
    """Reconstruct a single UTF-8 unified diff in memory, with exact context checks."""
    src = original.decode().splitlines(keepends=True)
    lines = diff.decode().splitlines(keepends=True)
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
                assert src[cursor] == line[1:]
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
    fixed=json.loads((OUT/'input-manifest.json').read_text())
    for row in fixed['inputs']:
        expected={k:row[k] for k in ('sha256','bytes')}
        assert ident((ROOT/row['path']).read_bytes())==expected,row['path']
        assert ident((OUT/'input-snapshot'/row['path']).read_bytes())==expected
    for row in fixed['external_inputs_verified']:
        assert ident(Path(row['path']).read_bytes())=={k:row[k] for k in ('sha256','bytes')}
    bindings=json.loads((REV/'diff-bindings.json').read_text())['bindings']
    results=[]
    for row in bindings:
        original=(PREV/'input-snapshot'/row['path']).read_bytes()
        assert ident(original)==row['from_snapshot']
        rebuilt=rebuild(original,(REV/row['diff']).read_bytes())
        assert ident(rebuilt)==row['to_current']
        assert rebuilt==(ROOT/row['path']).read_bytes()
        results.append({'path':row['path'],'result':'PASS','to':ident(rebuilt)})
    assert len(results)==10
    put('diff-checks.json',{'reconstructions':results})
    source_rows=json.loads((DELIVERY/'source-identities.json').read_text())['sources']
    assert len(source_rows)==21
    source_checks=[]
    for row in source_rows+[{'path':'PBS/types.txt'}]:
        path=row['path'];data=(REF/path).read_bytes()
        assert data==subprocess.check_output(['git','-C',str(REF),'show',COMMIT+':'+path])
        if 'sha256' in row:
            assert ident(data)=={k:row[k] for k in ('sha256','bytes')}
        source_checks.append({'path':path,**ident(data),'pinned_blob_match':True})
    put('source-checks.json',{'reference_commit':COMMIT,'sources':source_checks,'read_scope':'See reading-log.md; hash checks are not full-file semantic review.'})
    bounds=json.loads((DELIVERY/'boundary-checks.json').read_text())
    count=0
    def check_bound(value):
        nonlocal count
        if isinstance(value,dict):
            if all(k in value for k in ('receiver','sha256','bytes')):
                assert ident((ROOT/value['receiver']).read_bytes())=={k:value[k] for k in ('sha256','bytes')}
                count+=1
            for child in value.values(): check_bound(child)
        elif isinstance(value,list):
            for child in value: check_bound(child)
    check_bound(bounds)
    assert count==9
    package_fixed=json.loads((REV/'wp66c-fixed.json').read_text())
    for row in package_fixed['artifacts']:
        assert ident((ROOT/row['path']).read_bytes())=={k:row[k] for k in ('sha256','bytes')}
    scenarios={}
    for name,prefix,total in [('wp66-b-storage-and-pokedex-ui.md','B',39),('wp66-c-bag-item-storage-and-shop-ui.md','C',36),('wp71-tile-puzzles.md','T',21)]:
        ids=re.findall(r'^\| ('+prefix+r'\d+) \|',(ROOT/'specs/ui'/name).read_text(),re.M)
        assert ids==[prefix+f'{i:02}' for i in range(1,total+1)]
        scenarios[name]=len(ids)
    for path in list(DELIVERY.glob('*.json'))+list(REV.glob('*.json')):
        json.loads(path.read_text())
    head=subprocess.check_output(['git','-C',str(REF),'rev-parse','HEAD'],text=True).strip()
    status=subprocess.check_output(['git','-C',str(REF),'status','--porcelain'],text=True)
    assert head==COMMIT and status==''
    put('review-checks.json',{'date':'2026-10-01','mechanical_status':'PASS','behavior_status':'PASS_SCOPED','fixed_current_inputs_unchanged':len(fixed['inputs']),'snapshot_inputs_unchanged':len(fixed['inputs']),'external_inputs_unchanged':len(fixed['external_inputs_verified']),'diff_reconstructions':len(results),'source_blob_matches':len(source_checks),'delivery_source_rows':21,'boundary_bindings':count,'current_fixed_artifacts_match':True,'scenarios':scenarios,'reference_head':head,'reference_status':status,'method':'Reviewer-owned text/hash/JSON/diff checks; no reference execution.'})
    print(json.dumps({'mechanical':'PASS','inputs':len(fixed['inputs']),'diffs':len(results),'sources':len(source_checks),'bindings':count,'scenario_count':sum(scenarios.values())}))
if __name__=='__main__':main()
