# B-04 独立复核：WP47-A／WP47-B／WP48

结论：**REQUEST_CHANGES_SCOPED**。完整阅读本批5份原稿/附表、5份最终正文/附表及90条相关静态测试，完成新主体源族、已读共享调用者、登记/继承/重开、默认数据与生命周期交界复核。新增 **RUN-B-019（P2）**；另记录既有RUN-B-018计数问题向WP48传播，及RUN-B-003共享规则对SkillSwap的适用。不宣称B组或全局完成。

项目基线 `e1e01bb18d824931e54f182dd61af5a9f908ba85`；参考只读基线 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。分支 `review/2026-10-03-fd82a639/B`，上一批已发布 `ff0e74432d4cb56ac9dc749b1376570d507b1ffd`。本批仅写 `agents/B/B-04/`；规格、交付、规划、审计和参考材料均未修改。模型证据仅为请求并获spawn接受的gpt-6-astra/ultra；运行回显NOT_EXPOSED，速度UNVERIFIED，要求Standard且未改Fast/Ultrafast设置。

## 主要结论

- **RUN-B-019：动态目标被写成原始目标数据。** WP47-A原104/最终116以原始数据判断是否进入单目标重定向；实际构造和重定向都读取当前使用者决定的目标类别。默认CURSE静态目标User，幽灵使用者改为RandomNearFoe，因此可受跟我来接管。双打幽灵U0 HP101、对侧1先跟我来、固定CURSE初选3，实际诅咒1并扣U50至51；按错误原始数据门会诅咒3。需要改两版共同措辞并补正反测试。EXPANDINGFORCE受精神场地改AllNearFoes是反向边界，即使目标只剩1也不进单目标重定向。
- **RUN-B-018同根传播，不新增漏项。** WP48最终族标签StatusImmunity8／DamageCalcFromUser41／DamageCalcFromTarget15应为11／43／14。原表、最终明列身份及读过的源登记展开全部148键一致；只有标签统计不一致。
- **共享规则仍有效。** 131个唯一主/共享招式身份中，额外加载重开只有SkillSwap条款；skillswapclause真时目标拒绝。WP47-B局部能力交换表须同共享WP39规则一起读，既有RUN-B-003键/配置入口问题保持，不重复计新发现。

## 覆盖与等价性

[reading-log.tsv](reading-log.tsv)含83条实际读证记录。新完整Items470行；MoveAttributes、BattlerOther、ChangeMoveEffect的新族与B03实读合成完整主体覆盖；SwitchingActing948行、核心主阶段/目标/伤害/状态/阶级/初始化/回合尾复用自身固定基线全文阅读，并对本次关键路径再读。WP48全部27族、148展开身份逐项映射，空CertainSwitching另列。新读Target185行、Ability45行，受限Item不可移表、通用登记复制语义和配置字段另记。搜索/计数记录明确标为定位或结构证据，没有替代主体阅读。

[source-coverage.tsv](source-coverage.tsv)共299条：12个跨入口规则、55个WP47-A主身份、60个WP47-B主身份、17个共享行、148个能力展开身份与1空族、6个完整数据集合。[equivalence.tsv](equivalence.tsv)共30个原→最终决定，覆盖全部正文与附表、MA29/SB38/AB23测试。正文中具体条件、倍率槽、记录/PP/物品写入及既有异常总体保留；RUN-B-019为原与最终共同源行为错误，非净化丢失。

自然之恩67条物品/类型/数值、投掷578条物品/数值与已读PBS Flags的文本投影逐项一致；38个持物改类型映射、7列调用/复制排除、号令32及安可常6+新增6、8物种不可移组合逐项核对。未把578个数值表当成已审全部被动物品。默认19个具名招式段和8个能力段只为注册/目标/数据/标记佐证；描述文字不代替执行路径。

独立固定算术复核包括Hidden Power60/61/62/63中间值对应68/68/69/70，速度101×1.5→152、麻痹101÷2→51，命中80×121整除100=96及95/96界，基础伤害28、攻击倍增54、硬爪37、草之毛皮19、钢之魂叠加63/模式破坏者42、影盾14，HP101吸收25、替身25、诅咒50。都是手工/固定数值算术，未执行参考或战斗转译模拟器。

## 保留与未决

已存在修订保持：WP47-B-N01反射撤退射击0实计击数；N02号令specialUsage假和普通PP/状态；GR-014投掷当前空物首次失败及I13–I15对照；WP48-R01命中整数阈值；无防守/模式破坏者分层；觉醒力量旧代数值、调用名单拼写差异和MeteorBeam未明列、秘密之力环境附效/媒体未决。未修参考、未按官方习惯改这些异常。

B04首次判断已先存[independent-first-judgments.json](independent-first-judgments.json)，其后仍未阅读任何其它组未派发结论。完整生命周期/被动物品/AI组合留后续B05起主审；本批只审具名进入点和已读共享链。PBS/trainers的一组名字搜索未命中，仅是该文本文件结果；不推断demo不存在。运行观察=0、演示事件链=0；U01–U10、G01–G12、20条既有AX保留，未知不等于不存在。

## 交付与下一步

七件材料：本报告、[findings.json](findings.json)、[reading-log.tsv](reading-log.tsv)、[source-coverage.tsv](source-coverage.tsv)、[equivalence.tsv](equivalence.tsv)、[checkpoint.json](checkpoint.json)、独立首次判断。逐位置行号/输入前提/最小修订/确定性复核见发现文件。静态文件/范围/白名单检查后做本批检查点commit、正常push并核远端精确hash；精确提交号通过Git和交付消息报告。发布后按已授权顺序进入B05[WP49–51]，不关闭全局出口。
