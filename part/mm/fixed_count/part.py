from hikyuu import MM_FixedCount

# 部件作者
author = "fasiondog"

# 版本
version = '20200825'


def part(n=100):
    return MM_FixedCount(n)


part.__doc__ = MM_FixedCount.__doc__
