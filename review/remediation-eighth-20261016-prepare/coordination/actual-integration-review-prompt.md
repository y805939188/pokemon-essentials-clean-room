# 第八轮批次实际整合独立复核入口

本任务在所属批次候选独立PASS且正式目标已串行整合后启动。父任务须提供批次ID、真实候选commit及独立候选报告、真实实际整合commit、完整实际diff/逐项变更记录，以及明确的独占审查输出目录。缺少冻结输入时报告BLOCKED，不以当前分支HEAD或候选镜像代替正式目标。

配置为 `gpt-6.1-sol / ultra / service_tier default`、普通速度、Fast关闭。保存实际创建设置的证据，区分请求、创建设置和运行时回显；无法设置或存在冲突回显时报告阻塞，不换模型/强度/服务档。未提供的运行时回显记UNVERIFIED。审者必须是实际不同于作者的context；可以续用原合格候选审者，续turn不增加独立人数。作者或整合者不能给本人改动独立验收。

固定原始交付为 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`，B8为 `fd1df570cad987dc3852a3b958f03916e317f7fe`，只读参考为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。完整读取AGENTS、原审查inputs/review-SKILL.md、所属批次的 `review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/batches/<批次>/reviewer-prompt.md`、所属完整合同、必要readset及accepted-facts/history/policy伴件。

本次独立核验实际整合后的完整受影响文件及必要消费者，确认：

1. 候选独立报告确实PASS且绑定被整合的真实候选；所有回修后的输入和报告对应。候选PASS没有被登记成实际PASS。
2. 该批全部required修订及明确采纳的optional准确进入正式目标，原证据、章节/锚点、正反场景、引用/索引、验证资格可以逐项追溯。对候选与实际整合的差异逐项核清。
3. 正确且无关的内容、原测试ID/计数/别名、失败前缀/取消及早期门均保持。共享整文件及必要公共索引贡献完整接收；不能只读改动行。
4. 核对 coordination/integration-plan.json 中与本批有关的跨批接点。其它批尚未满足的关闭前提应明确指出，不能因九批编辑DAG为0跳过实际共享接收。
5. 正文符合clean-document-revision，不含纠错补丁式解释、无关架构或新框架实现。原版行为修正不因未来Showdown计划而省略。
6. 不执行Ruby或开发框架；静态推导、数据/元数据工具校验和参考/游戏/宿主执行分开，未执行的向量仍为NOT_EXECUTED。
7. 参考、main/tag、原历史审查及旧接受/关闭回执、用户修改和其它批贡献没有越界变化。U07采用后继overlay，不改写原历史；U06 WP67-A和U09共享Creature catalog按完整保持范围接收。

只写父任务分配的独占review证据目录，不修改候选、正式目标、公共登记或他人报告。输出实际输入commit/范围/审者及配置证据、实读和证据复用资格、逐ID结论、保持范围检查、actual integrated PASS/FAIL/BLOCKED、精确阻塞及最小回修要求。不给整轮交付或打标授PASS，不自行登记ACCEPTED/CLOSED。

整合者收到合格actual PASS并确认必要共享/历史接收后，可登记该批ACCEPTED，向打标任务提供真实接受commit、回执、全文diff及受影响章节/锚点/行为/去向delta。这一批次接受是打标回填的前置事实，不等于最终整轮验收；CLOSED由最终整体验收后的后继登记负责。U07无正式章节变化时明确记录NO_FORMAL_DELTA，不虚造受影响功能。
