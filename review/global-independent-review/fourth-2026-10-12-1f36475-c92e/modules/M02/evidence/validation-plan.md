# 隔离验证计划（执行前）
目的：验证原始参考的 POST 请求前编码与事件墙钟计时入口，不修改参考，不实现替代规则。
工具版本：ruby 2.6.10p210 (2022-04-12 revision 67958) [universal.arm64e-darwin25]；python 3.14.0用于执行回执记录。
命令：ruby review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M02/evidence/probe.rb
输入：只读加载固定R的003_HTTP_Utilities.rb、001_Utilities.rb、003_Game_Variables.rb；HTTPLite替身只记录参数并返回200/OK，禁止任何网络。POST输入ASCII安全字符、空格、键空格、HTTPS；计时输入固定时间1000、1100、1101秒，持续100/0/负数，天数入口用1728000100及1天。
区分：原始入口被实际执行，分类 EXECUTED_REFERENCE（isolated Ruby / host doubles）；替代的时钟、地图refresh计数和HTTP不是宿主运行；不声称游戏或网络可用。
预期观测：基础与便利POST是否传播/吞没请求前异常、宿主调用次数；计时存储/严格到期比较/未到期清零/天数结果。
副作用：只在进程内写假变量、假地图及假网络调用数组；输出JSON到M02/evidence，无保存、无删除、无外部连接。加载来源不写入。

追加探针（首次执行后、二次执行前）：首次普通字符串键在Ruby2.6被散列表冻结，请求前出现FrozenError；保留首回执。二次增加符号键，隔离键冻结与空格转义：符号k/安全值应触达假宿主，符号k/空格值观察编码分支。仍无网络或文件写入副作用。
