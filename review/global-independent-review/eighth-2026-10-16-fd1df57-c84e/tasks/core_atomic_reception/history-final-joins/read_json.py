import pathlib,json,hashlib,datetime,subprocess,sys,uuid
P=pathlib.Path(__file__).resolve().parent;f=pathlib.Path(sys.argv[1]).resolve();pointers=sys.argv[2:]or[''];b=f.read_bytes();d=json.loads(b);selected=[]
for pointer in pointers:
 x=d
 for key in pointer.strip('/').split('/')if pointer else[]:x=x[int(key)]if isinstance(x,list)else x[key.replace('~1','/').replace('~0','~')]
 selected.append(dict(pointer=pointer,complete_object=x))
q=P/'io'/('read-'+uuid.uuid4().hex+'.json');r=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),actual_receiver='/root/core_atomic_reception',path=str(f),parent_bytes=len(b),parent_sha256=hashlib.sha256(b).hexdigest(),selected=selected,qualification='Selection output/identity only until actually read completely in tooloutput; no raw-source FULL or historicalpurpose credit automatically granted.');q.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False,indent=2));print('CAPTURE',q.name)
