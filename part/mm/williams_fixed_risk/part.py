from hikyuu import MM_WilliamsFixedRisk

# 部件作者
author = "fasiondog"

# 版本
version = '20200825'


def part(p=0.1, max_loss=1000.0):
    return MM_WilliamsFixedRisk(p, max_loss)


part.__doc__ = MM_WilliamsFixedRisk.__doc__
