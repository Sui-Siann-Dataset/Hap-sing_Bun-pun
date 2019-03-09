# Hap-sing Bun-pun
允言變調實驗文本。觀察文本8段，試驗文本9段。

## 觀察文本
1. POJ版本：`tsingli/leku-0612.txt`
2. 教育部漢字羅馬字版本：`tsingli/leku-0612-hanlo.txt`
2. 詞性kah變調情形：`tsingli/leku-0612-mark.txt`

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

