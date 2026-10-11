"""Report assembly for independently read static materials; no game behavior execution."""
from pathlib import Path
import json,csv,re,hashlib
OUT=Path(__file__).resolve().parent
ROOT=OUT.parent
REPO=OUT.parents[3]
REF_COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REF_TREE='7589c800b61ba13a13040ed0d686979b80a84fd0'
SPEC_COMMIT='167296dbe9e2384627b0ed696e87aeb01f211252'
SPEC_TREE='33598d8a2a3acdd093cc4fe23f48eea8666100f3'
source={x['path']:x for x in csv.DictReader((ROOT/'reference-file-inventory.tsv').open(),delimiter='\t')}
formal={x['path']:x for x in json.loads((ROOT/'formal-spec-identities.json').read_text())}
def dump(n,d): (OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def tsv(n,rows):
 with (OUT/n).open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
def sp(n):return 'deliverables/final-specification-set/creature-rpg/'+n
W24=sp('wp24-player-trainers-partners.md');W25=sp('wp25-party-and-storage.md');W26=sp('wp26-acquisition-gifts-and-script-trade.md');W27=sp('wp27-bag-and-item-storage.md');W28=sp('wp28-item-use-and-training.md');W29=sp('wp29-shops-and-exchanges.md')
U='Data/Scripts/013_Items/001_Item_Utilities.rb';E='Data/Scripts/013_Items/002_Item_Effects.rb';B='Data/Scripts/013_Items/003_Item_BattleEffects.rb';BAG='Data/Scripts/013_Items/008_PokemonBag.rb';ST='Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb';TR='Data/Scripts/015_Trainers and player/001_Trainer.rb';TL='Data/Scripts/015_Trainers and player/002_Trainer_LoadAndNew.rb';PL='Data/Scripts/015_Trainers and player/004_Player.rb';UP='Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb';UT='Data/Scripts/019_Utilities/001_Utilities.rb';PTY='Data/Scripts/016_UI/005_UI_Party.rb';TRADE='Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb';MART='Data/Scripts/016_UI/020_UI_PokeMart.rb';BP='Data/Scripts/016_UI/021_UI_BattlePointShop.rb';OW='Data/Scripts/012_Overworld/001_Overworld.rb'
# Each row reflects a substantive behavior family read by the independent primary reviewer.
F=[
('训练家身份/名称/随机双半',[TR],[W24],'§3.1','32位标识两个16位；外来生成重复排自身；NoName与完整显示；语言初始化不随UI改','SUPPORTED_STATIC','宿主语言实际值未采集'),
('队伍派生/可战斗/查询与治疗',[TR],[W24,W25],'§3.1;§3/5','非空/非蛋/able三个集合不同；first/last、种族形态属性招式、全队治疗；满按原长度>=6','SUPPORTED_STATIC','动态形态查询可有副作用，不能作纯缓存API要求'),
('成员移除与最后可用',[TR],[W25],'§4.1/5','索引边界和其它可用成员先验，成功delete压缩；盒直删不继承训练家门','SUPPORTED_STATIC','脚本其它入口不同；UI守卫M10'),
('训练家装载/缺失/检查/新建',[TL],[W24],'§5.2–5.3','未知类型装载报错/缺记录nil；非debug检查真，debug拒类型false；首成员强制录入、0..255首空版本','SUPPORTED_STATIC','交互写回和编译完整工具M12；未运行文件写入'),
('玩家初始化/功能许可',[PL],[W24],'§3.2/4.3','character0/outfit0/8false徽章/资源初始化/新Dex/功能false；构造初始钱直接metadata而写入器才钳','SUPPORTED_STATIC','剧情许可写入者缺地图；不将默认metadata价变为所有输入域保证'),
('资源四整数域与刷新副作用',[PL],[W24,W29],'§3.2/4.1','Integer验证后0..配置上限；outfit/character先写后刷新、同值不刷新；badges严格true计数','SUPPORTED_STATIC','初始化绕 setter 不构成源设计模板；地图刷新可失败'),
('角色切换/命名建议',[UT,PL],[W24],'§3.3;PT29–34','编号<1拒，缺编号回记录1；两次长度严格<10，最终完整用户名截断；取消空名走建议','SUPPORTED_STATIC','UT239–292实读；真实host用户名未知'),
('伙伴注册/阶段性失败',[OW,TL],[W24],'§6.1','先类型→取消载具→load→事件→owner重设→记录ID非version；nil队伍访问时已有载具清理保留','SUPPORTED_STATIC','OW635–657实读；事件异常GR3-M02-001，参与/战后完整caller M06/M07'),
('伙伴参与/道具再读/战后链',[TR,PL],[W24],'§6.2–6.4','身份ID作version再查询可能命中另一记录；可行性/参与谓词/恢复两个分支不同','PARTIAL','当前条款/限定FINAL已读，整体消费者M06/M07/M09独立审，不代签'),
('盒容量/空位/清空/直写',[ST],[W25],'§3.1–3.2','默认30/40，实际长度；clear后empty/full同时；显式写可覆盖扩展；party−1追加定位','SUPPORTED_STATIC','源数组组织仅取证，允许重设计'),
('复制同对象/移动删源/失败',[ST],[W25],'§4.1','party忽略目标格追加；box负索引扫描、正索引覆盖；空源入盒失败；成功复制后才删源','SUPPORTED_STATIC','非深复制，读写身份共享必须保留；UI中另一持有位门'),
('捕获入队/入盒/全盒扫描',[ST],[W25,W26],'§4.1/6','入队成功返回个体真值；入盒首空；store当前→0起，治疗先于找位，全满可已治疗','SUPPORTED_STATIC','接收/图鉴/战斗选择分别M06/M07/M10'),
('地区储存代理与错误',[ST],[W25],'§3.3','地图变重新地区缓存；无地图/地区报错；移动只复制、删除未定义、墙纸proxy缺方法','SUPPORTED_STATIC','仅机制；默认基础storage，动态使用/地图可达未证'),
('墙纸目录/显示写回',[ST],[W25],'§3.4;PS32–42','16+24目录/锁解；显示nil空不写，旧完整行text归整数、不可用回boxmod16写回','PARTIAL','ST领域全文；显示兼容caller由M10实核，素材缺失；C120旧有效限定复用'),
('普通/静默/仅队伍获得',[UP],[W26],'§3.1–3.2;AQ01–08,36','初满门先于构造；交互与静默不同Dex/消息/记录顺序；partySilent默认nil等级失败','SUPPORTED_STATIC','消息期间容量变为后复检前提，不假定所有运行环境能达'),
('外来赠送/蛋入口',[UP],[W26],'§3.2','外来仅队伍、替Owner/非空nickname截断、直接存储不询问；蛋改字段、创建form可先登记seen','SUPPORTED_STATIC','M04创建/M06孵化/M11Dex引用联合；未编译/执行内容'),
('命名存储复检与部分提交',[UP],[W26],'§3.3/7','3次容量检查；确认否保名、同意后空清；图鉴/名字先提交，内层拒不改外层true','SUPPORTED_STATIC','真实并行事件与演出依宿主/地图'),
('脚本交换/演出后提交',[TRADE,PTY],[W26],'§4;AQ19–27','统计最先、已有对象不reset、形态演出Dex和进化后才替换；旧成员不入箱，过程无取消入口','PARTIAL','TRADE217–251、PTY1172–1207/1534–1561实读，演出UI全过程M10，进化M06'),
('背包数量/纯预检/部分增删',[BAG],[W27],'§3.1–3.3;BG01–07','跨槽求和；无限仅length+1扫描；负quantity错误/0成功；直接不足保部分，all先预检','SUPPORTED_STATIC','TripleTriad相同helper消费者M11；不移植源容器'),
('口袋替换/游标/清空',[BAG],[W27],'§3.2/7','只旧口袋改ID不合并不验证新pocket；clear保登记/lastpocket；索引只上界可存负值','SUPPORTED_STATIC','完整UI游标竞争M10'),
('登记三层/快捷收集',[BAG,U],[W27,W28],'§5;§3.1/3.3','领域只合法去重，菜单资格处理器，图标重要；收集持有不再次资格；未持有登记保留','PARTIAL','M10快捷菜单完整输入；root核心机制全文，UI未单独全文再签'),
('PC种子/容量/存取丢弃',[BAG],[W27],'§4.1–4.3','999×999严格查询；metadata合法种子；取存先预检删再加，重要整叠/单数显示','PARTIAL','PC UI全部执行守卫由M10源全文；本root机制+完整正文/测试'),
('物品处理器10家族/返回域',[U],[W28],'§3.1','缺bag handler回野外1/0；confirm缺真，field缺−1，对个体缺假；maximum默认1配置门','SUPPORTED_STATIC','Registry条件lookup机制M01/M02限定；实际插件扩展未知'),
('背包/队伍/野外消费时点',[U,E],[W28],'§3.2–3.4','OnPokemon只非蛋队伍，handler真才消费；循环最后取消返回0但先效果不撤；field确认只快捷入口','SUPPORTED_STATIC','没有统一库存0门，直接调用不保证界面资格；消息等待宿主未证'),
('多量上限/效果/扣量三层',[U,E],[W28],'§3.2/5.3','handler原量→配置至少1→库存→选择；效果仅bool、先成功后触限真，外层扣传入量不退差','SUPPORTED_STATIC','qty0/负/插件坏数据不扩大正常合同'),
('HP族完整参数/状态复活',[U,E,B],[W28],'§5.1;IU01–06,51–53','请求20/真60假50等完整映射、比例floorH/4、满量封顶；战斗仅混乱可全治，复活半至少1','SUPPORTED_STATIC','主动与AI估量/持物分开；无真实治疗执行'),
('PP回复/成长/在场同步',[U,E,B],[W28],'§5.2','选招取消假、maxPP<=0失败；ELIXIR总增0失败；UP<=1/已3拒，未transform且ID同才在场同步','SUPPORTED_STATIC','同步时序全战斗由M07/M08'),
('EV维生素/羽毛/树果',[U,E],[W28],'§5.3;IU09–17,49–50','6项10/1、世代100门、252/510额度；树果max清EV份与友好份；逐份h与合并EV不同','SUPPORTED_STATIC','设施模板可255非全局存储上限；数学向量未运行'),
('21薄荷/能力胶囊药膏',[U,E],[W28],'§5.3;IU56','先相同性格拒/确认取消；只计算Nature；胶囊0↔1/药膏2，隐藏/无第二/ZYGARDE拒','SUPPORTED_STATIC','固定25性质由M04表N，不扩动态任意目录'),
('糖果/等级经验/进化取消',[U,E],[W28],'§5.3;IU18–19,54','五经验量100/800/3000/10000/30000一次合并；满级普通糖目标可取消但effect真仍消耗','PARTIAL','GR3-M06-001 经验差量消息先写入前；完整收益/成长M06，root源已完整读'),
('机器教学/PP/统计/首招',[U,E,UT],[W28],'§5.4;IU20–23,58','满槽遗忘、取消放弃，机器保旧PP门；背包TR包装计stat/add_first，party直接不计不加','SUPPORTED_STATIC','UT452–500实读；满槽/零招UI失败M10负责'),
('进化石与资格/消耗',[E],[W28],'§5.4','条件按flag，Shadow先拒，目标hit不可取消evolution，effect真外层消费；nohit失败','PARTIAL','M06完整全部evolution条件与提交；M05只道具边界'),
('14形态/融合工具合同',[E],[W28],'§5.6;IU44–48,57','种族/形态/HP门；第二目标自身蛋濒死错种拒，fused同引用移队、工具换ID、满队拆拒','SUPPORTED_STATIC','setForm让出→形态改招后的失败有既有先写状态；M04改招映射全读'),
('驱虫喷雾/耗尽/黑白笛',[E,U],[W28],'§3.3;IU37','100/200/250，ice不减，0后确认过滤再用；黑白互斥rate/level按配置；repeat拒','SUPPORTED_STATIC','全遭遇抽样消费者M06；不可由use真推战斗启动'),
('甜蜜/离洞绳/圣灰',[E],[W28],'§3.3;IU35,38–39','honey遇天气阻仍真；rope follower/点门，先传送后清点，后失败不回滚；ash逐治疗至少1真','PARTIAL','场地/世界传送全部caller M03/M11；媒体/地图缺失'),
('自行车/鱼竿/地图/硬币盒',[U,E],[W28],'§3.3/7','bike surfing/diving/地形/follower/alwaysbicycle门；鱼当前格出边；地图fly temp/状态不同；coins显示','PARTIAL','完整运动/钓鱼/地图UI M03/M10/M11，sourcehelper/handler全文已读'),
('探测仪搜索与响应',[U,E],[W28],'§3.3/4','同图事件含hiddenitem不区分大小写；dx<8 dy<6、自开关A未拾；Manhattan最短平局保先枚举；脚下4右转','UNRESOLVED','GR3-M05-002：当前只有功能名，完整过滤/响应参数未合同；真实地图/素材不可用'),
('经验共享标识开关',[E,BAG],[W28,W27],'§3.3/6.8','EXPALL/OFF原口袋换所有ID不移动合并，消息/真，实际经验资格消费者另规则','SUPPORTED_STATIC','defaultenable/插件组合未证'),
('战斗物品资格/效果/退款',[U,B],[W28],'§3.5','1/2/3存在门，4/5不同；可否默认真，登记扣、执行拒退而不清物品、成功清；球不退','PARTIAL','GR3-M07-001 同轮终局再退需WP28共同修改；M07/M10完整caller独立支持'),
('战斗增益/娃娃/雾/笛/球',[B],[W28],'§5.5','X6属性4档、基础+1/2；Mushrooms5项；Focus门/写2,2,3；Mist5；娃娃仅可逃野战；Soundproof门','SUPPORTED_STATIC','完整特性/战斗尾消费者M07/M08，球captureM06，不以handler返回推退款'),
('买卖价格/覆盖/库存别名',[MART,BP],[W29],'§3.1/5','买>0卖>=0覆盖，卖command×2/旧槽保留；同买槽BP共享；stock原地删重要已持有，退出不还','SUPPORTED_STATIC','MART1–215/579–760、BP1–100/419–560实读；非选定UI绘制由M10'),
('购买退款/赠品/售出先后',[MART],[W29],'§3.2–3.4/6','逐add全成stat→money→filter→msg→bonus；失败删已add，售money→actualstat→remove不检查','SUPPORTED_STATIC','赠品添加0仍来源显示0数量，不承诺跳消息；资源/宿主未运行'),
('BP兑换/显示半价与实扣',[BP],[W29],'§4;SH20–28','普通数量max floorBP/price≤999，显示qty×floorprice/2，确认与扣全价、统计→BP；无卖/赠品','PARTIAL','M10数量同时键GR3-M10-002；host未验证；价数据/断言失败范围有限'),
('平衡等级公共数学消费',[UP],[W24],'派生/跨域 WP36§6.2','含蛋濒死、人口σ与0.001/0.999分支、归一取整再+2/max；空与sum0直接1','PARTIAL','UP194–238全文；具体WP36/77由M06/M12共同签，当前不在W24重建公式'),
('个体尺寸辅助数学',[UP],[W24],'§3.1；WP18§3.2 height责任','PID低两byte、六原始IV低4位确定离散毫米输出，双整数阶段及14段/尾默认，無随机或状态写入','UNRESOLVED','GR3-M05-001：可得无静态调用者helper缺独立数学合同；不声称demo钓鱼使用'),
('物品图标/持物图标',[ 'Data/Scripts/013_Items/007_Item_Sprites.rb'],[W27,W28],'UI/资源交界','height48水平frames、1秒同步uptime、9原点、blankzero、换item资源释放；held随当前物品更新','PARTIAL','源全文，M10/M03资源UI总体；缺Graphics/真实帧渲染'),
]
rows=[]
for i,(name,ss,pp,cl,b,st,lim) in enumerate(F,1):
 rows.append(dict(capability_id=f'M05-C{i:03}',module='M05',category='Creature-RPG / Pokémon Rules / Combat / Engine/UI',capability=name,source_paths=';'.join(ss),source_loci='固定全文主源或file-coverage精确额外范围',spec_paths=';'.join(pp),spec_clauses=cl,test_design=cl+';BG/IU/SH/PT/PS/AQ设计，NOT_EXECUTED',normal_failure_boundary=b,status=st,limitations=lim))
tsv('capability-coverage.tsv',rows)
assigned=json.loads((OUT/'assigned-files.json').read_text());aset={x['path'] for x in assigned}
extra={UT:'239–292,452–500 named player/naming/teaching callers',OW:'635–657 partner registration; ground grants inherited finite M03/M11 evidence',TRADE:'217–251 script entry; presentation/Dex/evolution caller M10/M06',PTY:'1172–1207,1534–1561 trade chooser; remaining UI independent M10 scope',MART:'1–215 adapter/price and579–760 all transaction/domain/wrapper',BP:'1–100 adapter/price and419–560 all transaction/domain/wrapper'}
frows=[]
for p in sorted(aset|set(extra)):
 frows.append(dict(source_path=p,git_blob=source[p]['git_blob'],category='Creature-RPG / Pokémon / Engine/UI',read_scope='FULL_TEXT_READ' if p in aset else extra[p],status='SUPPORTED_STATIC' if p in aset and not p.endswith('Item_Sprites.rb') else 'PARTIAL',capability_ids=';'.join(x['capability_id'] for x in rows if p in x['source_paths'].split(';')),limitations='完整主源行为读；extra只是精确范围。运行/behavior case/realDemo均0，跨域全链独立join不代签。'))
tsv('file-coverage.tsv',frows)
# Reverse records include prose paragraphs/list items as well as named table rows/headings.
specs=json.loads((OUT/'assigned-specs.json').read_text()); extra_test='deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md'
specrows=[]
for ident in specs+[formal[extra_test]]:
 p=ident['path']; section=''; rel=[x for x in rows if p in x['spec_paths'].split(';')]
 if '/test-catalog/' in p: rel=rows
 for i,line in enumerate((REPO/p).read_text().splitlines(),1):
  if not line.strip() or line=='---' or line.startswith('| ---'):continue
  if line.startswith('#'):section=line.lstrip('# ').strip()
  key=line.split('|')[1].strip() if line.startswith('|') else (line.lstrip('# ').strip() if line.startswith('#') else section+' / paragraph or item')
  status='SUPPORTED_STATIC';lim='实际逐条正文/表族/静态设计读取，未执行。行为族及源范围见forward/file records。'
  if '/test-catalog/' in p:
   owned=(p==extra_test and (i>=88)) or (p!=extra_test and 5<=i<140)
   if not owned:status='NOT_REVIEWED';lim='CI/HP由M04、GR/DC由M06，M05未重复阅读/签其全文。'
  elif any(a in section for a in ['未决','未验证']):status='UNRESOLVED';lim='具名未知和宿主/资料边界保持，不由读文件消除。'
  elif p==W28 and ('主要野外效果' in line or 'ITEMFINDER' in line):status='PARTIAL';lim='GR3-M05-002 探测搜索/响应核心缺失，保留已述其它效果。'
  elif p==W28 and ('战斗上下文' in section or '战斗退回' in line):status='PARTIAL';lim='GR3-M07-001 执行退款与终局再次退款需联合合同；正常分支仍支持。'
  elif p==W24 and '派生查询' in line:status='PARTIAL';lim='GR3-M05-001 辅助尺寸可得但未定义；WP36已有平衡等级独立数学，不重复缺口。'
  elif any(p==v for v in [W25,W26,W27]) and any(a in section for a in ['界面','脚本交换','地区化','墙纸']):status='PARTIAL';lim='核心已读，完整显示/演出由M10，地区默认启用/host未证。'
  specrows.append(dict(spec_path=p,clause=f'line{i} {key}',source_paths=';'.join(sorted({s for x in rel for s in x['source_paths'].split(';')})),source_loci='细分主入口/参数见capability记录；extra caller范围见file记录',status=status,test_design='BG31/IU59/SH28/PT69/PS42/AQ36全部静态设计读取；NOT_EXECUTED',limitations=lim))
tsv('spec-coverage.tsv',specrows)
def evidence(p,loc,note,spec=False):
 x=formal[p] if spec else source[p]
 return dict(repo='y805939188/pokemon-essentials-clean-room' if spec else 'Maruno17/pokemon-essentials',commit=SPEC_COMMIT if spec else REF_COMMIT,tree=SPEC_TREE if spec else REF_TREE,path=p,git_blob=x['git_blob'],loci=loc,note=note)
findings=[dict(id='GR3-M05-001',severity='P3',status='CONFIRMED',disposition='REQUIRED_REVISION',title='可得个体尺寸辅助缺少独立毫米数学合同',module='M05',capability='个体尺寸数学辅助',category='Pokémon Rules / Demo-DX',reviewer='/root',source_evidence=[evidence(UP,'243–271','完整辅助数学已读；全432文件rg只有定义，无普通静态caller，不推出动态不存在')],spec_evidence=[evidence('deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md','§3.2 height/weight责任，line74；§6派生line275','只有物种0.1m/0.1kg字段，不是该个体毫米计算',True),evidence(W24,'§3.1 line54','派生查询未穷尽，完整131搜索未有该可得数学定义',True)],evidence_level='SUPPORTED_STATIC_SOURCE_AND_COMPLETE_SPEC_SET_REVIEW; NOT_EXECUTED',premises=['合法个体，物种height字段为7（0.7m）；六项原始IV均0，PID32位合法；只调用可得尺寸辅助，未运行游戏。','不把该入口当默认游戏/钓鱼使用，静态调用者未定位，真实Demo/外部调用未知。'],scenarios={'normal':'PID0给203mm；不抽随机、不改个体状态。','boundary':'PID2304（低byte0、高byte9）给209mm，PID2560（高byte10）给210mm；分段10边界不同。','reverse':'原始IV低4位和PID低两byte参与；EV/Nature/ivMaxed不是该规则输入。','execution':'NOT_EXECUTED; manual fixed arithmetic only'},current_vs_expected={'current':'只给物种高度/重量和未穷尽派生查询；不能从独立材料推导个体尺寸输出。','expected':'给出独立单位、位字段输入及组合数学、全部分段边界/比例和整数阶段、正常/边界向量；与物种高度展示区别。'},impact='从零实现会遗漏已可得数学辅助或用物种高度误当个体尺寸。',implementation_risk='单位、截断和阈值易产生不同结果；默认可达性未知，不夸大当前玩家受影响。',consumers=['外部事件/开发者辅助潜在使用；当前固定脚本仅定义','WP18个体信息与WP77/DX能力分母'],historical_relation='原229查尺寸相关为地图词法/显示，未见同一个体辅助根因；不重开旧控制。',recommendation='在适当个体或开发者行为合同补独立数学/参数表，不复制源表达式或强制源helper接口；明确静态无消费者和未运行。',acceptance_criteria=['允许材料独立推导203/209/210mm三个输入及全部分段两端。','明确原始IV/PID位输入与物种height单位，整数阶段；未把潜在调用写成已启用。'],dependencies=['M04 个体字段','M11/M12 外部/示例调用界限'],aliases=[],unknowns=['地图/Demo/插件调用者未得','原作者用途与未来是否保留该辅助需用户范围决策；规则文档可先补，不强制现代API'] ),
dict(id='GR3-M05-002',severity='P2',status='CONFIRMED',disposition='REQUIRED_REVISION',title='探测仪只列功能名，缺少搜索、方向与响应合同',module='M05',capability='野外探测仪及隐藏道具响应',category='Creature-RPG / Engine-Overworld / UI / Demo-DX',reviewer='/root',source_evidence=[evidence(U,'556–576','筛选同图事件、矩形排除/自开关A、Manhattan距离和平局'),evidence(E,'318–356','统计先增、音效请求、无结果/脚下/邻近三路、别名')],spec_evidence=[evidence(W28,'§3.3 line84；§4目录line131','仅打开对应功能/登记身份，未定义可得算法和响应',True),evidence('deliverables/final-specification-set/generic-kernel/wp06-stats-directory.md','line40 itemfinder_count','只给次数来源，不是搜索/响应合同',True),evidence('deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md','§4 item/hiddenitem转换','作者生成事件是上游，未承接探测搜索/时序',True)],evidence_level='SUPPORTED_STATIC_SOURCE_AND_COMPLETE_SPEC_SET_REVIEW; NOT_EXECUTED',premises=['玩家/当前地图/事件集合/自开关有效；名称含hiddenitem不区分大小写；媒体/转向等待正常返回，无额外回调改变地图或玩家。','隐藏道具事件可以是合法作者夹具，真实地图缺失，不宣称默认Demo可达。'],scenarios={'normal':'玩家(5,5)，候选(7,5)与(5,7)均未拾、名称匹配；两者Manhattan2，按当前事件枚举先者选；水平距离与垂直距离相等时朝垂直方向。','failure':'无候选或候选自开关A真：使用统计先+1，音效请求后无响应消息，效果仍真；不拾取任何物品、不写A。','boundary':'dx绝对7/dy5可入，8/6排除；同格候选先每0.2秒右转90度共4次，再等0.3秒脚下消息；近处转向后等0.3秒两段消息。','execution':'NOT_EXECUTED_STATIC_SCENARIOS'},current_vs_expected={'current':'功能列名不能确定哪些道具能被探测、多个目标如何选择、失败是否成功使用、角色方向/统计先后。','expected':'独立候选过滤/距离/平局、三路响应、请求和等待单位、统计与返回/消费交界，保持无实际拾取。'},impact='开发者可能使探测全图/已拾取道具、随机选平局目标或失败不统计；玩家方向与消息行为不同。',implementation_risk='事件身份和编译简写的上游规则、响应下游等待/使用返回容易遗漏。',consumers=['WP75隐藏道具事件生成','WP13事件/自开关与玩家转向','WP06次数统计','WP27/28快捷/背包使用','M10消息/等待，M11世界活动'],historical_relation='旧C103/C120为其它状态写入，未同根；旧候选不作为通过或新证据。',recommendation='补净室行为表/状态次序与具名正常、无目标、阈值、平局、脚下反例；保留资源/宿主未知。',acceptance_criteria=['上述候选窗口/已拾过滤/两距离及枚举平局可从最终合同唯一推出。','三路统计/返回/方向/时序及不自动拾取都明示；无真实运行签名。'],dependencies=['M03地图事件/转向','M10消息/等待','M12隐藏道具作者转换'],aliases=[],unknowns=['真实地图/媒体/时序运行未证','动态事件枚举实现组织自由，但平局外部次序须说明兼容策略'])]
dump('findings.json',findings)
f1path='review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/all229-dispositions.json'
f1=json.loads((REPO/f1path).read_text())['records'];idx={x['id']:(i,x) for i,x in enumerate(f1)}
regs=[]
cross={'GIR-FD82-A034','GIR-FD82-A047','GIR-FD82-A052','GIR-FD82-A059','GIR-FD82-B020','GIR-FD82-C003','GIR-FD82-C103','GIR-FD82-C120','GIR-FD82-D023'}
for c in json.loads((OUT/'regression-controls.json').read_text()):
 i,old=idx[c['id']];sem={k:v for k,v in old.items() if any(t in k for t in ['normal_reverse','normal_static','reverse_and','partial_failure'])}
 exclusions=[]
 if c['id']=='GIR-FD82-A059':
  exclusions=['FINAL1 neighboring_reverse 的“无记忆Q设置timer”不复用：参考是取消既有待播计时；当前WP24/PT58已经正确，不重开旧CLOSED。']
 regs.append(dict(id=c['id'],reviewer='/root',status='PARTIAL' if c['id'] in cross else 'SUPPORTED_STATIC',actual_read_scope='approved有效前提/反例/minimum/recheck/root与相关M05 extension；M04已独立读过的A020/A026/A036/A037/A040资格有限复用。C003只签A23域内恢复，不代签4root/8extension；其余交由对应模块。FINAL相应normal/reverse/partial语义实际读取。',historical_reuse={'commit':'c2bc1a341ba6acdf7c8c111dc88d39a162a093d6','path':f1path,'pointer':f'/records/{i}','record_sha256':hashlib.sha256(json.dumps(old,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'basis':'完整批准/FINAL身份已核；当前131不变，各scope限定，不转授签名'},historical_semantic_scope=sem,explicit_reuse_exclusions=exclusions,current_spec_paths=[W24,W25,W26,W27,W28,W29],new_finding_relations=['GR3-M07-001 related independent terminal refund counterexample; B008 existing family existence scope retained'] if c['id']=='GIR-FD82-B008' else (['GR3-M06-001 independent EXP message/order, not A047 reopened'] if c['id']=='GIR-FD82-A047' else []),execution='NOT_EXECUTED',limitations='跨域消费者/宿主/资源/动态及历史原状态保留；不以本模块签全部旧控制'))
dump('regression-review.json',regs)
dump('reuse-qualification-corrections.json',[{'historical_id':'GIR-FD82-A059','pointer':f1path+'#/records/'+str(idx['GIR-FD82-A059'][0])+'/normal_reverse_partial_failure_review/neighboring_reverse','excluded_text':'无记忆Q设置timer','current_contract':'WP24 §5.4/PT58 明确取消既有待播计时并记Q/0','decision':'旧句不作为复用基础，保留原资料/裁决；当前正式未错，不另增必修ID。','reviewer':'/root'}])
assigned_j=(OUT/'assigned-junctions.tsv').read_text()
(OUT/'junction-review.md').write_text('# M05 独立交界 review\n\n实际 reviewer /root；固定身份见baseline及各证据blob。输入导航不是判断，现有交界标识如下：\n\n'+assigned_j+'\n\n以下均静态，行为/游戏/案例/Demo执行0。\n\n1. 内容/配置→Item identity→handler→使用：主源全部读；未知合法身份/缺handler与4/5默认放行分开。正常HP/PP/培养全参数已对表，数量取消不写、部分成功扣qty不退差。GR3-M07-001要求WP28退款路径与终局联合改，保留B008当前存在性正确。\n2. 玩家/伙伴→容量→普通/静默接收→Dex：正常先容量再构造、同对象追加/盒扫描，静默满队不混消息；消息等待期再次变全满，内层拒但外层true、较早Dex/昵称保留。创建蛋的form登记由M04/M06/M11各自承接，不写成整个路径无Dex。\n3. 盒/队伍/UI→同对象/持物：领域复制到队伍追加，UI守卫按持有/格/可用成员区分；GR3-M10-001的cached held item与BoxLink修改必须把领域给予/移出源状态共同解释，不能用“正常最后索引未变”排除合法二次操作。源source持物工具、完整WP25/26与M10独立具体链join。\n4. 减/增经验→消息→写经验→UI：GR3-M06-001已由root源223–327及WP30§5.2定点独立支持。同等级也消息先于写，不是旧A047份额数学；M05糖果与M12调试共同回归。\n5. 金钱/BP→购买/销售→背包→stat：正常买逐件全成功才stat→扣钱→过滤库存，失败撤已add，售先钱再删物，不虚构统一事务；价格覆盖旧槽保留/BP共享/退出清。M10数量同时键的差异另记GR3-M10-002不吞本域资源合同。\n6. 寄养/捕获/净化/礼物→接收：M05只完整接收工具和限定旧有效前提；各端入口M06/M07/M11/M04，真实maps/host为缺项，不能由同一接收helper推所有调用前置门相同。\n7. 新交界：GR3-M05-002 hiddenitem事件生成→探测过滤→玩家转向/消息/stat；GR3-M05-001纯个体尺寸数学→潜在作者辅助，当前仅定义无静态caller，不编造Demo。\n8. 历史复用纠正：FINAL1 A059“设置timer”邻接句不复用，当前formal正确取消timer；仅记录历史scope排除，不修历史/重开旧状态。\n')
counts={s:sum(x['status']==s for x in rows) for s in sorted({x['status'] for x in rows})}
(OUT/'report.md').write_text(f'''# M05 玩家、集合与资源操作独立评审

实际 reviewer：独立主会话 /root，入口 codex://threads/01a12bbf-9300-7833-82d7-d392ae9fa731；未参与正式作者/登记。model请求 gpt-6.1-sol/ultra/Standard(default)，回显 UNVERIFIED。固定交付/正式/reference commit/tree见baseline，所有输入只读。

有限静态范围已完成：{len(rows)}行为族（{json.dumps(counts,ensure_ascii=False)}），10分配主源全文及6额外caller的明确范围；6正式正文全文及第7测试BG31/IU59/SH28，额外PT69/PS42/AQ36全文。CI/HP/GR/DC未由M05重复全读，分别M04/M06责任。不是全内容表、实际启用、宿主或真实Demo通过。

新增2项：GR3-M05-001/P3 可得无静态caller的尺寸毫米数学漏项；GR3-M05-002/P2 探测仪搜索与三路响应合同漏项。完整前提、blob/条款、反例、结束条件见findings.json。M06经验提示、M07退款、M10持物/UI竞争是关联新ID，未复制为M05发现。核心资格、数量、取消、已有部分提交及数学参数与现有条款大部分支持，未把源对象组织提升成未来框架架构。

25旧控制全部具名记录；16本域SUPPORTED_STATIC、9跨owner PARTIAL；有效前提、反例、最低修订/确定复核与相关extension实际消费，M04此前同root实读按精确身份复用。原229关闭/341 scoped贡献没有回写。FINAL1 A059一条“设置timer”邻接文本与当前source/formal相反，剔除该句复用，保留历史完整记录/其它有效basis，不新增正式错误。

净室检查：正式6文说明数据标识不强制API，行为/表/数学而非源翻译；地区代理、容量及来源对象身份仅保外部语义。报告不复制源码；本构建器只是产物索引汇编，没有游戏行为实现。所有静态测试设计仍NOT_EXECUTED。游戏、参考执行、行为/静态案例执行、真实Demo链均0；文件/JSON/Git/hash核验不计为行为。

限制落到具体族：故事许可/伙伴特殊模式/地图事件/礼物实际发放、媒体/帧响应/主机语言、地区储存实际使用、动态插件、完整PBS内容语义与运行编译未证。尺寸辅助无静态caller，探测仪真实地图不可得；保留这些能力的可得静态核心，不从素材缺项推能力不存在。逆向条款/表/段与forward机制见spec-coverage.tsv、capability-coverage.tsv；交界与对应其它reviewer见junction-review.md。
''')
print(json.dumps({'capabilities':len(rows),'files':len(frows),'spec_records':len(specrows),'findings':len(findings),'regression':len(regs),'counts':counts},ensure_ascii=False))
