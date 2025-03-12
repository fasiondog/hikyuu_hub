
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "admin"
version = "20240526"


def part(n: int = 14, tm: TradeManager = None) -> System:
    """
    使用简易波动率指标（EMV）的交易系统。
    EMV 在0 以下表示弱势，在0 以上表示强势；EMV 由负转正应买进，由正转负应卖出。
    """
    local_hub = get_current_hub(__file__)
    emv = get_part(f'{local_hub}.ind.emv', n=n)
    my_sg = SG_Bool(emv > 0, emv <= 0)
    my_tm = crtTM() if tm is None else tm
    my_mm = MM_Nothing()
    my_mm.set_param("auto-checkin", False)
    my_sys = SYS_Simple(tm=my_tm, sg=my_sg, mm=my_mm)
    return my_sys


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

    my_sys = get_part(f"{local_hub}.sys.emv择时")
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
