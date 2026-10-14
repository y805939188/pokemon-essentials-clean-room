import sys,json,hashlib,datetime
from pathlib import Path
root=Path(__file__).resolve().parent
path=Path(sys.argv[1]); data=path.read_bytes(); obj=json.loads(data)
selector=sys.argv[2] if len(sys.argv)>2 else ''
for key in selector.split('/') if selector else []:
    obj=obj[int(key)] if isinstance(obj,list) else obj[key]
dictionary={}
def intern(value):
    if isinstance(value,dict):
        if ('sha256' in value and 'git_blob' in value) or 'payload_identity' in value:
            encoded=json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'))
            key=hashlib.sha256(encoded.encode()).hexdigest()[:16]
            dictionary[key]=value
            return {'exact_dictionary_ref':key}
        return {k:intern(v) for k,v in value.items()}
    if isinstance(value,list): return [intern(v) for v in value]
    return value
out=intern(obj)
record=dict(path=str(path),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),selector=selector or 'FULL_OBJECT',emitted_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),method='Exact full selected JSON subtree; repeated identities losslessly interned, no summary or omitted fields')
with (root/'json-readings.jsonl').open('a') as f: f.write(json.dumps(record,ensure_ascii=False)+'\n')
print(json.dumps(record,ensure_ascii=False)); print(json.dumps({'complete_selected_object':out,'exact_dictionary':dictionary},ensure_ascii=False,separators=(',',':')))
