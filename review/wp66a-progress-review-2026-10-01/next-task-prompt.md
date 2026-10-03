# 继续覆盖优先提取：从 WP63 开始

在 `/Users/dingshinn/Desktop/pokemon-framework-reference` 继续工作。已完成WP66-A初稿；用户的现行策略是先完成剩余内容包，再WP78／WP79整体review，之后统一修订，最后WP80。

先读取根AGENTS、planning/extraction-plan.md §2.2和WP63计划行、原coverage-first-handoff-2026-10-01/prompt.md，以及本目录report.md、findings.json、inputs.json、final-checks.json。WP66-A本次为CONTINUE_WITH_DEFERRED_FINDINGS，保留Drafted；9条P2和3条P3进入统一修订，不把它们改记为通过或关闭。本次不先返修WP66-A、旧GR、N01或整合B批。

开始WP63：Pokégear、地图／旅行入口、音乐、电话／联系人／再战生命周期（F15-02、F15-03），依赖WP24、WP11、WP59、WP17。按原计划逐包查源、写独立行为规格、场景、自检、实际身份和矩阵增量；参考只读，不执行参考实现，不设计／实现框架。

特别带入WP66A-R05：从队伍FLY地图取消返回时，不写新的飞行目的地，但队伍重建选中位归0且本次Box Link许可丢失。核对 `Data/Scripts/016_UI/005_UI_Party.rb:479–526,1204–1213,1288–1302`，再追地图入口与调用者。按来源写新稿交界，注明WP66-A旧稿待统一修订；不用先改旧稿来解除依赖。WP24相关语言交界按GR-009具名证据处理，界面语言与训练家／拥有者语言不得混同。

沿用第一组 `review/wp66a-wp63-wp64-delivery-2026-10-01/`：WP63使用自己的固定身份、自检与来源文件；组摘要追加WP63实际范围。保留WP66-A被审原件／快照，不覆盖其self-checks冒充新结论。新规格保持Drafted，材料不足的必需部分具名Partial／Blocked；不提前标Reviewed。新增产物与矩阵增量按现有manifest／主TSV规范登记，最后另存登记完成后的复核，避免自引用。

WP63正常提取与自检完成后，可依原覆盖优先安排继续WP64，不把逐包外审或“要我继续吗”当默认关卡。写WP64时先读WP66A-R01、C02（邮件取消仍有已提交变化；快照顺序为后第二名、后第一名、本人），避免将已知错误带入新稿。真实缺失资料如实登记，继续其它可独立提取内容。

保持原阶段边界：旧问题统一待办；WP78～WP80不提前执行；不创建任务／Agent、不发跨会话消息、不提交／推送。阶段结束按实际完成与未决汇报，不虚报通过或运行验证。
