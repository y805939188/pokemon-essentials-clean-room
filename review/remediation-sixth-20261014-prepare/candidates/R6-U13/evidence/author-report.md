# R6-U13-A 候选交付

作者状态：八个 required ID 已实际修订，供独立审者和唯一整合者接收。不是独立 review PASS、正式接受或 CLOSED；未写正式 deliverables、公共台账、其它候选目录。唯一作者分支从固定准备提交开始，普通提交/推送。

固定输入为 prepare `469a268b92daed7b4d28d7fd0da75520cbb7228f`，正式 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。父线程已发布的 c975a9d3 不替代本批基线。云端 repo 根 `/workspace/pokemon-essentials-clean-room`；没有操作 Mac。预置参考对象库未提供，已从参考远端获取固定对象到 Git 对象库、只读 `git show`；没有检出/改写参考源。

请求配置 gpt-6.1-sol / xhigh / default / 普速。actual model、effort、tier、speed、UUID 未获可信平台回显，均记 UNVERIFIED；未运行模型证明 CLI、未派额外代理、未自签独立审查。

完整阅读：适用根 AGENTS；485217 字节提示全文（8383 行连续分段），其首个 JSON 区块与合同字节一致；合同指定 28 份源全文、8 份固定正式全文；七份原反证全文。另完整读取 Challenge_Data 与 Battler_Initialize，必要共享消费者单位 WP09 全文、WP17 §3.3.1/§7、WP65 §4/§6、WP66-A §4.6。逐段机器记录在 reading-ledger.jsonl；初期提示/AGENTS/三小反证的读取早于记录助手，其实际阅读声明与分段/身份在 input-identities.json，未补造 UTC。

| ID | 实际修订与逐项验证 | 状态 |
| --- | --- | --- |
| GR6-F-001 | WP55 §2.3 列出内层清理、外层身份/注册/六计数及内层轮次上限保留。WS-W13/W36：有效开始后取消恢复O，六计数5/2不变；再结束当前0/0、最大/上次保持、身份−1、玩家队伍nil、无保存/刷新；直接胜利结束、无快照取消、取消再开始、未开始结束独立对照，W30原规则保留 | AUTHOR_STATIC_COMPLETE |
| GR6-F-002 | WP54 §2.1/2.3：正数界面读取值才限制加入；最终下限/上限独立。QC-Q48核0/1/3的注记、容量、焦点、首错、返回身份；Q49区分原始负数读取6与标准样本读取−1/最终6，七员仅为直接最终判断工具输入。普通3/4杯、nil取消、空数组提交不改 | AUTHOR_STATIC_COMPLETE |
| GR6-F-V001（含 F-004、C AF001） | WP56 §3.1与PA-P14/P15/P29/P30：状态1在执行/PP/记录门后，状态2只证明目标分支完成，结算限当前存活者。Tackle→Protect伤害0却技−2；普通命中＋1；状态1/保护真夹具保留旧槽；无目标反射原使用者一般＋1可与失败历史并存；最后整体失败不补记与稍后结算消费待状态分别限定 | AUTHOR_STATIC_COMPLETE |
| GR6-F-V002 | WP58 §1/3字段表及RC-W27：构造默认与准备后现值分开，fallback indoor1、Cave地图time2、环境/基值按解析或覆盖；捕获18键与回放恢复保持、不重新准备；跳过与准备异常前缀分开 | AUTHOR_STATIC_COMPLETE |
| GR6-F-V003 | WP56自动入口、WP58不记录项、RC-W18/W28：Tower/Arena普通菜单显式开Mega/AI正常登记才能执行且不录；Palace玩家/AI自动入口在登记前返回，资格本身不产生Mega；旧待登记清理与外部登记排除 | AUTHOR_STATIC_COMPLETE |
| GR6-F-V004 | WP56 §3.2、差异表、WP40 §5.2.1、PA-P16/P31：只取消列明持续招；存活未替代者回复期2→普通回合末1→裁判仍1，下一轮回复门有效；败者倒下/补位清效另算，取消逆鳞不附带结束混乱 | AUTHOR_STATIC_COMPLETE |
| GR6-F-V005 | WP56 §2.5、PA-P32：严格最大从0开始；合法1/205取整0无best，h24/r0/factor30命中走后段标记true并换；3/205取整1走best早返、标记false；无合法后备真标记/假返回、正同值先者保持。独立整数算术已工具核验，P12/P24原义不改 | AUTHOR_STATIC_COMPLETE |
| GR6-F-S001 | WP53 §2/8.3/8.4、SF01/30/36–40（覆盖S001-A–E）：专门Save区域/活动门与普通Quit Game分开。活动Safari字段与捕虫player单员/global spares/K/origin进入序列化的成功前缀；拒退出回菜单，拒保存/覆盖仍退出；IO只回退计数、其它前缀保留，未捕获异常不保证退出尾部；重载时钟未证 | AUTHOR_STATIC_COMPLETE |

原反证的口径：root提案及generator旧包关于失败确认后沿用Entry局部变量误进Summary的推断，被 isolated-entry-rejection-counter 的实际 Ruby 块局部变量结果纠正。本候选采用已证人数门/最终校验规则，未写误入Summary或其异常承诺。GR6-F-003地形遗漏是 optional，不实施；不能用它把18键扩大为完整状态。旧审者/提出者运行结果不作为本作者新执行。

证据层分开：SOURCE_STATIC＝固定源和正式文本完整阅读；DERIVED＝上述状态/分支向量；TOOL＝身份、分段覆盖、allowlist、实际diff、计数/唯一性、原行保留及独立整数算术；REFERENCE_EXECUTION / ISOLATED_WRITER / BEHAVIOR_MODEL / HOST_UI / REAL_SAVE / RELOAD / DEMO均未执行。未实现 TS 引擎或源行为仿制模型。测试目录每条仍声明未执行。

精确历史回归在 historical-regression.json：R1按原WP限定；R2按B12/B13的局部/共享贡献身份及裁决范围；R3/R4只读实际相交文件的原scope，改变的WP40仅回复期句尾，旧主体逐字保持；共享pokemon测试的BP/FP/PD/VF/LT后缀逐字保持。R5执行前拒绝、节拍器、异常重试主前提及原受影响段保持。新检查不是转移旧PASS。R2 229/21/341、R3 23/76（M09 optional/U08未开始、M02无必修）、R4当前17/76与B5旧16/75、R5唯一92CLOSED的原限定保持；旧FAIL、两MISMATCH、SC跨LF排除、optional7/noRequired7/policy6/limits13及原静态/执行分期不改。

唯一整合者接收事项：本候选八文件与 changed-spans.json；公共追溯/矩阵/计数/接受由R6-I更新。WP66-A固定正式§4.6第132行仍无条件写“达到规则人数后再Entry提示上限”，须在该共享文件接收本批“界面读取值>0”限定，并重验其消费者；其第236行同样引用最终失败后继续，正常块局部变量结论保持。WP65 §6.2 Save行的“在Safari中”按区域查询解释，普通Quit Game和四组合既有规则保持。WP17确认期间更新门要求无无关到期/其它回调前提；不扩大为暂停时钟保证。必要接点已只读定位，未越本批allowlist写共享文件。

剩余门：父线程指定非作者审者逐ID候选审查；R6-I实际整合后共享全文独立审查、直接及传递接口接受、精确历史回归、正式接受及最后关闭登记。作者范围内无未解决源事实；宿主/媒体/真实保存与重载时钟、接待事件材料仍按既有scope保留。

修订01：固定非作者报告 `3ef4854ef43eac92fd1dc57350e4cf6aa160082b` 判冻结00b45de6候选 FAIL：S001的SF30丢失正常保存/载入及默认无专用模式迁移两控制，另有R5路径说明和工具证明能力勘误。旧FAIL保持。本后继在SF30同一ID恢复两个子例，保留菜单对照；三条R5恢复说明及生成脚本纠正，原失败原因保持未知；原始行唯一性及SF30文本检查补强，并撤回因子30常量的独立概率计算证明。七份其它镜像与S001正文均未改，仍40条SF/新增14ID。完整差量、反向工具控制和待复核边界见 [修订01](repair-01/report.md)，本后继待同一非作者审者复核，未标正式接受/CLOSED。
