from hikyuu import MM_FixedUnits

# 部件作者
author = "fasiondog"

# 版本
version = '20200825'


def part(n=33):
    return MM_FixedUnits(n)


part.__doc__ = MM_FixedUnits.__doc__
