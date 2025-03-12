
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250223"


def part(boll_n: int = 20, band: float = 2.0, squeeze_n: int = 50):
    """
    布林线挤压策略
    进入信号: 当股价突破上轨或出现Squeeze。
    退出信号: 当股价跌破下轨。

    :param boll_n: 布林线周期, 默认20
    :param band: 布林线带宽, 默认2.0
    :param squeeze_n: 移动平均周期, 50
    """
    local_hub = get_current_hub(__file__)
    sg1 = get_part(f"{local_hub}.sg.买入收盘价突破布林线上轨", n=boll_n, band=band)
    sg2 = get_part(f"{local_hub}.sg.买入布林线挤压", boll_n=boll_n,
                   band=band, squeeze_n=squeeze_n)
    sg3 = get_part(f"{local_hub}.sg.卖出收盘价跌破布林线下轨", n=boll_n, band=band)
    sg = SG_Add(sg1, sg2, False) + sg3
    my_sys = SYS_Simple(sg=sg)
    my_sys.name = "布林线挤压策略"
    return my_sys


if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
    if len(sys.argv) > 1:
        my_sys = part()
        print(my_sys)
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
    my_sys = part()
    print(my_sys)

    stk = sm[options['stock_list'][0]]
    sg = my_sys.sg
    sg.to = stk.get_kdata(Query(-200))
    sg.plot()

    my_tm = crtTM(Datetime(20150101), init_cash=0,
                  cost_func=TC_FixedA2017())
    my_sys.tm = my_tm
    my_sys.mm = MM_FixedCount(100)
    my_sys.mm.set_param("auto-checkin", True)
    my_sys.run(stk, Query(Datetime(20150101)))

    import matplotlib.pyplot as plt
    my_sys.performance()
    plt.show()
