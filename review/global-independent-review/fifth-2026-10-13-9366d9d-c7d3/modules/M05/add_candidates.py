import review_state as s
from copy import deepcopy
D=s.load('findings'); template=D['findings'][0]
P='deliverables/final-specification-set/'
def src(path,a,b,symbol,fact,caller):return {'path':'Data/Scripts/'+path,'version':s.R,'lines':[a,b],'symbols':[symbol],'caller/config':caller,'supporting_facts':fact}
def sp(path,sec,a,b,fact):return {'path':P+path,'version':s.B,'sections':[sec],'lines':[a,b],'current_statement':fact}
def neg(path,a,b,result):return {'path':path,'read_ranges':[[a,b]],'result':result}
def base(n,title,root):
 q={k:deepcopy(template[k]) for k in ['module','severity','disposition','status','reviewer','source_baseline','specification_baseline','evidence_level','execution_status','confidence','user_decision_needed','review_resolution']}
 q.update(id='GR5-M05-'+str(n).zfill(3),title=title,category='cross_module_semantic_contradiction',root_cause_group=root,priority='P2',history_links=[],related_findings=[])
 return q
q=base(2,'融合第二成员选择允许盒子重入，最后可用成员移除失败后仍提交融合与工具替换','M05.fusion-selection-storage-reentry')
q['source_anchors']=[src('016_UI/005_UI_Party.rb',746,800,'pbChoosePokemon','SPECIAL允许访问盒子；仅canswitch==2禁用，普通融合调用使用缺省0','已打开允许BoxLink的主队伍界面'),src('016_UI/005_UI_Party.rb',1204,1218,'pbPokemonScreen','has_box_link或POKEMONBOXLINK且开关35关/地图未禁用时场景保存允许访问盒子','默认主队伍菜单'),src('016_UI/005_UI_Party.rb',1394,1405,'party_menu_item/use','在打开背包前保留选中成员对象，使用工具收到同一对象','主队伍Item→Use'),src('013_Items/002_Item_Effects.rb',1291,1524,'fusion families','全部四融合入口保留主体对象；选出对方后写fused、调用移除并忽略真假；随后替换工具','DNASPLICERS为最小反例，其余同型'),src('015_Trainers and player/001_Trainer.rb',116,125,'remove_pokemon_at_index','删除候选以外不存在可用成员即返回假，不删除','嵌套盒子操作可使候选成为最后可用'),src('016_UI/017_UI_PokemonStorage.rb',1500,1693,'pbStartScreen/Move mode','BoxLink开启的是可移动成员模式；存主体时另一合法存活成员仍在队伍，最后可用守卫允许','空盒位、主体无邮件且可存放')]
q['spec_anchors']=[sp('creature-rpg/wp28-item-use-and-training.md','§5.6融合表',255,277,'成功融合把对方从队伍移出并写入fused，工具变已用；表未限定第二选择期间不能进入盒子'),sp('creature-rpg/wp25-party-and-storage.md','§3.1/§5最后可用门',43,58,'删除时须保留其它可用成员；此底层门正确'),sp('user-interface/wp66-a-party-and-summary-ui.md','§3通用选择/§4物品',48,113,'BoxLink与选择入口已列，但未承接融合中主体可离队及移除失败后提交'),sp('test-catalog/creature-rpg-wp27-28-29-30-33.md','IU45–48/IU57',89,103,'只给未变更选择、取消、满队拆分与正常成功，无嵌套变更反例')]
q['expected_reference_behavior']='从允许BoxLink的主队伍Item→Use开始，普通存活KYUREM与RESHIRAM两人；第二成员选择时将KYUREM存入盒子，回选择RESHIRAM。保留的KYUREM对象仍被设形态1并写fused=RESHIRAM。删除RESHIRAM因它是队伍最后可用成员失败，但失败被忽略；工具仍替换为已用，效果真。最终盒中的KYUREM引用仍在队伍中的同一RESHIRAM。'
q['current_spec_behavior']='WP28成功表给对方已移出队伍的输出；没有允许主体离队后删除失败但仍成功的分支。'
q['gap']='把选择开始时的队伍关系延续到提交；没有组合通用选择的盒子重入与独立删除守卫。'
q['preconditions']=['R固定、默认世代8、无插件；普通非蛋非Shadow存活KYUREM0与RESHIRAM0两成员，主体未融合','BoxLink许可成立、开关35关、地图无DisableBoxLink；盒有空位，KYUREM可存放且无邮件','DNASPLICERS1；前后形态处理、消息、刷新正常；只进行下述嵌套移动']
q['minimal_counterexample']={'initial_state':'party=[K,R]；K.fused为空；盒空位；DNASPLICERS1','input':'主队伍选K→Item/Use/DNASPLICERS→第二成员选择按SPECIAL进盒→存K→回选择R','final_observable_state':'party=[R]；盒中K形态1、K.fused与R同一对象；DNASPLICERS0、DNASPLICERSUSED1；效果真'}
q['normal_case']='同起点不进盒子直接选R：K仍在队伍且可用，R成功删除，party=[K]、K.fused=R、工具已用。'
q['failure_or_boundary_case']='进盒子后取消第二选择：融合效果假且工具不替换，但已存入盒子的K不自动返回队伍；BoxLink禁用时不可经此普通UI重入路径。'
q['impact_on_independent_implementation']='照当前成功表实现强制移除或事务回滚，会失去参考的同对象双重可达状态；也会误判取消必定保持原队伍。应先记录参考再另定未来兼容政策。'
q['negative_evidence_search']=[neg(P+'creature-rpg/wp28-item-use-and-training.md',1,346,'全文已读；融合输出没有移除失败分支'),neg('specs/creature-rpg/wp28-item-use-and-training.md',1,389,'原稿全文同一成功表，无独有嵌套规则'),neg(P+'creature-rpg/wp25-party-and-storage.md',1,218,'删除守卫有明确合同；不保证caller检查结果'),neg(P+'pokemon-rules/wp21-dynamic-forms-and-display.md',1,327,'完整形态提交与异常表不覆盖存放中的选择状态变化；不禁止盒中setForm'),neg(P+'user-interface/wp66-a-party-and-summary-ui.md',1,259,'完整选择/物品/连续状态和向量，未承接本融合重入'),neg(P+'user-interface/wp66-b-storage-and-pokedex-ui.md',1,123,'存放守卫允许仍有可用R时存K'),neg(P+'test-catalog/creature-rpg-wp27-28-29-30-33.md',41,120,'IU全59与主动PP补充已读；没有本分支'),neg('review/remediation/20261003-prepare/batches/B16/author-draft-1/traceability.json',1,1,'已读相关具名控件有效约束/目录；仅静态补充，不改变融合移除检查；JSON范围以已读控制ID而非此占位行定位')]
q['proposed_spec_change']='WP28融合表增加第二选择中盒子重入与移除失败输出；取消只保证不新增融合/库存替换，不撤销已完成盒子移动。给正常/重入成功/重入取消对照，UI与WP25以唯一共享合同引用。'
q['affected_files']=[P+'creature-rpg/wp28-item-use-and-training.md',P+'user-interface/wp66-a-party-and-summary-ui.md',P+'test-catalog/creature-rpg-wp27-28-29-30-33.md']
q['shared_contracts']=['party.selection-reentry','party.last-able-removal','item.fusion-commit']
q['acceptance_criteria']={'static_required':['复核主队伍保留对象→SPECIAL盒子→选对方→setForm→fused→删除假→替换工具顺序','明确同一对象别名与持久队伍/盒子结果，不能只写泛化异常','正常不重入与禁BoxLink、嵌套后取消对照'],'execution_required':[],'execution_boundary':'NOT_EXECUTED；运行另报父会话'}
q['dependencies']=['WP21形态提交','WP25删除/存放','WP66-A选择','WP28工具身份替换'];q['related_capabilities']=['item.fusion','party.storage'];q['batch_owner']='M05业务；M10界面投影'
q['unknowns']=['未运行宿主交互；按前序UI成功返回前提作静态链','其它主体/融合目标组合未声称每种都同终态'];q['excluded_claims']=['不声称引用被复制成新个体','不声称全队变空','不要求未来复现漏洞或修改R']
D['findings']=[x for x in D['findings'] if x['id']!=q['id']]+[q]
q=base(3,'盒中摘要给予邮件时邻接快照来自玩家队伍，现行“持有者之后成员”合同缺少上下文索引','M05.mail-snapshot-caller-index')
q['source_anchors']=[src('016_UI/017_UI_PokemonStorage.rb',1247,1260,'pbSummary','盒中摘要传完整盒与盒子索引，持有位摘要传单元素数组和0','正常盒子Summary'),src('016_UI/006_UI_Summary.rb',1195,1229,'pbOptions','Give item传当前摘要索引；过滤允许可持有邮件','普通非蛋目标'),src('013_Items/001_Item_Utilities.rb',781,819,'pbGiveItemToPokemon','无旧持物时写信使用调用者索引，成功后设持物并消费','正常给予新邮件'),src('013_Items/006_Item_Mail.rb',100,125,'pbWriteMail','poke1/2总从玩家队伍索引+2/+1取；poke3取实际目标，不读取摘要容器','盒子索引0时取party2/party1')]
q['spec_anchors']=[sp('creature-rpg/wp64-mail-and-mystery-gift.md','§2.1/§2.2',25,33,'快照称持有者在队伍中之后第二/第一成员，未定义不在队伍的持有者'),sp('user-interface/wp66-a-party-and-summary-ui.md','§4.4/§5摘要给予',95,160,'统一快照次序与摘要Give转交通用给物，没有索引上下文差异'),sp('user-interface/wp66-b-storage-and-pokedex-ui.md','摘要共享消费者',1,123,'盒中摘要仍可给予邮件的合同，与“持有者之后”不存在统一队伍定位'),sp('test-catalog/creature-rpg-wp35-36-57-64-68.md','MG01',96,96,'只给队伍持有者后第二/第一/自身样本')]
q['expected_reference_behavior']='盒0格0普通空手成员B在摘要Give新图标邮件，玩家队伍[A,C,D]。写作完成时poke1取D、poke2取C、poke3取B，即使B不在玩家队伍；盒子邻居不参与。若盒索引+1/+2超出队伍长度，相应快照为空。'
q['current_spec_behavior']='快照统一以持有者在队伍的位置描述；无法确定盒中或持有位摘要目标的另外两项。'
q['gap']='共用写信工具的数值索引被解释成始终是实际持有者队伍位置，丢失合法caller中的盒索引/单元素索引。'
q['preconditions']=['固定R默认GRASSMAIL1，B普通非蛋、无持物无邮件且在盒0格0','玩家队伍至少三个普通成员A/C/D，盒子Summary正常打开','Give选择GRASSMAIL并输入非空消息；UI、数据解析正常，无插件改写']
q['minimal_counterexample']={'initial_state':'party=[A,C,D]；box0[0]=B且B不在队伍；bag.GRASSMAIL=1','input':'盒子B→Summary→Give item→GRASSMAIL→非空消息','final_observable_state':'B仍在盒中，持GRASSMAIL且mail快照[D,C,B]；背包-1；不读box0[1/2]'}
q['normal_case']='普通队伍索引0的A经Give写信，快照仍[D,C,A]，与当前队伍案例一致。'
q['failure_or_boundary_case']='盒中索引>=5且玩家队伍上限6时poke1/2都不存在；持有位单元素摘要索引0仍读取party2/party1；取消不产生新快照。'
q['impact_on_independent_implementation']='独立实现可能改取盒内邻居、按目标重新找队伍位置或填空，都会改变邮件图标内容；需要明确每种caller的快照输入合同。'
q['negative_evidence_search']=[neg(P+'creature-rpg/wp64-mail-and-mystery-gift.md',1,161,'全文及MG目录定义统一队伍相对位置，无盒索引'),neg('specs/creature-rpg/wp64-mail-and-mystery-gift.md',1,193,'原稿同样描述，无净化遗漏反证'),neg(P+'user-interface/wp66-a-party-and-summary-ui.md',1,259,'完整给物、邮件、摘要与连续状态，没给盒索引快照'),neg(P+'user-interface/wp66-b-storage-and-pokedex-ui.md',1,123,'盒子摘要持物可改，未更改写信快照源'),neg(P+'user-interface/wp66-b-storage-and-pokedex-ui.md',219,271,'尾部不变量/测试/补充无此例外'),neg(P+'test-catalog/creature-rpg-wp35-36-57-64-68.md',92,127,'MG01–32无盒索引对照'),neg(P+'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',1,1,'前窗已全文读取A01–41/B01–39/C01–36及相关B16行；仅局部组范围，不声称整个混合目录已审')]
q['proposed_spec_change']='在WP64定义快照的玩家队伍基准与调用者所传索引：普通队伍位置、盒子位置、持有位单元素0；WP66-A/B共享引用。补盒索引0、有/无队伍邻位与普通队伍对照。'
q['affected_files']=[P+'creature-rpg/wp64-mail-and-mystery-gift.md',P+'user-interface/wp66-a-party-and-summary-ui.md',P+'user-interface/wp66-b-storage-and-pokedex-ui.md',P+'test-catalog/creature-rpg-wp35-36-57-64-68.md'];q['shared_contracts']=['mail.snapshot-input-context','summary.give-held-item']
q['acceptance_criteria']={'static_required':['盒Summary传参→摘要索引→给物→写信四跳完整复核','快照三项指向明确，不以源类或方法结构规定未来实现','正常队伍、盒子与持有位索引分别列向量'],'execution_required':[],'execution_boundary':'静态限定；无媒体/宿主运行确认'}
q['dependencies']=['WP64快照','WP66-A摘要','WP66-B盒子'];q['related_capabilities']=['mail.snapshot','held-item.give'];q['batch_owner']='M05邮件业务；M10摘要消费者';q['unknowns']=['真实图标视觉输出未运行'];q['excluded_claims']=['不扩大为所有盒子Item快捷菜单都能给予邮件：此为Summary路径','不要求复制源代码或具体容器结构']
D['findings']=[x for x in D['findings'] if x['id']!=q['id']]+[q]
# Remove placeholder numeric ranges in bounded JSON/catalog entries; preserve exact logical ranges.
for f in D['findings']:
 for x in f.get('negative_evidence_search',[]):
  if x.get('read_ranges')==[[1,1]]:x['read_ranges']=['logical controls/catalog groups explicitly named in result; no whole-file claim']
s.save('findings',D)
