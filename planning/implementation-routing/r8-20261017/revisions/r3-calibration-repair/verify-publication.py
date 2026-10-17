#!/usr/bin/env python3
"""Fresh remote-only full-byte readback of the published routing candidate."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
INV = HERE.parents[1]
ROOT = INV.parents[2]
PREFIX = str(INV.relative_to(ROOT)) + '/'
BASE = 'c0f62d973180679134f2eb1a488c1dc359c8658f'
BRANCH = 'codex/r8-r3-seven-line-recovery-20261017'
URL = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'


def identity(data):
    try:
        lines = len(data.decode().splitlines())
    except UnicodeDecodeError:
        lines = None
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'lines':lines,
            'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sha',required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    assert len(args.sha)==40 and all(c in '0123456789abcdef' for c in args.sha)
    commands=[]
    def run(argv,cwd,input=None):
        start=datetime.datetime.now(datetime.timezone.utc).isoformat()
        done=subprocess.run(argv,cwd=cwd,input=input,capture_output=True)
        commands.append({'argv':argv,'started_utc':start,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                         'exit_code':done.returncode,'stdin_sha256':hashlib.sha256(input).hexdigest() if input else None,
                         'stdout_bytes':len(done.stdout),'stdout_sha256':hashlib.sha256(done.stdout).hexdigest(),
                         'stderr':done.stderr.decode(errors='replace')})
        done.check_returncode()
        return done.stdout
    result={'schema_version':'routing-r3-repair-remote-full-readback.v1','candidate':args.sha,
            'base_candidate':BASE,'branch':BRANCH,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'acquisition':'New remote-only shallow blob-filtered clone; no local alternates or shared objects.'}
    with tempfile.TemporaryDirectory(prefix='r3-remote-readback-') as tmp:
        tmp=Path(tmp)
        run(['git','clone','--quiet','--filter=blob:none','--depth=1','--single-branch','--branch',BRANCH,'--no-checkout',URL,'remote'],tmp)
        fresh=tmp/'remote'
        assert not (fresh/'.git/objects/info/alternates').exists()
        assert run(['git','rev-parse','HEAD'],fresh).decode().strip()==args.sha
        commit=run(['git','cat-file','commit',args.sha],fresh).decode()
        assert [l.split()[1] for l in commit.split('\n\n')[0].splitlines() if l.startswith('parent ')]==[BASE]
        tree=run(['git','ls-tree','-r',args.sha,'--',PREFIX.rstrip('/')],fresh).decode().splitlines()
        records=[]
        for line in tree:
            meta,path=line.split('\t',1);mode,kind,blob=meta.split();assert kind=='blob'
            records.append({'path':path,'mode':mode,'blob':blob})
        # Explicit blob wants hydrate the entire bounded routing directory in one transfer.
        wants=''.join(oid+'\n' for oid in sorted({r['blob'] for r in records})).encode()
        run(['git','-c','fetch.negotiationAlgorithm=noop','fetch','--quiet','--filter=blob:none','--no-tags','--no-write-fetch-head','origin','--stdin'],fresh,wants)
        requests=''.join(r['blob']+'\n' for r in records).encode()
        raw=run(['git','cat-file','--batch'],fresh,requests)
        offset=0;contents={};files=[]
        for row in records:
            end=raw.index(b'\n',offset);header=raw[offset:end].decode().split();oid,kind,size=header;size=int(size)
            assert oid==row['blob'] and kind=='blob'
            data=raw[end+1:end+1+size];offset=end+1+size
            assert raw[offset:offset+1]==b'\n';offset+=1
            info=identity(data);assert info['git_blob']==row['blob']
            assert data==(ROOT/row['path']).read_bytes(),row['path']
            contents[row['path']]=data
            files.append({'path':row['path'],'mode':row['mode'],**info,'local_bytes_equal':True})
        assert offset==len(raw)
        manifest_name=PREFIX+'candidate-file-manifest.json'
        manifest=json.loads(contents[manifest_name])
        assert {r['path'] for r in manifest['files']}==set(contents)-{manifest_name}
        for row in manifest['files']:
            assert identity(contents[row['path']])=={k:row[k] for k in ['bytes','sha256','lines','git_blob']}
        formal=run(['git','rev-parse',args.sha+':deliverables/final-specification-set'],fresh).decode().strip()
        assert formal=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
        before=json.loads(contents[PREFIX+'revisions/r3-calibration-repair/pre-publication-protection.json'])['remote_before_publication']
        refs=run(['git','ls-remote','origin','refs/heads/main','refs/heads/codex/r8-disposition-tagging-20261017','refs/heads/'+BRANCH],fresh).decode().splitlines()
        remote={line.split('\t')[1]:line.split('\t')[0] for line in refs}
        assert all(remote[k]==v for k,v in before.items())
        assert remote['refs/heads/'+BRANCH]==args.sha
        result.update(files=files,total_files=len(files),total_bytes=sum(r['bytes'] for r in files),
                      candidate_identity_manifest_including_self_fully_read=True,
                      all_remote_and_local_file_bytes_equal=True,all_candidate_manifest_entries_match=True,
                      new_commit_parent_exactly_c0=True,formal_tree=formal,main_and_original_author_refs_unchanged=True,
                      remote_after_publication=remote,commands=commands,all_passed=True,
                      completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['files','commands']},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
