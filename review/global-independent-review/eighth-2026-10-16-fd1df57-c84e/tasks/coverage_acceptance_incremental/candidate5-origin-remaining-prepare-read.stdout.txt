"""Local static readset verification only. No target code or imported audit tool."""
import collections,datetime,gzip,hashlib,json,pathlib,subprocess,struct
ROOT=pathlib.Path(__file__).resolve().parent
REPORT=ROOT.parent.parent
REPO=REPORT.parents[2]
R=pathlib.Path('/workspace/pokemon-essentials')
def sha(b): return hashlib.sha256(b).hexdigest()
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(n,x): (ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def ident(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
start=utc()
contract=json.loads((REPORT/'delegation/readsets/binary_remaining_texts.json').read_text())
ids=[]
for row in contract['files']:
 p=REPORT/row['path'];b=p.read_bytes();assert len(b)==row['bytes'] and sha(b)==row['sha256'],row
 item=ident(p)
 if p.suffix=='.gz':
  raw=gzip.decompress(b);name=p.name[:-3];(ROOT/name).write_bytes(raw)
  item['decompressed']={'path':str(ROOT/name),'bytes':len(raw),'sha256':sha(raw),'lines':len(raw.splitlines())}
 ids.append(item)
for path in ['inputs/eighth-global-review-prompt.md','inputs/review-SKILL.md','delegation/prompts/binary_remaining_texts.md','delegation/readsets/binary_remaining_texts.json']:
 ids.append(ident(REPORT/path))
ids.append(ident(REPO/'AGENTS.md'))
texts=[json.loads(l) for l in (ROOT/'remaining-text-readset.jsonl').read_text().splitlines()]
unread=[json.loads(l) for l in (ROOT/'remaining-unread.jsonl').read_text().splitlines()]
assert len(texts)==41849 and len(unread)==57948
refs={r['candidate_id']:t for t in texts for r in t['refs']};assert len(refs)==57948
raws={p:(R/p).read_bytes() for p in ['Game.exe','x64-msvcrt-ruby310.dll','zlib1.dll']}
for row in unread:
 raw=raws[row['path']][row['start']:row['end_exclusive']]
 assert len(raw)==row['bytes'] and sha(raw)==row['sha256']
 assert raw.decode('ascii' if row['encoding']=='ascii' else 'utf-16-le')==refs[row['candidate_id']]['text']
for p,b in raws.items():
 item=ident(R/p);item['git']=subprocess.check_output(['git','-C',str(R),'ls-tree','HEAD',p],text=True).strip();ids.append(item)
pe={}
for p,b in raws.items():
 h=struct.unpack_from('<I',b,60)[0];assert b[h:h+4]==b'PE\0\0'
 n=struct.unpack_from('<H',b,h+6)[0];optsize=struct.unpack_from('<H',b,h+20)[0];o=h+24
 assert struct.unpack_from('<H',b,o)[0]==0x20b
 sections=[]
 for i in range(n):
  s=o+optsize+40*i;name=b[s:s+8].split(b'\0')[0].decode();vs,va,sz,ptr=struct.unpack_from('<IIII',b,s+8)
  sections.append({'name':name,'virtual_size':vs,'rva':va,'bytes':sz,'offset':ptr,'end':ptr+sz,'flags':hex(struct.unpack_from('<I',b,s+36)[0])})
 pe[p]={'image_base':struct.unpack_from('<Q',b,o+24)[0],'section_table':o+optsize,'sections':sections}
dump('identities.json',{'schema':'gr8.binary.remaining.identities/v1','created_utc':utc(),'identities':ids,'fixed':contract,'original_bytes_verified':57948,'report_head_at_start':subprocess.check_output(['git','-C',str(REPO),'rev-parse','HEAD'],text=True).strip()})
dump('pe-sections.json',pe)
groups=collections.defaultdict(list)
for row in unread:groups[(row['path'],row['section'],row['start']//100000)].append(row)
summary=[]
for (p,s,g),rows in groups.items():
 summary.append({'path':p,'section':s,'range100k':g,'count':len(rows),'start':min(r['start'] for r in rows),'end':max(r['end_exclusive'] for r in rows)})
dump('navigation-buckets.json',summary)
dump('progress.json',{'schema':'gr8.binary.remaining.progress/v1','logical_task':'/root/binary_remaining_texts','status':'RUNNING','start_utc':start,'updated_utc':utc(),'readsets_verified':True,'full_finite_occurrences':57948,'distinct_texts':41849,'semantically_received':0,'requested_config':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'Fast off'},'actual_config':dict.fromkeys(['model','effort','tier','speed','platform_uuid'],'UNVERIFIED'),'business_vectors':'NOT_EXECUTED','business_execution_count':0,'update_status':'UPDATE_NOT_STARTED'})
print(json.dumps({'start_utc':start,'end_utc':utc(),'identities_verified':len(ids),'candidate_bytes_verified':57948,'sections':pe,'buckets':summary},ensure_ascii=False))
