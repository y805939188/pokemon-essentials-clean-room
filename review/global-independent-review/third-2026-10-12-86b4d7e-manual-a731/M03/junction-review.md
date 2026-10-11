# M03 交界核查

固定参考8c5911e、正式167296d、交付86b4d7e；运行=0。以下为当前M03静态判断，跨模块最终裁决属于独立root。文件位置为审计入口，不是运行证据；normal/failure/boundary逐项区分。

| 交界 | M03 正常/失败/边界结论 | 具体来源与当前条款 | 另一模块消费者与保留限制 |
| --- | --- | --- | --- |
| G2-5 显式种子与有限可复现 | 地牢选固定/待播/新种子后无条件清待播并重播全局随机；内部重绘不重播。奇数构造失败发生在清种子之前，空节点/密度失败之后未到原图回写。未驻留查询也可触发生成。 | RandomDungeons:347–450,1063–1116；MapFactory:54–92,203–206；WP14§3.5/4.1；GR3-M03-002 | M02随机、M09回放、M11彩票/挖矿；只对本地来源/消费顺序支持，不承诺跨实现同seed地图。查询副作用是新增交界，不用旧PASS覆盖。 |
| G2-8 世界天气显示 | 进入天气消费者先旧图非0且异图，再元数据概率得新类，类型相同跳过；变化局部duration0。合法连接之后独立写20，显式重建无该后写；同类显式保持旧7，在途先拒，同类强度改变不再交付显示。 | Overworld:241–254；MapFactory:95–112；Spriteset_Global:33–62；Weather:66–96,425–479；WP11§4/WP16§5.1/5.1.1 | M11天气意图/概率与场地；20不是20秒，默认9种参数静态读，实际粒子/闪光/音频未证。 |
| G7-1 交互合同/消费者 | 102及101合入同缩进选项合并；确认与BACK先查可见→原映射，隐藏A时BACK raw1→原2/C；禁止取消/指定取消/403分开。新增过场注释读取空数组也成立，不能与nil归并。 | Interpreter_Commands:162–337；Messages:26–50；Game_System:279–287；WP13矩阵§3.2及IM36–41；GR3-M03-003 | M10消息/输入、M05物品、M11特殊模式；M03未重审全部消息主规格，下游完整用户交互按各owner结论。 |
| G7-4 失败阶段 | 传送有音频时缺图先于清地图；无音频更后失败。整个路线脚本求值失败先于任一行前缀检查/索引推进；直接位图/条带/普通包装不同错误出口。新事件恢复条件异常保留先前条目提交。 | Scene_Map:56–102；Game_Character:428–560；Cache:38–65；AnimatedBitmap:5–17,46–73,141–155；WP11§8/WP13路线§1/WP15§5.1；GR3-M03-004 | M01/M02/M11/M12编译/文件/插件/转换各自错误阶段；本模块不推统一原子恢复，不执行宿主异常画面。 |
| G9-2 Demo引用合同 | 连接19条与地牢cave/forest文本是可得配置；默认参数5×5与cave5×4不同。结构/数学机制已审，未提供地图事件，不能证明HOME起点或开关置位链/实际地牢启用。 | PBS/map_connections全文；dungeon_parameters/dungeon_tilesets全文；WP11§3/WP14§3.3及DG01/25 | M12 Demo、M06遭遇、M11场地/电话等；WP77完整语义未在M03独立审，缺材料保留。 |
| G9-4 素材缺失与回退 | 缺Graphics/Audio事实与解析nil/原串、普通动画32空白、直接缓存/条带异常不同。BGM/BGS缺文件仍登记请求，不能推实际静音或发声。 | FileTests:109–141,181–285；AnimatedBitmap全文；Cache:38–65；Game_System:44–84,170–185；WP15§3/5.1/6 | M12资源包、M10消息图像消费者；EXE/DLL/SF2/工具图片未执行/解包，字体/像素未知。 |
| G9-5 资格vs地形/运动 | 当前格通行、面向地形、徽章/成员/载具门分列；上水先状态/计数/基点后跳，失败无回滚；瀑向上+本体/顶才置位，外层true不保证激活；冰清理不清through。 | FieldMoves:705–759,891–926；Game_Player:163–204,264–276,601–646；Overworld:158–170,540–551；WP12§3/5 | M04玩家、M05物品、M11场地；完整CanUse/确认/FLY/FLASH/鱼竿三入口未在M03全重审，原限定FINAL语义复用保持PARTIAL。 |
| CHAIN-8 世界显示/时序/目标几何 | 四零时长只写当前不取消旧任务；计时器高于闪烁与图片；地点FLY门先于消息；天气意图→连接后写→显示守卫分层；动画只当前帧定时；普通世界与战前选曲/播放/清预置时点不同。 | Game_Screen:38–120；Game_Picture全文；Sprite_Timer:19–49；Overlays:28–49；SpriteAnimation:135–152,216–234；BattleIntro全文；WP16两正文/IM27–35/XC/B04-W | M05/M07/M10/M11；NearAlly战斗目标几何属M07，M03不覆盖或消除其异议。像素/宿主动画未证。 |
| 新：通知失败与步进前缀（GR3-M02-001） | 普通移动开始已写逻辑坐标/距离后触发离格；普通步完成的全局步数先写，再逐订阅，失败中止后项并保留先前步数。角色on_step_taken异常还可阻止其后灌木/完成标记写入；不补回滚。 | Game_Character:386–402,977–988；Game_Player:539–550；Overworld:172–187；WP12§4.1引用WP06；消费者保持M02的失败关系 | M02主通知/计步；M06遭遇、M11繁殖/树果/场地；回调正常返回是后继运行前提，额外任意回调输入不证明实际Demo注入。 |
| 新：镜头/商店/纸牌 | source镜头支持速度等级/钳边/等待与事件立即继续；绘制量化不能代替输入生成，需GR3-M03-001补合同。 | Game_Map:323–393,439–460,497–565；Game_Player:center/update_screen_position；PokeMart:244,349,362；BattlePointShop:159,217；TripleTriad:1065,1137,1155,1243 | M10商店/M11纸牌/M12镜头编辑；调用点只局部定位，具体UI全部链未在M03审。 |
| 新：事件变更记录与保存恢复 | Game.load→load_map两分支进入通知→清局部记录→图更新→恢复辅助。正常无新增写入时辅助空操作；已有实例可仍保状态，重建另判。同ID实际setup旧ID非0会leave，非重建标记变更不leave。条件未清记录的异图同IDthrough真可写B事件；false保持；异图缺ID真时失败，同图缺ID先跳过。 | StartGame:63–104；MapFactory:17–27,142–153；Overworld:224–237；Overworld_Metadata:144–182；WP11§5.2/6、WP09§4.1；GR3-M03-004 | M02保存主消费者；M01仅metadata身份/schema，M03负责运行语义。条件错误不能写成默认读档必达；缺真实存档/事件。 |
| 新：过程图片/事件呈现与缩略图工具 | PictureEx/事件呈现可得排程、回调、裁剪、输入先BACK后USE；Intro/Button、战斗/进化/交换消费者可定位。TileDrawingHelper可生成缩略图与通行图；不能由“未穷尽”推能力不存在。 | PictureEx全文；EventScene全文；TileDrawingHelper:75–239；C41/C42 | M10各场景、M12作者编辑器；源机制已读，全部具体消费/参数与未来义务保持PARTIAL，无独立新系统实现。 |

历史交界身份导航：`assigned-junctions.tsv` 的精确FINAL1指针已消费，完整FINAL语义对象按 `regression-review.json` 逐ID绑定；旧签名仅有原有效范围，不能支持四项新finding。主角色需整合上述新增消费者/失败边界。所有material/host/sample/default-enabled/full-content状态分开，未运行。

## 精确历史交界定位

- G2-5: commit c2bc1a341ba6acdf7c8c111dc88d39a162a093d6, `review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/9`；当前消费者正常/反向/部分失败语义已消费；M03范围局部复核、其它owners范围保持PARTIAL，旧签名不转移。
- G2-8: commit c2bc1a341ba6acdf7c8c111dc88d39a162a093d6, `review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/12`；当前消费者正常/反向/部分失败语义已消费；M03范围局部复核、其它owners范围保持PARTIAL，旧签名不转移。
- G7-1: commit c2bc1a341ba6acdf7c8c111dc88d39a162a093d6, `review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/39`；当前消费者正常/反向/部分失败语义已消费；M03范围局部复核、其它owners范围保持PARTIAL，旧签名不转移。
- G7-4: commit c2bc1a341ba6acdf7c8c111dc88d39a162a093d6, `review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/42`；当前消费者正常/反向/部分失败语义已消费；M03范围局部复核、其它owners范围保持PARTIAL，旧签名不转移。
- G9-2: commit c2bc1a341ba6acdf7c8c111dc88d39a162a093d6, `review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/49`；当前消费者正常/反向/部分失败语义已消费；M03范围局部复核、其它owners范围保持PARTIAL，旧签名不转移。
- G9-4: commit c2bc1a341ba6acdf7c8c111dc88d39a162a093d6, `review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/51`；当前消费者正常/反向/部分失败语义已消费；M03范围局部复核、其它owners范围保持PARTIAL，旧签名不转移。
- G9-5: commit c2bc1a341ba6acdf7c8c111dc88d39a162a093d6, `review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/52`；当前消费者正常/反向/部分失败语义已消费；M03范围局部复核、其它owners范围保持PARTIAL，旧签名不转移。
- CHAIN-8: commit c2bc1a341ba6acdf7c8c111dc88d39a162a093d6, `review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_chain_results/7`；当前消费者正常/反向/部分失败语义已消费；M03范围局部复核、其它owners范围保持PARTIAL，旧签名不转移。
