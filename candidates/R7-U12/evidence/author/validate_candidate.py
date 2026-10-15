"""Author-only bounded identity/navigation checks. Never executes reference code."""
import json
from pathlib import Path
import posixpath
import re
from build_candidate import B, H, R, PREFIX, ERRATA, ROOT, OUT, EVID, git, identity, dump

def links(path, text, names):
    rows = []
    for number, line in enumerate(text.splitlines(), 1):
        for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', line):
            label, target = match.groups()
            if '://' in target or target.startswith('#'):
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), target.split('#')[0]))
            isdir = any(n.startswith(resolved + '/') for n in names)
            rows.append({'source': path, 'line': number, 'label': label, 'target': target,
                'resolved': resolved, 'is_directory': isdir, 'exists': resolved in names or isdir,
                'working_exists': (ROOT / resolved).exists()})
    return rows

def main():
    contract = json.loads((EVID / 'frozen-contract.json').read_bytes())
    plan = json.loads((EVID / 'recovery-plan.json').read_bytes())
    names = set(git('ls-tree', '-r', '--name-only', B).decode().splitlines())
    frozen = Path('/workspace/r7-context/R7-U12-author')
    verified = []
    for row in plan['artifacts'] + plan['evidence'] + plan['fixed_read_inputs']:
        actual = identity((frozen / row['local_path']).read_bytes())
        assert all(actual[k] == row[k] for k in ('bytes', 'sha256'))
        assert actual['git_blob'] == row['git_blob_content_id']
        verified.append({'local_path': row['local_path'], **actual})
    dump(EVID / 'restored-input-recheck.json', {'files': verified, 'semantic_credit': False})
    # Verify each complete-contract raw-byte pointer against the restored original payload.
    raw = {p.stem: p.read_bytes() for p in (frozen / 'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs').glob('*.raw')}
    checked = {}
    def walk(v):
        if isinstance(v, dict):
            if 'input_sha256' in v and 'raw_member_byte_offsets' in v:
                h = v['input_sha256']; start, end = v['raw_member_byte_offsets']
                assert h in raw
                d = raw[h][start:end]
                assert len(d) == v['raw_member_bytes'] and identity(d)['sha256'] == v['raw_member_sha256']
                checked[(h,start,end)] = {k:v[k] for k in ('input_sha256','raw_member_byte_offsets','raw_member_bytes','raw_member_sha256')}
            for x in v.values(): walk(x)
        elif isinstance(v, list):
            for x in v: walk(x)
    walk(contract)
    dump(EVID / 'raw-binding-recheck.json', {'status':'EXACT_RAW_MEMBER_SLICES_VERIFIED', 'members':list(checked.values())})
    originals = []; successors = []; occurrence_diffs = []
    baseline = json.loads((EVID / 'mirror-identities.json').read_bytes())
    for record in baseline['files']:
        path = record['path']; data = (OUT/path).read_bytes()
        assert identity(data) == record['new']
        if path == ERRATA: continue
        original = git('show', B + ':' + path)
        if path.startswith('deliverables/'):
            old = links(path, original.decode(), names); new = links(path, data.decode(), names)
            originals += old; successors += new
            old_missing = [r for r in old if not r['exists']]
            new_hrefs = re.findall(r'\]\((https://raw\.githubusercontent\.com/[^)]+)\)', data.decode())
            assert len(new_hrefs) == len(old_missing)
            for row in old_missing:
                url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/' + H + '/' + row['resolved']
                assert url in new_hrefs and not (ROOT/row['resolved']).exists()
                occurrence_diffs.append({**row, 'new_immutable_target':url})
            # Only the ten destination strings and one named retrieval note per file may differ.
            restored = data.decode()
            restored = re.sub(r'^GR7-M19-001 历史导航勘误：.*\n\n', '', restored, flags=re.M)
            for row in old_missing:
                restored = restored.replace('https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/' + H + '/' + row['resolved'], row['target'])
            assert restored.encode() == original
        else:
            before=original.splitlines(keepends=True); after=data.splitlines(keepends=True)
            assert len(before)==len(after)
            changed=[i+1 for i,(a,b) in enumerate(zip(before,after)) if a!=b]
            expected=553 if path.startswith('planning/') else 1828
            assert changed==[expected]
            a=before[expected-1].decode(); b=after[expected-1].decode()
            new='WP72 §5.3／WP27（当前导航勘误：[GR7-H08-001](../'+ERRATA+')）'
            assert b.replace(new,'WP72 §5.2／WP27')==a
    assert len(originals)==136 and sum(x['exists'] for x in originals)==126
    assert len(occurrence_diffs)==10 and len({r['resolved'] for r in occurrence_diffs})==4
    assert len(successors)==126 and all(x['exists'] for x in successors)
    directory=[r for r in originals if r['target']=='user-interface/']
    assert len(directory)==1 and directory[0]['exists'] and directory[0]['is_directory']
    family=[r for r in originals if r['source'].endswith('test-catalog/README.md') and '/' not in r['target'] and r['target'].endswith('.md')]
    assert len(family)==17 and all(r['exists'] for r in family)
    controls={}
    for path,line in [('README.md',7),('CURRENT-DELIVERY.md',5),('delivery/2026-10-14-sixth/README.md',7)]:
        data=git('show',B+':'+path)
        rows=links(path,data.decode(),names); selected=[r for r in rows if r['line']==line]
        assert selected and all(r['exists'] for r in selected)
        assert (ROOT/path).read_bytes()==data
        controls[path]={'line':line,'links':selected,'file':identity(data)}
    dump(EVID/'navigation-check.json',{'stage':'TOOL_VALIDATION; no browser or reference execution',
        'baseline_local_inline_destinations':136,'baseline_resolved':126,'baseline_missing':10,
        'baseline_unique_missing':4,'candidate_local_inline_destinations':126,'candidate_resolved':126,
        'candidate_immutable_hrefs':10,'candidate_unique_immutable_targets':4,
        'ten_replacements':occurrence_diffs,'baseline_all_parsed_links':originals,
        'candidate_all_parsed_local_links':successors,'directory_control':directory,
        'seventeen_family_links':family,'ordinary_controls':controls,
        'limits':'Bounded inline Markdown destination parser, accepts Git-tree directories; fragments, other syntaxes, browser presentation, all131 bodies not audited.',
        'old_attempt':'Preserved original 012 exit1 (11/5 error), 013 exit0 corrected 10/4; never run old scripts.'})
    preserve_paths=['deliverables/final-specification-set/demo-dx/wp72-debug-contexts-and-controls.md',
        'deliverables/final-specification-set/creature-rpg/wp27-bag-and-item-storage.md',
        'deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md',
        'review/remediation-sixth-20261014-prepare/integration/public-sync-20261014/sync-input.json',
        'review/remediation-sixth-20261014-prepare/contracts/R6-U08.json',
        'review/remediation-sixth-20261014-prepare/completion/final-delivery.json']
    preservation=[]
    for path in preserve_paths:
        data=git('show',B+':'+path); assert (ROOT/path).read_bytes()==data
        preservation.append({'path':path,'commit':B,**identity(data),'result':'EXACT_BASELINE_BYTES_UNCHANGED'})
    # Whole historical R6 directory is unchanged: tree identity plus worktree/index diff.
    history_path='review/remediation-sixth-20261014-prepare'
    unchanged=git('diff',B,'--',history_path)
    assert not unchanged
    r6tree=git('rev-parse',B+':'+history_path).decode().strip()
    errata=json.loads((OUT/ERRATA).read_bytes())
    assert errata['current_label']=='WP72 §5.3／WP27' and errata['old_label']=='WP72 §5.2／WP27'
    assert errata['current_clause']['rule_line']==124
    source=[]
    for row in plan['fixed_read_inputs']:
        if row['commit']==R:
            source.append({'commit':R,'path':row['path'],**identity((frozen/row['local_path']).read_bytes()),
                           'read_lines':[[778,797]] if 'MenuCommands' in row['path'] else [[81,93],[263,281]],
                           'stage':'SOURCE_STATIC','execution':'NOT_EXECUTED'})
    dump(EVID/'history-preservation.json',{'files':preservation,'frozen_R6_subtree':{'commit':B,'path':history_path,'tree':r6tree,'worktree_and_index_diff_from_B':''},
        'source_ranges':source,'formal131_tree':git('rev-parse',B+':deliverables/final-specification-set').decode().strip(),
        'formal_files':len([n for n in names if n.startswith('deliverables/final-specification-set/')]),
        'unchanged_formal':git('diff',B,'--','deliverables/final-specification-set').decode(),
        'note':'Tree/hash proves identity preservation, not full R6 semantic re-approval. No all-nine-supplement semantic reading claimed.'})
    dump(EVID/'validation-summary.json',{'status':'AUTHOR_TOOL_CHECKS_SATISFIED_NOT_INDEPENDENT_REVIEW',
        'restored_files':len(verified),'raw_member_slices':len(checked),'mirrors':6,
        'B_links':{'local_inline':136,'resolved':126,'missing_occurrences':10,'missing_targets':4},
        'candidate_links':{'local_resolved':126,'local_missing':0,'immutable_occurrences':10,'immutable_targets':4},
        'catalog_families':17,'formal_documents_unchanged':131,'reference_execution':0,'host_execution':0,
        'model_execution':0,'Demo_native_media_real_save_replay':0,'effective_configuration':'UNVERIFIED'})
    print((EVID/'validation-summary.json').read_text(),end='')

if __name__=='__main__':
    main()
