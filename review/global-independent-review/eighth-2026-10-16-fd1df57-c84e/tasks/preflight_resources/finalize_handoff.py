"""Freeze precise handoff metadata and final readonly protection observations."""
from pathlib import Path
import datetime,hashlib,json,subprocess
O=Path(__file__).resolve().parent;B=Path('/workspace/pokemon-essentials-clean-room');R=Path('/workspace/pokemon-essentials')
BC='fd1df570cad987dc3852a3b958f03916e317f7fe';RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
sha=lambda b:hashlib.sha256(b).hexdigest()
save=lambda p,v:(O/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
records=[]
def command(argv,binary=False):
 start=now();p=subprocess.run(argv,capture_output=True);end=now()
 base=O/'evidence'/('final-protection-'+str(len(records)).zfill(3))
 base.with_suffix('.stdout').write_bytes(p.stdout);base.with_suffix('.stderr').write_bytes(p.stderr)
 records.append(dict(argv=argv,start_utc=start,end_utc=end,exit=p.returncode,stdout=str(base.with_suffix('.stdout').relative_to(O)),stderr=str(base.with_suffix('.stderr').relative_to(O)),stdout_bytes=len(p.stdout),stdout_sha256=sha(p.stdout)))
 assert p.returncode==0,argv
 return p.stdout
assert command(['git','-C',str(B),'rev-parse',BC+':deliverables/final-specification-set']).decode().strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
assert command(['git','-C',str(B),'diff','--name-only',BC,'--','deliverables/final-specification-set','planning','audit','AGENTS.md'])==b''
assert command(['git','-C',str(R),'status','--porcelain=v1','--untracked-files=all'])==b''
identities=json.loads((O/'source-identities.json').read_text())
for path,row in identities.items():
 data=(R/path).read_bytes();assert sha(data)==row['sha256']
 frozen=command(['git','-C',str(R),'show',RC+':'+path],binary=True)
 assert data==frozen
save('evidence/final-protection-records.json',records)
index=json.loads((O/'handoff/readset-index.json').read_text())
nav=[]
for repo,commit,path in [
 (R,RC,'mkxp.json'),(R,RC,'Data/Scripts/001_Technical/004_Input.rb'),
 (R,RC,'Data/Scripts/016_UI/001_Non-interactive UI/002_UI_Controls.rb'),
 (B,BC,'deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md'),
 (B,BC,'deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md')]:
 data=subprocess.run(['git','-C',str(repo),'show',commit+':'+path],check=True,capture_output=True).stdout
 nav.append(dict(repo=str(repo),commit=commit,path=path,bytes=len(data),sha256=sha(data),lines=len(data.splitlines()),qualification='Frozen consumer/formal navigation candidate; this is not a complete caller denominator or a new semantic read receipt'))
index['frozen_consumer_formal_navigation']=nav
index['current_decoder_identity']={'path':'freeze_controller_string_readset.py','bytes':(O/'freeze_controller_string_readset.py').stat().st_size,'sha256':sha((O/'freeze_controller_string_readset.py').read_bytes())}
index['controller_readset_identity']={'path':'handoff/controller-readset.json','bytes':(O/'handoff/controller-readset.json').stat().st_size,'sha256':sha((O/'handoff/controller-readset.json').read_bytes())}
index['totals']={key:sum(x['counts'].get(key,0)for x in index['strings'])for key in ['ascii','utf-16-le-ascii-subset','UNREAD_FINITE_STRING_CANDIDATE','CONTAINED_IN_PREVIOUSLY_FULL_READ_UNIT','CONTAINED_IN_PREVIOUSLY_READ_NONPROGRAM_UNIT','CONTAINED_IN_NEWLY_READ_FINITE_SCAN_CANDIDATE']}
index['totals']['finite_candidates']=index['totals']['ascii']+index['totals']['utf-16-le-ascii-subset']
save('handoff/readset-index.json',index)
ledger=json.loads((O/'reading-ledger.json').read_text());ledger['updated_utc']=now()
ledger['rows'].append(dict(owner='/root/preflight_resources',repo='R',path='5PE finite ASCIImin4 and UTF16LE-ASCII-subsetmin4 candidate inventory',evidence_level='TOOL_VALIDATION',reading_status='STRUCTURE_INVENTORIED_NOT_FULL_READ',structural_units=index['totals'],accepted=False,remarks='Exact rule inventory and precise UNREAD freeze only. Existing units keep their individual full-read receipts; all unreceived candidates remain available readable candidates, including incidental machine bytes; not L04. Handoff prompt delegates complete new reception.'))
save('reading-ledger.json',ledger)
findings=json.loads((O/'findings.json').read_text());findings['unread_readable'].append('Finite min4 ASCII/UTF16LE-ASCII-subset inventory has255158 unreceived candidates of260161 total. Includes incidental printable machine bytes; not every candidate is a real string. Classification and actual text semantics remain UNREAD, not L04.')
save('findings.json',findings)
manifest=[]
for p in sorted((O/'handoff').iterdir()):
 if p.is_file()and p.name!='manifest.json':manifest.append(dict(path=str(p.relative_to(O)),bytes=p.stat().st_size,sha256=sha(p.read_bytes())))
save('handoff/manifest.json',dict(created_utc=now(),files=manifest,current_decoder=index['current_decoder_identity'],requested_config=index['requested_configuration'],actual_config=index['actual_configuration'],qualification='Frozen exact bytes for parent-managed new context; no inherited semantic acceptance. Failed-first artifacts remain incomplete/not accepted.'))
progress=json.loads((O/'progress.json').read_text());progress['status']='DELIVERED_WITH_OPEN_READ_ITEMS';progress['updated_utc']=now();progress['update_started']=False
progress['outputs']+=['handoff/readset-index.json','handoff/controller-readset.json','handoff/next-context-prompt.md','handoff/manifest.json','evidence/final-protection-records.json']
progress['remaining']=['parent-assigned new-context complete1666controller and finite string/metadata reception','resource_media_serialized font/SF2/messages semantic reception','full actual downstream/formal denominator reception','independent non-proposer counterreview/acceptance','opaque native CFG/selector and named host limits remain qualified']
progress['handoff_status']='FROZEN_READSET_READY_FOR_PARENT_ASSIGNMENT';progress['actual_execution_note']='Task behavior0; own first static readset extractor interrupted and preserved; optimized v2 exit0. Global executions managed by root.'
save('progress.json',progress)
print(json.dumps(dict(status=progress['status'],finite_string_totals=index['totals'],ledger_rows=len(ledger['rows']),source_identities=len(identities),readset='handoff/readset-index.json',behavior_executions=0),ensure_ascii=False))
