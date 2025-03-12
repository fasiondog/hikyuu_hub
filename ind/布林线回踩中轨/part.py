
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "root"
version = "20250213"


def part(n=20):
    """
    布林线回踩中轨买入：价格在上涨过程中，有时会回调至布林线中轨附近，若中轨能对价格起到支撑作用，
    价格在此处止跌企稳并再次向上，是较好的买入时机，表明中轨的支撑有效，上涨趋势有望延续。
    其本质就是均线回踩，通常需要配合长期趋势，比如价格在长期200日均线智商

    :param n: 均线周期
    :return: 布林线回踩中轨指标
    """
    ma = MA(CLOSE(), n=n)
    #  前一日收盘价大于中轨，当日最低价小于等于中轨且收盘价大于中轨
    ret = (REF(CLOSE(), 1) > ma) & (LOW() <= ma) & (CLOSE() > ma)
    ret.name = '布林线回踩中轨'
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
        "stock_list": ["sh000001"],
        "ktype_list": ["day"],
        "load_history_finance": False,
        "load_weight": False,
        "start_spot": False,
        "spot_worker_num": 1,
    }
    load_hikyuu(**options)

    # 请在下方编写测试代码
    s = sm['sh000001']
    k = s.get_kdata(Query(-200))
    ind = part()
    x = ind(k)
    print(x)

    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    bull = get_part(f"{local_hub}.ind.布林线")(k)
    import matplotlib.pyplot as plt
    ax1, ax2 = create_figure(2)
    k.plot(axes=ax1)
    DRAWICON(x, RESULT(bull, 2), 1, kdata=k, axes=ax1)
    RESULT(bull, 0).plot(axes=ax1)
    RESULT(bull, 1).plot(axes=ax1)
    RESULT(bull, 2).plot(axes=ax1)
    x.plot(axes=ax2, legend_on=True)
    plt.show()
