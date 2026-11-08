#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"


def part(n: int = 30, initial_pct: float = 5.0, step_pct: float = 1.0,
         tier_count: int = 5, tier_size: int = 100, tm=None):
    """
    SMA 偏离渐进加仓系统

    价格偏离 SMA 下方 ≥ initial_pct% 时首次买入；
    已有仓位时，价格继续偏离上次入场价 ≥ step_pct% 时按分档加仓（每档 tier_size 股）；
    收盘价回到 SMA 上方时全平。

    :param n: SMA 均线周期
    :param initial_pct: 首次入场偏离阈值（%）
    :param step_pct: 加仓偏离步长（%）
    :param tier_count: 最大加仓档位
    :param tier_size: 每档买入股数
    :param tm: TradeManager，默认用占位配置
    :return: SYS instance
    """
    if tm is None:
        tm = crtTM(Datetime(20180101), init_cash=100000,
                   cost_func=TC_FixedA2017())

    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    sg = get_part(f"{local_hub}.sg.买入SMA下方偏离", n=n,
                  initial_pct=initial_pct, step_pct=step_pct)
    sg.set_param("alternate", False)

    mm = get_part(f"{local_hub}.mm.渐进加仓",
                  tier_count=tier_count, tier_size=tier_size)

    ret = SYS_Simple(tm=tm, sg=sg, mm=mm)
    ret.name = "SMA偏离渐进加仓系统"
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
    tm = crtTM(Datetime(20180101), init_cash=0, cost_func=TC_FixedA2017())
    my_sys = part(tm=tm)
    my_sys.mm.set_param("auto_checkin", True)
    print(my_sys)

    stk = sm[options['stock_list'][0]]
    my_sys.run(stk, Query(Datetime(20180101), Datetime(20261023)))
    print("期末现金:", my_sys.tm.current_cash)

    # 导出交易明细
    base = os.path.dirname(__file__)
    my_sys.tm.tocsv(f"{base}")
    my_sys.performance()
    import matplotlib.pylab as plt
    plt.show()
