"""Encode the reviewer's read facts. Counts/serialization do not confer review credit.

This file writes this task's evidence only. It is not an implementation or an
execution of the reference. Literal-table recovery follows the complete human
read of both tables and the field-to-consumer crosswalk below.
"""
import ast
import datetime
import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = Path('/workspace/pokemon-essentials-clean-room')
REF = Path('/workspace/pokemon-essentials')
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
B = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
def get(name): return json.loads((HERE / (name + '.json')).read_text())
def put(name, value): (HERE / (name + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
def git(repo, *args): return subprocess.check_output(['git', *args], cwd=repo)
def identity(repo, commit, path):
    data = git(repo, 'show', commit + ':' + path)
    return dict(repo=str(repo), commit=commit, workspace_tree=git(repo,'rev-parse',commit+'^{tree}').decode().strip(),
                path=path, git_blob=git(repo,'rev-parse',commit+':'+path).decode().strip(),
                bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), lines=len(data.splitlines()))

# A row is an independently checkable semantic proposition, not a source line,
# an execution, a PASS, or a claim that every implementation literal is required.
# A typed tuple (position, tone, mapping) is one proposition; its scalar leaves
# are separately counted for the two finite variance tables.
MANUAL = {
1: '''世代>=5启用特性提示条。
普通消息全显后的常量驻留为1秒。
暂停消息的常量驻留为3秒。
排列条球位数读取MAX_PARTY_SIZE，默认配置为6。
成员坐标按双方和1/2/3席位采用不同偏移。
训练家位置按本侧训练家总数和索引偏移。
动画焦点常量与实际成员坐标是不同输入。''',
2: '''外部update先图形后输入再场景帧更新。
场景帧先推进已入队动画。
完成的入队动画在该轮被销毁并移出。
可中止且尚未中止时BACK触发一次中止。
场景刷新分别刷新框、立绘和影子。
刷新立绘保留显式传入的显示个体。''',
3: '''五个窗口模式分别控制消息框及三个菜单的可见性。
brief标记只由下一次相应消息等待消费。
brief等待从当前时刻另等1秒。
brief等待结束清标记并清文本。''',
4: '''普通消息在文字全显后才开始1秒计时。
brief普通消息全显即返回并保留文字。
消息块在首次全显时至多调用一次。
普通消息忙时USE/BACK调用快进。
普通消息不忙时USE/BACK可立即关闭。
暂停消息非战末全显后3秒自动关闭。
战末暂停消息不自动关闭。
可中止场景自动快进文字不消除后续计时。
每轮消息等待继续驱动场景。''',
5: '''确认列表初始选择Yes。
确认BACK返回No。
普通列表初始索引为0。
普通列表默认取消返回值-1禁止取消。
列表文字忙时允许的按键仅恢复文字显示。
列表文字不忙时USE返回当前索引。
列表文字不忙且取消值非负时BACK返回该值。''',
6: '''普通精灵创建的局部资源失败救援不等同平面加载路径。
换位交换成员精灵绑定。
换位交换影子绑定。
换位交换命令及招式游标记忆。
换位更新数据框的成员绑定和位置。''',
7: '''攻击阶段清除全部选择高亮。
正常结束淡出并销毁场景图形。
选择数组对非nil席位设置选择态。
换图使用侧别决定正背面。
影子可见性还受物种影子规则约束。
胜负音频入口设置战末标记。''',
8: '''初始化分别保存可中止、已中止及战末状态。
初始化建立动画队列。
战斗视口位于高层。
命令和招式记忆按席位零填。
初始精灵创建完毕后才开始开场演出。''',
9: '''初始化创建消息框及三个菜单。
双方分别创建排列条和特性条。
玩家、伙伴与对手采用各自训练家资源入口。
存在成员的席位建立数据框、立绘及影子。
野生对手初始立绘采用暗色。''',
10: '''背景图与消息图独立选择时段后缀。
组合平台是否可用由base0资源检查决定。
组合可用时双方共同采用该前缀。
组合不可用时才选择独立平台资源。
独立平台加载不保证额外第二次回退。''',
11: '''玩家训练家背图与伙伴/对手资源解析不同。
宽背图按五帧裁区。
训练家立绘原点为底中。
成员与影子精灵持有场景动画队列。''',
12: '''Call替换由SHADOW类型存在且训练家战共同开门。
命令按钮采用四格方向导航。
命令选择从本席位记忆恢复。
USE确认当前命令。
仅模式1允许BACK返回取消。
调试F9另行进入调试入口。''',
13: '''招式选择恢复本席位招式记忆。
Shift与Mega各有独立附加选择码。
回调返回接受才退出普通招式确认。
BACK退出与附加按钮返回分开。
退出写回当前招式游标。''',
14: '''队伍显示按战斗方给定显示次序构造。
队伍列表取消取决于canCancel。
子菜单取消返回队伍列表。
Switch选项要求可战斗且允许换入。
显示下标反查真实队伍下标后让渡。
接收方拒绝时继续当前选择。''',
15: '''正常进入背包保存并替换野外游标。
物品列表按battle_use过滤。
类别1/3先尝试自动选择目标。
自动目标拒绝后进入手动队伍选择。
类别2还需选择目标招式。
蛋不进入普通目标使用路径。
类别4单候选自动选择，否则打开目标页。
类别5不提供成员目标。
各层取消只返回相应上层。
正常收尾恢复野外游标并保存战斗游标。''',
16: '''目标文字nil代表不能显示选择按钮。
目标文字空串与nil不同。
RandomNearFoe显示用户不等同执行目标数为1。
NearAlly初选直接向Battle.nearBattlers?传入成员对象；该接收方不做index归一化。
初选和执行阶段目标校验不等同。''',
17: '''同侧水平导航以玩家视角正负2移动。
跨侧导航按预定顺序寻找非nil目标。
确认当前位置不重新验证目标文字。
结束目标选择清全部高亮。''',
18: '''遗忘入口淡出后进入摘要。
命名入口传入成员预览和长度上限。
新捕获图鉴入口淡出后打开对应条目。''',
19: '''基础开场演出阻塞等待。
训练家战排列可入队异步推进。
野生开场等待数据框、恢复色及叫声演出。
异色公共动画受动画开关约束。
普通排列和训练家滑入各有阻塞入口。''',
20: '''派出先等待已入队动画。
派出清除brief标记。
训练家淡出与多只球动画共同推进。
每只数据框仅等待自己的球动画。
离开派出等待还要求全部框及队列完成。
收回先等待球动画再等待数据框退场。''',
21: '''特性条显示受USE_ABILITY_SPLASH门约束。
已有特性条先隐去再显示新条。
出现及消失入口各自阻塞。
替换特性重新走显示入口。''',
22: '''可选HP公共动画受调用方参数和动画开关共同约束。
HP补间独立于该公共动画。
多目标伤害等待全部闪烁与HP补间。
EXP入口对无成员早返。
EXP入口对起止相同早返。''',
23: '''升级增量窗先于新数值窗。
倒下精灵与数据框退场共同推进。
投球等待自身演出并等待队列空。
野生捕获成功ME等待3.5秒后停止。
隐藏成功球与数据框退场并行。
挡球入口阻塞。''',
24: '''影子包装保存全部已有影子的可见标记。
影子包装先隐藏它们再调用核心。
只有核心正常返回才恢复影子。
该包装没有ensure恢复保证。''',
25: '''精确招式映射优先查对方OppMove。
精确命中编号叠加hitNum。
默认身份表按18类型各6格独立读取。
原始类别和多目标偏移是独立判断。
默认身份映射不叠加原hitNum。
缺失候选继续向后查。
普通查找异常被救援为nil。''',
26: '''招式无编号或无数据库直接返回。
有效招式播放进入全部影子包装。
Common按首个精确名称匹配。
Common核心入口本身不包全部影子。
焦点高度来自当前用户/目标。
核心正常返回后恢复用户/目标位置及origin。''',
27: '''球公共动画按名称选择首个匹配。
该入口移除用户/目标精灵参与。
该入口显式覆盖目标焦点原点。
该入口启动后入队并立即返回。''',
28: '''菜单可见性受菜单自身及每个子精灵开关共同约束。
索引变化触发刷新。
模式变化触发刷新。
dispose有重复销毁防护。''',
29: '''命令菜单五模式分别映射图块。
图形模式有四按钮及提示文本。
文本替代分支由窗口图配置决定。
当前选择决定图块和层次。''',
30: '''招式菜单可构造图形或文本分支。
图形分支持有类型图标和PP精灵。
Mega与Shift是独立按钮。
成员重绑触发刷新。
Shift状态变化触发刷新。''',
31: '''招式显示类型决定按钮图块。
招式名称颜色来自图块采样。
空招式槽隐藏。
图形PP仅在totalPP正时写数值。
PP颜色按ceil四分位边界。
文本模式零总PP使用占位。''',
32: '''Mega按钮按可见及按下状态选择图块。
Shift存在时横移Mega按钮。
无成员的额外按钮刷新直接返回。''',
33: '''目标菜单没有文本替代分支。
双方1/2/3席采用非对称布局。
任一侧超过2席采用窄按钮。
空串仍是有效按钮但没有名字。
nil目标采用中性不可选图块。
单选与多选使用不同层次。''',
34: '''仅玩家单席开启数字HP。
仅玩家单席开启EXP条。
2/3席采用各自框坐标。
框的位置、层、可见与颜色传播到子精灵。
重新初始化中的开启分支不主动重置已真的显示门。''',
35: '''动画时显示HP取补间值。
数字HP显示单独to_i。
EXP分母为0时使用防护值。
无HP变化不启动补间。
无EXP显示、零差及零范围各可直接返回。''',
36: '''长名字向左偏移。
等级及性别显示各自处理。
剧毒使用独立状态图标。
异色图标独立于状态。
Mega与两原始物种有各自图标条件。
owned图标仅对方显示。''',
37: '''正HP条宽至少1再按偶数像素量化。
HP选色比较当下浮点显示HP与整数四分位阈值。
EXP条宽按2像素量化。''',
38: '''HP补间固定1秒。
EXP补间按差值比例乘1.75秒。
满EXP槽闪0.2秒并请求满槽音。
框选择态1/2采用0.6秒摆动。''',
39: '''双方特性条分别位于对应半幅。
条显示成员名及特性名。
背景同步可见、色、层和坐标。''',
40: '''成员精灵使用底中原点。
物种metrics影响实际位置。
真实坐标与选择摆动偏移分离。
出现回调负责请求叫声。
选择态1采用0.6秒摆动。
选择态2采用0.3秒闪烁且保留原可见门。''',
41: '''影子使用中央原点及层3。
影子位置消费物种影子metrics。
重绑成员重新选择影子资源。
影子每轮推进动画位图。''',
42: '''一轮开始仍running的轨道使聚合本轮未完成。
最后轨道本轮结束还需要下一次聚合更新才done。
聚合销毁仅处理自己建立的临时精灵。''',
43: '''球色是15种显式RGB及默认RGB，Color的alpha由具体调用者另设。
球资源身份为ball加球ID，中心锚点。
球位图宽>=高时源区宽为高/2且高不变，否则完整资源。
静态训练家宽<2高，球第7单位可见，手位用训练家X减普通投掷累计位移和Y减半高。
动态训练家默认手位六参数为(-44,-32,-10,-36,118,-4)。
Leaf手位六参数为(-30,-30,-18,-36,118,-6)。
Brendan手位六参数为(-46,-40,-4,-30,118,-2)。
May手位六参数为(-44,-38,-8,-30,122,0)。
动态手中球从0可见，普通投掷0..5平移-5*floor(W/32)、5..7平移-2*floor(W/32)。
Safari手中球在0/5/7分别瞬移X -12/+34/-14。
返回出手坐标为手位六参数之和，再减普通累计时长*floor(W/32)位移或加Safari的8。
训练家投掷帧在0/5/7/9/18依次为1/2/3/4/0。
训练家X在0/5/7/9依次偏移-12/+34/-14/+28。
训练家10起3单位相对移动(-6,+6)，18偏移X -4，19偏移(-26,-6)。
手中球层为训练家层减1。''',
44: '''轨迹在delay置可见，按i=1..duration登记每段1单位运动。
横向按i/duration线性插值。
纵向二次曲线通过起点、t=.5的midY和终点。
midX参数不消费。
球图帧数为宽>=高时floor(2宽/高)，否则1。
滚动图帧按floor(帧数*i/duration)变化，取模后源X为索引*高/2。
轨迹末端图帧恢复0。
滚动旋转共3周，末端角度恢复0。
开合资源分别为ball_ID_open及ball_ID，沿用半高裁区门。
默认开球在delay起1单位压到120x80，在delay+5起1单位回100。
开球在delay+6切换开图，默认同时请求Battle recall音。
squish和playSE各自可关闭。
出现从delay可见且opacity255，5单位移动至最终位置并放大100。
出现移动完成回调请求叫声。
出现从delay+5起10单位把混色alpha恢复0。
普通吸入先10单位把混色alpha变255，再5单位移球心及缩0并隐藏。''',
45: '''释放表16行均按独立球种身份读取，不用捕获表替代。
每行14个逻辑字段的字段名、数值及消费者见release-variance-fields.json。
不存在的球种回退POKEBALL。
CHERISH两个ray tone字段被后续专用色循环绕过，仍登记其值。''',
46: '''释放建立15对粒子和10射线。
释放glare渐隐8、粒子寿命15/渐隐8、射线寿命13/渐隐5。
释放射线基础半径24。
glare下层/上层的z为105/106，中心锚点，初始zoom0、隐藏。
glare在delay可见，tone从delay+11起4单位至表终值。
MASTER下glare旋转-135/19单位并放大250/8单位。
DUSK下glare旋转-270/19单位，不登记放大，保留初始zoom0。
其它下glare的whirl为200、dazzle/ring3/web为100、其余250，均8单位。
MASTER上glare旋转-135/19单位并放大200/8单位。
其它上glare的dazzle/ring3/web为125、其余200，均8单位。
下/上glare在delay+11分别8/6单位淡0，delay+19隐藏。
射线随机角为整数0..359，初始Y缩放为50..99，X缩放200。
射线起点沿angle+90度半径24，底中锚点z100，初始opacity0。
第i射线从delay+floor(i/2)显示，13单位放长至初始Y缩放6倍。
射线2单位淡入255，在起点+8起5单位淡0，+13隐藏。
普通射线末5单位tone走表终值。
CHERISH按每单位循环5个RGB (-104,-144,-8)/(-64,-144,-24)/(-8,-144,-64)/(-8,-48,-152)/(-8,-32,-160)。
每对上下粒子共用随机整数半径256..383和角0..359。
下/上粒子z110/111，初始zoom80/60，资源ring2时再减半。
第i对粒子从delay+floor(i/4)显示，15单位径向移出并缩至10。
粒子从本起点+7起4单位变至终tone、8单位淡0，+15隐藏。''',
47: '''捕获表16行均独立于释放表读取。
每行17个逻辑字段的字段名、数值及消费者见capture-variance-fields.json。
不存在的球种回退POKEBALL。
NEST下粒子资源和tone仍被读取，但该粒子在显示同刻再隐藏。''',
48: '''捕获burst持续基数10，尾环5，粒子组9，初始角270度。
MASTER基础半径192，其余144。
三glare从下到上z100/101/102，初始zoom0、隐藏，表tone分别取下/中/上。
中glare初始opacity160，上glare除DUSK外160，DUSK保留默认。
下glare10单位放大至MASTER1200/DUSK350/其它600，在+5起5单位淡0。
三glare从delay起10单位变至各自终tone。
DUSK中/上glare10单位放大350/500，在+5起5单位淡0。
非DUSK中glare至MASTER400/其它250，上至MASTER800/其它500，+5起整数10/3=3单位淡0。
三glare在delay+10隐藏。
每组外出粒子资源particle、z105、zoom150、opacity160。
返回下/上粒子z110/111，初始zoom为NEST50/其它0。
PREMIER返回粒子各有随机初角0..359，DIVE上粒子opacity128。
所有粒子delay显示后NEST下粒子同刻隐藏。
第i组基角270+40i，10个步骤角逐步加4度。
返回半径先5步线性增至基半径再5步回0。
外粒子沿原角10单位移至2倍基半径并缩0淡0。
返回粒子前5单位放大：MASTER下225、DIVE下125、particle在PREMIER为50否则80、ring3为50、dazzle/ring4/diamond为60、其余100，按该优先次序。
返回粒子+6起3单位缩小：particle/dazzle/ring3/ring4/diamond到10，其余25。
PREMIER返回粒子10单位旋至绝对-180度。
返回粒子+3起4单位变终tone，+7起3单位opacity至128，+10隐藏。
NET额外web中心锚点z123、zoom120、opacity0、tone(-32,-32,-128)。
NET web在+5显示，2单位淡160；+5/+9各2单位放150再2单位回120，+13起2单位到150。
NET web在+10起5单位淡0，+15隐藏。
尾环资源ring1、z110、zoom0，+10显示，+8起7单位到125。
尾环+10起5单位变终tone并淡0，+15隐藏。
球零位移标记设在+15以扩展聚合总时长。''',
49: '''成功在delay请求Battle catch click。
球4单位变为RGB(-128,-128,-128)，星星起点取球累计时长。
三星资源ballBurst_star，中心锚点z110，初始zoom50/50/33、angle0/345/15、opacity0。
三星运动持续12，横向分别为-1/0/+1乘floor(72*n/12)。
三星纵向曲线的起/中/终高度分别(0,74,52)/(0,62,28)/(0,74,48)，从ballY扣除。
左右星旋转增量144/45，中星不登记旋转。
星4单位淡255，+3起3单位tone(0,0,-96)，+6起3单位恢复tone0，+8起4单位淡0。
星结束没有单独隐藏请求，由临时精灵销毁结束寿命。''',
50: '''收回burst基数为10+5=15单位，5粒子，基础角55度，半径64。
粒子中心锚点z110、zoom150、opacity0，delay显示并2单位淡255。
第i粒子第j步角为55+72i+135j/15。
半径前j<3由48增向64，中j=3..6为64，j>=7按64*(1-(j-7)/7)回0。
粒子位置为球心加(Rcos,-Rsin)，首步即时，其余每步1单位。
粒子15单位缩0，+5起5单位变(0,0,-192)，+10起5单位变(0,-128,-248)并淡0，+15隐藏。
第一环ring1、z110、zoom0，+13显示，4单位到100，+17隐藏。
第二环ring2、z110，+17显示，4单位到200并淡0，临时销毁而无单独隐藏。
收回burst自身不消费poke_ball参数，球色由外部另取。''',
51: '''Intro位移时长20单位。
第二背景存在才登记背景水平半幅位移。
背景起终偏移分别floor(W/2)及floor(-W/2)，奇数宽不擅自对称化。
玩家平台/训练家从+W进入，对方平台/训练家和野生奇数席从-W进入。
影子按席位奇偶从对应正负W进入。
缺精灵项跳过；平台1和影子中心锚点，其它所列立绘底中。
黑幕z999，0起8单位淡0。
命令栏黑条z998，15起5单位淡0。
Intro2仅对已有奇数席恢复tone，0起4单位至0。
Intro2叫声回调按第i成员10i错峰。''',
52: '''排列条显示宽248。
玩家条坐标(W-248,H-142)，球起点为条+(44,-30)。
对方条基准(0,114)再扣位图宽，球起点(174,84)，条锚点X248。
球间距32*(1-2side)。
条和球初始化opacity255并隐藏。
玩家只显示第二训练家起点之前的己方成员，越界槽用-1。
对方球位按NUM_BALLS/训练家数整数均分。
对方每槽拒绝跨入下一训练家的队伍起点。
条0可见、从本侧半屏偏移8单位回位。
开场球从条总时长+2i开始，普通球均从0开始。
资源优先空位、不可战斗、异常状态、健康状态。
每球显示并从本侧半屏偏移8单位回位。''',
53: '''数据框进退采用8单位侧向运动。
无对应数据框直接不建立轨道。
特性条出现请求出现音。
特性条消失轨道完成后隐藏。''',
54: '''TrainerAppear在新索引>0且旧训练家可见时先把旧者8单位向右W/4并隐藏。
新训练家存在时在标准对方位置右偏64+W/4显示，8单位左移W/4。
PlayerFade按连续训练家编号遍历，遇缺失停止，跳过隐藏或X<0者。
玩家训练家16单位左移W/2，16时隐藏。
宽玩家训练家图在0/5/7/9切帧1/2/3/4。
fullAnim仅控制排列运动，不阻止训练家运动或切帧。
可见排列条从3开始，fullAnim时16单位左移W/4，同时12单位淡0。
排列条15时隐藏后同刻opacity恢复255。
可见玩家球fullAnim时从3+2j起16单位左移W，淡出仍统一从3开始12单位。
球15时隐藏后opacity恢复255，已登记位移可继续于隐藏态。
TrainerFade跳过隐藏或X>W者，向右运动，对方训练家不切玩家投掷帧。
对方排列条/球采用对应向右位移，其淡出与隐藏复位同玩家侧。''',
55: '''派出构造时隐藏成员并保存及隐藏影子的原可见值。
球身份从实际显示立绘持有的个体读取，支持上游Illusion。
派出颜色取球RGB并把alpha设255。
球终点采用canonical成员位置，成员最终位置采用含metrics的实际位置。
玩家默认球起(-6,202)，中Y为canonicalY-144，终为(canonicalX,canonicalY-18)。
玩家开场且训练家存在且X>0时采用手中球轨道及训练家层减1。
玩家抛物线12单位，从手中球累计时长后开始。
玩家球绝对第9单位置于成员层减1，不加手中球delay。
玩家释放基点为轨迹累计时长+4，再加10*order；玩家开场不额外加10。
玩家开球压缩从基点-2开始，burst从基点开始，球基点+2起2单位淡0。
成员从canonical位置/zoom0开始，5单位到实际位置/zoom100并叫声，再10单位恢复色。
仅原影子可见时基点显示影子，+5起10单位淡255。
对手球无抛物线，直接(canonicalX,canonicalY-4)，层为成员层减1。
对手释放基点为球累计时长+6，开场加10，个体次序加10*order。
对手开球、burst、球淡出及成员/影子恢复参数同上述基点关系。''',
56: '''收回颜色取球RGB但alpha初值0，终点为canonical成员位置。
收回球在终点且层为成员层加1，0开始默认开球，得到开球时长6。
收回burst与普通吸入从6开始。
收回球绝对10起2单位淡0，不在6后再加10。
原可见影子0起10单位淡0，绝对6隐藏。
伤害效果0/1/2分别请求普通/弱/强伤害音，其他效果不请求该音。
伤害保存成员与影子的各自原可见性。
伤害在0/4/8/12隐藏，分别+2只恢复原可见者。
伤害16时恢复各自原可见性，不改倒下状态。''',
57: '''倒下裁切底线为canonicalY+8，立绘顶为实际Y-高度。
倒下运动时长为floor((裁线-顶)/8)，最少10单位。
优先寻找专用_faint叫声资源。
专用叫声存在时请求默认音高，等待ceil(专用长度*20)。
专用不存在而普通存在时请求音高75，等待ceil(普通长度/0.75*20)。
两者均不存在时基础等待10单位。
上述基础等待再加2才开始下落。
下落开始隐藏影子并请求Pkmn faint音。
下落同时淡0、向下移动裁线减顶并设置bottom裁切。
结束隐藏成员后同刻opacity恢复255。
源注释所称最少20不覆盖实际最少10表达式。''',
58: '''成功由原numShakes>=4确定，critical且原shake正才把展示次数压1。
投球保存原影子可见性并使用玩家owner训练家。
投球起(-6,246)、中Y78、终(canonicalX,112)、地面Y为canonicalY-4。
成功球保存临时精灵索引，失败为-1。
Safari仅在showingTrainer且训练家存在且宽>=2高时采用训练家投掷轨道。
投掷音按critical与普通区分，起点为手中球累计时长0或7。
投球弧线16单位，绝对9置成员层加1，起点+16请求击中音。
球累计时长+6开始开球，禁开球SE，开球结束开始捕获burst。
捕获吸入起点请求Battle jump to ball，5单位移至球心并缩0，结束隐藏，不写混色。
原可见影子同5单位缩0淡0并隐藏。
捕获burst结束合球，3单位变tone(96,64,-160,160)，+5起3单位恢复tone0。
critical空摇从累计时长+3开始，0/+4请求摇音。
critical空摇X依次+4/1单位、-4/2单位、+4/2单位、-4/2单位、回中心/1单位，再等3。
四次弹地半程时长4/4/3/2，反弹高度分母1/2/4/8。
首弹跳过上行，后续弹地压缩(100+5*(5-i),100-5*(5-i))再2单位恢复100。
每弹落地音量100-7i，终点把成员位置设到地面。
落地后等待12，地面摇动至多min(展示次数,3)。
第i次地面摇X振幅2*(4-i)、角振幅5*(4-i)，2/4/2单位左右回中，间隔8。
成功接成功三星轨道。
失败把球层置成员层减1，开球不压缩、释放burst，+2起2单位球淡0。
失败成员混色alpha255后出现至原位置并叫声。
失败仅原影子可见时+5显示、zoom100并10单位淡255。
成功dispose把球从临时销毁列表移出并赋captureBall；其他临时图形照常销毁。''',
59: '''挡球起(-6,246)、中Y78、终(canonicalX,112)，中X190不消费。
挡球球层90，0请求投掷音，弧线16单位。
挡球随后请求落球音，8单位退到(-32,H-64)并滚3周。
挡球不进入吸入、捕获判定或捕获球保留。''',
60: '''Debug场景不建立视觉图形。
Debug初始化固定选择记忆。
列明的视觉入口是空操作。
blitz随机30不是实际玩家输入。''',
61: '''Debug消息仅可选写日志。
Debug确认恒真。
Debug命令列表返回0。
Debug物品选择返回-1。
Debug遗忘返回0。''',
62: '''Debug命令先以1/15选择背包。
剩余条件下Call以1/10概率选择。
Debug招式缺失的单数move读取可失败。
Debug目标从对方存活成员随机选择。
Debug队伍最多尝试50候选并让渡接收方。''',
63: '''非暗影捕获个体先命名并写名。
满队接收有询问及必须入队模式。
99是列表取消的独立返回值。
换出旧成员先入盒再从队伍删除。
消息后才左移四类队伍记忆。
新捕获个体普通存放消息后才回填初始道具记忆。''',
64: '''图鉴先分别写caught、seen及owned条件状态。
新增图鉴页要求三个独立门。
暗影捕获另行登记。
捕获队列在全部个体处理后才清空。
中途异常不回滚已处理前缀。''',
65: '''倒下目标改选同侧存活者。
无可用目标可在后续nil查询提前失败。
投掷消息先于不可捕获挡球判断。
0..3分别走失败展示、效果与统计。
成功先移除场上成员再经验结算。
成功后还处理结果、球效果、形态、离场、藏球和待接收队列。
首次球标记与投掷结果分开更新。''',
66: '''调试直捕返回4。
UltraBeast对非Beast球有额外修正。
捕获率经过HP、球率和状态浮点计算后floor且最少1。
必捕门先于普通摇动检查。
普通至多四次检查并在首次失败停止。
critical资格和阈值消费图鉴倍数及护符。
该mixin混入Battle。''',
67: '''cel有27个索引及25种语义属性，见WP74字段合同。
轴退化时变换比例置0。
立绘中心消费origin和zoom。
反向判定比较源线与目标线X方向。
重置cel保留坐标、图案和焦点。''',
68: '''旧RPG屏幕焦点转换采用上下64偏移。
转换复制图帧及timing。
追加动画扩容额外1帧。
追加偏移坐标并排序时序。
复制出的属性与原属性分离。''',
69: '''时序分五类。
新时序音量默认80。
新时序音高默认100。
新时序时长默认5。
可选字段允许nil且兼容getter。
文字帧号为一基。''',
70: '''集合构造才保证至少1项。
集合持有独立内部数组。
按名返回首个同名项。
compact、insert、delete及resize分别改变集合。
selected越界时可赋为len而非len-1。''',
71: '''动画默认一帧并建立双锁定成员。
常规帧60槽。
speed默认20但播放器不消费。
resize允许0帧，没有全局至少一帧守卫。''',
72: '''每个实际访问帧先活动渐变后当帧事件。
命名SE与空名用户叫声分支不同。
有图与纯色板使用不同坐标分支。
背景及前景各共享旧值。
前景oldfo[2]捕获前景自身opacity。
可选坐标nil的负号可在后续设置前失败。
flash字段未由该播放器执行。''',
73: '''nil cel隐藏对应精灵。
普通图案表源区192x192且每行5格。
负图案使用用户/目标整幅立绘。
cel分别应用镜像、百分比缩放、颜色、tone及焦点层次。
编辑器半透明分支的布尔与数值比较不成立。''',
74: '''播放器借用用户/目标bitmap且不拥有其销毁。
播放器拥有58粒子及四背景前景。
discard仅移除用户/目标参与。
start建立时钟。
初始焦点中心及线变换建立后不逐帧重捕获。''',
75: '''播放器按经过时间*20向下取整帧号。
相同帧不重复处理。
迟到跳帧不补被跳时序。
先分配图样表再按pattern改回借用立绘。
末帧结束及循环各有分支。
焦点分全屏、用户、目标及双方连线。
反向普通图案镜像取反。
编辑播放偏移64。''',
76: '''球效果有四个独立handler集合。
缺handler回退false或原捕获率。
失败统计先增后调用失败handler。''',
77: '''MASTER必捕。
Great及Safari倍率1.5，Ultra倍率2。
Net及Repeat按配置倍率3.5或3。
Dive读取战斗环境。
Nest读取目标等级。
Timer读取经过轮数。
Dusk读取时段2。
Quick仅首轮倍率5。''',
78: '''Fast以速度>=100开门。
Level读取本侧最高等级比较。
Lure要求钓鱼战斗类型。
Heavy按配置使用不同重量阈值。
Heavy原rate为0时不改，否则钳在1..255。
Love排除同性别并要求同物种。
Moon检查整进化家族的月之石进化。
加成捕获率最高255。''',
79: '''Sport倍率1.5。
Dream睡眠倍率4。
Beast对UltraBeast倍率5，否则0.1。
Heal捕获效果恢复个体。
Friend按配置设友好150或200。
没有注册默认失败效果handler。'''
}

fw = get('forward-mapping')
assert set(MANUAL) == set(range(1, 80))
DETAILED = {43,44,45,46,47,48,49,50,51,52,54,55,56,57,58,59}
facts = []
for group in fw['facts']:
    number = int(group['id'][-3:])
    for i, proposition in enumerate(MANUAL[number].splitlines(), 1):
        facts.append(dict(id=f"{group['id']}.A{i:02}", group=group['id'], source_range=group['source_range'],
                          assertion=proposition, premise='固定R；该入口实际被调用；输入及资源满足该条所述分支；无其它并发写入。',
                          consumer=group['necessary_consumers'], formal_links=group['formal_links'],
                          disposition='PROPOSED_SCOPE_GAP_GR8_EXTCP_002' if number in DETAILED else 'STATIC_CONTRACT_COMPARISON',
                          evidence='SOURCE_STATIC_NOT_EXECUTED', reception='PENDING_MAIN_REVIEW'))

basepath = 'Data/Scripts/011_Battle/004_Scene/007_Battle_Scene_BaseAnimation.rb'
base = git(REF, 'show', R + ':' + basepath).decode().splitlines()
release_names = ['ray.start_tone','ray.end_tone','upper_particle.resource','upper_particle.start_tone','upper_particle.end_tone',
                 'lower_particle.resource','lower_particle.start_tone','lower_particle.end_tone','upper_glare.resource',
                 'upper_glare.start_tone','upper_glare.end_tone','lower_glare.resource','lower_glare.start_tone','lower_glare.end_tone']
capture_names = ['upper_glare.resource','upper_glare.start_tone','upper_glare.end_tone','middle_glare.resource',
                 'middle_glare.start_tone','middle_glare.end_tone','lower_glare.resource','lower_glare.start_tone',
                 'lower_glare.end_tone','upper_particle.resource','upper_particle.start_tone','upper_particle.end_tone',
                 'lower_particle.resource','lower_particle.start_tone','lower_particle.end_tone','ring.start_tone','ring.end_tone']

def record_table(name, start, end, names, group, consumer_range, expected_leaves):
    # Read all records, retain per-field source lines, and crosswalk each index.
    lines = base[start-1:end]
    starts = [(start+i, re.search(r':(\w+)\s*=>', line).group(1)) for i,line in enumerate(lines) if re.search(r':(\w+)\s*=>',line)]
    records=[]; leaves=0
    for index,(first,ball) in enumerate(starts):
        last=starts[index+1][0]-1 if index+1<len(starts) else end-2
        text='\n'.join(x.split('#')[0] for x in base[first-1:last])
        expr=text[text.index('['):text.rindex(']')+1]
        tokens=list(re.finditer(r'Tone\.new\(([^)]+)\)|"([^"]+)"',expr))
        assert len(tokens)==len(names), (name,ball,len(tokens))
        fields=[]
        for field_index,(field,tok) in enumerate(zip(names,tokens)):
            value=ast.literal_eval('['+tok.group(1)+']') if tok.group(1) else tok.group(2)
            line=first+text[:text.index('[')+tok.start()].count('\n')
            dormant=(name=='release' and ball=='CHERISHBALL' and field.startswith('ray.'))
            hidden=(name=='capture' and ball=='NESTBALL' and field.startswith('lower_particle.'))
            disposition='READ_VALUE_OVERRIDDEN_BY_CHERISH_CYCLE' if dormant else ('REQUESTED_FOR_SAME_TICK_HIDDEN_PARTICLE' if hidden else 'REQUESTED_BY_NAMED_CONSUMER')
            fields.append(dict(id=f'EXTCP-{name.upper()}-{ball}-{field}', index=field_index, field=field,
                               value=value, scalar_leaves=3 if isinstance(value,list) else 1, source_line=line,
                               consumer_range=consumer_range, disposition=disposition,
                               formal_disposition='PROPOSED_SCOPE_GAP_GR8_EXTCP_002', reception='PENDING_MAIN_REVIEW'))
            leaves+=3 if isinstance(value,list) else 1
        records.append(dict(ball=ball, source_range=[first,last], fields=fields))
    assert len(records)==16 and leaves==expected_leaves
    result=dict(schema='r8-typed-variance-facts/v1', source=identity(REF,R,basepath), group=group,
                source_range=[start,end], rows=16, logical_fields_per_row=len(names),
                logical_assertions=16*len(names), scalar_leaves=leaves,
                tone_channels=['red','green','blue'], omitted_fourth_tone_argument='Not supplied by these calls; host default not independently executed.',
                fallback='POKEBALL when ball identity has no record', field_consumer_crosswalk={str(i):n for i,n in enumerate(names)},
                evidence='Complete source table read and complete consumer read; extraction is serialization only.', records=records)
    put(name+'-variance-fields',result)
    return result

release = record_table('release',255,346,release_names,'EXTCP-F045',[347,457],544)
capture = record_table('capture',458,566,capture_names,'EXTCP-F047',[567,725],656)

colors=[]
for line_no,line in enumerate(base[72:92],73):
    m=re.search(r'(?:when :(\w+)\s+then return|return) Color\.new\(([^)]+)\)',line)
    if m:
        colors.append(dict(id='EXTCP-COLOR-'+(m.group(1) or 'DEFAULT'),ball=m.group(1) or 'DEFAULT',
                           rgb=ast.literal_eval('['+m.group(2)+']'),source_line=line_no,
                           consumer_groups=['EXTCP-F055','EXTCP-F056','EXTCP-F058'],
                           formal_disposition='PROPOSED_SCOPE_GAP_GR8_EXTCP_002', reception='PENDING_MAIN_REVIEW'))
assert len(colors)==16
put('ball-color-fields',dict(schema='r8-typed-color-facts/v1',source=identity(REF,R,basepath),group='EXTCP-F043',
    logical_assertions=16,scalar_leaves=48,records=colors,alpha='Separate call-site assignment; not inferred from the RGB table.'))

put('atomic-assertions',dict(schema='r8-atomic-review/v1',
    definition='One independently checkable semantic proposition, or one named typed variance-table field. Vectors are typed values, not extra propositions. Scalar leaves of the finite tables are reported separately. Loop instances are covered by the stated finite index rule, not counted again.',
    primary_files=12, primary_structures=79, manual_assertions=len(facts), variance_field_assertions=496,color_field_assertions=16,
    atomic_assertion_denominator=len(facts)+512, variance_scalar_leaves=1200,color_scalar_leaves=48,
    full_read_not_inferred_from_count=True, execution_credit=False, independent_receptions=0,
    assertions=facts, table_artifacts=['release-variance-fields.json','capture-variance-fields.json','ball-color-fields.json']))

for group in fw['facts']:
    number=int(group['id'][-3:])
    group['atomic_assertion_ids']=[a['id'] for a in facts if a['group']==group['id']]
    group['formal_scope']='逐条断言见atomic-assertions.json；已读源事实、正文接口支持和待裁决精度分开，未授最终PASS。'
    if number in DETAILED:
        group['status']='SOURCE_FIELDS_MAPPED_PROPOSED_SCOPE_GAP'
        group['mapping_disposition']='GR8-EXTCP-002：WP67-A接口支持不等于逐字段覆盖；WP74逐帧作者数据库不承接这些固定PictureEx轨道。精确轨迹/资源tone是否保留由主审裁决。'
    else: group['status']='SOURCE_ATOMIC_ASSERTIONS_STATIC_COMPARED'
    if number in {45,47}: group['typed_field_evidence']='release-variance-fields.json' if number==45 else 'capture-variance-fields.json'
    if number == 43: group['typed_field_evidence']='ball-color-fields.json'
fw['schema']='r8-forward/v3'
fw['atomic_assertion_denominator']=len(facts)+512
fw['manual_assertion_denominator']=len(facts)
fw['variance_field_denominator']=496
fw['color_field_denominator']=16
fw['all_semantic_pass']=False
fw['granularity_gap']='NONE_UNMAPPED_IN_DECLARED_PRIMARY_FACT_LEDGER; coverage-policy proposal and independent receptions remain open.'
fw['count_scope']='12 primary files / 79 structures; finite typed fields and semantic propositions, not a claim of global reception or line-count proof.'
put('forward-mapping',fw)

# Exact additional source/formal reads completed in the continuation. Partial
# means the complete named methods below, not the rest of that source file.
ledger=get('reading-ledger')
new_reads=[
 (SPEC,B,'deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md',None,'Shared resource/SE/cry lookup contracts; no claim that WP15 specifies fixed battle trajectories.'),
 (SPEC,B,'deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md',None,'Whole file read; PictureEx 6.3 and explicit battle-domain forwarding distinguished.'),
 (SPEC,B,'deliverables/final-specification-set/scope-statement.md',None,'Whole scope statement read; media/host limits do not exempt static output requests.'),
 (REF,R,'Data/Scripts/010_Data/002_PBS data/009_Species_files.rb',[[183,244]],'Complete cry selector/play/length methods; suffix selection does not fall back, length helper can fall back.')]
new_reads.extend([
 (REF,R,'Data/Scripts/007_Objects and windows/001_RPG_Cache.rb',None,'Whole cache/reference-count file; direct load differs from GifBitmap local rescue.'),
 (REF,R,'Data/Scripts/007_Objects and windows/007_BitmapSprite.rb',None,'Whole 243-line file, including IconSprite clear/name/load/restore order and frame update.'),
 (REF,R,'Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb',None,'Whole 228-line file; prefixed PNG branch validates dimensions, ordinary GifBitmap branch rescues to 32x32 placeholder.'),
 (REF,R,'Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb',[[1,173]],'Complete selection/register/target methods through132 read; priority method tail after173 not read or accepted. Eligibility delegates to named combat receivers.'),
 (REF,R,'Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb',[[95,220],[680,724]],'HP/status setters, display-only Illusion properties and positional wrappers; partial edges retained, no whole Battler credit.')])
for repo,commit,path,intervals,purpose in new_reads:
    ident=identity(repo,commit,path)
    actual=(repo/path).read_bytes()
    assert len(actual)==ident['bytes'] and hashlib.sha256(actual).hexdigest()==ident['sha256']
    if intervals is None: intervals=[[1,ident['lines']]]
    entry={**ident,'actual_cloud_path':str(repo/path), 'semantic_status':'FULL_READ' if intervals==[[1,ident['lines']]] else 'PARTIAL_READ_NECESSARY_METHODS',
           'read_intervals':intervals,'purpose':purpose,'evidence_level':'SOURCE_STATIC' if repo==REF else 'FORMAL_TEXT_READ',
           'reception':'PENDING_MAIN_REVIEW','continuation_recorded_utc':NOW}
    old=next((x for x in ledger['dependency'] if x['path']==path),None)
    if old: old.update(entry)
    else: ledger['dependency'].append(entry)
ledger['updated_utc']=NOW
ledger['continuation_read_details']=[dict(groups=[f'EXTCP-F{i:03}' for i in sorted(DETAILED)],
    action='All 16 ranges reread in full and individually mapped; both tables and consumer index mappings reread in full.',
    evidence='atomic-assertions.json and two variance-field artifacts',reception='PENDING_MAIN_REVIEW')]
put('reading-ledger',ledger)
print(json.dumps(dict(manual_assertions=len(facts),table_fields=496,color_fields=16,scalar_leaves=1248,total=len(facts)+512,dependency_files=len(ledger['dependency'])),ensure_ascii=False))
