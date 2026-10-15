"""Read only named immutable transport members; never execute restored programs."""
import concurrent.futures, datetime, gzip, hashlib, json, pathlib, urllib.request

DEST = pathlib.Path('/workspace/r7-context/R7-U10-reviewer/supplements')
AUTHOR = pathlib.Path('/workspace/r7-review-input/R7-U10-r1-583330fb69935ff6b2eb32ca11ede6c23bde5ecd/candidate/candidates/R7-U10/evidence/author')
OUT = pathlib.Path(__file__).parent
C2 = '4580645dfbfec4a3c7ccbad56ae293cc619b0d25'

def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'git_blob_content_id': hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}

def one(row):
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+C2+'/review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/'+row['transport_path']
    target = DEST / row['logical_path']
    if target.exists():
        data = target.read_bytes()
        transport = {'reuse': True}
    else:
        with urllib.request.urlopen(url, timeout=40) as response:
            encoded = response.read(2000001)
            status = response.status
        assert len(encoded) <= 2000000
        encoded_id = identity(encoded)
        assert encoded_id['git_blob_content_id'] == row['encoded_git_blob']
        data = gzip.decompress(encoded)
        transport = {'http_status': status, 'encoded_identity': encoded_id}
    actual = identity(data)
    assert all(actual[key] == row[key] for key in actual)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        with target.open('xb') as stream: stream.write(data)
    return {'local_path': str(target), 'logical_path': row['logical_path'], 'url': url, **actual, 'transport': transport, 'start_utc': start, 'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'semantic_credit': False}

if __name__ == '__main__':
    rows = json.loads((AUTHOR/'supplement-recovery-receipt.json').read_bytes())['files']
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(one, rows))
    result = {'schema': 'r7.u10.reviewer.named-supplement-reception.v1', 'files': results, 'count': len(results), 'bytes': sum(r['bytes'] for r in results), 'execution': 'TRANSPORT_ONLY; no restored program executed', 'selection_qualification': 'Named C06 body/EH displays from independent counter-review plus nested original bindings; author receipt used only as transport locator, each immutable decoded identity independently verified.'}
    (OUT/'supplement-reception.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'count': result['count'], 'bytes': result['bytes']}))
