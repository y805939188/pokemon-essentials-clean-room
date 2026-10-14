# R6 实际任务与日志入口

这是本轮审查查询方式，不启动任何update。逐入口ID、实际thread/PID/模型请求及未回显配置见task-register.json。协作工具的三个任务实际canonical名为/root/combat_review、/root/kernel_creature_dx_review、/root/world_ui_review；协作状态从collaboration.list_agents查询。CLI独立任务的真实UUID从stdout.jsonl的thread.started取得，不能把逻辑ID当UUID。

CLI 0.162.0-alpha.17.2 的帮助已实读。用codex agents打开现成会话浏览界面；对UUID使用codex resume UUID查看/继续属于操作，查询优先日志或本app read_thread/wait_threads。Desktop缓存read_thread曾给notLoaded/interrupted，同时实际CLI日志仍在推进；这类缓存不是实际进程退出凭据。

在项目目录可执行的只读查询示例（R6-D；其它ID替换最后路径组件）：

```sh
cat review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/control/task-register.json
cat review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-D/launcher-status.json
cat review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-D/task-status.json
tail -n 40 review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-D/stdout.jsonl
tail -n 40 review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-D/stderr.log
ps -p 44562 -o pid,lstart,etime,state,command
```

PID来自真实启动但退出后可复用，须合用launcher起止和日志，不以ps孤证断言原任务继续运行。launcher COMPLETED只表示CLI进程exit0，不自动表示全量审查完成；仍核task-status、reading ledger、双向矩阵和未审差集。退出原因/未捕获状态如实保留。

本轮真实启动方式是tools/run_cli_review.py按每目录prompt.md调用codex exec --json，精确argv/PID/start/end/exit已保留。内部模型/effort/tier/speed未回显，均UNVERIFIED；请求gpt-6.1-sol/ultra/service_tier=default，没有Fast请求。通过实际codex queue --help核验了--thread/--message，并在cli-coordination-001.json记录三个成功queued message ID；队列成功只证明排队，不证明已消费。

官方文档路由：CLI选项 https://learn.chatgpt.com/docs/developer-commands?surface=cli 与配置 https://learn.chatgpt.com/docs/config-file/config-reference 均已打开；具体可用命令仍以本机实读help为准，未臆造状态flags。没有检查额度、认证或访问token。
