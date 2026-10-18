"""Restore only resource review materials from fixed local gzip transport.
No network, imports from evidence, or restored program execution. Destination must
not exist. Verify encoded and decoded bytes, SHA256 and Git content identity.
"""
from pathlib import Path
import datetime, gzip, hashlib, io, json

ROOT = Path('/workspace/pokemon-essentials-clean-room')
OUT = ROOT / 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/preflight_resources'
TRANSPORT = ROOT / 'review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core'
DEST = OUT / 'recovered-resource-evidence'
def ident(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'git_blob_content_id': hashlib.sha1(('blob %d\0' % len(data)).encode()+data).hexdigest()}
def relative(value):
    path=Path(value)
    if path.is_absolute() or '..' in path.parts or not path.parts: raise ValueError(value)
    return path
def main():
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    index=json.loads((TRANSPORT/'payload-index.json').read_text())
    objects={x['transport_path']: x for x in index['compressed_objects']}
    selected=[e for e in index['logical_files'] if e['logical_path'].startswith(('temporary/binary-tools/','tasks/R7-M17/','tasks/R7-M18/','tasks/R7-D09/')) and not any(w in e['logical_path'] for w in ['events.jsonl','logs/','commands/'])]
    DEST.mkdir(exist_ok=False)
    receipt=[]
    for row in selected:
        path=relative(row['logical_path']); transport=relative(row['transport_path']); encoded=(TRANSPORT/transport).read_bytes(); obj=objects[str(transport)]
        assert len(encoded)==obj['transport_bytes']
        assert hashlib.sha256(encoded).hexdigest()==obj['transport_sha256']
        with gzip.GzipFile(fileobj=io.BytesIO(encoded),mode='rb') as stream: decoded=stream.read(row['bytes']+1)
        actual=ident(decoded)
        for key,value in actual.items(): assert row[key]==value,(str(path),key)
        target=DEST/path; target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(decoded)
        receipt.append({'logical_path':str(path),'transport_path':str(transport),**actual,'status':'RESTORED_EXACT_BYTES','semantic_reading_credit':False})
    result={'schema':'r8.local-resource-restore.v1','start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'fixed_transport_commit':'fd1df570cad987dc3852a3b958f03916e317f7fe','destination':str(DEST),'files':receipt,'count':len(receipt),'bytes':sum(x['bytes'] for x in receipt),'semantic_reading_credit':False,'programs_executed':0}
    (OUT/'resource-recovery-receipt.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['count','bytes','destination','programs_executed']}))
if __name__=='__main__': main()
