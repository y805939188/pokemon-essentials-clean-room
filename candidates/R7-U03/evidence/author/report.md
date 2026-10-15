# R7-U03 作者候选

状态：**CANDIDATE_READY_NOT_REVIEWED**。仅提交GR7-M05-001、GR7-M06-001的隔离候选，未正式接受或关闭任何问题。进度分母仍为27项/13批；旧56/92、L01–L14均保持。

## 固定输入与身份

已从origin的codex/remediation-seventh-20261015-cloud取回并确认派发提交6ec1d09e9c470954964d72761c83a760ef4f0364，完整读取该提交R7-U03-author.md及f622356f3beb9e84ea8cff9db07c7fb382565d3f的原七组/原入口。恢复工具和本批清单固定于658488c81f1f3181a488298ab27850c8af951d73，均先阅读再执行。

本独立容器实际恢复34文件/6,088,763字节并核bytes/SHA256/Git blob，resume全部复用匹配字节。原始提案、完整非作者C04两记录、根接收及全部149个具名JSON成员的offset/原字节SHA/JSON pointer/规范化SHA均另核。定向补取4个具体绑定输入（两个收到的提案、source/formal inventory）及12,802字节successor delta；没有读取80MB Manifest或扫描完整core索引。见input-verification.json、恢复回执、read-set.json。参考仅为固定R的所选只读快照，不冒称完整Git树/运行认证。

项目AGENTS.md全文已读；本容器/workspace/.agents为空、项目及固定提交没有.agents/skills，已如实登记缺失，没有伪称应用技能。真实环境ID、父来源线程与当前task/context未暴露的区别见context-and-configuration.json。作者请求gpt-6.1-sol/xhigh/default/普通速度；实际model、effort、tier、speed逐项UNVERIFIED。普通进程PID/UTC不充当模型认证；未创建子作者/reviewer，也未操作用户Mac。

## 本批变化与scope

- WP12：§4.1区分碰撞创建/完成及普通位移的开始/完成；创建不增全局步数/距离或发离格通知，正常完成可经一般通知进入合格玩家链；§8补失败/无完成更新的实际前缀，导航同步。
- WP61：§2/§3.1登记合格碰撞完成来源，保留强制路线、解释器、冰瀑自动运动、消费者中断及逐项次序；§11仅同步本批导航。
- 移动目录：限定MV01/MV02，新增R7-BP01–08，分别覆盖返回/完成、普通通行、完成前、触碰成功、失败对角、合法路线WAIT、一般/玩家消费者失败、无完成机会。
- 被动目录：新增对应R7-FP01–08；旧FP01–35、毒伤默认关闭、空寄养自身周期、非玩家受阻与MR02规则均保留。
- WP16目录：只修WR01的有效显示坐标实际增加128子像素输入及前后独立量化，并增加R7-CAM01–04小图、居中大图、右边缘与手动在途卷动对照。WP16正文及GR3-CAM06–08保持原字节。

只生成5份从B原字节建立的完整镜像；WP06算法与守卫正确，没有具体矛盾，不采用条件同步。不修改formal/reference/公共台账、main或tag。精确原B/新bytes/SHA/blob、行/字节范围与读写集见artifact-manifest.json及per-id.json；candidate.diff为零上下文差异（若工具消费需明确支持unidiff-zero），供逐条核对，不能用镜像覆盖其它批次贡献。

## 验证资格与尚待接收

validate-final-mirrors完成有界目录/差异位置/旧表行保持/新链接逻辑目标/JSON检查。共1,016个非目标旧表行保持原文（含表头/分隔行，数字不是行为案例分母）。该结果仅TOOL_VALIDATION，作者静态读源与纸面向量不作为独立PASS。所有新增行为向量仍NOT_EXECUTED；REFERENCE_OBSERVATION、独立完整模型、游戏宿主、Demo、native媒体与真实存档回放各0。失败/取消/部分提交按per-id.json分别登记，未把退出0提升为业务成功。

校验过程中第一次递归身份检查发现批清单外4个具体可读绑定，按精确C2对象定向恢复后149成员全部匹配；未把可读材料伪标limit。目录校验器先后因行号清单偏移、未排除本来就需修改的碰撞表行而退出1，修正校验器后通过；这些真实失败日志保留，不曾执行参考程序。首次git diff --check把标准补丁的空白上下文行标为尾随空白，命令编排的换行又使首个本地提交在该检查失败后仍生成；推送前已将补丁改为零上下文并重新完整检查，保留原提交，不reset/amend/force。该早期命令只有平台I/O，未补造分离日志。原始push输出也含远端尾随空格，按完整I/O要求保留，最终空白检查只排除commands/*.stdout与*.stderr，正文/JSON/工具不排除。初始侦察与内容读取仅有平台tool I/O，未另存逐命令UTC/stdout/stderr；不补造旧时间。后续commands/保存分离的可发布命令I/O、UTC、PID、退出，参考源正文不复制入公共证据，私有模型流不推送。

无作者前置批次阻塞；依赖仍OPEN：R7-I接收实际候选身份/scope并生成candidate-input.json，不同实际context的ultra审者复核，CG04（本批与U01/U13的移动目录）及CG05（本批与U09的被动目录）由R7-I串行按条款整合，再由新R7-IR审实际整合字节。WP12/WP61/WP06/Repel消费者与历史MR02、GR3-M03-001关系仍需最终接收，不自行宣称已满足全部直接/传递依赖或全历史回归。候选PASS、整合PASS、ACCEPTED、CLOSED分开。

## 传输与冻结约定

唯一成果分支codex/r7-u03-author-20261015-wave1，从固定B e646432c644dec04d306842cc5a559a29c718fbc创建。与B差异仅candidates/R7-U03/；只普通提交/普通push该分支。全部新文件进入提交。发布后按固定结果commit逐新文件完整HTTP远端读回并比较bytes/SHA/blob，另读远端branch及commit/tree。允许将首个候选内容提交的发布/读回回执提交为同分支后继证据；最终commit/tree及最终全量读回在最终交接中包外绑定，避免提交内自引用哈希。完成后冻结，停止写入，等待R7-I派发的ultra复审。

已完成首个内容候选的普通推送和完整远端读回：commit `9eeb3f72e677155348b5c9229be5fe0f5905a388`，tree `a1a3392d8a71d5273b94c1be49f6d58143d56d58`，73个新增文件逐个固定commit HTTP200完整读取，bytes/SHA/blob全部相等。完整逐文件回执在publication-content-readback.json，普通push及读回命令的I/O在commands/push-content.*、commands/readback-content.*。本次后继只加入发布证据及其身份/报告；5份候选镜像字节保持该内容提交不变。最终后继commit/tree及其全部新文件读回仍由最终交接包外绑定。
