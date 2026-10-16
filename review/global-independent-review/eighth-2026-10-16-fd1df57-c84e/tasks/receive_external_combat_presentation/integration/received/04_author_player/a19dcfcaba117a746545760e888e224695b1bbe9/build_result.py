"""Build this bounded review receipt from explicit per-object judgments.
Only reads frozen inputs and writes files next to this script. No reference execution.
"""
import json, hashlib, subprocess, os, datetime
from pathlib import Path
OUT=Path(__file__).resolve().parent
TASK=OUT.parent.parent
REPO=next(p for p in OUT.parents if (p/"AGENTS.md").is_file())
REF=Path("/workspace/pokemon-essentials")
CONTRACT="35d85e4484b892ebc32542346861440638d2183c"
X=json.loads((TASK/"continuation/04_author_player/readset.complete.json").read_text())
R=X["fixed_R"]; B=X["fixed_B8"]
def save(n,x): (OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n")
def ident(repo,commit,path):
    raw=(repo/path).read_bytes()
    stored=subprocess.check_output(["git","-C",str(repo),"show",commit+":"+path])
    assert raw==stored, path
    mode,_,blob=subprocess.check_output(["git","-C",str(repo),"ls-tree",commit,"--",path],text=True).split()[:3]
    assert blob==hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
    return dict(commit=commit,path=path,mode=mode,git_blob=blob,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),lines=len(raw.splitlines()))
# These are unique authored decisions, not inferred from prior PASS or counts.
J={
"025":[
("对方先OppMove，命中noFlip；无对方映射才共用；己方只共用。注册对象/字符串先由Move.try_get取登记身份。", "§9.4，266", "Opp→11与共用→10并存选11；删Opp才10。"),
("只有精确命中传入hitNum并与编号相加，0号动画在Ruby仍是真值。", "§9.4，266", "精确40/hit2→42；hit0→40。"),
("18类型×6身份全部逐格对照，空格和FAIRY共用TACKLE/SWIFT也保持；108格不另增主对象。", "§9.4.1，275–296", "FIRE特殊→EMBER；Ground自身变化空格仍继续候选。"),
("原始category先取值；目标数>1或敌侧门+3；status且目标数>0再独立+3，可能得到8。", "§9.4.1，275", "变化多目标可先到8，再减3试5；不能合并为一次+3。"),
("默认身份各次调用details省略hitNum，缺省0；最终TACKLE同理。", "§9.4，266；§9.4.1，298", "精确缺失/hit2/EMBER→10仍10。"),
("本格已登记才查；映射缺失继续条件减3格、列2，再TACKLE；未知类型直接最后回退。", "§9.4.1，275–298", "EMBER/SUNNYDAY/TACKLE的10→20→30→nil，分次删映射。"),
("findMoveAnimation的普通rescue覆盖加载、资料与索引等该函数中的普通异常后返回nil；不是整个播放/宿主的统一容错。", "§9.4，266–271", "加载映射抛普通异常→nil；后续核心异常无此保护。")],
"026":[
("场景先查ID；无ID早退，取得ID后加载库，无库再早退。已有缓存优先，不等于文件不存在永远无库。", "§9.4，266–269", "映射有而无缓存/无库文件→不进核心；缓存有效则可播放。"),
("有ID及库后进入保存全部既有影子包装；OppMove交换核心参数并设置oppMove以保叫声实际使用者；核心空动画仍可正常返回包装。", "§9.4，267、271", "第三席影子true正常隐藏后恢复；异常没有ensure。"),
("Common精确拼接Common:与输入名，遍历跳nil取首个同名；空输入/无库/无同名分别不播放。", "§9.4，267；WP74§15", "Common:X与Common: X不同，重复名仅首个。"),
("Common直接进核心、不自带全席影子包装；外层仍可包，不能说任何Common从不隐藏影子。", "§9.4，267、271", "独立Common:HealthUp不清第三席影子；move wrapper会清。"),
("核心按当前用户/目标位置和位图高度半值建立双方线段；缺位图高度128，缺目标继承用户位置/高度。单点锚点由播放器构造另捕获中心。", "§9.4，267；WP74§10.2，333", "bitmap高128的Y减64；单点中心还读src_rect/origin/zoom。"),
("核心正常循环结束后dispose，再恢复保存的x/y并调用各pbSetOrigin；成员重设底部中点，不是保存任意原ox/oy的快照，也不保证全部sprite属性恢复。", "§9.4，267、271", "正常返回恢复位置；中途异常无ensure，不授原bitmap/tone/visible等通用回滚。")],
"027":[
("球公共入口用集合get_from_name取Common:精确首同名，空名/无集合/无同名早退。", "§9.4，268；WP74§10.2，333", "无同名不构造；重复同名用首个。"),
("discard只把动画槽0/1置nil；保留借图、user/target引用与焦点，可供其它粒子槽的负pattern/层次使用。", "§9.4，268；WP74§10.2，333", "槽0不再参与；槽2若pattern=-1仍可借user bitmap。"),
("调用set_target_origin以传入(x,y)覆盖构造时目标单点锚点，无需目标精灵；不是每帧追踪。", "WP74§10.2，333–335", "focus=1粒子按覆盖锚点偏移；screen不消费它。"),
("start建立时钟后push场景队列，函数不进入阻塞循环；pbGraphicsUpdate逐项update、完成后dispose/compact。固定R全Scripts只找到此入口定义，无默认caller。", "§9.4，268；WP74§10.2，333", "直接调用正常返回即入队；后续场景更新才推进，不冒默认球轨道接线。")],
"067":[
("布局最大索引26，共27存储位置；9/10无命名字段，实际25语义属性，不能说27个语义字段。", "WP74§2，25–28", "25语义字段与可见/opacity分离；布局不要求未来数组API。"),
("源轴dx或dy为0时该轴归一比例取0，再映射到目标轴起点；其它轴各自线性。", "WP74§10.2，333", "源X退化→目标X起点，Y非退化照常映射。"),
("中心取src_rect宽高各整数半值，减origin后乘zoom再加x/y；无sprite/已dispose→0,0，缺位图→sprite坐标。", "WP74§10.2，333–335", "origin与zoom改变中心；缺bitmap仍有位置锚点。"),
("比较源线X方向与目标线X方向，源退化返回false；只在双焦点且普通pattern时翻转mirror。", "WP74§10.2，333", "源递增/目标递减→反向；负个体图案不反转。"),
("新cel先赋x/y/pattern/focus/locked，再重置其它默认；重置不动x/y/pattern/focus/locked。", "WP74§2、§4.4，123", "locked1经reset仍1；zoom100/opacity255/priority1。")],
"068":[
("必须更正原简写：旧position0是Y−64、position2是Y+64，非屏幕支直接加偏移；position3屏幕支使用两线变换，不加该64偏移。", "WP74§14.3，413–415", "相同旧Y10在position0→−54、2→74；3走变换。仅定义，未证活动caller。"),
("转换逐原帧/cell复制，pattern=-1产nil；缩放两轴同值、角度/镜像/opacity复制、blend强制0；timing帧/SE/flash字段复制，不代表flash被播放器执行。", "WP74§14.3；§2、§10.2", "flash保存与执行分列；原图帧顺序保留。"),
("追加覆盖范围抵达或越过当前尾时扩到frame+other.frames.length+1并更新frame_max，含一额外帧；实际复制循环依other.frame_max。", "WP74§14.3，413–415", "原2帧，起0加2帧→总3；不将此孤立辅助强制未来API。"),
("追加从目标原cell_max起写入、每cel只X/Y加给定偏移，其余8列分别复制；timing帧加偏移后按frame排序，不承诺同帧稳定顺序。", "WP74§14.3，413–415", "timing原f2/起3→f5；普通cellX10+5→15。"),
("分离须限实际新建/clone字段：新Frame列值与新Timing/SE/flashColor等分开；fromOther只复制元资料、无帧；转换graphic直接共享原animation_name引用，不是所有属性均深复制。", "WP74§14.3，413–415", "name.clone与graphic直接赋值不同，未建通用深拷贝合同；完整静态定义已接收。")],
"069":[
("timing类型0音效、1设BG、2渐变BG、3设FG、4渐变FG；旧timingType nil/false读为0，未知数值文本为空且无对应执行支。", "WP74§2，27；§9", "type0命名SE与空名叫声另分支。"),
("新时序volume=80，编辑器音量0..100，确认写入；取消原对象不改。", "WP74§2，27；§9.1，309", "新建不调确认80；取消不新增。"),
("新时序pitch=100，编辑范围20..250；请求保留具体pitch，不证实实际听感。", "WP74§2，27；§9.1，309", "默认100与选120各按保存值请求。"),
("新duration=5；getter nil/false回退5而0保持0，0渐变只捕获不活动。", "WP74§2，27；§9.3、§10.2a", "duration0≠nil，前者不立即应用目标。"),
("BG坐标、opacity和RGBA初始nil，控件未参与时仍nil；仅timingType/duration有兼容getter，不能说全部nil字段自动补0。", "WP74§2、§9.2–9.3、§10.2a", "设置有图且bgX=nil可先加载后在取负失败；正常UI设置会写数值。"),
("列表文字frame+1，五类分别显示名称/音量/音高/时长与可选坐标颜色；未参与渐变项省略或显示短横。直接损坏对象格式化不保证成功。", "WP74§9.4，319–321", "内部f0显示[1]；新设置型opacity未填的直接调用不许推统一容错。")],
"070":[
("集合构造把size<1改1；delete_at或resize可得0，不是全生命周期非空不变量。", "WP74§2、§7.1、§12", "单项delete后可0，构造size0仍1。"),
("每实例新建独立@array容器并逐项新建动画；[]=/insert可接受同一对象，不推出所有存入成员深复制。", "WP74§2、§7.1", "两次构造容器独立；显式传同对象可有共享。"),
("get_from_name按@array顺序取首个非nil精确同名，无命中nil。", "WP74§15；WP67A§9.4", "重复Common:X只首个，Common: X独立。"),
("compact就地去nil，insert移位，delete_at移除，resize尾删/新建；组织器直接操作集合并只在相应保存入口落盘。", "WP74§7.1、§12、§16", "删除可0；未保存不等于内存无改动。"),
("resize后selected>=len则赋len本身；不是len−1，len0时selected0也可为空槽。", "WP74§7.1，209", "selected2缩3→2后仍2，立即读取为空，导航可恢复。")],
"071":[
("新动画至少一帧，每新帧只有默认0/1双个体槽初建，-1/-2、focus2/1、locked1；其它常规槽可空。", "WP74§2，24–25；§6.2", "构造size0仍一帧；扩帧同样建两槽。"),
("MAX_SPRITES60定义可渲染0..59，帧实际数组可长于或短于60；超过槽无对应player sprite，不能误作序列必长60。", "WP74§2、§4.5、§6.3", "槽60数据可存、玩家无对应sprite。"),
("speed getter默认20；player用自身固定20，source中speed字段无此consumer，不用元数据改变帧率。", "WP74§2、§10.2，331", "元数据40仍按20的请求时钟；非实际时钟观察。"),
("直接resize(0)确可截成0帧；构造/编辑器1..1000门才至少一帧。零帧非循环更新即结束，looping0可能异常；不增加内部helper必需API。", "WP74§2、§6.2、§14.3", "正常UI滑杆最小1；直接定义的0帧不据此推UI承诺矛盾。")],
"072":[
("playTiming每访问帧先按存储序活动渐变(s<f<=s+d且d>0)，再按序f==s的事件，起始帧只捕获。", "WP74§10.2a，340", "B于f2启动先看到A当次100，再捕获100。"),
("非空名请求Anim/SE并传volume/pitch；空名且user.pokemon存在则物种/形态叫声，编辑MiniBattler.pokemon未设故静音。", "WP74§9.1、§10.2，336", "普通战斗空名可叫声；编辑预览无个体不发声请求。"),
("设置图形先setBitmap再负坐标/color/opacity并隐藏纯色；空名清图、图opacity0、写纯色。渐变按当前bitmap nil选纯色或图形，纯色不移动。", "WP74§10.2、§10.2a", "普通缺图占位非nil仍图形支；设置X10/目标20/d4中点25末40。"),
("BG/FG各一个可变旧值数组，渐变起点捕获完整位置/opacity/RGBA；同层后来项覆盖，活动项写完整RGBA，未参与颜色也回写共享旧通道。", "WP74§10.2a，340–348", "B红-only在s2重捕100，A在f3写175；另一层B则A150。"),
("固定581明确捕获foGraphic.opacity，非bgGraphic；无图分支捕foColor.opacity。H001旧110结论撤回有独立源码反证。", "WP74§10.2a，344；H001完整原提案", "背景20/前景100，前景目标200/d2，f2中点150；NOT_EXECUTED。"),
("有图设置调用负bgX/负bgY后才其余赋值，nil不被后面的||0保护；可能已完成换图但后续失败，无通用回滚。", "WP74§10.2a、§19的正常输入/宿主边界", "直接非法设置bgX=nil可在加载后失败；正常编辑器OK写数值，不能扩成默认UI必失败。"),
("flash属性可存/转换，但实际执行行是注释；播放器仅当前五类分支，不执行flash。", "WP74§2、§10.2、§14.3", "有flash元数据不构成屏幕闪烁观察或新需求。")],
"073":[
("helper在sprite存在而frame=nil时隐藏并把src_rect置1×1后返回；播放器另先隐藏所有常规sprite并跳nil cel。", "WP74§10.2，332", "上一帧有图/本帧空→不延续显示。"),
("pattern>=0按192格、列mod5/行整除5选源区，不由资源实际尺寸推保证有效像素。", "WP74§2、§10.2", "pattern6→第1列第1行，192×192请求。"),
("必须限合法-1/-2：player分别换user/target借图，helper对负pattern取当前bitmap整幅；其它非法负数不保证是个体图。", "WP74§2、§10.2，332", "-1用user全图、-2用target全图；-3不在合法编辑域。"),
("分别应用mirror>0、zoom/100、可见==1、opacity、RGBA/tone、中心origin及X/Y；非个体sprite按priority和focus给z默认/前后偏移。", "WP74§10.2，332–333", "focus=target/priority2→target.z−1；无focus立绘则默认层。"),
("布尔取反结果与数值1比较恒不等，所谓编辑半透分支不命中；可见0是隐藏而非半透明。", "WP74§10.2，332；AN-M23", "可见0/1两对照与opacity独立；无宿主像素执行。")],
"074":[
("构造保留用户/目标既有sprite及bitmap引用；dispose只处置自有图样表/58sprite/四层，不销毁借用个体bitmap/sprite，仍不保证恢复其全部属性。", "WP74§10.1–10.2；WP67A§9.4", "借图不能由particle dispose推出被销毁；核心另仅恢复x/y并重设origin。"),
("常规总槽60，0/1为借sprite，2..59共58个新sprite；另建BG图/色与FG图/色，层z5/85、opacity0。", "WP74§10.1–10.2", "缺user/target时0/1可nil，58自有粒子仍建。"),
("discard只清播放数组0/1，不清refs/借图/旧中心/叫声user，释放仍从2开始。", "WP74§10.2，333；WP67A§9.4，268", "球公共槽0不动成员，但槽2可借个体图和保留目标层次。"),
("start设置frame0并读System.uptime；animDone?只看frame<0。构造尚未start的frame−1也算完成。", "WP74§10.2、§10.2a", "构造→未开始完成标记；start后等待update。"),
("构造捕获中心；显式target_origin可覆盖，显式lineTransform存两线；更新不重新捕获sprite移动后中心。", "WP74§10.2，333–335", "同帧使用者X200/粒子X128，预览264/192；不是后槽跟随200。")],
"075":[
("非负经过时间乘固定20取整，不消费speed；单次迟到可跨帧，时间来自宿主uptime仅静态读取。", "WP74§10.2a，350", "0.1秒→帧2；未测真实精度/性能。"),
("必须限cel/timing：相同frame在sheet加载及四层update之后返回，避免重复cel重设和timing触发，不是整个update无工作。", "WP74§10.2a，350", "同f重复不重发SE；plane update调用仍先发生。"),
("只处理实际选中帧，无追补循环；跳过起始帧不补设置/SE/旧值捕获，跳过终点不保证目标值。", "WP74§10.2a，350；B20-C026", "访问f0再f3不会补f1音效；捕获没发生可使旧值缺失导致后续失败。"),
("首次按图样名/hue加载并deanimate后给所有存在sprite赋sheet；访问具体cel时-1/-2改回借图，其它图案用sheet。", "WP74§10.2，332", "不会把一次全槽sheet分配误当最终-1图；加载异常不通用恢复。"),
("越过末尾非循环置frame−1、销毁sheet并返回；循环取余并把起时加一周期；零长/极迟到/旧帧缓存不能推普遍无界循环保障。正常入口looping=false。", "WP74§10.2，331；WP67A§9.4", "普通末帧后结束；合法looping是另分支，未观察宿主。"),
("focus1/2相对捕获目标/用户锚点；focus3有两线才变换，无线时next会跳过该cel编辑偏移；focus4保持原坐标。", "WP74§10.2，333", "正常caller先设两线；screen不随立绘。"),
("双焦点、源/目标X反向且pattern>=0才把已应用mirror取反；个体负pattern不做此翻转。", "WP74§10.2，333", "普通mirror=false→true；负pattern原mirror保持。"),
("inEditor时各正常处理cel的x/y最后+64；画布常规应用也加64；场景战斗调用不传editor=true。", "WP74§10.1–10.2，327、335", "原128→预览192，战斗仍128；不推鼠标粘贴等其它入口基准。")]
}

READS=[
("Data/Scripts/011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb",[[1,844]],["a9b68b","105cbe","292ea1","fb40d9"],"PRIMARY_WHOLE","全部cel几何/转换/容器/timing/player。474为方法头，475起body已连续补足至586。"),
("Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb",[[390,579]],["5fea84","0ee3be"],"PRIMARY_NECESSARY_COMPLETE_METHODS","影子包装、details/find、move/common/core、球公共队列；其余固定演出不授全文。"),
("Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb",[[1,64]],["0ee3be"],"NECESSARY_WHOLE","两缓存读取/清理；读取失败与查询rescue分层。"),
("Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb",[[1,148]],["2f0ae4"],"NECESSARY_COMPLETE_METHODS","常量/坐标、update/graphics/input/frame/refresh及队列状态；后续窗口只见前缀不计。"),
("Data/Scripts/011_Battle/001_Battle/001_Battle.rb",[[838,844]],["2f0ae4"],"NECESSARY_COMPLETE_METHODS","showAnims领域包装两个完整方法。"),
("Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb",[[1271,1321]],["6d6785"],"NECESSARY_COMPLETE_METHODS","完整compile_animations及注释旧格式桥；不签全compiler。"),
("Data/Scripts/020_Debug/002_Animation editor/001_AnimEditor_SceneElements.rb",[[350,427],[451,511],[893,930]],["6163a0","c72395","7ea1fe"],"NECESSARY_COMPLETE_METHODS","画布构造/加载、完整play及update；正常恢复/释放与异常分开。"),
("Data/Scripts/020_Debug/002_Animation editor/005_AnimEditor_Functions.rb",[[1,24],[376,677],[951,1170]],["bfcc28","94fe11","6163a0","b785a1","ff92fd"],"NECESSARY_COMPLETE_METHODS","MiniBattler/MiniBattle；完整时序四函数；完整主循环与入口，预览/保存独立。"),
("Data/Scripts/020_Debug/002_Animation editor/004_AnimEditor_ExportImport.rb",[[89,146]],["c72395"],"NECESSARY_COMPLETE_METHODS","旧cel格式检测/转换与全量转换定义，非RPG转换，限定0..59。"),
("Data/Scripts/007_Objects and windows/009_Planes.rb",[[1,76]],["6d6785"],"NECESSARY_WHOLE","四图层的实际setter/清理委托；Plane update为空。"),
("Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb",[[1,228]],["0a5527","b785a1"],"NECESSARY_WHOLE","prefix PNG与普通GIF构造/占位、deanimate/释放全部读；真实解码未知。"),
("Data/Scripts/007_Objects and windows/001_RPG_Cache.rb",[[1,65],[116,144]],["b49108","a90bb5"],"NECESSARY_COMPLETE_METHODS","load_bitmap及fromCache/setKey；BitmapWrapper引用计数；tile方法片段不计。"),
("Data/Scripts/010_Data/002_PBS data/009_Species_files.rb",[[183,244]],["0a5527"],"NECESSARY_COMPLETE_METHODS","叫声选择/请求/长度完整；只接timing所用species/form选择，不裁CP002。"),
("Data/Scripts/011_Battle/004_Scene/007_Battle_Scene_BaseAnimation.rb",[[1,101]],["0763ef"],"NECESSARY_COMPLETE_METHODS","IR011只用Base update/addSprite/addNewSprite/dispose与addBallSprite来区分轨道所有权；额外RGB阅读不重复计主对象/字段。"),
("Data/Scripts/011_Battle/004_Scene/008_Battle_Scene_Animations.rb",[[462,524]],["b785a1"],"NECESSARY_COMPLETE_METHODS","完整对手派出类include BallMixin并登记PictureEx轨道，证明不是作者库player；ballBurst深层字段属02。"),
("Data/Scripts/010_Data/001_GameData.rb",[[78,116]],["fead91"],"NECESSARY_COMPLETE_METHODS","Symbol注册/exists/get/try_get完整，String转符号不trim。"),
("Data/Scripts/010_Data/002_PBS data/005_Move.rb",[[1,97]],["fead91"],"NECESSARY_COMPLETE_METHODS","category/type/target默认与status判定；原始类别与依世代物理特殊查询分开。"),
("Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb",[[1,212]],["bfcc28"],"NECESSARY_WHOLE","目标字段默认/全部登记；实际文件行数下方按身份核实。"),
("Data/Scripts/011_Battle/004_Scene/006_Battle_Scene_Objects.rb",[[571,575],[666,670]],["d481db"],"NECESSARY_COMPLETE_METHODS","成员/影子origin重设，非任意旧ox/oy快照。"),
("Data/Scripts/008_Audio/002_Audio_Play.rb",[[1,40],[202,219]],["a90bb5","d481db"],"NECESSARY_COMPLETE_METHODS","音效参数解析/请求路由，媒体执行未证。"),
("Data/Scripts/001_Technical/002_Files/001_FileTests.rb",[[109,115]],["a90bb5"],"NECESSARY_COMPLETE_METHODS","cry的SE解析委托；RTP内部检索/宿主不签全域。"),
("Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb",[[92,224]],["332ae4","eaf963"],"NECESSARY_COMPLETE_METHODS","完整必要LevelUp调用者；只接在场且正常逐级时调用公共动画，经验算法未重复主审。"),
("Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb",[[1,6]],["ff92fd"],"NECESSARY_COMPLETE_METHODS","完整abort抛出，无场景局部回滚。"),
("PBS/moves.txt",[[2603,2614],[2757,2767],[2782,2793],[2819,2827],[5326,5336]],["eaf963"],"NECESSARY_RECORDS","五个正常例身份/原始类别/目标记录完整；其余PBS未计。")]
reading=[]
for path,spans,chunks,kind,note in READS:
    row=ident(REF,R,path)
    if kind.endswith("WHOLE"): spans=[[1,row["lines"]]]
    assert all(1<=a<=b<=row["lines"] for a,b in spans),(path,spans,row["lines"])
    row.update(read_intervals=spans,tool_chunks=chunks,scope=kind,actual_reader=os.environ.get("CODEX_THREAD_ID","UNVERIFIED"),meaning=note,execution="SOURCE_STATIC_NOT_EXECUTED")
    reading.append(row)
F67="deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md"
F74="deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md"
for path,chunks,kind in [(F67,["33b297","77eaf9","c98472","a8be05"],"全文实读，只有本组9.4等接点核收；其它条款上下文阅读，不接管ui_full领域"),(F74,["a9ff1d","168c11","3b6baa","cf3d79"],"全文实读，按本组21反向命题及对应概念/定义核收，其它作者工具只上下文阅读")]:
    row=ident(REPO,B,path);row.update(read_intervals=[[1,row["lines"]]],tool_chunks=chunks,scope="FORMAL_FULL_READ_FINITE_RECEPTION",meaning=kind,execution="FORMAL_TEXT_NOT_EXECUTED");reading.append(row)
for path,spans,chunks in [
("deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md",[[154,192],[330,331]],["fa75e9","682f38"]),
("deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md",[[797,808],[846,851]],["682f38"])
]:
    row=ident(REPO,B,path);row.update(read_intervals=spans,tool_chunks=chunks,scope="FORMAL_NECESSARY_VECTORS",meaning="完整相关例子/前提/预期已读；超出本组算法的AN用例只上下文，不冒全表核收。",execution="DERIVED_VECTOR_NOT_EXECUTED");reading.append(row)
# Contract/state and compressed duplicate content are read as exact aliases, without extra credit.
contract_paths=["AGENTS.md",str((TASK/"continuation-contracts.json").relative_to(REPO)),str((TASK/"continuation/04_author_player/prompt.zh.md").relative_to(REPO)),str((TASK/"continuation/04_author_player/readset.complete.json").relative_to(REPO))]
contracts=[ident(REPO,CONTRACT,p) for p in contract_paths]
save("reading-ledger.json",dict(schema="gr8-cp04-reading/v1",contract_commit=CONTRACT,actual_reader=os.environ.get("CODEX_THREAD_ID"),contracts=contracts,contract_read_evidence=["9b0445","479188","cf84e0","723deb","56e49e","401dd3","a2515d","8fd147","35cb3b","e48e97","6eb817","e55126"],readset_remainder="原始完整readset嵌入对象与全局delegation文件精确相等；大重复源字段按同组共享值+逐对象差值无损呈现，非语义摘要。61项依赖候选全部读取身份/原作者声明，仅下方必要单元才授本context阅读信用。",inputs=reading,recovery="identity.json复核31原载荷身份并复用父恢复，未运行旧脚本。",output_repairs=[dict(chunks=["d15e00","8df61e","2edf36","8fd147"],reason="初期大输出截断；不能整包FULL_READ。后按完整字段/共享值无损去重，补齐12组67对象、原载荷31身份、61候选、3反向/3接口/完整提案及补件。"),dict(chunks=["fa75e9"],repair="682f38补读182–192及相关完整向量；不授被截断的全输出信用。"),dict(search_errors=["27f18a","b35af8","efd34d","7ea1fe","9ee8c1","332ae4"],reason="若干定位曾用错参考侧路径或仓库；exit2无缺失结论，已用rg --files/正确路径修复。")],configuration=dict(requested=dict(model="gpt-6.1-sol",effort="ultra",tier="default normal",Fast="off"),actual=dict(model="UNVERIFIED",effort="UNVERIFIED",tier="UNVERIFIED",speed="UNVERIFIED",Fast="UNVERIFIED",context=os.environ.get("CODEX_THREAD_ID"))),UPDATE_NOT_STARTED=True))
receipts=[]
groups={g["id"]:g for g in X["source_groups"]}
for original in X["primary_objects"]:
    group=original["group"];g=group[-3:];idx=int(original["id"].split(".A")[1])-1
    meaning,formal,control=J[g][idx]
    receipts.append(dict(id=original["id"],original_complete=original,accepted_complete_meaning=meaning,current_formal_locator=formal,source_complete_range=groups[group]["source_range"],source_read_evidence=["a9b68b","105cbe","292ea1","fb40d9"] if int(g)>=67 else ["5fea84","0ee3be"],consumer_join="interfaces.json的IF06及IR011/013/014；必要定义见reading-ledger，层内/跨域范围不外推。",normal_or_counter_control=control,decision="ACCEPTED_FINITE_SOURCE_STATIC_WITH_STATED_QUALIFIERS",reason="上列完整源单元与当前有关条款/必要实际入口支持该有限意义；内部无默认caller定义及合法UI门各按所述边界，不从源码结构产生未来API要求。",necessary_unreceived=[],execution="NOT_EXECUTED"))
assert len(receipts)==67 and len({a["id"] for a in receipts})==67
assert {g:len(v) for g,v in J.items()}=={g[-3:]:sum(o["group"]==g for o in X["primary_objects"]) for g in groups}
save("frozen-denominator.json",dict(schema="gr8-cp04-denominator/v1",contract_commit=CONTRACT,target_commit=X["target_commit"],target_checkout_tree=X["target_checkout_tree"],target_task_tree=X["target_task_tree"],B8=B,R=R,groups=X["source_groups"],primary_ids=[o["id"] for o in X["primary_objects"]],primary_count=67,reverse_ids=[s["id"] for o in X["reverse_current_contribution_objects"] for s in o["subassertions"]],reverse_count=21,interface_ids=[o["id"] for o in X["selected_reverse_interfaces"]],interface_count=3,not_extra_atoms="18×6默认身份格为F025.A03内部完整数据；重复引用不加主对象。全组1045/150/20及66provider不作本任务分母。",UPDATE_NOT_STARTED=True))
save("reception-ledger.json",dict(schema="gr8-cp04-reception/v1",status="READY_FOR_PARENT_RECEPTION",actual_receiver=os.environ.get("CODEX_THREAD_ID"),original_author="01a143b2-8ba3-76f5-a39d-7904a2dd1000",parent_receiver="01a14479-e75c-7131-85ed-aec1de217031",independence="运行环境CODEX_THREAD_ID与CODEX_SESSION_ID一致，且与原作者和父接收者不同；未spawn，不以角色改名计新审者。",primary=receipts,primary_received=67,primary_unreceived=0,necessary_units_unreceived=[],new_required=0,new_optional=0,new_policy=0,new_limits=0,root_task_final="RESERVED_FOR_ROOT",whole_review_complete=False,UPDATE_NOT_STARTED=True))
print("explicit receipts",len(receipts),"reading identities",len(reading))

RJ={
"EXTCP-R020":[
("Opp先/精确hit加成与source412–424相符，默认改用hit0；R4-AN01/04对照完整。",["EXTCP-F025.A01","EXTCP-F025.A02","EXTCP-F025.A05"]),
("18行六格所有108值逐格与447–464一致；空格/重复身份均保留。",["EXTCP-F025.A03"]),
("原始类别两个独立+3条件可到8；随后条件减3，默认不加hitNum；275文字无丢门。",["EXTCP-F025.A04","EXTCP-F025.A05"]),
("无映射/查找普通异常→nil；随后无库→返回；Common无同名→返回。缓存优先不能从磁盘缺失独立推nil。",["EXTCP-F025.A06","EXTCP-F025.A07","EXTCP-F026.A01","EXTCP-F026.A03"]),
("普通Common精确首同名直接核心；招式在ID/库门后包全部shadow。571–575源点重设非任意历史origin快照。",["EXTCP-F026.A02","EXTCP-F026.A03","EXTCP-F026.A04","EXTCP-F026.A06"]),
("完整core到564、saveShadows到405、player到844支持20fps阻塞/正常位置重设；均无ensure，不授中途异常必恢复。",["EXTCP-F026.A05","EXTCP-F026.A06","EXTCP-F075.A01","EXTCP-F075.A05"])
],
"EXTCP-R023":[
("25语义属性对应索引0..26两洞；60为可渲染槽容量，不是每帧实际数组长度；0/1默认双成员。",["EXTCP-F067.A01","EXTCP-F071.A01","EXTCP-F071.A02"]),
("PBAnimTiming五型、80/100/5/nil，getter兼容、frame+1显示；时序编辑确认才添加，取消不改。",["EXTCP-F069.A01","EXTCP-F069.A02","EXTCP-F069.A03","EXTCP-F069.A04","EXTCP-F069.A05","EXTCP-F069.A06"]),
("图层有图先载入再负坐标等设置，无图清位图写纯色；渐变按实际当前bitmap门，普通占位非nil仍图支。",["EXTCP-F072.A03"]),
("所有活动项按序先跑，再同帧所有起始项按序；s<f<=s+d，start只捕获，和340相符。",["EXTCP-F072.A01"]),
("每层一份old、后项重捕全部值，即使只改红；每活动项整RGBA写回；f3为175与普通对照150不同。",["EXTCP-F072.A04"]),
("图形origin插值符号与342给出的显示位置等价；X10/T20/d4在中25末40，纯色不动。",["EXTCP-F072.A03"]),
("独立复核581和setFG完整支，前景100到200中点150；H001原110是误读，未支持新正式修订。",["EXTCP-F072.A05"]),
("d0在活动阶段跳过而start事件仍捕获旧值，能影响同层其它渐变；并非立即写终点。",["EXTCP-F069.A04","EXTCP-F072.A01","EXTCP-F072.A04"]),
("经过时间*20取整；同帧只跳cel/timing，漏start或终点不追补，越界先结束；事件需实际访问，不以d保证完成。",["EXTCP-F075.A01","EXTCP-F075.A02","EXTCP-F075.A03","EXTCP-F075.A05"]),
("构造中心与caller建立线段彼此分列，不逐帧随早槽移动；原128/224锚点样例X200/128，编辑264/192，screen不偏。",["EXTCP-F067.A02","EXTCP-F067.A03","EXTCP-F067.A04","EXTCP-F074.A05","EXTCP-F075.A06","EXTCP-F075.A07","EXTCP-F075.A08"])
],
"EXTCP-R024":[
("完整pbConvertAnimToNewFormat扫描和修正均MAX_SPRITES次即0..59，唯60缺焦点不触发，常规触发也不改60。不要与pbConvertRPGAnimation混同。",["EXTCP-F068.A01","EXTCP-F067.A01","EXTCP-F071.A02"]),
("全Scripts查找RPG转换只有定义与编译器注释引用；fromOther/addAnimation也仅定义。可审定义已全读，未证默认活动调用，不强制未来接口/保证宿主RPG可实例化。",["EXTCP-F068.A01","EXTCP-F068.A02","EXTCP-F068.A03","EXTCP-F068.A04","EXTCP-F068.A05"]),
("完整compile_animations每次空映射，Opp/Move先匹配、前导空白消费、有效注册才映射，后槽覆盖；任何有效条目使changed为真才保存两文件，零有效不写旧盘。",["EXTCP-F025.A01","EXTCP-F070.A03"]),
("两个独立Game_Temp字段、各自loader；编辑退出只清集合，compiler从盘重建但不清两缓存；全局clear二者清空。物理写盘不等于同会话新播放。",["EXTCP-F026.A01","EXTCP-F070.A04"]),
("完整preview play/update只读动画与timing写临时sprite/old值，无save；主循环保存确认独立；正常预览恢复/释放后返回，异常不承诺同样清理。",["EXTCP-F074.A01","EXTCP-F074.A02","EXTCP-F075.A01","EXTCP-F075.A08"])
]}
reverse=[]
for original in X["reverse_current_contribution_objects"]:
    assert len(RJ[original["id"]])==len(original["subassertions"])
    for s,(reason,ids) in zip(original["subassertions"],RJ[original["id"]]):
        reverse.append(dict(id=s["id"],original_complete=s,original_group=original["id"],formal=original["formal"],formal_read_range=original["range"],accepted_meaning_and_reason=reason,source_object_links=ids,source_methods="reading-ledger列完整主定义；R024 additionally使用Compiler1274–1320、MiscPBSData全、AnimEditor_ExportImport89–146、preview451–511/update893–930",status="ACCEPTED_FINITE_STATIC",necessary_unreceived=[],execution="NOT_EXECUTED"))
assert len(reverse)==21
IR={
"EXTCP-IR011":dict(meaning="作者库lookup/player和球公共queue均已直接核实；固定BallMixin通过addBallSprite/addNewSprite建立PictureEx，与PBAnimationPlayerX作者帧/timing分离。球公共入口仅是可调用定义，无默认caller；不能把其名字视作固定球轨道实际统一分派。",producer="完整作者player1–844；Scene390–579；BaseAnimation1–101、对手派出462–524、Scene队列79–101。",scope="只核原接口所述机制区分；其source_assertions笛卡尔索引中的外组F043–050字段仍归02，不在本任务签收/计数。证明该单一机制区别不需要逐个Tone字段，未借接口批准整张球表。"),
"EXTCP-IR013":dict(meaning="WP74共享20fps/cel/timing消费同一个作者集合。编辑主循环确认写时序，预览接同一动画、无pokemon的MiniBattler；战斗按映射加载集合后接同player。字段值与借位图/58粒子/四层、焦点/层次均实际核实。",producer="AnimEditorFunctions1–24/376–677/951–1170；SceneElements451–511/893–930；Compiler1274–1320/MiscPBSData；Player全。",scope="静态可调用、正常输入及资源/宿主请求边界；不签全部作者工具UI/导入导出或编译全生命周期。"),
"EXTCP-IR014":dict(meaning="作者库player只访问当前floor(elapsed*20)帧、无补发循环；playTiming先活动后恰当帧起始，故跳帧不补发。PictureEx通用调度是独立定义，不从同单位20fps把到期事件规则套入本player。",producer="Player767–844及完整playTiming474–586，Scene/core与preview更新入口完整。",scope="对本作者player的反向断言已直接证明。PictureEx全body未在此重新主读，未签其任何超出区别陈述的行为或球字段；保留02/03和引擎owner现有责任。")}
interfaces=[]
for original in X["selected_reverse_interfaces"]:
    ids=[o["id"] for o in X["primary_objects"]]
    interfaces.append(dict(id=original["id"],original_complete=original,**IR[original["id"]],accepted_source_ids=[i for i in original["source_assertions"] if i in ids],foreign_index_ids_without_atom_credit=[i for i in original["source_assertions"] if i not in ids],status="ACCEPTED_FINITE_INTERFACE_STATEMENT",necessary_unreceived=[],execution="NOT_EXECUTED"))
save("interfaces.json",dict(schema="gr8-cp04-interfaces/v1",status="READY_FOR_PARENT_RECEPTION",reverse_current_contribution=reverse,reverse_received=21,selected_reverse_interfaces=interfaces,selected_received=3,IF06=dict(original="目标interfaces.json/IF06完整读，原IF09与continuation IF09同键不合并。",joined_facts=["五时序确认/取消→内存timing→完整playTiming；未确认不新增/不改。","集合从文件/已缓存对象读取与独立move2anim缓存；编译写盘无自动缓存失效。","两个实际consumer：完整Scene动画核心阻塞；完整编辑preview循环，无保存且正常恢复；球公共入口异步另列。","固定20fps、实际访问、不补漏事件；相同帧仍有图层update调用。","共享oldbg/oldfo和整RGBA写、duration0捕获、合法坐标与异常前缀。","前景自身opacity的H001静态独立反证；资源/宿主/物理时钟均未执行。"],status="FINITE_FACTS_JOINED",excluded="完整全局历史、整个compiler/UI/资源provider语义不授通过；其它IF01–05/07–10不在本67组接收。"),necessary_units_unreceived=[],root_task_final="OPEN_RESERVED_FOR_ROOT",UPDATE_NOT_STARTED=True))
save("qualifications.json",dict(schema="gr8-cp04-qualifications/v1",evidence_only_clarifications=[
 dict(ids=["EXTCP-F067.A01"],meaning="27存储位置含9/10洞，25具名语义属性，非27字段"),
 dict(ids=["EXTCP-F068.A01"],meaning="±64只旧position0/2非屏幕支；屏幕3走两线变换"),
 dict(ids=["EXTCP-F068.A05"],meaning="属性分离按clone/新建具体字段，graphic引用不全深复制"),
 dict(ids=["EXTCP-F026.A06"],meaning="恢复x/y并重设origin，不恢复任意旧ox/oy和全部精灵属性"),
 dict(ids=["EXTCP-F027.A02","EXTCP-F074.A03"],meaning="discard仅槽0/1，保留bitmap/角色引用/中心，不等于抹除全部参与资源"),
 dict(ids=["EXTCP-F073.A03"],meaning="个体全图仅合法pattern -1/-2；其它负数不获同义"),
 dict(ids=["EXTCP-F075.A02"],meaning="同帧不重做cel/timing；加载检查/图层update仍先发生")],H001=dict(original_complete=X["original_proposal_full"]["retracted_hypotheses"][0],independent_receiver=os.environ.get("CODEX_THREAD_ID"),decision="NO_REQUIRED_REVISION_SUPPORTED_BY_THIS_HYPOTHESIS",complete_source="player474–586（含558–583及581），WP74全文（338–350重点）",counterexample="有效图形背景opacity20/前景100、前景从s1以d2到200、逐帧访问且无覆盖：前景在f2=150；f1捕获100，f3=200。前景无图时捕纯色自身旧值。",control="无前景渐变保持100；持续0只捕获；另一层起始不重写前景oldfo。",execution="NOT_EXECUTED",root_decision="仍由主审最终登记；本凭据是真实非提出者独立复核"),CP002=dict(original_complete=X["original_proposal_full"],disposition="完整候选/撤回/保留ID已读；倒下固定轨道归03/06及主审ELR，04不新增required/optional/policy决定，也不把派发材料当已收反证。",status="OUTSIDE_THIS_BOUNDED_ADJUDICATION_KEEP_PARENT_OPEN"),battler_supplement=dict(complete_input_pointers=list(X["full_battler_supplement"]),status="FULL_QUALIFIED_TEXT_READ_NOT_ADOPTED_AS_SOURCE_PROOF_FOR_67",meaning="八条原话与后继强制澄清均保留；raw add/空子类、Exp/EV例外、wild初图/sendout分路、refresh非纯读、HP先写后通知不继承过强断言。这里不重收八事实整个源码/外域formal，主责06。"),history="第七轮27未重开；无旧PASS继承。本次实际源/条款证据独立，RPG死定义不自动变未来API。",limits=[dict(id="L02/L03/L11/L14(existing)",scope="实际图形/音频、System.uptime精度、宿主输入、异常展示/恢复与插件覆盖未运行/未证明；材料中无完整Graphics/Audio和作者动画数据库。",execution="NOT_EXECUTED")],new_required=0,new_optional=0,new_policy=0,new_limits=0,UPDATE_NOT_STARTED=True))
print("reverse",len(reverse),"interfaces",len(interfaces))
