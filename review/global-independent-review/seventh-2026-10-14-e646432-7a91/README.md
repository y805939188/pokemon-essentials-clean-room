# 第七轮独立全局审查

当前主入口：final-report.md、summary.md、canonical-records.json、coverage/summary.final.json、reading-ledger.final.json、progress.final.json。旧progress.json及所有中间WAIT/UNREAD保留原时点，以final后继和具名接收为当前结论。

完整中文可复制合同：handoff/cloud-seventh-update-handoff-prompt.md；结构化manifest、三图与26完整入口同目录。发布core/C1及逐载荷bytes/SHA/blob和完整远端回读结果由publication/final-delivery-binding.json固定，最后C2自身身份在交付消息给出。UPDATE_NOT_STARTED。

大量任务证据采用无损对象传输；在项目根运行（destination必须不存在）：

```sh
python3 -B review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-tools/transport.py restore --package review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core --destination /private/tmp/r7-e646432-restored
```

恢复后原tasks/<入口ID>/report.md、task.json、logs/及精确矩阵均可读；如查看R7-M09：

```sh
cat /private/tmp/r7-e646432-restored/tasks/R7-M09/task.json
tail -n 40 review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/platform-io/tasks__R7-M09__events.jsonl.jsonl
```

原私有reasoning流不发布，公开命令I/O投影完整身份单列；不把传输核验称语义审查。原输入B/R、历史恢复43份、旧报告、正式131和全部既有环境只读保护。

未来仅由用户手动委派。一个可复制的请求/状态示例（本轮不得加--launch）：

```sh
python3 -B review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-tools/manual_launch.py --project . --package review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff --entry R7-U01-A
python3 -B review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-tools/manual_launch.py --project . --package review/global-independent-review/seventh-2026-10-14-e646432-7a91/handoff --entry R7-U01-A --status
```

用户在另行update分支授权启动时才显式加--launch；立即记录实际Popen.pid，完整分流events/stderr和wait退出，状态不由进程0推导语义PASS。云端先解析实际project/package路径并保存映射，现有本机绝对路径不冒充未来云端路径。
