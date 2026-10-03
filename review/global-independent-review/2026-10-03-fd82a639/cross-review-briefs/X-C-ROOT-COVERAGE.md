# 独立第二审查说明

项目固定e1e01bb18d824931e54f182dd61af5a9f908ba85，参考固定8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。只读输入取自自己的固定worktree；参考取共享REFERENCE_ROOT。先读下面固定输入与场景，自行推导并保存 independent-judgment.md/json（有时间和精确来源范围），**保存前不得读原发现报告/其他当前结论**。根审查者会在保存后给对应原finding做确认/修正/争议判断。不要运行参考/编译器/生成器/反序列化/模拟器，只做文本核验和固定算术。不要因场景被列入而假定一定有缺陷。保留当前正常、裸入口、自定义数据和未知事件/运行的区别。报告写你自己的agent白名单目录，不改正式材料，不改原主审报告。

## X-C-ROOT-COVERAGE：世界显示层的反向范围检验

建议C在WP11/15/16/17主审首判保存后进行，尚未派发。固定原规格、最终正文、WP79旧source-judgments（仅作为待核声明）及WR/BT/事件矩阵测试。

独立从以下具名源码入口枚举可观察行为，并检查实际正文/测试承接或有理由的排除：Game_Picture全文件、Sprite_Picture全文件、Sprite_Timer全文件、Overworld_Overlays全文件、Overworld:278–314调用链；必要时读图形资源/场景/时间的消费者。

给定静态场景：地图是否改变、同名目的地、announce_location开关、NO_SIGNPOSTS地图对；飞行待完成、消息已打开/中途开消息；事件名light/outdoorlight（含可选资源名）；日夜亮度64/144；暗图刷新与FLASH状态；图片移动/旋转输入时长/速度1及经过1秒；计时器运行/停止/负剩余时间。只推导可静态确认的状态/输入合同，媒体实际渲染保持未验证。

保存自己的承接/缺口判断后，root会给总审首判供对照；不得提前读取root/independent-first-judgments.md。
