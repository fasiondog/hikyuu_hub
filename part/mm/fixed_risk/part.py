from hikyuu import MM_FixedRisk

# 部件作者
author = "fasiondog"

# 版本
version = '20200825'


def part(risk=1000.00):
    return MM_FixedRisk(risk)


part.__doc__ = MM_FixedRisk.__doc__
