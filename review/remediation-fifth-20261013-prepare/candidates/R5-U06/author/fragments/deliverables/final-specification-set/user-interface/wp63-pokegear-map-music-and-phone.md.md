<!-- U06-E028; target/location and exact B5 anchor in fragment-manifest.json -->
按钮主循环全部trigger，按BACK>USE>UP>DOWN只处理一个分支，没有列表先移动阶段。Map焦点同轮DOWN+USE确认当前Map；单DOWN才移Phone。

## 3. 区域地图

<!-- U06-E029; target/location and exact B5 anchor in fragment-manifest.json -->
每次移动逻辑坐标/地点信息先写，建立本次插值起点，显示移动名义0.1秒；发起移动当轮仍继续按钮动作。后续轮先更新横/纵显示坐标，任一读回未到终点便跳过本轮全部输入；到点同轮可继续方向和按钮，名义0.1不是真实宿主精确到点保证。

可输入轮先按dir8移动逻辑坐标、刷新地点，然后按BACK>(USE且飞行模式)>(USE且编辑器)>(ACTION且可切飞行模式)处理首个成立按钮分支。mode1 USE即使点不合资格也挡ACTION；mode0非编辑器USE不单独挡合格ACTION。CTRL press只属调试已访问豁免，不能省治疗点/显示门。合法飞行直接mode1、旧(13,11)、上邻(13,10)是可见已访问治疗点[7,47,11]时，dir8=8+USE当轮返回新点；加BACK先退出nil；后续插值更新未到点则二者均不处理。

### 3.4 飞行选择

<!-- U06-E030; target/location and exact B5 anchor in fragment-manifest.json -->
电话先更新活动列表（其repeat方向顺序），移动模式再按新索引实时重排，随后普通模式ACTION>BACK>USE；移动模式(ACTION或USE)>BACK，按钮为trigger。三个全可见联系人[A,B,C]、从索引0移动A且当前/上轮索引均0：DOWN repeat+USE+BACK先变[B,A,C]，USE落定胜BACK；独立DOWN+BACK先移动后还原[A,B,C]及索引0。不把隐藏联系人索引变体外推为已证。

### 4.2 联系人数据（全局持久，随存档）
