"""Generate J's bounded, independent junction-review artifacts. No reference execution."""
import json,pathlib,datetime,collections
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[4]
SHARED=HERE.parents[1]
SRC=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B='1f36475d22120a0d1175967d5b17d71fe8311d88'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
launch=json.loads((SHARED/'tasks/J-launch.json').read_text())
nav=json.loads((SHARED/'evidence/junction-navigation.json').read_text())
legacy=json.loads((SHARED/'evidence/legacy-projection-links.json').read_text())
formal=json.loads((ROOT/'delivery/2026-10-12/formal-identities.json').read_text())['records']
formal_paths={x['path'] for x in formal}

def dump(name,obj):
 (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def anchor(kind,name,ranges,fact,section=None):
 root=SRC if kind=='source' else ROOT/'deliverables/final-specification-set'
 matches=[root/"PBS"/name] if kind=="source" and name.endswith(".txt") and (root/"PBS"/name).is_file() else list(root.rglob(name))
 if len(matches)!=1: raise ValueError((kind,name,len(matches)))
 p=matches[0]
 d={'path':str(p.relative_to(SRC if kind=='source' else ROOT)),'commit':R if kind=='source' else B,'line_ranges':ranges,'fact':fact}
 if section:d['section_or_test_ids']=section
 return d
def S(name,ranges,fact):return anchor('source',name,ranges,fact)
def P(name,ranges,fact,section=None):return anchor('spec',name,ranges,fact,section)
records=[]
def add(n,title,status,**kw):
 r={'id':f'GR4-J{n:02d}','title':title,'review_kind':'fresh_bounded_independent_source_to_spec_review','status':status,
    'formal_baseline':B,'reference_baseline':R,'evidence_level':['SOURCE_STATIC','SPEC_STATIC'],
    'execution_status':'NOT_EXECUTED','material_availability':{'scripts_and_selected_PBS':'READABLE; identity/readiness reused from baseline.json','graphics_audio_maps_complete_demo':'UNAVAILABLE in fixed reference; root BMP/fonts/translation material presence is not runtime evidence'},
    'status_scope':'仅本记录具名分支的B条款与R源链关系；supported不表示整模块、历史整ID或运行PASS。','new_finding_ids':[],**kw}
 records.append(r)

add(1,'翻译/PBS → 登记/导入 → 电话运行消息','partial',
 primary_owner='WP08 本地化；电话PBS身份子合同由WP03单独主责，WP04与WP63引用',
 producers=['phone.txt重复属性候选与联系人/Default节','Text_语言_core/game文本域导入'],
 state_writes=['电话记录登记；终检登记PHONE_MESSAGES候选','译文按规范键或索引逐项合入；电话生成再战请求时旗标1→2'],
 consumers=['当前/起始版本/default电话消息选择','当前语言game→core→原文查找','电话分段与姓名/物种/地图替换后交消息窗口'],
 preconditions=['合法电话身份/可读输入；依赖数据和宿主调用正常','本次无扩展覆写；联系人可进入生成/播放；语言加载按独立阶段成立'],
 configuration=['PhoneMessage schema重复属性候选；PHONE_MESSAGES域22','LANGUAGES及PHONE_REMATCHES配置','电话显示姓名与数据身份不同；翻译导入和PBS编译是两种输入格式'],
 reviewed=['沿通用编译实际PhoneMessage存在性覆写、登记、终检到电话消费者','同域译文后键覆盖/重复节逐项合并与运行回退','普通占位插入与后续消息窗口分层；非字面特殊参数只关联M01既有问题'],
 not_reviewed=['全部文本域/所有翻译文件往返','跨文件次序所有组合、实际电话公共事件与可达性','宿主占位特殊字符执行未复跑；不沿用M01隔离回执为J运行证据'],
 boundaries={'normal':'合法单默认集经编译终检形成候选；联系人两版本均缺时选默认候选，再查当前语言，最终不保证显示原候选字面。',
 'failure':'联系人同三元重复在第二次登记前拒绝，前项内存保留；文本完整导入先打开输出，解析失败不能保证旧产物恢复；显示失败可发生在再战旗标已推进之后。',
 'cancellation':'作者导入的外部菜单取消未重新审；运行生成没有撤销旗标的局部事务；本链不把UI退出解释为恢复译文或电话状态。',
 'repetition':'两个Default节A/B后节整条替换（已正确承接）；同一翻译域后节只覆盖同键并留前节独有项（M01-001），这两种合并不能统一。',
 'ordering':'PBS候选登记→终检收集；翻译导入与语言加载另行发生；运行先选候选再本地化→生成期旗标提交→播放。'},
 vectors=[{'id':'GR4-J01-V1','input':'同一合法电话输入依序Default Intro A、B；联系人版本均缺','expected':'候选仅B；显示再经语言表。与KR14/KL36一致。','status':'NOT_EXECUTED'},
 {'id':'GR4-J01-V2','input':'同一翻译哈希域前节K1=A、K2=B，后节K1=C','expected':'K1=C、K2=B；为M01-001的同根交界，不另立问题。','status':'NOT_EXECUTED'}],
 source_anchors=[S('002_Compiler_CompilePBS.rb',[[4,68],[1237,1268]],'通用登记前探测、Phone专用身份规范化、终检文本收集'),S('021_PhoneMessage.rb',[[15,26],[36,69],[72,88]],'联系人三元查询与Default探测区别'),S('001_GameData.rb',[[78,85]],'直接登记后项替换'),S('003_Intl_Messages.rb',[[376,384],[437,489],[511,528],[589,631],[774,823]],'译文导入、加载、回退与占位阶段'),S('004_Item_Phone.rb',[[414,503]],'实际选择/状态提交/播放消费者'),S('phone.txt',[[3,13]],'默认电话重复属性候选存在')],
 spec_anchors=[P('wp03-content-identity-and-schema.md',[[121,134]],'Default与联系人重复规则已准确','§5.2'),P('wp04-pbs-lifecycle.md',[[82,92]],'通用编译消费者与Default例外'),P('wp08-localization.md',[[27,32],[44,67],[98,119]],'运行回退正确；本轮既有译文合并与占位问题'),P('wp63-pokegear-map-music-and-phone.md',[[140,145]],'电话候选/再战写入/播放'),P('generic-kernel-wp02-03-04.md',[[33,35],[76,76]],'反证排除新Default问题','KR14–16 / KL36')],
 historical_junction_ids=['G1-4','G1-5','G7-4','N01'],existing_finding_ids=['GR4-M01-001','GR4-M01-002'],
 conclusion='Default重复候选经全131同义检索被现有准确条款反证，保留GR3 CLOSED；译文合并与普通占位问题仅关联M01，不新增J根因。')

add(2,'保存/恢复游戏变量 → 墙钟计时查询 → 地图刷新','partial',
 primary_owner='WP06变量计时语义；WP09持久单元、WP11/13刷新为消费者投影',
 producers=['秒数或天数设置入口','存档变量单元恢复'],state_writes=['变量槽存入开始墙钟与期限','查询不成立清变量为0；设置/清零均直接刷新地图'],
 consumers=['墙钟有效查询','地图事件/公共事件刷新','正常保存再取变量整体、继续加载同一持久单元'],
 preconditions=['有效游戏变量槽和时间记录，合法数字期限；当前地图刷新依赖正常','继续加载值类型有效；不添加离线自动触发或默认调用者假设'],
 configuration=['合法变量范围；秒数负值夹0','天数负值夹0；t为设置时Unix秒，d为天数，期限=(t mod 86400)+86400d−t','游戏时间游玩锚点与墙钟记录不同'],
 reviewed=['变量生产、破坏性查询、保存取值与恢复绑定','查询为假后的地图即时刷新；变量未加载/非法边界仅按已读守卫'],
 not_reviewed=['任意损坏数组、所有变量编号边缘和刷新中的重入','实际旧档迁移/保存IO/运行计时','没有默认脚本调用者证据，不猜Demo事件使用'],
 boundaries={'normal':'正期限且经过时间严格大于期限时返回真、保留记录；保存/继续可保留该变量数据。','failure':'未到、恰到或非正期限均假并清0；设置天数不是通常的日历倒计时；保存类型/IO失败与计时查询失败分开。','cancellation':'设置/查询无取消接口；保存UI拒绝不调用保存，也不撤销此前计时查询清0。','repetition':'成功查询重复可保持真；一次未到期查询清0后再查仍假，不能把它当无副作用轮询。','ordering':'变量写入先于地图刷新；继续先恢复变量再恢复地图。查询清0后下一次成功保存会记录0；并非读档自动清计时。'},
 vectors=[{'id':'GR4-J02-V1','input':'槽v=[t0,10]；t=t0+10，正常查询及刷新','expected':'false、槽0；随后t0+11再次查询仍false。独立初态[t0,10]在t0+11查询则true且保留。','status':'NOT_EXECUTED'}],
 source_anchors=[S('001_Utilities.rb',[[157,191]],'变量计时三入口及写后刷新'),S('003_Game_Variables.rb',[[12,24]],'槽读写与默认0'),S('004_Game_SaveValues.rb',[[42,47]],'变量整体保存/恢复'),S('002_SaveData_Value.rb',[[239,248],[271,282]],'未加载恢复与保存汇编'),S('001_StartGame.rb',[[63,103],[111,124]],'继续/地图恢复与保存失败'),S('004_Game_Map.rb',[[429,445]],'事件/公共事件刷新消费者')],
 spec_anchors=[P('wp06-time-random-steps-stats.md',[[25,50]],'时间来源已分层；变量计时缺口关联M02-001'),P('wp09-save-startup-continue.md',[[59,81],[92,96],[107,115]],'变量持久目录、地图恢复与保存失败')],
 historical_junction_ids=['G2-1','G2-2','G2-6','G9-6','CHAIN-2','N03','N05'],existing_finding_ids=['GR4-M02-001'],
 conclusion='保存本身不增强计时记录的有效性；M02-001为唯一相关根因。M02-003依用户裁决不需修订，与本链无新增关系。')

add(3,'冲浪状态/临时基点 → 转移 → 精灵定位/解释器等待','partial',
 primary_owner='WP12载具状态；WP59场地动作提交；WP11/16/13分别消费转移/显示/等待',
 producers=['上水或成功上岸前跳','显式转移的取消游泳参数'],state_writes=['先冲浪/统计/底座再尝试上水前跳','上岸跳成功才写底座及ending标志','仅合格玩家步后通知清底座，ending为真才继续清结束状态'],consumers=['Scene_Map转移与玩家moveto/载具外观覆写','SurfBase以残留基点定位','解释器见ending_surf提前等待'],
 preconditions=['有效地图/玩家/载具配置；明确前跳失败或无完成步后通知的时段','同图保留游泳转移与默认取消游泳转移分列；无额外插件清理'],
 configuration=['转移cancel_swimming真/假','玩家移动外观配置、面对水域与落点通行','地图场景/玩家事件/底座存在三道清理门'],
 reviewed=['两个临时字段全脚本读写检索','实际转移、玩家moveto/外观覆写及两个下游消费者'],not_reviewed=['真实地图落点和屏幕位置','所有场地招式/边缘切图组合','无限等待或宿主自动恢复不作结论'],
 boundaries={'normal':'上/下水动作正常到合格步后通知才收尾；清理后精灵回跟随位置，结束冲浪等待门解除。','failure':'上水前跳拒绝时前缀已提交；转移及取消载具自身不清两个临时字段；取消游泳只可能隐藏底座显示，不等于清字段。','cancellation':'确认上水前拒绝不进入提交；提交后的转移中断不是事务撤销。','repetition':'残留非空时显示反复消费同一基点；ending真会持续阻解释器，直到相应清理发生；不推一定永远残留。','ordering':'冲浪置位/统计→基点→前跳；转移重建显示不是步后通知；解释器等待门在通常命令处理前。'},
 vectors=[{'id':'GR4-J03-V1','input':'上水写入后前跳失败；无合格步后通知；同图显式保游泳转移','expected':'临时基点无转移清零保证；重新显示仍读取基点。正常合格步后通知为独立清理对照。','status':'NOT_EXECUTED'}],
 source_anchors=[S('004_Overworld_FieldMoves.rb',[[692,751]],'上水提交/上岸标志/步后清理'),S('002_Scene_Map.rb',[[72,101],[121,133],[165,175]],'转移及默认201消费不清临时字段'),S('008_Game_Player.rb',[[64,100],[262,266],[575,592]],'实际覆写不补清理'),S('005_Sprite_SurfBase.rb',[[44,79]],'残留基点影响定位'),S('003_Interpreter.rb',[[103,123]],'结束标志阻解释器')],
 spec_anchors=[P('wp12-terrain-movement-vehicles.md',[[164,173]],'提交与步后门准确'),P('wp59-world-time-weather-field-moves.md',[[295,301]],'转移重置保证与实际链不符','§7 L296')],
 historical_junction_ids=['G2-3','G9-5','CHAIN-8'],existing_finding_ids=['GR4-M03-002'],conclusion='同一M03根因影响状态、显示和命令进度，不能分别计三个新问题。')

add(4,'动态形态 → 能力重算/图鉴 → 资源请求（含孵化）','partial',
 primary_owner='WP21动态求值，WP18提交副作用；WP15资源与WP35/67-B孵化为消费者',
 producers=['个体动态形态读取','DEERLING季节和FURFROU到期处理器'],state_writes=['变化时存储形态、特性缓存、能力与图鉴见过记录','孵化核心字段先写，演出读取后才通常拥有/见过蛋'],consumers=['物种内容读简化形态','按个体前/背精灵和图标读取动态形态','孵化蛋图/裂纹请求的调用实参先取动态形态'],
 preconditions=['无forced形态，非战斗/非储存才求动态；资源与消息必须实际到达查询点','DEERLING普通非Shadow、存储0、剩余1步、2月；媒体/玩家/图鉴有效，跳过命名、无额外改写'],
 configuration=['季节=(月份−1) mod 4','FURFROU缺时间戳或严格超5天回0','DEERLING命名形态数据与FURFROU剪毛形态存在；资产缺失'],
 reviewed=['普通form/简化form、完整提交、数值重算与图鉴映射','按个体取图及参数式取图的调用位置区别','孵化步后→核心→蛋图/裂纹→揭示→拥有/见过蛋完整具名链'],
 not_reviewed=['所有物种动态处理器','真实图像存在/像素、孵化演出或原函数执行','GIR-FD82-A053其余旧贡献与全部229/341控制'],
 boundaries={'normal':'到期FURFROU按个体取图先回0及提交，再请求图像；DEERLING2月在孵化早期取图实参求值时0→1。','failure':'形态变化可先于资源解析/显示失败发生，没有资源失败即回滚形态的保证；是否到达查询受更早资源/宿主阶段限制。','cancellation':'拒绝孵化命名不撤销此前形态/核心提交；不虚构可取消孵化。','repetition':'相同动态结果再次读取不再触发形态变更提交；forced或battle/storage门直接返回；核心直接孵化重复不是防重入口。','ordering':'计数先归0→孵化核心写入→调用者取form→完整提交→资源函数；参数式资源函数不自行求值，不代表调用者未求值。'},
 vectors=[{'id':'GR4-J04-V1','input':'EG-20完整前提：DEERLING存储0、月2、steps1；无forced/battle/storage','expected':'steps0，核心提交；蛋图实参取form得1，存储1/重算/登记已见；通常拥有及见过蛋随后发生。月1或forced为独立对照。','status':'NOT_EXECUTED'},
 {'id':'GR4-J04-V2','input':'FURFROU形态1，缺时间戳，按个体取图；独立显式形态参数1取图','expected':'前者先提交0再取图；后者本层仅消费参数，不求个体动态形态。若调用者已动态求值则另论。','status':'NOT_EXECUTED'}],
 source_anchors=[S('001_Pokemon.rb',[[113,115],[147,184],[1099,1127]],'简化内容读取与动态提交/重算'),S('001_FormHandlers.rb',[[322,328],[422,431]],'季节与五天形态'),S('003_Overworld_Time.rb',[[201,203]],'季节公式'),S('009_Species_files.rb',[[37,68],[92,109],[118,139]],'显式参数与个体资源请求分层'),S('003_Pokemon_Sprites.rb',[[49,69],[124,138]],'真实精灵/图标调用'),S('003_UI_EggHatching.rb',[[13,40],[84,129],[212,221],[252,267]],'孵化完整消费者时序'),S('005_Player_Pokedex.rb',[[195,218]],'形态登记使用简化物种数据并映射展示形态'),S('pokemon_forms.txt',[[1397,1408],[1635,1661]],'具名形态数据')],
 spec_anchors=[P('wp18-creature-identity-species-ownership.md',[[140,153]],'L151图像泛称是M04既有矛盾'),P('wp35-eggs-and-hatching.md',[[93,117],[163,165]],'孵化合同已准确，不得倒退'),P('creature-rpg-wp35-36-57-64-68.md',[[23,30]],'限定旧投影与反向对照','EG-13 / EG-20')],
 historical_junction_ids=['G4-8','G5-4','CHAIN-5','N08'],existing_finding_ids=['GR4-M04-001'],
 legacy_control_projection={'id':'GIR-FD82-A053','status':'supported','scope':'仅DEERLING存储0、2月→1的孵化演出/资源消费者投影；旧完整scope保留。','revision_guard':'M04可删除WP18“图像均用简化读取”泛称；必须保留WP35§5.2/§9和EG-13/EG-20。显式形态参数函数无本层求值，不可改成孵化取图无动态提交。','binding':next(x['binding'] for x in legacy['adjacent_controls'] if x.get('legacy_id')=='GIR-FD82-A053')},
 conclusion='M04建议按其具名个体取图范围修订与旧孵化合同相容；本轮独立检查确认该有限消费者投影，不重开A053。')

add(5,'PP补给 → 战斗/野外资格 → PP写回与道具数量','partial',
 primary_owner='WP28主动道具资格；WP20 PP写回、WP40战斗登记、WP27库存为投影',
 producers=['主动ETHER/MAXETHER/ELIXIR/MAXELIXIR/LEPPABERRY选择'],state_writes=['成功PP恢复封顶','符合条件的场上副本PP同步','野外成功后扣数量；战斗登记先扣、失败复检按J07退款'],consumers=['战斗资格家族','队伍/背包使用包装','场上未变身且同槽同招式副本'],
 preconditions=['有效非蛋非Hyper目标和缺PP招式；道具在袋且为消费品','区分HP0与可战斗目标、主动LEPPA与被动持物'],configuration=['默认PBS FieldUse/BattleUse','回复10/全满；最大PP>0','场上同步要求未变身且同招式'],
 reviewed=['五物品家族别名、两上下文资格、实际战斗选择caller','PP辅助与野外扣减包装、战斗登记时机'],not_reviewed=['被动LEPPA恢复','AI所有道具策略、全部异常招式索引','真实队伍界面输入'],
 boundaries={'normal':'HP>0缺PP的合法目标战斗可登记；野外回复成功才扣；场上副本满足同步门才写穿。','failure':'HP0非蛋仍可在野外恢复PP，但战斗资格拒绝且尚未扣物；满PP/无有效总PP不生效。','cancellation':'野外招式/数量取消不扣；战斗目标/招式取消不登记；已登记取消按J07。','repetition':'一次回复使PP满后再次使用失败，不能重复扣；多件/别名按同门。','ordering':'战斗目标选择允许非蛋进入招式选择，随后资格拒HP0；不是UI先过滤所有濒死者。'},
 vectors=[{'id':'GR4-J05-V1','input':'普通非蛋HP0，TACKLE PP0/35，ETHER库存1，无其它拒绝门','expected':'野外选该招→PP10、库存0；独立战斗初态资格拒→PP0、库存1；HP>0为正常对照。','status':'NOT_EXECUTED'}],
 source_anchors=[S('003_Item_BattleEffects.rb',[[155,186],[501,531]],'战斗可战斗门/别名/效果'),S('002_Item_Effects.rb',[[632,684]],'非战斗PP条件和取消'),S('001_Item_Utilities.rb',[[367,382],[644,686],[710,775]],'封顶、同步、消费与非蛋通用门'),S('009_Battle_CommandPhase.rb',[[100,137]],'资格先于登记'),S('003_Scene_ChooseCommands.rb',[[265,284]],'目标选择只预排蛋，招式取消重选'),S('001_Pokemon.rb',[[264,270]],'able与HP0区别'),S('items.txt',[[3294,3333],[5242,5250]],'默认用途/别名身份')],
 spec_anchors=[P('wp28-item-use-and-training.md',[[112,129],[202,206]],'缺战斗HP门是M05-001；保留正确退款合同'),P('wp40-commands-obedience-and-action-order.md',[[99,114]],'登记/复检/退款')],
 historical_junction_ids=['G6-1','G6-2','G7-3','G7-5','CHAIN-3','N12'],existing_finding_ids=['GR4-M05-001'],conclusion='M05一条根因，战斗与UI/数量交界只引用，不新计。')

add(6,'育种亲本单持物 → 继承预算 → 静态向量','partial',
 primary_owner='WP34继承预算；WP20单持物身份为前提，测试目录为消费者',
 producers=['两亲本规范化持物身份','世代与力量道具映射'],state_writes=['先默认预算3；gen≥6且一方Knot才5','每种力量能力写入并扣预算一次；余下不同能力从剩余池取得'],consumers=['后代IV与最后能力重算','BR16–19测试向量'],preconditions=['正常两亲本、每只单一持物；没有扩展多持物或替换处理器','实际生成入口不接独立继承预算'],configuration=['MECHANICS_GENERATION','DESTINYKNOT与六件Power为独立身份','默认IV初始化保持未继承项'],
 reviewed=['生成caller→IV继承→末次calc_stats','单一持物规范化查询、不同道具数据、正文与BR18关系'],not_reviewed=['随机抽样运行、全部遗传通道','亲本Demo获取/寄养事件与时间','多持物插件前提不存在于本链'],
 boundaries={'normal':'单Knot+单Power在gen≥6为1固定+4其它；无Knot为3总项。','failure':'双不同Power不能同时再持Knot，故BR18的5−2分支不可由其前提满足；正文正确而测试不一致。','cancellation':'IV继承内部无取消；寄养领取取消未审，不补回滚。','repetition':'双方相同Power只占一个能力项、从两值择一；不同Power占两项，剩1；再次生成另一个蛋重新抽取。','ordering':'预算在力量项前计算；力量项去重并逐项扣；不把两种数量规则并列当无前提可选。'},
 vectors=[{'id':'GR4-J06-V1','input':'母POWERWEIGHT、父POWERBRACER，gen8，合法单持物','expected':'固定HP/ATTACK两项+随机不同1项，总3；BR18应只保3−2。','status':'NOT_EXECUTED'},{'id':'GR4-J06-V2','input':'一方DESTINYKNOT、另一方POWERWEIGHT，gen8；独立gen5','expected':'gen8总5（1+4）；gen5总3（1+2）。','status':'NOT_EXECUTED'}],
 source_anchors=[S('007_Overworld_DayCare.rb',[[21,51],[173,212]],'产生后代/预算/力量去重/剩余池'),S('001_Pokemon.rb',[[551,576]],'每亲本单持物'),S('items.txt',[[766,774],[1423,1439]],'三个身份互异')],
 spec_anchors=[P('wp34-inheritance-and-offspring.md',[[128,133]],'正确正文'),P('pokemon-rules-wp19-21-22-23-34.md',[[239,242]],'BR18错误预算分支','BR16–19')],historical_junction_ids=['G5-5','G5-6'],existing_finding_ids=['GR4-M06-001'],conclusion='仅测试向量根因关联M06，不改正确WP34，也不发明额外持物能力。')

add(7,'战斗选择登记 → 取消/退款 → 下一轮或正常终局','supported',
 primary_owner='WP40选择生命周期；WP28效果资格、WP42终局、WP27库存投影',
 producers=['合法战斗物品选择'],state_writes=['登记选择并扣库存','效果成功清物品身份；失败退款保留身份','下一命令/正式失能清选择；正常终局撤销选择可再次退款'],consumers=['攻击阶段物品分派','取消与正常战斗结束','下一命令阶段、正式失能'],preconditions=['普通内部战斗、有效库存/容量/消费者','重复退款例无伙伴、无中间失能/换人/清选择；宿主提示正常'],configuration=['消耗属性和物品BattleUse家族','玩家与非玩家业主资源','球家族4独立，无统一效果失败退球'],
 reviewed=['登记→消费→失败复检→退款→残留→终局/下轮/失能的实际链','成功效果返回不以true判退款；显式取消后清选择'],not_reviewed=['完整毒伤胜利夹具与所有终局原因（只检到达终局后的消费者）','宿主异常后的全局恢复','Safari/捕虫等覆写不纳入普通链'],
 boundaries={'normal':'成功效果正常返回清物品身份，终局不再退；取消未执行选择退回后清选择。','failure':'资格复检失败退物但不清身份；退物容量不足报错保留此前前缀。','cancellation':'取消调用退款→撤Mega→清选择；正常执行失败不是调用取消。','repetition':'执行失败已经退一次后，若同轮正常终局仍有身份可再退；次轮清选择/正式失能清选择不再退。','ordering':'登记先写选择再扣；终局接收捕获/场景结束之后才撤销选择，因此先前阶段异常不保证退款到达。'},
 vectors=[{'id':'GR4-J07-V1','input':'后备T缺1HP，POTION2、两名存活使用者顺序指T，容量正常；执行后当轮到正常终局','expected':'登记2→0，首件治满清身份，次件复检失败退至1留身份；终局再退至2。只改下一命令先到则保持1。','status':'NOT_EXECUTED'}],
 source_anchors=[S('006_Battle_ActionUseItem.rb',[[34,75],[87,147]],'登记/扣退/清身份'),S('009_Battle_CommandPhase.rb',[[5,23],[174,180]],'取消与下轮清理'),S('010_Battle_AttackPhase.rb',[[69,88]],'实际效果分派'),S('002_Battle_StartAndEnd.rb',[[479,511]],'正常终局退款消费者'),S('003_Battler_ChangeSelf.rb',[[69,88]],'正式失能清选择')],
 spec_anchors=[P('wp40-commands-obedience-and-action-order.md',[[97,114]],'分入口清理已准确'),P('wp28-item-use-and-training.md',[[112,131]],'库存/效果投影'),P('wp42-growth-end-of-round-and-battle-outcomes.md',[[177,191]],'正常终局可重复退款与异常边界')],historical_junction_ids=['G6-2','G7-5','CHAIN-3','N12'],existing_finding_ids=[],conclusion='限定生命周期投影supported；不重签U04-RF整套执行或全部战斗引擎。')

add(8,'自耗树果 → 续击属性/基底查询 → AI只读预测','supported',
 primary_owner='WP47-A自然之恩重读合同；WP50消费状态；WP46击循环；WP52-B预测投影',
 producers=['NATURALGIFT首击、目标JABO反伤','使用者ORAN半血自动消费'],state_writes=['首击HP、反伤、回复、当前/还原/可回收/拾取/吃果状态','持久持物写穿；背包不扣'],consumers=['下一击真实基底查询','正常招式结束消费守卫','AI当前状态失败/基底查询'],preconditions=['沿WP47-A§3.1.1完整合法夹具；有效PARENTALBOND，U ORAN H160/h81，T JABO首击后存活','排除共生/压制/保护/替身/画皮/冰脸/失手/免疫/睡冻/换人/紧张感/治疗封锁/RIPEN/CHEEKPOUCH及额外回调；提示正常'],configuration=['ORAN自然之恩毒/80与恢复10','JABO物理反伤总HP整除8','AI失败门与基底1→0转换'],
 reviewed=['首击HP提交→被击道具→使用者HP物品检查→持物清除→逐击calcDamage基底重读','当前有ORAN的AI只读查询与真实反应链分开','普通计算先会心再基底，吸收早返排除'],not_reviewed=['精确全伤害数值、获得PARENTALBOND操作链','AI完整候选评分与全随机策略','局部异常后宿主继续/退出/保存是否发生'],
 boundaries={'normal':'h101对照反伤后81>半血，ORAN仍在；第二击重读80，正常结束再耗。','failure':'h81→61→71并自耗；第二击空持物身份访问先失败，早于默认1与第二击HP写入；前缀不回滚。','cancellation':'已经起用的本地击循环无玩家取消；失能/睡冻/目标全倒停止与取消选择不同。','repetition':'目标JABO首击耗掉不重复反伤；单击对照ORAN已空时结束消费守卫跳过；不把多击初检当每击重跑。','ordering':'真实每击重读当前持物；AI在消费前只读当前ORAN可正常得到80，不执行JABO→ORAN链。'},
 vectors=[{'id':'GR4-J08-V1','input':'完整U04-NG01前提','expected':'81→61→71、ORAN空；第二击基底查询局部失败；对照h101不自耗，单击不进入第二查询。','status':'NOT_EXECUTED'}],
 source_anchors=[S('008_MoveEffects_MoveAttributes.rb',[[1338,1379]],'起用/类型/逐击基底/结束消费'),S('009_Battle_ItemEffects.rb',[[364,386],[1311,1330]],'ORAN/JABO效果'),S('006_Battler_AbilityAndItem.rb',[[212,243],[315,323]],'门/消费记录/清物'),S('010_Battler_UseMoveTriggerEffects.rb',[[5,45]],'反伤后即时查询'),S('007_Battler_UseMove.rb',[[403,429],[623,664],[683,701]],'每击写入和后续循环'),S('003_Move_UsageCalculations.rb',[[239,253]],'普通会心先于基底'),S('004_AI_MoveEffects_MoveAttributes.rb',[[1423,1435]],'只读资格与真实基底复用')],
 spec_anchors=[P('wp47-a-move-attributes-targeting-and-calling.md',[[55,71]],'续击失败准确'),P('wp50-held-item-triggers-and-consumption.md',[[113,121]],'消费投影准确'),P('wp52-b-field-damage-healing-and-target-evaluation.md',[[54,54]],'AI对应为B，不误指C')],historical_junction_ids=['G6-3','N13'],existing_finding_ids=[],conclusion='保留旧准确异常和范围；局部失败不得改成必然崩溃/正常还原或AI也失败。')

add(9,'设施临时等级/替换队伍 → 退出还原 → 统计/保存','supported',
 primary_owner='WP55会话主责；WP54单场经验还原；WP57租借提交；WP09保存投影',
 producers=['会话开始/报名或租借提交','设施单场等级策略'],state_writes=['保存原队伍引用并替换玩家队伍后安全保存','双方完整EXP按位置记录、临时改级；调整返回后才记持物','单场结果计胜负但不自动写会话决定/加胜；会话结束另回收记录'],consumers=['单场正常返回EXP与持物还原','取消/结束队伍恢复','会话类型统计与安全保存'],preconditions=['有效规则、队伍、对手与地图/保存宿主','按位置对应若要正确恢复必须保持两侧成员顺序/身份；不预设深拷贝'],configuration=['临时等级策略/适用侧','显式会话决定/加胜','安全保存返回false与传播异常分层'],
 reviewed=['经验/等级写入口、调整/还原与单场真实顺序','会话队伍引用、取消、重复结束、胜次统计','工厂选入/交换提交与保存位置临时替换'],not_reviewed=['完整设施名单/随机生成/评级','真实接待收费领奖地图事件','旧GR3-M09-001可选事项继续暂缓'],
 boundaries={'normal':'单场正常返回依位置恢复EXP、再双方治疗/解除变换/恢复持物，之后记录像/统计；会话正常结束另恢复原队伍。','failure':'调整/战斗/还原中失败只保留到达前缀，无统一确保恢复；安全保存false仍执行后续坐标恢复，传播异常可跳过。','cancellation':'会话取消有原队伍才恢复并reset，不保存；工厂交换取消仍提交当前租借集合但不增交换数。','repetition':'显式加胜可重复增加；结束重置后再结束先把玩家队伍设为已空原队伍字段，再非进行中返回。','ordering':'会话记录回收早于会话reset；单场胜利布尔不等于会话决定；临调记录是EXP不是仅等级，不能按新成员身份自动匹配。'},
 vectors=[{'id':'GR4-J09-V1','input':'两成员不同EXP/持物，临调后交换其位置，再正常还原','expected':'按当前位置恢复旧EXP/物品，不能保证按成员身份正确；不主张正常用户流程一定重排。','status':'NOT_EXECUTED'},{'id':'GR4-J09-V2','input':'活动会话取消；独立初态正常结束后再结束','expected':'取消恢复并重置不保存；重复结束可把队伍写为空。','status':'NOT_EXECUTED'}],
 source_anchors=[S('004_Challenge_LevelAdjustment.rb',[[28,78]],'完整EXP、位置还原'),S('001_Challenge_ChallengeRules.rb',[[61,80]],'策略主入口/双侧便利门'),S('004_Challenge_Battles.rb',[[40,104]],'真实单场还原与统计'),S('001_Challenge_BattleChallenge.rb',[[79,103],[200,229],[243,281],[292,318],[345,361],[388,427]],'会话队伍/取消/保存/工厂交界')],
 spec_anchors=[P('wp54-entry-eligibility-level-adjustment-and-clauses.md',[[72,103]],'单场EXP与失败顺序'),P('wp55-facility-session-and-restoration.md',[[54,65],[101,130]],'队伍引用、统计/保存分层')],historical_junction_ids=['G3-3','G4-1','G4-2','CHAIN-4'],existing_finding_ids=[],conclusion='限定静态链支持；不把设施脚本能力升级为Demo会话已运行。')

add(10,'同轮文本/数量/命令输入 → UI提交 → 状态恢复','partial',
 primary_owner='WP17输入原语；WP66-C/29数量业务与WP13变量提交为投影',
 producers=['光标命名同轮按键','共享物品数量与金钱商店数量输入','通用命令/逐位数字'],state_writes=['命名helper先编辑，确认返回后caller写昵称','商店返回数量后再确认/容量/资源提交','事件数字返回写游戏变量并标记刷新'],consumers=['命名调用者（孵化/赠送）','买入/物品使用包装','解释器103与普通/帮助菜单'],preconditions=['静态同轮查询成立；正常窗口/音效/输入返回','各入口保持自身顺序，不假设同一物理设备必产生组合'],configuration=['逐位数字最小/最大/取消编码','商店价格/上限；共享数量初值','光标命名与键盘模式区分'],
 reviewed=['光标命名方向消耗轮与SPECIAL/ACTION/BACK/USE顺序','共享数量BACK优先、商店方向优先，后续确认/提交','普通命令允许取消时BACK优先；逐位数字先编辑，USE压过BACK与越界分支','正常退出窗口可见性/帮助显示和事件等待标志交接'],not_reviewed=['BP商店本次未沿源重审（沿旧限定证据）','真实键盘/手柄竞争、全部命名特殊上限','所有UI异常资源释放、跨场景重入'],
 boundaries={'normal':'文本需确认才返回；数量返回非零仍要业务确认/容量；合法数字可本轮编辑后提交变量。','failure':'数字USE越界蜂鸣继续，同轮BACK不执行；窗口异常不保证恢复等待/可见性；购买资源复查失败不提交。','cancellation':'共享数量BACK+USE→0；普通可取消命令BACK+USE→取消编码；数字合法USE+BACK→确认值；命名BACK+USE只删除。','repetition':'商店方向重复+USE仅编辑等待；下一轮仅USE才返回；各次成功业务提交保持，后来退出不回滚。','ordering':'先组件更新再数字确认；命令组件导航先于结果；光标实际移动消耗本轮；商店交易确认在数量返回之后。'},
 vectors=[{'id':'GR4-J10-V1','input':'共享数量和商店各初值1/上限≥11，同轮RIGHT重复+USE触发','expected':'共享返回1；商店改11仍等待，下一轮仅USE才返11。','status':'NOT_EXECUTED'},{'id':'GR4-J10-V2','input':'逐位数字合法编辑与USE+BACK同轮；独立越界编辑对照','expected':'合法返回本轮新值；越界只蜂鸣继续，未取消；关联M10-001。','status':'NOT_EXECUTED'}],
 source_anchors=[S('025_UI_TextEntry.rb',[[658,717],[743,785]],'光标操作/结果/包装'),S('018_UI_ItemStorage.rb',[[276,337]],'共享数量顺序与显示恢复'),S('020_UI_PokeMart.rb',[[477,538],[598,646]],'商店顺序与交易提交'),S('011_Messages.rb',[[166,205],[721,801]],'通用命令/数字竞争'),S('005_SpriteWindow_text.rb',[[687,730]],'数字先编辑'),S('004_Interpreter_Commands.rb',[[325,334]],'结果变量/地图刷新/等待清除')],
 spec_anchors=[P('wp17-messages-windows-input.md',[[92,121],[146,171]],'命名已准确；通用命令/数字差异关联M10-001'),P('wp66-c-bag-item-storage-and-shop-ui.md',[[88,108],[124,158]],'数量竞争与业务提交分层已准确')],historical_junction_ids=['G7-1','G7-3','CHAIN-3','N15'],existing_finding_ids=['GR4-M10-001'],conclusion='只补通用命令/逐位数字缺口；不把旧正确物品数量/光标命名合同重计为新问题。')

add(11,'图鉴记录/MapSize → 可访问列表/可见点 → 栖息地显示','supported',
 primary_owner='WP62图鉴记录与Area集合；WP63地点首条查询、WP66-B显示为不同投影',
 producers=['捕获/赠送/形态登记（接收入口详J13）','遭遇表与MapPosition/MapSize、区域Point/游戏开关'],state_writes=['seen/owned/form/last-seen及可访问图鉴刷新','Area每次构建局部格集合，无持久栖息地图层写入'],consumers=['可访问区域列表','遇表按版本枚举与目标物种匹配','Area点亮/unknown显示；区域地图游标与名称/详情/治疗点对照'],preconditions=['固定B/R直接源审，不消费M11报告','正常01形状、合法区域/地图元数据和遭遇物种','当前UI/资源/消息正常；媒体实际不可验证'],configuration=['USE_CURRENT_REGION_DEX/解锁与seen门','当前遭遇版本、HideEncountersInPokedex','Point可见开关；MapSize宽/形状'],
 reviewed=['记录与刷新、Area表枚举→物种→元数据→mask→可见并集→绘制','v>0枚举回退键不一致的已知缺陷','区域地图长度定位和首条同格查询，不与Area并集混用'],not_reviewed=['M11任何未冻结提交','全部图鉴筛选、历史记录清理和语言体型转换','真实地图、Point完整有效性、任意非01/越界输入'],
 boundaries={'normal':'宽3/形状11111只亮5格；仅已登记存在的可见Point相交；重复同格按集合点亮。','failure':'物种不在表/地图元数据缺/隐藏/区域不同均不贡献；无点显示unknown；不添加任意坏数据兜底。','cancellation':'Area查看无取消回滚语义，本地格集合非持久；图鉴浏览其它写入不在本链重新审。','repetition':'重复登记同形态是布尔写；Area重新计算，不叠加重复点；同格后一可见Point可使Area亮，首条隐藏仍让WP63查询空。','ordering':'图鉴seen驱动可访问列表，不是Area点亮条件；Area来自表而非捕获地点历史；版本单次get正确回退不能替代each枚举。'},
 vectors=[{'id':'GR4-J11-V1','input':'MapPosition=(0,13,12)，宽3，S=10000；所有需用点可见','expected':'仅(13,12)亮；11111为五格，尾格(15,13)不亮；区域游标按长度可到尾格。','status':'NOT_EXECUTED'},{'id':'GR4-J11-V2','input':'同格首Point开关51关闭、第二Point无门','expected':'Area可亮；WP63名称/详情/治疗取首条仍空。','status':'NOT_EXECUTED'}],
 source_anchors=[S('005_Player_Pokedex.rb',[[24,45],[147,160],[195,227],[315,332]],'状态写入/刷新/形态'),S('013_Encounter.rb',[[30,35],[53,68]],'查询/枚举分层'),S('004_UI_Pokedex_Entry.rb',[[302,390]],'占位和可见点交集到显示'),S('009_UI_RegionMap.rb',[[89,100],[183,190],[211,230]],'长度定位与首条查询')],
 spec_anchors=[P('wp62-pokedex-records-regions-and-content.md',[[73,78],[116,139]],'记录与Area准确'),P('wp66-b-storage-and-pokedex-ui.md',[[198,200]],'条目页投影'),P('wp63-pokegear-map-music-and-phone.md',[[44,48]],'首条同格规则')],historical_junction_ids=['G3-4','G7-2','N17'],existing_finding_ids=[],conclusion='仅具名图鉴/地图交界supported；不接受、等待或假定M11结论。')

add(12,'工具单项导出/导入 → 集合保存/关联编译 → 动画资源消费者','supported',
 primary_owner='WP74作者交换/关联规则；WP04编译时机、WP67-A播放与WP15资源投影',
 producers=['选中动画.anm导出/导入','集合改名保存；Move/OppMove关联编译'],state_writes=['导入替换当前内存槽，集合保存另外确认','有效映射才写关联和集合；零有效保留旧磁盘映射','集合与映射缓存独立'],consumers=['战斗按侧映射查槽并叠hit号','类型/类别回退再TACKLE（本次仅核回退流程，未审默认表全集）','选中集合槽和媒体消费者'],preconditions=['有效动画对象和当前选中槽、可读写目标；宿主/媒体正常是假设','若希望播放看到新映射，缓存须未加载或已失效；编译写盘本身不是清当前映射缓存'],configuration=['Move:/OppMove:有效注册招式身份与Common:精确名称','单项.anm不包含媒体复制','集合/映射文件与当前缓存分开'],
 reviewed=['单项导出取消/失败、导入替换先于缺图警告','编辑器保存/退出→集合缓存失效；编译有效/零有效与后槽覆盖','运行显式映射/回退/槽消费；不把文件写出当资源存在'],not_reviewed=['批量导入导出与资源安全复制所有分支','默认类型动画映射数据全集（M10-004仍由主责处理，不在J重新判缺失）','所有逐帧播放器、真实.anm解码/媒体/编译执行'],
 boundaries={'normal':'非空名导出选中单项；导入成功替内存槽，之后保存/编译/缓存消费各是独立步骤。','failure':'导入坏编码返回选择循环；缺图警告时槽已替换；零有效关联编译不清旧文件，播放仍可能旧关联；异常不补原子回滚。','cancellation':'空导出名不写；导入BACK不改；编辑器不保存但退出时清集合缓存，按原落盘状态重载。','repetition':'同侧有效关联后槽覆盖；重复编译有有效项仍写；已缓存映射不会因另一步写盘自动更新。','ordering':'外部交换不直接更新运行集合/映射；播放先查关联，再读集合槽，再到媒体请求。'},
 vectors=[{'id':'GR4-J12-V1','input':'原映射含TACKLE；把最后有效Move名改普通名并保存、再编译；缓存初为空','expected':'零有效不重写映射，播放器仍可取旧槽关联；不证明那个槽或媒体成功显示。','status':'NOT_EXECUTED'},{'id':'GR4-J12-V2','input':'同侧两个合法Move:TACKLE名称先槽a后槽b','expected':'映射取b；OppMove另域。','status':'NOT_EXECUTED'}],
 source_anchors=[S('004_AnimEditor_ExportImport.rb',[[20,83]],'单项格式/替换/取消/失败'),S('005_AnimEditor_Functions.rb',[[994,1001]],'保存与退出分开'),S('002_Compiler_CompilePBS.rb',[[1274,1282],[1295,1319]],'从空映射到有条件写入'),S('001_MiscPBSData.rb',[[39,53]],'集合/映射缓存消费者'),S('004_Scene_PlayAnimations.rb',[[412,443],[469,525]],'显式关联、回退和槽消费')],
 spec_anchors=[P('wp74-battle-animation-authoring-and-exchange.md',[[335,343],[394,421]],'作者/编译/缓存/播放交界已准确')],historical_junction_ids=['G8-2','G8-3','G9-4','CHAIN-6','N18'],existing_finding_ids=[],adjacent_unreviewed_finding_ids=['GR4-M10-004'],conclusion='有限单项/显式关联链supported，不扩为默认类型映射数据充分或批量工具全部通过。')

add(13,'捕获/赠送接收 → 容量/队伍盒子 → 图鉴与部分提交','supported',
 primary_owner='WP38捕获接收；WP26赠送独立入口；WP25容量与WP62图鉴投影',
 producers=['合法球登记与成功捕获队列','普通/静默赠送个体'],state_writes=['成功捕获先移对方队伍/效果/来源/形态再排待接收','终局捕获计数/见过/拥有/末次形态先于命名/实际存储','队伍/盒子写入及当前盒更新；失败不撤销前序图鉴'],consumers=['默认战斗Peer与储存接收扫描','满队替换菜单','图鉴可访问/条目显示；玩家/储存持久单元'],preconditions=['本链普通内部战斗/默认Peer、有效玩家与存储；无伙伴投影','初始双满预检与后段容量变化/直接触达分开','宿主和提示在各向量指定点前正常'],configuration=['HEAL_STORED_POKEMON、送盒档位0/1/2','更频繁显示新物种配置仅赠送门；捕获条目省略该配置','see_form与静默两入口不同'],
 reviewed=['球资格的双满门→成功排队→终局先图鉴后接收','队伍有位/满队送盒/储存扫描、满盒局部失败','赠送三次容量检查和返回值分层；静默加入与仅入队静默see_form差别'],not_reviewed=['捕获概率/球表全集','伙伴合并参与集合的错物还原旧控制（仅复用其限定证据，不重审整CP21/22）','Safari/捕虫覆写、实际容量变化事件、真实存档'],
 boundaries={'normal':'队伍有位先入队；满队当前盒再其余盒首空；捕获首次拥有可展示后再命名存放。','failure':'默认菜单双满先拒不扣球；后段若触达双满，默认Peer缺消息入口可在返回前失败，已有图鉴/命名/可选治疗保留；赠送内层容量拒绝外层仍可true。','cancellation':'捕获询问档取消=送盒，强制档取消重选；成员选择取消重回菜单；拒绝昵称不取消接收；赠送同意后空文本清名。','repetition':'相同物种可再次获得，拥有布尔保持、捕获计数可增；待接收循环全部正常完成才清队列，异常后不称重入幂等。','ordering':'捕获队列图鉴在容量存储前；赠送获得消息/图鉴/昵称之间有等待，后置复检可与入口结果不同；保存只取实际已写状态。'},
 vectors=[{'id':'GR4-J13-V1','input':'未拥有X，初始容量通过；到后段存储时双满，默认Peer','expected':'可能已捕获计数/已见/拥有/昵称后于存储兜底失败；不承诺原子撤销或正常返回。','status':'NOT_EXECUTED'},{'id':'GR4-J13-V2','input':'合法已有个体、see_form=false；静默加入 vs 仅入队静默，队伍有位','expected':'静默加入显式已见+拥有；仅入队静默仅拥有，本调用不写已见。','status':'NOT_EXECUTED'}],
 source_anchors=[S('003_Item_BattleEffects.rb',[[28,63]],'球菜单容量守卫'),S('005_Battle_CatchAndStoreMixin.rb',[[5,106],[165,200]],'接收/队列/提交顺序'),S('004_Battle_Peers.rb',[[4,36]],'默认存储与全满失败'),S('004_PokemonStorage.rb',[[231,251]],'可选治疗后扫描'),S('002_Utilities_Pokemon.rb',[[4,90],[96,129]],'赠送三层复检与静默差别'),S('001_Battle.rb',[[658,674]],'内部战斗计数/见过门'),S('004_Game_SaveValues.rb',[[3,8],[97,102]],'玩家和储存持久单元')],
 spec_anchors=[P('wp38-capture-and-receiving.md',[[90,118]],'队列/接收/全满失败合同'),P('wp26-acquisition-gifts-and-script-trade.md',[[63,89]],'赠送与部分提交'),P('wp62-pokedex-records-regions-and-content.md',[[50,64]],'不同入口图鉴顺序')],historical_junction_ids=['G3-1','G3-2','G3-4','G3-5','CHAIN-1'],existing_finding_ids=[],conclusion='接收部分提交链supported；图鉴先写不等于个体必已入队/盒；固定R/B独立检查不依赖M11。')

add(14,'新游戏 → 遭遇/战斗 → 接收 → 保存继续：静态流程边界','partial',
 primary_owner='各领域单主责；J仅记录端到端静态交接，不设新的总事务主规格',
 producers=['启动初始化/新游戏注册值','合法场地步进遭遇与生成个体'],state_writes=['玩家/背包/存储/变量默认值与地图/遭遇上下文','实际战斗效果与接收提交（J13）','保存取值写盘/继续恢复未加载值、重新建遭遇上下文'],consumers=['地图步进门、WildBattle覆盖门/核心','战斗正常终局接收','保存UI确认/保存/继续地图恢复'],preconditions=['系统/地图/事件/媒体与合法初始队伍、捕获道具须由完整工程提供','普通流程无DEBUG跳过/模式覆写、异常与额外改写','当前材料不包含上述完整工程，不补造初始授予/遭遇可达事件'],configuration=['起始地图/位置与注册新游戏值','遭遇版本/表/地形/可战斗成员/步进门','捕获容量/送盒选项','save magic_number/safesave/类型与已加载标志'],
 reviewed=['初始化对系统/起始地图依赖；新游戏值加载→遭遇setup','步进生产候选→生成/可覆盖战斗→正常核心返回','J13接收后玩家/存储随正常保存恢复','保存取消、IO/类型失败、继续地图重建条件'],not_reviewed=['真实新游戏→初始队伍/图鉴/球授予→遭遇地图→捕获→继续完整Demo','所有遭遇概率和战斗轮次；用户输入/媒体','任意旧档转换/断电/损坏文件恢复；不存在运行通过声明'],
 boundaries={'normal':'条件齐全才有静态连接：新值→地图/遭遇→战斗→接收→玩家/储存保存→继续加载。各入口结果不是单一通关布尔。','failure':'无起始图/系统材料不能证明启动；无可战斗成员步进遭遇早退；战斗覆写/异常可跳过正常链；保存类型失败在打开前、IO失败仅回退save_count，继续可在地图恢复失败。','cancellation':'保存确认拒绝不写盘；接收/命名取消语义由J13；标题与覆盖存档额外确认不能替代领域提交回滚。','repetition':'新游戏只初始化有值且未加载/强制重置项；继续会话统计再增；重新建立遭遇服务，不从持久全局字段推定临时触发器跨档保持。','ordering':'保存捕获后的真实状态须正常到保存取值；先接收部分提交后保存只可能保存实际前缀；没有总事务、可玩Demo或成功恢复保证。'},
 vectors=[{'id':'GR4-J14-V1','input':'所需工程数据齐全、合法授予和遭遇前提已成立、普通捕获正常接收并成功保存','expected':'player含队伍/图鉴、storage含盒子写入通过各自注册单元恢复；地图/遭遇随后恢复；这是条件静态交接而非实测。','status':'NOT_EXECUTED'},{'id':'GR4-J14-V2','input':'本次固定参考材料状态','expected':'真实地图/系统/完整Demo交接未证；不制造端到端PASS。','status':'NOT_EXECUTED'}],
 source_anchors=[S('001_StartGame.rb',[[4,16],[39,104],[111,124]],'新游戏/继续/保存与地图依赖'),S('004_Game_SaveValues.rb',[[3,8],[35,47],[63,102]],'相关持久单元'),S('001_Overworld.rb',[[172,218]],'步进与遭遇守卫'),S('003_Overworld_WildEncounters.rb',[[7,27],[445,468]],'上下文setup/生成通知/主动请求'),S('001_Overworld_BattleStarting.rb',[[356,440]],'覆盖门/核心开战/返回分层'),S('002_Battle_StartAndEnd.rb',[[479,511]],'正常终局接收交接'),S('001_SaveData.rb',[[24,60]],'读取/转换写回/汇编先于覆盖写'),S('002_SaveData_Value.rb',[[239,282]],'已加载门与新游戏/汇编'),S('014_UI_Save.rb',[[100,121]],'UI确认/覆盖确认/保存结果')],
 spec_anchors=[P('wp09-save-startup-continue.md',[[85,115]],'启动/继续/保存边界'),P('wp36-wild-encounters-and-modifiers.md',[[151,158]],'步进全链'),P('wp38-capture-and-receiving.md',[[104,118]],'接收提交'),P('wp77-demo-evidence-and-capability-coverage.md',[[5,27]],'配置/入口非可玩证据')],historical_junction_ids=['G2-6','G3-1','G9-2','G9-4','G9-6','CHAIN-2'],existing_finding_ids=[],conclusion='静态交接可定位，但缺完整工程且未执行；整体状态partial而非missing规格或端到端支持。')

# Final bounded consumer anchors, read directly before output validation.
records[2]['spec_anchors'].append(P('wp11-map-topology-transfer.md',[[59,71]],'实际转移参数及状态消费者'))
records[3]['source_anchors'].append(S('006_UI_Summary.rb',[[117,135]],'摘要实际调用个体精灵/图标'))
records[3]['spec_anchors'] += [P('wp21-dynamic-forms-and-display.md',[[157,163],[177,181]],'个体资源副作用与限时形态'),P('wp15-resource-matching-and-audio.md',[[48,50]],'资源个体入口投影')]
records[4]['source_anchors'].append(S('moves.txt',[[5326,5336]],'静态PP向量所用TACKLE最大PP35'))
records[7]['source_anchors'] += [S('002_Move_Usage.rb',[[45,53]],'有效亲子爱与单目标真实计划两击'),S('items.txt',[[5252,5260],[5721,5727]],'ORAN与JABO配置'),S('moves.txt',[[5581,5591]],'默认自然之恩物理及效果身份')]

records[4]['source_anchors'].append(S('002_ShadowPokemon_Other.rb',[[165,177]],'战斗通用道具资格实际覆写，不取消PP家族HP门'))
records[7]['source_anchors'] += [S('006_Battler_AbilityAndItem.rb',[[272,286]],'持物效果成功后的真实消费调用'),S('001_Battle_Battler.rb',[[85,89]],'清持物写穿关联个体')]
classification=[
 ['Generic Kernel','User Interface','Demo / Developer Experience'],
 ['Generic Kernel','Engine / Overworld Integration'],
 ['Engine / Overworld Integration','User Interface'],
 ['Creature-RPG','Pokémon Rules','User Interface'],
 ['Creature-RPG','Combat Requirements','User Interface'],
 ['Creature-RPG','Pokémon Rules'],
 ['Combat Requirements','Creature-RPG'],
 ['Pokémon Rules','Combat Requirements'],
 ['Combat Requirements','Creature-RPG','Generic Kernel'],
 ['User Interface','Creature-RPG','Engine / Overworld Integration'],
 ['Pokémon Rules','User Interface','Engine / Overworld Integration'],
 ['Demo / Developer Experience','Engine / Overworld Integration','User Interface'],
 ['Pokémon Rules','Creature-RPG','Combat Requirements'],
 ['Demo / Developer Experience','Generic Kernel','Creature-RPG','Combat Requirements','Engine / Overworld Integration']]
for r,groups in zip(records,classification):r['classification']=groups

# Preserve exact qualified history text/identities; links are projections, not whole-row PASS.
historical=[]
for i,old in enumerate(nav['records']):
 linked=[r['id'] for r in records if old['id'] in r['historical_junction_ids']]
 historical.append({'id':old['id'],'kind':old['kind'],'title':old['title'],
  'status':'not_reviewed','history_use':'historical_qualified_evidence_reused' if linked else 'not_reviewed',
  'current_bounded_projection_ids':linked,'does_not_promote_whole_historical_scope':True,
  'retained_normal_scope':old['normal'],'retained_failure_and_boundary_scope':old['failure_and_boundary'],
  'original_identity':old['original_identity'],'original_pointer':old['original_pointer'],
  'original_object_sha256':old['original_object_sha256'],'accepted_successor_binding':old['accepted_successor_binding'],
  'historical_required_ids':old['historical_required_ids'],
  'navigation_source':{'path':'evidence/junction-navigation.json','pointer':f'/records/{i}','verification':'shared navigation/readiness reused; not reaudited'}})

j={'schema_version':'1.0','reviewer':'J','thread_id':launch['thread_id'],
 'scope':'14具名有限静态源链；历史54+8+18逐条原scope保留；M11未冻结材料不在输入。',
 'records':records,'historical_coverage':historical,
 'classification_legend':{'supported':'该具名静态投影的B合同获R支持，不是执行PASS','partial':'投影有已存在GR4问题或所请求全链材料未证','missing':'只用于完成全131反证后仍无合同的新问题；本轮无此项','unresolved':'证据仍不能裁决；本轮没有独立新增此项','not_reviewed':'未在J本轮审整个范围'},
 'retained_controls':{'GR3':'CLOSED states retained; only linked bounded semantic projections checked',
 'legacy_229_341':'原ID与每条限定scope不升级/缩减；仅A053具名孵化投影额外亲审。',
 'GR3-M09-001':'optional deferred, no reopen','GR4-M02-003':'no revision required per explicit user instruction',
 'M11':'unsealed submission NOT_CONSUMED; no waiting or acceptance; direct fixed-B/R review only'}}
dump('junctions.json',j)

# Single semantic owner with consumer projections; these are documentation responsibility suggestions.
ownership = [
 ('内容身份及重复判定','wp03-content-identity-and-schema.md',[1],'WP04编译、WP63电话选择只消费本域身份；Default例外不跨域推广。'),
 ('译文导入和运行查找','wp08-localization.md',[1],'电话/窗口消费当前语言结果；占位和显示控制阶段分开。'),
 ('变量墙钟计时','wp06-time-random-steps-stats.md',[2],'WP09仅持久化变量；地图刷新消费已写状态。'),
 ('保存和继续生命周期','wp09-save-startup-continue.md',[2,9,13,14],'计时、设施、接收只能引用各自持久单元；不补总事务。'),
 ('冲浪临时运动状态','wp12-terrain-movement-vehicles.md',[3],'WP59动作生产；WP11转移、WP16精灵和WP13解释器各按实际门消费。'),
 ('动态形态求值','wp21-dynamic-forms-and-display.md',[4],'WP15资源和WP35孵化须保留调用者求值时点。'),
 ('个体形态提交副作用','wp18-creature-identity-species-ownership.md',[4],'WP21引用能力/缓存/图鉴写入；资源失败不生成新事务。'),
 ('主动PP补给资格和效果','wp28-item-use-and-training.md',[5],'WP20封顶和副本同步、WP40登记、UI只投影资格。'),
 ('命令选择/物品身份清理','wp40-commands-obedience-and-action-order.md',[5,7],'WP28复检、WP42终局撤销；退款与清身份不可等同。'),
 ('IV继承预算','wp34-inheritance-and-offspring.md',[6],'WP20单持物为前提，BR18为测试消费者，正文不被错误向量覆盖。'),
 ('被动持物消费状态','wp50-held-item-triggers-and-consumption.md',[8],'WP47-A续击消费当前持物；WP27主动库存不受被动消费扣减。'),
 ('自然之恩逐击基底查询','wp47-a-move-attributes-targeting-and-calling.md',[8],'WP46击循环与WP50反应接点保持；AI只读另有主责。'),
 ('AI自然之恩预测','wp52-b-field-damage-healing-and-target-evaluation.md',[8],'只读当前输入，不复制真实被击/自耗反应链；不误归WP52-C。'),
 ('设施临时EXP/等级还原','wp54-entry-eligibility-level-adjustment-and-clauses.md',[9],'WP55单场包装按位置消费，不新增按身份还原保证。'),
 ('设施会话/队伍替换/结束','wp55-facility-session-and-restoration.md',[9],'WP57租借提交、WP09保存、单场统计均为分立消费者。'),
 ('通用文字/数字/命令输入','wp17-messages-windows-input.md',[10],'WP13变量提交、WP26/35昵称caller消费编码；不统一取消含义。'),
 ('物品数量特化竞争顺序','wp66-c-bag-item-storage-and-shop-ui.md',[10],'WP29业务确认/容量/扣款消费返回数量；通用逐位数字属于另一合同。'),
 ('图鉴状态记录与访问集合','wp62-pokedex-records-regions-and-content.md',[4,11,13,14],'孵化/捕获/赠送负责调用时点；展示和玩家持久单元仅投影。不表示接受M11。'),
 ('Area栖息地可见格集合','wp62-pokedex-records-regions-and-content.md',[11],'WP36提供遭遇表，WP66-B绘制；WP63首条查询不能替代可见Point并集。'),
 ('区域地点/详情/治疗点查询','wp63-pokegear-map-music-and-phone.md',[11],'同格首条语义独立于Area集合；长度游标消费者也不取mask占位。'),
 ('队伍/盒子容量与放置','wp25-party-and-storage.md',[13,14],'WP26赠送与WP38捕获各自有前置门和部分提交；不能由容量服务推原子接收。'),
 ('赠送接收工作流','wp26-acquisition-gifts-and-script-trade.md',[13],'图鉴、昵称、容量消费者按三次检查顺序引用；不与捕获合并。'),
 ('捕获与战后接收工作流','wp38-capture-and-receiving.md',[13,14],'WP40球登记，WP42终局调用、WP25存储、WP62图鉴各有门。'),
 ('动画交换/保存/关联编译','wp74-battle-animation-authoring-and-exchange.md',[12],'WP04生命周期调用、WP67-A槽消费、WP15媒体解析只投影；单项导出不带媒体。'),
 ('野外遭遇候选及启动交接','wp36-wild-encounters-and-modifiers.md',[14],'WP39战斗/WP38接收为消费者；新游戏授予与Demo可达性没有材料。')
]
shared=[]
for i,(semantic,owner,nums,projection) in enumerate(ownership,1):
 related=[records[n-1] for n in nums]
 owner_path=next(x for x in formal_paths if pathlib.Path(x).name==owner)
 shared.append({'id':f'GR4-JSC{i:02d}',
  'main_identity':{'semantic_capability':semantic,'formal_baseline':B,'single_primary_owner':owner_path},
  'consumer_projection_recommendation':projection,'junction_ids':[r['id'] for r in related],
  'existing_finding_links_in_related_chains':sorted({f for r in related for f in r['existing_finding_ids']}),
  'primary_owner_anchors_reviewed':[a for r in related for a in r['spec_anchors'] if a['path']==owner_path],
  'ownership_only_if_no_anchor':'主责归属建议，不签整文件通过；精确亲审边界仅junction记录。',
  'classification':'documentation responsibility only; not implementation architecture',
  'deduplication_rule':'相同finding只计一次。多个消费者投影、重复引用及相邻已正确合同不新增根因。'})
dump('shared-capabilities.json',{'schema_version':'1.0','records':shared,
 'cross_chain_unifications':[
  {'identity':'库存资源计数','owner':'WP27','projections':['GR4-J05主动PP物品','GR4-J07登记/退款','GR4-J10商店数量提交'],'separation':'WP28主责效果资格；WP40主责命令身份清理；被动持物J08不扣背包。'},
  {'identity':'形态求值与提交','owners_by_distinct_semantics':{'动态求值':'WP21','提交副作用':'WP18'},'projections':['GR4-J04摘要/精灵/孵化','GR4-J11图鉴登记','GR4-J13离场与捕获'],'separation':'资源请求点与领域提交不是新的重复根因；M04只计一次。'},
  {'identity':'图鉴记录','owner':'WP62','projections':['GR4-J04孵化见过','GR4-J11区域/Area显示','GR4-J13捕获/赠送','GR4-J14玩家持久单元'],'separation':'登记/拥有/捕获次数/末次形态各入口门保持；J不接受未冻结M11。'},
  {'identity':'保存生命周期','owner':'WP09/10','projections':['GR4-J02变量计时','GR4-J09设施临时坐标','GR4-J14继续'],'separation':'失败返回与未捕获异常分开；不增加跨领域总事务。'},
  {'identity':'输入竞争','owner':'WP17通用输入；特化数量顺序由WP66-C具名承接','projections':['GR4-J10事件数字/命名/商店','GR4-J13昵称接收'],'separation':'M10-001不吸收旧准确共享数量/命名控制；取消编码由消费者解释。'}],
 'not_new_coverage_claim':'单主责建议不改变Feature Matrix、正式规格或全局aggregate；不是未来类/包设计。'})

links=[]
for fid in sorted({f for r in records for f in r['existing_finding_ids']}):
 links.append({'id':fid,'junction_ids':[r['id'] for r in records if fid in r['existing_finding_ids']],
  'disposition':'existing_finding_link_only_not_new_count','acceptance':'J independently inspected the named source/spec projection; parent final counterreview/acceptance remains separate'})
dump('findings.json',{'schema_version':'1.0','findings':[],'existing_finding_links':links,
 'rejected_candidates':[{'candidate_id':'J-CAND-01','title':'电话Default重复覆盖是否缺合同','disposition':'REJECTED_ALREADY_SUPPORTED_IN_B',
 'counterevidence':'candidate-counterevidence.json；全131文件检索，WP03§5.2/WP04 L89/KR14–16/KL36准确承接；源覆写/登记/终检/消费已追。',
 'new_issue_id_assigned':False,'historical_closure':'GR3 CLOSED保留'}],
 'new_substantive_findings_count':0,'parent_targeted_challenge':'No new J issue requiring new GR4-J-001 challenge; existing module issues remain on parent workflow. Do not infer acceptance of all domains.'})

# Fix read-log ranges to reflect only actual returned lines; retain unsuccessful range attempts separately.
reads=json.loads((HERE/'read-log.json').read_text())
for x in reads:
 p=(SRC if x['kind']=='source' else ROOT)/x['path']; n=len(p.read_text().splitlines())
 requested=x.get('requested_ranges',x['ranges'])
 x['requested_ranges']=requested
 x['ranges']=[[a,min(b,n)] for a,b in requested if a<=n]
 x['empty_requested_ranges']=[[a,b] for a,b in requested if a>n]
 x['whole_file_read_claim']=False
 (None)
dump('read-log.json',reads)
ce=json.loads((HERE/'candidate-counterevidence.json').read_text())
ce['result']='REJECTED_ALREADY_SUPPORTED_IN_B'
ce['reviewed_contexts']=['WP03§5.2 L121–134','WP04 L82–92','KR14–16/KL36','WP63§5.3 L140–145']
ce['scope_files']=[x['path'] for x in formal]
ce['limitations']='一次针对性候选反证，不是131条款全新语义通过；无新missing/contradiction判定。'
dump('candidate-counterevidence.json',ce)

execution={'schema_version':'1.0','reviewer':'J','thread_id':launch['thread_id'],'requested_model':launch['requested'],'actual_model_echo':'UNVERIFIED',
 'identity_basis':{'shared_baseline':'../../baseline.json','launch':'../../tasks/J-launch.json','frozen_input_list':'../../tasks/J-input-identities.json','formal_commit':B,'formal_tree':'d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a','reference_commit':R,'reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','reference_root':str(SRC),'mode':'shared identity/readiness reuse; no old administrative audit rerun'},
 'unsealed_M11':'NOT_READ_NOT_WAITED_NOT_ACCEPTED',
 'execution':{'source_function_execution':'NOT_EXECUTED','isolated_original_function_probes':'NOT_EXECUTED','reference_runtime':'NOT_EXECUTED','UI_gameplay':'NOT_EXECUTED','PBS_translation_compilation':'NOT_EXECUTED','animation_import_export':'NOT_EXECUTED','real_save_load':'NOT_EXECUTED','complete_demo':'NOT_EXECUTED'},
 'performed':['Read-only rg searches and bounded line reads of fixed source/current formal material','Manual producer/state/consumer/ordering comparison and static vectors for 14 chains','One full formal131 synonym counterevidence search for candidate J-CAND-01, rejected as already covered','Python artifact generation/schema-anchor checks only; not behavioral tests'],
 'prior_probe_policy':'Module isolated execution receipts are not J executions; no copied run-PASS. Source readability and preserved root BMP/font/translation availability do not establish runtime.',
 'write_scope':str(HERE),'writes_outside_scope':False,'reference_or_formal_modified':False,'shared_aggregates_modified':False,'history_modified':False,'agents_started':0,'commits_or_pushes':0,'new_framework_implementation':False,
 'tooling_notes':['Some initial filename/range navigation guesses returned no file or no lines; corrected with inventory and exact reads. read-log requested vs actual ranges distinguish these attempts. No absence claim is based on a failed navigation.'],
 'read_statistics':{'unique_source_files':len({x['path'] for x in reads if x['kind']=='source' and x['ranges']}),'unique_formal_files_bounded_read':len({x['path'] for x in reads if x['kind']=='spec' and x['ranges']}),'formal_counterevidence_search_files':len(formal)},
 'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'artifact_validation':'See validation.json; validation is TOOL_VALIDATION only'}
dump('execution.json',execution)

counts=collections.Counter(r['status'] for r in records)
report=['# J：独立跨模块有限静态取证报告','',
 f'本轮14条具名链：supported {counts["supported"]}、partial {counts["partial"]}；新增J实质问题0，关联已有GR4问题{len(links)}。这不是14次运行通过，更不是历史80项新PASS。',
 '',f'- 固定B `{B}`，tree `d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a`。',f'- 固定R `{R}`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。',f'- 实际thread ID按J-launch.json：`{launch["thread_id"]}`；请求 gpt-6-astra / ultra / default / noFast，实际模型回显 **UNVERIFIED**。',
 '- 身份/readiness复用共享baseline与J输入清单。M11启动时未冻结，本报告未读取、等待或接受其提交；图鉴交界直接按固定B/R审查。',
 '- 原函数、隔离验证、游戏、UI、编译、存档与完整Demo均 **NOT_EXECUTED**。资料可读不等于运行成功；本轮Python仅用于报告与锚点校验。',
 '- 仅写J目录；没有修改正式规格、参考、历史或共享聚合，没有提交/push、启动agent或实现框架。',
 '', '## 逐链结果','', '| ID | 有限链 | 状态 | 已有问题关联 |','| --- | --- | --- | --- |']
for r in records:report.append(f'| {r["id"]} | {r["title"]} | {r["status"]} | {", ".join(r["existing_finding_ids"]) or "无新增"} |')
report += ['', '## 关键归属与修订护栏','',
 'M01译文导入/占位、M02变量计时、M03冲浪残留、M04动态取图、M05主动PP资格、M06育种预算测试、M10通用输入竞争分别保持单一已有根因。消费端新增定位不增加finding数量。具体主责/消费者建议在shared-capabilities.json；这不是未来实现架构。',
 '', '**孵化护栏：**GIR-FD82-A053仅具名投影亲审。DEERLING存储形态0、2月、steps1、无强制形态且非战斗/储存，在前置媒体/消息正常时，先计数归0和核心写入，再由演出实参读取动态形态而提交1，随后才通常拥有/见过蛋。WP35§5.2、§9及EG-13/EG-20已经准确。M04建议删除WP18的图像泛称是相容的；不能把“参数式取图函数不自行求值”改写成“孵化调用者没有求值”。',
 '', '电话Default重复覆盖候选已完成全131正式材料同义反证，WP03/WP04/KR14–16/KL36已承接，故拒绝新增；具体检索在candidate-counterevidence.json。其余没有新增missing/contradiction裁决，不用该检索冒充131文件全新语义验收。',
 '', '## 每条亲审范围与证据','']
for r in records:
 report += [f'### {r["id"]} {r["title"]}', '',f'**结论：{r["status"]}。** {r["conclusion"]}', '',f'主责：{r["primary_owner"]}。',
 '生产者：'+'；'.join(r['producers'])+'。', '状态写入：'+'；'.join(r['state_writes'])+'。', '消费者：'+'；'.join(r['consumers'])+'。',
 '', '前提/配置：'+'；'.join(r['preconditions']+r['configuration'])+'。','',
 '| 边界 | 本次独立核对 |','| --- | --- |']
 for k,l in [('normal','正常'),('failure','失败'),('cancellation','取消'),('repetition','重复'),('ordering','顺序')]:report.append(f'| {l} | {r["boundaries"][k]} |')
 report += ['', '已审：'+'；'.join(r['reviewed'])+'。','未审：'+'；'.join(r['not_reviewed'])+'。','',
 '静态向量（均NOT_EXECUTED）：']
 for v in r['vectors']:report.append(f'- {v["id"]}：{v["input"]} → {v["expected"]}')
 report += ['', 'R源锚点（仅审计，不复制源码）：']
 for a in r['source_anchors']:report.append(f'- `{a["path"]}` L'+','.join(f'{s}–{e}' for s,e in a['line_ranges'])+'：'+a['fact']+'。')
 report += ['', 'B正式锚点：']
 for a in r['spec_anchors']:report.append(f'- `{a["path"]}` L'+','.join(f'{s}–{e}' for s,e in a['line_ranges'])+(' / '+a['section_or_test_ids'] if a.get('section_or_test_ids') else '')+'：'+a['fact']+'。')
 report += ['', '历史映射：'+', '.join(r['historical_junction_ids'])+'；仅对应本链投影，原范围不扩大。证据SOURCE_STATIC / SPEC_STATIC；脚本及选定PBS可读，图像/音频/地图/完整Demo缺项，显示/保存/恢复均未执行。','']
report += ['## 历史与交付边界','',
 'junctions.json的historical_coverage完整保留共享导航54 junction + 8 chain + 18 new chain各条原normal/failure scope、固定身份、原对象摘要及后继绑定。其整条status仍为not_reviewed；有本次有限投影的标historical_qualified_evidence_reused并列GR4-Jxx，其余not_reviewed。共享导航验证不转成语义通过。',
 '', 'GR3 CLOSED不重开；旧229/341的每条限定scope保留，A053也仅增加上述孵化投影；可选GR3-M09-001继续暂缓，GR4-M02-003依用户指令不需修订。没有新的GR4-J-001待质疑；已有模块问题的最终独立质疑/接受由父会话处理，本报告不替代该步骤。',
 '', '新游戏至保存继续只建立条件静态交接。真实起始队伍/图鉴/球授予、遭遇地图、接待事件和完整Demo缺材料，故J14为partial，不将工程缺项判成不存在能力，也不制造运行成功。',
 '', '产物：report.md、junctions.json、shared-capabilities.json、findings.json、execution.json、progress.md。附read-log.json、candidate-counterevidence.json与审计生成/校验工具，均位于J目录。']
(HERE/'report.md').write_text('\n'.join(report)+'\n')
(HERE/'progress.md').write_text(f'''# J 进度（已完成）

- 已读AGENTS.md与共享身份/readiness、冻结输入、计划、历史导航/旧投影绑定；不重做旧行政审计。
- 固定B/R直接审完14类有限链：supported {counts['supported']}、partial {counts['partial']}；全部行为验证NOT_EXECUTED。
- 新增J问题0，关联已有GR4问题{len(links)}；电话Default候选经全131同义反证已拒绝，既有准确合同保留。
- GIR-FD82-A053的DEERLING存储0、2月→1孵化消费者具名静态投影supported；M04修订不得倒退WP35/EG-20。
- 历史54+8+18原normal/failure范围/身份/指针保留，不冒80新PASS；GR3 CLOSED、旧229/341限定scope、可选GR3-M09-001暂缓、M02-003不需修订保持。
- M11未冻结报告未读、未等待、未接受；图鉴/可见点/捕获交界直接按固定源/规格独立检查。
- 六个要求产物已写；validation.json校验输出结构、锚点、历史绑定及记录数量，仅TOOL_VALIDATION。
- 仅写本目录；无正式/参考/历史/共享修改，无agent、提交、push或新框架实现。完成后结束。
''')
print(json.dumps({'records':len(records),'statuses':dict(counts),'new_findings':0,'existing_links':len(links),'historical':len(historical)},ensure_ascii=False))
