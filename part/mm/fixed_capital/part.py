from hikyuu import MM_FixedCapital

# 部件作者
author = "fasiondog"

# 版本
version = '20200825'


def part(capital=10000.00):
    return MM_FixedCapital(capital)


part.__doc__ = MM_FixedCapital.__doc__
