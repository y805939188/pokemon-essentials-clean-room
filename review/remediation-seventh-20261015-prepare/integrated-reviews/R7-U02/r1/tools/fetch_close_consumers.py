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
    ('Data/Scripts/016_UI/022_UI_MoveRelearner.rb', '407545d2f6b2710f67426c9ee9f809477a411b25'),
    ('Data/Scripts/016_UI/023_UI_PurifyChamber.rb', 'db36770ee7bcc05db8bbeb67ce2f6159980f5d5c'),
    ('Data/Scripts/018_Alternate battle modes/001_Battle Frontier/005_UI_BattleSwap.rb', '13f193a0f3bbc64d4cc440702d73618d56b67f21'),
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
(root/'close-consumers-receipt.json').write_text(json.dumps(receipts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipts,ensure_ascii=False))
