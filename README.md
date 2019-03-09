# Hap-sing Bun-pun
允言變調實驗文本。觀察文本8段，試驗文本9段。

## 觀察文本
1. POJ版本：`tsingli/leku-0612.txt`
2. 教育部漢字羅馬字版本：`tsingli/leku-0612-hanlo.txt`
2. 詞性kah變調情形：`tsingli/leku-0612-mark.txt`

| 編號 | 文本                            | 年    | 作者               | 數位典藏原文                                                             | 原文頭幾字                 | 其他連結                                                                          | 
|----|-------------------------------|------|------------------|----------------------------------------------------------------|----------------------|-------------------------------------------------------------------------------| 
| 1  | Tang-pō͘ thôan-tō kiàn-bûn-kì 東部傳道見聞記 | 1961 | Tân Kàng-siông 陳降祥  | [連結](http://ip194097.ntcu.edu.tw/nmtl/dadwt/thak.asp?id=975)  | 「Lín kiám無講，         | [台語文記憶](http://ip194097.ntcu.edu.tw/memory/tgb/thak.asp?id=929&page=3)                 | 
| 2  | Tang-pō͘ thôan-tō kiàn-bûn-kì 東部傳道見聞記| 1961 | Tân Kàng-siông 陳降祥  | [連結](http://ip194097.ntcu.edu.tw/nmtl/dadwt/thak.asp?id=975) | 我若問hia ê兄弟講，         | [台語文記憶](http://ip194097.ntcu.edu.tw/memory/tgb/thak.asp?id=929&page=10)                | 
| 3  | Chháu-tui-téng ê Bîn-bāng 草堆頂ê眠夢    | 1955 | N̂g Hôai-un 黃懷恩     | [連結](http://ip194097.ntcu.edu.tw/nmtl/dadwt/thak.asp?id=781)         | 到hit ē暗，烏暗暝逼倚，              |                                                                               | 
| 4  | Chháu-tui-téng ê Bîn-bāng 草堆頂ê眠夢    | 1955 | N̂g Hôai-un 黃懷恩     | [連結](http://ip194097.ntcu.edu.tw/nmtl/dadwt/thak.asp?id=781)         | 瑪莉有時著用雙手來掩伊          |                                                                               | 
| 5  | Sin-bûn Ê Cha̍p-lio̍k 新聞ê雜錄        | 1913 | Bô Chù-bêng  無注明 | [連結](http://ip194097.ntcu.edu.tw/nmtl/dadwt/thak.asp?id=307)         | 有一日我tī 街路teh行        |                                                                               | 
| 6  | Sin-bûn Ê Cha̍p-lio̍k 新聞ê雜錄        | 1913 | Bô Chù-bêng  無注明 | [連結](http://ip194097.ntcu.edu.tw/nmtl/dadwt/thak.asp?id=309)         | 過幾日koh得著機會thang 結謙遜、 | [台灣白話字文獻館](http://pojbh.lib.ntnu.edu.tw/script/src-3311.htm)                              | 
| 7  | Cha̍p-hāng Kóan-kiàn 十項管見         | 1925 |  Chhòa Pôe-hóe 蔡培火  | [連結](http://ip194097.ntcu.edu.tw/nmtl/dadwt/thak.asp?id=314)         | 外國人o-ló 咱ê 台灣秀麗；     | [冊目錄](http://www.laijohn.com/archives/pc/Chhoa/Chhoa,Phoe/works/chap/contents.htm) | 
| 8  | Cha̍p-hāng Kóan-kiàn 十項管見         | 1925 |  Chhòa Pôe-hóe 蔡培火  | [連結](http://ip194097.ntcu.edu.tw/nmtl/dadwt/thak.asp?id=314)         | 親像án-ni來講，           | [冊目錄](http://www.laijohn.com/archives/pc/Chhoa/Chhoa,Phoe/works/chap/contents.htm) | 

## 試驗文本
1. POJ版本：`tsingli/leku-0705.txt`
2. 教育部漢字羅馬字版本：`tsingli/leku-0705-hanlo.txt`
2. 詞性kah變調情形：`tsingli/leku-0705-mark.txt`



## 檔案說明
### 楊允言-台語變調系統實作研究.pdf
實驗論文

### un-gian.pdf
允言老師的實驗資料統計

### re/
允言老師提供的檔案，`big5`編碼

#### `leku-0000.txt`, `*-poj.txt`
原始檔案，之間版本可能無仝

#### `*-mark.txt`
有標詞性的檔案，請參考論文第8頁下底`表2 變調註記`。
佮`*-poj.txt`的檔案小可仔無仝，有改過腔口、詞綴。

### re-utf-8/
`re`轉做`UTF-8`

### tbk/
照老師的檔案，揣出[數位典藏](https://github.com/Taiwanese-Corpus/nmtl_2006_dadwt)ê文章

### tsingli/
1. `leku-****.txt`
2. `leku-****-mark.txt`
3. `leku-****-hanlo.txt`是照

第1,2種是自`re-utf-8`ê檔案，照 #5 一步一步整理好--ê。
無mark(第1種) kah 有mark(第2種)--ê，除了空白kah連字符外，攏是相仝--ê。
第3種是照第1種整理出教育部ê漢字kah羅馬字寫法。

### Un-gian.py
統計字數的程式

