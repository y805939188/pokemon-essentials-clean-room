"""Qualified historical payload and old-clause preservation; never transfers verdicts."""
import concurrent.futures, datetime, hashlib, json, pathlib, subprocess, urllib.parse, urllib.request
ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
OWN=pathlib.Path(__file__).resolve().parent
ACTUAL='86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
OLD_REVIEW='4be1e586fcbe2416c33ede333430e5f2918f3cae'
PREFIX='review/remediation-sixth-20261014-prepare/'
REF=ROOT/(PREFIX+'reviews/R6-U04-R/.scratch/reference.git')
def stamp():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args,repo=ROOT):return subprocess.check_output(['git','-C',str(repo),*args])
def load(c,p):return json.loads(git('show',c+':'+p))
def save(p,j):(OWN/p).write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
def ident(d):return dict(bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest())
begin=stamp()
reuse=[]
old=git('show',OLD_REVIEW+':'+PREFIX+'reviews/R6-U04-R/reading-ledger.jsonl').decode().splitlines()
for number,line in enumerate(old,1):
 r=json.loads(line)
 repo=REF if '/reference.git' in r['repository'] else ROOT
 d=git('show',r['commit']+':'+r['path'],repo=repo)
 same=all(ident(d)[k]==r[k] for k in ['bytes','sha256','git_blob'])
 assert same
 reuse.append(dict(prior_ledger_row=number,commit=r['commit'],path=r['path'],identity=ident(d),prior_start=r['start'],prior_end=r['end'],prior_json_key=r['json_key'],identity_equal=True,
                   boundary='Same reviewer same-session earlier reading at exact immutable payload; no prior candidate verdict or runtime claim transferred; these ranges are not new actual reads.'))
save('same-session-reading-reuse.json',dict(prior_review_commit=OLD_REVIEW,prior_ledger_path=PREFIX+'reviews/R6-U04-R/reading-ledger.jsonl',rows=reuse,level='IDENTITY_VERIFIED_READING_REUSE_ONLY'))
spans=[]
u02=load('e34925c2857204bd013033b8cb22b62e839ea7aa',PREFIX+'reviews/R6-U02-R/verification.json')['historical_spans']
for r in u02:
 old=git('show',r['historical_commit']+':'+r['path']).decode().splitlines(keepends=True)
 a,b=r['historical_lines'];text=''.join(old[a-1:b])
 now=git('show',ACTUAL+':'+r['path']).decode()
 lines=[x for x in text.splitlines() if x.strip()]
 contiguous=text.rstrip('\n') in now
 contained=all(x in now for x in lines)
 spans.append(dict(origin='U02 historical span',id=r['id'],path=r['path'],historical_commit=r['historical_commit'],historical_lines=[a,b],old_span_sha256=hashlib.sha256(text.encode()).hexdigest(),prior_declared_sha256=r['span_sha256'],continuous_old_span_preserved=contiguous,all_old_nonblank_lines_preserved=contained,source_rows_are_navigation_not_new_game_PASS=True))
 assert contained
u05=load('77681decbc0d6382b71d3238c4244f5a39fc0264',PREFIX+'reviews/R6-U05-R/historical-span-checks.json')
for r in u05:
 now=git('show',ACTUAL+':'+r['formal_path']).decode()
 text=r['full_old_span'];lines=[x for x in text.splitlines() if x.strip()]
 # Shared WP40 appends an Arena boundary to an existing paragraph. Retain the
 # entire old sentence sequence, rather than claiming identical full paragraphs.
 contained=all(x in now for x in lines)
 ordered=0
 units=lines if contained else [s+'。' if n<len(line.split('。'))-1 else s for line in lines for n,s in enumerate(line.split('。')) if s.strip()]
 for unit in units:
  i=now.find(unit,ordered)
  assert i>=0, (r['historical_scope_consumer'],r['formal_path'],unit)
  ordered=i+len(unit)
 spans.append(dict(origin='U05 historical span',id=r['historical_scope_consumer'],path=r['formal_path'],qualified_fixed_record=r['candidate_clause'],historical_lines=r['formal_lines'],old_span_sha256=hashlib.sha256(text.encode()).hexdigest(),continuous_old_span_preserved=text in now,all_old_nonblank_lines_preserved=contained,old_sentence_order_preserved=True,new_game_PASS=False))
save('historical-clause-preservation.json',dict(actual_commit=ACTUAL,spans=spans,count=len(spans),continuous_count=sum(x['continuous_old_span_preserved'] for x in spans),boundary='Mechanical old clause preservation only. Report gives bounded semantic collision assessment; no fresh global historical verdict.'))
selected=load('64c77cf1733ab7db300e9f5ac7c79a2886c8ac68',PREFIX+'candidates/R6-U05/evidence/selected-historical-scopes.json')
fixed='c0ff33024aea424c68d29f9778fe7c8e807d21e8'
scratch=OWN/'.scratch';scratch.mkdir(exist_ok=True)
def fetch(path):
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+fixed+'/'+urllib.parse.quote(path,safe='/')
 started=stamp()
 with urllib.request.urlopen(url,timeout=30) as r:d=r.read();status=r.status
 (scratch/path.rsplit('/',1)[1]).write_bytes(d)
 return path,d,dict(commit=fixed,path=path,url=url,http_status=status,utc_start=started,utc_end=stamp(),identity=ident(d),full_remote_bytes_read=True,behavior_execution=0)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: fetched=list(pool.map(fetch,sorted({r['bound_identity']['path'] for r in selected})))
raw={p:json.loads(d) for p,d,m in fetched}
qualified=[]
for i,r in enumerate(selected):
 b=r['bound_identity'];v=raw[b['path']]
 for key in b['pointer'].strip('/').split('/'):v=v[int(key)] if isinstance(v,list) else v[key]
 digest=hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 projection={k:v[k] for k in b['scope_keys']}
 assert projection==r['qualification'],i
 assert digest==b['record_sha256'],(i,digest,b['record_sha256'])
 qualified.append(dict(index=i,id=r['id'],record_key=r['record_key'],owner=r['owner'],binding=b,canonical_record_sha256=digest,exact_scope_projection_equal=True,whole_ID_or_old_verdict_reused=False))
save('qualified-historical-bindings.json',dict(utc_start=begin,utc_end=stamp(),remote_payloads=[m for p,d,m in fetched],selected_count=len(qualified),qualified=qualified,scope_semantic_boundary='41 projections mechanically bound only. New reading is limited to relevant combat/AI fields and exact partial owner tuples; reports and frozen qualification are navigation, not current-game PASS.'))
print(json.dumps(dict(reused_ledger_rows=len(reuse),historical_spans=len(spans),continuous_spans=sum(x['continuous_old_span_preserved'] for x in spans),qualified_exact_projections=len(qualified),reference_execution=0),ensure_ascii=False))
