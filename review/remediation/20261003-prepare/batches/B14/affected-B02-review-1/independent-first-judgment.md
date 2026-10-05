# R-B02：B14 candidate2 独立先行判断

本记录写于阅读 B14 candidate2 的 fix-response.md/json、revised-identities.json、validation.json、staged-validation.json 和作者修订解释之前。此前仅读取委托、AGENTS、B09-C 下游合同、candidate1 请求性质的 B02 reverse-impact package、candidate2 的有界范围授权、正式候选差异和固定参考静态文本。范围授权只确认可改路径，不证明正确。

被审身份 af39efbf32549be964cb083bd49bed6d1d5c0d2a；接受前驱 1e6b11a47370f1c7c4659a32443fc1afda597bac；candidate1 47f7514765f8569ae9172bb06a2cd615e2b83b8a。完整前驱→candidate2 共46路径、正式12路径；candidate1→candidate2 共22路径、正式8路径。审查不是仅增量审查，也不是重批准 WP59–61 整域。

独立结论：**PASS_SCOPED（B02 受影响接口）**；目前未发现本范围新增阻断项。结论基于以下独立证据，不继承作者通过标签。

- 固定参考 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b，独立仓库 /tmp/r-b14-b02-reference；tree 7589c800b61ba13a13040ed0d686979b80a84fd0，origin 与 clean 已验证。Weather 239–289：合法活动水花重置把 opacity 写255，update 到期调用后立即返回；普通更新才适用剩寿命<.2。故 .40重置255／后续.30为0／.19为255相容，不能将重置当次套隐藏门。原/最终 WP16 单句与 WT31、WP59 相容。
- BerryPlants 97–159：未种植及 time_delta≤0 早退；覆盖物先修正参数；重植上限 reset/return 是另一分支。正常公共写为 time_alive、growth_stage、time_last_updated，再分旧雨水/新干涸。已存 GROWTHMULCH、旧对象显式结算、3h、9h首生命周期给8100秒与阶段5；不推出旧UI施肥或普通旧显示链调用。BP18 与原/最终§5.2保持此层次。
- FieldMoves 471–512、MessageConfig 559–591、Overlays 8–44：FLY 计数/落位/BGM/refresh 在 optional yield 前；该处普通异常且演出 ensure 正常结束时，后续等待和两个记录清理未达，异常继续传播。正常返回才按先 E 后 D 清理后 true。地图转移成功不能代替整个工具正常返回；内部正常 false 与外层 true 保留。窗口只能在另有合法更新机会时推断 D 守卫优先，不推断未处理异常后游戏继续。普通静态菜单调用点未见传回调。
- Time 82–109：缓存门 System.uptime 差≥30，重算取宿主分钟；关闭开关返回旧缓存。新 WP59 表/WT03/WT37 与 B02 WP06/TM14 不冲突；同端点06:30及23:30数值本身不足以证明插值/回绕。
- BerryPlants 437–470 与当前 WP60§6.4、WP06统计目录/TM09：确认/容量先于 picked、qty阈值、入包；阈值单位仍单株本次果实数。BP14 是终态列举且字节未变，不把外层植物重置插到工具内或改成株数阈值。旧 BP07、BP13 也字节未变。
- Overworld 172–185、Character 981–985、Player 543–552：普通步后回绕先于玩家周期与遭遇门；强制/解释器早退不加计数。实际完成移动的一般通知与步后早退通知可两次，新增限定不破坏 B02 TM12 的直接入口一次和计数前提。
- 独立 Git/hash/text 审计已通过：两共享目录非 WT/FS/BP/FP 整段字节保留；全部旧 ID 顺序/重数保留。311→329与141→148，只有13个 WT/FS旧行、6个FP旧行变化；新增18+7行。B02原13正式路径及 B01 EP01–21 均字节保留。72个合同输入按当前前驱或明示历史SHA验证；C003完整4根裁决/8扩展与固定原对象、有效 acceptance 相等，B02全部12完整对象/acceptance哈希吻合。

所有例均未执行。U01–10/G01–12/AX01–20与具名未读材料保留；运行观察、Demo链、静态行为向量执行、子任务均0。canonical229 OPEN/0 CLOSED。C003全局各扩展、A015 B16、A017 B21/A-REG及 C081 全局合并验收责任保留；B08现有已接受修订不能被旧B02记录写成当前未修。候选意见不替代未来 exact actual integration 受影响复核。

补记（打开作者响应后的独立计数纠正）：初版行计数正则只接收无连字符的 ID，漏数28个 B04-R 行；前述311→329是该子集的计数，不应称为目录总数。修正 reviewer-owned 文本审计后，完整目录是339→357与141→148，总480→505；全部480个旧 ID 的次序及重数、所有者外整段字节仍独立通过。candidate1→candidate2 是503→505，仅 WT28/BP18旧行变更，新增WT39/WT40。此纠正未改变语义判断；审计代码、完整记录和最终报告采用完整计数。作者数字仅提示复查，不作为通过依据。
