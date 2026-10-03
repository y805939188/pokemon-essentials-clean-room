# 仅补修GR-007／GR-009的剩余边界；GR-008保持CLOSED

在 `/Users/dingshinn/Desktop/pokemon-framework-reference` 工作。先读AGENTS、本目录report.md／findings.json／inputs.json／registration-checks.json／final-checks.json及原全局GR-007／009。

本次REQUEST_CHANGES：GR-008已经CLOSED；GR-007淡出目标与GR-009训练家默认宿主映射均已正确，只补以下边界。不开始GR-010～012或新WP。

## GR-007

WP15§6.3分别写清两条触发条件：当前相应通道已有播放登记、目标图对应autoplay开关开启、名称不同（BGM目标名含其夜间变体解析）。BGS满足自身条件时调用的仍是BGM淡出，不要改成BGS淡出，也不要额外要求BGM分支成立。

补齐“仅BGM变化”正例的播放记录与autoplay_bgm=true前提；保留原“仅BGS变化”正确结果；增加对应目标开关关闭的对照。共同固定系统对象存在、非暂停、无defaultBGM覆盖、白天或无夜间变体，观察点仍在autofade返回且后续autoplay之前。不播放真实音频或执行参考方法。

## GR-009

WP18§6.1的language指引不能无条件写“来源为宿主语言映射”。限定：宿主映射是训练家默认构造的语言来源；Owner直接构造采用传入整数，new_from_trainer复制训练家现有字段，new_foreign默认语言2，setter也可采用显式值。保持与UI选择索引分离、不随UI切换自动回改的正确结论。

按这个最小范围修WP18第203行指引及相应历史注记；WP24中若有同样可能被理解成所有Owner都重新读取宿主的概括，只作限定，不重写已正确的宿主映射／四组场景。补宿主ja-JP下外来Owner默认2、显式language=3、训练家字段改为7后复制7的静态对照即可。不得读取或改真实主机语言。

矩阵GR-009主登记F07-03已获本次裁定接受，无需为了本项补修挪到F07-02；不是一GR只能一行的普遍规则。WP08已正确UI规则、经验／繁殖公式不改。WP20当前GR-008已通过字节9d688fd6／37,484保持不变。

## 交付

新建 `review/gr007-gr009-revision-2026-10-01/revision-v2/`：两项逐ID回应、实际来源读段、反例与正例、自检、相对本次input-snapshot的精确diff和程序化完整身份。旧被审材料／reviewer原件与快照留史；当前正文、回应、摘要／自检不得互相矛盾。

按实际修改同步必要矩阵／manifest／主TSV和当前身份引用；不猜哈希，先定稿上游正文再测量引用与登记。最终登记检查独立保存，不自登记进描述的清单。修订完成只标待定点复审，不自行CLOSED／Reviewed，并停止送审。

GR-001～006、GR-008、第一组31项、N01已通过范围保持；GR-010～016、新WP、行政回填与B批整合不扩入本次。reference只读；不运行参考代码／表达式、游戏／事件／编译转换／生成器、真实网络，不操作真实地图／存档／输入，不实现框架；不创建任务／Agent、不发跨会话消息、不提交／推送。
