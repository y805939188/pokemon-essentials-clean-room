# R6-B 本轮语义阅读记录（审计分析，不是正式规格）

固定输入 main 8ea169f / workspace tree 6ab3429 / formal tree 1046fbb（131）/ R 8c5911 / tree 7589c8。实际模型、effort、tier、speed、UUID均 UNVERIFIED。原程序、Ruby、IL、DLL、宿主、Demo执行均0。本记录的数学和分支结论均为本轮静态阅读或人工推导。

## 兼容明文三单元

全部3448行已连续阅读：BIN-0079 1–500、501–968；BIN-0080 1–500、501–1004；BIN-0081 1–500、501–1000、1001–1476。表中路径仅审计定位，不能作为未来对象组织要求。三个模块拥有同名声明，不应叠加成同一活动环境。

BIN-0079是带四层地图数据、region encounter、BaseItem/Feature、Damage/Effect和Vehicle/Terms的兼容定义；BIN-0080是三层地图、Area、六维旧参数、独立装备字段、Audio子类的另一套定义；BIN-0081是三层XP数据与Cache/Sprite/Weather的定义。当前Game.ini缺失、mkxp.json未设rgssVersion，原生选择逻辑未审明；不能仅按出现顺序推出当前选择哪一套。Ruby对象存档加载、构造函数默认和访问器返回三者分开：读档对象不必调用构造默认。

- BIN-0079 Map 3–65：输入宽高保留；默认tileset1、scroll0、遭遇步30、4层Table、空events与encounter列表，音乐空名/默认100，环境声空名/80，false flags与0 parallax移动。初始化的battleback_floor/wall和暴露的battleback1/2不是同名字段；新实例读取后两者无初始化值，不能自动修正。Encounter 4–13 默认troop1/weight10/空regions；MapInfo 67–82空名/父0/序0/折叠false/scroll0。
- 0079 Event 84–174：六个有效性标志false；switch/item/actor ID1、variable0、自开关A；graphic tile0/空character/index0/方向2/pattern0；page move0/speed3/frequency3、walktrue其它false、priority0/trigger0、终止命令列表；坐标来自入参，ID0、空名、单页。EventCommand 176–185保留code/indent/parameters；MoveRoute 187–198 repeattrue/skippablefalse/waitfalse/单终止；MoveCommand 200–207保留code/parameters。
- 0079 BaseItem 209–235：ID0、空name/description/note、icon0、features空；Feature保留code/data/value。Actor 237–259继承公共字段、nickname空/class1/levels1..99、空character/face及index0、5个装备0。Class 261–304包含level1/skill1/note空的Learning；8×100参数表只填1..99、四EXP参数30/20/30/30、空learnings以及7个预置feature；等级经验输出按所列4参数计算并round，不对负级/acc_b0补保护。
- 0079 UsableItem 306–421：scope/occasion/speed/tp/hit/animation为0，success100/repeats1；Damage默认type0/element0/formula0/variance20/criticalfalse，type集合分别决定HP/MP/恢复/吸取，恢复符号负；动态formula以a/b/v上下文求值后取非负再乘符号，可局部捕获错误回0，不保证任意表达式安全/无副作用。Effect四字段保留。scope1..6敌、7..11友、9/10倒下友、11自身、1/3/7/9/11单、3..6随机且目标数scope−2、2/8/10全、1/7/9需选择；occasion0/1战斗、0/2菜单；hit0/1/2分别certain/physical/magical，未知值各判断false。
- 0079 Skill 423–442：scope1/stype1/cost0/空双message/武器要求0。Item 444–458：scope7/itype1/price0/consumabletrue；key predicate只等2。Equip 460–470 price/etype0、8个参数0。Weapon/Armor 472–498各添feature，武器wtype0/animation0，护甲atype0/etype1；performance分别额外双计攻击相关或防御相关两项加全参数和，不是战斗伤害公式。
- 0079 Enemy 500–547：Drop kind0/data1/denominator1；Action skill1/condition0/params0/rating5；默认参数100/0/其余10、exp/gold0、3个独立Drop与1Action及3features。State 549–583 restriction0/priority50、两个turn1、chance100/steps100、所有移除标志false、空4message。Troop 585–649：members空/单Page；member敌1/坐标0/hiddenfalse；condition5flagsfalse/turn0/index0/HP50/actor1/switch1；page span0与终止表。
- 0079 Animation 651–701：Frame cellmax0、0×0Table；Timing frame0/SE空80/flashscope0/whiteRGBA255/duration5；动画双图名空/hue0、position1/frame1/单Frame/无timings；screen判断position3。Tileset703–721：mode1/9空图名/8192flags，0项0x10，两段指定区间0x0f，note空。CommonEvent723–742 ID0/空name/trigger0/switch1/终止表，autorun仅1/parallel仅2。
- 0079 System 744–870：Vehicle空character/index0、空BGM、起图/坐标0；Terms各8/8/5/23空串；TestBattler actor1/level1/5equip0。title空/version0/Japanese true、party[1]、nil首项的元素/技能/装备/开关/变量名表；3独立vehicles；标题图空、8个opt flags逐项（drawtitle/followers/displaytp真，其余假）、中性色调、4独立音乐对象、24独立SE、测试列表空/测试troop1/startmap1/坐标0/Terms/背景与battler空/hue0/editmap1。
- 0079 Audio 872–968：统一name空/volume100/pitch100不钳制。BGM/BGS空名stop并清last；非空拼分类路径、传pos、克隆self为last；replay读pos（构造未赋）；last查询会把宿主当前pos写入last后返回同last。stop/fade请求后清last，不表示声音已停；ME空名stop否则play，SE空名无请求，二者无last；SE只有stop。这些字段和分派的效果仍取决Audio外部能力。

BIN-0080的所有数据访问器均读写对应字段，未见alias声明；构造不校验宽高、ID、阵列长度、注册存在性或资源存在。

- 0080 Map 2–41：三层/无tileset字段、scroll0、emptyAudio BGM默认100/BGS80、dashingfalse、encounter空/step30、空parallax与全false/offset0。MapInfo43–58同0079。Area60–75 ID0/空name/map0/0Rect/空encounter/order0。Event77–167与0079同条件和graphic/index形式、priority0；命令169–201保留入参；route含waitfalse。
- 0080 Actor202–258 ID0/name空/class1/level1/EXP25/35，空character/face且index0，6×100表1..99已读其分段增长，单weapon与4armor0，6个特性标志false。Class259–291 ID0/name空/position0、weapon/armor空、两1长度rank表、learning空、skill-name-validfalse/空名；Learning level1/skill1。
- 0080 BaseItem293–307公共ID/name/icon/description/note。Usable308–384所有数值0（variance20）、四damage flagsfalse、三集合空。scope判别与0079差异：one含4、random仅4/5/6、dual仅3、two仅5/three仅6、selection含3；其余敌友/全/occasion相同。Skill385–399 scope1/cost0/hit100/双空message。Item400–422 scope7/price0/consumabletrue、8恢复/能力量0。
- 0080 Weapon423–454 ID等继承、animation/price0/hit95、atk/def/spi/agi0、4标志false、两个集合空。Armor455–486 kind/price/eva及4stats0、4标志false/两集合空。Enemy487–572 Drop kind0/3IDs1/denominator1；Action kind/basic0/skill1/condition0/两个params0/rating5，skill?仅kind1；主体6stats10/hit95/eva5/expgold0/2Drop/levitatecriticalfalse/1长度两rank表/单Action/note空。
- 0080 Troop573–640 member敌1/坐标0/hiddenfalse/immortalfalse；Page条件同0079/span0/终止表；主体pages构造用BattleEventPage名字而该文本未定义此常量，构造成功需另有外部定义；不得当已活动游戏失败。State641–693 priority5/四rates100、6flagsfalse而battle_onlytrue、hold/auto0、4message空、两sets空/note空。
- 0080 Animation694–742双图型/Timing空Audio80/flash0白255 duration5、无Timing.condition字段；Frame默认同0079。CommonEvent743–757无trigger谓词。System758–918含Vehicle/完整35个独立空Terms字段/TestBattler 5装备，passages8192，3车辆、4专用音乐类、20个AudioFile声效、其它ID/起点与空名表已逐字段读；不含0079全部opt flags。Audio919–1004无pos/replay/clone：BGM/BGS last指向self，因此后续修改self也改last；stop/fade清last；ME/SE行为同0079而不读pos。

- 0081 Cache2–79：path字符串键复用未disposed对象，空filename建32×32，hue非0以path/hue键clone再变色；12分类路径已读；tile额外filename/tileID/hue键、固定32格/8列、ID384基准；clear只是换空cache并GC，不逐对象dispose。此load_bitmap/tile在散文件被重新定义（RPG_Cache38–86），不能把旧体共享/clone结论无条件当当前输出。
- 0081 Sprite81–460：whiten/appear/escape/collapse分别16/16/32/48步，互清各自其它3计时；damage先清旧对象，文字160×48、数值绝对值、负数绿色/其它白色、critical加独立标题，实例定位于父坐标并40步；两种动画引用计数共享位图、每个最多16cell，屏幕动画同帧去重、循环同对象不重启。dispose_damage与两动画族先清资源再清引用；blink32步alpha折返；effect只含6种计时而不含blink/loop。update顺序super→四effect→damage跳动/透明→偶帧普通/循环→blink→清同帧动画登记。动画cell pattern −1/空/无sprite隐藏，否则192格5列，screen/viewport定位与相对父定位分开，offset/zoom/angle/mirror/opacity乘父/255/blend逐字段处理；Timing.condition0全、1hit、2miss，SE非空播放，flash scope1本体/2viewport/3隐藏，duration×2。x/y改变增量同步各cell然后super。散文件RPG_Sprite覆盖initialize/update/animation/effect/x/y等，活动消费者为SpriteAnimation；不能把旧时间表替代当前WP16。
- 0081 Weather462–582：3种生成小位图/40实例、数值type0/max0/原点0；type=max setter按1..40索引而初始化数组0..39，所以首sprite不参与该循环、40为空；update1..max，max夹0..40，type0无update；雨/暴风/雪各位移与透明损失、阈值/范围触发随机重置。散文件Weather全部活动方法已覆盖：symbol天气、60粒子、真实time delta；0079/0080没有这个可读Weather定义，不能混合。
- 0081 数据584–1476：Map/MapInfo/Event/MoveRoute/MoveCommand/EventCommand/Actor/Class/Skill/Item/Weapon/Armor/Enemy/Troop/State/Animation/Tileset/CommonEvent/System/AudioFile全部默认字段与访问器已读。XP的Event只有4条件flags（无item/actor）、Graphic hue/opacity255/blend0而无index、Page always_on_topfalse而无priority/wait字段；6×100 Actor表、level1..99/EXP30/30、5装备fix false；技能occasion1/int100/mdef100/variance15，其它值和集合分别0/空；Item occasion0/hit100/consumabletrue、恢复/防御量0；Weapons/Armor独立物理/魔法防御与4加值、guard集合；Enemy HP/SP500/四stats50/atk与两def100、exp/gold0、treasure100；State各rates100/battle_onlytrue/其余标志false与量0。Troop pages使用RPG::BattleEventPage而当前块未定义，是条件依赖；Animation单图型、Timing.condition0；Tileset7autotiles/3表384/priorities[0]=5、fog64/zoom200、空资源；System Words20空串、12独立SE80、4音乐100、party[1]/nil首项名表/startmap1/坐标0/editmap1；AudioFile三字段默认100/100，不含BGM等子类。其actual消费者及数据反序列化属于WP13/75等，不能推出所有旧数据库战斗概念必修。

## animmaker 全15方法静态审查

方法1–6：Frame保存filename和输入rect；Animation保存filename并建空Frames；各getter直接返回字段，无clone/验证。方法7缓存Dispose逐weakrefs.Values读取Target，只有仍是Image才Dispose；enumerator有finally，Clear在循环正常结束后，Image.Dispose若失败不保证Clear。方法8创建字典。方法9以精确filename键寻找WeakReference且Target为Image即复用；无存活目标重新Image.FromFile；非alpha PixelFormat才转Bitmap，以(0,0)像素作透明色、释放原Image；alpha图直接保留；写WeakReference；加载/像素/释放失败无本地catch。

方法10 ParseXmlInt只捕获FormatException，提示属性/文件/行号并Environment.Exit(1)；方法11虽名positive但只拒负数，0通过，同样只catch FormatException，不吞Overflow/ArgumentNull等不同类别。该signed方法10无调用者（其余14方法及调用表新审）。方法12先Exists，false提示Exit1；XmlTextReader构造只catch IOException并Exit1；是否构造/读取依赖成功不作为静态完成事实。方法13首次ReadToDescendant，后续ReadToNextSibling，索引仅选首次/非首次，非一类xml全树扫描。

方法14：先建reader与总列表；root非animations返回空（finally Close）；每animation取name直接创建并先追加；每pattern取filename。x缺失或空串创建全零rect，y/width/height未读取；x非空则四属性逐个ParseXmlPositiveInt，故非负允许0，缺剩余属性没有工具自己的默认，96×96没有代码守卫。全部XML读完后才Main开始输出。IOException在LoadAnimationData被捕获，显示后可返回已经聚合的前缀列表；XmlException分支format文本使用{2}却只提供两个替换参数，不能声称稳定显示并成功返回前缀；外围finally仍请求Close，Close自身若失败也无成功保证。环境Exit不是UI Cancel，程序无独立取消分支。

方法15：无参显示help及XML示例后ReadLine并返回；有参仅用args[0]（额外参未消费）。LoadAnimationData正常返回后建缓存，逐animation枚举。每张表宽960；n=0高192，否则高192×ceil(n/5)。空位图构造与Graphics.FromImage→InterpolationMode数值5→逐Frame。filename不存在提示且跳过绘制，仍保留该frame编号，所以后续不前移补洞；存在才LoadImage。rect.IsEmpty才改整图。第i格原点(192(i mod5),192 floor(i/5))，目标矩形左上加(96−w,96−h)，大小(2w,2h)，源矩形保持x/y/w/h，DrawImage末参数数值2；不把外部Graphics语义、像素插值、Image.Save输出编码当已执行。单animation循环完马上Save(filename)，随后finally依次Graphics/Bitmap Dispose；全局enumerator/缓存Dispose有finally。第2张失败保留已成功第1张，当前失败Save能否截断/写部分由外部库决定；没有工具整体回滚。提示的96上限是文档陈述，不是此代码输入门。WP74§18本来限定doc scope，所以应先作为可选新静态能力，不升级既有正文矛盾或未来必修。

## extendtext 有限原生静态工作体

原PE32入口VA401219，新objdump .text字节读完；callback真正入口40129c需重新起始解码，原线性解码40129b对齐错误已识别并修正。 .idata被objdump误当可执行反汇编，实际是导入结构，不计程序语义PASS。

17导入：Kernel32 GetLastError/CloseHandle/RtlUnwind/CreateMutexA/Sleep；User32 GetWindowTextA/FindWindowA/GetDlgItem/GetClassNameA/FindWindowExA/EnumWindows/SetWindowPos；CRT __GetMainArgs/exit/raise/signal/strstr。CRT/SEH启动/展开、signal与exit皆静态路径，不执行。

工作主函数4013c2→用固定名字CreateMutexA(securityAttributes=null,initialOwner=false)。handle0产生−1；已有mutex错误183时Close并返回0；新handle返回handle。主函数只拒0，故mutex创建失败返回−1仍可能进入工作循环，不能保证单实例或成功持锁。正常结束清理只close非0/非−1句柄。callback枚举窗，GetClassNameA(...256)后strstr(Afx:)；命中再GetWindowTextA(...256)并strstr(RPG Maker XP)；两者命中才设置found=1、回false停止枚举；未命中继续。读取结果未检查，不能保证每缓冲都得到有效文本。

先检查宿主窗口found，再四类对话框的FindWindowA(#32770,title)：Script请求840×240且EDIT800×176；Show Text840×144/EDIT800×72；Comment840×164/EDIT800×92；Batch Text Entry840×444/EDIT800×372，还GetDlgItem1/2分别请求坐标(25,392)/(150,392)。尺寸请求flags0x16、位置请求flags0x15；分别是API参数，SetWindowPos返回值均未检查。子控件找不到跳过该子请求，父成功与否不能推出子成功。每一轮末Sleep(150)，再枚举RPG Maker XP窗；无匹配即close mutex并返回0→CRT exit。150是请求的毫秒睡眠，不保证精确总轮耗时、实际窗口修改、语言/版本兼容或成功退出效果。

## 根作者工具与Formal接合

scripts_combine/extract均7380bytes，1–181同字节（SHA256 5c407c...），只有182/183两行调用/注释方向互换。两文件均本轮全文阅读后才用同定义矩阵关联；旧PASS未参与。守卫提取<10/合并>10，清树删所有普通文件与所有子目录（不仅rb），提取解压去全部CR，两层计数/文件最后999/目录末两节999、结构判别与非空script写出分开；先全部散文件前缀再备份再loader。合并是本层rb先字母序后子目录递归、隐藏目录排除/隐藏普通rb纳入；根子目录前18等号、第1层前空节；ID随机，旧归档仅数量门，聚合全部成功才覆盖，无备份；filename按字节重释Unicode/实体反转/无underscore归unnamed；标题9字符转义全读。文件/目录/备份/loader失败均无工具本地catch或全局rollback。WP75§12与CV-M26/27/B20-C024已覆盖这些核心方向，未发现方向错误。

townmapgen实际414行（wc newline413），extendtext.txt实际4行（wc newline3），均已补尾。HTML所有事件/helpers全文读，地区图480×320/格字段文本默认16/无校验，鼠标边界后floor，标记相对两BMP；load先清数组逐条赋值，badline提示后访问null未保护，前缀保留；CSV只修剪剩余/引号入口注释；gen未转义原始值/CRLF/仅textarea/需手工节标题；Save只在选择存在时提交数组，Cancel只重载当前坐标字段然后清选择。注意btnSave.enabled状态：MapClick置false(disabled)，Save自身置true；Cancel/Refresh/Load清选择但不disable该按钮。当前WP75§13的“点选才启用”可读为初次启用条件，不能直接裁定其承诺Cancel必禁用；即使仍enabled，无选择时Save业务分支不进，不发生业务保存。暂作边界记录而非缺陷。

WP75 438行和demo测试327行全文新读；WP75事件编译/文件名更新非根工具源仍需消费者接合，不能单凭读规格当source通过。对应root/K主合同、源Compiler生命周期及FileMixins的关系在矩阵内各归属与证据分开。WP74 435–472仅审本工具边界，不代表其编辑器整篇语义审过。主矩阵不会把其它DG/CE/WE/GN/DM条款在本任务的阅读提升成全域source认证。
