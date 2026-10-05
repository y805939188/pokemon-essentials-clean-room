# 本轮验证说明

权威元数据结果为 independent-metadata-checks.json：45项通过、0失败。保留的 initial-metadata-check-attempt.json 是早于修正的自有检查记录，含3项失败；它不证明候选有3项缺陷。

两份封包补丁按 Git `diff --binary` 生成。本轮初次加上 `--full-index` 重构，导致 index 元数据宽度不同、字节比较失败；按封包 README 的实际命令重构后，两份补丁逐字节相等，原始声明的 SHA256／字节数也相等。没有路径过滤、文件遗漏或内容修复。

初次递归身份检查把 commit=null 一律绑定当前候选，误用于 candidate-1 的 additional_unplanned_readers_history 和批准文件的 current_unmodified 历史快照。read-coverage 的 history 名称和 approval 的 file_records_are_exact_historical_proposal_inputs／historical_file_status_note 明示这些是原提案输入。修正为 candidate-1 固定 SHA 验证；所有当前 refreeze 仍绑定精确本轮候选。548次声明身份均匹配，不修改候选或历史字段。

首判 independent-first-pass.json 与首轮 source-reading-log.json 未重写。首判 SHA256 为 ad70c3771dca33cc83f6287135899ff7fbeac4892247bd45023ba012c6f2b8bc；来源日志为 46cb066d04d2908dafd80044ca91adbb0218fd24d63da0a5155d8eab8d9c397a。初次检索中若路径猜测不存在或在主项目 cwd 查找参考路径，均按失败查询处理，不记为语义读取；通过 rg 定位后才读取参考文件。首轮日志的存储308–355仅是包装范围，同身份插入的决定性证据在38–44／170–175／231–249。以前B05的定位勘误保留在原报告目录，不被本轮覆盖。

对照作者后另直接读取参考 001_Battle_Battler.rb:662–676，确认当前记录读写以该侧及个体队伍索引为输入；它是首判后补充验证，记录在 author-comparison.json，不倒填首判日志。使用的自有 Python 仅做 JSON、Git、文本、文件身份记录，不执行作者脚本、参考代码或行为模型。

报告内 independent-formal-diff.patch 是原始 Git 差异证据，保留上下文空行的单个空格前缀和末尾上下文；对补丁文件自身运行 git diff --check 会把这些证据字节视作新文件尾随空白。未为消除此提示修改原始补丁。排除这一原始补丁后，报告 JSON／Markdown 的 staged diff --check 通过；补丁仍与固定起点→候选 Git diff --binary --full-index 逐字节相等。
