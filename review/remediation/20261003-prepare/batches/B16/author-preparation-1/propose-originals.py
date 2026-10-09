"""Generate exact private original-clause amendment proposals; never apply them."""
import difflib
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prepare import BASE, OUT, blob, dump, identity, package

ORIGINALS = {
 "H": "specs/ui/wp65-controls-help-appendix.md",
 "T": "specs/ui/wp65-title-load-options-pause-and-pc.md",
 "A": "specs/ui/wp66-a-party-and-summary-ui.md",
 "B": "specs/ui/wp66-b-storage-and-pokedex-ui.md",
 "C": "specs/ui/wp66-c-bag-item-storage-and-shop-ui.md",
}

CHARACTERISTICS = """
个性描述的兼容数据：先找最高 IV；并列时按 **HP、攻击、防御、速度、特攻、特防** 的循环次序，从 personalID 对 6 的余数位置起取首个最高项；再用获选 IV 对 5 的余数选择列。下表为行为含义，不保证未读翻译资源的字面文本。

| 属性 | 余0 | 余1 | 余2 | 余3 | 余4 |
| --- | --- | --- | --- | --- | --- |
| HP | 喜欢吃东西 | 常睡午觉 | 常打瞌睡 | 常散落物品 | 喜欢放松 |
| 攻击 | 对力量自豪 | 喜欢胡闹 | 稍易急躁 | 喜欢打斗 | 易急躁 |
| 防御 | 身体结实 | 擅长挨打 | 很执着 | 耐性强 | 很坚毅 |
| 速度 | 喜欢奔跑 | 对声音敏感 | 莽撞傻气 | 爱逗乐 | 逃得快 |
| 特攻 | 好奇心强 | 喜欢恶作剧 | 很机灵 | 常陷入思考 | 很挑剔 |
| 特防 | 意志坚定 | 有些虚荣 | 不服管束 | 不愿认输 | 有些顽固 |
""".strip()

RULERS = """
搜索大小候选是离散标尺，不能输入任意数值。下列公制标签对应过滤使用的原始身高分米与体重百克值；切换显示单位不改变候选或过滤。

| 标尺 | 37 个候选标签（升序） |
| --- | --- |
| 身高（m） | 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,8.0,9.0,10.0 |
| 体重（kg） | 0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,7,8,9,10,11,12,14,16,18,20,25,30,35,40,50,60,70,80,90,100,125,150,200,300,500 |

大小子页先聚焦上界。用 L/U 表示两端所存候选索引；具体档为0..36，-1为未选，37为表长哨兵；这些位置不同，不能合并为一个“无界”。下表保留导航不对称，§9继续规定过滤时的数值含义。

| 输入及所在位置 | 焦点/端点变化 |
| --- | --- |
| UP，在OK/Cancel | 聚焦下界，取L |
| UP，在下界 | 聚焦上界，取U；上界再UP不动 |
| DOWN，在上界 | 聚焦下界，取L |
| DOWN，在下界 | 聚焦OK；OK/Cancel再DOWN不动 |
| LEFT，在Cancel | 聚焦OK；不写端点 |
| LEFT，上界未选-1 | 若L<36，改U=36；否则不动 |
| LEFT，上界0 | 若L<0，改U=37；否则不动 |
| LEFT，端点>0（含下界37） | 下界可减1；上界仅在L≤下一索引时减1；上界37不递减 |
| RIGHT，在OK | 聚焦Cancel；不写端点 |
| RIGHT，上界37或更大 | 改U=0 |
| RIGHT，上界36 | 改U=-1 |
| RIGHT，端点其余位置且索引<37 | 上界可加1；下界在U未选，或U<37且U≥下一索引时加1；下界负索引不递增 |
| ACTION（任意子页） | 只聚焦OK，不执行提交 |
| USE，在OK / Cancel；BACK | 提交当前子页参数 / 放弃当前子页参数；BACK也放弃 |

大小子页左右直接改变所存端点；相等端点允许，禁止越过对端的分支以表中条件为准。搜索主画面ACTION只聚焦Start，随后USE才运行搜索；参数子页ACTION后USE仅提交参数，不执行搜索。无USE不得推导模式写入或结果态。
""".strip()

ICON_TABLE = """
界面图标的行为数据（合法资源尺寸前提，真实素材与宿主输出未证）：动画相位按绝对运行时间，重新创建不保证第0帧。

| 消费对象 | 切片与周期 | 特殊状态 |
| --- | --- | --- |
| 个体成员图标（队伍/载入等） | 首行方形，边长为图高，帧数为图宽除图高的整数部分；常态一周0.25秒 | HP≤一半变0.5秒，HP≤四分之一变1秒，濒死固定首帧；选中前半周期偏移(+4,+6)，后半(+4,-2)；空成员不显示 |
| 种类图标 | 同样首行方形，0.25秒一周 | 不按对象HP降速 |
| 道具图标 | 高48时48×48切片，帧数为宽/48向下取整且至少1，一周1秒；其他高度使用整图单帧 | 空值是否隐藏须按消费者：设为空隐藏的界面与请求通用空图的界面分开；不能假设同一处理 |
| 持有道具图标 | 装载持物对应图并随成员持物变化刷新 | 无持物时不显示 |
| 盒内静态成员预览 | 首个方形格 | 不等于队伍个体动画或命名预览 |

例如个体128×64是2帧，HP10/40一周1秒；道具96×48是2帧一周1秒。帧取按周期相位均分的所在段，不以更新次数或新建时间清零。命名预览另为四个水平切片、一周0.4秒；继续面板行走图取4×4图集首行四格、一周0.5秒。
""".strip()

FORMS = """可列形态计算：遍历同种各形态，先排除原始名称不存在或为空的非0形态及图鉴展示形态不等于自身的条目；“显示全部形态”仅绕过随后已见门。结构上是否存在合格非0形态在已见过滤之前认定，不能从最终已见列表长度倒推。单一雌性种查雌档，无性种查雄档、生成标签后仍以雄档展示；双性种按雄后雌检查。默认形态0的双性正面解析结果相同，取首个合格性别后停止、统一以雄档展示（仅雌已见也如此）；没有标签时先给One Form。其它双性分支按雄后雌，名称非空时首个合格性别后停止，名称为空时可保留两性。显示全部开启则雄首先合格。已有名称包括空串原样保留，但无结构多形态且基形没有性别图差异时置空；其它缺名称条目按性别补Male/Female，无性结构多形态补One Form，否则Genderless。资源双方解析为nil相同不证明资源存在。排序按形态号再性别档；首次进入选择器的现有末次形态写入合同保持。"""

# (qualified ID, original file, exact original line, proposed entire clause)
EDITS = [
 ("C114", "H", 34, "- **换页时序**：先将旧页键图/标签用0.5秒淡出至0，再将新页键图/标签用0.5秒淡入至255，顺序执行，总目标1秒；初始首页也经这两阶段，旧内容原本不透明度0。时间单位为1/20秒，非固定宿主渲染帧。"),
 ("C114", "H", 40, "- **否则**：当前页号递增1 → 清除旧确认回调 → 旧页0.5秒淡出、新页0.5秒淡入 → 完成后重挂确认键推进。等待仍更新图形与输入；清除回调期间确认输入不推进页码，不能仅凭Input更新声称又跳一页。最终页退出0.4秒与换页两阶段分列。"),
 ("C114", "T", 49, "- **开场序列**：逐张播放登记的开场图（默认2张）；每张先0.4秒淡入，再停留最多2秒，最后0.4秒淡出，无输入目标总2.8秒。USE提前仅在停留检查窗口生效，淡入/淡出不检查这一跳过键。放完后标题背景与确认提示进入闪烁（目标40个1/20秒单位一周），播放登记标题BGM；真实素材/宿主时序未运行。"),
 ("C114", "T", 50, "- **标题画面离开**：USE请求随机物种叫声后，等待1秒，再两幅标题图0.4秒淡出，同时请求BGM按1秒淡出，随后进载入画面。等待/淡出前清除标题更新与确认回调；不保证叫声全长播放或听感。下＋BACK＋CTRL进入删除画面也经过此离开过程。"),
 ("C114", "T", 274, "| T01 普通无存档启动 | 普通构建、无存档、LANGUAGES 空、资源齐备且开场无输入 | 开场2张每张0.4淡入＋2停留＋0.4淡出（目标共5.6秒）→标题→按C→等待1秒＋0.4标题淡出（BGM淡出请求1秒）→载入菜单新游戏/选项/退出三项（无继续/神秘礼物/语言/调试）；停留USE可提前，淡入/淡出无此跳过检查 |"),
 ("A058", "T", 65, None),
 ("C058", "T", 122, "| SE Volume | 滑杆0–100步长5（默认100） | 无 | 写SE音量；数值变更且正在播放BGS时，把当前BGS记录音量改为新SE百分数，再暂停/恢复；恢复请求再次乘SE百分数并取整，随后播放光标音。若先记忆同一BGS记录，记忆音量同步变化；例SE100/记录80，记忆后改SE50→两记录50→请求25。无BGS或数值不变不套此分支；真实听感未证 |"),
 ("C115", "T", 132, "| Screen Size | S/M/L/XL/Full；默认索引为SCREEN_SCALE×2向下取整再减1（默认1=M） | 无 | 读取只取min(保存值,4)，不钳负值。0/1/2/3先请求内部尺寸，再关闭全屏并按0.5/1/1.5/2倍居中；4或负数先请求内部尺寸再请求全屏。启动保存7按4请求但仍保存7；选项退出应用后写4。宿主实际输出未验证 |"),
 ("C125", "A", 60, None),
 ("C124", "A", 126, None),
 ("C126", "A", 155, None),
 ("A048", "A", 179, "- 候选计算保持蛋/Shadow、等级、已会排除与去重/首招式顺序规则。**空候选的画面入口在首次绘制时，对不存在的首候选作严格招式ID校验并抛ArgumentError，发生于选择循环之前**；无BACK/USE取消窗口、不进入放弃确认、不学习。非空合法候选才适用下述列表选择和放弃确认；不能用“空列表可取消”保证代替此失败。"),
 ("A048", "A", 200, "- 重学候选为空：若进入该画面，首绘严格ID校验失败，尚未进入选择循环；没有取消返回或学习写入。至少一合法候选的BACK才进入正常放弃确认。"),
 ("C003", "A", 238, "| A23 | 奶招：来源hp50/totalhp120，目标非蛋、非来源且hp30/totalhp50，资格与菜单检查成立 | 计算上限24但实际仅缺20，目标到50、来源到30；循环继续，来源不足门按计算上限检查。对照目标totalhp120则实际24、来源26/目标54；未给目标上限不能唯一推出24 |"),
 ("C003", "A", 246, "| A31 | 重学：等级20非蛋非Shadow，≤20升级未会U1/U2，初始未会U1，默认更多候选开 | 去重候选2招，U1在前；对照初始I1与U1/U2不交且均未会才是3招。选定确认后走§7.1，学会才记统计并true |"),
 ("A048", "A", 247, "| A32 | 重学画面入口、合法非蛋非Shadow成员、所有候选计算结果空、资源合法 | 首绘查空首候选触发严格ID类型ArgumentError，在BACK循环前失败；无放弃确认/学习；对照一合法候选BACK正常取消 |"),
 ("C003", "A", 248, "| A33 | 事件资格要求非蛋且hp>0，队伍仅一个hp>0蛋、无其他满足成员，allowIneligible为假 | 没有合格者但仍打开选择画面：蛋注解NOT ABLE，选蛋提示不能选且留循环；BACK写变量-1与空串。不得称蛋为“合格成员”。对照同对象非蛋且其余条件成立，选择可成功并写其索引/名称 |"),
 ("004", "B", 71, None),
 ("A056", "B", 134, None),
 ("C123", "B", 152, None),
 ("C121", "B", 170, None),
 ("C122", "B", 174, FORMS),
 ("C120", "B", 189, None),
 ("006", "C", 29, None),
 ("C118", "C", 30, None),
 ("C117", "C", 36, "- USE／ACTION确认落位；BACK把被拖物品搬回排序起始位置、当前游标恢复并关闭排序态，但移动期间已经写入的口袋保存索引**不会恢复**。例原索引0拖到2再BACK：顺序/当前游标回0，保存索引2；普通关闭再打开读2。没有拖动则不发生这个保存索引差异。"),
 ("D023", "C", 98, "**BP商店差异**：资源为BP（两处检查文案不同），无出售/赠品，统计为BP消费与共用件数。数量窗按 **数量×⌊单价÷2⌋** 显示，确认与实扣按数量×全单价。例单价20数量3显示30BP而实扣60；单价21数量3也显示30、实扣63；原C29单价20数量2显示20仍正确。此怪癖保留，非正常全价显示。"),
 ("B035", "C", 120, "| 购买部分放入 | 有限口袋容量/自动排序设置明确 | 普通删除回退已添加件数，物品总量可恢复、资源/统计不变，**槽分布可能改变**。有限2槽、无自动排序、POTION槽上限999，旧[999,997]买3→加2失败→从首槽回退2→[997,999]；单槽[997]同操作回[997]。无限口袋不套该容量失败前提；money/BP共用此袋路径 |"),
]


def diff(path, before, after):
    return ''.join(difflib.unified_diff(before.splitlines(keepends=True), after.splitlines(keepends=True),
                                       fromfile='a/' + path, tofile='b/' + path, n=0))


def main():
    snapshots = {k: blob(BASE, p).decode() for k, p in ORIGINALS.items()}
    lines = {k: t.splitlines(keepends=True) for k, t in snapshots.items()}
    dynamic = {
      ("A058", "T", 65): lambda old: old.rstrip() + " 行走预览按合法4×4图集首行四格，0.5秒一周，按绝对运行时间取帧；命名预览四水平格0.4秒一周，两入口不混同。",
      ("C125", "A", 60): lambda old: old.rstrip() + " **盒侧收缩队伍后旧源索引不重绑**：队伍[A,B]先选B源1，普通Switch中经SPECIAL存B入盒，返回[A]游标0后USE，先交换旧源1与目标0，队伍变[空,A]，随后换位结束对空面板赋成员失败；B仍在盒、部分队伍写入不回滚。ACTION快捷换位禁SPECIAL，不套此链。",
      ("C124", "A", 126): lambda old: old.rstrip() + "\n\n" + CHARACTERISTICS,
      ("C126", "A", 155): lambda old: old.rstrip() + " **取消合同的前提是首次详情绘制成功**。零招式成员普通MOVES页可画四个空位；进入详情、直接忘招或事件选招时先绘制所选招式的字段，空首招式造成字段访问失败，发生在BACK输入循环之前。无取消返回/招式写入；普通学招在不足4招时直接加入，不经过此失败入口。",
      ("004", "B", 71): lambda old: old.replace("放下／交换／释放／存入后暂持清空", "放下／释放／存入成功后暂持清空；交换X与目标Y成功后格位为X、暂持改为Y，仍禁止退出").rstrip(),
      ("A056", "B", 134): lambda old: old.replace("每行＝区域名＋见过数／拥有数／区域长度", "每行可见字段＝区域名＋见过数／拥有数；区域长度是内部完成阈值，不绘作第三个计数").rstrip(),
      ("C123", "B", 152): lambda old: old.rstrip() + "\n\n" + RULERS,
      ("C121", "B", 170): lambda old: old.rstrip() + " 显示按语言字符串位置3–4是否为US分支：非US身高分米除10为m、体重百克除10为kg，均1位小数；US信息页总英寸=round(原始身高/0.254)，按总英寸整除12的英尺和余数（两位数字）显示，重量=round(原始百克值/0.45359)/10（1位小数lb）。US搜索身高同除0.254取整，但重量=round(原始百克值/0.254)/10，保留两页差异；例原始重量100，Info22.0lb、搜索具体档39.4。搜索未选/表长哨兵先按下限0/999或0/9999及上限999/0或9999/0映射；US搜索下限表长、上限未选显示99英尺00英寸、重量9999.0，其他位置照转换。过滤仍比较原始分米/百克值，换locale不改资格；未拥有对象Info以身高/体重占位显示，真实翻译素材未读。",
      ("C120", "B", 189): lambda old: old.replace("其余均为纯查看", "另有查看盒子的背景刷新写入：首次装载或背景值改变时，旧box数字格式转整数；非法或未解锁墙纸写回盒号模16，空串/nil只采用显示fallback而底层可保持原值。盒号5（零基）锁定16→存储/显示5，空串→显示5但仍存空，合法可用3保持3；不以单纯退出回滚这些写入。其余查看是否写入按各入口明确合同判断").rstrip(),
      ("006", "C", 29): lambda old: old.rstrip() + " 合法三帧箭头按绝对运行时间循环：横向专用箭头一周0.1秒，通用箭头一周0.15秒；新建不保证首帧。文字暂停/导航图另有八帧与各自周期，不能套此三帧数据。",
      ("C118", "C", 30): lambda old: old.rstrip() + "\n\n" + ICON_TABLE,
    }
    proposals = []
    per_file = {k: {} for k in ORIGINALS}
    patchdir = OUT / "original-proposals"
    patchdir.mkdir(exist_ok=True)
    grouped = {}
    for short, key, n, after in EDITS:
        before = lines[key][n-1].rstrip('\n')
        after = dynamic[(short, key, n)](before) if after is None else after
        assert before != after and n not in per_file[key]
        per_file[key][n] = after + '\n'
        grouped.setdefault((short, key), []).append({"original_line": n, "before": before, "proposed_after": after})
    for (short, key), clauses in grouped.items():
        path = ORIGINALS[key]
        changed = list(lines[key])
        for clause in clauses:
            changed[clause["original_line"]-1] = clause["proposed_after"] + '\n'
        after = ''.join(changed)
        fullpatch = diff(path, snapshots[key], after)
        name = f"GIR-FD82-{short}-{key}.patch"
        (patchdir / name).write_text(fullpatch)
        proposals.append({
          "id": "GIR-FD82-" + short, "path": path, "input": identity(BASE, path),
          "status": "PROPOSED_NOT_APPLIED_NO_ORIGINAL_WRITE_AUTHORIZATION",
          "clauses": clauses, "fullpatch": "original-proposals/" + name,
          "fullpatch_sha256": hashlib.sha256(fullpatch.encode()).hexdigest(),
          "proposed_after_file_sha256": hashlib.sha256(after.encode()).hexdigest(),
          "proposed_after_bytes": len(after.encode()),
          "control_analysis": "contribution-analysis.json#contributions/" + "GIR-FD82-" + short,
          "basis": "Actual original extraction defect/missing decisive compatibility data at assigned qualified clause; not a blanket original neutralization.",
          "application_gate": "Parent sole registrar must confirm precise amendment at refreshed original identity before any application; this private proposal does not amend or authorize originals.",
        })
    combined = []
    for key, changes in per_file.items():
        after_lines = list(lines[key])
        for n, text in changes.items():
            after_lines[n-1] = text
        after = ''.join(after_lines)
        content = diff(ORIGINALS[key], snapshots[key], after)
        name = f"combined-{key}.patch"
        (patchdir / name).write_text(content)
        combined.append({"path": ORIGINALS[key], "input": identity(BASE, ORIGINALS[key]),
                         "fullpatch": "original-proposals/" + name,
                         "sha256": hashlib.sha256(content.encode()).hexdigest(),
                         "proposed_after_file_sha256": hashlib.sha256(after.encode()).hexdigest(),
                         "applied": False})
    dump("original-sync-proposals.json", {
       "formal_input": BASE, "proposal_only": True, "original_writes": 0,
       "proposal_count": len(proposals), "qualified_IDs": sorted({p['id'] for p in proposals}),
       "patch_format": "Complete zero-context unified diff; dry-check with git apply --check --unidiff-zero. Exact frozen blob/SHA256 and before clauses are mandatory before any authorized application.",
       "independent_per_ID_patches_not_to_be_applied_sequentially": True,
       "combined_patches_apply_each_file_once_on_exact_input_only": combined,
       "correct_originals_preserved": [
          "A044 UI TR first-move distinction", "A055 failed Start/Cancel persistent mode",
          "A015 T03 empty/nonempty data distinction; SV02 outside original sync scope",
          "003 original audit source-organization evidence not automatically an extraction defect",
          "D023 originalC29 quantity2×price20 display20BP", "004 B swap row already retainsY",
          "B15/B06/B07 accepted original and UI clauses including B31/B38 and storage sentinels/last-able guards",
       ],
       "proposals": proposals,
    })
    print(f"{len(proposals)} exact private proposals in five original files; none applied.")


if __name__ == '__main__':
    main()
