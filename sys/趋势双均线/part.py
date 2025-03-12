
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20240504"

_default_mm = MM_Nothing()
_default_tm = crtTM()


def part(fast_n: int = 10, slow_n: int = 120, tm: TradeManager = _default_tm, mm: MoneyManagerBase = _default_mm, sp: SlippageBase = None):
    """
    趋势双均线，短期均线在长期均线之上买入并持有，否则卖出

    :param fast_n: 短期均线周期
    :param slow_n: 长期均线周期
    :param tm: 交易管理器
    :param mm: 资金管理器
    :param sp: 滑点管理器
    :return: part instance
    """
    ind = MA(CLOSE, fast_n) > MA(CLOSE, slow_n)
    my_sg = SG_Bool(ind, NOT(ind))
    ret = SYS_Simple(tm=tm, sg=my_sg, mm=mm, sp=sp)
    ret.name = "趋势双均线系统"
    return ret


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

    my_sys = get_part(f"{local_hub}.sys.趋势双均线")
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
