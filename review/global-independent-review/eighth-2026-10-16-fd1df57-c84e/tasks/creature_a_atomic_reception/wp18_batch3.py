"""Manual WP18 copy/owner/provenance/size and remaining clauses; no business run."""
from pathlib import Path
import json, datetime
O=Path(__file__).resolve().parent
P='deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md'
ROWS={
229:['普通复制保持个人身份数值','区别新建重新随机PID/IV'],
231:['clone新建iv表并复制六主能力值','clone新建ivMaxed表并复制六键值','clone新建ev表并复制六主能力值','moves外层新数组','每个Move对象clone独立','Move身份保留','Move当前PP保留','Move提升计数保留','first_moves克隆外层','owner对象clone独立且四值相等','ribbons克隆外层','随后一方字段或其新容器改变不自动改另一方'],
232:['数值身份/形态/等级经验/HP/状态计数按复制时值保留','来源记录当前值保留','昵称/球/友好/PID当前值保留，不推字符串深克隆','未重建markings数组共享','未重建fused个体引用共享','未重建mail对象共享','通过共享对象原位改动可被对方看见','仅替换本方引用不等于改共享对象，正常Mark整体赋表可分离引用'],
233:['两对象初PID相同','Owner四值初相同','保留的派生缓存初相同','相同未缓存输入产生相同派生结果','后改PID不自动清已有缓存'],
237:['复制不重新随机IV','复制不重新初始化MovePP','复制保持当前来源记录','复制保持当前HP','复制保持当前异常'],
238:['一方改PID不自动清另一方缓存','一方改species不自动清另一方缓存','两对象数值缓存字段各自独立','复制保留的可变对象仍有共享边界'],
239:['普通clone本身不发事件通知','普通clone本身不登记图鉴','不同于显式form提交副作用'],
247:['正常Owner.id整数','正常Owner.name字符串','正常Owner.gender以0/1/2表示男/女/未知','正常Owner.language为语言编号','正常输入域不等于构造校验逐值取值范围保证'],
248:['语言取值按Owner构造路径区分','不能统一成每次构造都读取宿主'],
249:['直接Owner语言采用传入整数'],
250:['训练家转Owner复制当时id','复制当时name','复制训练家type派生gender','复制当时language','Trainer默认language来自宿主映射','已改language复制改后值','该转换不重读宿主'],
251:['外来Owner语言省略取2'],
252:['四个独立字段setter采用显式传值','每个setter只校验并写自己的字段'],
253:['Owner语言与UI消息语言索引不同','后续UI切换不自动回写已存Owner语言'],
254:['构造请求四项类型校验','独立四setter请求各自类型校验','普通等值Hash实参条件由后项保留','整数名字等于后gender或language可遮蔽String条件','构造(0,0,0,2)名字0被保留','构造(1,0,0,2)名字0被保留','构造(1,0,1,2)String检查仍存在因而失败','该失败在四字段赋值前','正常字符串名字仍按String条件接受','此为有界构造事实，不扩大任意散列/自定义相等输入'],
255:['单独name setter仍独立检查String','对合法Owner写名字0报错','该失败保留原name','Pokemon创建接已有Owner不递归复验内部','畸形Owner不因此保证所有后继成功','未来兼容畸形输入是独立产品决定'],
256:['外来ID由player.make_foreign_ID产生32位','该ID循环直到不同玩家ID','外来Owner构造默认名字空串','默认gender2','默认language2'],
257:['Owner public_id取低16位','Trainer还有取高16位secret_ID入口'],
258:['给ID0x12345678低16位是0x5678','该值十进制22136'],
262:['owner=仅接受Owner类别','非Owner在引用替换前报错','成功仅替换引用不重算','不显式图鉴登记','不清派生缓存','已缓存异色保留','未缓存异色以后按新Owner参与求值'],
266:['孵化把Owner改为玩家快照','孵化清昵称','孵化写happiness120','孵化写方式1'],
267:['交换写外来Owner且采用对方名字','采用对方gender','写方式2','新物种输入创建后reset_moves','既有Pokemon路径不reset','完整演出及进化先于最终party槽替换'],
268:['snag捕获写玩家Owner','普通捕获没有同样Owner改写'],
269:['外来赠送Owner默认空名','该包装默认gender0而非Owner.new_foreign默认2','已有个体的来源方式保留','物种新建先按命运开关得方式0或4','完整赠送仍按其独立容量/命名/图鉴合同'],
270:['partner注册逐成员Owner转为伙伴训练家','每个Owner写后重算','本次非外来只相对伙伴训练家，非相对玩家保证'],
271:['调试Owner可改为玩家','仅调试入口，不当正常取得流程'],
279:['方式0表示遇到','方式1表示蛋来源/孵化','方式2表示交换','方式4表示命运相遇','UI显示0为Lv遇到','UI显示1为收到蛋','UI显示2为Lv交换','UI索引3为空行','UI显示4为Lv命运相遇','该正常域不夹制所有直接obtain_method赋值'],
280:['obtain_map存地图编号','非空obtain_text显示优先地图名','该显示用来自自定义文本语义'],
281:['获得时刻存整数秒','孵化时刻仅方式1读取','其它方式返回nil','其它方式下写孵化秒数不改变读取门'],
282:['方式1展示孵化日期','方式1展示hatched_map地点'],
283:['默认所在球POKEBALL','捕获写实际ball身份','友好正增量读取LUXURYBALL标记作奖励','所在球不同持物字段'],
284:['孵化写方式1','孵化写hatched_map和孵化时间','交换写方式2','MysteryGift写方式4/获得时间/地图','装蛋工具写obtain_text','调试可写方式0/1及清孵化图','普通创建默认独立'],
288:['foreign默认训练家全局player','ID与名字都相等才非外来','任一不同为外来','gender不参与','language不参与'],
289:['ID同名字异为外来','ID异名字同为外来','ID名字同而性别语言异仍非外来'],
290:['已定位服从性消费foreign与等级/配置','完整服从门由WP40定义','调试显示也消费foreign','目录不声称其它消费者已穷尽'],
294:['有非空昵称返回昵称','无昵称返回本地化物种名'],
295:['nil昵称清空','空文本昵称清空','等于当前物种名清空','清空后name回物种名','其他文本本setter不截断','10字符上限由具体输入入口负责'],
296:['外来赠送非空昵称截到10','命名入口传10长度上限','输入控件实际边界依WP17','givenicknames非0跳过询问'],
297:['height从当前简单形态物种读','height单位0.1m','weight从当前简单形态物种读','weight单位0.1kg','独立mm辅助另用IV/PID','mm输出不覆盖height/weight字段'],
298:['装蛋包装通常赋Egg名','孵化清昵称','清后显示物种名'],
304:['这是可得数学辅助能力而非默认玩家流程证明','输入H为有效整数0.1m高度','输入P为合法32位PID','输入六原始IV','输出整数mm','不抽随机','不写个体状态','不读EV','不读level','不读表现Nature或计算Nature覆盖','不读强化IV标记','固定rb检索只有定义','地图/Demo/plugin/动态caller仍未知','不强制未来同名接口'],
306:['六IV分别取低4位0..15','攻击余数异或防御余数后乘HP余数','该乘积再异或PID最低字节为B','特攻余数异或特防余数后乘速度余数','该乘积再异或PID次低字节为C','异或是整数位运算','乘积不先截断','B/C均0..255','s=256B+C在0..65535','PID高16位不参与'],
308:['每段选择A/D/T','先q=A+floor((s-T)/D)','再M=floor(q*H/10)','两整数阶段不可合并','H仍是0.1m单位而非mm','表区间含两端并覆盖合法s'],
328:['默认段起点65410','默认段T为65510','负的s-T是合法数学输入','不能补不存在1600/1650新段','不能把默认段移到65510才开始','H7/IV0/P0得s0/q290/203mm','P2304得s9/q299/209mm','P2560得s10/q300/210mm','给零IV且P=256*(s mod256)+floor(s/256)可构造任意合法s','全端点导航至15成对向量'],
330:['静态数学前提是有效个体','原始IV/PID须合法','H须有效整数','非法字段/缺物种不建立新恢复合同','未知用途/未来产品范围未决','所有尺寸向量NOT_EXECUTED','没有调用参考辅助/独立模型'],
334:['完整合法个体持有基species','持有存储form','持有Owner记录或正常占位','持有PID','可由exp沿有效成长曲线换level','不把构造失败半对象当成功个体保证'],
335:['正常来源方式域0/1/2/4','孵化时刻读取受方式1门'],
336:['换Owner不追溯清派生缓存','foreign仅ID与name'],
337:['异基species=默认形态优先','否则目标正形态','否则原形态','同基身份先早退'],
338:['三入口差异按表成立','simple不handler','simple不登记','simple不清ability缓存'],
339:['普通clone保PID','保Owner四值','保IV','新建重抽PID/IV'],
340:['昵称等于物种名视无昵称','未命名按物种名读取'],
341:['命运开关开创建方式4','否则创建方式0','只在创建时读该开关条件','后来开关变化不主动改原个体','事件运行实际未验证'],
345:['严格get未知物种报错','try_get等入口缺失可nil','创建走严格查找'],
346:['创建/设置等级越界报错','范围由GrowthRate.max_level接口决定'],
347:['owner=非Owner在替换前报错','构造仍保留的条件失败在四字段赋值前','同值Hash遮蔽例外独立','四个setter分别校验并在字段写入前失败'],
348:['species=同基形态键不改形态'],
349:['动态相同结果不提交','显式同值提交仍handler/重算/登记','创建复检返回同值仍显式提交'],
350:['共享清单之外不扩大全字段保证','未逐一核全部共享对象后继则保留准确未知'],
351:['cannot_*仅定位调试写入','仓库/队伍UI读这些标志','正常事件/plugin写入未知','搜索未命中不证明不存在'],
352:['超长字符串直接name=保原文本','具体入口截断合同不推广给底层setter'],
358:['命运开关创建0转4'],359:['givenicknames非0跳询问'],360:['昵称输入上限常量10'],361:['装蛋新建等级取EGG_LEVEL'],
363:['孵化/交换/礼物各自显式覆盖方式','之后命运开关不会主动改这些已写方式','事件实际组合未执行'],
380:['正常cannot_*写入者未定位，需精确负证据域'],381:['事件脚本直接字段写面未穷尽','完整赠送交换/捕获caller各有主合同'],382:['共享引用清单不是全字段穷尽保证'],383:['命运开关Demo事件触发缺实际工程证据'],384:['Owner外其它语言消费者尚需独立接合'],385:['跨文件形态继承值须实读编译层及实际数据'],386:['全部本文件静态无运行确认','所有场景为静态设计']
}
ADMIN={264:'Owner变更表列标题。',310:'尺寸分段数学表列标题，后续各参数/端点实际拆分。',356:'配置表列标题。',367:'CI01–31具名案例与覆盖主题导航；实际31个案例各须独立接受，本导航不授测试运行。',369:'四个Happiness作者静态案例导航，不授执行或创建流程全通过。',371:'五个尺寸与15成对端点案例导航，全部NOT_EXECUTED。',375:'上游依赖路由WP03/WP02/WP06，不替代实际内容接收。',376:'完整跨域依赖路由；不是相应领域已接受的状态声称。'}
# Hand-entered mathematical segment facts; each tuple has distinct semantic roles.
SEGMENTS={312:(0,9,290,1,0,290,299),313:(10,109,300,1,10,300,399),314:(110,309,400,2,110,400,499),315:(310,709,500,4,310,500,599),316:(710,2709,600,20,710,600,699),317:(2710,7709,700,50,2710,700,799),318:(7710,17709,800,100,7710,800,899),319:(17710,32709,900,150,17710,900,999),320:(32710,47709,1000,150,32710,1000,1099),321:(47710,57709,1100,100,47710,1100,1199),322:(57710,62709,1200,50,57710,1200,1299),323:(62710,64709,1300,20,62710,1300,1399),324:(64710,65209,1400,5,64710,1400,1499),325:(65210,65409,1500,2,65210,1500,1599),326:(65410,65535,1700,1,65510,1600,1725)}
for line,(lo,hi,a,d,t,qlo,qhi) in SEGMENTS.items():
    ROWS[line]=[f'本段s从{lo}含起点',f'本段s到{hi}含终点',f'A取{a}',f'D取{d}',f'T取{t}',f'低端q为{qlo}',f'高端q为{qhi}']
def contract(ln):
    source=['Pokemon complete1227L + ShadowPokemon complete override','Owner/Move/Trainer/Pokedex/Storage complete files','Trading and EggHatching complete files','Utilities_Pokemon complete292L','Species/GrowthRate/FormHandlers complete source']
    if ln>=304 and ln<=330: source=['Utilities_Pokemon pbSize243–272 complete definition','Pokemon height/IV/PID source complete','actual literal caller-search io/size-caller-search.json']
    pending=[]
    if ln in [271,284,290,351,380]:pending=['exact complete debug Owner/source/cannot_* tools and obedience consumers not yet read; source definitions/normal acquire/hatch/trade are independently read']
    if ln in [284,363]:pending+=['Data/Scripts/016_UI/024_UI_MysteryGift.rb complete reward mutation/claim caller still to read']
    return {'source_units':source,'named_received':['UI P/S/B/D/E complete contributions','KERNEL VAL/LANG/SAVE/SP/EVT complete facts','CORE CAR-CRE11 + CAR-CAA4','UI-BF55'], 'premises':'固定普通字段与合法成功个体/合法IV-PID高度；direct容器与普通UI替换入口区分；无反射/plugin覆写；明确负例按其有限普通整数/文本域。','normal':'采用上述完整实际源顺序，Owner与PID缓存、同对象/clone容器与引用分别观察。','cancel':'克隆/字段/尺寸定义无交互取消；昵称拒绝/交换演出/孵化后昵称按实际caller，先写前缀不回滚。','failure_partial':'Owner校验先于赋值；保存/场景/重算后段失败不能提升成功；尺寸非法输入没有新容错；其它具体失败仅按到达写点。','consumer_chain':'创建/clone→Owner/字段或共享容器→Trading/Hatching/Utilities/CatchStore→Party/Storage→Pokedex→UI→SaveData注册load；native引用保持仍未执行。','open_exact':pending,'business':'NOT_EXECUTED'}
def main():
    a=json.loads((O/'manual-atomic-clauses.json').read_text());old=json.loads((O/'old-locator-disposition.json').read_text());new=[]
    for r in old['rows']:
        if r['path']!=P or r['range'][0]<229:continue
        ln=r['range'][0]
        if ln in ADMIN:r.update(decomposition='COMPLETE_BOUNDED_TYPE_DISPOSITION',type_disposition=ADMIN[ln],accepted=True);continue
        assert ln in ROWS,ln
        ct=contract(ln);ids=[]
        for i,t in enumerate(ROWS[ln],1):
            aid=f'CAA-W18-L{ln:03d}-A{i:02d}';ids.append(aid);new.append({'id':aid,'old_locator':r['id'],'formal_path':P,'formal_line':ln,'assertion':t,'complete_contract':ct,'parent_decomposition':'MANUALLY_EXHAUSTED_BOUNDED_FORMAL_ROW','source_support':'PARTIAL_EXACT_SOURCE_PENDING' if ct['open_exact'] else 'SUPPORTED_BOUNDED_STATIC','business':'NOT_EXECUTED'})
        r.update(decomposition='MANUAL_EXHAUSTED_BOUNDED_FORMAL_ROW',manual_children=ids,source_support='PARTIAL_EXACT_SOURCE_PENDING' if ct['open_exact'] else 'SUPPORTED_BOUNDED_STATIC',consumer=ct,premise=ct['premises'],accepted=False)
    a['atoms']+=new;a['recorded_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();a['formal_wp18_batch3_atoms']=len(new)
    old['manually_exhausted_locators']=sum(x['decomposition'].startswith('MANUAL_EXHAUSTED') for x in old['rows']);old['typed_dispositions']=sum(x['decomposition']=='COMPLETE_BOUNDED_TYPE_DISPOSITION' for x in old['rows']);old['not_manually_exhausted_locators']=sum(x['decomposition'].startswith('OPEN') for x in old['rows']);old['fully_accepted_locators']=sum(x['accepted'] for x in old['rows'])
    for fn,obj in [('manual-atomic-clauses.json',a),('old-locator-disposition.json',old)]: (O/fn).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    (O/'wp18-batch3-result.json').write_text(json.dumps({'utc':a['recorded_utc'],'new_atoms':len(new),'rows':ROWS,'admin':ADMIN,'contracts':{str(k):contract(k) for k in ROWS},'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'},ensure_ascii=False,indent=2)+'\n');print(len(new),len(a['atoms']),old['manually_exhausted_locators'],old['typed_dispositions'],old['not_manually_exhausted_locators'])
if __name__=='__main__':main()
