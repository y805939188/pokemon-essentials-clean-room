import pathlib,sys,json,hashlib,subprocess,datetime
R=pathlib.Path('/workspace/reference-pokemon-essentials-B07'); C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
assert subprocess.check_output(['git','-C',str(R),'rev-parse','HEAD']).decode().strip()==C
p=sys.argv[1];b=(R/p).read_bytes();lines=b.decode().splitlines(); ranges=[]
for v in sys.argv[2:]:
 a,z=map(int,v.split('-'));z=min(z,len(lines));ranges.append([a,z]);print(p,a,z)
 for i in range(a-1,z):print(f'{i+1}: {lines[i]}')
r={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':C,'path':p,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'file_lines':len(lines),'opened_ranges':ranges,'operation':'read text only'}
with open('/tmp/b08-r07-actual-reading.jsonl','a') as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
