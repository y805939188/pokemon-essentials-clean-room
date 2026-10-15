"""Record the actual first publication and full fixed-byte readback."""
import hashlib,json
from pathlib import Path
E=Path(__file__).resolve().parent
p=E/'receipts/core-remote-readback.json';raw=p.read_bytes();r=json.loads(raw)
assert r['all_complete_byte_matches'] and r['files_count']==88 and r['bytes_count']==1075700
assert r['commit']=='a4cba73dbb41a57ec3df90502964043b7d66b7f5' and r['tree']=='4e54838193e0ada3837fc792037fa79aa0f1f24d'
for n in ['050-commit-review','051-push-review','052-core-commit-identity','053-core-full-remote-readback']:
 assert json.loads((E/'logs'/(n+'.json')).read_bytes())['exit_code']==0
v={'schema':'r7.u07.r2.first-publication-receipt.v1','core_commit':r['commit'],'core_tree':r['tree'],'branch':r['branch'],'ordinary_push':True,'readback':{'path':'receipts/core-remote-readback.json','bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest(),'files_count':r['files_count'],'bytes_count':r['bytes_count'],'all_complete_byte_matches':True,'start_utc':r['start_utc'],'end_utc':r['end_utc']},'qualification':'This subsequent evidence-only commit adds actual publication receipts/logs and manifest. Candidate decision/configuration/execution/old-WAIT unchanged. Final result commit/tree and all final files are fully read back again in final public tool return; not recursively self-bound here.'}
(E/'publication-receipt.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
receipt=json.loads((E/'review-input-receipt.json').read_bytes());receipt['first_result_publication']=v
(E/'review-input-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
with (E/'report.md').open('a') as f:f.write('\n首个r2证据载荷 `'+r['commit']+'` / tree `'+r['tree']+'` 已普通推送，远端分支头前后相同；88文件/1,075,700字节均按固定commit完整HTTP读取并核bytes/SHA256/blob，包含manifest自身。详见 `receipts/core-remote-readback.json`、`publication-receipt.json` 与日志050–053。后续提交仅收入真实发布证据及对应manifest，候选语义结论不变；最终新提交全部文件另做完整远端回读并包外返回。\n')
print(json.dumps(v,ensure_ascii=False,indent=2))
