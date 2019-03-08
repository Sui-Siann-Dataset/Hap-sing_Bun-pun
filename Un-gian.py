from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.公用變數 import 標點符號
it_lo = 'Tāi-eng kap Tāi-bí kok ê peh-sìⁿ khah-chōe sǹg sī Iâ-so͘ kàu ê lâng, só͘-í hiah-ê só͘-chāi khah tùi-tiōng Siōng-tè ê hoat-tō͘; chhin-chhiūⁿ Lé-pài-ji̍t lóng m̄-sái chòe kang, ia̍h m̄-sái chòe seng-lí, pêng-siông ê chèng-sū koaⁿ-hú m̄-sái pān, hō͘ koaⁿ-hú kap peh-sìⁿ lóng-chóng thang thiaⁿ tō-lí pôe-ióng liông-sim. Kiám-chhái lâng chhiàⁿ tn̂g-kang, bōe bián-kióng i Lé-pài-ji̍t chòe kang. Taⁿ beh hoan-e̍k chi̍t-chat ê sin-bûn.'
it_lo = '  Lâng ū chhài-hn̂g, khòaⁿ-kìⁿ chhù-piⁿ ê tn̂g-kang, miâ Jīm teh-chòe kang, kiò i kóng, “Jīm-ló-ah, Lé-pài-ji̍t chá-khí tio̍h lâi góa chhài-hn̂g tàu pang-chān chòe kang, lí beh mah ?”'
it_lo = '  Chāi che Tâi-ôan tó-lāi, ha̍k-būn sī hùi-thûi chin kú lah! Chū chin-chiàⁿ kú ê í-chêng, ha̍k-būn sī kan-ta kúi-ê tha̍k-chheh-lâng teh bat; í-gōa tōa-pō͘-hūn ê lâng, chiū-sī chòe seng-lí ê, choh-sit ê, iā-sī chòe-kang ê, it-chhè kap ha̍k-būn sī chha-put-to lóng bô koan-hē. Koh-chài hiah-ê tha̍k-chheh-lâng só͘ tha̍k só͘ bat ê, lóng sī kúi-pah nî-chêng iā-sī kúi-chheng nî-chêng ê jîn só͘ gián-kiù ê kū chô-phek; khah chē sī lóng bōe-thang ha̍h sî-sè. Chiông-tiong khoah iā-sī ū hit-hō put-sî to-si chin, kàu to̍h-lo̍h to-sī ōe ha̍h-ēng ê hó ha̍k-būn; chóng-sī hō͘ hiah-ê tha̍k-chheh-lâng chhau-pôaⁿ liáu í-keng lāu-lāu bô mê-kak.'
it_lo = 'Chhin-chhiūⁿ án-ni lâi kóng , chāi lán Tâi-ôan kīn-kīn chi̍t tia̍p-á-kú ê kang-hu , ài soaⁿ chiū ū soaⁿ , ài hái chiū ū hái , beh jo̍ah chiū ū jo̍ah ,kôaⁿ chiū ū kôaⁿ . Só͘-í thang kóng Tâi-ôan sī chi̍t ê sió Tang-iûⁿ . Lán Tâi-ôan ū chit-khóan thian-jiân ê hó-kéng ,hó khì-hāu , chiong-lâi nā-sī koh ēng-sim ke lâng ê kang-hu tōa-tōa lâi chéng-tùn , tek-khak ē chiâⁿ-chò Tang-iûⁿ ê tōa kong-hn̂g , hō͘ Tang-iûⁿ ê lâng chi̍p-óa lâi hióng-hok an-lo̍k .'


def in_in_leh(ku):
    # it_lo=it_lo.replace(',','').replace('!','').replace('.','').replace(';','').replace('?','')
    # 共輕聲詞拆開，a--b => 2
    ku_bo_khinsiann = ku.replace('--', ' ') 
    it = 拆文分析器.建立章物件(ku_bo_khinsiann)
    piau = 0
    for ji in it.篩出字物件():
        if ji.型 in 標點符號:
            piau += 1
#     print('piau', piau)
    詞數 = len(it.網出詞物件())
    字數 = len(it.篩出字物件())
    print('{},{}, {},{}'.format(詞數, 詞數 - piau, 字數, 字數 - piau))
#     print(len(it.網出詞物件()), len(it.篩出字物件()))
#     for ku in it.內底句:
#         print(ku.看型('-', ' '), len(ku.網出詞物件()) - 1)


# chi̍t tia̍p-á-kú => chi̍t-tia̍p-á-kú
# chi̍t ê => chi̍t-ê

# http://xdcm.nmtl.gov.tw/dadwt/
# http://ip194097.ntcu.edu.tw/nmtl/dadwt/
# tbk

with open('./tsingli/leku-0612-hanlo.txt', encoding='utf-8') as tong:
    for lineId, ku in enumerate(tong.readlines(), 1):
        isLomajiLine = (lineId % 11 == 3) or (lineId % 11 == 7)
        if isLomajiLine:
            try:
                in_in_leh(ku)
            except Exception as e:
                print('無法度印：', str(e), ku)
