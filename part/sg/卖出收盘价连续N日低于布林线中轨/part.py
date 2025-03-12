
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250214"


def part(n: int = 3, boll_n: int = 20):
    """
    连续 N 日收盘价低于布林线中轨

    :param n: 连续 N 日收盘价低于布林线中轨, 默认3
    :param boll_n: 布林线周期, 默认20
    :return: 卖出收盘价连续3日跌破布林线中轨信号
    """
    sg = SG_OneSide(COUNT(CLOSE() < MA(CLOSE(), n=boll_n), n=n), False)
    sg.name = "卖出收盘价连续N日跌破布林线中轨"
    return sg


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
    sg = part()
    print(sg)

    stk = sm[options['stock_list'][0]]
    k = stk.get_kdata(Query(-100))
    sg.to = k

    from matplotlib import pyplot as plt
    k.plot()
    sg.plot(new=False)
    plt.show()
