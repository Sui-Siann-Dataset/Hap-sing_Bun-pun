import re
from sys import argv
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


def main(hanlotongmia, marktongmia):
    huho = re.compile('[%$#&@~^]')
    susing = re.compile('(\([^)]+\))')
    for (han, lo), mark in zip(hanloku(hanlotongmia), markku(marktongmia)):
        bosusing_mark = susing.sub('', mark)
        poj_mark = huho.sub('', bosusing_mark)
        拆文分析器.建立句物件(lo, poj_mark)
        hanlo_list = 拆文分析器.建立句物件(han, lo).篩出字物件()
        tsitma = 0
        kiatko = []
        for mark in 拆文分析器.建立句物件(bosusing_mark).篩出字物件():
            if mark.型 == '#':
                kiatko.append('#')
            elif huho.search(mark.型):
                pass
            else:
                kiatko.append(hanlo_list[tsitma].型)
                tsitma += 1
        print(''.join(kiatko))
        print(lo,)
        print()


def hanloku(tongmia):
    with open(tongmia, encoding='utf-8') as tong:
        tsua = tong.readlines()
        for kui in range(len(tsua) - 2):
            if (
                len(tsua[kui]) < 5
                and len(tsua[kui + 1]) >= 5
                and len(tsua[kui + 2]) >= 5
            ):
                漢字上尾毋是年代 = not tsua[kui + 1].rstrip()[-1].isdigit()
                if 漢字上尾毋是年代:
                    yield tsua[kui + 1].rstrip().replace("'", " ' "), tsua[kui + 2].rstrip().replace("'", " ' ")


def markku(tongmia):
    with open(tongmia, encoding='utf-8') as tong:
        for tsua in tong.readlines():
            if len(tsua) > 5:
                yield tsua.rstrip().replace("'", " ' ")


if __name__ == '__main__':
    main(argv[1], argv[2])
