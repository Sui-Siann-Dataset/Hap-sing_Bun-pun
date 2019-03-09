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
                if not tsua[kui + 1].rstrip()[-1].isdigit():
                    句物件 = 拆文分析器.建立句物件(tsua[kui + 1], tsua[kui + 2])


if __name__ == '__main__':
    main(argv[1])
