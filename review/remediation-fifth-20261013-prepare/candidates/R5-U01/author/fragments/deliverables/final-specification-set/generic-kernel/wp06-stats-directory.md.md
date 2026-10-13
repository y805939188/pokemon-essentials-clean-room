- `play_time_per_session`：先惰性取得当前T再求T/S；正整数T/S保整数商，浮点T为连续商，S正常为正整数。
- `time_since_last_save`：先惰性取得T再求T−L，负结果保留。两查询可能修改T与临时锚点，但不新增声明字段，74项计数保持；独立向量与零会话限制见[主正文§3.1.1](wp06-time-random-steps-stats.md#311-派生游戏时间查询)。

