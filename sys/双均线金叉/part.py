
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250221"


def part(fastn=5, slown=20):
    """
    双均线金叉系统是一种常见且基础的技术分析交易策略，它基于两条不同周期的移动平均线（MA）的交叉情况来产生买卖信号。

    :param fastn: 短期移动平均线周期
    :param slown: 长期移动平均线周期
    """
    local_hub = get_current_hub(__file__)
    sg1 = get_part(f"{local_hub}.sg.买入双均线金叉", fastn=fastn, slown=slown)
    sg2 = get_part(f"{local_hub}.sg.卖出双均线死叉", fastn=fastn, slown=slown)
    sg = sg1 + sg2
    my_sys = SYS_Simple(sg=sg)
    my_sys.name = "双均线金叉"
    return my_sys


if __name__ == "__main__":
    # 执行 testall 命令时，会多传入一个参数，防止测试时间过长
    # 比如如果在测试代码中执行了绘图操作，可以打开下面的注释代码
    # 此时执行 testall 命令时，将直接返回
    if len(sys.argv) > 1:
        ind = part()
        print(ind)
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

    local_hub = get_current_hub(__file__)
    update_hub(f'{local_hub}')

    # 请在下方编写测试代码
    fastn = 5
    slown = 20
    my_sys = part(fastn=5, slown=20)
    print(my_sys)

    stk = sm[options['stock_list'][0]]
    k = stk.get_kdata(Query(-200))

    my_tm = crtTM(k[0].datetime, init_cash=100000,
                  cost_func=TC_FixedA2017())
    my_sys.tm = my_tm
    my_sys.mm = MM_Nothing()
    my_sys.run(k)

    my_sys.tm.tocsv(os.path.dirname(os.path.abspath(__file__)))
    my_sys.performance()

    k.plot()
    MA(CLOSE, fastn)(k).plot(new=False)
    MA(CLOSE, slown)(k).plot(new=False)
    my_sys.plot(new=False)

    import matplotlib.pyplot as plt
    plt.show()
