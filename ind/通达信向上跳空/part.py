from hikyuu import *

# 部件作者
author = "fasiondog"

# 版本
version = '20231223'

TK = (O > REF(H, 1)) & (L > REF(H, 1))
TS = BARSLAST(TK)
XG = BETWEEN(C, REF(H, TS+1), REF(L, TS)) & (TS < 10)


def part(n=10, fast_n=2, slow_n=30):
    """
    通达信百变一阳指选股器
    参考：https://zhuanlan.zhihu.com/p/629837085    
    """
    XG.name = "通达信向上跳空"
    return XG
