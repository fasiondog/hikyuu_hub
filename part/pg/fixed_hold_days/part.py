from hikyuu import PG_FixedHoldDays

# 部件作者
author = "fasiondog"

# 版本
version = '20200825'


def part(days=5):
    return PG_FixedHoldDays(days)


part.__doc__ = PG_FixedHoldDays.__doc__
