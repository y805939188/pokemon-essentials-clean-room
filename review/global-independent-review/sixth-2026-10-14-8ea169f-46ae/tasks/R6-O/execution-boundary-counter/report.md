# R6-O 本轮执行与限制独立反证

已独立核对要求的探针脚本、原始完成命令、结果及限制记录，没有重跑探针。下列进程数、当前保留向量、被捕获异常和工具断言分别计量；这份反证不裁正式提案、不修formal，也不把源请求视作宿主结果。

| 记录 | 实际进程与结果 | 证据边界 |
| --- | --- | --- |
| O | 5次Ruby：3个exit0、2个exit1；当前22向量＝Fishing7＋Owner5＋Phone10 | 第一次错误路径未加载R；第二次原Fishing部分执行后缺x替身停止。成功三次执行原定义／协调器。预期异常向量不增加失败进程。FishingUTC未捕获；Owner／Phone具实际UTC。 |
| K | 2次原Ruby；2个tee管道exit0，Ruby独立exit与实际UTC未知；2bag回调＋5Owner向量 | 日志“TOOL_VALIDATION”不是正确源执行分类；原定义和回调确已调用，应记隔离源执行／替身观察。没有普通完整迁移、真实save或UI；更新时间不补运行时间。 |
| CA | 1次原handler进程exit0；24行含9个诊断捕获NoMethodError、15个无异常 | 9不是失败进程；稀疏数组／随机／诊断替身，不是完整战斗或频率验证。 |
| F | 3种脚本，实际5次Ruby：4个exit0、1个exit1；当前结果10例＝5＋2＋3 | 首次坏menu替身误入Summary；修正后成功。entry脚本又做一次换物种标签的成功重跑，旧输出被覆盖；不能声称只有3进程或13个独立保留向量。Game.save计数只是内存请求；录制包由夹具自造。 |
| UI | 5次Ruby：4个exit0、1个exit1；有效夹具3成功进程，当前7例＝Purify2＋Capture2＋Bag3 | Purifyv1/v2缺Sprite.angle；v2捕获错误exit0仍是无效夹具。v3补继承reader后首刷新成功，原怀疑撤销。Capture／Bag故障为注入消息异常，不是物理用户取消。 |
| CM | 19与150个算术断言，另generic Ruby Array／名字查询语言探针；源执行0 | 算术案例有重叠；不是169个独立战斗向量或完整模型。语言探针未加载R，不能证实真实工厂／compiler／host运行。 |
| SF2／PE | 两条具UTC的root重解析工具命令exit0；源执行0 | 读取PCM／RIFF／PE／CIL字节、解析外部MemberRef或完整IL不加载synth、EXE、DLL、IL；没有真实声音／GPU／WindowsAPI／CLR结果。 |

所核Ruby尝试合计18：已知exit0为12、exit1为4、独立Rubyexit未知为2；其中1次未加载R，其余17次进入原定义／协调器。合计仅是上述指定家族，不能当作全队所有工具调用普查，也不能把exit0等同于语义PASS。向量保留各家族原分母，共享Owner案例／F重跑／无效Purify版本没有合并为全局唯一向量。

本轮记录没有完整原宿主、Demo、独立完整玩法模型、真实save、网络／外部服务或物理Input执行，均0。Sprite／Bitmap／音频资源请求、保存请求、时钟／抽样和动画调用只证明源侧发起或替身记录；实际可见／可听／持久化结果仍未知。model／effort／tier／speed／UUID无实际回显，均UNVERIFIED。R6-B剩余native CFG/dataflow、runtime／兼容选择、GPU精度／拼接／采样、WindowsAPI／CLR及未选字符串候选limits保留；字节工具成功不消除限制。算术oracle确执行，但完整游戏或战斗模型未执行。

**INC-R6-001须保留真实流程违规。** UI Party最初汇总命令遗漏cwd，在仓库根创建`build_review.py`和`forward-matrix.jsonl`两个新untracked文件，随后移入自己的任务目录。现根路径不存在、protected tracked无差异与R clean只能说明当前状态及保护检查，不能改写为全队从未越界写入。它是过程事件，不能制造formal缺陷ID。报告时间也不当作创建／移动实际UTC。

`counts.json`为分层计数；`process-evidence.json`保留实际命令／退出／输出字段及缺失元数据；`artifact-bindings.json`与`reading-ledger.jsonl`锁定新读工具体／指定记录。既有错误夹具、失败、被覆盖重跑和修正均保留。只写本独立目录，未运行参考程序、未知脚本或宿主来补证。
