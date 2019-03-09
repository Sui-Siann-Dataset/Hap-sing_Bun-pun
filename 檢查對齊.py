from sys import argv
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


def main(tongmia):
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
                    處理掉分析器無法度處理ê印號 = tsua[kui + 2].replace("'", " ' ")
                    句物件 = 拆文分析器.建立句物件(tsua[kui + 1], 處理掉分析器無法度處理ê印號)


if __name__ == '__main__':
    main(argv[1])
