"""Identity, exact reuse and contribution joins only; no reference code execution."""
import datetime
import difflib
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path('/workspace/r6-actual-c')
OUT = pathlib.Path(__file__).parent
ACT = '86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
PRIOR = '9d5b4e99b617828690e6529b77a1e555d7c9eb1b'
PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
BASE = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PREFIX = 'review/remediation-sixth-20261014-prepare/'
OWN = PREFIX + 'actual-reviews/group-C/'
OLD_REVIEW = '44e3b725850315c8f050fcdd8cb1e88d5bd5c5ec'
OLD_DIR = PREFIX + 'reviews/R6-U07-R/'

def git(*args, reference=False):
    argv = ['git', '--git-dir=/tmp/r6-u07-reference.git'] if reference else ['git', '-C', str(ROOT)]
    return subprocess.check_output(argv + list(args))

def blob(commit, path, reference=False):
    return git('show', commit + ':' + path, reference=reference)

def identity(raw):
    return {'bytes':len(raw), 'sha256':hashlib.sha256(raw).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}

def write(name, value):
    (OUT / name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def main():
    inp_path = PREFIX+'integration/U01-U14-final-composite-20261014/actual-review-input.json'
    inp_raw = blob(ACT,inp_path)
    inp = json.loads(inp_raw)
    assert inp == json.loads(pathlib.Path('/tmp/group-c-final-actual-input.json').read_bytes())
    binding = {'actual_commit':ACT,'workspace_tree':git('rev-parse',ACT+'^{tree}').decode().strip(),
               'formal_tree':git('rev-parse',ACT+':deliverables/final-specification-set').decode().strip(),
               'actual_input':{'path':inp_path,**identity(inp_raw)},
               'preparation_commit':PREP,'baseline_commit':BASE,'reference_commit':REF,
               'reference_tree':git('rev-parse',REF+'^{tree}',reference=True).decode().strip(),
               'prior_actual_commit':PRIOR,'prior_actual_is_not_this_signature':True,
               'AGENTS':{'path':'AGENTS.md',**identity(blob(ACT,'AGENTS.md'))},
               'requested_configuration':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'default','fast':False},
               'actual_configuration':{k:'UNVERIFIED' for k in ['model','effort','tier','speed','task_uuid']},
               'configuration_cli_probes':0,'subagents':0,
               'logical_reviewer':'R6 independent actual group-C; prior R6-U07-R',
               'declared_reviewer_thread':'01a13acf-046d-764f-b8fb-1ea14dcf6002',
               'runtime_thread_echo':'UNVERIFIED',
               'not_any_selected_author':True,
               'write_directory':OWN,
               'source_execution':0,'behavior_model_execution':0,'host_execution':0,'Demo_execution':0,
               'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    assert binding['workspace_tree']=='67e8c55d520fa8cad2928cb4b95e24c3ed602d5a'
    assert binding['formal_tree']=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
    write('binding.json',binding)

    joins=[]
    primary_ids=[]
    for batch in inp['batches']:
        if batch['batch'] not in ['R6-U06','R6-U07','R6-U08','R6-U09','R6-U14']:continue
        con_raw=blob(PREP,batch['contract_path']);con=json.loads(con_raw)
        assert identity(con_raw)==batch['contract_identity']
        if batch['batch']!='R6-U14':primary_ids+=con['required_ids']
        for path in batch['all_candidate_allowlist_paths']:
            a=blob(BASE,path).decode().splitlines(True)
            candidate_path=PREFIX+'candidates/'+batch['batch']+'/mirror/'+path
            b=blob(batch['candidate_published_commit'],candidate_path).decode().splitlines(True)
            c=blob(ACT,path).decode()
            added=[line for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes()
                   if tag!='equal' for line in b[k:l] if line.strip()]
            missing=[line for line in added if line not in c]
            joins.append({'batch':batch['batch'],'path':path,'candidate_commit':batch['candidate_published_commit'],
                          'candidate_path':candidate_path,'baseline':identity(''.join(a).encode()),
                          'candidate':identity(''.join(b).encode()),'actual':identity(c.encode()),
                          'candidate_added_nonempty_lines':len(added),'exactly_surviving_added_lines':len(added)-len(missing),
                          'changed_by_other_contributor_or_editorial_join':missing,
                          'mechanical_only_not_semantic_verdict':True})
    assert len(primary_ids)==19 and len(set(primary_ids))==19
    write('merged-contribution-checks.json',{'primary_ids':primary_ids,'rows':joins,
          'boundary':'Exact line retention is navigation. All ID semantic conclusions are manual in per-id-review.json.'})

    prior_coverage=json.loads(blob(OLD_REVIEW,OLD_DIR+'execution-and-read-coverage.json'))
    reused_sources=[]
    for row in prior_coverage['source_full_reads']:
        current=identity(blob(REF,row['path'],reference=True))
        assert current=={k:row['identity'][k] for k in current}
        reused_sources.append({'path':row['path'],'identity':current,'prior_complete_root_read':row,
                               'reason':'Same direct reviewer, same fixed reference blob; re-evaluated against final actual prose, not transferred candidate signature.'})
    pairs=json.loads(blob(OLD_REVIEW,OLD_DIR+'paired-document-identities.json'))
    reused_documents=[]
    for pair in pairs[1:]:
        original=blob('6f6521983006519a0b55a5414177c71a2b59810e',pair['candidate'])
        assert identity(original)=={'bytes':pair['candidate_bytes'],'sha256':pair['candidate_sha256'],'git_blob':pair['candidate_blob']}
        actual=blob(ACT,pair['baseline'])
        a=original.decode().splitlines(True);b=actual.decode().splitlines(True)
        matching=[];edits=[];reconstructed=[]
        for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
            if tag=='equal':
                assert a[i:j]==b[k:l]
                matching.append({'prior_lines':[i+1,j],'actual_lines':[k+1,l],
                                 'bytes':len(''.join(a[i:j]).encode()),'sha256':hashlib.sha256(''.join(a[i:j]).encode()).hexdigest()})
                reconstructed.extend(a[i:j])
            else:
                edits.append({'kind':tag,'prior_lines':[i+1,j],'actual_lines':[k+1,l],
                              'actual_text_sha256':hashlib.sha256(''.join(b[k:l]).encode()).hexdigest()})
                reconstructed.extend(b[k:l])
        assert ''.join(reconstructed).encode()==actual
        patch=''.join(difflib.unified_diff(a,b,fromfile='prior-directly-fully-read-U07-mirror',tofile=ACT+':'+pair['baseline'],n=5))
        name=pathlib.Path(pair['baseline']).stem+'-reuse-delta.patch'
        (OUT/name).write_text(patch)
        reused_documents.append({'path':pair['baseline'],'prior_identity':identity(original),'actual_identity':identity(actual),
                                 'prior_full_read_evidence':pair,'same_full_file_reconstructed':True,
                                 'matched_full_text_ranges':matching,'novel_actual_ranges':edits,'complete_novel_read_patch':name,
                                 'manual_read':'Entire bounded patch and full shared context considered; all actual lines either identical to prior personally fully read text or included in fully read delta.'})
    write('shared-full-read-reuse.json',{'prior_fixed_review':OLD_REVIEW,'prior_coverage_path':OLD_DIR+'execution-and-read-coverage.json',
          'sources':reused_sources,'documents':reused_documents,'old_verdict_transfer':False})

    journal=[json.loads(x) for x in (OUT/'read-journal.jsonl').read_text().splitlines()]
    identities={}
    for row in journal:
        key=(row['commit'],row['path'])
        if key not in identities:identities[key]={'commit':row['commit'],'path':row['path'],**{k:row[k] for k in ['bytes','sha256','git_blob']},'displayed_requested_spans':[]}
        identities[key]['displayed_requested_spans'].append({'role':row['role'],'mode':row['mode'],'span':row['span']})
    write('read-identities.json',{'rows':list(identities.values()),
          'boundary':'Journal requests are not automatic complete-reading or semantic PASS. Report records truncations and recovery; only expressly attested continuous/full reuse scopes count.'})
    print(json.dumps({'primary_ids':len(primary_ids),'joined_files':len(joins),'missing_exact_added_lines':sum(len(x['changed_by_other_contributor_or_editorial_join']) for x in joins),'read_identity_rows':len(identities)},ensure_ascii=False))
    for x in joins:
        if x['changed_by_other_contributor_or_editorial_join']:print(json.dumps({k:x[k] for k in ['batch','path','changed_by_other_contributor_or_editorial_join']},ensure_ascii=False))

if __name__=='__main__':main()
