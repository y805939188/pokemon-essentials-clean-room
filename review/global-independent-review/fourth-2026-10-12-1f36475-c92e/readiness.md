# 现场 readiness：PARTIAL_READY

B 正式131文件完整bytes/SHA256/blob与清单及两处工作字节一致；R独立Git仓库432 tracked完整匹配，无tracked修改。观测值与时间见baseline.json；命令实现见evidence/readiness-check.py。没有用历史回执代替现场身份核验。

主仓库main/HEAD/origin-main/交付tag与远端广告main均为B。原62个未跟踪候选逐文件身份、ignored目录、12个原worktree及本轮新增worktree见evidence/workspace-protection-before.json与protected-untracked.json。全部受保护；只新建本轮隔离worktree、报告分支及报告目录，没有覆盖旧候选。

参考实际434个非Git元数据文件：432 tracked+两份.DS_Store。历史467计数包含Git元数据与否未追溯，不把旧数当现场分母。没有完整资源包叠加。源码312、PBS73、翻译18、字体8；knownpoint.bmp/selpoint.bmp在根目录实际存在且属于R；无Graphics/Audio/地图/完整Demo。Scripts.rxdata/messages_core.dat及Windows工具存在，不等于已解析、可启动或运行成功。

Ruby2.6.10、Python3.14、Node可用；PATH未发现wine/wine64/mkxp/mkxp-z。/Applications有RPG Maker MZ相关应用；未证明与R的RGSS兼容。可以继续静态源码/数据/数学/规格审查，必要时隔离纯路径验证；完整Demo、宿主输入渲染音频及缺媒体行为保留未知。当前所有行为执行类别NOT_EXECUTED。

根AGENTS.md适用，新review路径各祖先没有其他AGENTS.md。正式集、reference、历史报告、原工作内容均禁止写入。只写本轮目录和必要隔离临时目录。全局Feature Matrix本轮以新coverage矩阵表达，不改正式矩阵。
