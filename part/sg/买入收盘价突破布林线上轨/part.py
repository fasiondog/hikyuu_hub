
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250223"


def part(n: int = 20, band: float = 2.0):
    """
    收盘价突破布林线上轨时买入

    :param int n: 布林线周期, 默认20
    :param float band: 布林线带宽, 默认2.0
    :return: 买入收盘价突破布林线上轨信号
    """
    local_hub = get_current_hub(__file__)
    ind = RESULT(get_part(f"{local_hub}.ind.布林线", n=n, band=band), 1)
    sg = SG_OneSide(CLOSE() > ind, True)
    sg.name = "卖出收盘价跌破布林新下轨"
    return sg


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

    # 请在下方编写测试代码
    sg = part()
    print(sg)

    stk = sm[options['stock_list'][0]]
    k = stk.get_kdata(Query(-200))
    sg.to = k

    import matplotlib.pyplot as plt
    k.plot()
    sg.plot(new=False)
    plt.show()
