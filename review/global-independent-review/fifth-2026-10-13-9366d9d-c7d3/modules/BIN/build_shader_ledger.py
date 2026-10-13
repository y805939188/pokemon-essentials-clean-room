"""Read-only extraction and sanitized shader audit ledger; no compilation/rendering."""
import pathlib,json,re,hashlib
O=pathlib.Path(__file__).parent
r=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Game.exe').read_bytes()
blocks=json.loads((O/'block-inventory.json').read_text())['blocks']
programs=[]
for b in blocks:
 if b['kind']=='embedded_shader_text' and b['id']!='B52':programs.append((b['id'],b['offset'],b['size']))
short=json.load(open('/tmp/gr5-bin-readable/short-code.json'))
for i,b in enumerate(short[:-1]):programs.append((f'S{i:02}',b['offset'],b['size']))
main={
'B01':'纹理坐标先判断x≤288且y≤384，满足时加水平动画偏移；再用已经改变的x判断384≤x≤512且y≤384，满足时加垂直偏移。两个判断顺序相关，不是互斥分类，没有下界检查。几何位置先加translation再由projMat投影；纹理坐标逐轴乘texSizeInv。',
'B02':'将纹理y/128朝0截去小数得到自动元件索引，先读取7项帧数表；余数为动画序号减去“帧数×朝0取整的整数商”，再以朝0整数商拆成8列布局的行/列。仅在x≤96且y≤896时，给x加96×列、y加32×行；但帧数读取/除法不受这个条件保护。几何加translation后投影，纹理乘逆尺寸。负坐标、零帧数、索引7或更大都未在程序里保护；不能将条件乘0误当短路。',
'B03':'几何位置先经spriteMat再经projMat；基础纹理坐标乘texSizeInv。renderPattern为假时不写图案坐标。为真时令s=patternScroll×patternSizeInv/texSizeInv，平铺分支输出(texCoord/patternZoom−s)×patternSizeInv，非平铺分支改乘texSizeInv；均逐轴计算，无零尺寸/零缩放保护。',
'B04':'把纹理坐标乘sourceSize后加半像素，分出小数相位和整数像素基点。横纵各取索引0至5（偏移−2至3）的核权重并各自除以其总和；采样基点在整数位置减半个texSizeInv，36个RGBA采样作可分离加权和。无显式颜色钳制、采样边界保护或总权重为0救援；sourceSize和texSizeInv是独立输入。',
'B05':'采样RGBA；按亮度系数(0.299,0.587,0.114)求灰度并以tone.w在线性色彩与灰度间插值；加tone.rgb；alpha乘opacity；RGB最后按color.a向color.rgb插值。无范围钳制，color不改变alpha。',
'B06':'与B05相同顺序：采样、灰度、加色调、alpha乘不透明、覆盖色；最后再按flash.a向flash.rgb插值。闪光晚于覆盖色，也不改变alpha。',
'B07':'source在输入纹理坐标采样，destination在“坐标减subRect前两项、再乘后两项”的坐标采样。令a=源alpha×opacity、b=目标alpha×(1−a)，结果alpha=a+b；若恰为0则RGB取源RGB，否则RGB=(a×源RGB+b×目标RGB)/(a+b)。零alpha仍保留源RGB；无显式alpha范围保护。',
'B08':'读取transMap红通道m，把m夹在[prog,prog+vague]得到c；alpha=(c−prog)/vague。当前画面向冻结画面按该alpha插值。vague=0时程序自身没有处理除零；参数归一化、纹理匹配和实际分支选择由原生消费者决定，未证。',
'B09':'采样后将RGB转HSV，在色相分量上加hueAdjust，再转回RGB；保持原alpha。颜色转换函数单独列明，输入hueAdjust在这里不做角度单位转换或范围钳制。',
'B10':'顺序为：采样主体；renderPattern真时用图案坐标逐轴模1采样，以图案alpha×patternOpacity为插值权重，patternBlendType=1用加法、=2用减法、其它用普通覆盖；再按(0.299,0.587,0.114)灰度插值、加tone.rgb、alpha乘opacity、按color.a覆盖RGB；invert真时RGB各变为1−分量；最后草丛alpha乘夹在[0,1]内的(bushOpacity+指示量)，指示量仅在纹理y<bushDepth为1。等于深度走较暗分支；图案本身不改主体alpha；单元repeat=(1,1)。',
'S00':'几何直接投影；输出归一化中心纹理坐标和垂直上/下各1像素的归一化坐标。',
'S01':'几何直接投影；输出归一化中心纹理坐标和水平左/右各1像素的归一化坐标。',
'S02':'几何先乘matrix再乘projMat；纹理乘texSizeInv；顶点颜色原样传递。',
'S03':'采样中心与两个模糊坐标的RGBA，等权平均，即三者和除3；没有alpha特别处理或显式边界钳制。',
'S04':'几何先平移再投影，纹理乘texSizeInv，颜色原样传递。',
'S05':'几何先平移再投影，纹理乘texSizeInv；没有颜色传递。',
'S06':'把二维位置补为z=0、w=1后投影；没有纹理或颜色。',
'S07':'RGB为传入颜色RGB乘alpha参数；输出alpha固定1，输入颜色自身alpha不参与。',
'S08':'纹理RGBA采样后仅把alpha乘输入alpha；RGB保持。',
'S09':'纹理RGBA采样后仅把alpha乘顶点颜色alpha；顶点RGB不参与。',
'S10':'输出传入顶点RGBA，不修改。',
'S11':'输出纹理RGBA采样，不修改。最大可打印跨度末端另有单字节I；程序大括号正文到结尾换行已完整审读，不能据该相邻字节断言实际编译输入含I，原生长度参数未追。',
'S12':'输出统一RGBA颜色，不采样纹理。',
'S13':'纹理RGB按亮度系数(0.299,0.587,0.114)求灰度，以gray参数线性插值；alpha不变，无显式钳制。',
'S14':'在冻结画面与当前画面的RGBA之间按prog线性插值：0冻结、1当前；prog没有在文本内部夹值。',
'S15':'使用固定管线模型视图投影矩阵转换顶点，传递固定管线颜色。',
'S16':'输出插值颜色RGBA。',
'S17':'固定管线模型视图投影转换顶点，传递颜色和第0纹理坐标的前两分量。',
'S18':'纹理RGBA采样后先把alpha设1，再逐分量乘顶点颜色；原纹理alpha被忽略。',
'S19':'纹理RGBA逐分量乘顶点颜色，保留纹理alpha的作用。',
'S20':'要求外部图像扩展GL_OES_EGL_image_external，使用samplerExternalOES采样，再逐分量乘u_color；扩展或纹理可用性不是明文程序能证明的事实。',
'S21':'纹理采样RGBA，alpha强制1，再逐分量乘u_color。',
'S22':'纹理采样后交换红/蓝通道，alpha强制1，再逐分量乘u_color。',
'S23':'纹理采样后交换红/蓝通道，保留alpha，再逐分量乘u_color。',
'S24':'纹理RGBA直接逐分量乘u_color。',
'S25':'输出u_color，不读纹理。',
'S26':'角度属性第0项作为s，第1项加1作为c；围绕a_center把位移(dX,dY)映射为(c·dX+s·dY,−s·dX+c·dY)，再加回中心并由u_projection投影。传递原纹理坐标；点大小固定1。程序未计算三角函数，不能假定传入原始弧度。',
}
constants={
'B01':{'区域A上界':[288,384],'区域C横向闭区间':[384,512],'区域C纵向上界':384},
'B02':{'自动元件数':7,'tileW':32,'tileH':32,'单元宽高':[96,128],'区域宽高':[96,896],'动画偏移单位':[96,32],'动画每行列数':8},
'B04':{'核半宽':3,'最小绝对参数':0.00001,'圆周率近似':3.141592654,'每轴采样数':6,'像素中心偏移':0.5},
'B05':{'亮度系数':[0.299,0.587,0.114]},'B06':{'亮度系数':[0.299,0.587,0.114]},
'B09':{'转换偏置组1':[0,-1/3,2/3,-1],'转换偏置组2':[1,2/3,1/3,3],'除法保护增量':1e-10,'色相扇区数':6},
'B10':{'亮度系数':[0.299,0.587,0.114],'重复周期':[1,1],'混合编号':{'1':'加','2':'减','其它':'普通覆盖'}},
}
coef={
'A':{'offset':[0,-0.501960814,-0.501960814],'rgb_rows':[[1,0,1.402],[1,-0.3441,-0.7141],[1,1.772,0]]},
'B':{'offset':[-0.0627451017,-0.501960814,-0.501960814],'rgb_rows':[[1.1644,0,1.596],[1.1644,-0.3918,-0.813],[1.1644,2.0172,0]]},
'C':{'offset':[-0.0627451017,-0.501960814,-0.501960814],'rgb_rows':[[1.1644,0,1.7927],[1.1644,-0.2132,-0.5329],[1.1644,2.1124,0]]}}
for i in range(14,32):
 bid=f'B{i:02}'
 if i<=22:
  c='ABC'[(i-14)%3];layout=['三个平面，各读红通道','Y读tex0红，U/V分别读tex1红/alpha','Y读tex0红，U/V分别读tex1的alpha/红'][(i-14)//3]
  coords='Y用原纹理坐标，U/V用原坐标乘UVCoordScale；该量须由独立前缀提供。';color='v_color'
 else:
  c='CBA'[(i-23)%3];layout=['Y读u_texture红，U/V读u_texture_u的alpha/红，u_texture_v虽声明但未使用','Y读u_texture红，U/V读u_texture_u的红/alpha，u_texture_v虽声明但未使用','Y/U/V分别读三个采样器的红通道'][(i-23)//3]
  coords='各平面都用相同v_texCoord；采样器自身尺寸/归一化约定未在该函数内验证。';color='u_color'
 constants[bid]=dict(coef[c],coefficient_family=c)
 main[bid]=f'{layout}。{coords}把采样得到的YUV加offset，再与rgb_rows各行点积得到R/G/B；alpha先设1，最后RGBA逐分量乘{color}。所有常量逐项列在constants；矩阵构造的列序已换成输出通道的行表，未把GPU列序误记为行序。无条件分支、显式输出夹值或错误回退。'
func={
('B04','lanczos3'):'先取输入绝对值并以10⁻⁵为下限，令t=3.141592654乘该值；权重为sin(t)·sin(t/3)/t²。此函数本身没有半宽之外归零分支；实际六点采样范围来自main。',
('B09','rgb2hsv'):'用绿色与蓝色的大小先排序，再与红色比较，确定最大分量V、最小分量与色相扇区偏置；色差D=最大−最小，饱和度=D/(V+10⁻¹⁰)，色相为相应扇区偏置加通道差/(6D+10⁻¹⁰)后取绝对值。灰色D=0也经过同一保护除法。两次step分支在相等时取≥侧。偏置常量0、−1/3、2/3、−1见constants；这是RGB→HSV的文本运算，不证明GPU精度。',
('B09','hsv2rgb'):'把色相分别偏移1、2/3、1/3后取小数部分，乘6并减3取绝对值，再减1夹到[0,1]；在白色与该三角波RGB之间按饱和度插值，最后乘明度。色相用周期小数自动环绕；饱和度/明度未夹值。',
}
rows=[]
for bid,offset,size in programs:
 data=r[offset:offset+size];text=data.decode('ascii');fn=[]
 for m in re.finditer(r'\b(void|float|vec[234])\s+(\w+)\s*\(([^)]*)\)\s*\{',text):
  name=m[2];start=text.count('\n',0,m.start())+1;lev=1;q=m.end()
  while lev and q<len(text):
   lev+=(text[q]=='{')-(text[q]=='}');q+=1
  params=re.findall(r'\b(?:vec[234]|float|int)\s+(\w+)',m[3]);behavior=main[bid] if name=='main' else func.get((bid,name))
  if bid=='B10' and name!='main':
   if name=='blendNormal':behavior='不带权重时结果直接取图案RGB；主体参数不参与。'
   elif name=='blendAdd':behavior='逐分量（标量重载为单值）将主体与图案相加，上限截为1；不设下限。'
   elif name=='blendSubtract':behavior='逐分量（标量重载为单值）将主体减图案，下限截为0；不设上限。'
   if len(params)==3:behavior+='随后以opacity在主体值与该结果之间线性插值；权重未钳制。'
   if m[1]=='float':behavior+='该标量重载没有在本块main中直接使用。'
  assert behavior,(bid,name)
  fn.append({'name_for_trace':name,'parameter_names_for_trace':params,'return_type_for_trace':m[1],'lines':[start,text.count('\n',0,q)+1],'behavior':behavior})
 interfaces=[]
 for m in re.finditer(r'\b(uniform|varying|attribute)\s+(?:(lowp|mediump|highp)\s+)?(\w+)\s+(\w+)(?:\[([^]]+)\])?',text):
  interfaces.append({'role':m[1],'precision_qualifier':m[2],'type_for_trace':m[3],'name_for_trace':m[4],'array_size_for_trace':m[5]})
 rows.append({'id':bid,'offset':offset,'size':size,'sha256':hashlib.sha256(data).hexdigest(),'review_extent':'full','interfaces':interfaces,'constants':constants.get(bid,{}),'functions':fn,'evidence_level':'supported_static_program_definition_only','failure_boundary':'没有执行或编译；实际纹理绑定、过滤/边缘策略、uniform值、前缀组合、GPU精度及原生选择入口未证明。'})
# Independently visible preprocessor fragments; byte spans from fixed R.
frags=[]
for pid,off,n,desc in [
 ('P01',10582784,155,'若定义GLSLES则声明默认浮点精度mediump；否则把highp/mediump/lowp三个限定词定义为空。只影响编译环境，不自行选择宿主渲染器。'),
 ('P02',10678624,24,'定义FRAGMENT_SHADER宏；该片段没有main，也不证明在哪个程序之前拼接。'),
 ('P03',10678656,15,'定义GLSLES宏；与P01的条件语义相连，但原生拼接顺序未追证。'),
 ('P04',11657192,89,'把二维采样器和二维采样操作名替换成矩形纹理对应形式；UVCoordScale设0.5。影响B14–B22的色度坐标及采样接口。'),
 ('P05',11657282,25,'UVCoordScale设1.0，与P04形成可读替代前缀；选择条件未知。')]:
  data=r[off:off+n];frags.append({'id':pid,'offset':off,'size':n,'sha256':hashlib.sha256(data).hexdigest(),'review_extent':'full','behavior':desc})
(O/'shader-behavior.json').write_text(json.dumps({'schema_version':'gr5.review.v1','program_count':len(rows),'long_program_count':28,'additional_program_count':27,'records':rows,'prefix_fragments':frags,'not_a_claim':'系数/参数语义不等于当前Essentials必用该渲染路径；无编译、参考、模型、宿主执行。'},ensure_ascii=False,indent=2)+'\n')
print('programs',len(rows),'functions',sum(len(v['functions']) for v in rows),'prefixes',len(frags))
