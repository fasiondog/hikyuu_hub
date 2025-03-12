
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250223"


def part(boll_n: int = 20, band: float = 2.0, squeeze_n: int = 50):
    """
    布林线宽度在 squeeze_n 周期内为最小值时买入

    :param boll_n: 布林线周期
    :param band: 布林线带宽
    :param squeeze_n: 布林线宽度在 squeeze_n 周期内为最小值时买入
    """
    sd = DISCARD(STDEV(CLOSE(), n=boll_n), discard=boll_n)
    squeeze = LLV(sd, n=squeeze_n)
    ret = SG_OneSide(sd == squeeze, True)
    ret.name = "买入布林线挤压"
    return ret


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
