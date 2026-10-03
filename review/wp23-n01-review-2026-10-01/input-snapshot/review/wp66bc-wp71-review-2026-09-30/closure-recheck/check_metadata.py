"""Reviewer-owned final identity and registration verification; text only."""
from pathlib import Path
import json,hashlib,re,difflib,subprocess
OUT=Path(__file__).resolve().parent
ROOT=OUT.parent.parent.parent
PREV=OUT.parent/'closure-review'
DEL=ROOT/'review/wp66bc-wp71-delivery-2026-09-30/closure-metadata-fix'
def ident(b):return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def put(p,v):(OUT/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
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

def unified_exact(a,b,fromfile,tofile):
    parts=difflib.unified_diff(a.decode().splitlines(True),b.decode().splitlines(True),fromfile=fromfile,tofile=tofile)
    output=[]
    for line in parts:
        output.append(line)
        if not line.endswith('\n'):
            output.append('\n\\ No newline at end of file\n')
    return ''.join(output)

def main():
    fixed=json.loads((OUT/'input-manifest.json').read_text())
    for r in fixed['inputs']:
        want={k:r[k] for k in ('sha256','bytes')}
        assert ident((ROOT/r['path']).read_bytes())==want
        assert ident((OUT/'input-snapshot'/r['path']).read_bytes())==want
    expected=json.loads((PREV/'history-identity-audit.json').read_text())['rows']
    corrections=json.loads((DEL/'identity-corrections.json').read_text())
    bad={(r['round'],r['path']):r for r in expected if r['errors']}
    good={(r['round'],r['path']):r for r in expected if not r['errors']}
    got={(r['round'],r['path']):r for r in corrections['corrections']}
    assert len(got)==len(corrections['corrections'])==18 and set(got)==set(bad)
    assert {(r['round'],r['path']) for r in corrections['originally_correct_rows']}==set(good)
    measured_bad=measured_good=0
    for key,r in bad.items():
        row=got[key]
        for side in ['before','after']:
            want=r['expected_'+side]
            assert row['actual_'+side]==want
            if want is None:continue
            assert row[side+'_snapshot']==r[side+'_snapshot']
            assert ident((ROOT/r[side+'_snapshot']).read_bytes())==want
            measured_bad+=1
    for r in good.values():
        for side in ['before','after']:
            want=r['expected_'+side]
            if want is not None:
                assert ident((ROOT/r[side+'_snapshot']).read_bytes())==want
                measured_good+=1
    assert measured_bad==35 and measured_good==32
    manifest=(ROOT/'planning/review-manifest-2026-09-19.md').read_text()
    section=manifest.split('### 3.1 历史身份勘误',1)[1].split('\n## 4.',1)[0]
    table=[]
    for line in section.splitlines():
        if not line.startswith('| 第'):continue
        key=(int(re.search(r'第(\d+)轮',line)[1]),re.search(r'`([^`]+)`',line)[1])
        assert key in bad
        hashes=re.findall(r'`([a-f0-9]{64})`',line)
        sizes=[int(v.replace(',','')) for v in re.findall(r'／([\d,]+)',line)]
        r=bad[key]
        wanted=[r['expected_before']]+([r['expected_after']] if r['expected_after'] else [])
        assert hashes==[x['sha256'] for x in wanted],key
        assert sizes==[x['bytes'] for x in wanted],key
        table.append(key)
    assert len(table)==len(set(table))==18 and set(table)==set(bad)
    assert '原历史行保留' in section and '下表取代' in section
    for r in expected:assert r['recorded_line'] in manifest
    summary=(ROOT/'review/wp66bc-wp71-delivery-2026-09-30/delivery-summary.md').read_text()
    assert re.search(r'v3 摘要 `([a-f0-9]{64})`',summary)[1]=='edd48222503490a2ab3084e252e56173545ac1e44c2e0e4f4f11d449b8d3bb3c'
    put('history-layer-checks.json',{'status':'PASS','error_rows_covered_exactly':18,'corrected_identities_matched':35,'excluded_manifest_self_output':1,'previously_correct_rows_preserved':17,'previously_correct_identities_matched':32,'excluded_original_manifest_self_outputs':2,'original_history_rows_preserved':35,'manifest_errata_matches_exactly':True,'summary_history_correct':True})
    stage_results=[]
    (OUT/'stage-registration-diffs').mkdir(exist_ok=True)
    for r in json.loads((DEL/'diff-bindings.json').read_text())['bindings']:
        original=(PREV/'input-snapshot'/r['path']).read_bytes()
        assert ident(original)==r['from_snapshot']
        stage=rebuild(original,(DEL/r['diff']).read_bytes())
        assert ident(stage)==r['to_current']
        final=(ROOT/r['path']).read_bytes()
        result={'path':r['path'],'submitted_target':ident(stage),'actual_final':ident(final),'submitted_diff_rebuilds_target':True,'target_is_final':stage==final}
        if stage!=final:
            name=Path(r['path']).name+'.diff'
            tail=unified_exact(stage,final,'registered-stage/'+r['path'],'final/'+r['path'])
            (OUT/'stage-registration-diffs'/name).write_text(tail)
            assert rebuild(stage,tail.encode())==final
            result['registration_tail_diff']='stage-registration-diffs/'+name
        stage_results.append(result)
    assert sum(r['target_is_final'] for r in stage_results)==1
    for r in json.loads((OUT/'final-bindings.json').read_text())['bindings']:
        original=(PREV/'input-snapshot'/r['path']).read_bytes()
        assert ident(original)==r['before']
        (OUT/r['diff']).write_text(unified_exact(original,(ROOT/r['path']).read_bytes(),'a/'+r['path'],'b/'+r['path']))
        result=rebuild(original,(OUT/r['diff']).read_bytes())
        assert result==(ROOT/r['path']).read_bytes() and ident(result)==r['after']
    put('diff-stage-checks.json',{'submitted_diffs_rebuild':3,'submitted_target_is_final':1,'submitted_targets_are_registration_stages':2,'reviewer_exact_final_diff_reconstructions':3,'records':stage_results,'treatment':'Submitted manifest/TSV target hashes are before their own diff artifacts were registered. Reviewer final diffs and final-bindings fix the actual final version; no input files rewritten.'})
    links=0
    for p in [DEL/'response.md',ROOT/'review/wp66bc-wp71-delivery-2026-09-30/delivery-summary.md']:
        for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
            if '://' in link or link.startswith('#'):continue
            assert (p.parent/link.split('#')[0]).exists(),link
            links+=1
    for p in DEL.glob('*.json'):json.loads(p.read_text())
    put('review-checks.json',{'decision':'PASS_SCOPED','CLOSURE-R01':'CLOSED','current_fixed_inputs_and_snapshots_unchanged':len(fixed['inputs']),'manifest_current_rows':991,'TSV_current_rows':895,'history_error_rows_covered':18,'history_corrected_values_matched':35,'historical_good_rows_preserved':17,'historical_good_values_matched':32,'final_diffs_rebuilt':3,'submitted_stage_diffs_rebuilt':3,'current_links_checked':links,'specifications_and_matrix_unchanged':True,'original_14_items':'CLOSED unchanged'})
    print(json.dumps({'CLOSURE-R01':'CLOSED','corrected_values':35,'good_values':32,'final_diffs':3,'submitted_stage_diffs':3,'links':links}))
if __name__=='__main__':main()
