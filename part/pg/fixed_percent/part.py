from hikyuu import PG_FixedPercent

# 部件作者
author = "fasiondog"

# 版本
version = '20200825'


def part(p=0.2):
    return PG_FixedPercent(p)


part.__doc__ = PG_FixedPercent.__doc__
