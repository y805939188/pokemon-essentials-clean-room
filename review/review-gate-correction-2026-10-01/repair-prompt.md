# 第一组三包有限修订：修好并送复审前不进入第二组

在 `/Users/dingshinn/Desktop/pokemon-framework-reference` 工作。用户已澄清：某次review发现问题就先修复、复审通过后才能继续下一包／批；全部WP处理完后再做整体double review。旧“带问题继续、留到最终统一修订”的提示不再有效。

## 本次范围：29项全部处理

先读AGENTS、planning/extraction-plan.md §2.2、本目录correction.md／issue-ledger.json／inputs.json／final-checks.json；再完整读取下列两个审查报告及findings.json：

1. review/wp66a-progress-review-2026-10-01/：WP66A-R01～R09、C01～C03，共12项。
2. review/wp63-wp64-progress-review-2026-10-01/：WP63-R01～R07、C01～C03，共10项；WP64-R01～R05、C01～C02，共7项。

仅修这三份主稿及必要的场景、交界、矩阵状态说明、fixed／self-checks／摘要／身份登记：

- specs/ui/wp66-a-party-and-summary-ui.md
- specs/ui/wp63-pokegear-map-music-and-phone.md
- specs/creature-rpg/wp64-mail-and-mystery-gift.md

逐项回源核对，按finding给出的最小场景更正行为与输入前提。若确有新证据推翻某项，写出原ID、证据和反例交reviewer裁定，不能静默跳过。清理正文总述、表格、例子、自检和摘要中的同根因重复错误，不能只改一处。

## 修订重点与同步

- WP66-A区分普通菜单换位与ACTION快捷、事件选招与必选、交易助手各入口、缓存资格与显式刷新；按真实顺序记录邮件部分提交、Box Link返回夹限、背包／队伍机器路径及入场前置。
- WP63修正电话注册与查询包装、再注册、倒计时、BGM实际播放覆盖、地图缺失失败；完整哈希与编辑／问候边界同步。原WP13绑定以磁盘实测替换，不凭前缀补全。
- WP64补邮件取下前置，限定礼物ID过滤、下载与解码失败、管理内存与落盘范围、调试取消的成员状态写入；同步ID合法域与对象转移。
- 已正确承接的FLY取消、邮件快照次序及部分提交保持正确，不为统一措辞而退回旧错误。三包间修改后的完整身份引用要同步。
- 本次来源与reviewer原件、快照保持只读。新建 `review/wp66a-wp63-wp64-revision-2026-10-01/` 保存逐ID回应、实测输入、真实读段、修订diff、自检、场景及当前身份；旧被审交付／审查原件留史。若需要承接活动登记，明确新修订材料与历史材料的角色，避免覆盖旧版本证据。
- 29项回应必须完整列出，含原问题、修改位置、来源、场景预期和自检结果。修订后标“已修订待定点复审”／ReviewPending，不自行CLOSED或Reviewed。
- 正文与上游材料先定稿，再计算摘要引用，最后更新manifest／主TSV；完整哈希与字节从磁盘生成。登记完成后的最终检查单独保存，不自登记进其描述的清单。

## 停止点

修订完成后交付材料并停止，送定点复审。**不启动WP65／WP67-A／WP67-B或其它新包。** 较早GR-001～016另有16项已知整改，本次不混入三包行为修订、不关闭它们；第一组通过后仍需处理该清单，不能自动恢复新包推进。N01已通过结论不重开，管理性回填和B批整合不在本次范围。最终double review用于检查额外遗漏，不能代替当前问题闭环。

reference只读；不运行参考实现／游戏／事件解释器／编译转换／生成器／真实网络或未知序列化载荷；不实现新框架、不设计API／类层级；不创建任务／Agent、不发跨会话消息、不提交／推送。
