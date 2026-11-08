#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"

_default_mm = MM_Nothing()
_default_tm = crtTM()


def part(n: int = 70, rsi_n: int = 2, buy_th: float = 10.0, sell_th: float = 90.0,
         tm: TradeManager = _default_tm, mm: MoneyManagerBase = _default_mm, sp: SlippageBase = None):
    """
    RSI 均值回归系统

    上升趋势中的短期超卖买入：收盘价 > n 日均线且 RSI 低于超卖阈值时买入，
    RSI 高于超买阈值时平仓。

    :param n: 趋势过滤均线周期
    :param rsi_n: RSI 周期
    :param buy_th: RSI 超卖买入阈值
    :param sell_th: RSI 超买卖出阈值
    :param tm: 交易管理器
    :param mm: 资金管理器（默认等仓）
    :param sp: 滑点管理器
    :return: part instance
    """
    local_hub = get_current_hub(__file__)
    sg1 = get_part(f"{local_hub}.sg.买入RSI超卖", n=n, rsi_n=rsi_n, buy_th=buy_th)
    sg2 = get_part(f"{local_hub}.sg.卖出RSI超买", rsi_n=rsi_n, sell_th=sell_th)
    sg = sg1 + sg2
    sg.set_param("alternate", True)
    ret = SYS_Simple(tm=tm, sg=sg, mm=mm, sp=sp)
    ret.name = "RSI均值回归系统"
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

    my_sys = get_part(f"{local_hub}.sys.RSI均值回归")
    print(my_sys)

    my_tm = crtTM(Datetime(20180101), init_cash=100000, cost_func=TC_FixedA2017())
    my_sys.tm = my_tm
    my_sys.run(sm['sz000001'], Query(Datetime(20180101)))
    print(my_sys.tm)
    my_sys.tm.tocsv(os.path.dirname(os.path.abspath(__file__)))
    my_sys.performance()
    import matplotlib.pylab as plt
    plt.show()
