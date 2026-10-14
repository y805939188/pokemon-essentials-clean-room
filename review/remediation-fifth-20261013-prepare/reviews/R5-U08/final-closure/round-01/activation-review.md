# CLOSE-04 / CLOSE-07 限定关闭字节复审

PASS_SCOPED_CLOSING_BYTES，返修0，阻塞0。固定core `13fddb0a217b36974c75657aa68da0caf104ee48` / tree `92a241ab8ca04f4f60211e60a2fa7cf284eb0c86`；locator `bd9399c30d56640cf4f336acfb71bb9f11ea7393` / tree `31f482807059d97f8f380e977e4627c5b3f8fe5f`；接受基线 `b0e5a90fe954a02f81e05c5c0062b977617bd1f0`。本签署只覆盖 CLOSE-04/07，不代签其他关闭门或未来激活。

92项各自的 current_effective 与精确已接受 ledger 一致：OPEN_REQUIRED、final_CLOSED=false；另存的 proposed_only_after_valid_activation 才为 CLOSED、final_CLOSED=true。逐项 ID/batch/severity、基线 formalaccepted、空关闭回执、候选 closingreview WAIT/receiptfalse 均核对。51P2/41P3，无缺项、重复或提前 CLOSED；当前有效 OPEN92/CLOSED0。gate-state、唯一U08接受、post-gates和activation-contract一致。eligibility、actualPASS、21shared或accepted标志不能越过关闭审查和唯一激活。

已接受 ledger 保存的旧 aggregate “review still pending”及 whole_shared_files WAIT叙述按明确后继限定读取：successor_scope、supersedes_current_U08_gate_state、精确U08实际接受字段已覆盖旧阶段，并仍明确closing OPEN92/CLOSED0。本复审不回写历史字段，也不把任何旧WAIT或已接受flag解释成CLOSED。

核心、locator、接受基线和当前工作树都没有约定 activation-receipt.json。未来唯一R5-I必须绑定准确core/tree/8载荷SHA/blob、同原非作者closing报告固定commit/tree/PASS/repairs0、b0接受/e9actual/formal1046/shared21和原92/410/568资格。回执选择**同一不可变载荷内**已审 proposed 对象；不改候选，不另造未审 CLOSED 台账。有效状态解析也明说旧 current_effective 是生成时点快照。身份/范围不符为WAIT，若状态载荷必须改变，先由同审者核新准确字节。现有actual报告不能替代新的closing报告，审者报告本身不能签激活。

必要引用闭环实核：input的proposal/gate/hash与core相同；proposal全部 prerequisite 与immutable-input-bindings吻合；引用各固定commit/path的bytes/SHA/blob已核。独审报告保留在外部独审域的固定debf提交，不要求导入当前locator；其余当前接收引用在locator/工作树保持同字节，closure-report五个当前链接都有效。e9/b0/core/locator正式树均为1046，support3同blob。未重读正式131或把原有限实际语义签署扩成全局签署。

同原非作者支持任务 `/root/shared_a` 继续，精确接受回执的 continued_original_support_tasks 包含本任务。父引用 `01a13807-81f1-7572-898f-31201a4dd026` 不是实测UUID；真实UUID/模型/effort/tier/speed回显均UNVERIFIED，请求sol/ultra/default/普速禁Fast不等同已验证运行设置。只读remote main仍 `9366d9d17aaeac3b4414236468affa650fb3dd27`（B5）。原环境/未发布成果保留、普通push和准确readback是后续登记纪律；本任务未触外部环境、push、merge、force、归档/释放/reset、正式正文、source或接受/激活，外部实体环境状态不冒充实测。

R4历史隔离4、R5原review4与本次update0分开保留。新增reference/model/host/Demo执行0；此处Git/hash/JSON/链接核验是TOOL_VALIDATION，向量或静态判断不升级运行PASS。精确读字节、92项逐状态结果及引用坐标见同目录 activation-reading-log.json / activation-results.json。
