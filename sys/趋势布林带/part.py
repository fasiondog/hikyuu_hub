
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240517"


_default_mm = MM_Nothing()
_default_tm = crtTM()


def part(n: int = 100, band: float = 0.5, tm: TradeManager = None) -> System:
    """
    布林带趋势交易策略：当股价向上突破上轨时，为买入信号，当股价向下突破下界时，则为卖出信号

    :param int n: 窗口周期，默认 100
    :param float band: 轨道宽度, 默认 0.5
    :param TradeManager tm: 账户管理实例，未指定时，默认使用 crtTM()
    """
    local_hub = get_current_hub(__file__)
    my_sg = get_part(f"{local_hub}.sg.趋势布林带", n=n, band=band)
    my_tm = crtTM() if tm is None else tm
    my_sys = SYS_Simple(tm=my_tm, mm=MM_Nothing(), sg=my_sg)
    return my_sys.clone()


if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
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

    my_sys = get_part(f"{local_hub}.sys.趋势布林带")
    print(my_sys)

    if len(sys.argv) <= 1:
        my_tm = crtTM(Datetime(20200101), init_cash=100000,
                      cost_func=TC_FixedA2017())
        my_sys.tm = my_tm
        my_sys.run(sm['sz000001'], Query(Datetime(20200101)))
        print(my_sys.tm)
        my_sys.tm.tocsv(os.path.dirname(os.path.abspath(__file__)))
        my_sys.performance()
        import matplotlib.pylab as plt
        plt.show()
