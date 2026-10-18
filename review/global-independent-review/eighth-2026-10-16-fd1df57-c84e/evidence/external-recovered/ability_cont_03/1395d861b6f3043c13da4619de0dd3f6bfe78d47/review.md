# ABILITY-CONT-03：旧证据与历史资格有限接收

本组结论为 `COMPLETED_BOUNDED_RECEPTION_PENDING_PARENT`。CONT-03 指定的旧证据内容、格式澄清、强制更正及本域历史资格已完成有限接收；本组必要旧语义未接收为 0。新增正式差异提案 0；没有全特性域 PASS，也没有全局 `NO_REQUIRED_UPDATE`。`UPDATE_NOT_STARTED`。

冻结输入为 `b924c4cec2ce2eab65964d7bb4879feb456b4f87`，实际 workspace tree `d7258b1a8a2b925797461c498f2684743486c7da`。原完整合同/readset 按 `40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232` 读取；B8 与 R 保持原身份。唯一写集为本目录，专用分支 `codex/r8-ability-cont-03-20261016`。没有改原贡献、正式规格、参考源码、公共台账、main 或 tag；没有 spawn。最终实际报告 commit/tree 和逐件远端回读结果由最终回复绑定，避免未来身份和自哈希。

## 已接收内容与去重依据

完整读取适用 AGENTS、36,653B 全局 prompt、3,598B 指定 skill、4,599B 原 prompt、5,727B complete readset，以及冻结 next-dispatch/review/recovery。指定 clean-document-revision 明确排除评审报告和审计记录；本任务不修正式正文。

三件旧大对象共 6,068,626B，均按 recovery 中不可变 Git blob 实际取回，重新计算 UTF-8 bytes、SHA256、Git blob 后逐项相符：

| 旧对象 | Git blob |
| --- | --- |
| source-facts.json | `c35438e5215353125222707050ce59f066121fee` |
| forward-mapping.json | `3e5bcddd57dbf3cb2b8b8aacb2db31bec9ec1ff8` |
| reverse-mapping.json | `1db83aba96d56fcb1c9d8486cac3467376ec3b50` |

正向 463 个身份对象、80 个族对象与 source-facts 中对应对象完全相等；1,003 次嵌入断言与反向完整记录的对应字段完全相等。实际逐组读取 80 个族意义、24 个 caller 意义、441 个不同完整断言、全部共享前提/判断字段及结构处置。1,479 个子定位文本均位于完整父断言，其支持数组逐项等于父数组，可无损关联；这不能证明那些支持判断成立。完整旧内容接收与当前逐子断言支持认证分别记账。WP48 §9 和身份名单仅提供身份，不因旧 `ALL_CONCRETE` 或 `SCOPED_BEHAVIOR_SUPPORTED` 授予当前批准。

旧 received-contributions 51,739B 全文接收，原源读者 `/root/com_move`、其中 Battler 7–10 的 `/root/com_move/attributes_calling`、原正式读者 `/root/com_ability_item` 均保留。原 2R4F 和两共享目录的阅读身份不改成 CONT-03 新 FULL_READ，也不重复扩大源分母。旧六个有限接收、两个开放接口保留原时点；不能从旧报告“局部完成”推导当前全量完成。

463 行 tuple 的每个九字段行已读；精确 unit-map、意义/spec/consumer/assertion 字典已解码并逐字段还原到原 463 个对象。列字典大小为 2/448/2/41/76/70/4/289；321 个 assertion 对象和 289 个 assertion 列表仍只是表示/定位口径。跨文件相同行范围不合并来源身份。原单 JSON 的 Extra data 失败、误扩展名及全文 format clarifier 保留；逐行合法不改写成“全部 JSON 解析 PASS”。可复核的逐对象等值与恢复步骤见 [deduplication.json](deduplication.json)。

## 强制后继与有限反证

mandatory supplement、20,541B 八事实接收和 135,566B exact-input companion 中全部 31 个完整必要窗口已实读。原事实与更正后继同时保留，实际解释/普通对照/静态反例见 [forward-mapping.json](forward-mapping.json)；未复制源码进本报告。

- RX-HANDLER：add 保存原键；lookup/trigger 的 id 规范化不能反套到 add。Ability/Item 子类为空。A→B 复制后再替换 A，B 仍引用原 handler；不是动态别名。
- RX-ABILITY-DISPATCH/RX-ITEM-DISPATCH：nil 才回退，false/0 保留。经验缺省 −1；EV 看登记有无，有登记调用后即 true，不能概括为所有计算都保持输入。通知返回也不统一成为成功或消费。
- RX-MOVE-BASE/USAGE：默认钩子和实际 override 分开；默认公共过程也可能写记录，不能由默认实现推导全部处理器纯读、总返回或自动回滚。
- RX-SCENE-REFRESH/HP：refresh 仅限定直接委派；下游动态读取不获纯读保证。HP 写穿早于场景通知，部分记录/恢复跨半清理在通知之后；显示异常可保 HP 而跳过后段。
- RX-SCENE-ILLUSION：野生初始化用真实敌方 party 个体换图，后续 sendOut 可取 Illusion；普通 shiny 与自身 super_shiny 分开。消息/请求不证明最终像素或声音。

这些是既有证据资格更正和有限接收，不新增 formal required，不重新裁决原提供者，也不签整个 Battler/Move/UI 域。

## 九处历史资格

九个旧待接收定位均保留原 ID、完整原文和本次解释，见 [reverse-mapping.json](reverse-mapping.json)。

其中 WP48.L007、WP50 主文 L007、WP50 附表 L003 仅含范围/身份/输出说明，不含历史接受结论；两处具名关闭标记分别由原 BATCH-N01 与 WP50-R01 的实际有限复审报告接收；三处“依赖已限定通过”仅保留旧输入、范围和静态阶段；WP49.L005 的批次 12 是净化输入追溯，audit/source-traceability 的 1116–1129 行有对应条目，不是 R7-U12 导航整改。没有把三条非历史定位误计成新缺陷，也没有将旧证书扩成 B8 全文批准。

原 N01 对照继续区分半无敌放行与普通命中：目标无防守/模式破坏者真、q70 时，r69 与 r70 不同。原 WP50-R01 的 false 半血门、true 贪吃扩展、世代、forced、Nature、RIPEN 和消费层保留；本任务只接收旧关闭资格，未重跑行为。

父历史提供者的当前权威字段、U06/U08/U12 必要完整记录与七组共享接收已有限接收。U06 过程裁决明确不授 PASS，后继同 context 完整内容结果 `55a843b3` 另计；U12 原部分 WAIT 与 `fd112431` 完成结果分列；原作者/审者/时点不倒填。其它不相关完整历史载荷未重审，也不继承提供者的 whole243 FULL 声称。

当前 GR7-M04-102 的可调用前提仍为 optional；GR7-M04-101 的准备/受保护求值区别仍为 no_required_revision，二者不同根因。已读全部七组当前事实与裁决范围，未自动采用可选修改。R6/R7 其它政策不在本组替用户选择兼容方式。L01–L14 原记录全文已读，结合本域解释保留；可读 PBS/caller/compile/cache/reload 未接收继续是普通开放工作，不能改标宿主 limit。详见 [history-qualification.json](history-qualification.json)。

## 真实边界与主审整合

所选容器在 container_creation 阶段失败，随后 executor 配置也不可用。本次通过 GitHub 连接器完成不可变对象阅读、静态 JSON/NDJSON/等值/hash 验证与报告分支发布；本地 shell、工作树/缓存状态及原 Mac 保护审计均未冒称已核。本组静态材料已可取得，容器失败未用来豁免可读语义。

参考 Ruby、独立行为模型、native、游戏/Demo、媒体、真实存档/回放全部 `NOT_EXECUTED`。请求配置沿合同登记，实际 model/effort/tier/speed/Fast/opaque session ID 无权威回显均 UNVERIFIED，父 source_thread_id 不冒充当前 ID。工具失败、截断与修复范围如实保留，平台私有原始流没有声称已公开发布。

CONT-01 的穷尽子意义/反向支持、CONT-02 的必要当前 provider/caller/default/override/data 激活与流水线接收仍归原独占任务；本次只消除 CONT-03 的旧证据/历史资格接收缺口。主审接收本增量后负责合并判断与最终签收；未新增后续任务、自动审查层或整改。
