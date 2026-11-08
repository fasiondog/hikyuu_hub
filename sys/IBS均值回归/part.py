#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"

_default_mm = MM_Nothing()
_default_tm = crtTM()


def part(buy_th: float = 5.0, sell_th: float = 99.0, st_p: float = 0.02, pg_p: float = 0.10,
         tm: TradeManager = _default_tm, mm: MoneyManagerBase = _default_mm, sp: SlippageBase = None):
    """
    IBS 均值回归系统

    收盘价贴近当日最低价（IBS 低于超卖阈值）时买入；IBS 高于超买阈值时平仓，
    同时带固定百分比止损与固定百分比盈利目标。

    :param buy_th: IBS 超卖买入阈值
    :param sell_th: IBS 超买卖出阈值
    :param st_p: 固定百分比止损
    :param pg_p: 固定百分比盈利目标
    :param tm: 交易管理器
    :param mm: 资金管理器（默认等仓）
    :param sp: 滑点管理器
    :return: part instance
    """
    local_hub = get_current_hub(__file__)
    sg1 = get_part(f"{local_hub}.sg.买入IBS极端低位", buy_th=buy_th)
    sg2 = get_part(f"{local_hub}.sg.卖出IBS极端高位", sell_th=sell_th)
    sg = sg1 + sg2
    sg.set_param("alternate", True)
    ret = SYS_Simple(tm=tm, sg=sg, mm=mm, sp=sp,
                     st=ST_FixedPercent(st_p), pg=PG_FixedPercent(pg_p))
    ret.name = "IBS均值回归系统"
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

    my_sys = get_part(f"{local_hub}.sys.IBS均值回归")
    print(my_sys)

    my_tm = crtTM(Datetime(20180101), init_cash=100000, cost_func=TC_FixedA2017())
    my_sys.tm = my_tm
    my_sys.run(sm['sz000001'], Query(Datetime(20180101)))
    print(my_sys.tm)
    my_sys.tm.tocsv(os.path.dirname(os.path.abspath(__file__)))
    my_sys.performance()
    import matplotlib.pylab as plt
    plt.show()
