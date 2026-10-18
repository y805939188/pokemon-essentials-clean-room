# 主线程直接派发入口

这四个任务已具体冻结、尚未启动。本接收者未自行spawn；用户要求由主线程新上下文并行。派发时用本次最终消息给出的**实际发布commit C**读取这些文件，并将该C一并传给每个上下文；不要解析同名分支未来HEAD。载荷输入固定805468320bf8a44499f6d59f53820215b27899fb，原受审目标90b9e27ef03feb2c018bb2f258b5e0d5aaed012b。

| 逻辑任务 | 独占记录对数 | 完整prompt | 完整readset | 独占写集后缀 |
| --- | ---: | --- | --- | --- |
| receive_elr_records_a | 2756 | prompts/records_a.md | readsets/records_a.complete.json | continuation/parts/records_a/ |
| receive_elr_records_b | 1620 | prompts/records_b.md | readsets/records_b.complete.json | continuation/parts/records_b/ |
| receive_elr_records_c | 1061 | prompts/records_c.md | readsets/records_c.complete.json | continuation/parts/records_c/ |
| receive_elr_records_d | 4827 | prompts/records_d.md | readsets/records_d.complete.json | continuation/parts/records_d/ |

表中路径相对于本contracts目录，完整仓库前缀为 `review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/receive_external_localization_records/`。每个prompt已包含完整执行边界；COMMON-CONTRACT.md是强制全文共同合同。dispatch.json绑定全部prompt/readset/view/原业务字段/身份索引的字节身份与全部ID，validation.json核并集10264且与既有433无重叠。

主线程给各上下文的启动指令应明确：执行本表的具名子任务；从该实际固定C完整读取本prompt、readset、COMMON-CONTRACT及其引用全局prompt/AGENTS/skill；禁止仅使用摘要；不得自行spawn或整改。请求gpt-6.1-sol/ultra/default普速/Fast off，实际逐项无权威回显UNVERIFIED。实际上下文必须不同于原作者01a143ad-a413-739d-b640-d4896e2e5029及父接收者01a14465-d18e-725b-b69c-2e6f52300005。

四个任务可并行读取共享定义，写集完全互斥。完成后各自普通push专用分支，仅回读自身增量报告载荷；父接收者按真实固定C接收全部实质贡献并合并各ID的真实阅读，不按任务退出或READY计PASS。父仍负责七接口、全部35PBS必要值、125反向source-linkage、历史原合同/canonical和213目标载荷用途/语义收口。全部全局task-final仍由主审签字。
