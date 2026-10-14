# 云端准备发布回执

已普通推送准备core `2cad33e41732ee9e013a7ab03f8140a5b178fc3b`，workspace tree `e54079adb19d502435209f4401b75b01866252fc`，准备目录tree `17b258a8e99c56172a32e0486033949486ef3034`。277个新增载荷共20,066,913 bytes全部以固定commit远端完整字节回读，bytes/SHA256/blob一致；独立Git回读库从缺失该core对象的固定pack-only缓存取得新commit/tree并核全部path/mode/type/blob，没有重传700MB历史。回执和原始分离输出见本目录。

初次GitHub API元数据入口出现proxy tunnel403，原错误与工具保留。随后换可用Git传输核远端对象，再用raw固定commit入口逐字节回读成功。Git工具补读是新验证，不补造初次API失败的UTC/PID。

当前56 OPEN、作者／审者实际启动0、所有语义PASS／接受／CLOSED均0；28个完整启动入口、14批精确合同、115份原证据、79份baseline镜像和独占接收规则已经可恢复。default模型能力障碍见 `../verification/runtime-capability.json`。本发布不声称语义整改已开始、全文审者阅读完成或用户最终目标已达成。

此有限P发布只新增本目录的回执／工具／原始输出。其实际commit/tree由外部最终响应绑定；P中的core载荷必须逐项与已完整回读C载荷一致，新P载荷另作完整回读。没有self-hash循环，也没有自动下一轮review、main合并、force或删除。
