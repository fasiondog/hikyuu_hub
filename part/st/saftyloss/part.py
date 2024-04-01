from hikyuu import ST_Saftyloss

# 部件作者
author = "fasiondog"

# 版本
version = '20200824'


def part(n1=10, n2=3, p=2.0):
    return ST_Saftyloss(n1, n2, p)


part.__doc__ = ST_Saftyloss.__doc__
