# R6-U07-A 候选交付

状态：AUTHOR_COMPLETE_CANDIDATE_READY_FOR_NON_AUTHOR_REVIEW。七项作者静态自检完成；非作者候选审查、实际整合复验、正式接受和 CLOSED 均待父线程安排，本文不签独立 PASS。

固定准备提交 `469a268b92daed7b4d28d7fd0da75520cbb7228f`；正式输入 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`；参考输入 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。唯一作者分支 `codex/remediation-sixth-r6-u07-author-20261014`。实际根 `/workspace/pokemon-essentials-clean-room` 等价映射历史 Mac 根；只写本批 mirror/evidence。未启动 CLI 或额外代理。请求模型 gpt-6.1-sol/xhigh/default 普速；实际模型、effort、tier、speed、平台 UUID 无有效回显，均为 UNVERIFIED。

| ID | 实质修订 | 反例与保留对照 | 本批静态验收 |
| --- | --- | --- | --- |
| R6-DX-AN-001 | WP74 §4.4/§6.3/§8.2/§19；AN-M05/B20-C025 | 0/2 两使用者允许删未锁 0；2 换到 60 后计数 1、拒删且无写；换回恢复。空槽前置放行、锁定/图案顺序及重置字段保留 | 完整回源删除门、复制/重编号生产链、TAB/键盘/清空消费者；槽 60 存储与不可渲染范围保留 |
| R6-DX-AN-002 | WP74 §3.2/§7.4/§11.1/§16；AN-M09/M12 | A 默认 4/位图可用，Delete→B→BACK 后 Focus Target 写 B=1，A 仍 4、画布新增仍 4；保存/导出取 B。取消/重新 Load 对照；空选中槽失败早于菜单 | 集合成员与画布对象消费者分别定位；未保存缓存可见性、失效不回滚保留 |
| R6-DX-AN-003 | WP74 §10.2；AN-M23；WP67-A 全文一致性核查保持原字节 | 捕获中心 128 后槽 0 移至 200，槽 2 仍 128；预览加 64 为 264/192。不移动/Screen 对照；双方沿已建立线段、球爆开可显式覆盖目标锚点 | 捕获时点、逐帧消费者、预览与战斗建立者完整回源；20fps、时序、正常恢复与异常未知保持 |
| R6-DX-AN-004 | WP74 §8.4 的 11 项范围/初值、§9.3 七项范围/现值优先；AN-M16/M22 | 旧 Opacity17 只勾直接确认写255，Zoom100/Priority1；渐变 X550 工作值500，取消保持550，合法20保持；全不勾/空槽/共享属性保留 | 各控件构造、勾选消费、即时钳制与取消门分别核查，不把属性页现值当批改初值 |
| R6-DX-AN-005 | WP74 §11.2/§19-11/§20；AN-M25 | 仅外部类型正确、长1/空帧0/空图样/空时序夹具：转换跳帧、槽先替换，随后画布更新失败；缓存可见、未保存、无槽回滚、宿主结局未知。有效结构/坏解码/错类型保留 | 覆盖补充，级别 P3 保持 root 裁决；不推广正常 UI，不指控全部坏结构已有回滚承诺 |
| R6-DX-AN-006 | WP74 §8.6/§19-8；AN-M18 | 同窗旧 P→重开 Curve→未显示线 BACK：点标记清、P留，OK写旧 P；首次无 P 不写；外层取消不写；Freehand首ESC换为空路径，保留先扩帧后失败 | 路径变量、可视点及 OK 写入链完整阅读，三套采样和已显示线 BACK 仍生成新路径保留 |
| R6-DX-AN-007 | WP74 §8.6默认控制点/§19-8；B20-D024 | 默认0→300的中间点按0.3333/0.6666请求约99.99/199.98；量化未知；显式四点N5原向量保持 | 只落实 mandatory 默认点。一般 N 浮点递推位级兼容仍为独立 optional facet，未修未纳入必修 |

本批实际改动两个镜像：

- `mirror/deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md`
- `mirror/deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`

第三个允许镜像 `mirror/deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md` 保持固定基线字节。整合者应接收精确差分，不能用整份共享测试目录覆盖其他批次；WP74 与 U09、测试目录与 U06/U08/U09 的接收和整合审查仍待 R6-I。唯一整合线程为 `01a13a93-d1da-71e4-a488-63b8524f503d`。原 specs、公共追溯/覆盖和台账由 R6-I 按整合结果同步，作者没有写入。

完整七组作者记录见 `author-evidence.json`；30 项实际正文/向量修改与逐 ID 对应见 `revision-operations.json`；可审零上下文差分见 `candidate.patch`（按固定基线使用 `git apply --unidiff-zero`；共享整合仍按逐 ID 操作接收）。三个正式基线全文（1147行）、七份指定参考全文（5130行）、原 WP74 全文（560行）、七个完整合同记录、原动画反证及相关历史精确范围均已阅读。读取过程中对重复原值采用可逆的字面锚点，未用摘要替代；截断输出及失败读取的纠正见 `early-and-read-attempts.json`。原始行号和身份见 `read-journal.jsonl`、`semantic-read-coverage.json`、`history-scoped-inputs.json`。

验证分层：SOURCE_STATIC 为作者新回源与手工反例；DERIVED_VECTOR 为七项状态推导及四组独立常量算术；TOOL_VALIDATION 为固定 bytes/SHA256/Git blob、写集、历史保留性、测试行顺序和差分检查。`validation_package.json` 记录 Python 3.12.14 的准确 argv/cwd/UTC/stdout/stderr/独立退出码 0；317 项检查零失败，多数是字节/保留性检查，不能称为 317 项参考行为运行。30 项修改按固定镜像重放后与最终两个镜像逐字一致。

R1 原 WP74 具名资格与18项旧关闭限定、R2 229/21/341、R3 23/76、R4 17/76与B5 16/75、R5唯一92 CLOSED原范围均保留。当前 §4.3/§4.5/§4.6/§6.1/§8.1/§8.3/§8.5/§9.2/§10.2a/§14.1/§15/§17等原条款和未改测试行逐字保持；C025/D024/C032与共享旧值等精确历史 scope 新核，不转用旧 PASS 给新改动签署。没有重开历史 FAIL/MISMATCH/LF纠正，没有扩大任何旧分母或独立政策。

参考定义、隔离替身、完整行为模型、宿主、Demo、真实保存/媒体执行均为 0。无新增实质阻塞；实际像素/音频/输入/序列化与异常收口保持未知。独立 ultra 候选审者须绑定发布后的实际 commit/tree 与载荷 SHA，完成正常/反例/取消/失败前缀及历史、接口复验；作者自检不能替代该验收。

发布身份由后继有限发布回执和最终响应绑定；manifest 不递归自哈希。
