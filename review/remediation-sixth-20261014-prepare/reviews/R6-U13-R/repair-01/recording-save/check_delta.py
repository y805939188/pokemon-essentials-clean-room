import collections
import datetime
import difflib
import hashlib
import json
import pathlib
import re
import subprocess

ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
OWN=ROOT/'review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/repair-01/recording-save'
NEW='9971fe84896786645cdcda3ab45e5caf7785cabc'
OLD='00b45de642f07cee9953e42f04cce9c35d77346f'
REVIEW='3ef4854ef43eac92fd1dc57350e4cf6aa160082b'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PREFIX='review/remediation-sixth-20261014-prepare/'
E=PREFIX+'candidates/R6-U13/evidence/'
M=PREFIX+'candidates/R6-U13/mirror/'
TEST=M+'deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def raw(commit,path):return git('show',commit+':'+path)
def doc(commit,path):return json.loads(raw(commit,path))
def identity(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())

assert git('rev-parse',NEW+'^{tree}').decode().strip()=='93ebe95d038954fd0dfb14fd07ac2f95a2485baf'
manifest=doc(NEW,E+'candidate-manifest.json')
mirrors=[]
for r in manifest:
    p=r['candidate_path'];new=raw(NEW,p);old=raw(OLD,p)
    mirrors.append(dict(path=p,old=identity(old),new=identity(new),bytes_equal=new==old,
                        manifest_identity_equal=identity(new)==r['candidate'],
                        mode_type_blob=git('ls-tree',NEW,'--',p).decode().strip()))
assert all(r['manifest_identity_equal'] for r in mirrors)
changed=[r['path'] for r in mirrors if not r['bytes_equal']]
assert changed==[TEST]
a,b=raw(OLD,TEST),raw(NEW,TEST)
left,right=a.splitlines(keepends=True),b.splitlines(keepends=True)
assert len(left)==len(right)==274
different=[i+1 for i,(x,y) in enumerate(zip(left,right)) if x!=y]
assert different==[40]
assert a.split(b'## BP\xef\xbc\x9a',1)[1]==b.split(b'## BP\xef\xbc\x9a',1)[1]
old_columns=left[39].decode().split('|');new_columns=right[39].decode().split('|')
assert len(new_columns)==5 and new_columns[1].strip()=='SF30'
assert all(new_columns[i].strip().startswith(old_columns[i].strip()) for i in (2,3))
ids=re.findall(r'^\| (SF\d+) \|',b.decode(),re.M)
counts=collections.Counter(ids)
assert len(ids)==len(counts)==40 and all(v==1 for v in counts.values())
assert ids==[f'SF{i:02d}' for i in range(1,41)]
(OWN/'mirror-diff.patch').write_text(''.join(difflib.unified_diff(a.decode().splitlines(True),b.decode().splitlines(True),fromfile=OLD+':'+TEST,tofile=NEW+':'+TEST,n=3)))

old_hist,new_hist=doc(OLD,E+'historical-regression.json'),doc(NEW,E+'historical-regression.json')
history=[]
for before,after in zip(old_hist['R5_exact_scopes_read'],new_hist['R5_exact_scopes_read']):
    d=raw(after['source_commit'],after['source_path'])
    history.append(dict(id=after['id'],qualified_scope_unchanged=before['qualified_scope']==after['qualified_scope'],
                        identity=identity(d),fixed_path_identity_equal=all(identity(d)[k]==after[k] for k in identity(d)),
                        earlier_path_absence_inference_withdrawn='inference is withdrawn' in after['retrieval_note'],
                        original_failure_cause=after['retrieval_transition']['original_failure_cause']))
assert all(r['qualified_scope_unchanged'] and r['fixed_path_identity_equal'] for r in history)
old_ledger=[json.loads(s) for s in raw(REVIEW,PREFIX+'reviews/R6-U13-R/recording-save/reading-ledger.jsonl').decode().splitlines()]
source_binding=[]
for path,length,intervals in [('Data/Scripts/002_Save data/003_SaveData_Conversion.rb',223,[[1,223]]),
                              ('Data/Scripts/002_Save data/005_Game_SaveConversions.rb',420,[[1,210],[211,420]])]:
    loc=REF+':'+path;records=[r for r in old_ledger if r.get('locator')==loc]
    covered={n for r in records for n in range(r['presented_range'][0],r['presented_range'][1]+1)}
    d=raw(REF,path);ident=identity(d)
    assert covered==set(range(1,length+1)) and all(all(r[k]==ident[k] for k in ident) for r in records)
    source_binding.append(dict(commit=REF,path=path,**ident,old_review=REVIEW,
                               old_presented_intervals=[r['presented_range'] for r in records],
                               full_old_range_bound=True,new_full_semantic_reread=False,
                               reuse_basis='Same reviewer, same immutable source, no source/contract delta; parent authorized exact qualified reuse.'))
assert raw(OLD,PREFIX+'contracts/R6-U13.json')==raw(NEW,PREFIX+'contracts/R6-U13.json')
tool=doc(NEW,E+'tool-validation.json')
assert tool['probability_factor_semantics_proved_by_this_tool'] is False
assert tool['expected_constants_not_computed']=={'h24_m0_factor':30,'h24_m1_factor':30}
assert all(len(v['raw_ids'])==v['raw_row_count'] and len(set(v['raw_ids']))==v['unique_id_count'] and not v['duplicate_counts'] for v in tool['raw_catalogue_rows'])
assert not any(tool[k] for k in ['reference_execution','behavior_model_execution','writer_execution','host_execution'])
delta=doc(NEW,E+'repair-01/delta-manifest.json');delta_matches=[]
for r in delta['changed_payloads_except_this_manifest']:
    matches=identity(raw(NEW,r['path']))==r['after']
    if r['before'] is not None:matches=matches and identity(raw(OLD,r['path']))==r['before']
    delta_matches.append(dict(path=r['path'],bound=True,exact=matches))
assert all(r['exact'] for r in delta_matches)
metadata_paths=git('diff','--name-only',OLD,NEW,'--',E).decode().splitlines()
metadata_diff=git('diff','--unified=2',OLD,NEW,'--',E)
(OWN/'metadata-diff.patch').write_bytes(metadata_diff)
result=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),cwd=str(ROOT),new_candidate=NEW,
            new_tree='93ebe95d038954fd0dfb14fd07ac2f95a2485baf',old_candidate=OLD,old_review=REVIEW,
            mirrors=mirrors,changed_mirrors=changed,different_physical_lines=different,
            all_other_273_lines_byte_equal=True,non_SF_suffix_byte_equal=True,
            old_SF30_menu_input_and_expectation_prefix_preserved=True,
            raw_SF_count=len(ids),unique_SF_count=len(counts),raw_SF_ids=ids,
            source_qualification_binding=source_binding,R5_metadata_only_recovery=history,
            delta_manifest_checks=delta_matches,metadata_delta_paths=metadata_paths,
            constant_factor_30_is_expected_value_not_tool_computed=True,
            metadata_tool_corrections_match=True,source_execution=False,
            author_script_execution=False,behavior_model=False,real_save_load=False,
            semantic_verdict='Separate human/model static report; document checks do not prove semantic preservation.')
(OWN/'delta-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='DOCUMENT_CHECK_PASS',mirror_delta=changed,changed_lines=different,
                     source_bindings=len(source_binding),SF_raw=len(ids),SF_unique=len(counts),
                     delta_payloads_checked=len(delta_matches)),ensure_ascii=False))
