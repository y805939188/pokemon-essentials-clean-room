"""Finite positive/corrupt-fixture tests for actual remote byte readback."""
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

TOOL=Path(__file__).with_name('remote_readback.py')
def blob(raw): return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def ident(raw): return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'git_blob_content_id':blob(raw)}
def git(repo,*args):
    return subprocess.check_output(['git','-c','user.name=R7 isolated tool fixture','-c','user.email=r7-tool-fixture.invalid@example.invalid','-c','commit.gpgsign=false','-C',str(repo),*args],stderr=subprocess.STDOUT).decode().strip()
with tempfile.TemporaryDirectory(prefix='r7-readback-test-') as temp:
    root=Path(temp); repo=root/'fixture'; repo.mkdir(); git(repo,'init')
    prefix=repo/'report/publication-transport/core';prefix.mkdir(parents=True)
    raw=b'finite fixture\x00\xff\n'; enc=gzip.compress(raw,mtime=0); (prefix/'objects').mkdir(); (prefix/'objects/a.gz').write_bytes(enc)
    e={**ident(raw),'logical_path':'finite-data.bin','transport_path':'objects/a.gz','encoding':'gzip'}
    obj={'sha256':e['sha256'],'transport_path':'objects/a.gz',**{'transport_'+k:v for k,v in ident(enc).items()}}
    index={'schema':'r7.lossless-report-transport.v1','logical_files':[e,{**e,'logical_path':'duplicate.bin'}],'compressed_objects':[obj]}
    ip=prefix/'payload-index.json'; ip.write_text(json.dumps(index)+'\n');(repo/'report/summary.md').write_text('Fixture only.\n')
    git(repo,'add','report');git(repo,'commit','-m','isolated readback fixture')
    commit=git(repo,'rev-parse','HEAD');branch=git(repo,'branch','--show-current')
    def check(label,expected):
        argv=[sys.executable,str(TOOL),'--remote',str(repo),'--branch',branch,'--commit',git(repo,'rev-parse','HEAD'),'--report-root','report','--bare-dir',str(root/(label+'-bare')),'--output',str(root/(label+'.json'))]
        p=subprocess.run(argv,capture_output=True)
        assert p.returncode==expected,(label,p.stdout,p.stderr)
        return p
    check('positive',0);receipt=json.loads((root/'positive.json').read_bytes())
    assert receipt['counts']=={'physical_files':3,'logical_files':2,'unique_decoded_payloads':1}
    index['logical_files'][0]['sha256']='0'*64; ip.write_text(json.dumps(index)+'\n');git(repo,'add','report');git(repo,'commit','-m','isolated corrupt index fixture')
    p=check('corrupt',1); assert b'KeyError' in p.stderr or b'mismatch' in p.stderr
    print(json.dumps({'tool_validation':'PASS','positive_full_remote_members':3,'positive_logical':2,'duplicate_content_preserved':True,'corrupt_index_rejected':True,'reference_or_model_execution':0,'fixture_directory_temporary_and_removed':str(root)}))
