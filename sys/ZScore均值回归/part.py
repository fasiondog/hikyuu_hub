#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"

_default_mm = MM_Nothing()
_default_tm = crtTM()


def part(n: int = 500, buy_th: float = -2.5, sell_th: float = 2.5,
         tm: TradeManager = _default_tm, mm: MoneyManagerBase = _default_mm, sp: SlippageBase = None):
    """
    Z-Score mean-reversion system (long-only A-share mapping).

    Buys when the average of the high and low price Z-Scores drops below an
    oversold threshold (buy_th), and exits when it rises above an overbought
    threshold (sell_th).

    Calculation (per bar):
        high_z = (HIGH - MA(HIGH, n)) / STDEV(HIGH, n)
        low_z  = (LOW  - MA(LOW,  n)) / STDEV(LOW,  n)
        zscore = (high_z + low_z) / 2

    :param n: lookback window for the mean and standard deviation
    :param buy_th: oversold entry threshold (standard deviations)
    :param sell_th: overbought exit threshold (standard deviations)
    :param tm: trade manager
    :param mm: money manager (default equal-weight)
    :param sp: slippage
    :return: SYS instance
    """
    local_hub = get_current_hub(__file__)
    sg1 = get_part(f"{local_hub}.sg.买入ZScore超卖", n=n, buy_th=buy_th)
    sg2 = get_part(f"{local_hub}.sg.卖出ZScore超买", n=n, sell_th=sell_th)
    sg = sg1 + sg2
    sg.set_param("alternate", True)
    ret = SYS_Simple(tm=tm, sg=sg, mm=mm, sp=sp)
    ret.name = "ZScore均值回归系统"
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
    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    my_sys = get_part(f"{local_hub}.sys.ZScore均值回归")
    print(my_sys)

    my_tm = crtTM(Datetime(20100101), init_cash=100000,
                  cost_func=TC_FixedA2017())
    my_sys.tm = my_tm
    my_sys.run(sm['sz000001'], Query(Datetime(20100101)))
    print(my_sys.tm)
    my_sys.tm.tocsv(os.path.dirname(os.path.abspath(__file__)))
    my_sys.performance()
    import matplotlib.pylab as plt
    plt.show()
