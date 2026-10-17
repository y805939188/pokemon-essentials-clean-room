#!/usr/bin/env python3

# Historical author step: never overwrite later calibrated evidence.
import hashlib as _r3_hashlib, pathlib as _r3_pathlib
_r3_guard_manifest = _r3_pathlib.Path(__file__).resolve().parent.parent.parent / 'routing-manifest.json'
if _r3_hashlib.sha256(_r3_guard_manifest.read_bytes()).hexdigest() != 'ff32f7359af3dbc6044a4dc0559f6ad5a2887811a61f98465073181041f93777':
    raise SystemExit('Historical R3 author step refuses changed/final manifest; use fixed archive and recorded patch for audit.')
"""Correct author source-delta prose only; preserve the initial application receipt."""
import pathlib,json,hashlib,datetime
R=pathlib.Path(__file__).resolve().parent;H=R.parent.parent
replacements={
'随机地牢连接/边界拒绝与地图缓存/出生位置等直接交界按有限入口修订；保留合法生成和空间邻格合同。':'默认PBS地图元数据[051]明确Dungeon=true，[050]未写该属性；文本配置已知，不证明成功编译/登记/装载、真实Map051资源/图块集/区域/事件或Demo可达性。',
'强制路线/等待的非字符指令、非法动态目标、并行解释器的生命周期/局部结束边界由新增3.4与矩阵指令行明确。':'117子公共事件携父当时事件编号、绑定建立时当前图而父原绑定不变；直接119从头取首个标签，正常缺目标继续物理下一命令，末尾入口、101仅向前预读与后继失败前缀分开。',
'邻图/路线目标会话、事件容器与并行解释器的刷新/结束边界补明；事件编号与映射所属图不可混为单一当前图查找。':'117父/子分别消费各自绑定图和携带编号；SPECIAL跳过后的末端静止沿普通移动/碰撞计时而不额外排跳跃；直接119缺目标正常继续，矩阵/目录/未决资格同步。'
}
def transform(v):
 if isinstance(v,str):
  for a,b in replacements.items():v=v.replace(a,b)
  return v
 if isinstance(v,list):return [transform(x) for x in v]
 if isinstance(v,dict):return {k:transform(x) for k,x in v.items()}
 return v
mp=H/'routing-manifest.json';raw=mp.read_bytes();m=json.loads(raw);new=transform(m);changed=[]
for before,after in zip(m['features'],new['features']):
 if before!=after:
  assert {k:v for k,v in before.items() if k!='differences'}=={k:v for k,v in after.items() if k!='differences'}
  changed.append({'feature_id':before['feature_id'],'field_changes':[{'pointer':'/differences','before':before['differences'],'after':after['differences']}]})
assert len(changed)>0
for name in ['source-file-reassessment.json','feature-source-deltas.json','source-refinement-patch.json']:
 p=R/name;data=json.loads(p.read_text());p.write_text(json.dumps(transform(data),ensure_ascii=False,indent=2)+'\n')
# Original patch BEFORE must remain exact archive content; it contains no newly-authored narratives.
p=json.loads((R/'source-refinement-patch.json').read_text());assert p['input_manifest_sha256']=='35175c7094b008e77af35cf6a7811c5fcd6f1a0dd20020b64d32b40d5670256e'
mp.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
(R/'source-narrative-correction.json').write_text(json.dumps({'schema_version':'routing-r3-author-source-narrative-correction.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reason':'作者逐38源复核后纠正三篇源差异摘要，未修改正式正文/任何去向或职责','manifest_before_sha256':hashlib.sha256(raw).hexdigest(),'manifest_after_sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),'consolidated_patch_sha256':hashlib.sha256((R/'source-refinement-patch.json').read_bytes()).hexdigest(),'records':changed,'original_application_record_retained':'author-refinement-application.json'},ensure_ascii=False,indent=2)+'\n')
print(len(changed),'difference annotations corrected; final',hashlib.sha256(mp.read_bytes()).hexdigest())
