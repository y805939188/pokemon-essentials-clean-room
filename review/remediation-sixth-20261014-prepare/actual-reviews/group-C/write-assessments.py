"""Persist the reviewer's manual source/prose judgments; never run behavior vectors."""
import json
import pathlib
import importlib.util

spec = importlib.util.spec_from_file_location('review_identity_helper', pathlib.Path(__file__).with_name('assemble-evidence.py'))
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
ACT, PREP, PREFIX, OLD_REVIEW, OLD_DIR, OUT = (getattr(helper,k) for k in ['ACT','PREP','PREFIX','OLD_REVIEW','OLD_DIR','OUT'])
blob, identity, write = helper.blob, helper.identity, helper.write

F = 'deliverables/final-specification-set/'
DX = F+'test-catalog/demo-dx-wp72-73-74-75-76-77.md'
K = F+'test-catalog/generic-kernel-wp02-03-04.md'

# Entries are independently reasoned observations, including reverse/cancel/failure
# boundaries. The exact frozen acceptance wording is attached below by identity.
MANUAL = {
'R6-B-001':('局部图块集诊断与无效 tile 诊断分开',
 ['004_Compiler_MapsAndEvents.rb:293–323,348–400,1625–1751','001_Compiler.rb:1101–1115'],
 ['wp75-project-conversion-and-authoring-tools.md §10/§15.1','CV-M24'],
 ['有效地图5/10×10/(2,3)，编号读取正常为7；缺对象或属性访问抛可局部捕获异常，只构造tileset7/map5，未到坐标/层查询。',
  '表访问成功且顶层非空tile通行条目无结果，构造map5/(2,3)/一基层3；合法tile不产生这两类异常；属性只正常返回nil不保证第一种诊断。',
  '活动柜台查询到达该访问；停用通道不能代证活动性。首个异常中止驱动，已保存先前图不回滚；外层打印/清理不补局部坐标。']),
'R6-B-002':('生成售货提示先于接收入口',
 ['004_Compiler_MapsAndEvents.rb:139–181,1192–1223,1683–1751','003_Interpreter.rb:84–136','004_Interpreter_Commands.rb:162–209,656–661,1168–1179','001_Overworld.rb:706–736'],
 ['wp75-project-conversion-and-authoring-tools.md §8.3','CV-M11','wp27-bag-and-item-storage.md §7','wp29-shops-and-exchanges.md §3.2/§6.2','wp17-messages-windows-input.md §7'],
 ['独立最小有效页面、注册POTION、单行正常生成提示、初钱1000/数量0、可放1、无并行/插件/重入：免费提示调用时1000/0，收费200时800/0；此时接收脚本尚未执行。',
  '继续到接收自身获得消息时仍数量0；add及后续消息成功后1。生成提示失败前缀：收费仍800/0，免费1000/0；没有退款/提前入包/整体回滚。',
  '容量或金额拒绝不扣钱、不接收；ASCII括号逗号/大小写/非负价/首行门保留；没有购买事务取消。原＋不强判字面反序，WP29普通商店先物后钱不转授本入口。']),
'R6-DX-E001':('物种实际 Types 使用一般池',
 ['008_Species.rb:113–147,175–221,392–453','002_Editor_DataTypes.rb:496–523,1040–1182,1624–1706','001_Editor_Utilities.rb:116–155','001_EditorScreens.rb:926–987','002_Compiler_CompilePBS.rb:292–330','003_Compiler_WritePBS.rb:174–223','001_Pokemon.rb:313–334'],
 ['wp73-a-content-editors.md §3.5/§4.4','CE-M15/CE-M19/CE-TYPES-01–06'],
 ['有效S原[NORMAL]，添加FIRE/WATER、Apply Yes再父Yes，各写出成功：工作槽/登记/dat/基础PBS保留三项顺序，直接个体types完整副本、成员判断能命中第三项；不授全部三类型战斗效果。',
  '注册伪类型P在一般池可选；专门单引用选择器排P，双槽控件独立。重复添加只定位，改成其它位置已有值删当前项；Types不自动排序。',
  'Apply No/父No不提交新增表；两种Cancel回编辑。原共享[NORMAL,FIRE,NORMAL]打开即去重，No不撤销原地变化，也不新增文件。登记后dat失败/档案后PBS失败各保留前缀。',
  '实际字段绑定逐项核：Types/EggGroups/Abilities/HiddenAbilities不重复不自动排序；Tutor/EggMoves不重复、入口ID序/刷新名称序；Offspring和三档野生持物允许重复不排序。进化投影空表与父层保存门保持；UI Happiness255不替PBS接受256。']),
'R6-DX-E002':('WE-M20 基础记录输出主体正确',
 ['003_Compiler_WritePBS.rb:291–351','010_SpeciesMetrics.rb:1–101','004_EditorScreens_SpritePositioning.rb:1–136'],
 ['wp73-b-world-editors.md §7.5','WE-M20','KL23–KL26'],
 ['仅基础后缀s改A→B：档案B、无PBS路径、旧s仍A；同后缀基础B/不同非零D：选s、两节输出。',
  '同后缀基础B/相等非零B：选s、基础节输出、仅非零节省略；不同后缀基础s/非零t：仅选t，不改旧s。保存时判断五组相等，不用修改前相等。',
  '懒查询整条缺失非零克隆基础并带空后缀、可增默认路径；已有部分形态按自身默认，不逐字段继承。No重载、Yes档案→PBS、后段失败无总回滚、已有布局不广播重定位。只修目录主体，正文旧正确条件未被重写。']),
'R6-DX-DEBUG-001':('反馈使用请求数量，部分添加仍可能发生',
 ['002_Debug_MenuCommands.rb:778–827','008_PokemonBag.rb:1–301'],
 ['wp72-debug-contexts-and-controls.md §5.2','DG-M11/DG-M30/DG-U08-01–04','wp27-bag-and-item-storage.md §3/§7'],
 ['一槽/单槽999合法POTION，空请求2→实入2/true/消息2；998请求2→实入1至999/false/消息2且不走成功排序；999请求1→入0/false/消息1。',
  '列表取消或数量BACK0不添加、无给予消息；添加后消息失败保留已入量。无限口袋原999请求1可扩槽全入；填包先清、重要各1/其余3并保留容量跳过门。',
  '没有预检或返回值检查，也没有部分失败退款/回滚。U14复数名独立默认/语言命中不改变反馈数量或赋予成功条件。']),
'R6-DX-DEBUG-002':('warp 同步刷新与独立刷新请求分开',
 ['002_Debug_MenuCommands.rb:11–39,198–206','002_Scene_Map.rb:1–252','004_Game_Map.rb:429–489','011_Messages.rb:18–20,640–683'],
 ['wp72-debug-contexts-and-controls.md §2.3/§3.2','DG-M05/DG-U08-05–08','wp17-messages-windows-input.md §7.2'],
 ['地图与非地图转移正常后，末尾直接refresh依地图事件E1/E2→公共C1/C2完成本次计数各＋1，清need_refresh，再返回true关闭；转移内部其它刷新不并入本次。',
  '独立Refresh map只直接置请求true；必须在消息尚未提供地图更新机会时观察。消息微更新本身可消费请求，所以真实效果返回时不保证仍true/计数旧。这是源约束下消解冻结向量过强观察点，不漏验或拒绝源事实。',
  '选择取消返回false不转移/末尾刷新；E1完成而E2抛错保留转移、释放及E1，公共事件未到，清标记与true返回不保证。']),
'R6-DX-DEBUG-003':('F9 新登记与旧请求消费分两阶段',
 ['002_Scene_Map.rb:114–119,165–230','002_Overworld_Metadata.rb:121–123'],
 ['wp72-debug-contexts-and-controls.md §2.1','DG-M01/DG-U08-09–16','wp12-terrain-movement-vehicles.md §4.3:171–177'],
 ['旧请求假、debug真、停、无消息/解释器/冰滑上下瀑布/早键/菜单请求：F9按住登记并消费；先清请求再音效/整姿/菜单。三自动移动标记才是这里的强移，不扩大到move_route_forcing或静止WAIT。',
  '消息提前返回；解释器或上述自动移动挡新请求；USE/ACTION/SPECIAL先检测命中即不再读F9，其内部门失败也不回落。debug假旧请求假不登记。',
  '普通行走能登记当帧不开，停后F9已松仍可消费；已有请求消费不重检解释器/自动移动新门，菜单优先则调试保留。消息仍挡两阶段；清请求后音效失败不恢复。']),
'R6-DX-DEBUG-004':('零分数变化在全部输出门之前早退',
 ['001_PBDebug.rb:1–77','005_AI_ChooseMove.rb:240–324','004_BattleArenaBattle.rb:1–201'],
 ['wp72-debug-contexts-and-controls.md §9','DG-M23/DG-U08-17–22'],
 ['amt0、两标志真、原空缓冲：无echo/append/flush/I/O；人工已有B且任意标志配置、amt0仍保留B。',
  '＋1/−1两真并正常文件：带符号回显、追加、立即flush；非零任一标志假不接受日志。显式flush两真写B再清，标志关只清不写；不能混成amt0清缓冲。',
  'echo后append完成而文件失败，不保证后段clear；旧异常打印不受这零值门统一控制。AI先评分再log差值，没行不等于没评估；Arena技槽状态与AI评分/log是独立量，新增U13不会改变此门。']),
'R6-DX-DEBUG-005':('建议名不消费性别且无活动随机回退',
 ['002_Debug_MenuCommands.rb:1115–1133','001_Utilities.rb:235–284','025_UI_TextEntry.rb:180–255,666–786'],
 ['wp72-debug-contexts-and-controls.md §5.1','DG-M10/DG-U08-23–28'],
 ['非空Bert直接赋名；空结果且默认Yes、合法类型性别0/1、假想稳定Ada Lovelace/max10均Ada。性别有查询/传入但活动建议函数未用，return后的随机模板不可达；没有读取真实用户名。',
  'abcdefgh12首片段长度10不接受，去尾数字得到Abcdefgh；ABCDEFGHIJ Tail首片段仍10拒，完整用户名capitalize后截10为Abcdefghij；空用户名回退仍空保留Old。严格＜max，不写成≤。',
  '默认No不查询类型/用户名，保持Old；类型/用户名失败早于赋值不保证新名，赋后消息失败保留新名。keyboard min0 ESC返空；cursor BACK删字，不一律取消或回旧名；设施随机名未改。']),
'R6-DX-COMP-001':('运行中直接编译与启动检查有不同失败前缀',
 ['002_Debug_MenuCommands.rb:1335–1344','001_Debug_Menus.rb:69–146','006_Event_HandlerCollections.rb:80–123','001_Compiler.rb:940–1117','002_Compiler_CompilePBS.rb:4–68,205–231','004_Compiler_MapsAndEvents.rb:1683–1751'],
 ['wp04-pbs-lifecycle.md §3.3/§4.5','wp72-debug-contexts-and-controls.md §10','wp75-project-conversion-and-authoring-tools.md §3.1/§4','KL37–KL39/DXCOMP-C01–03'],
 ['完整工程/PBS/旧dat、兼容改写及先行阶段正常；唯一合法Status/Power40在moves条目校验拒：类型/特性先保存新，坏招未登记、内存可留新前缀，旧moves.dat仍在。没有main的预删/局部诊断删除转换，没有整体回滚，完成/窗口释放未到。',
  '同态启动main先建立清单/预删，失败后只有diagnostics正常返回才尝试全部清单删除；删除系统错误被忽略不保证全删，Reset/SystemExit原抛，缺PBS更早失败可能尚无清单。',
  '未登记Map007直接入口不导入，主事件驱动只遍历登记图；启动import可登记且触发编译，999排除不变。全合法直接流程按PBS→动画→登记地图/公共→文本→消息结束；不冒认Demo可运行或全缓存失效。旧正文启动条件本来正确，只补独立入口。']),
'R6-DX-COMP-002':('磁盘、会话缓存与反写是不同观察点',
 ['002_Compiler_CompilePBS.rb:593–629,1274–1320','003_Compiler_WritePBS.rb:364–391,794–821','001_MiscPBSData.rb:1–64','001_Utilities.rb:389–418','001_EditorScreens.rb:1099–1203','001_StartGame.rb:1–17','005_Game_MapFactory.rb:383–492','004_Scene_PlayAnimations.rb:412–579'],
 ['wp04-pbs-lifecycle.md §5.6','wp75-project-conversion-and-authoring-tools.md §3.1','wp74-battle-animation-authoring-and-exchange.md §15/§16','wp62-pokedex-records-regions-and-content.md §5.1','KL40–KL45/DXCOMP-C04–08'],
 ['区域0预载A=[BULBASAUR]、合法作者B=[IVYSAUR]、两种有效、直接全流程成功无失效：datB/读A，编号Bulba1/Ivy0、成员A；随后单项或全量成功反写PBS为A内容，datB/cacheA不变，不保证A旧字节。反写失败可截断/部分写，datB不回滚。',
  '初次缓存尚无时成功编译后读B；地区编辑总Yes档案C→清区域缓存→反写C，No无这条链但子No压洞保留。初始化新Game_Temp改变其三缓存读取前提，不会清独立MapFactoryHelper连接/尺寸缓存。',
  '预载集合/关联A，磁盘集合B含合法Move:TACKLE不同关联：编译按盘更新关联及集合，两个预载仍A；集合单独清不等于关联清。零有效动画名不写保留旧磁盘M是另一门。',
  '连接A预载/编译合法B：盘B/查A；只重建Game_Temp仍A，明确连接清理/新进程另算。pbClearData确有清理，但所读直接编译链无调用；System.reload_cache只证明宿主请求，未知内部副作用不作新保证。']),
'R6-DX-COMP-003':('普通分节的缩进独立注释有阶段差异',
 ['001_Compiler.rb:72–145,232–249','002_Compiler_CompilePBS.rb:4–68,143–200,791–862'],
 ['wp04-pbs-lifecycle.md §4.2','wp03-content-identity-and-schema.md §5.1','KL33–KL35/KL46–KL50'],
 ['普通合法类型A完整后遇B节头，B内空格＋# note：A已yield/校验/登记；预处理把行删空后没有二次略空，B收集处非法属性拒，B未yield/登记、终检/save未到；A不回滚。外层按直接/启动分开。',
  '首列#与纯空物理行在预处理前被略过，A/B正常；同缩进注释放在首节之前是缺初始节、尚无该节登记，不冒认全部磁盘不变。',
  'Name Alpha#Beta/AlphaBeta得Alpha/AlphaBeta，引号不保护#、q不恢复后缀；专用trainers先prep再略空，接受同注释。显式Flags=属性是合法键值行，后续nil元素问题与这非法空行不是同根。'])
}

def main():
    binding=json.loads((OUT/'binding.json').read_text())
    rows=[]
    previous=json.loads(blob(OLD_REVIEW,OLD_DIR+'per-id-review.json'))
    prior_by_id={r['id']:r for r in previous['rows']}
    for batch in ['R6-U06','R6-U07','R6-U08','R6-U09']:
        path=PREFIX+'contracts/'+batch+'.json';raw=blob(PREP,path);con=json.loads(raw)
        for n,c in enumerate(con['scope_contracts']):
            rid=c['id'];r={'id':rid,'batch':batch,'verdict':'ACTUAL_PASS_SCOPED_STATIC',
                          'actual_commit':ACT,'formal_tree':binding['formal_tree'],
                          'contract':{'commit':PREP,'path':path,**identity(raw),'pointer':'/scope_contracts/'+str(n)},
                          'seven_complete_groups_and_original_full_proposal':'Read entire fixed contracts/original counters. U07 exact earlier direct full prompt/contract read reused; no author-summary shortcut.',
                          'severity':c['identity_and_verdict'].get('severity'),
                          'frozen_acceptance_and_regression':c['acceptance_and_regression'],
                          'frozen_minimum_revision_contract':c['minimum_revision_contract'],
                          'blocking_failures':[],'minimum_substantive_changes':[],
                          'behavior_vector_execution':0,'formal_acceptance':False,'CLOSED':False}
            if rid in MANUAL:
                title,sources,actual,cases=MANUAL[rid]
                r.update({'reviewer_title':title,'source_context_anchors':sources,'actual_prose_and_catalog_anchors':actual,
                          'independent_static_acceptance_vectors':[{'case':i+1,'manual_expected_result_and_premises':x,'assessment':'PASS_STATIC_THIS_ACTUAL','executed':False} for i,x in enumerate(cases)]})
            else:
                old=prior_by_id[rid]
                r.update({'reviewer_title':c['identity_and_verdict'].get('title'),
                          'prior_exact_direct_work':{'commit':OLD_REVIEW,'path':OLD_DIR+'per-id-review.json','pointer':'/rows/'+str(n)},
                          'same_source_read_reuse':'shared-full-read-reuse.json /sources; all seven exact reference identities verified',
                          'current_manual_assessment':'Final actual WP74 full text, catalog full exact-text reuse plus complete novel delta, and WP67 full exact-text reuse plus complete novel delta independently reviewed. Original candidate added behavior lines all survive exactly. Source producer/consumers and original reverse/cancel/failure vectors reevaluated with final U09 caches/U14 consumers/U13 interfaces; no semantic regression. Prior candidate verdict is not the actual signature.',
                          'prior_review_reasoning_attribution':old['reviewer_assessment'],
                          'independent_static_acceptance_vectors':[{**{k:v for k,v in x.items() if k!='verdict'},'assessment':'PASS_STATIC_THIS_ACTUAL','execution':False} for x in old['all_static_vectors']],
                          'actual_prose_and_catalog_anchors':{'AN-001':['WP74 §4.4/§4.5/§8.2','AN-M05/B20-C025'],
                              'AN-002':['WP74 §3.2/§7.1/§7.4/§11.1/§16','AN-M09/AN-M12'],
                              'AN-003':['WP74 §10.2','AN-M23','WP67-A §9.4'],
                              'AN-004':['WP74 §8.4/§9.3/§17','AN-M16/AN-M22'],
                              'AN-005':['WP74 §11.2/§19','AN-M25'],
                              'AN-006':['WP74 §8.6/§19','AN-M18/AN-M19'],
                              'AN-007':['WP74 §8.6/§19','B20-D024']}[rid[-6:]]})
            r['all_frozen_conditions_disposition']='All listed conditions covered by the independent vectors and necessary scoped regressions. DEBUG-002 return-point qualification explicitly resolved from source; no host result assumed.' if rid=='R6-DX-DEBUG-002' else 'All listed conditions covered by the independent static vectors and necessary scoped regressions; no required acceptance item omitted.'
            rows.append(r)
    assert len(rows)==19 and len({r['id'] for r in rows})==19
    write('per-id-review.json',{'reviewer':'independent actual group-C','binding':binding,
          'verdict':'ACTUAL_PASS_SCOPED_STATIC','required_ids':19,'passed':19,'failed':0,
          'rows':rows,'method':'Direct manual source/context/actual-full-text/counterevidence review. Tool-generated hashes/joins do not generate these judgments.',
          'AN007_optional_boundary':'Required approximate automatic controls only. General-N float accumulation/endpoints remain independent optional; no bitwise/native quantization/compatibility mandate.',
          'formal_acceptance':False,'CLOSED':False})
    print('manual rows',len(rows),'static vector groups',sum(len(r['independent_static_acceptance_vectors']) for r in rows))

if __name__=='__main__':main()
