from hikyuu import *

# 部件作者
author = "fasiondog"

# 版本
version = '20231223'


def part():
    """
    累积收益率 (Cumulative return)

    示例: 
        ind = get_part('default.ind.累积收益率')
        k = get_kdata('sz000001', Query(-200))
        x = ind(k.close)
        x.plot()
    """
    return ROCR(0)
