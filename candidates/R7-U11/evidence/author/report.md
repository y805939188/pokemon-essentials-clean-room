# R7-U11 作者候选交付

状态：CANDIDATE_READY_NOT_REVIEWED。两项仅完成隔离候选准备；没有独立PASS、ACCEPTED或CLOSED。共享正式文件未改，完成普通推送和逐新文件读回后冻结等待R7-I派发ultra复审。

固定输入：远端 codex/remediation-seventh-20261015-cloud 的6ec1d09e9c470954964d72761c83a760ef4f0364；该提交的95行作者派发全文已读。原七组合同f622356f3beb9e84ea8cff9db07c7fb382565d3f全文1369行及原作者入口全文76行已读；派发明确只覆盖旧“不提交/不推送”传输限制。行为B=e646432c644dec04d306842cc5a559a29c718fbc，B实际Git根tree=84f79ec6e772aacbf3a464fde68cdc5a280e2950，正式规格子tree=ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c。唯一成果分支codex/r7-u11-author-20261015-wave1，从B创建；创建前本地/远端无同名分支，初始work分支干净。

本容器按已读的658488c81f1f3181a488298ab27850c8af951d73工具/清单恢复28文件、6,312,155字节，逐文件bytes/SHA256/blob匹配；同目录resume重用全部匹配字节。扩展核对normalized records20/22原始指针时发现5个具体binding载荷未在批次计划中；在固定C2精确logical_path查找，定向取gzip并核编码/解码身份，补394,874字节。没有假设共享目录、扫描80MB Manifest或恢复完整core；新增数据只是有界快照，不认证完整参考树。完整回执见recovery-receipt和supplemental-restoration.json。

GR7-M16-001仅改变WP75 §16-6分类句：从停用枚举移出单节档案装载器，另列兼容未加密宿主到达唯一Main、可枚举/可读与先前依赖正常时的条件发现/求值请求，并交叉引用§12.4。§12.4和§18原字节不变，保留899/900、失败分层、已加载前缀和无整体回滚；WP08收集范围不改。惰性token解析消费全部594字节，安全解压得到唯一Main49行，末尾调用可读；这只是TOOL_VALIDATION与SOURCE_STATIC，不是Ruby/eval、宿主启动或Demo。

GR7-M17-002在WP75 §14新增固定旧工具四目标请求表、门、互斥、失败/退出前缀，必要同步§1/§3.2/§17的入口和证据范围交叉引用。四外框/EDIT尺寸分别840×240/800×176、840×144/800×72、840×164/800×92、840×444/800×372；Batch按钮id1/id2只定位(25,392)/(150,392)。有限反汇编读取核8个尺寸请求点、2个定位点、数据、入口与导入；没有执行exe或Windows API。测试目录仅尾附12个独立静态向量，CV-M29及整个B目录前缀不变；审计T-WP75-01后附一段新静态证据，原批准输入记录不变；矩阵仅F18-04注记变化，不升级历史Reviewed状态。全新或旧向量均NOT_EXECUTED。原说明书两目标陈述、Interpreter只诊断、R6 L07运行/归属/自动启动未知、WP74/animmaker格式边界全部保留。

四个required镜像均从固定B完整原字节建立。未创建条件specs/demo镜像：无根明确继续维护/同步的依据，不扩大可选写集。exact scope与原B/新bytes/SHA/blob见edits.json与artifact-manifest.json；逐文件正式路径与候选的完整差异见四份.diff。合同写入范围仅candidates/R7-U11下四镜像与evidence/author；bootstrap/恢复输入在仓库外，不夹入提交。读集明确区分全字节身份/全文定位扫描与具体语义读取范围，见read-set.json；不声称全审计/矩阵/其它历史正文都获新的语义批准。

验证：28个固定恢复文件身份匹配；205处合同/normalized原始范围与canonical绑定匹配；594字节档案结构/49行文本身份核验；10个native请求点的静态参数核验；四镜像与B的完整差异和未改区间、目录原字节前缀、矩阵仅259行、正式跟踪字节不变及候选路径包含性检查通过。validation.json仅为作者工具检查，不是独立复审。L01–L14、27项/13批、旧56/92边界保持。参考/独立完整模型/原生API/宿主/Demo/native媒体/真实存档回放新增运行均0。

真实身份：作者平台thread/session从CODEX_THREAD_ID/CODEX_SESSION_ID读回为01a13f80-12b3-72ef-ab3d-8ba6a20af008，指令context=/root，父source_thread_id=01a13f49-a154-7054-9b04-ce31f924d01c。独立task/context ID与模型进程PID未暴露，保持UNVERIFIED；日志分别记录实际审计子进程PID。请求gpt-6.1-sol/xhigh/default普通速度、禁Fast；model/effort/tier/speed无有效回参，逐项UNVERIFIED。没有查额度或认证。项目AGENTS全文已读；本容器项目及固定输入没有.agents/skills，workspace .agents可见为空，executor技能列表为空，不编造技能读取。

真实失败与日志：003-input-audit exit1因新具名inventory绑定未恢复；补取5项后005-input-audit exit0。006-candidate-validation exit1因校验器把允许改变的矩阵备注列误纳入“不变列”，修正列选择后007 exit0，未据此改候选业务文字。早期一次组合侦察中xxd不存在（127），后续用Python定向字符串读取/objdump核对；组合最终0不冒充该子命令成功。初期平台工具I/O保留，但未独立记录逐命令UTC/stdout/stderr，不回填；持久公共包装从001起，保留各真实完整输出、退出与UTC。私有模型流、参考源文本和原始反汇编不推送；公共输出为身份/静态事实/工具验证。

未满足接收门：R7-I完整差异/身份接收与candidate-input.json；不同实际context的ultra非作者审查；R7-I处理CG01/CG03/CG07并串行整合；新的R7-IR复审实际整合字节；直接/传递消费者及精确历史回归接收均OPEN。没有作者排程前置边不代表这些依赖不存在。作者不自行派生reviewer、不正式接受、不关闭依赖、不改main/tag、不force或推送其它分支。最终commit/tree和普通push后逐新文件全字节远端读回由提交后的真实工具结果外部绑定，避免自引用清单；发布工具publish_and_readback.py保留该流程。运行结束后停止写入等待复审。
