"""Static audit formatter. Does not import, evaluate, or execute reference programs."""
import ast, hashlib, json, pathlib, re
OUT=pathlib.Path(__file__).parent
R=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Game.exe')
B=json.loads((OUT/'block-inventory.json').read_text())['blocks']; raw=R.read_bytes()

def data_value(s):
    s=s.strip()
    if s in ('true','false','nil'): return {'true':True,'false':False,'nil':None}[s]
    if re.fullmatch(r'-?\d+(?:\.\d+)?',s):return float(s) if '.' in s else int(s)
    if re.fullmatch(r'[A-Za-z_]\w*',s):return {'由输入取得':s}
    if s.startswith(('"',"'")) or s in ('[]','{}'):
        return ast.literal_eval(s)
    if s.startswith('['):
        m=re.fullmatch(r'\[(.*)\]\s*\*\s*(\d+)',s)
        if m:return {'重复值':data_value(m[1]),'长度':int(m[2])}
        inner=s[1:-1]
        if re.search(r'\.new',inner):return {'顺序表':[data_value(inner)]}
        return [data_value(t) for t in inner.split(',')]
    m=re.fullmatch(r'Array\.new\((\d+)\)\s*(?:\.collect)?\s*\{(.*?)\}',s)
    if m:return {'各槽独立构造':data_value(m[2]),'长度':int(m[1])}
    m=re.fullmatch(r'([\w:]+)\.new(?:\((.*)\))?',s)
    if m:return {'新值类别_仅源定位':m[1],'构造输入':[] if m[2] is None else [data_value(t) for t in m[2].split(',')]}
    raise ValueError(s)

special={
('B11','RPG::Class','initialize'):'先建立基础条目默认值。8×100参数表仅填等级1至99：槽0为400+50L，槽1为80+10L，槽2至5为15+⌊5L/4⌋，槽6至7为30+⌊5L/2⌋；0级保留宿主表初值。经验参数为[30,20,30,30]。顺序添加特征三元组(23,0,1)、(22,0,0.95)、(22,1,0.05)、(22,2,0.04)、(41,1,0)、(51,1,0)、(52,1,0)，不将这些兼容编号解释成宝可梦规则。',
('B11','RPG::Class','exp_for_level'):'把等级L和四项参数b,e,a,c转换为浮点数，返回最接近整数的 b·(L−1)^(0.9+a/250)·L·(L+1)/(6+L²/(50c))+(L−1)e。无等级/参数范围保护，无局部异常回退；异常输入、c为0和非实数幂不保证有效结果。',
('B11','RPG::UsableItem::Damage','sign'):'恢复类型3或4返回−1；其它返回1。',
('B11','RPG::UsableItem::Damage','eval'):'在可见a、b、v的当前求值环境解释公式文字，先把结果下限截为0，再乘恢复符号；被该局部救援捕获的异常返回0。没有按目标属性另算伤害，也没有在这里应用暴击或方差。公式可有副作用；不执行它。本处救援不是所有异常类型的普遍保证。',
('B11','RPG::UsableItem','number_of_targets'):'范围编号3至6返回编号减2，即1至4；其它编号返回0。',
('B11','RPG::Weapon','initialize'):'承接装备/基础条目的默认值；再添加特征(31,1,0)和(22,0,0)。',
('B11','RPG::Weapon','performance'):'八项参数全数求和，再额外计入索引2与4；无钳制或异常救援。',
('B11','RPG::Armor','initialize'):'承接装备/基础条目的默认值；装备类别改为1，添加特征(22,1,0)。',
('B11','RPG::Armor','performance'):'八项参数全数求和，再额外计入索引3与5；无钳制或异常救援。',
('B11','RPG::Enemy','initialize'):'承接基础条目默认值；三份掉落条目彼此独立，初始动作一份；添加特征(22,0,0.95)、(22,1,0.05)、(31,1,0)。',
('B11','RPG::Tileset','initialize'):'8192项标志表：索引0设16；2048至2815及4352至8191设15；其余由宿主新表默认值决定；九个图像名称为空。',
('B11','RPG::Map','initialize'):'保存宽高并请求四层数据表；创建事件空映射、遇敌空表及默认音频。构造所写战斗背景字段名为floor/wall，而可读写接口为battleback1/2；后两者未在本构造赋值。不能替它们补默认空字符串。',
('B12','RPG::Actor','initialize'):'6×100参数表仅填等级1至99：槽0为400+50L，槽1为80+10L，槽2与3为15+⌊5L/4⌋，槽4与5为20+⌊5L/2⌋；0级保留宿主表初值。',
('B12','RPG::Troop','initialize'):'建立空成员表；默认页面引用BattleEventPage，本块仅定义嵌套Page。若环境没有提供该名称，此构造在建立页面时失败；本块未局部捕获。宿主是否另提供该名称未知。',
('B12','RPG::System','initialize'):'建立系统默认值及8192项通行表；sounds由空表顺序加入20份独立AudioFile。船、舰、飞艇分别新建；标题/战斗音乐与结束乐使用不同音频包装类别。',
('B13','RPG::Actor','initialize'):'6×100参数表仅填等级1至99：槽0与1为500+50L，槽2至5为50+5L；0级保留宿主表初值；默认等级上限99、经验基数/增长30。不是宝可梦种族值或经验曲线。',
('B13','RPG::Troop','initialize'):'建立空成员表；默认页面引用RPG::BattleEventPage，本块只定义Troop::Page。若环境未补该名称，则构造失败且不局部救援；不据此认定当前游戏必然报错。',
('B13','RPG::Tileset','initialize'):'七个自动元件名称由同一个空字符串重复填入，初始槽位共享该可变字符串；三张384项表分别供通行、优先级、地形使用，仅把优先级索引0写为5。雾默认不透明度64、混合0、缩放200、滚动0。',
}
cache={
'self.load_bitmap':'资源键为目录与文件名直接拼接的路径；缺缓存或已释放则重建。空文件名请求32×32空位图，其它请求路径位图。色相0返回基础对象；非0用(路径,色相)另建克隆并改变色相，之后复用未释放对象。无缺文件救援、引用计数或复制返回保证。',
'self.tile':'以(文件名,图块号,色相)为缓存键；缺项或已释放时创建32×32位图。令n=图块号−384，来源列为n模8、来源行为⌊n/8⌋，各乘32；从Tilesets资源复制32×32再改色相。没有负号、范围或缺图检查。',
'self.clear':'把缓存替换为空映射并请求垃圾回收；未逐项调用位图释放，不等于同步销毁外部仍持有的对象。'}
for name,folder,hue in [('animation','Animations',1),('autotile','Autotiles',0),('battleback','Battlebacks',0),('battler','Battlers',1),('character','Characters',1),('fog','Fogs',1),('gameover','Gameovers',0),('icon','Icons',0),('panorama','Panoramas',1),('picture','Pictures',0),('tileset','Tilesets',0),('title','Titles',0),('windowskin','Windowskins',0)]:
    cache['self.'+name]=f'把文件名送入Graphics/{folder}/资源缓存；'+('显式转交色相。' if hue else '使用默认色相0。')+'没有另外的搜索或异常处理。'
for k,v in cache.items():special[('B13','RPG::Cache',k)]=v
sprite={
'initialize':'先构造宿主精灵并转交可空视口；白化、出现、逃离、崩解、伤害、单次动画计数均为0，闪烁关闭。循环动画/伤害子精灵未在此创建；共享动画身份表与位图引用计数在定义期各建一次空容器。',
'dispose':'按伤害数字、单次动画、循环动画顺序释放附属表现，最后调用宿主释放；中途异常没有继续清理保证。',
'whiten':'设置普通混合、白色覆盖且alpha128、精灵不透明255，白化计数16；清零出现/逃离/崩解三个计数；不清伤害、动画或闪烁。',
'appear':'普通混合、无覆盖色、不透明0，出现计数16；清零白化/逃离/崩解。',
'escape':'普通混合、无覆盖色、不透明255，逃离计数32；清零白化/出现/崩解。',
'collapse':'混合编号1、覆盖色(255,64,64,255)、不透明255，崩解计数48；清零白化/出现/逃离。',
'damage':'先释放旧数字。数值显示绝对值，非数值转文字；请求160×48位图、Arial Black字号32。正文在(0,12)区域160×36居中，四个对角偏移±1绘黑边；负数正文(176,255,144)，其余白色。critical为真时另在顶部160×20绘字号20的CRITICAL，黑边后白字。子精灵用同视口，原点(80,20)，坐标(x,y−oy/2)，z3000；持续40次更新。字体命中/最终像素未证。',
'animation':'先释放旧单次动画，再登记输入；空值立即返回。保存命中标志和帧数，按动画名称/色相取资源，位图引用计数先增1。通常建立16个同视口、共位图且初始不可见的子精灵；位置编号3且同动画已在共享身份表中则不建子精灵。未登记的动画加入身份表；立即显示第0帧并处理定时事件。抑制分支仍增加引用但无第0子精灵供释放路径递减，定义级不配平。',
'loop_animation':'与现有循环动画相等则完全不变；否则释放旧值，空值返回；索引归0，加载资源并增引用，始终创建16个初始不可见子精灵；立即更新第0帧。零帧数未在这里拒绝。',
'dispose_damage':'存在数字子精灵才依次释放其位图、子精灵，再清空引用和持续计数；不存在时不操作。',
'dispose_animation':'有子精灵表才清理；仅第0精灵存在时递减其位图引用，计数恰为0才释放位图；随后逐子精灵释放并清空表和动画。空表不递减；未直接清零持续计数。',
'dispose_loop_animation':'与单次清理相同的第0精灵引用计数条件；最后清空循环表与循环动画；未重置循环索引。',
'blink_on':'关闭到开启才把闪烁计数置0；已开启重复调用不重启。',
'blink_off':'开启时关闭并清空覆盖色；已关闭不修改其它色彩。',
'blink?':'返回闪烁开关，不计算是否当前可见。',
'effect?':'六个计数（白化、出现、逃离、崩解、伤害、单次动画）任一大于0即真；循环动画和闪烁不参与。',
'update':'先调用宿主更新。依次更新白化/出现/逃离/崩解，各先减计数：经过k次更新后分别请求覆盖alpha=128−10k、不透明=16k、256−10k、256−6k。超界是否被钳制属于宿主。伤害先减计数，剩余38–39上移4、36–37上移2、34–35下移2、28–33下移4，其余不动；不透明请求256−32(12−剩余)，到0清理。全局帧号为偶数时单次先减后更新；循环先更新当前索引再加1并对帧数取模。闪烁最后覆盖颜色：计数加1模32，alpha=6·|16−计数|，RGB白；最后清空共享动画身份表。因此开始时已显示循环第0帧，下次合格更新仍先显示第0帧；同帧抑制范围随每个实例update清空，不是全局帧锁。',
'update_animation':'持续值大于0时取“总帧数−剩余”的帧，更新16槽，再按原顺序处理所有frame相等的timing；否则释放单次动画。没有数组越界救援。',
'update_loop_animation':'用当前索引取帧并更新16槽，按原顺序处理该帧所有timing，命中参数固定真；推进和取模发生在调用者update。',
'animation_set_sprites':'逐索引0至15读取图样；缺精灵、缺图样或图样−1时隐藏存在精灵并跳过。每格192×192，五列，裁切列=图样模5、行=⌊图样/5⌋；原点(96,96)，z2000。位置3：有视口用(宽/2,高−160)，无视口用(320,240)；其它位置取本精灵裁切中心，0再上移高度/4、2下移高度/4。之后加单元偏移；缩放=第3项/100，角度第4项，镜像只在第5项=1，不透明=第6项×主体不透明/255，混合取第7项。超出−1的其它负图样未单独拒绝。',
'animation_process_timing':'条件0总执行，条件1仅hit严格为真，条件2仅hit严格为假，其它不执行。非空SE名先向Audio/SE/发出音量/音高请求；再按flash_scope：1闪主体，2仅有视口时闪视口，3主体以空颜色闪（隐藏请求）；其它无闪光。持续时间一律乘2。声音失败无局部救援，可能中断后续闪光。',
'x=':'计算新旧x差；差非0且动画表存在时，对单次及循环表各访问全部16槽并加差，最后设置主体x；不跳过空槽。因此被全屏抑制而留下空表时，平移路径可能访问空值；damage子精灵不跟随此路径。',
'y=':'同x的差量传播规则用于y；单次和循环各16槽，最后设置主体；空表/空槽没有保护，数字子精灵不随之移动。'}
for k,v in sprite.items():special[('B13','RPG::Sprite',k)]=v
weather={
'initialize':'初始类型/数量/偏移均0。创建雨7×56、暴雨34×64、雪6×6位图：雨为7段、每段1×8白色阶梯；暴雨32段每段高度2，中间白两侧alpha128；雪的半透明矩形为(0,1,6,4)/(1,0,4,6)，白色核心为(1,2,4,2)/(2,1,2,4)。创建40个精灵（表索引0至39），各z1000、不可见、不透明0；此时不绑定天气位图。',
'dispose':'逐40个精灵释放，再释放雨、暴雨、雪位图；无重复释放保护或异常救援。',
 'type=':'相同类型直接返回；不同类型保存值，1/2/3选择雨/暴雨/雪位图，其它选空。循环索引1至40，只对非空槽设置可见=(索引≤max)及位图；实际第0槽永不被这里更新，索引40为空。类型0也没有单独强制隐藏所有槽。',
'ox=':'输入等于现值直接返回；否则保存并把所有40个精灵原点x改为该值，不重抽粒子坐标。',
'oy=':'与ox相同，更新所有精灵原点y。',
'max=':'原始输入等于现值即返回；否则把数量夹在0与40之间，按索引1至40更新存在槽的可见性。最多39个实际槽被启用，第0槽保留原状。',
'update':'类型0立即返回；按索引1至max处理，遇空槽中止。雨每次位移(−2,+16)、不透明减8；暴雨(−8,+16)、减12；雪(−2,+8)、减8；其它类型没有上述运动。随后若alpha<64，或相对偏移后x<−50/x>750/y<−300/y>500，则重置为x=偏移x+随机整数[0,799]−50、y=偏移y+随机整数[0,799]−200、alpha255。边界相等不触发；重新产生的y可达599，下一次可再次越界；不证明随机种子或宿主像素。'}
for k,v in weather.items():special[('B13','RPG::Weather',k)]=v

records=[];access=[]
for bid in ('B11','B12','B13'):
    b=next(x for x in B if x['id']==bid);data=raw[b['offset']:b['offset']+b['size']];lines=data.decode('ascii').splitlines();positions=[];q=b['offset']
    for line in data.splitlines(keepends=True):positions.append(q);q+=len(line)
    stack=[]
    for i,l in enumerate(lines):
        s=l.strip();ind=len(l)-len(l.lstrip())
        if re.match(r'(class|module) ',s):
            while stack and stack[-1][0]>=ind:stack.pop()
            stack.append((ind,s.split()[1]))
        if s.startswith(('def ','attr_accessor','attr_reader')):
            while stack and stack[-1][0]>=ind:stack.pop()
            scope='::'.join(v for k,v in stack)
        if s.startswith(('attr_accessor','attr_reader')):
            access.append({'block':bid,'line':i+1,'scope_for_trace':scope,'field':s.split(':',1)[1],'access':'读写' if s.startswith('attr_accessor') else '只读','behavior':'直接暴露对应字段；本声明无验证、计算或副作用。'});continue
        if not s.startswith('def '):continue
        name=s[4:].split('(')[0];end=next(j for j in range(i+1,len(lines)) if lines[j]==' '*ind+'end');body='\n'.join(lines[i+1:end]);key=(bid,scope,name)
        rec={'id':f'{bid}-F{sum(x["block"]==bid for x in records)+1:03}','block':bid,'source_scope_for_trace_only':scope,'function':name,'lines':[i+1,end+1],'byte_range':[positions[i], positions[end]+len(data.splitlines(keepends=True)[end])],'review_extent':'full','evidence_level':'supported_static_definition_only','consumer_selection':'待交界映射；名称不是未来架构建议。'}
        if (bid=='B11' and i+1>=872) or (bid=='B12' and i+1>=919) or (bid=='B13' and i+1>=1466):
            rec.update({'review_extent':'full','review_origin':'inherited','inherited':'../RES/reading-coverage.json#/extra_embedded_audio_ranges','behavior':'复用RES已审音频尾部准确行范围；本次重新核对整个块的字节哈希，无重复全文审读。'});records.append(rec);continue
        if name=='initialize':
            fields={}
            for m in re.finditer(r'^\s*@([A-Za-z_]\w*)\s*=\s*(.*)$',body,re.M):fields[m[1]]=data_value(m[2])
            rec['default_data']=fields
            rec['inputs']=[]
            args=re.search(r'\((.*)\)',s)
            if args:
                for a in args[1].split(','):
                    a=a.strip().split('=',1); rec['inputs'].append({'name':a[0].strip(),**({'default':data_value(a[1])} if len(a)==2 else {'required':True})})
            rec['behavior']=special.get(key,('先承接父级已述默认值，再' if re.search(r'^\s*super\s*$',body,re.M) else '')+'为新数据记录建立所列字段默认值。来自输入的值原样保存，不深复制传入容器；对象/表的构造请求按default_data记录，不补不存在的校验、域规则或持久化；这些构造器本身没有局部异常救援。')
        elif key in special:rec['behavior']=special[key]
        else:
            inc=re.search(r'\[([\d, ]+)\]\.include\?\(@(\w+)\)',body)
            eq=re.search(r'@(\w+) == (\d+)',body)
            if inc:rec['behavior']=f'仅当字段{inc[2]}属于数值集合'+str([int(v) for v in inc[1].split(',')])+'时为真；其它值为假，无状态修改。'
            elif eq:rec['behavior']=f'仅当字段{eq[1]}等于数值{eq[2]}时为真；其它为假，无状态修改。'
            else:raise ValueError(key)
        records.append(rec)
obj={'schema_version':'gr5.review.v1','purpose':'函数逐项静态审查账本；源名称仅定位，不是迁移代码或未来类设计。','source':'R/Game.exe','source_commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','scope':'三块完整明文，RES音频尾部精确复用；构造/公式/分支/资源请求均有解释。','records':records,'accessors':access,'global_limit':'宿主版本选择、原生表/色彩钳制、求值器/资源加载的实际行为未执行且不由明文定义反推。'}
(OUT/'script-behavior.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print('functions',len(records),'new',sum(x.get('review_origin')!='inherited' for x in records),'accessors',len(access))
