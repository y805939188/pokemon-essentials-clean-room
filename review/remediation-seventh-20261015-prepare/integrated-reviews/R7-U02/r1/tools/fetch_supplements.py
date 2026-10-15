import datetime
import hashlib
import json
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

root = Path(__file__).resolve().parents[1]
dest = Path('/workspace/r7-ir-R7-U02/supplemental')
dest.mkdir(exist_ok=True)
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
rows = [
    ('Data/Scripts/003_Game processing/003_Interpreter.rb', '21666002e7f4038dd3763b632538becaae5f8d7d'),
    ('Data/Scripts/003_Game processing/004_Interpreter_Commands.rb', '58167231199f1cb8bdc499a61f5ada544d3f7616'),
    ('Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb', 'e8be64d69b3bcb02def7a0cc09c0a5d4027cc628'),
]
receipts = []
for path, blob in rows:
    url = 'https://raw.githubusercontent.com/Maruno17/pokemon-essentials/'+R+'/'+urllib.parse.quote(path)
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with urllib.request.urlopen(url, timeout=40) as response:
        data = response.read(100000)
        status = response.status
    actual = hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
    assert actual == blob
    target = dest/path
    target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():
        assert target.read_bytes() == data
    else:
        target.write_bytes(data)
    receipts.append(dict(repository='Maruno17/pokemon-essentials',commit=R,path=path,url=url,http_status=status,start_utc=start,
                         end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=actual,local_path=str(target)))
(root/'supplemental-receipt.json').write_text(json.dumps(receipts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipts,ensure_ascii=False))
