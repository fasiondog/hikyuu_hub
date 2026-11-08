#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"


def part(n: int = 500):
    """
    Z-Score (average of high and low price z-scores)

    Calculation:
        high_z  = (HIGH  - SMA(HIGH, n))  / STDEV(HIGH, n)
        low_z   = (LOW   - SMA(LOW,  n))  / STDEV(LOW,  n)
        zscore  = (high_z + low_z) / 2

    Value above 0 means price is above its recent mean (overbought side);
    below 0 means oversold side. Magnitude is in standard deviations.

    :param n: lookback window for SMA and STDEV
    :return: part instance (indicator)
    """
    high_z = (HIGH() - MA(HIGH(), n)) / STDEV(HIGH(), n)
    low_z = (LOW() - MA(LOW(), n)) / STDEV(LOW(), n)
    ret = (high_z + low_z) / 2
    ret.name = "ZScore"
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
    stk = sm[options['stock_list'][0]]
    k = stk.get_kdata(Query(0))

    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    z = get_part(f"{local_hub}.ind.ZScore")
    print(z)

    import matplotlib.pyplot as plt
    ax1, ax2 = create_figure(2)
    k.plot(axes=ax1)
    z(k).plot(axes=ax2)
    plt.axhline(2.5, color='r', linestyle='--')
    plt.axhline(-2.5, color='g', linestyle='--')
    plt.show()
