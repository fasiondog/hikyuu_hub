#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"


def part(n: int = 500, buy_th: float = -2.5):
    """
    Buy signal: average high/low Z-Score below oversold threshold.

    Calculation:
        high_z = (HIGH - MA(HIGH, n)) / STDEV(HIGH, n)
        low_z  = (LOW  - MA(LOW,  n)) / STDEV(LOW,  n)
        zscore = (high_z + low_z) / 2

    Fires a buy when zscore < buy_th (deep oversold, expects mean reversion up).

    :param n: lookback window for mean and standard deviation
    :param buy_th: oversold threshold (standard deviations)
    :return: part instance
    """
    high_z = (HIGH() - MA(HIGH(), n)) / STDEV(HIGH(), n)
    low_z = (LOW() - MA(LOW(), n)) / STDEV(LOW(), n)
    zscore = (high_z + low_z) / 2
    cond = zscore < buy_th
    ret = SG_OneSide(cond, True)
    ret.name = "买入ZScore超卖"
    return ret


if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    if len(sys.argv) > 1:
        print("ignore test")
        exit(0)

    import os
    import sys
    if sys.platform == 'win32':
        os.system('chcp 65001')

    # 仅加载测试需要的数据，请根据需要修改
    options = {
        "stock_list": ["sz000001"],
        "ktype_list": ["day"],
        "load_history_finance": False,
        "load_weight": False,
        "start_spot": False,
        "spot_worker_num": 1,
    }
    load_hikyuu(**options)

    # 请在下方编写测试代码
    sg = part()
    print(sg)

    stk = sm[options['stock_list'][0]]
    k = stk.get_kdata(Query(-500))
    sg.to = k

    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    import matplotlib.pyplot as plt
    ax1, ax2 = create_figure(2)
    k.plot(axes=ax1)
    sg.plot(new=False, axes=ax2)
    plt.show()
