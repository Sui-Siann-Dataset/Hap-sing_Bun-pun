from sys import argv
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 用字.教典規範 import 教典

tsiapsiu = {
    ('莉', 'lī'),
    ('啥', 'sím'),
    ('過', 'kú'),
}


def main(tongmia):
    with open(tongmia, encoding='utf-8') as tong:
        tsua = tong.readlines()
        for kui in range(len(tsua) - 2):
            if (
                len(tsua[kui].rstrip()) < 5
                and len(tsua[kui + 1].rstrip()) >= 5
                and len(tsua[kui + 2].rstrip()) >= 5
            ):
                漢字上尾毋是年代 = not tsua[kui + 1].rstrip()[-1].isdigit()
                if 漢字上尾毋是年代:
                    boji = []
                    處理掉分析器無法度處理ê印號 = tsua[kui + 2].replace("'", " ' ")
                    句物件 = 拆文分析器.建立句物件(tsua[kui + 1], 處理掉分析器無法度處理ê印號)
                    for 字 in 句物件.篩出字物件():
                        if 字.敢是標點符號():
                            pass
                        elif 教典.有這个字無(字):
                            pass
                        elif 字.型 == 字.音:
                            pass
                        elif (字.型, 字.音) in tsiapsiu:
                            pass
                        else:
                            boji.append(字)
                    if len(boji) > 0:
                        print(tsua[kui + 1].rstrip())
                        print(tsua[kui + 2].rstrip())
                        print(boji)
                        exit(1)


if __name__ == '__main__':
    main(argv[1])
