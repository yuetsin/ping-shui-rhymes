# -*- coding: utf-8 -*-

import rhyme_words_tc as rhyme_words


def PingShuiYunInit(sheet, mainIndex, secondIndex, Chars):
    i = 0
    while i < len(Chars):
        oneChar = Chars[i]
        if oneChar in "[]":
            i += 1
            continue
        if i != len(Chars) - 1:
            if Chars[i + 1] == '[':
                polyDesc = ""
                j = i
                while Chars[j] != ']':
                    j += 1
                    polyDesc += Chars[j]
                sheet.append(rhyme_words.rhyme_word(
                    oneChar, mainIndex, secondIndex, polyDesc))
                i = j
            else:
                sheet.append(rhyme_words.rhyme_word(
                    oneChar, mainIndex, secondIndex))
        else:
            sheet.append(rhyme_words.rhyme_word(
                oneChar, mainIndex, secondIndex))
        i += 1


def get_sheet():

    allSheet = []

    PingShuiYunInit(allSheet, 0, 0, "風中空紅東同翁公宮通窮功雄工鴻叢蓬終融濛虹童桐蟲匆弓蒙戎忠瓏豐[豐收]隆崇穹櫳篷躬攻驄葱衷筒籠瞳楓聾銅聰充朧熊洪逢[鼓聲]峒[崆峒]嵩忡烘礱窿曨菘僮冲[深遠、淡泊]癃幪茸嵷芃曈恫仝盅悤崧筩[竹筒]矇馮[姓也]瀜夢[音蒙]絨騣璁朦訌蘢艟[艨艟，戰船]螽潨瞢[目不明]嚨狨谼侗[倥侗]翀藭棕霳潼葒鬉葓渢懵[懵懵，無知貌]雺氃蠓豵豅潀攏[音聾。理也]痌爞穜瘋罿烽酆巃种[音蟲。稚也]饛朣韸嵏艨芎螉總[縫也]瀧[雨瀧瀧]曚崆蝀酮髳灃哄[同叿，言語嘈雜]髼蚣駥葼篊逄[鼓聲]獞漴[水聲]肜硿悾娀珫茙犝渱玒緵[縷也，緵罟也]堫汎[音馮。亦浮也]懜鼨蓊衕菶涷烔[熱貌]鬷[釜屬]箜匑稯洚氋茼惾麷鍐愡[惺愡]靀鯼膧[肥貌]釭[轂鐵]罞塳鬔埪篵龐[充實]艐懞橦[木名]嗡谾蠪倥[倥侗]囱漎[水會也]哃蕫摓狪柊靇涳茺檬烿眮鏓憽絧倲叿鵼碽蔠詷浺檧鉷鶇魟猦靊鎓蝬菄霟蓪鮦[魚名]爖龓蘴鄸檒鴤寷繱痋餇錝灴偑蕯埄揔秱堸襱杛仹娻崠[山名]屸徖樋爜汷樥熢碂熜愩粡囲鸗勭瓨浲鶲熥湰嵡焪葻糿艂朡篢粠嘃疘曧鯟仜棇楤娂翪濍猣漨赨焢闂幊鑨硹鸏埬熍漗䧺㤝䃧䓗䮾㰍㚇䧆䕺㹣䯷㴦㣉䀄䙦䤓䆍㒥㳘䥂䞑㸗䂫㠦㼿㼧䍶䩺䪦䆔㮬䈦䵄㦕䅝㥖䁓䰸䈵䫹䈡㲁䐋䗓䟥㩚㨑㝫㠮㚅㠉䡯㠓䏊䆪䆚䴀㓽㕼䖝㒶㢥䰒䉺㺋䰤䮵㝟䴶䈺㕬㵯㳞䲨䡫䴿䧷䱵㣝䤝㓚㭜䝦䪊㣭䲲䑃㖓㦀䘪㙹㜴䒠㝘𦨴𩐠𢫨")
    PingShuiYunInit(allSheet, 0, 1, "峰龍容松蹤重[重複]濃鐘從[服從]封蓉宗逢胸鍾冬農慵筇鋒庸舂儂供[供給]凶恭悰雍溶蜂蛩墉穠鬆茸縫[縫衣]鎔醲衝[要衝]烽傭鏞兇邛淙邕忪鼕龔淞縱[縱橫]琮顒憧[意不定]喁[噞喁]彤饔籠[音龍。竹名]榕丰[丰采]癰共[敬也]噰卭洶跫鬃葑[菜名]噰廱蛬[通作蛩]匈賨鱅鎔蘢訩壅[與雍通]艟[艨艟]禺[音顒，越地名]咚鏦憃[騃昏也。或作憧]瑢摏嫞樅籦鄘鬞褣磫膿橦恟蓯[肉蓯蓉]蹱桻瞛蕹彸媶庝崶澭[水名]銎憹齈舼噥瑽傛伀摓躘鏧蝩浵臃漨凇佟妐蚣滽徸褈妦捀驡蕽搈犎孮鑫鉵浲縙郺誴鉖襛槦炂熧欁赨倧桏龏髶禯詾緟炵緃篈隀嵱[山名]蹖銿笗鰫夆榵痋鷛衳嫆穁堼蚒倯鸗暰灉賩檂媀髸苳慒[慮也]鍶刣婃䂌㲨䯳䗤㿈䗦䅃䧡㮪㧭㠽䡮㡣䘬䐫䳷㚵䗥䇀䅊㸼䀱㞱䙂㤏㴩㺎䝑㲇䌬䰌䳋䊄䳯㙡㣑㽫䆹䥢㜂䗬䤊䣏䃔㜉䇯㹐㫒䢉㣠䡴㐯䳉䡥㝐㟾䠜㷭䩼䗸䳍䂈䈶㢕㶻㮤㜡䢼㬝㫡䢨㼸㻾䡆䶱䇗𩂓")
    PingShuiYunInit(
        allSheet, 0, 2, "江窗雙邦降[降伏，降下]缸幢腔龐[高屋，又姓]撞扛艭厖淙釭[鐙也，一曰轂鐵]矼瀧[奔湍，又州名]杠樁尨摐哤茳鏦憃[愚也]逄[塞也]駹跫瑽谾庬玒樅[通摐]羫肛漎[水會也]梆椌洚噇狵痝蛖橦[帳極]豇刅悾[音腔]舽娏鬃噥[嗔語，語不明]啌囱涳跭栙魟愯胦憹峕垹浝牻膧[膧腔]佭孇堫鸏瓨欆訌㟅䉶䎫䵨㼻䜫䝄䁸䢶㼹䚒䄝䤸㟌䚎䆫㾤䜶㤶㒕䉘䚗䓼䭚㧿䃥")
    PingShuiYunInit(allSheet, 0, 3, "時詩知枝期遲之奇悲絲師池姿思移垂離宜疑眉辭誰隨持為[作為]馳詞衰癡兒卮碑旗夷吹儀危祠籬私欺滋支棋巵遺湄窺披茲斯墀嬉帷漪芝疲追規資施頤卑差[參差]基羈涯飢[餓也]虧岐脂炊怡皮熙嗤麾肌陲維陂慈璃灕伊醫茨螭曦蕤龜司累[係累]姬咨錐緇脾葵其歧髭雌欹彝尸釐飴疵颸巇痍推[順遷也，類推]迤[委迤，自得貌]尼糜縻羆攲騎[跨馬，動詞]夔貲隳羸狸箕貽篪肢治[理也]逵而蘺萎[蔫也]鴟彌綏楣麋羲笞鸝澌[水索也]椎醨媸洟[鼻液]噫[恨聲]綦陴屍嘻梨崎蛇[委蛇]洏匙嫠胝罳裨醾咿猗貔毗罹淄惟萁禧瀰[水曠遠之貌]鷀孜嵫蓍榱嵋比[比鄰]菑蚩緌錘鬐姨獅蘼犧隋絺祺鷥居[語助辭]祇耆麗[高麗]怩坻[水中高地]訾瓷騅祁圯扅嶷[九嶷]眵魑氏[月氏]耔[音茲]敧[以箸取物]齊[衣下曰齊。又與薺通]書[音詩]縭褷輀丕孳[生息]僛犂[牛駁]槌蜊祗琦驪篩崖邳凘坯攡黐蜞葹熹鎚提[羣飛貌]埤梔倕匜跜禆氂[犛牛尾也。又與釐通。]踦[蹇也]鰭玼瓻撝塒畸漦罷釐廝粢錙馗[與逵同]磁蠡[谷蠡。瓠勺]睢琪菭痿輜娭犄淇僖嚱[口聲]賫詒[相欺也。遺也]紕騏鈹脽鮞戲[嗚戲，歎辭]麒眙[舉目貌。又縣名]伾坨嬀鸃玆偲[偲偲，相切責也]厓茈踟黟禕戣鰣庳[下也]褫箠[節也]縲蚳蓰諆簃鼒壘[重也。又與累同]泜寅[音夷]埼觿妮釃栭倛胹甤觺髵鴯耛纚蘄[蘄茝也。求也]絁壝餈虒騤椸鵻椅[梓也]呞犠咦榿台[我也。悅也。]呢逶雖椑[木名]獼骴宧魌鎡郿稘委[委蛇]翍錤罙犛[牛黑色]貤濉劘黧琵黴趑酏唲耏峗溈鉟荽劙蔂爢郫鯔秠熺陑丌劑[翦齊也]錡蚭薋阰濰腄跂唯觜被[荷衣]緦枱訑狉饎鈚齍襹剞蛦觭榰駓嗞禔禠覗鍉娸鳷椔螄蜲衼噅甀倠轜偨蚾恞誺頯虆跠豾欙齹媐陭岯頄峓芓阺嵯[㠁嵯]鈈樆旇瓵疧鶥洢摫梩箷厜仳仔[克也，任也]吱茬詖蚑蚍栘胰蜘謻呲剺枇蠵踑觶螷孋蜱鵯呸躨鮧鵹鳲圌[山名]嫢腝虮甾禗鮍蟕簛縒齝夊誒犪孷膍瞡姕嗺鴺栺蠀姼苤鬾狓愢桋悂髬隹謘齜蘪萓璂蕬沶鶅鰦婎滖羠楑鐁毞蓶鰤軝掑桸蠝廲磃柂[木名]荾彽拸醚琟柌蛜熪銔轙燍攗荎謧荋爔浬鈭譩肶鯬芪鯕鼺袘嫘厶榹糦螔篃蜤擟芕瓃騩堳槻筣蟖桵嫛蟍娺犤纗暿濝紎郪秪衹鄬鸓諰崥[山足]攠眱倁璾稵篅蚔澬戂藣鶳魾袻魮讉耚檹啙艃箈菞洈杘蘳萆柅巙脪鉹怌猍娞錍鵸蔩薺巸倭侕飺穲怟恑妛眭諀徛瞦鶀瞝蟣邿蒒悘騦媊欐[屋棟]怶抾愭垐貾敮鈶抳鑴顀屔搋鴲鄈杒鬹麎猸剘陏嬨猚峏檇睝鄑瓍蚽鋖寪秓恖躸鮨錅鼶猈諅徥泀葿鳺籾狏萑葰蓷浽綥婑糸覹呰旖矖瑡嚟訵槣馶珆鑗趍[趍趙]惢聏魳湤簊亓苼湷墮矀濨寲臸秖藄抷秛瞴鵧焁跢荲醀胂鏔忯綨暆鶗鍦溡楒秜狋刕伎胔夂覣她鼭炋瑂瓕奞篺榯栥溮汖趀羛鋫鸍鳾隓乁侇孖汥箄[捕魚具]扺誃駍焷禌袲欈粸酈猉沘䍦㕒䂓㜷㒧㕧㒿䧅䲭䙰䴊㮰㶟㱦䬐㔣䤈䕻䱌䔟䨨䳢㬢㖇㠌㺔䔮䜔䡋㞴㤵䬜䧳䴽䥴㝖㿲䱘䩟䇪䀵㮛㾨䮊䈘䝷䲑䂀䓡㷰㥓䛴㽧䊷䇁㞿䴧㫅䳠㰨㺇㴯㽡䝝㨢䉻㲠䚿䊳㢑䅲䲉䧌䙹䂣䌤㣍㯄㠼䅔䊍䍘䓋㟚䇫䴻㯦䌳㹫䅑㐌䝴䥯䪹㞢㦾㫷㙓䯱䐖䖽䣽䖪䘒䲬䶔䎩䶴䧝䔆䞅䳄㚝㚦䕳㔭㗓䆅㩼㔻䅻㿳䮔䭨㞾䎟㠿䎠䬮䙙㺿䮆䋩㱆䞚㰎㲤㮃䧶䳫㸏䫠䶵䫏䛐䝚䩓㧫㺨㩽㣦䡳䈕䣎㴲䮈䶆䖒䫑䭶㺰䪧䑴㘂㰘㗪㮕䊚㖢㺈㸟䌕䜅㹎䟀䄬㰻䵹㽻㨳䫋䞾㰞㻟䐅䄜䩭㰚䣫䋥䧴㖷䓜䶞䎱䥸㯅䟚䪎䱈䙾㬐㜯䭣䧦㩾䖿㷢䲹㚀㒋䣡䛂㮅䕤䗐㲍㽄㘹㺣䲿䑊䳡㛓䉲㚸䨏䬁䫢䭼䟸㶨㓟䢫㼢𩅰𤪌𥯨𠠍𪗋𧩹𠻗𢓡𡖂")
    PingShuiYunInit(
        allSheet, 0, 4, "歸飛衣[衣服]微稀非机扉違暉機肥依輝圍磯威霏闈薇揮菲[芳菲]幃希畿妃晞徽璣幾[微也]譏饑[穀不熟]旂欷祈騑圻鞿緋韋腓沂巍翬睎唏淝馡頎豨囗煇蜚[與飛通]葳蝛誹狶褘痱[風病]嘰埼皈禨溰俙譩巋婓鵗耭厞悕溦湋騩[山名]騛犩浠郗蜰鬿烯裶蟣鐖蚚莃楲刏僟楎婔肵鰴魕靟奜媁琋灳椲喡鍏潿媙岓癓渄媈蟦鯡飝瀈隇覹屄玂矀鰄猆郼餥禈㣲䢜㟪㱕㚻㹆䩁䇵㙨䧇㳖㹷㟓㩣䓅㫵䟇䒾䪰䈈㵟㥋㫎㙎䬠䥩䉠䖷䙟㠻㛄")
    PingShuiYunInit(
        allSheet, 0, 5, "書餘魚居如疏廬初虛車除舒渠裾墟鋤閭余蔬漁予[我也]輿徐胥躇儲諸驢蕖梳歟噓歔琚蜍璵攄譽[動詞]鉏旟蘧畬豬樗狙袪于[歎辭]趄與[語辭]祛於菹蛆紓篨瀦臚且苴据[拮据]雎沮茹淤櫚疽鶋滁袽蒢妤磲洳驉挐魖砠綀箊帤櫧鴽畲糈璩呿藘蝫岨咀屠[休屠]慮[思慮]舁諝阹鋙醵胠櫫涂藷湑腒蝑伃鸒雓疋耝衙[衙衙，行貌。]齬瘀鐻摴籧鴡蒘蚷椐憈璷艅爈楈蜛抾蕠匷崌淭螶狳豦俆鵌嬩坥唹懙鵨菃侞捓婮曥伹硢捈捒涺鮽鱋櫖筎麆謯筡瑹偦籅蒣桇豠娪邚稌劯藇藸魼揟鷠郚紶㠊䃴㞐䕡䱬䈝䠧䱉㭬䝻㺞䥚㧧䔡䪶㝒䈌䣰䍱䱷䡤㯫㾒䟊䰻䢸䧾䋈䏣㡹㠠㥠䝣䘫㶛䣷㭕䮉䐳䅕䁩㱺㣄㯉䓚㽰䬔䊰䆽䂛䒧㻬㶆䐗䗨䰕")
    PingShuiYunInit(allSheet, 0, 6, "無圖湖夫孤珠都隅壺徒殊途枯須儒呼娛蘇俱蕪符愚扶衢烏趨軀吳奴株雛虞蒲爐區腴駒糊梧驅膚徂胡紆姑臾躕吾鳧吁迂涂乎塗沽廚敷模朱拘謨壚襦誅盧濡蘆樞誣癯逋鋪[鋪蓋]租楡鱸姝渝竽酥瑚晡臞狐辜嶇鴣弧盂粗顱銖輸孥摹需艫劬芻污[污穢]孚嗚趺愉毹諛巫轤屠于醐踰觚萸兪菟瑜逾揄殳雩酤桴俘菰痡繻歈郛盱蛛殂鼯嚅駑貙嵎蛄呱刳蒱玞蚨餔窬荼禺瘏酺覦矑苻鈇鏤洙櫨罛幮趍[俗趨字]瀘褕牾圩纑莩瓠跗鶘駼唔嬃櫥闍柎笯喁[聲相和]枹瞿穌旴圬毋芙麩絇罦玗摸[同摹]菇邾硃蝓荂稃懦孺葫茱莆於蒩瘉陬膜[拜也]諏蔞杅鴝娵瓿軥氍鰅羭戵帑邘洿箍鸕姁齬酴猢鼩浯嫫箛痀醹鋘玈軱騟嵞趎顬惡婁句母喩趣[與趨通]嘟嘑蝴匍稌軲齵跦跔鮬睮呋朐獹峬珸釪柧瓐粰獳苸邞癒峹膴殍澞腢幠鄜楰媀湡雽嘔鑺婁咕蠕菩葡侏喣隃謼虖胊歍鎢砮孵謣滹榑慺扜蠼牏欨欋攎鰞庯鑐荴犓鱬蠦堣媰冔氀廔膢袾蘛櫯鯆鸆蜈鈲氁枎哌魱躣楜薷箶絑螐柨跿陓莁鮢橭陠斪萮鵌鷜鍝虶窏骷歑衧瞜胕懯軤鴮蕍鷵鷡怤泒橾醏漊嬬鵏庩嶀鳺鷋譕鵐曘禂眗豧駯箁盓糐荹畉綒媩墲杸誧蒤灈咮垀虍葄翑鴸廜弙堬貗鶦蜅跍郚鮕蕦酑袧挎洖麆救鯂祦枸彋潳恗燸緰妋墿瑦祩扝衭紑芋桍鵵抭瑹捗緅踙伮憮嚧豠嫴臑姇崳娐陎郙岣玸雐桙騶胍釫娪幁鈽鈷黸捈垺秼紨颫喖葋筟忂軗晇聥穻梌馟愈淲骬譃瘻茣裯[與㡡通]鰸瞴郀璷蓃翵邭瓳麌鄃蛷螸萭鮈璑檡籚㬰㪺䧢䒀䱐㢝䅳䖘䛕㥚䈻䵾䩱㼶䓵䣯䎍㻌㹳䧸㕊䏏㪀㢳㡏䇕䆰㿖䠒䰰䫱䇓䮃㺏䝒㸖㭸㣘䖚㝼䩣䎁㭰㠸㭪㖩䩲㷻䍢㸡㯛㲎㜹㧣㽳㼋䭅䰅䂂䰧䟞䴸㱠䞛䜽䄮㦆㗅㟺㢏㺮㚥䭍㗙䔕㥥䄨䭌䎔㰭㷒䩴䞤㳛䡍㻍䢓䢐㮧㩤㪭䋶䣄㲗䮒㾰䉑䞮䃿䦜䵶㻯䮏䓏䩒㦵䅷䇬㚢䉿䈬䞕㬂䊿䊸㻀䣿㫙䣚䓊䐻㔧䉉䴣㭔㐡㼡䉐㓬𧦝𤝹")
    PingShuiYunInit(
        allSheet, 0, 7, "西啼低溪迷兮栖泥齊題雞堤攜蹄梯凄嘶藜蹊畦萋稽閨鼙躋黎霓圭妻犀倪悽提犂[同犂]韲臍荑鷖鯢猊暌筓鞮瓈梨奎睽奚篦羝稊隮賫蜺醯嵇擠綈鸝麛兒[音霓。姓也]鵜騠麑刲鞞撕黳批鎞氐韲臡齯袿狴粞輗坭[同泥]黧磾鼷蠐驪枅樨詆澌[與嘶同。]觿恓烓折[安舒貌]蠡[瓠瓢]罤瑿緹傒徯乩蠵窐繄霋懠褆醍銻媞巂鑴締鮭柢禔婗瑅緀遆桋邽郳椑[圜榼]偍酅鮧蜺鶗蝭鵹鸂崥[山貌]螇砒趧邌膍屖崹鷉忚棿袛嫛騱藈榽橀彽蝰麡肶謧盠廲豍艩鶈厗胿貕蒾湀鑗錍亝郪玭纗淣聧觬鑙笓鼶啙燍齌睼屔鴺斊奃猰儶豯蒵黊鬹鍗卟焍殹刕渧眱瓗蛂錅徆禵櫅鷤梋眭鑇趆茥珶磃鍷睳惿徲嗘謑驨楏媂銈腣檕釮碮螕梐郋䃜䬾䨑㙠㩦㜎䉫㼰䄢䅅䚣㢴㖒䒊㡙䮘㨒䶒䬫㯇㓳䍕䪢䝴䚷㾷㕃䵩䚜䀘㴝䫣㦒㯕䙵䔶㡗㫝䛊㔒㿽㰿㮷䯓㸄䛱㣢䐎䤍㛷䛏㰀㽯䐡䱱䧑䗗㩗䄺䪡䳶㓾䠁䖙䘽㔸䂑䔣𧋘𠜱𥌛")
    PingShuiYunInit(
        allSheet, 0, 8, "懷佳階齋諧乖排埋淮釵骸鞋街偕崖涯儕霾柴牌槐喈揩豺俳挨荄皆差[差使]鮭歪捱篩薶[古同埋]楷徘齊[同齋]秸褢箄[大桴也]螷痎稭湝啀櫰膎瀤崽睚齜搋祡榸蘹徍摨喍媘誽夈瑎棑娾捚犤掜薢煯膗榽擓徥蝔鶛啡猈諰輫篺猅唻麡淣腉慀溾䕸㠢䡨㗨㪓㥟㦟㔞㪰㾹㜥䁲䔝䃶㾩㨤䍲㨙䨪㗍㼮䓙䓱䴜㜳䙎䯐䳸䂷㩄䬩㾬䃈䡡䚑䱝䠹𥱼佳涯厓蛙娃鮭哇媧蝸騧靫緺徍猚唲芆䦱㰪")
    PingShuiYunInit(allSheet, 0, 9, "來開台[星名，山名]臺才哀苔埃哉萊材猜裁栽胎災垓腮孩財咍皚該荄駘毸陔獃徠擡鰓纔能[三足龞。又三能]鮐炱儓崍賅騋侅邰頦挼菑[同災]薹唉祴思[多鬚貌。]峐騃偲[彊力也]郲欸咳[咳笑]檯剴胲倈毢絯麳郂敱隑鶆籉跆愢懛棶毐颱鯠揌嵦斄烗淶旲珆啋磑睵渽婡溾箂孻賳唻猍琜箈庲倈輫豥奒嬯䑓䰄㶼䐩㜾㬃㯁䋱䚡䴭䠕䠽䱺䪱㸀㰩㰧㨟䅘㙵㾍㾂䬵䤤㒲㱾䞗㚊㷘䧒㱼䶣䯮㱯䀭回杯梅催雷灰徊堆嵬隈摧陪媒頽罍魁瑰枚醅培洄槐[守宮]豗推煤恢隤桅偎煨巍裴詼崔莓胚壞禖佪隗搥縗漼尵霉抔魋鋂虺衃啡賠玫傀崴脢塺磓敦嗺焞盔酶轠蘈悝紑頧慛蓷鎚[鍛也]櫑柸攂蛔恛咴腜羧鐳畾墔毰誒僓弚茴捼鏙蹪痦彽檑鑘椳凗瓃渨愄熣陫荋葨磪錑螚妚陮阫鞼湈燘簂詴鐜烠繢櫆鸓顝鮠棓碨晆揋藬藱鼿鰃廆洃脧坆讉阢儡[敗壞]鴭膭痽謘橔槯䍙䭔㿉䋿㕍㟴㢈䝅䙑㟝䊈䀃㵢㛱㜠㞜䂙㻁䨓䣙䖶䝇㷇䤂䜃㿗䍣㷟㺳㚰㾯㮎䫊㙁")
    PingShuiYunInit(
        allSheet, 0, 10, "人春塵新身眞神親臣鄰貧津頻民巾辰輪賓珍濱秦鱗陳倫仁因辛麟晨淪伸嗔巡宸旬綸勻紳薪茵顰銀均鈞蘋馴峋醇旻申淳唇榛論[同伦]闉循閩筠蒓粼椿囷緡蓴屯臻珉純詢垠皴磷振[厚也]呻遵諄嚬姻寅瞋岷湮裀禋恂漘鶉瀕堙紉踆迍泯嬪彬甄莘燐嚚轔蓁詵珣荀掄璘信[與申同]齗豳狺潾驎畇貞氤逡駪駰繽矉歅絪麇輴夤紃嶙溱甡殷[衆也，盛也]畛肫邠奫洵螓菌[《博雅》菌，薰也]誾竣玢侁犉窀豩鄞矜[矛柄]誾斌郇兟諲蠙殥錞僎娠忞鑌蜦墐[黏土也]轃罠珢翷塡檳瞵袀抻籸旼圇栒桭茞輑鷷笢霦禛筃圳贇朲壣瞤螾繗侲麐橁儐盹箘玭捘汃眒璸礥碅訔玟鞇嗪獜暋盿蔯鶞碖驞緸鷐莙洇衠峮螴峾頵痻棆厸鋆蛝嫃囩壿膞錀搸耣蔩姰駗苠怋砏扟忳栶阠揗閺鷆咰魜鯙憌檈盷凐瀙燊帪裑柛秵瑃瑧鏔曟敒敐胂竴杶鴖慇攽馪搷甐斴陯泿鰆猌毥宒椕陙珒湣疄腀峷蚐杊踚穦堻覠訷夋璡荺姺姄份檭妽狋眴鵢璌鈱芢屾浾籈暙磌馻鯩鳼偱槇殝訰屒薽汮駨顮礗蜠鏻蒖敃縜圁灥囜猵迿莀薼暽欭秂閿昀抿捪嫀樄媋麎珅鍲㕙䑳䞭䄄㻞㲀䰠䟴䖜㡦䍰㡄䥎㝄㧢䋸㝇䆣㵮䣩㛛㙬㔂䁕䙉㟩㝙㵌㟗䯂䮼㰋䎙㘦䈯䝧䓐䠳䇹䢻䚬㰉㨉㭄䋋䃌䀼䖲䈁䣅䐜䡑䘩㑗䡅䳲䘜㫩䓰䧣㞶䞺㥲㡒㰬䔚䊁䨈䅸䪸㖘㚬㫳䢅㾕䧬㽦䐇㛙𦟘𠬍")
    PingShuiYunInit(
        allSheet, 0, 11, "云雲君聞文分群軍紛勤曛勛氛裙墳芬薰焚氳紋醺欣濆熏紜耘斤芹蚊汾芸懃葷筋沄忻殷[衆也，盛也]棼雯緼蕡枌垠昕纁雰齦皸縕麇賁員矄熅狺鼢焄帉羵饙筠鼖觔廑慬蒀獯幩翂炘篔磤棻豶釿餴鄞瘽慇瘟[瘟瘟，小痛貌]鄖黂蝹彣轒馧[馚馧]妘熉蒶昐臐羒汶[黏唾也]馩誾萉衯濦鴍岎溵馚眃鍕溳橨芠桾妢搵肦妏蒑魰秎煇斦鳼愪蒷懄閺馼耺囩菫炆鼤畃妡鴖橒敃蕓梤弅宭葐嚑歏邤鳻堇[黏土也]蚚縜蘄[山蘄，當歸]玟盺訜隫鐼拚閿砏朌[大首貌]鮶錀魵鈖䈥㜏㪊䘇䙧㶏䰚㷊㥯䴦䩿䦩㯣䌲㹞䢵䉙䎹㹜㸮䭻㮗䈽㚃䭽䒺䓄䖐䗼㞣䵫")
    PingShuiYunInit(
        allSheet, 0, 12, "言園源原喧軒翻繁元垣猿煩冤轅暄藩樊蕃幡援[引也]萱鶱諼轓璠燔掀諠番黿鴛蘩反[平反]湲鵷鞬袁沅宛媛蹯墦膰礬爰袢籓蚖怨蜿嫄眢洹攑犍薠煊芫晅騵蠜笲拚[與翻同]阮[五原]喛暖[柔貌]槾甗螈裷貆僠樠咺鐇謜杬榞襎犿蒝瀪蒬鶢楥蓒娮昍喰臗笎瀿愃攐惌鷭琂箮喯靬豲帵佡睷榬蝖羱勫褑瀳橎媴葾翧噃溒鎱吅摱梡妴羳袸邧駌愋鱕抃[連抃，宛轉貌]嬎媗㠾䁔㟲䭈䊟䞿䚙㸋䓂䋦䪤䠝䉒㹇䖠㱪䋣䥉㓩䕰㨜㦥䮳䪛䇾㤋㹉䖤㪟䊕㥳䳦䲮䪃㓺㩮䚭䫶㺕䩩䡝𩒱𩔉𧑒門存昏魂村尊孫根痕恩論温樽坤吞奔盆閽渾昆暾藩屯崙豚捫蓀蹲飧敦墩鯤髡婚侖褌琨塤鵾惇跟噴賁惛垠黁燉沄掄臀璊猻啍輼焞湓飩拫緼芚亹們瘟魨虋鼲嶟軘蜳棔純[純束]囤焜吨蘊炖蜫餛憣搎穈殙弴縕忳噸渀[同奔]混汶[汶濛，玷辱也]吩涒錕錛涽騉豱繜噋驐菎墫鶤旽葐殟槂瓫猑鷷[與蹲通]惀瑥倴瘒撴蒽薞睯菛蟦庉貇喰鐼餫[與餛通]朜踚坉鞎霕怋菕棞禤犜溷[鬱熱也]暋澊黗訰緷轋惃瀳韞婨湣琿闦橔囩泍煾玧忶拵陯痻泿憞婫顐睧䑳䰟㹠䫒㖧䟂䐊㡓䴷㒭㮯㑮㱎䖵㬿㼔䴅㖹䗕䎜䕖䮝䡣䝠㛰㩔㯊䆭䵍䊐㸑㢯䃦㬈㻊㻹㼊䊩䔻𩒱𩔉")
    PingShuiYunInit(allSheet, 0, 13, "寒看安難[艱難]歡殘寛官端闌盤冠[衣冠]干丹餐蘭竿欄乾[乾燥]鸞鞍酸團觀[觀看]壇彈巒玕肝湍瀾漫[水大貌]蟠桓灘丸珊完翰攢單嘆韓鑾槃岏欒刊殫般紈摶棺漙檀瞞鄲跚圞簞瘢杆驩刓繁[馬腹帶]潘磐鑽汗[可汗]謾姍剜攔讙胖鞶襴柈曼[曼曼，長也]奸磻拚攤巑鼾[鼻鼾]髖狻貛嘽番[番禺]絙汍慱頇墁[同㙢]鰻倌芄判[普官切，音潘，正作ꆙ]癱讕癉莞灤襌敦峘鑚鏝邗萑媻囒鞔貆饅顢鏄羱弁[樂也]搬剸撣[音檀。触也。]蹣洹涫眢樠剬渜荁迀幋拌[舍弃]槫攛嬗桉釺皖抏酇嚾豻驒垸悗鳱烷羉豲痑睕豌慲躝鴅捖獌縏跘婠鷒驙籣忓槾貚灓耑灡帵忨貒韊檲褍喰灒窤萈繟竱攼梡羦嫨犿瓛芉塼砃犴酄篅荌搫毌椯繵雗螌鍴蠸褩寏曫臗鱄吅嬏媏雃綄嫥鷤臤矕蒰偳靬聅鬗馯虷鋑帴瀊欗煓穳唌糷暕匰躦雈㡩㨏䜱㙔䕊㠆㒼㣋䖂䐷㐤䪍䴟䵎㽃䀂㫨㗄䊡㟨䐽㥇䝎䃲䵊䙁㙢䃪㿻㸩㱚㗈㶥䒥䉔䦡䮧䝔䧲䱗䯈䗙䗕䝜䆺䡽㛽㠝䢿㘓䈲㢖㱍䊜䬧㿪䜌䑌䒟㩛䝳䈀")
    PingShuiYunInit(
        allSheet, 0, 14, "山間[中間]關還顔閑閒攀斑環班灣艱寰慳鬟蠻頑删彎潺湲殷[赤黑色]菅潸頒鷳患姦扳闤斕鐶孱[窄也]鰥瘝嫻綸[綸巾]鬘般訕鍰跧[伏也]蕳黫圜[繞也]瞷澴閂擐獌憪嬛狦虨癇僝豻鬝虤攽矕狠轘鳻螌眅詽矜[同瘝]澖掔羴朌[頒通作朌]臤肦葌覵馯曫睔譠羥瞯顅靬黰楌藖邖糫婜漹蛝硍㘖䰉㦨㻞㡲䚪䭴䃑䤽䅼䴉㘤㹕䡲㺗䓸㸶㰑㶎䦥䔵㗴㐴㯗䚲䂅䰋㣶䘎𠴨𤸷")
    PingShuiYunInit(allSheet, 1, 0, "年天然前邊仙船眠泉賢煙傳田憐川篇錢緣圓弦連姸懸筵全先顛禪偏鮮鞭遷蓮編千堅肩綿巓旋玄娟淵蟬箋翩牽宣權捐氊椽延鵑穿聯便[安也]煎拳廛騫阡鐫涎專旃焉漣燕[地名]纏躔愆僊虔膻涓鳶韉燃還[與旋同]鈿筌躚詮芊鉛壖湲蜒痊硏[硏究]舷鋋邅埏蠲磚沿闐甄塡濺[濺濺，水疾流貌]荃員乾[乾坤]攣韆鸇堧悁銓棉籩鱣湔鯿褰悛軿翾縣瀍饘咽駢佺蔫癲遄搴平[平平，辨治也]嫣畋戔圈滇顴蚿蜷棬籛儇圜[與圓同]顓漩牷胼惓卷[曲也]璇朘篿鬈孱挻弮揎潺綖蝝楩璿犍湮萹箯塼肰蠙跧蹎佃鼘菸瘨褼櫋眩蜎籼嬛鍵扇攧扁[扁舟]汧梴鋗獧鏈煽諞蠉諓睊豜譞嬋拴澶蝙撋櫞沺蹁瑄零[先零，西羌也]嘕剸歅瓀濱輇仟單[單于]鰱篅懁幵駽岍鬋廯燀猭瞑[與眠通，又弓名、菜名]駩祆扦楄竣胭儃窴婘甂孿狿騝噒枅蜁潫栴媊蟺碝絟捲輧玹勌烻鱄磌莚鐉媔攐栓嗹攓鞙唌餰耑骿蝒琁緶猵輲謰縓矎觠嫥矊翴蠸蹥琕閼[閼氏]羴鷆巏驙鶣鵳楥馢苮蟤媥葲縺犏僆茾蚈諯湶齤鰹盷鄢脠孉梋掔槤齻帴硟屇貚賆葥珗錕嫙鍹灒辿錈嫾鍽鰬腃奱玧璳瑔胘槫肙妶鷒漹惤厧玭詽純[猶全也]愃裫颴玆娫謜椯臤雃宀吅圌[同篅]縳焆繵犈媗豣篶鰁臱虇暷槇碊箞姾摼鄟銒橪頨酀籈揙檈繎忓峑剈娹冿弲閍顅驠牑瑼鋑搷鯅垠瓹騚囨瀳剶杄汘鶰繟絭圱矏酄痃奾棩暶瞤熞瞏黇裐璸翧矔菺姩誸糄珚狋叀芇恮跰薽膞稨鋻傿脧奷檰郔癴瑏嬵葏㫋㾓䳌䅌㘋㳙㙻䒶㨎䚯㟀䔐䁣䀽䰓㭹㒽䏈䌑䂴㝰㔯㰃䟍㦁㥕㫟䇂䗠㼷㩲䋌䱲䌯䳿䠰䃛㲔㵪㓲䏃㳭䟧㢺䊙䋗䶬䀒䚈㳬䛲㘣䡘㼐䙲㮍䮄䀬㒰䀖䥖䡒㡉㷑䢬䲂㢟䗎䚊䮁䲆䣺䕼㿊㹡䗡䳣㮵㮌㗔䟒㾫㩊䘰㝚䥧㛹䑏䳒㢆㳄䙴䔳㜣䳪䉳䢴䲻䆤䨊㶌㒙䙭䁢㶜䚶㟫䄳㢧䧃䉦䃉㕙㿼")
    PingShuiYunInit(allSheet, 1, 1, "朝遙橋消潮霄招寥條腰蕭飄宵簫銷驕搖饒樵苗凋瓢謡橈迢聊嬌綃焦嶢飆韶蕉標邀貂椒燒喬瑤翹堯瀟調[調和]超雕寮澆姚囂軺嶤描僚杓妖鑣遼嬈昭苕彫要[要求]颻梟跳憀髫蜩挑鴞撩譙漂歊貓蕘鷯夭[夭夭]徭翛刁枵窑驍祧僑陶麽[俗幺字]幺嘵漻徼魈料臕僥膋佻痟幖弨趫硝彯晁瀌繇蹺岧憔猺繰熇燋恌穮嶠熛鰩瞧鍬嘹橇喓剽猋祅鼂蕎怊嶕蛸薸繚鏢齠鷦劭獢虈葽鷂燎礁憍飂珧鞗趬鐐鱎轎[小車]獠逍錨佬箾鐎鷮鰷翲僄愮褕嗂摽膘橑嫖訞蟟蟯碉嶛釗髟儦鞽叼揱蠨襓簥呺毊佋噍鄡脁膮暸怮票哨炤癆銚吆笤撬嘄麃虭嫽潚憭藨嵺飉嘌驃[驃姚。]榣敹鶓櫹枖憢蟭驫蛁膫蟂颵蔈憿踃媱嫶瘭鋚爂烑荍瞗幧撨暚廫螵癄髎嘺彇鍣卲燆緰熮穚窷敫婤牊駋岹蓧鮡瞍緢奝褿鸄聎萩尞柖庣篍藃盄莜顠鴁橚翏篻莦顟磦刂玿弴狣啋犥謤蔋宎簝膲镽朷喿橾撽繑筄鄵灬菬鯛焇欩祒豂狕楆匋鎥獥鮹餆旫屪鐈旚皽魒隃贆孂妱璙顤鎐鉊刟穘蓨劁㵳䖴䮽䩦䁘㲖䖢䌃䎄䫞䚻䉼㝯㪣㓮䄏䀉㲵䨅䆙䳂㴅䒒䫿䎗㚠㼼䚺䵲㲬㕥㑾䁃㶮䜍㸈䕯䁭㚋䍃䶰㶾㡻䱔䩌䬙㨱䱁㟹㸛䅺䠛㠒䖺㯱䏆䢪䴩㹦䘟䁧䴛㲈䂏䳩㬸䙅㟘䯾㑸䌭䨭𢿣")
    PingShuiYunInit(
        allSheet, 1, 2, "交巢梢郊茅嘲敲拋蛟包坳苞庖匏爻抄膠肴呶淆胞殽鈔鐃茆筲教[使也]譊磽捎哮凹稍崤嘐蛸茭泡抓骹旓髾跑炰鞘[鞭鞘]鮫虓炮[炮制]咬烋聱髇弰啁磝怓庨瓟咆轇窼脬鵁媌詨勦[勦襲]轈鄛艄窙嚆漅麃撓刨謷枹婋跤筊訬吵犛[長髦牛]颮嵺鵃樔齙硇狍鮹捊[音庖。与掊同。]猇誵鞄鴢鶜軪痚涍髐硣賿謧墽窲梎姣[淫也]佼[與郊同]穘掊[引取也]焇礉[同磽]骲娋觘摷颵渵軳挍尥耖窌頝摎笣爮勽獿郩灱藃脟繷罺鄗[水名]柪罞莦緢泑輎侾芁蹘摮顤宯嵪倄嚗嗃洨顟䫜䬘䘯䞴䜈㹲䫸䍊㺒䟁㤊䍖䮦䉰㬵䩝䂭㫴䰫䈰㿰䅦䄻䃩㮁䢒䴃䋂㤍䈾䂚㶀㕭𥊌")
    PingShuiYunInit(
        allSheet, 1, 3, "高勞豪濤毛袍曹刀騷皋毫桃醪蒿逃遭號[號呼]鰲牢舠陶旄髦韜滔遨褒膏搔操[把持]螯篙槽萄猱饕嘈縧嗷糟熬忉橰鏖壕敖翺艘璈濠臊櫜噑叨羔糕洮薅淘嘷繅囂獒尻颾咷醄綯艚撓螬鼛嚎鼗慆漕[衛邑名]慅魛蚝裯嶆撈啕廒嶅掏謟溞轑[撓也，轢也。]芼驁蟧翿咎[咎繇]簩謷牦檮蜪幍挑[輕儇跳躍之貌]酕裪綢[韜也]嘮睾搯騊呺鏊氂爊澇慒[亂也]槮祹耗[獨貌]癆諕蹧憹軞鷱傮浶嶗髝鷔訄詜夲鄋簝聎橾瑫岕鏪膫巎憥朷蔜抭釖蝚翢臑覒峱鱢褿嵪獓籇髛摮枆鰠嶩鄵椃獋饀嵍滶嫍匋蕔隞蓸槄夵鋾䬞㺜㹗㟉㯾䜊䝁䯌㺀㩝䛌㞵㯥䀞㬔㥰㫦㞪㲏䕅䥝䫽䑹䓘䛝䄚䐬㰏㩠㮘䦋䬢䜮㗦䤾䧫䲏䛬䫨䈱㠙䜎㜖䆁䭷䮯䵅㫞㤒䬭䝥㷮䑬㡟")
    PingShuiYunInit(allSheet, 1, 4, "多何歌波過[經過]河羅和蘿磨跎柯戈阿坡科蓑娑峨荷摩娥梭哦珂魔皤窩訛窠鵝陀螺沱蛾禾駝酡莎呵他鼉挲婆訶麽頗疴渦那痾它苛莪軻哥佗拖牁磋騾馱鞾陁鍋瘥傞薖俄蛇蹉搓鑼囉迤[逶迤，行貌]儺[儺神]矬蝌嶓鹺紽籮娿舸瑳婀蠡[瓠瓢]醝挪蠃挼囮吪艖倭屙鮀趖覼鄱砣沲[同沱]睋犧[酒尊名]劘儸迦唆瘸猧喎番嵯[嵯峨]緺鈋邏茄[茄子]痤嗦碆哪詑伽髿難[同儺]玻蘑堶鸁桫捼盉鴕她岮莏菏獻柁鈛牱阤枷踒玀啵驒菠堝攞騀遳饠髁稞涹皒哬欏繁[姓]砢滒紴迗鴚渮萵虘咃萪鮻鼧袉誐錒鐹氌唩攎啝髍虆簻戨尛攠澕侳搫庹狏蒫戓魤濄鈳橠櫇覣躦翗覶睉妿姀魺嘙跢痑涐酇[酇城]鉫犐鉕蔖楇蚵戂柇枙腡摞咼硪[同峨]踻吔梛崜剆抲珴喛涶䯢㗻䋪䑘䃺㜑䌴䖸㽨䆼䈖䖕㤎䆧㱒䣜䴱䋍㔮䠡㰙䪑㸯㼠䐆䡐䭩䊨㿆䔀䔅䰿䤬䜏䝛㽿㚳䄉䴾㛖㸰㨇㭫㸫䒩䳗䯊㑚㩯㛗䓾㢦䌀㹻䍫")
    PingShuiYunInit(
        allSheet, 1, 5, "花家華斜霞沙涯賒鴉茶嗟車槎紗麻誇芽加遮嘉牙瓜嘩砂笳葩蛇衙邪遐差[差錯]瑕琶夸奢耶叉蛙葭撾蝦拏巴裟些洼丫蟆呀他查娃爬啞谺爺楂罝芭枒窪蝸鋣騧畬[火種]哇窊髽笆椏伽珈媧杷髿檛岈麚琊跏艖茄[荷莖]鞾痂姱杈迦豭枷喳驊笯垞鯊豝柤挐[同拏]緺雅[同鴉]渣揶羓污划[划船]椰闍瘕搽畲[火種]吧爹疤奓猳耞苴媽莎涂[沮洳]溠碬塗荼煆吒茬[斫木]齇嘛荂鉈鍜騢嗏佘蕸齟啦咱叭呿耙粑鏵蹅颬犘皻袈鴐幏蚆釶秅靫鷨舥吾[縣名]玡碴痧樺痲旯蚜唓孲嗻揢鈀畖瘑貑謯閕蒘莗踻錏筢釾蛼胍挓桬譇潖捓硰硨溛抯犽梌粆泇哆褨侉找峫咤抲癿苩謶秺婼袓鋘訍跒蒫蟼膼觰妑疨焻愘簻椵皅釫俹晇煱摦嫬腡嫅蔖誽銟睱椴笌捈夿吪歄腵浾哶諣潳藸咼鎈鴚吙犌燊搲祖[縣名]鉫鍦䴥㲚䗫䨟䔑䃁㜘㧓䂟㿬䑡䠍㚙䶕䶥䄰䁟䈔䅿㠺㳸㛻䫚㾚䵷䯯㢒㰺䫗㭉㢉㭨䵙䦈䪗㝞㠏䣝䕒䩖㤉㗾㦄㗇㸺㧎䔢㸭䐤㸙㚗䛔䠸㖿㽋㹢䐒䏧䍓䯲䔤㗬䶗䓉㪥䯞㦋㦊㵃䖯𣘻𥥸")
    PingShuiYunInit(allSheet, 1, 6, "香長光陽凉鄉堂霜方黃章腸郎芳茫場忙觴狂傷牀荒裳蒼忘王行[行列]妝梁常藏墻房翔塘桑亡央皇揚囊傍[通旁]良嘗量[衡量]羊岡張湘強[剛強]唐漿莊廊康旁昌裝航商將[持也送也]楊浪[滄浪]疆當[應當]祥凰芒望昂妨鴦湯糧棠徨洋娘琅狼詳粱徉坊綱箱煌剛僵璫驤倉簧防篁檣償彰臧殃慷遑襄繮鋩鏘筐糠秧羌鋩穰姜殤肓滂廂榔螿崗瘡潢戕閶惶璋槍猖庠杭頏隍颺蹌彊攘緗暘相艎漳邙鋼璜肪魴驦匡蝗簹喪[喪葬]倡鸘薑汪吭瀼[露濃貌]嫜襠禳麞倀螗螂尪創[傷也]枋泱嬙孀薌勷湟糖娼鶬硠踉纕斨眶愴[悲也]鎗樟盲滄橫逢[音房]稂贜筤霶蹡佯瘍蔣[苽蔣]慶[福也]殭瓤卬鏜雱鐺[鋃鐺]障幫洸蜣罡粻螳膛牂餭艙碭慌桹鞅[馬頸革]搪鑲偟菖杗肮膀煬萇瑲鱨亢[人頸也]忼[同慷]鰉礓鍚桁痒[病也]鄣磅喤輬磺堈嫦堭瑭鴹样[槌也]恇框迒鍠廧鞺鯧搶[突也]鬺蚄鉠鬤崀傏艡笐徬[與傍通]戧莨薔[同蘠，薔薇]軖蟷瑒桄[桄榔]螃畺煻鼚烊嶈洭胱趪蝪衁熿薚枊彭[多貌]昜漒蘉媓蕩[地名，水名]葟彺燙啷嗆彷溏囔鎊饟蹚鰟闛鋃踼劻爿篣傽躟俍蘠蟥儴餦徜橿椋蠰嫏樘棡抰槺蛘魧滳慞癀篬韹蓈筕黆蘘葙螪欀牄翞姎朚鴋弜蚟匨躴蓎磄蔃鷬珖蔏垟犅鱂禓胦鎕汸裮佒砊篖鶶傹錆茪忀琩躿烺矘尙[尙書]膷瑺綡莣邼獚哴鄌鱆恾邟崲撗咉粇埅騜欴瓺氜瓨炚榶妔艆垙羘霷嵢珜絴漮詤瑝蚢縍匚硄僙岇鼞凔鵟盳逿糃牨梉鑶謒皀暲橖鈁穔吂闣禟笀仼漟姯摚軭莔騯貥仰葁勆崵眏錩鸉苀鰑嵣膅騿眻嵻閍牥澢趽駺紻柍羏雵抂蔁胻欜赯獽斻摪淐晿嫝鄺嫎鋿疒邡婸愓諹㡛䍧䵼䁑䀪㫄䄱㽘䵃㝗㞷䅛䀮㙊䞹䥊䝶㠵䒢䛫㾿䯴㐬㼺㡃㼕㤚㱢㑌䲳㱂䅯䩷䢢㫕䍿䌅㦹㵴䗉㦂䪄䠙䒰䭹䗅䦭䯑㤺䊗䣼㾠䵰䬗㥬䗵㢜㾮㭃㹁㟍䏾䍭䀚㼚㨍㢃䌉㜍㭿䩕䧜䱀㭻㮜㝩䨦䮣䑟䡙㽆㟄䕬㲽㤃䠆䖱䅣䊣䅭䆡㙶㑽䆲䄃㶓䉎䐠㝑䔗䧛䌮㲥㚂㿝㿶䅨㹧䘕䯖䳨䮖䕋䗧䮲㹔㩖䣘㰠㽵㳾䉴𦵧𦳝")
    PingShuiYunInit(allSheet, 1, 7, "生聲情明清城名成行[行走]鳴平輕晴驚兵傾榮程橫[縱橫]京英營耕迎更卿盟纓爭精盈兄旌鶯嶸征[征伐]瀛誠楹羹荆衡幷[相從也，合也，兼也]笙評莖烹鯨縈觥酲箏瓊氓萌嬰檠庚呈貞撐晶枰坑擎亨贏泓塋罌獰頳甍攖眀賡睛粳宏籯正[正月]嚶鐺[酒鐺、茶鐺]甥轟櫻蘅鉦鏗餳嬴煢琤錚菁盛[盛受]紘牲盲彭怦坪橙霙禎楨槍[欃槍]閎傖瑛珩丁瞠黥鍧鯖虻棚勍苹訇硜韺綳令[使令]鶄鸚瑩崢鼪騂黌瓔鶊瑩檉璚棖祊抨砰脝鎗猩蟶搶[搶攘，亂貌。]翃瀠怔儜谹鬡麖榜[所以輔弓弩者。]絣吰弸睜喤伻桁搒泙焭睘瞪哼薨[衆也，疾也。]蜻趟澎輣栟裎罃鬇嬛箐鍠姘輷頃瀯宬掁藑洺珵偵拼鍈膨禜鐄盯蟛渹咣濚猙蠑巆浤閛匉鈜浜鉎牼撜諻狌脭醟凈峸猄浾請鴊揁圊擰硼掙磞洴恲耾軯娙牚謍檸鋐鄳嫇誙嫈汯駍虰鼱揘晟硡騯眐筕觲蠳腈彋朾濴賏眳棦瀴啨炡媖蘡憉奟鮃竑佂閍悙鴴攍鑅絾棾媜艵萾稝夐摼嬫挰帲帡[幄也]埩鸉苼輧殅憌倀雃摚橗痭嚝凔琁菮鑋宖饓鑏胻儝呯碤鼆娍廎妔嵤爃鎣郕臤蟼礯殸嬣聇婛鑍聙葏筬揨糽阷鶧銵竀硑碀邟洐俓柍珹寊鶁霐硻殌赹鋞湞汮瓗朠埥篣荿擏姃玶椖湦梈瑝羥泩莔胓靗棈蚲櫿瞏錓褮趽橩錋蝧簈韹葝浭樈砊劥珄埂[坑]麠垶煐烆嘭嗙渶䖟䪫䟫䲔䳟䬝䎕䃘䟓䉚䋊䆑㡕䙖䎴䭢䨍䗈䣐㮄䥋䊒㽒䝼㶈䨎䑫㓌䋫㒌䆸䨝䐵㹹㵬䨉㲆㼇㱶䇇䕦䡠䄘㘇䆖䊔䎽㚚㿮㛁䈍㣜䪯䱢㢬㲰䥰䦫㷣䵞㪅䴍䲼㰢䑉䁎䫆䁐㙃㔙䰃䍔䞓㧍㲂㝁䊅䡩䫺䢚㺸䆵䴤㤣䍬䯒䄓㧸㚾䦕㥊䡰䚘䔊㧶䍵䃷㿘㼩㹴䄇㙚䇸㬹㨕㢣𧭈𨆪")
    PingShuiYunInit(allSheet, 1, 8, "靑星亭靈經冥形醒[醉醒]庭聽屛扃停萍馨零腥齡銘溟汀甁寧刑泠螢坰霆翎欞鈴苓熒婷丁舲廷型廳硎瓴涇俜蓂伶惺鴒軿陘蜓玲醽聆仃嚀竮釘渟蛉螟邢暝令[脊令]囹鯖鉶莛駉瞑鞓箵町軨筳篂娉玎滎蓱鯹酃猩叮鼮嵉蘦鈃駢羚頩綎徑[行過也]詅呤竛聹簈輧娗[娗娗，容也。]爧濙笭娙[漢女官名]楟葶桯昤坽姈拎霝聠跉魿鉼瑆訂圊疔狌嫇帲駖榠甹蕶鋞狑絅鸋蛵砱蝏朎聤荓奵蛢帄柃靪睲鉎紷鎣侀鵧濴熲巠澪獜呬涄榳邒桱坙閝庁艼煋秢顈猽冂耓閮嬣藀鵛褮嵤銒朾諪帡[帲覆也]鏻郱郬衑彾孁龗鹷耵鄍㹶䖅䴇䋼䛣㯪㩕䯕㡵㯏䤰䗌䅽㭢㼛䩠䆨㓅㣔䃏䙥㽮㻂䄙䉹䱓䦺䡿䯍䈂䉖䣆䁝䓑㤯㸳䌢䢛䶄䚖䤯䕘㝕䫤䉁㦭䡼㾉㪮㼗𦀚")
    PingShuiYunInit(
        allSheet, 1, 9, "燈冰僧陵登層能升騰藤凭朋興[興起]曾蒸增憑澄棱乘[駕乘]憎凝繩勝[胜任]鷹蠅膺稱[稱贊]仍承鵬肱嶒丞崩徵應[應當]矜[矜夸]澠罾兢鐙[錠也]昇堘綾鬙繒懲蔆譍[答言也]恆弘縢凌矰烝淩簦緪滕棚謄楞瞢[目不明]礽馮[陵也，馮河]崚鼟疼磳艿鄫淜幐鯪薨輘橧豋扔儚掤堋殑譝姮掕漰噌芿蕄僜碐憕癥薐冫噔鬅睖砯邆倗騬憴竳螣陾畻鞃脀洆儯竑焺奟抍痭璔篜婈竲譄顭苰鹶耺璒裬傰溗辸踜祾漛厷蘉倰穪膯熷膡夌錂焩驓鞥仱覴嬁鵿僌庱栤鱦塴鰧嵭氶敒陹揯㲪䔲䡌㱥䁬䎖㵗䕟䚮㭁䈊䲍㷥䔖䱆䕨䒱䱭㜴㥄䗀㮱䠮㥤䒐䕝䧙䄧㴰䧹䙞㐩䳾䬋䩑䇰䉕䒏䮪㖫䉄䨜㔁䡏㔰㺱㣒㞼㛵𩜁𤮘")
    PingShuiYunInit(allSheet, 1, 10, "秋游流頭愁樓遊舟州畱休憂浮洲求幽侯收丘悠謀牛裘酬鈎羞鷗由周儔修投籌柔稠眸優不[夫不。又未定之辭也]謳溝疇猷甌尤旒囚虬繆[綢繆]邱搜讎仇颼劉漚[浮漚]遒脩鳩郵猶油侔輈騮楸啾陬球矛瘳讎抽喉偷湫猴騶毬飀蝣鎪篌貅篘橊篝耰酋疣髏鍪鄒牟否[未定之辭也]樛呦璆斿緱蕕裯韝咻鶹歐庥彪蜉婁鞲抔鰍麰勾兜鯈諏幬繇婾紬攸糇蟊逑蒐遛裒嚘售鰌鞦罘廋輶鶖摟齁啁艘飂泅鏐桴瀏槱詶饈賙鬮褠涪揉蟉蛑芻癅髹揫窶愀綢溲賕鞧漱崷叟觓揄僂蹂掊[把也]區揪骰琉蝥彄搊螻摳鯫滮吺侜罦掫烰浟菆勠魗丢蔞蝤惆句餿嶁俅鱐冘鍭調[朝也]醅瞀簍謅懮躊譸盩摎絿鵂艛麀鍮酘膢廔瀌妯瑈馗[音求]救萩赳鼽妞泵慺犨飍醧龜[龜兹，國名]鎦鞻莤峳銗鄹棷[木薪]睺葇嵧艀嘔庮錇羺卣琈銶鏉枹鯄瀀騪淍嘍雺颩篼耬瓿蚰硫蝚蓲泃蚯喌芤牏怮厹鯸瘊鴾髟鞣瞘芣鵃秞驫蛷怞恈鰷骺輖鎏慪逌楢鏂堥艽叴塸梂蟱淲枸葔鮂黀漊莍鞪鍒鉜摗頄獀剾鰽疁薵緰渞鄋吥撨蟗沋鮋鷔媃藰犰遱菗鶔鷜燽蒥熡騆烐磂嬦鰸騥鎀牞寠絒醔挎緅瞗腬姇櫙媝帿臹揂郮盚垺朹駀扏犙熮玌渘脜脙麍鰡棸箁恘椆銂苬噍涑煪抭瞴殏郖徟鏅剻浗銝翏訄哹抌穋鋀侸粰朻鑐熰瞍矪汼湭袧裗軥岣紑傮妋烌瞜劺剅珘釚齱鯦哞趜纋薷霌嬼皗樇坄鰇櫾齺膒瑬紌蓅媹篍蓃箃訅萮雔褸筄圳鄾栦鱃捒亠蟭蓨嚋偤糔翵慒[慮也]鴀趥鄇跾唒泑敄剹蛔匬眗釓櫹婤肍㡚䬟㬋䗋㱊㵞䎿䑼䨲䤹䋺㳺㗀㗋㐀䫛㳜䐓㘜䀺㹯㽛㧨㾋䑻㚭䤛㘳㖼䈭䱖㫍䡂㟊䰗㾞㘥䬌㨮䦾䨗㤹㡞㥢䒜㝹㻓䝏㟈䄛䧓㩅䑦䖥㖄䝀䲥㕱䱾䩳㭌䣇䰘㤑䧱㛏䢟䗜㛜㞗㻲㴗㐜䗏㭝㛩㽥䐐䬒㳋䰆㷕䐰䆶䙈㺅㚱䨂㱗䬲䚃䚧㧃䝗䗔䉧䋷䎧䉱䲖㓱䏬㖻㕤䌧䊵䡭䮟䟵䯽䓟䢊䰍䮫㺫䱸䌔䉩䍌䏫䞀䱕䠓㿧䳕䫫㥑䵸㽕䖻㤧㮲㒡䲫䐹㸨䥐䂉㿡䁱䜪䎇㳅䳼䕱𦢩𣏞")
    PingShuiYunInit(
        allSheet, 1, 11, "心深林陰音吟尋金琴今襟侵沉岑臨沈[同沉]禽簪斟森禁[勝也]霖砧任[負荷]潯衾淫欽箴駸針參[參差，人參]衿琳瘖涔嶔愔擒歆忱崟琛喑淋諶壬鬵唫[同吟]霪黔[黔羸，神名]祲鐔[劒鼻]蟫南芩湛蔭槮紝檎蔘郴燖鱘灊霃鵀妊吽蟳廞椹煁肣芯棽噙綅罧澿滲[淋滲]痳闇噷襂嵾黅嶜鍖碄銋箖綝攳笒惏愖莐樳崊鄩紟蚙靲埐甧櫼庈烎耹荶橬惍魫枔璕穇鱵瘎鈝襑諃瓭穼黚鑫誛曑葴乑瀶橝忴鈂摿汵鈙埁菳鳹鮼梣兓嬜玪杺韾撍扲鈊訦蠄幓鷣㞥䔷䪩㑴㕋䤃䤟䒞㪛㩒䅾㝝㜦㠁㕴䕾㾣䃡㴱䰼䚾䘳䋮䨧㖗䛘㸒䃢㜄㻸䋻䦦㕂㚞䥅䍼䣾䋕㪸䫐㽸㞤䑣㓎䨙䥆䜾䜷㦗䤁𠻝𩻛")
    PingShuiYunInit(
        allSheet, 1, 12, "南談酣潭堪三甘庵嵐參[參考]藍慚驂諳蠶龕貪探毿含男簪涵曇柑耽函[包函]鬖籃覃聃譚憨擔[負也]枏戡眈惔篸甔婪諵鐔儋醰蟫蚶韽湛[與耽同]驔泔盦嵁錟痰郯襤弇坩媅頷邯唅谽馣坍媕鏨舑餤鵪傪渰[與淹同]欦喑疳腤啉倓燂罈澹藫蜬苷甝酖蘫歛惏憛啽臢蕁噡莮痷喒佄儖肣嵅淦埮礛浛鋡萻晗橝愖炶姏汵鐕瞫闇[治喪廬也]撍儑弎葻媣醈娢嬠顃壜雸嘾玵筨笒厽馠謲撖聸暔犙頕瓭畘裺鄵萳婒韾欿懢璼腩頜緂梒鳹灆䳺䤴㟏䈄㴂㘱䊻䣻㽎䉡㼨㰫㤷㚮㓓䣟䌠㞩䟃㳩䐶䨄䜙㜞㤌䨬䥁㖤㴷㽑䳻䶃㑣䅖㶰䑙䆾䗝䗞㘛䘶㰫㵅㓧㽍㛺䵇䰐㨻㷋䎏䇞䆱䫮䜖𧮳")
    PingShuiYunInit(
        allSheet, 1, 13, "帘檐簾添簷纖尖嫌鹽嚴兼廉甜髥炎蟾潛瞻淹奩拈占[占卜]厭[同懨]沾恬霑籤縑黏閻鉗謙銛鐮粘殲懨忺鈐黔砭襜覘漸[流入也]鶼幨暹詹僉憸饜崦簽鮎蒹苫痁熸燖閹腌撏櫩阽噞蚺蔪濂爓枮瀸譫灊磏奄[奄留]鬵綅湉鬑惉蘞枏餂襝佔針槧掂櫼呥稴蠊棎鑯譣孅鋟臁詀鍁蛅憛笘襳嵰韱讝薝燂熑敁壛搛劆菾薕杴黇扲岒鐱妗[善笑貌]嬐誗玪鹼閆鋑袩槏讇酟鰜仱嶦殗檶溓秥肷舚虃諚顃蚙厃閚螹硽鳹螊撍釤偣馦胋耹婖冿嬚幓鋓煘覝慊噡忴黚彡衻瘎䛁䫇㡘䆎䵌㽐䯹㶣㷿㝺䘂䘋䪜㤿䦓㡨䏦㶄䬯䁠䈤㬲㿕䕭䋬䆂㿌䊱䯭㔐㲯䅧㾾䉷㦰㺤㰊㼓䑎䑚")
    PingShuiYunInit(
        allSheet, 1, 14, "巖衫帆銜凡緘杉咸函[書函]喃芟饞讒鹹鑱監[監察]嵌巉劖攙摻嚴諴椷嵓衘欃縿鵮碞嶄毚攕黬髟[屋翼也]儳嚵瑊彡獑杴穇渢羬艬站黯詀鍁櫼嘇幓礛輱崡柉厱尷稴礹覱揞趈甉譀肷鏩葴鰜杋淊[與浛同。沈也]釤玪酁螊舤鰔麣溓䟰䉷㴀㺥䫡䩂䖗㛾䤫䧯㩥㢛䂁䀐䪌㘙㮭㔆䩇㔋䭵䶨䜛䶠䑺䒦䲗䕔㘅㰹𩆷𥻧𥌈")
    PingShuiYunInit(
        allSheet, 2, 0, "孔董籠總滃懂蠓桶澒琫蓊菶垌幪攏塕動硐唪洞汞挏嵷捅埲暡墥曚空[孔]縱[急遽趨事貌。]統懵[心亂]蝀侗[儱侗]巃儱蕫揔眮聬晎檧瞈嵡竉勜詷倥[倥偬]徿嬞鬷[草名]鸗勭蓯[菶蓯，草貌]嗊諌龓箽庬棇憁姛熢槦莑悾[悾惚]愩郺琣翪鸏偬懜銾玤愡[憁恫]繱嗡[闇聲]漨䩬䉥䐥䭰㖦㷯䵜㳆㢔䞒㨂㹅䵔㪌㴳䋽䳞㬴㣚㛚㶹䡁䂢㷓䀧𢤱")
    PingShuiYunInit(
        allSheet, 2, 1, "寵冢涌勇擁聳隴壟拱踵冗捧竦腫踊悚洶重[鄭重]栱種[種子]鞏蛹茸[草生貌]恐俑氄珙壅恿甬奉覂尰溶拲蛬[蟋蟀]蛩[音拱。蟲名，百足也]湩[水濁也]詾嵷傱軵愯恟駷淎慫跫蓯[相入貌]躘輁臃塎埫嵱[山峰貌]坈鮦[魚名]悀傛喠捒愑煄漎[漎漎，疾貌]搈傇硧鰫衶筩[箭室]媑穁埇縙搑彮䢆䢇㩳䙕㤟㲝䩸㧬㤨㣫䞻䂬㨣䟪㷏㡖㭟䱋㓋䘴㕳㺬㙙䢇㦷㦶")
    PingShuiYunInit(allSheet, 2, 2, "講港項蚌缿傋棒耩硥夯漎[水會也]稖顜玤慃庬勜䎧䂜䰷䬕㭋䖫䐟䁰")
    PingShuiYunInit(allSheet, 2, 3, "水子起士此死喜耳理美市矣是史爾止李己紫指里履齒紙紀綺氏蕊旨壘[軍壘]恥祀擬髓靡恃滓軌鯉毁裏鄙駛矢已仕峙趾邇徙梓委芷雉涘豕始以址砥几[几案]咫沚俟妓詭晷侈杞巳似兕比婢彼倚圮姊旎耜祉弛徵[徵羽]嘴弭豸艤璽秕箠[策也]苡枳觜泚視蟻使跪汜邐你匕誄戺揆否[否泰]畤鬼燬痏簋唯[諾也]癸俚屣姒藟薿屺只宄駬迤[迤邐，旁行連延]芑薾訾裡阯瀰[水流貌]捶柅洧蘤枲鮪匭舐跬耔累[累日]棰骳技褫痞妣跽麂笫嚭庋巂被[寢衣，名詞]揣椅崺企秭痔纚机[木名]彌[止也，息也]跱髀諟庀餌萎[藥草]珥扆儗疻蓰苢仔樏抵厎骫酏胏橤屎佹籽壝縰偫娌峞礒跂葸釃憙佁蔿黹嶬漇葈瀡渼芈掎俾敉垝佌旖錡頍氿蟢您狔梩歭嶉舓踦[踦閭]攺俿庤躧跐軹咪剞齮呰杝蹝洱鸓骪咩庪繠姼毇趡讄栮哆傂峛啚坻[止也，又場也]庳[伏舍]薳馜坁恀垑恑蟡鞞唏傀匜吡姽鋅鞁扺哩啙魮阤憘輢甤仳廌孴瀢硊檷吇諰矖崣孊伲疕虸抳觤秠柀湀厽寪雟諀羠洔朹婍嬟菙滍貏杍攱灖蓶坭[地名]徥愢檓菧沇濔秄褆臎峲誃璻鈶卶鉹砋抁逘胣枇[同朼]拸畾狧袲沝枾濢玼[玉色鮮也]聛灅盀矷洈惿蛫譩袳妀欼弬鈻泤鈰崥[山足]腂敼祪娝劧芔朼嵄嶏飺皉虆抧孈吱[行喘息貌]唩惢聻鉃芓釲沘骩儰氐煃葞踓悝搋佊杫芛嶰巋噽懝秲噧訨諈鉂笖暿徛邔椯蚔撱淽崼鈮噿瓕渳猚鄬厬鴲藢奀攦娰鈘釨裿峐羛騃䃣䗁㞦䚹䉂㱟㷐㠯䤥㖐䰙㞔㢋䃾䂠䍯㶴䃽㕜䋙㢮䄎䠑㓼㔳㪜䛼䢎䂡䤏䅩㿂㾖㥴䔺䧽䧉䛗䭲䏢㚓䣥䴎䣀㲛䠋㫊㹝䞨㺭䏡䍴䤆䇃䦻䒨㫑䛏㥨㕽䘣䚦㜽㸻䝐㞛䔂㸚㞆㜫㠱䚟㾅䭉㧪䘦䇛㙼䚞䭧䧧㡶㷃䎣㰝㱀㲹䒻䘡䵋䳅䟖䢄㭒㠲䝰㩓㣥䈧㞨䊓㨊䐯㧗㠖㹬㸵䢳㚡䛶㧡䟗㚶㠧䤚䓈䊼䦵㵦䉝𠲿")
    PingShuiYunInit(
        allSheet, 2, 4, "尾偉葦亹篚虺斐娓煒韡韙悱瑋幾[幾多]顗鬼匪卉豨棐榧蟻朏蟣菲[菲薄]浘偯颹霼豈誹扆唏蜚蜰蘬餥庡魕愇泋膹韑媁梶鍏陫徫喡荱奜椲蕜䔇䤵䞔㬙䬿䅏䒈㕈䕁㥱䪘䍷㠕㞑㹃䇻")
    PingShuiYunInit(
        allSheet, 2, 5, "許侶暑渚舉所汝旅緒阻序黍鼠佇俎嶼煮墅杵呂語炬杼醑雨處拒禦去貯楮苧紵礎溆敍齬距膂予[賜予]籞與[給予]女筥圉苧圄楚簴巨羜鉅褚咀抒鱮宁苣糈莒弆敔虡梠湑籹芧秬駏篽稆著[著任]跙諝櫸鋙[鉏鋙]癙岨柜茹岠峿濋濘[澄也，澹也]沮紓儢稰眝蓹汿潻怇鼁作詝歫詎齟鐻齼歟詓椇蚷粔洰鱮瞘肗鉏[鉏鋙]耟紶憷垿盨螶銣藇絽楀袓疋苴諿麮郘坾姖檸壴豦挔衙鮔昛胠㷂䢹䠂㛎㲾㦛䔓㘧㪽㭚䝪㤖㾔䰞䃊䇡㐨㞰㜿䙘䦽㿾䘘㒜䘢㵰䥏䶙䍆𪓐")
    PingShuiYunInit(
        allSheet, 2, 6, "古土舞主戶府虎鼓浦宇武補縷父午五譜睹乳塢斧魯堵伍祖甫虜取杜輔組雨鵡櫓麈腑嫵侮弩釜腐滸股撫禹否[音甫]苦簿矩竪廡脯拄罟俯愈數姥母鹵吐庾扈莽詡瞽蠱羽圃普溥栩拊祜窶部賈[商賈]畝怙肚下踽僂[僂佝]估聚賭窳詁怒岵牯盬黼努樹[種植]柱貐膴羖稌傴簠頫擄楛瑀甒憮煦粗喣剖仵滬寠拇琥褸酤瘉醹嶁珇俁瘐珷荰簄牡咻齲莆昈冔鄔鄠謱珝弣簍砮埡裋薣帍橆滏砫蔞祤瑦癒斔婁旿槴宔氌嵨楰媽鐪擼萀雇嚕炷鈷蒟嘸鳸捬偊郙竘噳枸麌蔰椇蚥婟蜅暏罜跓磠頨蝺萭靻敄洿抌蛡殕竬潕墲鯆貗觰匬滹剫丶慺聥倵溩誧瞴峔烳芏弖暊玝楀芐鷜鰸嵀躌靯陚樦寙蔖斞蓾秿鄅焸萮麆熓譕潽帾熩琽棝籔㺄㝢㼌䇢䥈䩉㦿㑄㕮㐅䲐䨒㙛䀾䪔㢚䨞㕆䅡㒁㙑㾈䀯㬳㡰䲧䣁䡧䁈㔪㔱䭸䶚䄔㲾䔃䒉㵭䅓䥘䋨䀇㵲䌗䇠䟼䧁㨭䗂䗄䛩䝂㒇䃖䯙㑯𤬪𠰍")
    PingShuiYunInit(
        allSheet, 2, 7, "底禮體米啓洗陛醴邸蠡[彭蠡]薺悌眯禰棨抵澧觝牴弟泚詆癠鱭濟[水名]鱧鮆涕柢瀰[水流貌]遞綮苨徯髀齊[齊齊，恭慤貌]泥[露泥泥]緹坻[隴阪]盻欐[小船]啙謑醍鱺梐骶晲挮洣菧蔝阺呇袳玼[玉色鮮也]娣媞鑈趆奃悂隬卟盠眫匸欚弤肶鑙聜泲蒵蜌軧抳晵掜觬濔璾劙[麗上聲。刀刺也]䏶㡳䌡㭽䭬㼵䫌㝥䋛䕥䡔䑯䱊㙄䪆䰦㯇㪏㒅㪆䍤䯗䏿䢑䋜")
    PingShuiYunInit(
        allSheet, 2, 8, "買蟹駭解澥矮灑擺嬭楷妳拐獬罷騃捭罫夥嶰駴鍇柺廌矲薢矖蕒躧簤觟豥鷶犤箉娾攋檞襰鉙抧疓徥嘪猈㔥㗗䇑䒓㡁䉏䍉㧳㢊㙰㚷䲒㵋")
    PingShuiYunInit(
        allSheet, 2, 9, "海改待彩宰綵在乃凱醢茝亥采殆塏載[歲也]寀紿愷倍怠蓓迨闓睬頦鎧駘欸[欸乃]豈鼐歹颽詒[相欺]唻踩崽輆毐酼婇軩忋箈溾絠疓暟埰烸嵦䏁䰂䂾㴓㥒䑂㘆䇋䈢䮨㤳䈚䁗㱰䆀䣋罪餒蕾磊浼磈琲悔賄儡[傀儡]隗璀猥腿嵬皠每匯[盛器。水流匯合]頠磥礨漼瘣腇癗碨鮾嵔嶵餧俀[舊音妥]傀黣腲嶊鍡鏙鑸鑘聉挴錞娞琣殨廆櫑潣燘顝痱[風病]俖檌褽喛頧頛蛔灅浽槯烠詴陮湏礧僓鯦洡㠥䃬㞂㠑䫭㱱㼏㱬㵽㚍䏨䲎㱣㷄䊫䜸㒦䫥䕇䇏㵏㾼㼍㟎㨃䔒㒑𦞙")
    PingShuiYunInit(
        allSheet, 2, 10, "盡笋忍緊尹軫窘隕敏哂泯隼菌憫蚓準殞蠢[動詞]牝閔腎允畛鬒引霣稹臏惷疹狁盾楯囷脤嶙[嶾嶙，山峻貌]眹辴吮[舐也]稛診蜃轔箘簨紖縝頣僯靷埻胗眕矧黽髕純暋朕賑榫慜湣抎紾繾黰偆僶獜袗鶽螼嚍抮僒綧弞鰵駗蠠荵姫吲頵笉耣弫簢濜敐濜莙鈏埨裖橉玧芛愪鋠嬧箺撛舛[雜也]聄沇濥鈗棞廴揗屒喗睶囟鎨傊昣潣蔨婜鶣萶鵘敃疄麎亃鯅阭渳蜠刡槇馻荺㩈䀕䒡㽙㿤䲄㦏䪳㔼䟨䐔㯸㖺㰮㐱㾙䑐䝩䮞䇙䦮䨶㖥䪾䐏㨚䐃㣼㥸䂦䇖䊶㬆䀆䂧")
    PingShuiYunInit(
        allSheet, 2, 11, "粉憤吻謹槿韞殷[雷聲]惲卺隱搵听[笑貌]近癮緼刎蘊抿墳[土膏肥也]讔抆弅忿瑾抎攈菫磤[雷聲]檃膹嶾蘟秎坋凕齳歾呡勽賱齔縕喗愪黺魵赾熉漌伆夽䨸㹏䌍㻒䞫䠴㗃䤺䆬䌥䘆㥹㦩")
    PingShuiYunInit(
        allSheet, 2, 12, "晚暖返苑坂偃阮碗遠婉阪反幰娩飯宛蹇巘挽烜綣琬踠畹鍵揵鼹晼鶠夘菀蝘蜿[蜿蟮，蚯蚓]堰咺圈躽鰋楗緩匽皖沅軬箢寋夗愝倇妴攇鋺朊梡嬎喛湕傿鄢[地名]薳梚瓪邧桳睕奆褗媗鯇愃葂脕盶虇錪綩犿橎搟鰎㬉䜝㽜䅚䩊䡊䤷䊎䳃㱧䅋䞁䜢䘼䛀䪭䑱㨴䛷㿸䮿㫃䎡㔓穩本衮損沌閫混滾懇悃墾忖壼畚蔉遁鯀狠很輥噂渾[盛也]梱笨捆焜盾鱒暪撙躉刌獖棍吨噸硱掍稛齦[齧也]坉苯緄豤庉裍僔詪峎氽潡逇倱腞伅黗眃睴緷惃碖婫泍棞呠桳崸翸稐睔桽翉齳丨喗壿錕觨菎䔿䁚㵍䫟㝧㮥㨧㖔䃂㙥䠅㡷䵯㤓䓳䜇䚠䬱䐣䅰㯻䙛䛰䅙䧰𦠆")
    PingShuiYunInit(
        allSheet, 2, 13, "滿短管懶旱款煖誕椀坦傘罕琯盌纂瓚疃懣袒窾緩卵館斷筦散蜑伴稈蛋浣纘趲算赶盥亶笴潬痯悍[性急也]但侃脘嬗暵篹蔊柦癉悹匴憚焊疸擀錧瘓奤坢饊梡皯輨繵潵芉狚輐酇瓪玬觛裋衎忄靼衦皽璮厂鉡穳浫攋皔刐藧嵈秚灡棵[斷木也]粄鏾跘拌繟駳唌禶焌鏋睕埦糷捖簳綄䂎䍐䌣䬳㪔䓍䉽䞡䟎䠪䛞䝹䪀㫜䦔䲌䩥䄤䩪䵟㼫㦨㼝䗆㫁䦎䏓㣪㦌㬊䉈䘾䕀")
    PingShuiYunInit(
        allSheet, 2, 14, "眼限簡盞産板版赧莞睆柬嵼滻潸僩揀綰睅剗撰鏟棧丳戁矕僝昄蝂鈑撊轏拃驏輚摌闆唍瓪嶘舨眅羼捾橌睌硍魬鋎晘碊攌皖[明貌]鯇娨暕簅䱠䎒㹌䦘㸧㦃㡾䩆㫱㹽䁂䴼䐮㟞㯆")
    PingShuiYunInit(allSheet, 2, 15, "淺展辨軟典翦犬免篆顯蘚輦冕繭踐勉捲[斂也]翦辯泫喘卷[舒卷]緬臠峴鉉轉演扁燹殄沔闡腼鮮[少也]璉腆撚湎遣畎褊荈舛巘衍跣善艑謇蹇獮鱔蜓[蝘蜓]俛筧囅選匾辮兗件睍涊癬蕆墠洗孌戩瑑搴讞眄譾韅覥雋錢[銚也]餞銑耎筅毨棧鍵吮趼燀揃齴繾丏嵃襺愐沴鞬宴狷剸輾楗蹍淟蜆惼單幝緛晛鋧戭垷墡蟺愞羂膞圳勔趁[踐也]挽撰鏟踹蜎鬋黽[黾池]俴詃偭檽甗諞碝諓沇竱媆囝瀽橪錪菤揙齞蟮琄贙臔僎緶輲鮸鴘臇呟帴繟僤姺灦榐譂痶藊碥蜸賟搌梘喕抮蹨芇摙寋晪瑐豣咞僐脟磰渷哯槤蕇鞙躎橏潣弿鶣鱄膦圢豍跈蔩媔襈縳皽糄睓娊鄻貵悿熯埍牑烍奵抁繯挸婰覵矏藆樿覑琠孨剗遃腨禒莬簐萒誢蠕馻謰僆矊攓詪顈鍌鄟堟椼渳歂嘽唺鍽嫣㥏㾌䠄㜻䓴䤄㨠㹂㒄䛇䓦㥝䡢㣤㸁䱇㛯䁵㲢㧥䡱䭤䩙㨺㧋䧖䀎䗺㮒䁴䞂䧋䥪䥀䧘㮟㭠㬎䮿䙇䵐㔵㠭㙉䚚㩃㜊䉸䎒䏹䢾㶍㞡㱛䐌䵡㦓㢧㔊䍾䧠䄯㵷㕣䓣䆓㨵㓴䱼䩅䵤㦚䗾㷷䅐𠻤𧍒")
    PingShuiYunInit(allSheet, 2, 16, "鳥曉了[未了，了得]小表杳渺杪擾裊沼兆窕緲皎矯趙褭筱眇少[多少]窈窅繞紹旐淼蓼悄[憂也]嫋皦醥肇藐瞭皛縹繚秒嬲勦[圍勦]殍麨夭[夭折]溔愀挑[挑撥]撟湫[隘也]莩鷕標昭燎掉繳窱嬌蹻褾舀嬈晀佋剽[末也]佻錶鰾蟜朓麃釕眑鱎僚[好貌]吵瞟訬憭嫽騕鰷婹枖偠摽駣敫闄譑劋婊抭宨檦苭屌崾萩朻眧煍皫藠菬釥賋絩柖嫍芺敿髜鸄祒篻垗蔈鐈鄝袑岆仯璙誂镽鮡隢藨巐狣扚仸榚尞諘篎鼼丿顠鴢蓔璬宎肁楢柼膘㒟䑠㟽㵘䯚㵿㨄㝔㣿䦊䙚㹓㴭㡑䄦㭂䄪䂽䁏䆞䍮㵱䥵㜵䃵㠡㡽㪕䥞䂪䈃䔸䒚㹾㝋㫏䉆㫐㟱䙼䩍㹛㩰䘨䚩䏚䒕")
    PingShuiYunInit(
        allSheet, 2, 17, "飽爪鮑卯攪嚙撓狡昴泖姣[美也，媚也]齩[齧也]絞炒煼找佼鉸茆媌[同㚹]巧拗吵筊孢骲瑵鞄虠狕笷怉櫹鴢灚臫烄焣頝捁緢澩橚挍㶤䎐䲾㺐㕚㚽䕧䶧㥮㩭䝖㑃㚹㑿䀊䝤㑤㽱㚣")
    PingShuiYunInit(
        allSheet, 2, 18, "老草早島寶藻惱保槁討好考道浩稿稻昊潦棗抱掃皓蚤倒[跌倒]腦搗杲葆藁媼燥皂堡嫂褓鎬皞造[建也，作也，為也]襖縞顥瑙禱澡灝懆埽鴇栳夭橑璅薧栲澇纛烤碯袌璪繅轑繰愺暭懊拷狫恅駣夰套蝹嫐媢滈捯薃蓩鰝镺堢禂筶菒荖皃鄗壔狣窵淏洘芺傐郩槄勽絩怉菿忑譅梍咾屮賲聕鷱鮡駂簝丂祰恏檺峼悎憹祮糔燠皫鴁椺劋䴠䕩䎂䝤䲃䖣䳈䧚䯫㚼㺁䯠㤇㛮㧇㬶䇭䮻䗢䵏㙅㵆㨶㛴㼥䳰䆃㚖㻄䴐䵚㧯䴈㾸㑎䳓䒃䯪㿒")
    PingShuiYunInit(
        allSheet, 2, 19, "我火可墮果鎖墮禍朵顆裹瑣舸娜妥坐麽嚲左裸柁砢跛荷[負荷]頗[稍也]舵夥躲蠃[蜾蠃]惰笴垛柂[同柁]鬌簸叵軻瑳蓏峨坷輠橢沱脞那騀播堁佐儺[行有度也]沲陊婐哆揣蜾駊拖埵硪癉猓嶞惈哿伙瘰媠閜娑[馺娑，漢殿名]卵阿[與猗同]懡婀[婀娜]蟻爹墯棵跺嬷笸鎯爸髁婑岢餜鵎捰嗩彵誐粿鐹魺溑敤扡邩抲橠娿攞崜袳惢縒椯灬尛毻陏褨錁褍鍺睉袲掗她欏曪涐葰毑剆挆砈碋綶硰撱隓綞痑頋稞暛炣誃鈳淉攭㦬㰤㝾䴹䑨䵀䰀㛂㡅㪃䅜䒳䐝㻔㪼㰙㰁㯐䲊䩋㞹䯬䙤㦱䤻㰐䠤䩔䫂䂺㥩䰈䣔㙐㱻䙨㝿㛆䈗㧴㶡䌱䂳㩡㚌𡜮")
    PingShuiYunInit(
        allSheet, 2, 20, "者馬野社寫也雅瓦寡冶下灑舍[廢也]捨赭把假[假借]瀉灺惹斝檟且鮓打啞夏[華夏]踝苴嘏若厦耍姐賈撦銙剮庌髁傻瑪喏奼哆輠碼瘕閜叚厊疋螞乜壄毑奲痄邷厏苲藛藞搲椵蕥吔抯溤稞蘳掗楇錁雫跒耹觟忚謯騇漜襾婽鮺她鷌偖飷鰢黊顝蹃腂粿訯䰩䱹㿿䪵㗿㕐㨋㙒䟩䈑䊬䋀㡸䑝䄕䵦㼘䋾䥱㐄㵔䠚䬷")
    PingShuiYunInit(allSheet, 2, 21, "賞往響想象丈網爽掌壤像槳黨朗幌敞上鞅長[長幼]莽享仰廣枉氅奬恍惘罔漭痒養饗魎倆兩顙蕩仿曩蒼[莽蒼]攘[擾也]杖榜坱蠁晃倣蟒簜強[勉强]帑盎晌讜鏹昉沆紡橡瀁瀼[水淤也]怏蔣放襁輛彊仗駔儻慷穰昶輞鮝泱[泱漭，廣大貌]向魍惝髣誷蜽愰彷滉榥廠搶檔吭嗓髒[骯髒]磢磉奘緉嚮嚷骯懩駚厈瓬鋹謊獷[縣名]氧倘躺潒搡曭迋蒡蝄慌塽灢漺扄佒逛誆垧攮傢饟瀇愓爣菵抰襐矘岟旊欓儣灙裲黋櫎氆膙璗蟓懭弜掚咉茻軮蔃崵慡鐌曏誏仉銺蚢驡誩欀臦姎嶑俍縔脼柍鎤雵鶭酐鱌忹褬樉偒騯烺勨樃犺詤瓽躟覫紻詇蠰爙婸墏臩嵣眪攁扙滰汻俇炴壾懬謽宺魧爌鄺皝鞝榔[木名]傸奛瞊熿㟿䁳䣊䋄㬻㟐㫤䖹㗽㔝䴚䑗䒎㒉䇦䲱䠀䫪䴂䠃㬒㿩㴏䉃㤺㓪㒳䡦䫙䍩㕫䒋㔦䥒㼒䗮㑂䬬㛨㯍㳹䑆䒍䑋䒂䒽㽴䭺䁜䖆㶞䢍㢡䖮䟘㟠䡉䔪㫰")
    PingShuiYunInit(
        allSheet, 2, 22, "影冷靜景境嶺井永省幸領頃警梗整穎耿餅騁屛猛杏靖綆頸潁炳癭秉逞郢荇礦艋鯁眚哽黽請烱丙囧冏皿蜢靚幷璟獷箵悻憬箐阱怲打邴倖懭袊痙埂竫梬浻冥煚苪渻裎倖睜檠猙[飛狐也]睈勐蛃庰穬浧蟼悜瓾澋鯭檾徎陃奣浜栐鈵炅憼皏鋞鼆峺睲莄晸簈彾郠廎廮鉼眳偗鱦摼窉鮩塣臦擤眪柃璥朾侱暻胻炴帲掟鄳帡挭擏幜撔檸誁氶旲寎睛[眳睛，不悅目貌]㾪䴵㯳㗂䓷㣏㼳䗒㓏䊯䂔㩩㼬䚇㹙㢍䁄㹚䁅䩶䜘䵃䋑㑟䭊䭘㓑㮐䋁㲟䁞䭗䑍㨀㬌㴄䯧䚆㝭㾘𡈼𪍿")
    PingShuiYunInit(
        allSheet, 2, 23, "頂迥鼎艇茗等酊炯肯挺涬拯梃町醒鋌謦褧溟[与瀴同]剄絅酩泂艼嵿珽莛幷惺脡熲熲侹脛濙頲矃冼佲奵冂詗訂夐濘烴婞笭炅濎圢榠涏汫眳巊娗嫇巠靪烶顈漀踜耵煛瑩庱誙鑏鑋廎矨鋞檾姳朾侱緈閮徎瀴誔鎣䔛䵺㴿䗿㟰㱡㽪㷫㯋䦐㫥㫀䅍㷡䳙")
    PingShuiYunInit(
        allSheet, 2, 24, "酒手久有柳友口朽叟牖九偶丑否狗醜首走垢藪肘后斗阜守後帚咎厚臼藕畝缶韭負吼玖酉壽剖取舅苟紐母右莠塿糾誘受婦耦某蚪黝耇不[同否]陡擻笱瓿嘔綬蔀鈕杻扣罶紂牡瀏狃授掊[擊也]卣叩揉蹂抖糗槱蟉[蚴蟉，行動貌]綹莽滫嶁桕赳糺忸瞍糅扭毆部灸拇嗾篰黈眑枓羑垕醙掫趣[趣馬，趣養馬者也]簍蚴琇甊棷[同藪]苃歐[吐也]佑籔釦懰茩搝鈄禸岰婁茆溲漊妵涭麔鋀枸鯫鉚蚼殕睭岣艏鯞栯塸萯楺郈蛗蜏玽偩糔砪蝜踇缹櫢劶勏峊餢腢炄媀啂橾璹齱泑熮妞[姓]紤牳疛紑煣葤朻飳龓綇雬紏斢箁沑懮鮦[鮦陽，縣名]莥蘣奺吋侴棸杽鯦犼楢羐喁[聲相和]犃聈嬼湡庮煪培厶珋吘鴀舏吜媨齨嘍藰倃湵婄垺㪷䳇㰶㽲䪮㝅㱙㺲㧕䈹㔽䚵䅹㺃䭭䂇䕆㕗䅎䳝㔚䱏㪗䴺㞳䎻㞫䈙㥅䒴㺵㷆㶭㪹㸸䶇㰴䳑䏔㫶䘀䞜䖞㥉䏂䬀㨐䏽㒖䱂㓡䬏㕛䛮䊆㼴䳎㝊")
    PingShuiYunInit(
        allSheet, 2, 25, "錦品寢稔凛廩審枕飲稟甚諗沈飪蕈懍衽噤恁椹葚荏淰踸朕怎鋟檁磣墋腍嬸瘮凚魫伈趻覾栣鰧昑唫梫瞫橝銋棯菍訦嬐謲抌箖贂闇趛拰栚秹顲菻㾕䫈㶒䭙䄒㝲䭃㯢㾛䫖㤛㮳䪴䫬䚓㱃㔤㴨㐭㱈㰂䫴㶵䇮㜤㨆")
    PingShuiYunInit(
        allSheet, 2, 26, "感覽膽慘敢萏坎糝攬頷撼壈菼毯欖窞黮紞髧憯黲匼歜黕嵌淡啖槧禫餤菡槮澹砍闇黭醓耽[虎視]傪嗿醰贉轗罱顉惂鱤輡晻喊埳橄憺贛唵忐欿黵鏨澉揞昝歁腩啿黬竷霮醂朁湳顑莟鏒饏豃漤臽襑倓轁爦肣坅撍掩錎浨顲馾嘾醈揝馣莐罯參[與糝同]衴薝幓喒頜篢腤蜭燣暔澰揇寁惏澸瓭抌鰔䃭㯺㙳㛧㲜㨔䖔㽢䉞㰖㛦㧲䆦㣅㟛㜗䨢㸝䎨䊖䫩䭛㩜䫲䓿䤗䊉䭕䃫㺂㕪㞄䊤㜝䏙䊏䈒𦛜")
    PingShuiYunInit(
        allSheet, 2, 27, "險點染簟冉儉檢臉燄玷苒琰閃剡貶颭陝嶮漸[漸次]芡崦諂儼慊掩斂睒嗛歉魘忝撿广黶檿隒埯磹覢渰罨舔晱扊顩弇厴奄槧瀲瞼黵噞譣獫驔肷鏩黬裺螹薟晻稴曮棪扂礆鍩彡馣夵孍媣讇珃嬐澰咁鍩礆硽溓嬚婖疺蒧呥悿鼸橝羷龑蘞㴸䠾䄼䣍䒣䀹㚧㱘䍄䇜㪎㯬㰈䄋䣸䤡䭠㤁䎦䌞䎃㓠㚩㭺㢂㐁䌪㶘䟋䤔䭑䲓㚒㶑㨛𧞣")
    PingShuiYunInit(
        allSheet, 2, 28, "減檻范黯範犯艦斬摻湛黤轞軓嶄淰豏錽甉巉歉鹼闇溓趻豃懢啿鹻釩喊[怒聲]凵撖旵醦闞[虎聲]鰔偡槏瀺黬払濫[水名]瘎壏魙㺑㺖㧄㺝䤘㺌㴴")
    PingShuiYunInit(
        allSheet, 3, 0, "夢鳳送弄凍甕眾痛棟貢仲慟鞚諷中[擊中]控哢動閧洞鬨峒[山穴]粽哄[唱聲]衷[當也]霿羾礱恫空[空缺]偬賵瞢[與夢同]凇贛湩[乳汁也]齆蕻銃胴蝀涷咔衕嗊汞緵[緵罟]倊迵懜憁洚駧眮蚛詷菄戙惣霘腖崠[山脊]焨烔[火貌]齈堹姛謥煈愩梇妕翪趥懵[惛也]愡[憁恫]筗癑茽揔硦霥棇倲絧蘣娻槰焪祌繷㔶㢅㚇㳥㑋䠢㞲㖆䛪㜴䍟䇨㝱㯯䔈㲴㸜㗢㑝㮸䠻㐺㼯㓊䏵㧤𣹟")
    PingShuiYunInit(
        allSheet, 3, 1, "用共頌誦供[供養，名詞]從[僕從]宋訟俸縫[隙也]綜葑[菰根]雍[九州名]重[輕重]種[種植]縱[放縱]封憃[與戇同]奉瘲雺恐統壅躘緟徿偅揰捀謥縙昮錝諥龏緃苚澭[與灉同]贚湗碂褈[繒縷]灉䃔㙲䛦䝋㮔㴩㡝")
    PingShuiYunInit(
        allSheet, 3, 2, "巷降[升降]戇絳撞虹[音絳]幢憧[愚貌]鬨淙洚肨艟[短船。]憃[與戇同]漴[水所衝也]袶炐䡴㦼䎫䣈䚎䢽㟟㕩")
    PingShuiYunInit(allSheet, 3, 3, "事地意醉至淚字志寺異翠寐思睡寄吏義記致器利棄墜媚戲騎[車騎，名詞]瑞二避悴愧位類試秘賜遂議次置臂轡備吹[鼓吹]忌智驥治翅誼四膩侍値易[容易]鼻肆季邃笥閟稚瘁嗣祟自穗嗜僞魅熾幟祕駟泗饋粹庇示匱萃燧喟冀漬悸施[惠也，與也]躓恣帔屭芰遺[饋遺]隧貳懿為[因為]累[連累]謚伎誌刺鷙畀贄伺摯識[記也]詈惴輊莉緻痹遲[待也]覬賁胾厠肄視飼被[覆也，及也]恚穟豉譬蒔鞴[音備，本作絥。]使啻食懟劓勩知[與智同]寘似芘帥餌諉贔洎出植[槌也。又通置]裏莅簣積比縋觶糒已陂[傾也，邪也。]忮毖弑牸骴始彗胔惎膇澻屣俐縊織企曬痢蕢幾[未已也]眙[直視也]技睢襚瞶嚱[聲也]痣璲繸跂孳[乳化也。]倚司珥屁饎奰懫咡疐硾懥鉺觗翨萎[同餧]德質痿眦掎詖泌誶欬暨巋睟僿髲佽墍笓廙剚柲柶甀禭儩瓃攰肂尯儗垍瑟刵蚑螠旞近[已也。辭也]鵋錘[稱錘]敡侐蘱槌[蠶槌]蹕餧率澌[亦水索也]庳[有庳，國名]唏毦饐哩咥蜼洱鐀諈懻杘檖倳樲庛髶鬾謘裡穊鷾蛓鞼坒痓騩樻猤峜皕呬瀡揓欭謉鯚螆貱檇衈蝞亄駤絘嘳嚊呮錗袣滍糦螅蔧攱訵坔忥稩螝貤栨鍦憙芖筫潪腄[縣名]瀃徛戠邔嬑瞡翆鶅輢鄪賥沶妼珕婎覟佊邲聏眭術嬟贀檍扻梞埴袘牭醀楴鐾鑆胒囟藣秲茡夡蔇[至也]蕼帺搱吱[行喘息貌]鷧饖誃馶詒[遺也，貺也]浰瓗祱硊枈唭佴怶酨鴲撌腃蟌孖韢跮潩燱肶卶畁羛娷誀痵濢其[語已辭]禷絥洷諅芓穖徝杫殔詄垝娡汥鞁嚜纗煝憄犕柴[積也]聭轛肞臎蚝[同蛓]騺枇[細櫛]貄怬洓恎襣哆茦粊嬘睸㩻䆳㘩㱁䞃㑶䎶䠔㞓㢰䜐䬥㦐㳏䀣䣵䔬㿫㛅㑥㢀㱴䐉㣇㯜㕄䩀䳐㱖㹑䪐㞖㨖㒾䰎䜻䏪㙺㻑㱲㑧䏯㸂㐸䀿㸢㵨㢻䇐㿷䔹䠦䜜㜇㤦㽷䦯䎵䆊㨁䅆㣁㢽㣈䛈㦉䩃䛋䄁䉅㰣䙡䚳䆈䄲䉜䠏㧘䉾㳵㥡䐀䰨㸍䕌䕗䝯䓽䢦㴛㻽㦤㽈㒸㴃䣦䰡䞈䗹䁛㓨䓌䘭䰯䋘㒃䗽䑄䲀䝸㥞䫁䯸䜵㴚䯣㥍䉌䭄㩼䡵䉋㮹䋟䥙䢋䨳㿙䦙㾽䕚䏤䨽𩥉")
    PingShuiYunInit(
        allSheet, 3, 4, "氣貴味未畏慰沸費緯魏謂渭諱旣毅猬胃尉欷餼蔚衣[著衣，動詞]罻芾髴彙[類也。聚集也]狒卉愾汽漑暨墍誹熂屝翡蜚剕媦黖菋霨熨唏瞶痱[熱瘡]菲[菲薄]煟黂芔瞶穊胇顡泋藙俷藯昲螱靅笰攈陫鯡緭刏奜霼犚旡盵喡荱蛂摡甶忥蔇濷鮇蘶炥禨餥鱀滊犔蕜䠊䤒䛍㭑㔗䪋㒫䬣䭳䮎䰁䲁㵒㩌䝘䵝㰟䙿㫓䆏䝿䊧㥜䊠䀈䉨䬑䨾䊊")
    PingShuiYunInit(
        allSheet, 3, 5, "絮曙御馭助署據箸譽慮豫翥踞遽庶覷恕預洳飫去處澦鋸倨語[告也]如[音茹]輿[舁車]蕷茹濾與[參與]除[去也]著淤薯醵舁鋁鑢穥噓詛懅悆櫖鏣楚詎呿瘀鐻憷沮歟礜悇麆豦忬爈濖櫡藇棜躆鸒椐暏藷女[以女妻人]勴澽耝嗻勮狙櫲謯怚饇儊坥壉嫬莇胠竌麮謶㰦㵂䎝䭖䥨䁦䂊䘄㵖㫢㾻䢩䱟䉀㣽㫂䛯㫹䬡")
    PingShuiYunInit(allSheet, 3, 6, "路暮住露賦霧步渡顧遇素故誤具度[制度]護注悟慕妒墓固鷺布句駐訴趣兔屨戍務傅懼蠹樹寓附付污[動詞]晤鑄騖疏[書疏]哺互屢赴庫怖祚褲忤寤負喩溯數冱裕孺措痼婦芋諭愫嫗濩捕怒輅錮瓠富惡[憎惡]迕莫[同暮]雨娶鮒聚訃吐澍鶩婺仆[偃仆]醋嫭募賂塑頀颶璐呼[號呼]炷亍胙鋪[店鋪]苦[困也]霔呴圃籲愬蛀柱嗉羽祔阼煦埠絝潞錯副咐[嘱咐]簬斁賻酗戽擭鍍驅厝傃埧頋輸[送也]瞀酺枑捂祻菟酤茹餔[餹餔]謼馵屬足瞿跗疰蚹堌袝作胍穫[焦穫，地名]雇胯絇覦抪蒟俉啎腧虂熃綔紸窹涸奼詛駙鮬捗鉒飳葄殶韄祩鵵棝崓蕗嵍婟裋芏侸尌誧鵏娪鱯鏴嫊豧怘孵榡怐鵅饇詂瘻龥姇魱媀稒鸌敄旿聥陚摢咮縸鯝縤秅姹捬鈷篧禺[獸名，猴屬]攎忂嬎秙蘁榑紨弖罜齼鴮秨盓胕迬凅喥捒墿荹軴慔秺埾緅陠隃奦趶姁邭䊺䑰䪒㬬㤔㾟䴁㸦䵕䒀䐍䍛㽽䝬㻉䞯㲓㓃㳍㜐䠼䣴䥄䦌䨁䨼䮛㯝䎷䇘䛾㺛䂤㨞䠵㹘䝵䟔䊇䟻㧽䔯㕖㚴䘱䀠㹥䈮㴑䣱䝾䜑䜴䓢䎸")
    PingShuiYunInit(allSheet, 3, 7, "世計際歲細霽勢麗桂袂逝第制帝系繼滯砌裔翳惠厲繫衛髻藝憩蔽蔕稅替唳荔製敝例脆鋭詣弊閉慧契[契約]婿誓蕙睨礪隸曳癘睇贅噬戾諦勵幣斃綴枻禊薊澨儷劑毳嘒薙汭係曀祭彘蚋離[偶也。]棣濟瘞蛻筮罽謎剃涕濞殪偈囈睿殢羿嚏弟遰枘堄遞盭蠣媲猘説[游説]嬖泄貰嚌泥[拘泥]懘傺締劌柢蓺揭蜧穧沴禘踶薜屉漈涖糲芮筀噦[鳥鳴也]愒蹶切掣槥寱妻[以女妻人]擠彗襼轊釱蘙揥秇甈逮鱖題[視也]眦埶帨穄涗軑螮蟪綟憏砅箅瞖竁墆鯷欐[梁棟]悷嫕睥瘈齊[火齊]唑璿軎蜹珶棙鏏熭觢晢醫[弓弩矢器]暳捩銴昋霓蜺娣盻裼紒鷩攦迾醊洟[與涕同]跇杕簭蝭慸蹛劙[音麗。義同。]稧躗葪嵽枍濿淠鄨迣讆獙疐摖檵畷偙櫗腣瘱檕銐儶焍鐴齌跩瀱豷媂僀蟿殹蘮槸鮨彑彆橇渧彐罊楴怟蘻鷤摕袣奃鮤蛈裞栵詍疶挮浙[通作淛]狾妎幆鈌鈗懠丿魝櫅贎誽浰鑖韢橞痸赽栛骶炔濔鏸栺寭帠櫔祱忕鰶轚犡潎慀潓泲哾鱥暩睼忚玴捙抁曞遾靪炅臷達[足滑也]眱譓噎[咽痛]戻嫛鶗眭爄淣趆瞉栬榽猰挩璏瘛笍巁裚呭溎攭靾瓗餀悘蓕禲珕梊掜㵝䳏䱥䬅㝣㓷䲪䙆䄌㪒㜒䡟㨹㘑㩨䘙㓹䇽䦇㡂㸷䚕䄿㳪䢃䭁䏅䚉䁹䄟䆿㙪㑦䤞㡼㜆㖂䨆䅄㯔㾐㦣㡜䟤䶏䬽䵻䎈㬩㰥䶑䗟㿃㲅䂱䩢䫔䤱䇧䓲䔾䜞䠠㿛䋵㽝㡀䏿䐭䶩䀙㨅㥷䇩㪈䧥㻰䕍䰏㴉㸄䛖䤧䶍䎺䎮䟷㼖䨖㵩䲦㥣㹭㡫䟡䀸㓯㭡䇤䠘㑜䩚㗣㛳䓞㤡䶓㔺𧫚𥶙")
    PingShuiYunInit(
        allSheet, 3, 8, "外帶靄賴籟泰瀨艾害大鱠藹蔡蓋壒柰奈鄶太汰獪丐馤磕癩旝忲糲軑[地名]愒釱濭瞹藾糩堨噯戤嗐跢忕廗篕忦冭贎攋匃餀鴱摕溙昹刏艜棑胈簤婡舦瓂毻笩渿瘌㟋䮑㞭䡷㐲㲡䯤䱞䈆䨠䭝䔽㪡㘷䲚㲕㥭䓶㞧䠭㯂㧩㮏䊪外會旆最檜膾繪沛貝霈薈澮狽昧兌儈蕞翽蛻廥酹襘噦祋禬駾濊茷杮徻鋇梖浿癐璯鋷戻裞珼綐餯幆姵鐬鈗郥眛杸襊頪懀祱瀢犡翇娧絊劊嬒馷瞺昁稡䔴㝮㸽㙂㤄䟺䢈䠿㣛䬈䰽䵳㛝㸬")
    PingShuiYunInit(
        allSheet, 3, 9, "界怪拜戒債快邁隘派敗賣介壞芥械瘵湃憊薤寨誡懈唄屆稗聵蠆嘬疥廨砦蒯玠犗噲解曬夬邂韛瀣噫[飽食息也]价喟齘粺勱獪孬蚧齂欬柴[柴藩]佅躗繲魪衸阨咶唏駃[快也]呃嶰譺韰賹吤懀膪袃悈欯攦庍簣炌欳丯紒蕢楐棑欼琾祭汖慸囆狤祄噧帴浿骱睉烗眦[恨視貌]訍餲斺鶛砈嘳忦嬇纗謑妎璯庎喝蘾㬠䪥䯰䜕㑘䅬䢙㝏䶐㠹䇒㧔䈛㠔㳗䛺䵘㾏㞒㦅㿍䖰㕟㒠䊽䝽䘍㭛䒔䦏䦤䴝㖑㳦䚸㶔㿄𣏟話挂畫卦絓褂鎩殺衩尬繣瘥罫榨睚嗄詿杷舙黊澅諣䛡䇈")
    PingShuiYunInit(
        allSheet, 3, 10, "愛態代慨礙黛菜再槪戴耐岱槩貸賽靆袋在睞嘅埭賚塞[邊塞]曖柿靉閡裁[製裁]載[載運]襶逮簺縡漑玳薆鼐徠[慰勞]欬縩鎧愾咳怠劾曃瑁棌褦輆皧采酨摡嬡蝳燤螚墤埰蚮栽[築板]杚儗懝棑瀻婇璦佴洅柋鴱㤥䣬㾢㝵㕢䒫䚅䵧㻖㧉㙕㑷㕌輩內佩對碎背廢退晦珮隊吠穢塊妹肺配潰喙耒昧誨闠碓刈乂憒焙痗回[音繢]纇淬倅沬磑憝酹悔瀣悖頮礌晬繢靧頮倍北瀩抺啐綷儽鐓邶韎濧薱圚儽孛攂眛敦朏昩誶褙茷捘脢癈憞篃繀胇啛蝐槶鮁殨鼣嶏苝犻顪砩饖橃靅柭銇錊嬇烠鞼嚜杮櫑鼥膭燊蓌螝櫠哱埣怢獩慖轛礧瀢刏詯頪琗簂睟祽跊眊[好也]姵䨴㾦㣻䃍䉪䕠䯟䋳䏗䨺㑍㘨㐻䵢㳃㫲㲼䠩䘹䀛䌆㻗䮹㔨䈐䊃䩈䜋䚨㠚䐴䃀䂕㬣䒹䉬䣂䛛䖊㥆")
    PingShuiYunInit(
        allSheet, 3, 11, "潤信鬢印進陣訊仞峻俊鎮燼晉駿順刃舜震認吝振瞬迅閏愼覲衅殉軔浚櫬襯疢胤殯徇贐藎擯饉藺畯躪憖趁[追逐]汛僅燐磷餕牣陳[同陣]舋韌訒親[親疏]憖遴紉蕣雋[同俊]墐[塗也]殣酳菣引瑨晙儐賑堇搢盹娠袗呁瑱瑾殾楯圳診蜃齔睃驎螾縉轥焌靷鵔囟攈瞤侲嚫橉儭訰垽葰檼甐閵朄塡鬊枃抻菫琗扨焛稕螴璡懏洕麐眒疄鋠馸螼覕茚毥帪濥鏻夋諄湚軐敒揗獜侚岕賐寴挋汮瞵[視不明貌]寯奞杒綧鈏歏迿屻阠埈鮣嫤璶溍廴橍猌瀙荵臸䭀䏰䗲㒞㠴䀔䴄㬜䀢䚏㧈䢯㢙㣀㷠㝻䒖㸾䛜㼱䪿䦞䉮㕙䚱䜭䚔䗯䞋䑞䫃㖁䛨㶦䏖㪦㠈㐰㥧㝦㶳𠬍𧥺")
    PingShuiYunInit(
        allSheet, 3, 12, "問郡韻運分[名分]訓暈奮愠醖靳糞紊聞[名譽]近份僨腪璺焮捃瀵鄆餫汶[水名]隱蘊絻坋煇拚[埽除之名]忿堇[國名]抆攈垽韗懚緷秎渂鱝鶤檃員鱝檼珺賱妏泿挋鼤忶鵘鑂莬縥桾鐼歏縕馸斤[察也]脕枟臐魵㨷䩵㸪㟦㥼䝍㡈㱵㧆㒚㡥䲰䚋㿎㞬㴈")
    PingShuiYunInit(
        allSheet, 3, 13, "恨論困寸嫩悶頓鈍遜褪坌噴溷巽艮慁遁噀鐏囤奔[急赴]諢搵涽捘睔碖硍摌媆憞殙謴焝敦[通作頓。]陯瀳焌忳炃睴㥃㯎㥵㫻㫔䅱㴫㶧㨰㧷䵪䭡䭓䬶䍎䤜䫀溣茛涃埨銌袸詪扽拵俒捹顐渀健愿怨願万萬勸獻蔓建憲券楥曼販飯遠[遠之也]郾圈[地名]堰綣畈挽腱畹媛蟃番旔毽隁獌韏妴踺褑謜絭婏僆脕褍鄤閞鬗鬳楥傿贎卍鶨傆槾瓛褗虇臶汳椻牶奿瀗漹嫣㪻㰽㝃䄐䇟㬅䛄䏍䉊㸘㽹䧮㤪㤆㜛䝡㶗䡬")
    PingShuiYunInit(allSheet, 3, 14, "亂漢岸半畔看換嘆旦觀[樓觀]玩案爛漫喚粲翰幹貫段炭難[災難]幔汗爨絆燦竄冠[冠軍]熳腕贊泮煥灌散璨彈[名詞]判閈榦斷按惋渙叛鸛鍛旰算奐懦瀚捍蒜逭伴漶悍晏館憚彖瀾沜骭罐瓘祼煅盥矸犴墁鑽謾浣毈鼾[臥息也]讕涆桉[同案]衎垾灘杆攛緞暵駻爟愞諺宴豻頖捥碫哻盰縵侃碳雚簳抏鴠笇釬靽偄螒攤[按也]胖巏熯疸酇垸椴餪痑腶鑹瓓悹獌牉饡鏆毌忨愌怑湠鮟澯姅矔殩洝狚忓肒婩釺嚾瑍兓拌觛鶨妲皔傼雗檊鑚湪妧睕皯喛褖峖咹穳鑭淉竱攼倝坢仠遃錧錌糷躖薒貚禶遦梡灒暺屽詊帴衦灡瑖溿馯鱹碝槾媻蠸厂襸鳱炍灓䡬䝺㬮䯛㛶㪱䮗㪋㱫㪵䏎㢨䠉䛃䥗㡢㵄㜺䏷㽩㯘䅁䀓㣓㻮䃹㬇㲦䗰䯎䕿㡺䯘䮧䎯䬤䝢㛑䍐䕕𤳉")
    PingShuiYunInit(
        allSheet, 3, 15, "雁幻澗慣宦患辦諫盼綻慢間[間開]瓣鴳串豢莧贋丱訕篡晏汕薍襻扮閒[隔也]虥覸嫚擐棧轘骭襇鏟綰虦謾扳柵縵疝僈涮剗藖羼鐧赸孿槵輚卝矔騴銏繯菚摱暥摜奻梘洝摜鳱覵梡澋贃麲妟鋬睔姲瞯粯蔄繝釆綄䴮䋎㵎䆠䍺䊲㕕䚲䗃䉯㬄䒛䙪䳛䙮䁙㝈㹖㻵䘺㷳")
    PingShuiYunInit(allSheet, 3, 16, "見面變遍殿燕倦戰賤院戀羨扇練彥片綫縣箭傳[傳記]電荐薦硯甸便現霰眷饌囀掾茜膳奠絹顫鍊擅煉絢宴眩弁炫譴轉釧衒禪[封禪]咽援[救助]濺嚥汴卷[書卷]罥硏[同硯]旋[打轉、屢次]鈿唁繕淀忭碾暗倩抃善緣[衣飾]選眄先[先之也]纏澱漩衍卞劵楝瑗餞遣麪靛牽[牽挽也。]眴拚[抃本字]煎[甲煎]狷佃瑱竁煽勌撰騙堰諺晛惓媛飯穿[貫也]孌渲輤嬿綪昡剸昪袨縼悁[躁急也]鄄湔鬋桊甗俔繾淃睊涀帣塡晵騗餋鋻臶弮這揀輾僝圈[猪圈]蜆樿騸諓浰縓莚狿湅葥獧贙絭鄯嵃萰栫婩癜褑衏軐埢蔙蜔噮烇瓹孨閞玣禐瑓趼琔鶨勬哯湣迿汳姰繏抁梘婘僆曫牪夐珔偭襈裫鼰堜瀳棈汧嫸縳橏鰊梋纞刋糋灷琠烻覵溎涏檈槇驠矎瞑[瞑眩劇也]咞怰惗豣篟儙擶閵飬睼猭糆駨袸蒝媡肙硟帴謆楥汌姩摙灓頨繟牑廎諯匽竱婝橂榗怋鱄牮皘闐[于闐，國名]䄠䢭䉵䈠䖭㯠㪨䪈㭇㪇䝮䅈䪻㜃䀎䍻䡓㧦㞟䏒㳎䍗㴐㸤㳬㝸㺹䑶㴜䥖䢥䵖䠣䀏䬼䒪䂩䛉㢾䴏䛹㬫㼑䡀䬇䆄㪝㬗㢧䡪䄅䨘㭓𢿌𤩱")
    PingShuiYunInit(allSheet, 3, 17, "笑照嘯妙調[音調]詔廟釣眺召耀峭嶠料叫竅要[重要]誚徼曜肖燒[野火]療弔釂俏藋蔦少[老少]跳[行貌。]邵獠鞘[劍鞘]醮劭糶窔驃噭漂[水中擊絮也]譙[責備]掉轎[𨋖車也]噍銚炤燎穾剽[砭刺也]鷂爝哨蓧窱脁嘂溺繞票嘹悄[急也]尿裱僄約鷯僬搖[音曜。亦動也]瘭鐐俵偢覜嬥朓卲窵誂尥膫潐趭藠獟摽葽[草盛貌]瘹髚艞伄帩僺嘺讑抭絩撨璙尞踃炓鸄晱熮嬈[不仁也]訆鋽嬓熎鷣篍嫽枛筄獥竨敿顤劁篎訋敫顅瞾蔈翏顟莜徱樢顠覞熽窲嫖[輕也]鑃鐈䔄䊥䂃䔙㗛㢗䠷䎆㔅䆻㴥㬭䬰䉼㬓㞙㚁㞁䏇䃝㳮㧼㰾䐹䇌㿢䢧䨅㙩䞄㷖䧂䊮䆗")
    PingShuiYunInit(
        allSheet, 3, 18, "貌孝豹鬧教[教訓]效校罩淖窖稍炮[槍砲]棹趠砲覺[寤也]鈔泡珓較疱樂[好也]橈膠敲礮坳酵巧恔儤哮[喚也，呼也]獶笊袎踔箹爆[火裂也]窌靿娋刨斅拗艄挍餃婥睄潲撽岰嗃髱烄骲麭緢犦詏悎奅仯礉洨漖軪䶂䑲㹸䏴㹿㒵䡚䫉䶌㯡䍜㷹䔠䈇㘐")
    PingShuiYunInit(
        allSheet, 3, 19, "到報帽操[操行]竈傲噪奧盜誥號導蹈耗悼耄勞[慰也]告隩躁暴[暴虐]道好[愛好]奡冒靠嫪氉漕燾造[就也]犒膏芼抱掃翿驁倒[顛倒]幬[覆盖]瀑瑁墺眊纛糙禱慠曝鑿秏瘙郜懊燠搞謷慥鷔謟旄套縞埽澇癆澳媢鏊軂嶅髞鮳憦髝僗毷軇橯璹瓙蔜镺烄哠菿耮襙萺鄵祮覒祰鐭藃艒鯌嚗芺冃擙喿叝扷檤圫鯌翢鼜䤖㟼㜩㬥㧌㿞㪞㘪䊭㚪㺺䒵㞻㿋㲒㴘䌦㜜䋃䜒䎋㥿㲧㙱䚽䐧㚐㒻䪽𩼈")
    PingShuiYunInit(
        allSheet, 3, 20, "過[歌韻同。又過失，獨用]臥破座和[唱和]个賀課餓唾箇[枚也]些[語辭]涴磨[磨磐]貨大做挫坐個邏奈[那也]佐惰作懦[怯也]剉糯簸那播左銼莝馱蹉堁坷軻磋愞他刴媠癉譒騍逤盉蓌哆哪啊髁蚵摞毻藦耱袔蔢誃欏腂硰夎楇娑[邏娑]袏襎吤侳跢攠侉尮沎敤攍鐹俰纙涶痑桗挆䙃䃺䞆㘞㰤䇔䉓㿚䟶㖠㳀㞅㾧㵑㟇㘸𧟌")
    PingShuiYunInit(
        allSheet, 3, 21, "夜化駕暇謝亞榭稼架罅嫁駡訝下華[華山。又姓]詫怕麝罷借跨射舍[廬舍]詐卸蔗赦迓柘藉乍價夏霸咤瀉稏炙壩帕汊婭砑靶姹吒嚇胯假[休假]斝嚇灞鷓差[短缺]岔貰禡籍把[與弝通]蜡厦嗄弝榨嗎髂睱賈[姓]樺杷耙衩獁鵺奼諕蓌槬酠渣唬哆哧掗偌榪觟爸跁侘摦褯鬕厙傌杹騇閕揢哋膪嗻諣坬衙[與迓同]侂仛疜鱯犽愘芐懗謑搲渃誜笡宱夎狛躤灹俹砟椵踷疨觰閯涻襾訍矺叭嬅䏑䕢䄍䆉㕦㣾䟕䉣䤳㰳䂞㖡㾝䃎㓔䵭䣕䩗䒲䖳㴬䃻㙈㾺䆛䗪䠶䩾䧞䢝䀅")
    PingShuiYunInit(allSheet, 3, 22, "望壯相[卿相]浪悵唱帳恙曠狀訪將[將帥]漲嶂樣障尙舫釀亮上讓妄喪[喪失]漾況餉暢瘴匠量[數量]葬貺藏[庫藏]謗王[霸王，又盛也]向忘傍[倚也，亦近也]放愴[傷也]宕抗杖纊諒當[適當]颺醬創蕩誑幛旺閬行[輩行]倡鬯桁[椸也]壙盎仗亢長[度長短]養[供養]兩[車乘]仰[恃也。俟也，資也]頏揚[同颺]絖嚮張伉悢擋韔炕脹臟[內臟]吭碭妨賬儻[倖也]償怏強[倔强]防榜[進船也]鄣[與障同]廣淌閌踼旁瀁喨醠煬艕燙饟畼曏掠綁棓懹糨菪湯[與蕩通。又與盪同]矌埌羕烺棒誆桄[橫木、充滿]晾攩戧爌迋逿儾塝枊懬哴搒湸軦弶犺唴緉囥岲櫎焋嵣晑摾掚諹凔懭盳姠焻摥畺曂嫎蠰邟鐋趽摪姎賶蟓嗙砊鐋趤珦瀇焵瞕瓺俇蒗柍詇礑臦羻眖灀倞嵹徬圵逛[欺也]欀邡萫潢[與滉同]恦蚢俍眻誏撗䩨㼽㤮䩫䅮䦒䵁䵮㾗䭐䍚㔀䞪㼜䬬䤑䕞䦳䊑䬺䀶䌙㢓㙣㺊㫛")
    PingShuiYunInit(
        allSheet, 3, 23, "病命鏡性詠凈盛聖政映令勁競正姓柄慶敬竟孟逬聘鄭泳橫[蠻橫]硬更諍儆獍凊行[德行]迎[往迓之也]評[平言也]另夐幷靚榜[進船也]幀偵輕[疾也]倩[請]證醟阱証請掙禜摒晟娉盟[盟津]碰婧渹摬檠請詗邴鋥跰怲啈詺胻璥鑋曔絎詇鉼掅墭妌梷滰誩澃賏靗窉悙倞眐姃賆浧鈵貹狌絎矎瀴寎牚儬竧炩朾葝竀鴴鞕㡠䈣䀻䓝䨻䔔㽀䛭㘫䂻㶇㼞䡖㡧䰢䙬𩓞")
    PingShuiYunInit(
        allSheet, 3, 24, "定興[興趣]徑勝[勝敗]贈暝[夜也]應[答應]磬磴稱[相稱]乘[車乘]聽甑罄賸佞蹬瑩凝[止水也]凭飣亘孕瞑鄧媵鐙[鞍鐙]秤凳醒碇瀅亙靘綮證錠經[經緯。又織也]瞪凌[冰也]庭訂濘嶝釘[以釘釘物也]廷隥瑩脛甯譍[以言對也]穪懵蹭懜墱鸋鑋倰踜靪掟膡揯碃鎣冥鋞鼮氶芿掕堋誔濎橙[几屬]濪驓俓鱦殸霯覴堩烝[熱也]碠傰臖桱掅褮榺僜邆痭睲蕂撜靐忊㵾䒅䒌㲌䥌㿦䠬㣷䲛䵴㹵㑞㚺䙢㞌䮴䱆䰝㮓㓈䱍䔭䮚𨆪")
    PingShuiYunInit(allSheet, 3, 25, "舊秀瘦袖候就晝漏奏岫繡透豆茂陋溜宙構鬥竇皺寇獸驟謬胄臭逅又究后鬬鬭[爭也]堠祐逗甃酎幼救嗅彀後狩狖搆售覯咒廄耨宥壽凑鷲疚覆囿詬籒遘漱輳右霤縐富脰鏤僽侑授宿[星宿]蔻畱[宿畱，停待也]媾走厚購雊懋貿咮餖冑首[告發。自首]扣受柩銹戊簉仆[頓也]守復够姆副繆瞀餾腠僦嗽叩袤廏綬吼鼬讀[句讀]鷇冓收[獲多也]蹂糅柚佑灸廖琇繇[卦兆辭]釉嗾漚[久漬]姤糗槱廇句[句當]鄮伏[禽覆卵也]揉癅謏噣[喙也]懤愗畜痘鱟楙佝蜼釦擩揍塯貁鍑楱譳窌狃睺油[地名。又與釉同]毭複猶[獸名]輶雺飂輮僂瘻酘娒螑鍭鎦鷚浢筘豞鈾姷怞匓鏅怐栯迶瞉煣嗖粙櫾駎惾韝慦竎鮜骺疛凁斣嬦鞣撀暓鴢猚磂牰璓糔溴鏉輻韖峟殧郖敊嬬鮈嗕煹憱熰梎豧袧鯦遚嬼鬸鄇蜏椆窛蔟[律名]珛褔洉䀁㖟䙔㳶䳹䊘䩜㜌䍍䝭䪖䤅㗜䃓䋓㕻䛆㑳㖃䔰䟬㔷䟝䒄䆜䞧㦞㗕䀤㛒㺠䦣㲃㵵㡱䋴䅢㔿㼙㩆䬦㽬䔏㙧䞬㨌㝊㶯䬨㰯䐢䠫䄈䓮㙀䇺㔌䠐䪷䩽㝌㝤䜬䛵䛠㹨㠇㤱㝅䞥㢄㾭䌂𤬏")
    PingShuiYunInit(
        allSheet, 3, 26, "禁蔭讖浸任祲沁鴆闖賃譖滲飲[使飲]甚深[度淺深]臨枕窨寖紝吟罧喑[喑噁]噤揕紟衽鵀癊沈鋟妗妊僸酖[通鴆]吢邥齽笒瘎赺愖鈊鈂抋搇侺莐伈瞫扲搇夦䜟䶖㓄䥠䏕䧵䲴㱽㼉㵕䜗䑤㤈䈜䌝䫴㯲")
    PingShuiYunInit(
        allSheet, 3, 27, "憾纜暫瞰探擔[所負也]勘暗紺歛淡濫甔賧磡澹[水搖動貌]憨墈唅啖[狂也]闞闇憺贛鏨憛霮壏爁僋汵嚂莟腅俕琀淦儑浛沊詌誩馾揞閐錎倓篸懢參[參鼓]黚竷癚凵帎撍蜭顑饀姏瞫三[三思]婻漤顲䌫䬓䯥䗊䀍䲺㤾䫅㜮䐺䨵䟅䘓䐄䗣")
    PingShuiYunInit(
        allSheet, 3, 28, "念艷焰店驗灔塹占[占據]釅贍墊坫僭窆厭殮饜劍掞砭覘韂欠斂苫佔傔潛瀲煔醶曕沾[水名。縣名]舚淹歉忝鹼襜爓痁俺熌噞獫驔酓裧嬱艌嬮鰜幨埝譣槧兼鹽[以鹽腌物也]覎爁菾敥姭裺殗羷澰趝嶦頕脅[妨也]稴覎棯㮇䪜㝪㶺㷔䠨㙴㛪㣣䛳䶫䃸䀡䯡䃱䊴䧔㱨㟻䱤㪁䦲㼭䁮䈴㜞𪙊𦁤")
    PingShuiYunInit(
        allSheet, 3, 29, "鑑泛梵監陷汎懺蘸賺鑱站帆[張帆行駛]欠餡渢摲釤訉儳劍湴譀讒闞[犬聲。獸怒聲]甉釩埳[同陷]艬覱揞溓顑肷錎臽滼淹韽湛[姓]䪌䬚㒈䀀䜛㦑㣌㸥㺘㽉䱿㪠䶟㕨")
    PingShuiYunInit(allSheet, 4, 0, "竹屋谷目木熟菊腹哭服肉獨福速逐祿鹿麓肅軸牧宿[住宿]卜陸六族筑轂祝沐斛馥穀犢掬縮築牘叔讀[讀書]粥簇蹙育禿覆碌復伏穆瀆戮淑蓄縠矗扑幅鏃菽漉竺燠蓿蔌撲瀑麯[酒麯]簌櫝睦鵩鞠鶩觫蹴簏蝠黷郁霂塾澳謖夙轆餗麴恧僕[羣飛貌]畜榖衄洑濮蔔槭樕毓輻朴複孰匊倏濁舳醭讟樸輻鬻僇煜角蝮稑暴[日乾也]箙昱彧槲曝啄鞫朒盝韣匐睩琭齪蓼蹜滀毣忸鵴瀫俶踧袱鷫柷澓髑輹柚搐摝瘯慉殰鏕碡副[剖也，判也，裂也]囿菔茯薁剭螰苜踀喌嘼蔟虙趚驌蹗鱐楅贕鵚簶閦噈繆[與穆同]稢虪穋觳朷告葍腛勠鋉瑴縬濲摍藗焀蓛熇遬汋[激水聲也]蹼唷唂橚趢儥蜟拲娽坶蔛涑樚鶝踾跾豖匑翏錥圥鴔趗栜棴鮛楘蚞襡艒纀蕧栿獛熝嬻躹鵱蔍茿剹諔踿喐韇蓫沑鱁蠨梀惐梮皾莥逳箼荲騼宓騳驧潚畐斀稪萺莤玊哊鉐鵦癁鉃粶丵焂埱坴襆敊涋粷喅蓻鱳瓄珿軮鰒踓剢犕鑟蔋椈嗀聏琡鞪鏉蘛鼀疛巈淕絥鄜齱璛淯璹樢婅蒮斣穙鍙趜雮偪阿[阿誰]疁骲篴媨罜殐掓稶嚛磩槒膔栯礇炑鄐鳪轐殧塶螜閰媉棛篫諨摵椱砡樎鎐誎垘苖婌泦椂鐭攴堉嗖鯥觷觻䘵䩮䮷䱙䎘䍡䉛䃤䛢㳤㰗㜚䞱䃙㕰㰲㓘䑿㚆䫝㽤㥔䙒㶖䜡㲫㩋㧅䟿䥮䘻㓐䢱䟟䋭䢗㑉䗇䴪䇚䃞㪩䑁䔎㦇䊾䄾䘐䋹㜙㮋䏋㗤㤢䗛㥌䶊䪁㠅㣎㜅㬼䐨㼾䧤䎌䡜䕮䈸䜯䫳㾄䃚㘲䏱㝛䨱䵈㾥㻃㒔䪕䟮䌒䎼㖨㴼䮱䳱㡔㵀䨹㞺䞽㑐㛬䙯㪶㯟䤋㙏䗱䚼䎑㯈㜈䛙䜼䱡䐿㑛㯷䐁䀰㣃㷤㺉䀲㹼㪖䖡㽇㾇㞘㬘䇍㦽")
    PingShuiYunInit(
        allSheet, 4, 1, "綠玉俗燭足續粟束促辱局鵠躅欲錄蜀觸毒浴獄旭矚籙屬酷淥醁篤沃曲贖褥斸勖督囑溽梏縟鵒纛菉騄蠋蓐瘃峪趣牿頊僕鄏幞裻告挶鳿嚳襮歜輂斶鋦鋈逯藚媷臅慮憟匤熇臛旮[同旭]蛐欘趢犦哫灟拲娽傉彳鸀駶軉筁蝳蠾趗髷鏷薥鋊脨砡檋琟輍頶俈捁澩斀珛钃搙潥隺絭悎觷螸傶襡鈺洬嚛錊噣孎錖誎嗕斣襆疁梮捒蔋鶮䠱䪅㯮㒒䒼䟉㮂䥔䌚㙇䞖䶜䎤䌵䜹㻿䞝䧊䕽䙱䐂䳔䡞䚄䑑䅶䋰䚛䛤㫽䱚䴰㩴䴆㿥㔄䧼䅇㦺䈞𤌍𧛔")
    PingShuiYunInit(
        allSheet, 4, 2, "學岳朔幄渥角濯邈握璞剝覺[知覺]琢确卓殻雹擢鷟槊斲犖捉駁濁喔啄榷桷數[頻數]朴駮灂諑樂[音樂]齪樸埆搉啅鐲較倬珏戳鸑涿翯鷽跑桌踔娖鸐硞嶨椓擉藥浞謈愨搦碻[同确]鋜豰懪穱欶爆瞀瓝偓瑴韄嚗傕箾穛噣眊觳搠斠斮齷掿捔趵礐蒴烞晫洬嗍鵫墣蠗窇鞄籗瓁悎瞐鞪皃汋隺鎙劰燢豿娕礭仢欘韷澩颮矠骲楃斀丵瞨墧鰒硺觷腛燩棹[樹枝直上貌]釙鑡簎菿龏斅攴顜齺篧捳髉琸珿犦籱搻壆鳪媉齱殐㧻㲉㩧䃗䓎㙾㰌㓸䂍㮶㼎䈏䑈䁷㰒䃕䪨㔬䮸㱿䦠㙸㺪㹒㿺㺟㪬䇶㱋㹊䨌㴶䡈㦝䥤䮓㵡䥃䠎𦢊")
    PingShuiYunInit(
        allSheet, 4, 3, "日筆室一失密實術疾逸律畢匹膝出帙漆栗溢詰七橘必述秩吉蜜恤瑟乙質櫛秫蝨蟀蓽悉慄黜弼叱潏嵂嫉汩朮謐戌昵窒篥鎰率侄怵鑕騭壹卒[終也]篳絀節佚苾鷸軼蹕馹茁抶桎喞姪崒獝繂沭疋韠遹繘泆罼鳦袐銍衵蟋凓飋聿飶霱咥蒺袟蔤沏泌鴥蛭佾訹珌妷挃鞸礩厔耴尼[近也，止也]茟肸熚觱堲翐紩桼傈瀄踤窋姞駜溧晊帥捽矞佶拮鷅銊馝璱饆佖荗膟鴄眣瓆鬻摔圪咭沕疙宓蛣滭枇[枇杷]鉥郅鵯銡楖怸螲怭鉍潷趌黢鱊痆窸齣滵柣庢呹箻鷝秷峚狤珬欪祑胵螏逫蠠秖抳塛榓跮恎絉鮅欰炢咰趉袕揤浂擳銉肷柫衹眰比[比次也]鏎腟僁焌搮恄箤燏鴓笜怷麜臷鮚豑犵臸秪[與秖通，適也]蝍詄瑮郆縪妼琗寽祇[適也，僅僅也]嬄宲鶐炪鴶邲祗[與祇通，適也]胇欥洷柒暨彃淧樒膣魓槉鞊櫍驈蹫欯釰芛䫻䁥㗚䘌䭿䬆䟆䎉㘉㾁䮡㔕㯃䢖䫕㵥䮇㪤㺩㻎䒤䏘䑇㓖䶡䵒䢞㗧䬹㻫䬛䳳㟳䔁䩛䢦㚕㣟䬄䣛㴵㮿㜱㜼䱃㑁㤕䢤㞊㫘㣰䄶㻶䔞㳑䌏䡃㧒㢶䤎㳚㰵㗭㘍㳼㮚䱣䟈䏄䆝䘤㔑㢸䜉䳀䰬㺷䋖䜠㳴䖩㻭䵑䢕㗌䟣䤉㖅㑵㲺㤜𧗿𩋡")
    PingShuiYunInit(
        allSheet, 4, 4, "物佛屈拂紱乞黻綍勿紼祓詘鬱訖屹茀韍倔黦咈弗歘怫髴芴欻仡蔚刜沕崛不[與弗同]吃[言蹇難也]掘熨岪汔迄坲镼釳厥[突厥]魆肸艴[色怒也]尉岉沷菀昒忔鶌粅灪帗炥誳鮄芞柭爩紑嶏蛂昲冹莔烼袦虳柫弡翇趉伆鉘乀砩阢笰甶芾惌㗵䘿㭾䏌䎢㷉䵥䭮㐹䖇䁌㻕䒗䰴䛥㪄䞞䠇䞷㠨")
    PingShuiYunInit(
        allSheet, 4, 5, "月發骨闕沒髮窟忽兀伐謁袜樾鉞笏粤蕨突襪渤惚歇勃歿罰筏越窣曰閥蹶柮訥卒[士卒]屼劂橛猝獗羯杌矻矹竭卼滑[亂也]鶻軏腯搰咄淈垡硉蠍崒紇揭碣汨馞撅峍蟨核掘噦刖愲狘扢凸暍孛浡嗢堀鷢揬悖訐捽曶榾泏扤鱖蚏抇閼齕抐瞂胐麧玥蜶匫钀莈不厥崛脖唿昒餑鵓梲囫鐝犵鈉膃淴怢餶艴猲蓇桲葧椊葖稡阢昢瘚侓馧[馧馞]飿蚎荸鈯嶡絗縎鼵鶟杚枂颰冹榲趃亅埣坺顝熓怴朏籺摕侼欮堨迌趉寣搵瞃囝憠宊殨笜舭郣捸璏抈殟橃沷熭碿藅鋍尳湥岄垏鍎歾琷鍻啒瘟[心悶貌]糏哱犻貀鼿榲挬㪍䬂䓤䎳㷎㶿䞘䨚䑔䬍䥟䓛㖀㫚䴯䚝㪐䦍䟠㻠䎀䖓䘚䣹㳷㩿㐳䩐㧾㟑䪬㵐㒴䡇䝆䑢㨡䀜䯇䟜㬞䇅䂗䁫㘺㴾䯿䋐䙠䭯㔜㵠䍪䠈㲞㞽㧮㾶㛘㽾䮩䪲㕹㛲𣔻")
    PingShuiYunInit(
        allSheet, 4, 6, "闊末活脫渴豁鉢奪闥葛割沫聒抹遏撥潑達括秣剌跋辣魃怛薩蝎斡轕栝撮筈撻茇躠撒捋喝頞臈鶡敚褐鞨掇拶鱍糲囋喇獺鈸适[疾也]韃靺澾髺裰妺拔閼噶剟躂曷軷毼摋襏越咄蘖噠獦呾泧嶱醱犮胺炟胈焥薘繓鴰捾暍鏺丐挖轢碣捺咱叭侻饐齾妲嶭笪齃猲瘌鵽蛞蝲敠靼嵑濊帓枺粖姡頢攥囐揦蟽茉鼥癹礤萿毲秳癶莌妭頱濣趏蛶睕柭嬒餲炥魩秡狚冭灒懖羍磆劊洝昩橃堨坺奯鬝匃驋攃汰痥燤螛咹幯湏颰仴鮁蔎眓襊橽歇馛葀佸昲噧揧鮵啈蹳挩炦攋抈骱皌鶷枂砞瓎脟懀眜䌨㔇䯋䡾䴲䅥䍨䟯㦫䄑㳨䁊㸊䒷㓉㵶㿣㞈㕲䫘䏞䟦䶛㻝䟛䢌䄆㵧㣵䦢䯏䵣㧊㒓䣶㶬䯦㮫䣪䱫䦚䈓䕣䃮㿹㣞䖧䳁㵣㺚䱅䯺䳚㞉㖕㭮䣮㩵䬴𩩲𤸎𦤦𠱥𧙕")
    PingShuiYunInit(
        allSheet, 4, 7, "札刹八察轄黠軋戛殺煞刮猾哳扎恝揠瞎秸滑圠楬拔蚻肭擦嘎茁嗗窡刷齾鍘妠豽扴鬝扒[刨，挖]鎩稭榝螖搳頡劼娺圿秳痆帓汃鶻帕獺捺咶刖紥鴰錣磍鴶擖砎捌朳哵鶷傄礣劜窫詙鮚聐磆柭菝詚蠿猰颳耫捾糪忦硈揳玐骱眣摖鱊咭閁捖帴睰釛嗐縖袺檫趏仈歇螛袹鵽叭釟貀䀣㗫㓤䕓䝟䦪㮖㔍䴳㓞䫄䀨㨸䃰䶪䱻䯉㑻䓭䥷㭭䦖䵵㪴㕯㳐䚴䂒㺴䆯㔠䤢䰲")
    PingShuiYunInit(allSheet, 4, 8, "雪別絶滅血結拙熱穴潔鐵裂列烈缺轍訣傑舌悅節徹説設屑決哲冽劣咽[嗚咽]閲切澈折纈闋輟孼鱉玦瞥竊啜鴂爇埒紲齧垤截擷挈跌耋泄掣嵲泬譎歇撤吷糵孑涅迭餮撇褻薛蔑洌鐍竭抉蕝瓞桀惙噎拽浙卨楔臬契歠闑閉絜綴蠛僣臲褉頁觖襭霓篾碣絰揭捏蹩衊凸蘖巀昳岊媟呐驖莂隉軼緤晢頡嗶楶朅蛚禼茁趐刷掇苶嶭焫茢捩鍥揲蜇摰咥訐蜺渫癟碟拮醊梲搣癤蠥蠘丿鋝蛭桔鷩橇迾趹蛣槷偈辥悊颲幭挒嫳棳篞馝絬準[頰權也]覈佚批褐讞姪踅憋齕帨剟咧紒屮唰瀎詄趔硩潎蟞奊跮蠽咇僪蠮蚗爡刔襒畷蒛蛥嵥糏蔎懱芵鐅瞲蛈僁醛掜蝢逫鱴櫗囐藒孓赽趃袺啘蛂鮚胅鈌鴷脟敜駃蠿齛罬烲砓栨彆蠞夨呭滊臷幯鱊猰揳螲聺勶镻棙潱爄摕狤迼聅鄨笍湀洯眓攦劽坲乴鮤朳莭恎叕靼滐粖姴趌蛶魝痥袕郣覕炦洇捌緳瞮尐榝稧柭妜蛞擳栵諁籺蛪歽矞[同譎]詍睙搩靾炔眣蜹疶敠哾桖怢戜疀麧鑖眜苵嵽巁眰揊炪哷坹櫍瘛鴓虌徶疦馛砄毻燤櫭菍暼娎剈翓㧙㙞䨮䁾䥫䆷㿱䫾㗧䕵䖦䚢䞵㴮㛃㬯㔢㴪䇷㩪㴽䌩㝂㲳䫎䘊㘿㓭䅀䭇㯙㳿䋉䂼䒸㮮䌘䂐䳤㭞㓗䙽䩤䦑䪼䆕䊦䱑㸞㩢䦬䊝㖶㢼㸹㤠䯵㐖㨝㬚㭩䮕㭈䩧㖏㔃㔡䍳䫼㦢䆢㘶䟹䛎㹟䠥䋢䤿䏟䭱䝌䟙㔎䘷䒆䘁䓆䨆䏳䟾䞰㼤䀗㣯䩏㒝䏐㕞㸅㓶䈼㞕䥕䏲䲙䐼㽟𩠻𥄎")
    PingShuiYunInit(allSheet, 4, 9, "落薄鶴閣壑寞郭托酌漠泊略腳雀卻廓昨託躍洛弱縛惡鵲作萼樂[哀樂]約諾索爵削鑰橐絡著博錯箔鑠著[同着]藿謔籜虐柝幕灼鐸嚼礴霍怍鶚藥愕瘼爍鑿屩若酢籥鍔託[同托]搏酪勺崿粕噱攫杓斫度[謀也]鰐蠖雘彴各掠莫貉涸鑊諤綽瘧鄂穫瀹堊恪珞拓笮魄摸駱膊椁爚膜[肉膜]箬矱擴噩蘀雒玃烙繳擱堮鎛蠚濼妁遌鞹焯[明亮]齶龠彍澤[星名]爝格[樹枝也]獲蒻亳钁艧飥礿礴矍醵咢襮躩蹻躒臛鏌郝硌皭霩臄篗皵臒鑮熇[與謞同]踱芍岝矐郤皬轢柞嗃煿蒪蒦糳愨斮汋攉靃謞欂漷戄瞙飵鄀汑鄚蝁獵躇[超也]昔琧燋暯婥厝咯逴喏胳迮鷇貜顎犦隺鐯瀖碏袼嚯鮥猼喥彠辵婼硸袥烵凙矆楉馲鄗峈縸沰剒胉嚩磭餺貈嗼杔崞毭剫笿矌犳曤鞽踖焲櫎蘁偔娋莡稓慔謶蛒仢藃莋櫮鎍岞秨逽魠敫覨劐斱擆狛搻鶸彏圴嚛鈼撗谻櫡湂扚葃鑩棤檴噋矡鱳籱溹嫋[長貌]擽庹庴縒矺癋妰詻嬳龥跅仛纅鉻蹃趞蠼鶮鸌茖繑禚鉑墌癨塻蠌牔鬕婩砟檡挄鰝苲佫侂籗渃蘥鸙溺䋏㟧㠋㹱䨥㜰䱜䭦䮤㓢㸕㒂䧄䖃㦜㦡㿑㦍䨰䎰㬦㚟㤞䎊䖼㕡䌇㸲㪾㗥㨯䶳䪙㮙㨼䨣䈷㴖䅴㘀䣤䖛㩱䝫䂄䚥㷾㲋䁨䯨䫷䧐䟑䶈䶅䠯㖸㬍㓵䁻㤩䥬䛚䀩䥣䗚䌎䐘㰛䣞㕁䅵䲵䮬䬪㤰䍸㱳㗉䙏䐞䰊㗁䇥䇎䅂䤕㷬䂮㑼䧿䈅䖋㖾䖈䋤䐾䞢䢲㗘䉟䄸䨋𢱢")
    PingShuiYunInit(allSheet, 4, 10, "客白石迹碧夕宅尺席隔策惜役屐陌璧益伯赤癖柏窄百驛劇脈辟戟翮隙迫擲液僻責麥昔釋舄積額厄澤册帛坼易[變易]逆赫革籍脊擇拍謫幘磧掖拆魄瘠格斥腋奕擘懌繹畫[卦畫也]獲索磔譯適珀射舶藉汐弈檗蹠膈碩綌鶒蹐嘖軛貊隻幗炙扼賾馘螫簀骼蜴斁穸阨唶帟摘疫劃[劃破]埸躑襫虢蟈嶧啞[笑聲]摭核刺[穿也，傷也]奭嚇襞腊祏覈[同核]擿咋薜摵迮柵躄亦湱擗虩霢借踖磶搦驀穫醳鯽嗌槅騞嚄剨嫿峉筴鬲阸媳摑鶺喀塉耤齸莫[靜也]齰嗝砉蚱潟觡圛粣鼫翟愬鸊嘓齚撠貘睗洦呃[雞聲。]霸[古與魄同]謮晹縌詻橶敀滆郤霹睪胔啪哧柞[除木]硅嘀虴徦蛨佰礉檡塥緙礋漍乇覤鸅墌簂皟蕮蚅茖膕郄舴蹃曎襗鐴鉐榒帞銆雿箣鯣躤襀垎嗼鮊嵴捇擌諽庴獈砈趞膉潪枙鱯扸鳽杔瞔炈疒覞歵鈠厏頙銏犱焃檘澅燚苩岶茦蚸拺嚿袹臵樍讗簎諎谻呄鰿焟楁嬕跅丮釽鉻躆蚇眲馲坄籷狛厝慖啋脨廦焲焬熤絔啙墿糪痬棤溹矠蠌烢凙褯聑矺鏼棭謋獥貖洓葃泎窢莋劐掝憡聻厇礊韄嫧燡罊雃虉挀豛胉啇蛒瞁煂搩瘷揢蒚鶪屰焷耫碦覛豟閴㶁㗲㫺㡿䘸䇲䵂㧖㽚㛭㦴䐙䶦㥽䄷䘔䃒㮦䩹䳭䕉㼟䐱㟙䳆㩍䂹䊞䘑㮝䱮䛿㜋䜺㑊㹮䟄䬉䮮䂸䐸䳮䁺㡯㝜䨛㘌㣂㖪䮰㩇䡛䧍䌟䕪䭆㘁㦎㠛㿟䙐䈿䖌㗆䰜䪂䚂㭙䤨㿭䲽䞠㶠䣢䨫䖨㣱䁤䦝㴁䭞䊂㳻㵹䦴㼣㒀㾊㦦䞟㴒䂝䞦䪝𢮎𢫦")
    PingShuiYunInit(
        allSheet, 4, 11, "壁寂笛敵滴歷覓激戚檄績擊錫的靂瀝礫滌覿鷁櫪鏑析惕狄淅荻皪羃溺櫟甓晰冪糴劈闃逖剔喫迪靮嫡皙菂覡嚦趯甋瓅霓鵙艗幕踢篴惄適轢鬩汨[汨羅]焱酈鴃蹢籊殈赥鼊摘蜥癧樀澼轣裼鼜鬲倜礰緆秝翟鼏覭簚糸弔狊壢蚸繴薂濗砳焃霹墒砉攦踧墼悐鶪幦虉磿幎嚁瓋毄焬鐴菥譤藶塓湨鷊啇玓馰熐釽漃憵鱳纅扸樍撽儮苖爏讈扚欫椺墑漞趘冖仢儥銢頔轚燩覛硩礕靋觻磩鎘肑綼糑惁敫蒚犑獥婥蓨蓧瞁歒廦鸄虳郹鼳鄓蔋擽盢梑䍥䍽㰅㭊䓇䢮䥶䤙㿨㣙䟐䤨䢰䚫㤸㢩䴞䨤䵠㻺䗩䣓䮥㲻䂆䖑䔉㦘㹍㒪䳬䁶㔏䮭㬏䞶䚐㛫䰛䑀㱤䈪㱹䌐㽁䨀㱸㺡䚍䟏㷴䯜𠴫")
    PingShuiYunInit(allSheet, 4, 12, "色得息國力極翼側直黑憶墨域識[知識]測棘職臆賊刻食逼北惻默德飾勒惑稷特則即拭織蝕仄匿陟穡億塞[閉塞]式植抑殖敕亟克弋熄肋昃忒慝蜮軾飭嗇踣閾泐殛嘿洫翊薏赩湜纆僰屴杙愊寔崱裓墄匐罭愎嶷偪螣[螟螣]剋埴尅棫襋衋劾喞轖淢湢遫扐蠈緎淂蟘幅或恧萴栻鷘鰂翌畟副仂餩醷侐釴鯽腷繶竻膱芅癔瀷蒠淔稄戫蟔稙樴堲蝍菔犆趩堛掝蕀蛡忑嫟恜瘜黓楅冒蘵惐膕赲嘚稫脦煏玏戠溭穓鉓遈棏薔烒鶝艒鰏禃潩捗畐霬噫皕嫼皀嬂謋琙捑骮揤蚮爅熤踾浳螚蟙鳨釛澺垘鄎氻潶艻閄朸臸忇諽檍焏悈窢茍烅嚜鉽侙殕懎慗揊熼鰳阞懝繬㳁㥾㚤㘈䰥䁿䈟㔴䵗䘃㤫㮩㥂㱇䄩䐚䙷䯆䁼䅞䧗㕵䘅㯤䵱㞃䬎㝶䱛䭒㢞㭲㷵㻷䗷䞳㱄䐈䖁㘠㹄䩯䘝㧹㥁䴬㷶㽣㔹㴧䦗㚜䣧䎪䮙㫯㥛㯰㥀㥶䮠䦼㮨㵓䁇㞋䉢䆐䤭𧏾")
    PingShuiYunInit(allSheet, 4, 13, "急立入濕集泣及邑十澀拾蟄習笠粒汲給吸襲揖什級執隰挹縶汁戢葺岌浥緝輯悒翕熠笈伋楫噏濈歙裛潗唈蕺槢廿潝霫芨霵鈒褶啃漐苙鰼湆礏飁雭圾煜闟砬歰熻鵖湁俋咠卙慹鷑譅雴驫彶箿礘叺瓡岦鴔鏶偮翜釞淁趇騽喅鴗蓻謺嶯漝皀嬆湒譶馵鉝孴卌諿䏉㴕㦻㤂㙷㪧䦹㠍䁯㬛㵫䔼㴔䶘䶋㗊䩰䮶䏠㲸㽺䓃㣬䒁䭂䉗㡮㧀㱞㙫㘊㿇䏩㬤㗱䐕㒊䇼䅤㒆䲯䔱㕸䙄㞚㩉㞏㗩䁒")
    PingShuiYunInit(
        allSheet, 4, 14, "合榻塔答雜闔衲匝納颯榼閤踏沓蛤鴿盍遝荅塌蹋盒搭鞳拉臘蠟帀蒳靸漯嗑趿嗒噆鎝咂闒遢剳卡溘誻匌嚃搨馺罨鑞搕唈韐岋濌褟涾耠軜蓋卅磕[石聲]哈瘩磣褡嘁鰈瞌鈒欱狧耷錔鮯鞜鰨匎溻頜歞砵菈鰪砐匒傝崉雥囃詥溚篕魶峇鉔峆鑉譶痷魳罯磼畗魼圾鞥矺抸廅毾礘佮砝魥熆笚鎉翋龖儑姶磖拹笝殧柆鉿硆厒榙枼韴遪䬃䕹㔩䑽㷈㗳䗶䑥䂰䗘䍇㛥䐦㹺㧁㯓䵬㕇䈳䌈䐛䂿䪏䧻㿯䵽㕉䫦䈫䈋䑜䃳䶁䍝䪞㕎㨥䶀䙣䳴㭼㠷㧺㥺䢔䪺㛕㾑䜚㿴㽂䨿䑪㝓㯚䪚䞙㚫䓠㰰䆟㡴𪘁𤸱𢶍")
    PingShuiYunInit(
        allSheet, 4, 15, "叶葉接蝶疊捷涉帖篋愜頰堞妾鋏俠睫鬣牒靨浹屧躡莢協攝貼懾燮挾楫饁燁摺鑷躞諜曄獵蹀捻輒跕囁氎躐讋艓擪屧褶褋惵梜怗聶箑裛衱喋呫韘苶楪笈籋襵歙鞢鍱魘霎厭婕偞菨崨倢椄讘欇筴邋鰈熀蛺擸顳儠擛踥牃踕謵緁僷灄犣聗鎑錜銸徢惗穕帹蠂痷鱲脻迠萐敜慹綊謺鮿鯜埝挕踂瞱淁瞸獦鑈聑褺鏶昅揞巤煠疌踗劦誱寁唊蓻枼殜霅[霅霅，震電貌]帇蓵渫㲲㫸䩞䈉䐑䌖㱌䢡䳖㪑䁋䜆䝃䵿㩎䇣䜲䝱䐲㸎䧪㡇㬪㢵䤮䪓㤴㥈䴑㥦䪉㴇䭟㢎㩸㯿䯀㤐㰼㭯㳧㙷㚔䛟䝓䈎䜓䌰㑙㾜㚲㼪㩶㼲䌌㤲㰔㒤䠟䁽㨩㷸㛍㽊䝕䴴䥡䌜𣶏𦀖𣀳")
    PingShuiYunInit(
        allSheet, 4, 16, "業法甲劫峽怯洽匣壓狎乏鴨插狹鍤嶪夾閘押袷柙帢唼歃掐劄呷恰裌翣胛硤鄴霎陜霅箑嗋祫眨跲啑郟恊鵊扱凹脅鞈搯熁玾喋愶筴岬胠葜烚渫擖姂庘哈鉀萐嚈魻圔喢蜐餄譗姶湆魥鉣驜呿翜韐疀笚埉厒笝煠殗搚痷鉿唊欱[與歃同。嘗也]翈昅磼曱珨鸈魼歰嶯澲砝疺圶抾帹炠筪拹殜餣舺殎垥偛䶎㡊㰱䬊䆘㭘㵊㕅㛼㳌䖎㡋䎎䛅䨐䧨䕛䤶䛽㘝㹤䂲䮢㗼㽠䞩㾀㙝㴙㮑䱒䀴㓣䮜䖖䀷䀫䩡䘥䲜㘡㾎䁆䁍㑢㿓㸣㵤䶝㭱㷅𢘉")
    return allSheet
