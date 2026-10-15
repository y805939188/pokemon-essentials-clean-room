"""Build four bounded candidate mirrors from the frozen B bytes. No reference execution."""
from pathlib import Path
import hashlib,json,subprocess
B='e646432c644dec04d306842cc5a559a29c718fbc'
ROOT=Path('candidates/R7-U11'); E=ROOT/'evidence/author'
WP='deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md'
TC='deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md'
AUD='audit/source-traceability.md'; FM='planning/feature-matrix.md'
def ident(data): return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob_content_id':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
changes=[]
def replace(text,old,new,record,scope):
    assert text.count(old)==1,(scope,text.count(old))
    changes.append({'record_id':record,'scope':scope,'old':old,'new':new})
    return text.replace(old,new,1)
originals={p:subprocess.check_output(['git','show',f'{B}:{p}']) for p in [WP,TC,AUD,FM]}
texts={p:d.decode() for p,d in originals.items()}
s=texts[WP]; rec='GR7-M17-002'
s=replace(s,'外围宿主工具文档边界（extendtext；animmaker 已归 WP74，不重提取）','外围宿主工具文档与有限静态请求边界（extendtext，§14；animmaker 已归 WP74，不重提取）',rec,'§1 purpose: same tool evidence scope')
s=replace(s,'extendtext 文档边界）；F','extendtext 文档与有限静态请求边界，§14）；F',rec,'§1 range: same tool evidence scope')
s=replace(s,'不反编译 exe；','可执行文件的静态补读仅限 §14 的文字扩展工具请求范围；',rec,'§1 non-goal: remove contradiction with bounded static supplement')
s=replace(s,'`extendtext.exe`：RMXP 显示文本/脚本对话框的放大外挂（仅文档陈述，§14）。','`extendtext.exe`：RMXP 文字编辑外围工具；说明书的两目标陈述与固定程序的四目标静态请求分别见 §14，实际效果未验证。',rec,'§3.2 entry cross-reference')
old='''## 14. 外围工具文档边界（E-4）

- `extendtext.exe`：**仅存在性与身份核验**——未反编译、未执行、无源码。`extendtext.txt` 全文陈述：Peter O. 出品的小工具，**放大 RMXP 的「显示文本」与「脚本」对话框**；用法＝对话框显示时运行程序。宿主兼容行为（实际放大效果、版本适配）未验证；文档陈述与运行验证分开登记。
- animmaker：已归 WP74（辅助制作/交换边界），本稿不重提取、不重复登记。
- 无源码/无文档部分保持未知；不因 exe 存在推断其内部行为。'''
new='''## 14. 外围工具的文档与有限静态请求（E-4）

原批准输入对 `extendtext.exe` 只作存在性与身份核验，未反编译、未执行、无源码；其文档证据保持：Peter O. 出品的小工具，放大 RMXP 的「显示文本」与「脚本」对话框，用法为对话框显示时运行程序。CV-M29 保留这一文档案例。下列补充来自固定程序业务入口、窗口查询、请求分支与导入的有限静态读取；不是程序执行、实际放大效果或版本适配验证。

**进入前提与选择门**：兼容窗口查询/尺寸接口、正常到达业务入口、无重复实例结果、目标在所述一轮内无外部改变时，先检查标记窗口。标记是顶层窗口的类名含区分大小写的 `Afx:` 且标题含 `RPG Maker XP`；这是存在性门，不校验目标进程归属。没有标记则不进入目标处理。目标窗口类须为 `#32770`，标题按下表精确英文匹配；对每个存在的目标只取首个 `EDIT` 子控件，不认证本地化同义标题或其它版本。

| 独立处理次序／精确标题 | 外框尺寸请求（宽×高） | 首个 EDIT 尺寸请求（宽×高） | 其它请求 |
| --- | --- | --- | --- |
| 1／`Script` | 840×240 | 800×176 | 无 |
| 2／`Show Text` | 840×144 | 800×72 | 无 |
| 3／`Comment` | 840×164 | 800×92 | 无 |
| 4／`Batch Text Entry` | 840×444 | 800×372 | 存在的按钮 id1 定位到 (25,392)，id2 定位到 (150,392)；只改位置，不改尺寸。 |

四个目标依 Script→Show Text→Comment→Batch Text Entry 独立查询，前一目标缺席只跳过该目标。外框请求先于 EDIT 请求；外框存在但无 EDIT 时仍已请求外框，跳过该子控件并继续后继目标。Batch 的两个按钮各自查询、各自存在才定位；缺 EDIT 不阻断按钮，缺一个按钮不阻断另一个。外框/EDIT 尺寸请求保持原位置、z 序和激活状态；按钮定位保持原尺寸、z 序和激活状态。尺寸/定位接口的返回未检查，假返回本身不触发中止后继请求；请求不保证接口成功或实际几何值。

**重复、退出与失败前缀**：互斥对象已存在时辅助结果为 0，停止本次业务；创建失败返回 −1，与重复实例分开，不能把它当成同一个停止分支或有效句柄。每轮目标处理后请求等待 150 毫秒，再检查标记；150 是等待入参，不是实测精确周期。没有独立业务取消；下一次检查发现标记消失时退出，并仅关闭有效互斥句柄，不恢复此前请求的尺寸/位置。后继目标、子控件缺席或接口假返回不撤销已发出的请求，所读业务循环无文件写入事务。运行时故障及真实窗口后果仍未知。

解释器错误路径只在诊断建议中提到这个工具，不启动工具、不修复脚本，也不证明兼容窗口存在。上述是旧宿主的有限请求事实；未来是否支持旧工具、英文窗口或同等编辑空间由兼容政策另选，不要求采用相同接口或内部组织。R6 L07 的真实接口返回、尺寸、周期、进程所有权、本地化/版本、自动启动及运行库启动余部未知保持。新静态对照见测试目录 R7-U11，全部 DERIVED_VECTOR／NOT_EXECUTED。

animmaker 仍归 WP74，本稿不重提取或借用其输出文件规则。未读取的程序余部与全部实际宿主运行保持未知，不因文件存在或静态请求推出运行成功。'''
s=replace(s,old,new,rec,'§14 bounded static request contract')
s=replace(s,'6. 停用/不可达：玩家转移处理的大停用块、通道补设的唯一调用点、事件 ID 工具的无效实现、装载器脚本（可静态解码读取但不执行，§12.4）、townmapgen 的引号处理停用代码。','6. 停用/不可达：玩家转移处理的大停用块、通道补设的唯一调用点、事件 ID 工具的无效实现、townmapgen 的引号处理停用代码。单节档案装载器另属当前可读的条件入口：兼容未加密宿主到达唯一 Main，目录可枚举且所选 .rb 可读、先前依赖正常时，末尾请求发现并求值散文件（§12.4）；静态可达不等于实际宿主启动或加载成功。','GR7-M16-001','§16-6 classification sentence only')
s=replace(s,'外围工具（extendtext 仅文档＋存在性）','外围工具（CV-M29 保留 extendtext 原文档＋存在性，新四目标静态对照见 §14 与测试目录 R7-U11，效果未验证）',rec,'§17 catalog cross-reference')
texts[WP]=s
section='''
## R7-U11：文字扩展工具的有限静态请求对照

以下均为 SOURCE_STATIC 支持的 DERIVED_VECTOR／NOT_EXECUTED；只读固定程序，不执行可执行文件、窗口接口、独立行为模型或 Demo。成功到达请求的共同前提：兼容窗口查询/尺寸接口、正常业务入口、无重复实例结果，目标在该轮无外部改变。标记与精确目标门见 WP75 §14；每个子例独立复位，表内数字均为请求值，不是实测几何。

| ID | 输入／前提 | 静态预期与观察边界 |
| --- | --- | --- |
| R7-U11-EXT-01 | 标记有效；只存在类 #32770、标题 Script 的目标及首个 EDIT | 外框840×240→首EDIT800×176；其余三个目标缺席分别跳过。 |
| R7-U11-EXT-02 | 同前，只存在 Show Text 及首个 EDIT | 外框840×144→首EDIT800×72；不依赖 Script 存在。 |
| R7-U11-EXT-03 | 同前，只存在 Comment 及首个 EDIT，Script/Show Text 均缺 | 外框840×164→首EDIT800×92；前两缺席不取消 Comment 处理。 |
| R7-U11-EXT-04 | 同前，只存在 Batch Text Entry、首EDIT及按钮id1/id2 | 外框840×444→首EDIT800×372→id1位置(25,392)→id2位置(150,392)；按钮只定位，尺寸保持。 |
| R7-U11-EXT-05 | 四目标都在；分别只移除其中一个目标；另全缺对照 | 按Script→Show Text→Comment→Batch独立处理，单一缺席只跳过该目标，其它请求顺序保持；全缺时仍到等待与下次标记检查。 |
| R7-U11-EXT-06 | 各目标分别存在但无EDIT；另同目标存在两个EDIT | 无EDIT仍已发出该外框请求，跳过该子控件并继续后继目标；两个EDIT只选择查询所得首个。Batch无EDIT时按钮请求仍独立。 |
| R7-U11-EXT-07 | Batch外框在，分别缺id1、缺id2、两者都缺；各例再分别有/无EDIT | 每个按钮仅自身存在才定位，缺一个不阻断另一个；两者都缺只保留外框及存在的EDIT请求。无EDIT不阻断存在的按钮。 |
| R7-U11-EXT-08 | 四目标及子控件在；分别令某次尺寸/定位接口返回假 | 假返回未被检查，本身不阻断下一子控件或后继目标；已发请求不回滚，实际尺寸/位置未知。尺寸保持位置/z序/激活，按钮保持尺寸/z序/激活。 |
| R7-U11-EXT-09 | 无标记；另仅把Afx:改成afx:；另标记有效而目标标题本地化或目标类非#32770 | 前两例不进入目标循环；后者只跳过不精确匹配的目标。标记存在不认证任一目标属于该进程。 |
| R7-U11-EXT-10 | 互斥对象已存在／创建失败−1两独立样本 | 重复结果0停止业务；−1不是该0分支，可继续至标记门，不能当有效句柄或成功运行。 |
| R7-U11-EXT-11 | 一轮已有请求；等待后标记消失；另标记保持 | 请求等待150毫秒→下次检查；消失则退出且仅关闭有效互斥句柄，无恢复尺寸/位置；保持则可继续下一轮。无独立业务取消，不承诺精确周期或文件事务。 |
| R7-U11-EXT-12 | 解释器到达含工具建议的诊断路径 | 只产生诊断建议，不启动工具、不自动修复脚本，不证明实际窗口或效果。R6 L07全部运行未知及CV-M29原文档向量保持。 |
'''
texts[TC]=replace(texts[TC],texts[TC],texts[TC]+section,rec,'EOF append only; CV-M29 and all old cases unchanged')
anchor='\n### T-WP76-01 《设施内容生成与模拟》'
note='''
第七轮有限静态补充（GR7-M17-002）：固定R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 的 `extendtext.exe`（4640字节，SHA256 `8aefdb578c521bc05e1bfae21f239a2e0f64a9d12fdd24527c3dc541cccb4efc`，blob `50f6ea5c2611101e22ed797483a3776da2afd90e`）：字节[1692,2764)业务/导入跳板、[3072,3348)数据，并定向核入口[1561,1684)及导入表。静态确认标记门、互斥分支、四目标独立请求与按钮只定位、缺席/假返回/退出前缀；见WP75 §14、测试目录R7-U11-EXT-01–12。`extendtext.txt`全文及解释器L120–195仅支撑原文档和诊断不启动边界。SOURCE_STATIC／DERIVED_VECTOR，程序/接口/模型/宿主/Demo均NOT_EXECUTED；R6 L07运行未知保持，原批准输入身份及CV-M29不变。
'''
texts[AUD]=replace(texts[AUD],anchor,note+anchor,rec,'T-WP75-01 append static evidence row; preserve original record')
oldline=next(x for x in texts[FM].splitlines() if x.startswith('| F18-04 |'))
newline=oldline[:-2]+'；第七轮有限静态补充：固定文字扩展工具的标记门、四目标独立尺寸请求及Batch按钮只定位见净化WP75 §14与R7-U11-EXT-01–12；SOURCE_STATIC／DERIVED_VECTOR，实际接口/尺寸/周期/进程归属/自动启动仍未验证，原Reviewed历史资格不扩张 |'
texts[FM]=replace(texts[FM],oldline,newline,rec,'F18-04 evidence-scope note only')
rows=[]
for p,text in texts.items():
 dest=ROOT/p; assert not dest.exists(),str(dest); dest.parent.mkdir(parents=True,exist_ok=True); data=text.encode(); dest.write_bytes(data)
 assert originals[p]==(Path('/workspace/r7-context/R7-U11-author/inputs/project')/p).read_bytes()
 rows.append({'path':str(dest),'formal_path':p,'base_commit':B,'base':ident(originals[p]),'new':ident(data)})
# Avoid duplicating the complete catalog inside the edit recipe.
for c in changes:
 if c['scope'].startswith('EOF'):
  c['old']='<complete fixed B catalog; see base identity>'; c['new']='<fixed B catalog unchanged followed by R7-U11 section>'
(E/'edits.json').write_text(json.dumps({'mirrors':rows,'changes':changes},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'FOUR_CANDIDATE_MIRRORS_BUILT','mirrors':rows,'conditional_specs_demo':'NOT_CHANGED_NO_ROOT_MAINTENANCE_CONFIRMATION','scope_changes':len(changes)},ensure_ascii=False,indent=2))
