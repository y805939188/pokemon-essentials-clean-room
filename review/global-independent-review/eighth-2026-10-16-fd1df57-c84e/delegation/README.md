# 第八轮云端独立全局审查：冻结与可派发分工

这是启动分工检查点。全量语义审查仍在进行，当前没有全局 PASS，也没有宣称全部条款/结构分母已闭合。后续整改尚未启动：`UPDATE_NOT_STARTED`。

完整合同在 `../inputs/eighth-global-review-prompt.md`，36653 bytes，SHA256 `63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b`；最终态修订技能在 `../inputs/review-SKILL.md`，3598 bytes，SHA256 `ac3c8560f38192269b65b061673896a77f5eb794b90e90644e3c445b2c3be1f8`。两份已全文读取并核同字节；Library 直接下载在本环境 DNS 失败，合同副本来自完整 Library read 文本、经精确字节核验与官方 metadata helper 关联。

当前 B8 规格仓库 `/workspace/pokemon-essentials-clean-room`，固定 commit `fd1df570cad987dc3852a3b958f03916e317f7fe`，tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，正式 tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`。R 在 `/workspace/pokemon-essentials`，固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；固定 commit/tree 均已实核。实时远端 main 和交付 tag 准确指向 B8，云端没有本地 main/origin-main/tag refs，原 work 分支保留。

实际机械分母 R432、formal131；14组 domain readsets 覆盖两者各恰一次，库存审者另行核得漏项0、重复0。87条 WP 计划行与113功能组及全部配套/测试路由正在接收；逐结构/条款/有效补充分母必须由实际领域阅读闭合。所有 inventory_only 和 UNREAD 均不能改称 FULL_READ。Mac 状态只是历史证据；主线程已确认 R 中历史两个额外文件为 Finder 元资料，不是必要语义材料。

`scope-freeze.v1.json` 和 `readsets/*.json` 是穷尽 primary 文件路由，允许跨域依赖全文读取。当前六个实际独立上下文分别为 `/root/inventory_denominator`、`/root/history_current`、`/root/preflight_resources`、`/root/kernel_review`、`/root/creature_review`、`/root/combat_review`。合计 root 在内7个活跃上下文，达到当前 collaboration 工具提供的7槽容量。全部请求 gpt-6.1-sol / ultra / default普速 / Fast off；实际没有回显的字段逐项 UNVERIFIED。

`first-wave.json` 给17个可立即独立读取的未启动任务，全部列出 prompt/readset/独占写集。它不重复启动现有6个上下文；COM-CORE继续由现有 combat_review 承担，6个未启动战斗子片补其余完整范围。每个任务读完整合同、全部指定文件/结构/clauses及消费者，交双向映射、反例提案、真实已读/未读/未接收与执行边界。共享正式文件/公共状态仅 root 写；独立反证必须由实际非提案者上下文承担，不能靠改名或续审充数。

主线程可以从固定发布 commit 获取 `prompts/<id>.md` 与 `readsets/<id>.json` 直接创建云端会话。新环境先核两个真实 checkout，按固定对象读取；不得假设 Mac 路径存在或用替换已有 checkout 隐藏差异。独立输出写各自 `tasks/<id>/`，普通独立报告分支提交，不改正式规格；root 接收回传贡献与完整 I/O。各报告需保留真实平台 ID/开始更新结束 UTC；实际 ID 未回显记 UNVERIFIED。

本机已核 `codex --help`、`exec --help` 及 app-server schema，支持请求模型与 effort/service_tier；一次受控 `codex exec` 实际在初始化进程内 app-server client 时报只读文件系统错误，exit1，新增 CLI 审查上下文0。日志在 `tasks/reference_metadata/launcher.stderr`；不得把该任务标已启动。故本检查点请求主线程用其实际可用会话能力代建17项，不提供未经跑通的 CLI 方法。后继更多合法子片可继续增加，不设人为并发上限，服从实际服务容量和独立写集。

当前材料访问障碍：Library 云端 ZIP `libfile_4b51216024e48191b2cf3166a331583d`（16531493 bytes/SHA256 `6a2b23bd78ba13effe19dd00fc26c268edb9ac53a4927eb1ea13412db6e2511e`）仅返回 signed transfer，官方 helper 因 DNS 不可达未取得字节。已请求同一 ZIP 的固定 Git commit/path 替代传递；包内新的 cloud prompt、readiness、final-input-binding/recovery-map 尚未在本环境全文读取，保持具名未读，不影响独立 B8/R 静态审读。原完整合同已读，主线程明确云端版第4节至结尾同字节。

可用进度入口：平台 canonical task name 与各 `tasks/<id>/progress.json`；root 公共 `../progress.json`。`launcher-status.json` 是进程事实，`progress.json` 是任务报告；两者均不自动代表语义接收。最终报告 core、完整整改 handoff、独立反证和全量远端读回尚待完成，此分工发布不能替代最终验收。
