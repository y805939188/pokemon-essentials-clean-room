"""Clarify independent fixture premises and display the five metrics defaults."""
from pathlib import Path
import datetime,hashlib,json
OUT=Path(__file__).resolve().parent;ROOT=Path(__file__).resolve().parents[5]
M=OUT.parent/'mirror/deliverables/final-specification-set';changes=[]
def edit(path,old,new):
    p=M/path;b=p.read_text();assert b.count(old)==1,(path,old)
    a=b.replace(old,new,1);p.write_text(a)
    changes.append(dict(path=str(p.relative_to(ROOT)),old=old,new=new,before_sha256=hashlib.sha256(b.encode()).hexdigest(),after_sha256=hashlib.sha256(a.encode()).hexdigest()))
edit('generic-kernel/wp03-content-identity-and-schema.md',
'合法物种的指标作者节已经存在且成功转换／登记时，省略 BackSprite、FrontSprite、FrontSpriteAltitude、ShadowX、ShadowSize 分别得到 (0,0)、(0,0)、0、0、2。基础节与非零形态节都按这组自身默认，不按物种形态字段继承，也不逐字段复制基础指标。',
'''合法物种的指标作者节已经存在且成功转换／登记时，缺字段结果如下：

| 省略字段 | 该记录自身的默认 |
| --- | --- |
| BackSprite | (0,0) |
| FrontSprite | (0,0) |
| FrontSpriteAltitude | 0 |
| ShadowX | 0 |
| ShadowSize | 2 |

基础节与非零形态节都按这组自身默认，不按物种形态字段继承，也不逐字段复制基础指标。''')
edit('creature-rpg/wp27-bag-and-item-storage.md','显式给 NamePlural=Reviews 才保存 Reviews。','显式给 NamePlural=Reviews 才保留该复数原名。')
edit('generic-kernel/wp04-pbs-lifecycle.md','schema／查询无覆写，其余转换、终检依赖正常时，省略 Flags','schema／查询无覆写，缺值对象未被额外赋予字符串比较能力，其余转换、终检依赖正常时，省略 Flags')
edit('generic-kernel/wp04-pbs-lifecycle.md','一个正常蛋原剩2步、首个被检查的非蛋队员带该特性且此前正常','一个正常蛋原剩2步、除该蛋外仅一个正常非蛋队员带该特性且此前正常')
edit('test-catalog/generic-kernel-wp02-03-04.md','显式BackSprite=7,8，其余五组字段按省略规则','显式BackSprite=7,8，其余指标字段按省略规则')
edit('test-catalog/generic-kernel-wp02-03-04.md','正常蛋原剩2步，首个检查的非蛋队员带此特性，之前正常；独立省略Flags对照','正常蛋原剩2步，除该蛋外仅一只正常非蛋队员且带此特性，之前正常；独立省略Flags对照')
edit('test-catalog/generic-kernel-wp05-06-07-08-09-10.md',
'合法物品和口袋，库存添加成功后到达LZ37条件的口袋提示；独立作者取消导出／非法导入对照',
'合法物品和口袋，库存添加成功后到达LZ37条件的口袋提示；独立当前游戏语言A、选择导出目标B后在核心／游戏选择取消，尚未进入导出；另独立合法SCRIPT_TEXTS头仅一行键K，经完整导入，旧输出可写且已成功覆盖打开')
edit('test-catalog/generic-kernel-wp05-06-07-08-09-10.md','取消未进入导出不写；完整导入旧输出已覆盖打开后解析失败','取消未进入导出不写文件、不切游戏语言；完整导入单键哈希因奇数行解析失败')
(OUT/'refinement-receipt.json').write_text(json.dumps(dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),changes=changes),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(document_refinements=len(changes),status='AUTHOR_CLARIFICATION_ONLY; no nonauthor review signed')))
