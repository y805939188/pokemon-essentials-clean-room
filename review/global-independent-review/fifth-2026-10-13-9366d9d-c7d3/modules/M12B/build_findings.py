from assemble_review import P,R,RV,BV,FT,F,base,save,identity
import json
# All facts below are static deductions. No executed fixture or reference model is claimed.
def src(path,rr,symbol,fact,caller=None,config=None):
 return dict(path='Data/Scripts/'+path if not path.startswith(('Data/','PBS/')) else path,version=RV,lines=rr,symbol=symbol,caller=caller,configuration=config,supporting_fact=fact)
def spec(file,section,rr,statement):
 return dict(path=str(F/file),version=BV,section=section,lines=rr,current_statement=statement)
def neg(file,scope,result):return dict(path=str(F/file),version=BV,actual_read_scope=scope,result=result)
common_negative=[neg('generic-kernel/wp03-content-identity-and-schema.md','complete 1–240','Direct registration/defaults are described generally; they do not specify tool creation text-key mismatch or BP editor projection.'),neg('generic-kernel/wp04-pbs-lifecycle.md','complete 1–227','Writer/compiler lifecycle, including known evolution/encounter/metric non-roundtrips, does not specify these new type/item cases.'),neg('demo-dx/wp73-a-content-editors.md','complete 1–174','All text, property tables, editors, save matrix and boundaries read; candidate-specific behavior is not supplied elsewhere.'),neg('test-catalog/demo-dx-wp72-73-74-75-76-77.md','complete 1–295','All CE and B17/B19/B20 cases read; ID/pocket/price BACK/evolution cases do not test textual creation outputs or untouched BP1 save.')]
findings=[]
def make(num,title,sev,disp,category,anchors,specs,expected,current,gap,pre,minimal,normal,boundary,impact,negative,proposal,files,shared,accept,dependencies,capabilities,rootcause,excluded,unknowns,confidence):
 return {**base,'id':f'GR5-M12-{num}','title':title,'severity':sev,'disposition':disp,'status':'candidate_pending_independent_counterevidence','category':category,'source_anchors':anchors,'spec_anchors':specs,'expected_reference_behavior':expected,'current_spec_behavior':current,'gap':gap,'preconditions':pre,'minimal_counterexample':minimal,'normal_case':normal,'failure_or_boundary_case':boundary,'impact_on_independent_implementation':impact,'negative_evidence_search':negative,'proposed_spec_change':proposal,'affected_files':[str(F/f) for f in files],'shared_contracts':shared,'acceptance_criteria':{'static':accept,'must_execute':[],'optional_future_execution':'An isolated authorized fixture may later confirm host-visible results; no execution is needed to establish the source-level chain and none was performed in this review.'},'dependencies':dependencies,'related_capabilities':['M12-'+x for x in capabilities],'related_findings':[],'root_cause_group':rootcause,'priority':sev,'batch_owner':'M12/root; proposed spec author owner Demo/DX','history_links':['original-comparison.json','reading-coverage.json','spec-to-source.json'],'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_COUNTEREXAMPLE'],'execution_status':'NOT_EXECUTED_THIS_REVIEW','confidence':confidence,'unknowns':unknowns,'excluded_claims':excluded,'user_decision_needed':False,'review_resolution':{'independent_counterevidence':'pending root/another independent reviewer','final_required_signoff':False,'note':'Disposition is a proposed classification, not self-approved final remediation. Preserve fixed reference behavior separately from any future compatibility policy.'}}
findings.append(make('101','新建训练家类型与道具的名称输入未成为保存文本','P2','required','incorrect_output_and_missing_creation_boundary',[
 src('020_Debug/001_Editor screens/001_EditorScreens.rb',[[392,443],[869,921]],'new trainer type / new item','名称用于ID和成功消息；新建提交的文本键不被当前记录构造读取。数值/口袋等仍传入。','Debug menu and missing-trainer creation paths'),
 src('010_Data/001_GameData.rb',[[78,85]],'direct register','直接用输入构造记录，没有把旧文本键转为当前文本字段的适配步骤。'),
 src('010_Data/002_PBS data/014_TrainerType.rb',[[18,30],[101,117]],'trainer-type schema/default/name','原始名称缺失时为 Unnamed；显示经消息表读取这个默认原文。'),
 src('010_Data/002_PBS data/006_Item.rb',[[25,44],[119,138]],'item schema/default','新建后原始单数名/复数名为 Unnamed，描述为 ???。'),
 src('021_Compiler/003_Compiler_WritePBS.rb',[[1,65],[158,160],[447,449]],'generic writer and item/type writers','从已登记记录的当前字段写出，保存链不会恢复用户文本。'),
 src('015_Trainers and player/002_Trainer_LoadAndNew.rb',[[62,80]],'trainer text conversion','从已登记原始名称更新文本/反写；默认值继续传播。')],
 [spec('demo-dx/wp73-a-content-editors.md','§4.1、§4.3',[[79,101]],'新建名称/描述后注册、保存、反写；明确称复数名为名称+s。'),spec('test-catalog/demo-dx-wp72-73-74-75-76-77.md','CE-M05/M08/M10',[[52,57]],'验证ID/嵌套保存/口袋取消，未核保存文本。')],
 '正常完成新建时，类型的保存原始名称为 Unnamed；道具的保存原始单/复数名称均为 Unnamed、描述为 ???。输入仍决定ID并用于创建成功消息。名称的最终本地化显示取决于消息表，不能无条件保证屏幕字面正是默认英文。',
 '名称输入被自然理解为新记录名称；道具复数名还被明确断言为输入+s；没有区分成功消息和实际保存文本。',
 '错把创建过程收集的值当成登记/持久化后的值，遗漏当前参考的新建文本默认化。',
 ['固定R、无插件改写注册；输入非空且ID空闲；合法口袋/价格/类型性别；所有保存和反写正常完成。','比较原始记录/PBS字段；若观察UI，消息表中没有对默认文本的额外翻译覆盖。'],
 {'input':'新建道具名 Amber、口袋1、价格100、描述 A small token；不存在AMBER。','source_result':'ID AMBER，价格100/口袋1，但原始Name和NamePlural均Unnamed、Description为???；成功提示仍含Amber。','spec_implied_result':'复数Ambers并保留输入文本的记录。'},
 {'input':'编辑已有合法道具/训练家类型的Name字段，确认保存。','result':'现有项编辑按schema写入正确文本字段，可保存所改名称；不能把缺陷推广到所有编辑。'},
 {'input':'新建名称空且无default_name，或道具口袋BACK返回0。','result':'按现有合同提前放弃，没有这次新记录。若后续写出失败，只能承诺此前已发生的登记/存档，不保证完整产物。'},
 '独立实现可能产生与固定参考不同的列表名称、文本消息键、PBS内容和重新载入结果；错误地以成功提示作为保存正确的证据。',
 common_negative+[neg('creature-rpg/wp24-player-trainers-partners.md','complete 1–289, especially §5.3','只把调试新建交界给WP73；未补新建类型默认名称事实。'),neg('creature-rpg/wp27-bag-and-item-storage.md','complete 1–174','容器合同不覆盖作者创建文本。'),{'path':'review/wp73a-delivery-2026-10-02/revision-v4/entry-coverage-table.md','version':BV,'actual_read_scope':'complete 1–58','result':'新建行同样只记输入与保存，无默认文本边界。'},{'path':'fixed B21 supplements','version':'e58486178e746273fb6fab55df00722807f1dc44','actual_read_scope':'static-cases.json full; eight-chains.json CHAIN-6 behavioral fields','result':'数值取消/口袋和物种链不消除此文本失配。'}],
 '在两种新建合同分开列输入名称、ID/成功消息和真正保存的原始文本；删除道具保存复数=输入+s的承诺，保留它只作为创建阶段意图的非合同事实。加新建类型/道具与已有项编辑对照向量。',
 ['demo-dx/wp73-a-content-editors.md','test-catalog/demo-dx-wp72-73-74-75-76-77.md'],['M12-S02','WP03 content registration','WP08 raw text versus localized display'],
 ['新建类型、道具各有原始字段与PBS预期，和已有项编辑正常例分列。','ID派生、口袋/价格取消、嵌套持久行为不因本修订改写。','描述独立可见行为，不抄原始hash结构或修参考代码。'],['normal registration/archive/PBS write; localization boundary'],['E03','S02'],'new-record-text-binding',
 ['不是数据编译器普遍丢Name；不是已有记录编辑无法改名；不保证任何消息语言的最终字面显示；不修改参考。'],['未执行UI/写盘/重新编译；实际宿主失败呈现未知。'],'high source chain; proposed P2 pending independent review'))
findings.append(make('102','原样确认道具编辑会把默认 BP 价格 1 保存为 0','P2','required','missing_roundtrip_default_transition',[
 src('010_Data/002_PBS data/006_Item.rb',[[49,71],[119,138],[253,267]],'BPPrice property/constructor/export','BP价1被PBS投影省略；编辑字段用非空有界数值型；显式0构造保留。'),
 src('020_Debug/001_Editor screens/001_EditorScreens.rb',[[822,860]],'item existing edit','先取PBS投影，空值填控件默认，再在Yes后将所有字段注册/保存/反写。'),
 src('020_Debug/002_Editor_DataTypes.rb',[[56,103],[1624,1706]],'numeric default / property confirmation','非空数值型默认0；Yes不要求实际更改字段；可空SellPrice默认nil是不同对照。'),
 src('021_Compiler/003_Compiler_WritePBS.rb',[[1,65],[158,160]],'item PBS output','登记BP0不再被默认1省略，写出0。')],
 [spec('demo-dx/wp73-a-content-editors.md','§3.2、§4.3、§6',[[36,46],[96,101],[128,142]],'通用默认0和已有项确认保存存在，但没有将BP1省略与控件0连接为原样保存改变价格。'),spec('creature-rpg/wp29-shops-and-exchanges.md','§5.1、§9',[[109,114],[180,188]],'数据BP价格默认1；编辑器上限与运行价格分开。')],
 '已有合法道具BPPrice=1，打开属性列表不碰该字段而选Yes：编辑工作值先成0，成功后登记/档案/PBS均为0。选No保持原1；BP=2等非默认值保持2。',
 '给出默认1和普通保存流程，却缺少常见默认值在编辑器投影/回填之间的非恒等转换。',
 '消费者用导出时省略默认值的视图作为编辑初值；空值被另一个默认0替代，原样确认仍产生语义修改。',
 ['合法道具原始BP价1；正常已登记数据/属性列表；不手动改BP；选Yes且全部保存步骤成功；无外部改写。'],
 {'input':'一个BP价1的已登记道具，进入Items编辑器，直接BACK后Save changes? Yes。','source_result':'BP价0；PBS出现BPPrice=0。','contract_gap':'未说明原样保存使默认1变0，独立实现很可能保留1。'},
 {'input':'相同操作但原BP价2。','result':'保持2；也可显式在属性页把工作值改为1，登记1而写PBS时省略。'},
 {'input':'原BP价1，Save changes? No。','result':'当前登记/档案/PBS不因本属性编辑改变。后续PBS失败时已保存档案可为0，不许总回滚。'},
 '作者不改该字段的保存可把BP兑换变成零价；规格驱动的实现和自动测试会漏掉该内容与经济行为差异。',
 common_negative+[neg('creature-rpg/wp29-shops-and-exchanges.md','complete 1–210 and SH tests122–157','价格默认/零价/输入层级正确，但没有编辑器的1→0消费链。'),neg('creature-rpg/wp27-bag-and-item-storage.md','complete 1–174','与物品容器无关，不能补此原样保存结果。')],
 '在道具已有项保存中加入BP1→编辑0→确认后登记/档案/PBS0的阶段链；加No、非默认2和显式设1三个相邻对照。保持缺省PBS价1本身不变。',
 ['demo-dx/wp73-a-content-editors.md','test-catalog/demo-dx-wp72-73-74-75-76-77.md'],['M12-S02','WP03 default records','WP29 BP price input'],
 ['确认无需手动改字段，完整说明1→0的三层结果。','No不写与值2保持/显式改1对照齐全；不把该行为推广到可空SellPrice或SkillLevel。','静态推导与必须执行分开。'],['Item PBS projection and property defaults'],['E03','E01','S02'],'editor-default-projection',
 ['不是所有价格都变0；不是PBS缺省价改为0；不是输入控件拒绝1；不同于历史物种复数进化投影但共享持久交界。'],['未运行商品交换，实际经济影响只按下游价0合同推导。'],'high source chain; proposed P2 pending independent review'))
findings.append(make('103','调试形态编辑的图鉴门遗漏底层提交登记','P2','required','cross_contract_contradiction',[
 src('020_Debug/003_Debug menus/007_Debug_PokemonCommands.rb',[[740,802]],'nonbattle species/form handler','多形态变化或单形态重置用普通form提交；后面的显式register才有非准备且非蛋门。'),
 src('014_Pokemon/001_Pokemon.rb',[[136,195]],'form submission and simple form','普通提交在玩家存在时登记图鉴，无settingUpBattle/egg门；简化提交不登记。'),
 src('015_Trainers and player/005_Player_Pokedex.rb',[[195,219]],'register','不检查蛋；写seen/seen_form/首次last_seen并刷新，不写owned/seen_egg。'),
 src('020_Debug/003_Debug menus/005_Debug_BattlePkmnCommands.rb',[[756,790]],'battle form edit','先简化写原个体；有在场对象时随后设置在场形态。'),
 src('011_Battle/002_Battler/001_Battle_Battler.rb',[[67,70]],'battler form write-through','在场形态同步再次到原个体普通提交，引出登记。'),
 src('PBS/pokemon.txt',[[11113,11140]],'SHELLOS base','命名West Sea基础形态。',config='No Shellos getForm handler in fixed script search'),
 src('PBS/pokemon_forms.txt',[[1119,1123]],'SHELLOS form1','命名East Sea非0形态，可作无动态处理器的确定对照。')],
 [spec('demo-dx/wp72-debug-contexts-and-controls.md','§6通用、§6.4、§7.4',[[129,129],[160,160],[206,206]],'非战斗图鉴副作用门列形态，仅非构造测试且非蛋登记；形态条重复引用该门；战斗条未说明写穿引发登记。'),spec('pokemon-rules/wp21-dynamic-forms-and-display.md','§4.1',[[185,196]],'普通形态提交登记，简化不登记；这是正确的上游反证。'),spec('pokemon-rules/wp62-pokedex-records-regions-and-content.md','§3.1/§3.4',[[32,46],[71,82]],'任何来源普通形态提交无内部战斗门，直接register不拒蛋。')],
 '有全局玩家时，非战斗调试的实际形态提交即使在构造测试模式或目标是蛋，也会经底层写见过/形态记录；有在场对象的战斗形态同步同样可到此。没有在场对象且只走简化写入时，无这条提交登记。',
 'WP72的局部总结把后置显式登记的条件当成整条形态编辑调用链的门，和WP18/WP21/WP62正确通用合同相冲突。',
 '入口层条件没有包住此前的具有副作用的下游调用。',
 ['全局玩家/图鉴、有效Shellos两形态及刷新依赖存在；目标形态确实改变；无forced/getForm/plugin干扰。','为避免先前记录掩盖差异，形态1见过记录初始未置；构造测试个体已创建、此次只比较编辑前后。'],
 {'input':'设置测试战斗中的Shellos由形态0改1，settingUpBattle为真，玩家图鉴尚未记录形态1。','source_result':'底层普通提交登记形态1；外层显式register虽然跳过，最终记录仍已写。','spec_result':'按WP72“仅非构造测试且非蛋”的门会预测不登记。'},
 {'input':'普通非蛋、非准备情境改Shellos形态0→1。','result':'仍登记；重复显式登记不清既有记录。'},
 {'input':'分别给蛋个体、战斗中有在场对象、战斗队伍中无在场对象；另列表BACK/选原形态。','result':'蛋普通提交仍登记；有在场对象的同步经普通提交；无在场对象仅简化写无该登记；BACK/同形态不执行这次提交。owned与seen_egg不由register置真。'},
 '独立实现会错误压制作者测试/调试产生的图鉴记录，或把场上/场下形态编辑当同一副作用；状态隔离测试预期不一致。',
 [neg('demo-dx/wp72-debug-contexts-and-controls.md','complete 1–447','通用非沙盒提示不能覆盖§6的明确“才”门；两处具体条件都需收窄。'),neg('pokemon-rules/wp21-dynamic-forms-and-display.md','complete 1–327','普通提交合同正确；问题在WP72入口投影，非上游缺规则。'),neg('creature-rpg/wp18-creature-identity-species-ownership.md','§3.4 complete131–155 plus targeted search of full file','三种形态入口差异正确。'),neg('pokemon-rules/wp62-pokedex-records-regions-and-content.md','1–118 all related registration sections','明确普通提交无门且register不拒蛋；因此加强具体矛盾，不能归因为缺Pokedex内容。'),neg('test-catalog/demo-dx-wp72-73-74-75-76-77.md','complete1–295 DG-M15/DG-M19 and B20-C029','未给settingUpBattle形态提交记录差异；B20-C029是动态读取守卫，不是普通提交禁止。'),neg('test-catalog/pokemon-rules-wp19-21-22-23-34.md','FM01–FM43 rows84–131','普通提交/动态读取既有向量正确，未覆盖这条调试调用链。'),neg('test-catalog/creature-rpg-wp18-20-24-25-26.md','CI01–CI28 rows5–36','创建/简化提交对照正确，但未复现调试准备模式后续form提交。')],
 '将WP72图鉴条件限定为处理器自身的显式登记；分别列非战斗普通形态提交、有在场同步和无在场简化提交，引用既有WP21/WP62；加测试准备真/假、蛋、场上/场下、同值取消对照。',
 ['demo-dx/wp72-debug-contexts-and-controls.md','test-catalog/demo-dx-wp72-73-74-75-76-77.md'],['WP18 form submission','WP21 §4.1','WP62 §3','M12-S02'],
 ['解释显式登记门与嵌套提交副作用，不能只增一个泛化非沙盒警告。','至少覆盖准备中0→1、蛋、在场/无在场、BACK/同形态；见过与拥有/见过蛋分开。','保留正确上游合同，不为修工具描述改参考或强行增加图鉴抑制。'],['effective species form data; global Pokedex refresh dependencies'],['D04','D07'],'debug-form-inner-registration',
 ['不是所有调试字段都会无条件登记；不宣称owned或seen_egg改变；动态读取守卫不是普通提交守卫；不证明可玩Demo链。'],['未执行场景；具体UI刷新或扩展异常仍由宿主/插件决定。'],'high static chain; proposed P2 pending independent review'))
findings.append(make('104','安全复制应区分用于比较的资源位置与实际写入位置','P3','optional','bounded_contract_clarification',[
 src('020_Debug/001_Editor_Utilities.rb',[[16,44]],'safe copy','存在性/尺寸/内容/覆盖询问始终看第二位置；第三位置只替代最终写入路径。'),
 src('020_Debug/003_Debug menus/003_Debug_MenuExtraCode.rb',[[615,633]],'batch resource import','比较位置为资源解析结果，第三位置为项目目标。'),
 src('001_Technical/002_Files/001_FileTests.rb',[[195,241]],'resource path resolution','当前仅当前目录，通常两者相同；字面未命中后追加后缀可能找到另一存在路径。')],
 [spec('demo-dx/wp74-battle-animation-authoring-and-exchange.md','§13.2/§13.3',[[368,374]],'以单一“目标”描述比较/覆盖，再称可选第三参数改目标路径。'),spec('demo-dx/wp73-a-content-editors.md','§5',[[126,126]],'概括相同跳过、不同确认覆盖。')],
 '比较资源与最终输出可以不同：源与比较资源相同则直接跳过，即使输出不存在；源与比较资源不同且确认后只写输出，不修改比较资源。',
 '单一目标词没有明确第三位置是否也替代比较/询问对象，正常同位置例没有区别。',
 '可选参数变体中的可见文件状态缺少两位置区分；没有证据把它扩大为默认同路径流程普遍错误。',
 ['源存在且可读；比较位置与输出位置不同；无并发改写；不执行文件操作，仅静态对照。'],
 {'input':'源X与既有比较Y同字节；实际输出Z不存在；请求三位置复制。','source_result':'不创建Z，不提示；因为Y已相同而提前返回。','ambiguous_alternative':'把Z当比较目标会创建Z。'},
 {'input':'普通两位置复制，源与目标不同、确认。','result':'按现有合同写目标；第三位置省略时不产生新差别。'},
 {'input':'X与Y不同，Z另指一个可写位置；拒绝/同意覆盖Y的提示。','result':'拒绝不写；同意只写Z，Y保持。默认导入通常解析为相同路径，不能假定远端RTP路径默认存在。'},
 '独立工具可能在资源兼容参数变体中创建本来应跳过的副本，或比较/提示不同文件；范围较窄，列可选澄清。',
 [neg('demo-dx/wp74-battle-animation-authoring-and-exchange.md','complete1–472','导入、保存矩阵及安全复制均未区分比较位置/写入位置。'),neg('demo-dx/wp73-a-content-editors.md','complete1–174','只引用同一概括。'),neg('engine-overworld/wp15-resource-matching-and-audio.md','§3完整21–32及相关17–46/117–162','解析规则只给路径，不提供复制参数合同；当前仅当前目录限制了默认影响面。'),neg('generic-kernel/wp07-diagnostics-files-http.md','complete1–143','通用文件复制/移动不是该三位置安全复制入口。'),neg('test-catalog/demo-dx-wp72-73-74-75-76-77.md','complete1–295 AN-M27/M28/B20-C020','无比较Y与输出Z分离的静态例。')],
 '可选将安全复制的两个位置用独立行为术语区分，并加相同跳过和不同确认后的文件状态对照；无须新增API或要求未来支持额外搜索目录。',
 ['demo-dx/wp74-battle-animation-authoring-and-exchange.md','test-catalog/demo-dx-wp72-73-74-75-76-77.md'],['M12-S01','WP15 resolved resource location'],
 ['若接受修订，比较位置和写入位置各自定义，两个静态对照可判定。','不声称默认多RTP目录、不把可选问题升成所有导入失败。'],['safe copy third-destination variant'],['S01','A07'],'safe-copy-comparison-vs-destination',
 ['没有运行实际复制；没有证明默认数据触发分离；不是安全漏洞指控；无需用户此刻选择兼容政策。'],['未来是否保留该变体由独立兼容阶段决定，不影响固定参考事实。'],'high behavior; low breadth; optional only'))
save('findings.json',{**base,'status':'candidate_pending_independent_counterevidence','findings':findings,'counts':{'proposed_required_P2':3,'optional_P3':1,'final_required':0},'no_reopened_deferred_history':['GR3-M09-001','GR3-M02-003']})
# Same root cause: do not split the nullable portion-name defaults into another finding.
f=findings[1]
f['title']='原样确认道具编辑会改写默认 BP 价格与未指定份量名称'
f['source_anchors'].append(src('020_Debug/002_Editor_DataTypes.rb',[[906,919]],'item-name property default','未指定份量名称/复数份量名称使用同一名称控件，默认???。'))
f['source_anchors'].append(src('010_Data/002_PBS data/006_Item.rb',[[54,70],[119,138],[149,163]],'portion text defaults/readback','两项原始份量名称本可为空并回退普通名称；编辑回填???后构造保存显式???，读取不再走原来的名称回退。'))
f['expected_reference_behavior']+=' 同一未改确认还把原先未指定的PortionName、PortionNamePlural从空写为???；它们此前读名称回退，之后读显式份量文本（最终显示仍经过本地化）。'
f['gap']+=' 缺失份量名称同样在编辑回填中由空变为控件默认???；与BP省略默认值是同一编辑初值/构造默认不等价根因，合并处理。'
f['minimal_counterexample']['additional_same_root_case']={'input':'合法既有道具名称/复数有效，两项份量名称都未指定，打开后不修改并Yes。','result':'两原始份量名称均???并保存/反写；No保留未指定，显式非空份量名称保持。'}
f['proposed_spec_change']+=' 在同一例中分列可选份量名称的空→???，并给未打开/No及原来明确非空的反向对照。'
f['acceptance_criteria']['static'].append('同根因覆盖两项未指定份量名称，区分原始字段、回退显示和消息本地化；不另立重复问题。')
f['negative_evidence_search'].append(neg('demo-dx/wp73-a-content-editors.md','§3.3/§4.3/§6 in full read','通用名称控件默认???虽已写明，但未交付两可选份量名称原样保存会从未指定变显式默认的消费结果。'))
save('findings.json',{**base,'status':'candidate_pending_independent_counterevidence','findings':findings,'counts':{'proposed_required_P2':3,'optional_P3':1,'final_required':0},'no_reopened_deferred_history':['GR3-M09-001','GR3-M02-003']})
# Independent counterevidence records keep root IDs; none is copied as a new M12B finding.
conv='021_Compiler/004_Compiler_MapsAndEvents.rb'
wp75='demo-dx/wp75-project-conversion-and-authoring-tools.md'
root_negative=[neg(wp75,'complete1–394','Read all current正文/tables/examples including specific narrower clauses; no reliance on observation summary.'),neg('test-catalog/demo-dx-wp72-73-74-75-76-77.md','complete1–295 including CV01–30 and B20','All relevant cases compared; abstract fixture labels are not treated as behavior guarantees.'),{'path':'specs/demo/wp75-project-conversion-and-authoring-tools.md','version':BV,'actual_read_scope':'complete1–460 (equal spans reused from independently read formal; all differences directly read)','result':'No unique original fact resolves the four confirmed gaps.'},{'path':'review/wp75-delivery-2026-10-02/revision-v4/entry-coverage-table.md','version':BV,'actual_read_scope':'complete1–81','result':'All44 rows plus inactive appendix read; exact facts assessed below, not accepted from old PASS.'}]
cs=[]
def ce(n,decision,disp,sev,facts,anchors,specs,reason,controls,negative,unknowns=[]):
 cs.append(dict(observation_id=f'M12-OBS-{n:03d}',originator='root',independent_reviewer='M12B',module='M12',decision=decision,recommended_disposition=disp,proposed_severity=sev,source_baseline=RV,specification_baseline=BV,source_anchors=anchors,spec_anchors=specs,independently_established_facts=facts,reason=reason,normal_and_boundary_controls=controls,negative_evidence_search=root_negative+negative,execution_status='NOT_EXECUTED_BY_M12B',parent_execution_usage='Parent execution records were not read or adopted as M12B execution evidence; this decision uses direct static source/contract reads.',unknowns=unknowns,status='independent_counterevidence_complete_for_observation',final_catalog_action='Root owns final finding identity/classification and merge; this file does not edit the shared report.'))
ce(1,'confirm_with_scope','required','P2',[
 '已安全解压实际Scripts.rxdata Main全文49行（不是执行、不是反序列化）；解码字节SHA256 da24a2220936c6d44ddc60f180aed37beede022012d7addc99b5562ed07c52e1。',
 '每目录先枚举，文件和子目录分别排序；本层所有大小写不敏感.rb文件先装载，再递归子目录；点开头目录排除，但点开头.rb普通文件仍入选；没有递归层数上限。',
 '文件读取在局部求值保护之前；ScriptError被替换为基类异常并保留消息；普通默认捕获类别尝试回溯消息重写，消息长度>=900时覆写traceback.log并抛固定说明；较短原样再抛。更外层异常/文件失败不能承诺同一日志路径。'],
 [dict(path='Data/Scripts.rxdata',version=RV,lines=[[1,49]],coordinate_system='safely decoded Main text',decoded_sha256='da24a2220936c6d44ddc60f180aed37beede022012d7addc99b5562ed07c52e1',supporting_fact='Independent decoded body read in full; compressed member offset29,1197bytes')],
 [spec(wp75,'§1/§2/§12/§16/§18',[[18,31],[282,283],[378,392]],'明确仍只登记装载器形状，内容不解包/未核。')],
 '通用插件装载与主运行异常合同不是此启动前装载器；新可读文本消除了“仅二进制不可研究”的材料理由。确认可提静态行为缺口，但不推实际宿主可启动或精确消息改写一定成功。',
 ['a.rb、b.RB按序先于子目录；.hidden/x.rb跳过而.hidden.rb可入选。','900长度门与899对照；读文件失败早于局部求值捕获；无需运行任一文件证明顺序。'],
 [neg('generic-kernel/wp05-events-extensions-plugins.md','complete1–141 + EP01–27','插件预编译发现/依赖/执行错误通道不同，不补此散文件Main装载。'),neg('generic-kernel/wp07-diagnostics-files-http.md','complete1–143 + IO01–20','正常主代码报告/文件工具不补装载器排序、隐藏项、900门。'),neg('generic-kernel/wp09-save-startup-continue.md','complete1–163 + SV01–17','启动状态合同从更后阶段开始，未提供此装载策略。')],['是否实际执行至主游戏、脚本错误消息可变性、日志权限及原生宿主最终结果未知；只审静态分支。'])
ce(2,'confirm_narrowed_to_literal_line_match','required','P2',[
 '六族匹配都使用行首/行尾边界，并以可跨行内容捕获括号内部；它们不是整个字符串绝对边界。',
 '任一行合法完整旧调用即可被命中；转换输出重新组合被捕获的调用参数，前后独立行文本不被保留。',
 '同一行前缀/后缀、错误大小写函数名和空括号不等同于独立行包围；必需参数缺失仍不保证正常。'],
 [src(conv,[[979,1133],[1499,1578]],'six-family replacement / conditional branch consumption','独立逐个阅读六模式、参数重排和写回；换行环境可匹配而整个参数串被替换。')],
 [spec(wp75,'§8.2',[[192,209]],'用整体旧调用的语义限定匹配。'),spec('test-catalog/demo-dx-wp72-73-74-75-76-77.md','B20-C034',[[291,291]],'旧形整体调用、整体旧形匹配的表述。')],
 '静态正则边界本身足以反驳全串保证；确认六模式同类边界，但不把父方个别执行推广成本轮六模式实测。',
 ['独立前行标记＋合法旧调用行＋后行标记：可转换且两标记丢失。','同一行紧贴前后文字不通过相同门；空括号也不通过。','默认可选尾值及非默认canLose插入顺序按既有18夹具保持。'],
 [{'path':'review/remediation/20261003-prepare/batches/B20/author-draft-1/six-family-fixtures.json','version':'3f521e6dea0b442e4bb174a9715c458416386b37','actual_read_scope':'all18 fixture objects','result':'测试核心/默认/非默认参数，没有多行包围反例；不能作全串锚定证据。'}])
ce(3,'confirm_parameters_only','required','P2',[
 '门入场请求Door enter，等待2单位后左/右/上转向，各后等待2；玩家穿透开→上一格→穿透关并等待。跟随者入口及等待独立。',
 '入场关门等待2，再右/左/下各等待2；RGB全黑请求6单位，事件等待8，玩家显形→原转移→中性色调6。',
 '出场页在位置条件内隐藏玩家/跟随者，门左转等待6、玩家显形下行一步、跟随者归位，门上/右/下各等待2；条件外置临时A。',
 '独立转移规范化将转移设无fade；Exit Door明确80/100，色调黑6、等待8、转移、中性6。原额外音效被替换。',
 '通用命令/路线规格规定1单位=1/20秒及210等待；不提供这些具体输出参数。实际总动画耗时不等于等待值简单相加。'],
 [src(conv,[[88,140],[815,903],[1398,1413]],'route builder / door recipe / standalone transfer','直接读取所有输出参数与插入顺序；资源名与时长不是架构规定。')],
 [spec(wp75,'§7.2及§17向量导航',[[109,124],[386,386]],'门动画/音效/淡黑/等待的概述，缺具体方向、资源名和时长。'),spec('test-catalog/demo-dx-wp72-73-74-75-76-77.md','CV-M09/M13',[[160,160],[164,164]],'两配方没有给出具体音效/方向/等待值。')],
 '确认缺少可用于独立测试的具体产物参数；应限定在这两种转换配方，不能重开通用跟随或主事件命令架构。',
 ['结构门未过但Switch22重注册仍保留既有副作用；不能把此参数补齐改成全事务。','门音效只给名称，源未显式给音量/音调，不凭宿主默认猜成固定100/100。','普通独立转移固定Exit Door80/100与门入场名称请求分开。'],
 [neg('engine-overworld/wp13-map-events-npc-followers.md','complete1–190, especially§6.3','跟随快照/through/等待合同正确，只给消费语义，不给门配方全参数。'),neg('engine-overworld/wp13-move-route-matrix.md','complete1–81','方向/等待/路线推进规则可解释参数，但不提供生成配方。'),neg('engine-overworld/wp13-interpreter-command-matrix.md','1–84 plus123–159, all relevant wait/transfer/tone rows','给单位/控制结果，不能补丢失的数值。'),neg('engine-overworld/wp15-resource-matching-and-audio.md','§3 and§6 relevant17–46/117–162','无Door enter/Exit Door生成资源约定。'),neg('engine-overworld/wp16-world-rendering-and-visual-transitions.md','§5.3–5.4 relevant203–229','色调通用时钟和零时长合同，不提供门6/8配方。')])
ce(4,'confirm_duplicate_boolean_boundary','required','P2',[
 '每个事件转换开始DoubleBattle/Continue为假；被收集块依序解析，遇修剪后的TRUE/YES才把相应标志置真。',
 '随后FALSE/NO/其它字面不写假，所以同族多个注释为累计真（锁存）；后续假不撤销早真。',
 '首页和再战页均消费这两个最终标志，分别发双打/可败规则；标量最后写与列表累加为其他字段，不能统一成最后值覆盖。'],
 [src(conv,[[509,567],[596,599],[647,669]],'trainer annotation parse and emitted rule consumers','初值、两条真写入和两页消费者直接读到。')],
 [spec(wp75,'§5.2/§5.4',[[70,87]],'只说明TRUE/YES为真，未列重复标记后的状态规则。')],
 '确认是具名重复输入边界不足；建议只补两布尔族锁存和真→假/假→真/全假对照，不泛化所有注释键。',
 ['独立DoubleBattle:YES后DoubleBattle:NO，或Continue:TRUE后Continue:FALSE：最终仍启用。','仅NO/FALSE维持默认假；反向假→真为真；每事件重新开始是假。'],[])
ce(5,'exclude_required_revision','no_required_revision',None,[
 '直接消费者只对TrainerBattle.start分支执行空分支退出补丁；野外起式转换仍可能重访，但无同一补退出门。',
 '现行§10及CV-M19e/f/CV-M22明确训练家前提；有效18夹具的empty_branch_revisit字段是重访阶段标签，并没有统一声称野外也插退出。'],
 [src(conv,[[997,1133],[1499,1569],[1683,1751]],'old conversion + trainer-only empty branch patch','六族转换与只处理训练家空分支是不同门。')],
 [spec(wp75,'§8.2/§10',[[192,209],[257,264]],'泛称重访说明须按具体训练家补丁读。'),spec('test-catalog/demo-dx-wp72-73-74-75-76-77.md','CV-M19e/f、CV-M22、B20-C034',[[170,170],[173,173],[291,291]],'具体空分支向量给TrainerBattle；B20补充不废止其限定。')],
 '不能仅凭较宽泛摘要或fixture字段名立必修；具体合同足以排除“所有野外空分支必须补退出”的读法。可在root编辑其它句时顺带明确，但无独立必修。',
 ['野外单/双/三两轮仍无训练家补丁；训练家默认第二轮、插命令同轮。此处全为静态推导。'],
 [{'path':'review/remediation/20261003-prepare/batches/B20/author-draft-1/six-family-fixtures.json','version':'3f521e6dea0b442e4bb174a9715c458416386b37','actual_read_scope':'all18 objects','result':'各核心/默认/可败三列按其族有序转换；revisit不等于exit inserted。'}])
ce(6,'narrow_to_optional_clarification','optional','P3',[
 '符合berrytree前缀且不为已加下划线/四阶段名后，替换的是串内每个小写berrytree出现点；事件页引用同样处理。',
 '当前§11并未明确承诺只替换第一处；通常单次出现的CV-M25向量不能推出任意重复串的保证。'],
 [src('020_Debug/003_Debug menus/008_Debug_FilenameUpdater.rb',[[1,89]],'filename and event graphic replacement','全文件独立读，入口门与全串替换分开。')],
 [spec(wp75,'§11',[[266,273]],'使用前缀插入下划线概括，无“仅首次”断言。')],
 '源事实确认，但现有文字至多未显化窄重复字面变体，按optional而非已证事实矛盾；不复制为新的M12B发现。',
 ['berrytreeOakberrytree.png → berrytree_Oakberrytree_.png；已berrytree_前缀仍被门跳过。','精确四阶段名保持；不外推大小写或目录遍历规则。'],[])
ce(7,'exclude_required_revision','no_required_revision',None,[
 '地图事件驱动依序执行通用35替换等步骤；公共事件的后段只调用fix_event_use后按changed保存。',
 '当前§10完整顺序已把两类入口分开，公共事件缺通用35替换步骤可以直接由该具体管线推得。'],
 [src(conv,[[1683,1751]],'complete main converter driver','直接阅读全文驱动，地图序列与公共事件单步分支。')],
 [spec(wp75,'§10',[[257,264]],'地图包括旧用法替换；公共事件列另一条fix_event_use管线。')],
 '排除必修。括号未逐一列所有省略步骤不构成与明确管线相矛盾的保证。',
 ['含通用旧标识的公共事件与地图事件分别遵各自pipeline；不可从同一个修复helper推得全部前置转换相同。'],[])
save('counterevidence.json',{**base,'observations':cs,'decision_counts':{'confirm_or_confirm_narrowed':4,'no_required_revision':2,'optional_only':1},'scope':'Seven root observations independently counterchecked; no parent summary treated as independent source evidence; no root files modified.'})
