#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"

_default_mm = MM_Nothing()
_default_tm = crtTM()


def part(rsi_n: int = 2, buy_th: float = 25.0, hold_n: int = 5,
         n: int = 50, use_ma_filter: bool = True,
         tm: TradeManager = _default_tm, mm: MoneyManagerBase = _default_mm, sp: SlippageBase = None):
    """
    RSI oversold reversal system with MA filter and fixed holding-period exit.

    Buys when RSI turns up from below the oversold threshold (optional MA filter:
    close above the MA), then exits after a fixed number of holding bars
    (via PG_FixedHoldDays), regardless of price.

    :param rsi_n: RSI period
    :param buy_th: RSI oversold entry threshold
    :param hold_n: fixed holding bars before forced exit
    :param n: MA trend-filter period
    :param use_ma_filter: whether to require close above the MA
    :param tm: trade manager
    :param mm: money manager (default equal-weight)
    :param sp: slippage
    :return: SYS instance
    """
    local_hub = get_current_hub(__file__)
    sg = get_part(f"{local_hub}.sg.买入RSI超卖反转", rsi_n=rsi_n, buy_th=buy_th,
                  n=n, use_ma_filter=use_ma_filter)
    pg = PG_FixedHoldDays(hold_n)
    ret = SYS_Simple(tm=tm, sg=sg, mm=mm, sp=sp, pg=pg)
    ret.name = "RSI反转固定持有系统"
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

    my_sys = get_part(f"{local_hub}.sys.RSI反转固定持有")
    print(my_sys)

    my_tm = crtTM(Datetime(20180101), init_cash=100000, cost_func=TC_FixedA2017())
    my_sys.tm = my_tm
    my_sys.run(sm['sz000001'], Query(Datetime(20180101)))
    print(my_sys.tm)
    my_sys.tm.tocsv(os.path.dirname(os.path.abspath(__file__)))
    my_sys.performance()
    import matplotlib.pylab as plt
    plt.show()
