"""Mechanical report checks only; never substitutes for semantic reception."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

START = datetime.datetime.now(datetime.timezone.utc).isoformat()
HERE = Path(__file__).resolve().parent
REPO = Path('/workspace/r8-external-legacy')
WRITE_ROOT = str(HERE.relative_to(REPO)) + '/'
checks = []

def record(name, condition, detail):
    checks.append({'name':name,'passed':bool(condition),'detail':detail})
    assert condition, (name,detail)

def git(*args):
    return subprocess.check_output(['git','-C',str(REPO),*args]).decode().strip()

for p in sorted(HERE.glob('*.json')):
    json.loads(p.read_text())
record('all_json_parse',True,'All task JSON parsed; no behavior execution.')
frozen=json.loads((HERE/'frozen-primary-structure.json').read_text())
purpose=json.loads((HERE/'purpose-dispositions.json').read_text())
ledger=json.loads((HERE/'reading-ledger.json').read_text())
expected=set(range(1933,2080)) | set(range(2849,4115))
record('physical_denominator_exact', len(frozen['units'])==1413 and {x['line'] for x in frozen['units']}==expected,'1413 physical lines, not atomic assertions.')
read=[]
for item in ledger['primary_reads']:
    a,b=item['range']; read.extend(range(a,b+1))
record('continuous_actual_read_ranges',set(read)==expected and len(read)==1413,'Exact contiguous ledger cover, no duplicate/read credit outside primary.')
record('all_structures_disposed_once',len(purpose['units'])==1413 and {x['line'] for x in purpose['units']}==expected,'Purpose routing includes every physical line, still incomplete atomic inheritance.')
manifest=(REPO/'planning/review-manifest-2026-09-19.md').read_bytes()
for u in frozen['units']:
    part=manifest[u['byte_start']:u['byte_end']]
    assert len(part)==u['bytes'] and hashlib.sha256(part).hexdigest()==u['sha256']
record('all_primary_offsets_and_hashes',True,'1413 line slices verified against fixed manifest, not semantic reading credit.')
record('primary_bytes_exact',sum(x['bytes'] for x in frozen['units'])==627400,'Both ranges total627400 bytes including original line endings.')
semantic=json.loads((HERE/'semantic-purpose-review.v2.json').read_text())
routes=json.loads((HERE/'current-primary-contribution-routes.v2.json').read_text())
record('declared_local_purpose_state',purpose['status']=='PRIMARY_PURPOSE_REVIEW_COMPLETE_PENDING_ROOT_RECEPTION' and semantic['reviewed']==156 and semantic['unreviewed']==0 and ledger['actual_counts']['currentness_unclosed_content_paragraphs']==0,'Finite documentary purpose state only; no engine/global semantic approval from this check.')
record('meaningful_event_denominator',len(semantic['units'])==156 and {x['round'] for x in semantic['units']}==set(range(16,172)),'156 coherent version/review/authorization events, not punctuation/JSON fields.')
record('every_paragraph_event_binding',all(x['semantic_event'] in {u['id'] for u in semantic['units']} for x in purpose['units']),'Every1413 structure associated with a reviewed event and881 full paragraph dispositions.')
record('current_primary_routes',len(routes['formal_routes'])==131 and len({x['path'] for x in routes['formal_routes']})==131,'All current formal identities routed; no131-file FULL_READ credit.')
record('no_self_reception',all(x['root_reception']=='UNRECEIVED' for x in purpose['units']),'All1413 primary physical units explicitly unreceived.')
changed=git('diff','--name-only','30cfed0996003b6ebf4b5c51cc04f31ca9255440','--').splitlines()
untracked=git('ls-files','--others','--exclude-standard').splitlines()
record('write_scope',all(x.startswith(WRITE_ROOT) for x in changed+untracked),{'changed':len(changed),'untracked':len(untracked),'root':WRITE_ROOT})
record('branch',git('branch','--show-current')=='codex/r8-external-legacy-manifest-currentness-20261016',git('branch','--show-current'))
record('formal_tree_unchanged',git('rev-parse','HEAD:deliverables/final-specification-set')=='f292698cdd4a8e725525a9be6dc34b75faaf151e',git('rev-parse','HEAD:deliverables/final-specification-set'))
record('reference_clean',subprocess.check_output(['git','-C','/workspace/pokemon-essentials','status','--porcelain']).strip()==b'','Read-only reference remains clean.')
result={'schema':'r8-external-legacy-validation/v1','start_utc':START,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'command':['python',str(Path(__file__).relative_to(REPO))], 'bottom_exit':0,'checks':checks,
        'stdout_summary':'All mechanical report consistency checks passed.','stderr':'','evidence_level':'TOOL_VALIDATION',
        'business_tests':'NOT_EXECUTED; no semantic or root-reception upgrade'}
(HERE/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'passed':True,'evidence_level':'TOOL_VALIDATION','business_tests':'NOT_EXECUTED'},ensure_ascii=False))
