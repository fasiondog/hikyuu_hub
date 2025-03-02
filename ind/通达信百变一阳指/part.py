from hikyuu import *

# 部件作者
author = "fasiondog"

# 版本
version = '20231025'

VAR1 = LLV(LOW(), 13)
VAR2 = HHV(HIGH(), 13)
VAR3 = SMA((CLOSE()-VAR1)/(VAR2-VAR1) * 100, 5, 1)
VAR4 = SMA((VAR2-CLOSE())/(VAR2-VAR1) * 100, 5, 1)
AA = VAR3
BB = VAR4
VAR5 = SMA(MAX(CLOSE() - REF(CLOSE(), 1), 0), 5, 1) / \
    SMA(ABS(CLOSE()-REF(CLOSE(), 1)), 5, 1) * 100
CC = EMA(VAR5, 3)
XG = CROSS(CC, BB) & (CC >= REF(CC, 1)) & (BB <= REF(BB, 3)) & (CC >= 49.5) & (
    MA(CLOSE(), 3) >= REF(MA(CLOSE(), 3), 1)) & (MA(CLOSE(), 7) >= REF(MA(CLOSE(), 7), 1)) & (MA(CLOSE(), 60) > REF(MA(CLOSE(), 60), 3))


def part(n=10, fast_n=2, slow_n=30):
    """
    通达信百变一阳指选股器
    参考：https://zhuanlan.zhihu.com/p/629837085    
    """
    XG.name = "通达信百变一阳指"
    return XG
