"""Byte membership and frozen-packet identities only; no reference evaluation."""
import datetime,hashlib,json,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5];OUT=Path(__file__).resolve().parent
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';CORE='5210b009db5191f307301115845e31475cd798ef'
BASE='review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/'
def blob(ref,path):return subprocess.check_output(['git','show',ref+':'+path],cwd=ROOT)
def identity(ref,path):
    b=blob(ref,path);meta=subprocess.check_output(['git','ls-tree',ref,'--',path],cwd=ROOT,text=True).split()
    return dict(commit=ref,path=path,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=meta[2],mode=meta[0],type=meta[1])
def offsets(haystack,needle):
    result=[];pos=0
    while True:
        pos=haystack.find(needle,pos)
        if pos<0:return result
        result.append(pos);pos+=1
srcpath='Data/Scripts/012_Overworld/001_Overworld.rb'
source=blob(R,srcpath).splitlines()[680]
literal=source.split(b'_INTL("',1)[1].split(b'",',1)[0]
assert literal.count(bytes([92,92,110]))==1
collected=literal.replace(bytes([92,110]),bytes([10])).replace(bytes([92,92]),bytes([92]))
runtime=literal.replace(bytes([92,92]),bytes([92]))
bare=runtime.replace(bytes([92,110]),bytes([10]))
dat=blob(R,'Data/messages_core.dat')
membership={k:dict(separator=sep,needle_bytes=len(v),needle_sha256=hashlib.sha256(v).hexdigest(),offsets=offsets(dat,v)) for k,v,sep in [('collected',collected,[92,10]),('runtime',runtime,[92,110]),('bare_lf',bare,[10])]}
assert membership['collected']['offsets']==[798247,798325]
assert membership['runtime']['offsets']==membership['bare_lf']['offsets']==[]
newline=dict(method='TOOL_VALIDATION: bounded lexical byte transformation and membership; no Marshal decoding, reference function or gameplay model executed',source=identity(R,srcpath),line=681,source_separator=[92,92,110],binary=identity(R,'Data/messages_core.dat'),membership=membership)
(OUT/'newline-byte-validation.json').write_text(json.dumps(newline,ensure_ascii=False,indent=2)+'\n')
contract=json.loads((ROOT/'review/remediation-sixth-20261014-prepare/contracts/R6-U14.json').read_text())
normative=json.loads(blob(CORE,BASE+'findings/normative-records.json'))
selected=[]
for c in contract['scope_contracts']:
    matches=[(i,n) for i,n in enumerate(normative) if n['id']==c['id']];assert len(matches)==1
    i,n=matches[0]
    # Batch wrapper adds write/read sets and receivers; original proposal identity must match.
    assert n['original_full_proposal']==c['original_full_proposal']
    assert n['identity_and_verdict']==c['identity_and_verdict']
    selected.append(dict(id=c['id'],pointer='/'+str(i),original_full_proposal_equal=True,identity_and_verdict_equal=True))
handoff={}
for path in ['handoff/batch-assignment.json','handoff/file-conflict-graph.json','handoff/dependency-graph.json']:
    d=json.loads(blob(CORE,BASE+path));s={}
    for k,v in d.items():
        if k=='batches':s[k]=[{kk:vv for kk,vv in x.items() if kk!='scope_contracts'} for x in v if x['id']=='R6-U14']
        elif isinstance(v,list):s[k]=[x for x in v if 'R6-U14' in json.dumps(x)]
        elif isinstance(v,dict):s[k]={kk:vv for kk,vv in v.items() if 'R6-U14' in kk or 'R6-U14' in json.dumps(vv)}
        else:s[k]=v
    handoff[path]=dict(payload=identity(CORE,BASE+path),selected_original_records=s)
additional=['Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb','Data/Scripts/007_Objects and windows/011_Messages.rb','Data/Scripts/001_Technical/002_Files/001_FileTests.rb','Data/Scripts/007_Objects and windows/001_RPG_Cache.rb','Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb','Data/Scripts/007_Objects and windows/007_BitmapSprite.rb']
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),normative_payload=identity(CORE,BASE+'findings/normative-records.json'),selected_normative_identity_checks=selected,handoff=handoff,additional_readonly_source_identities=[identity(R,p) for p in additional],execution=dict(reference=0,independent_behavior_model=0,host=0,save=0,media=0),status='TOOL_IDENTITY_AND_BYTE_CHECKS_COMPLETE_ONLY')
(OUT/'packet-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(newline_membership=membership,normative_selected=len(selected),additional_sources=len(additional),reference_functions_executed=0)))
