"""Produce exact semantic-field views, retaining every non-identity field.

Pure transport identities are separately disposed at exact JSON pointers. The
output is a reading aid, never proof that a model actually read any payload.
"""
import hashlib
import json
from pathlib import Path

B=Path('/workspace/pokemon-essentials-clean-room/review/global-independent-review/eighth-2026-10-16-fd1df57-c84e')
O=B/'tasks/coverage_acceptance_incremental'; V=O/'ledger-views-v2';V.mkdir(exist_ok=True)
S=json.loads((B/'delegation/readsets/coverage-incremental-v2.json').read_text())['snapshot_entries']
PURE_IDENTITIES={'repo','repository','commit','frozen_commit','tree','workspace_tree','formal_tree','git_mode','git_type','git_blob','git_bytes','actual_mode','actual_kind','bytes','sha256','actual_blob','exists','matches_git_blob','identity_matches_frozen','working_bytes_equal_fixed_commit','mode','blob','matches_frozen_blob','matches_frozen_bytes','actual_matches_fixed','frozen_blob','current_blob','byte_count','size_bytes'}
index=[]
for n,e in enumerate(S):
    if not e['original_path'].endswith(('reading-ledger.json','/source-reading.json','/formal-readset.json','/read-state.json')):
        continue
    raw=(B/e['snapshot']).read_bytes();data=json.loads(raw);disposed=[]
    def transform(value,pointer=''):
        if isinstance(value,dict):
            result={}
            # A matching key outside a proven identity object may be a rule.
            # In particular, mode/bytes can be substantive under nested values.
            is_identity = ('path' in value and any(k in value for k in ('sha256','blob','git_blob','commit','repo','repository')))
            is_identity = is_identity or (pointer.rsplit('/',1)[-1] in ('identity','input','actual') and any(k in value for k in ('sha256','blob','git_blob')))
            for key,child in value.items():
                at=pointer+'/'+key.replace('~','~0').replace('/','~1')
                if key in PURE_IDENTITIES and is_identity:
                    encoded=json.dumps(child,ensure_ascii=False,separators=(',',':')).encode()
                    disposed.append({'pointer':at,'value':child,'value_sha256':hashlib.sha256(encoded).hexdigest(),'purpose':'EXACT_TRANSPORT_OR_BASELINE_IDENTITY_ONLY; does not contain rule/read-state/claim/reader/consumer content'})
                else:result[key]=transform(child,at)
            return result
        if isinstance(value,list):return [transform(child,pointer+'/'+str(i)) for i,child in enumerate(value)]
        return value
    view=transform(data)
    # Compact per object while retaining every value; continuous physical view
    # lines provide readable windows without manufacturing source line ranges.
    rendered=json.dumps(view,ensure_ascii=False,indent=2)+'\n'
    p=V/f'{n:03d}.semantic-fields.json';p.write_text(rendered)
    dp=V/f'{n:03d}.identity-dispositions.json';dp.write_text(json.dumps(disposed,ensure_ascii=False,indent=2)+'\n')
    index.append({'index':n,**e,'semantic_fields_view':str(p.relative_to(B)),'semantic_fields_view_bytes':len(rendered.encode()),'semantic_fields_view_lines':len(rendered.splitlines()),'semantic_fields_sha256':hashlib.sha256(rendered.encode()).hexdigest(),'exact_identity_dispositions':str(dp.relative_to(B)),'inventory_only_fields':len(disposed),'reading_credit':'NONE_UNTIL_ACTUAL_CONTINUOUS_READING','qualification':'No source rule, purpose, read status, reader, range, premise, consumer, case, qualification, actual operation or error field was removed.'})
(V/'index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'index':e['index'],'path':e['original_path'],'bytes':e['semantic_fields_view_bytes'],'lines':e['semantic_fields_view_lines'],'identity_only_fields':e['inventory_only_fields']} for e in index],ensure_ascii=False,indent=2))
