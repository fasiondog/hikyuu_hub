#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"


def part():
    """
    IBS（Internal Bar Strength，内部柱强度）

    收盘价在当日高低区间中的相对位置，取值 0~100。计算公式：IBS = (CLOSE - LOW) / (HIGH - LOW) * 100

    取值越接近 0 表示收盘贴近当日最低价（日内极端弱势），越接近 100 表示收盘
    贴近当日最高价（日内极端强势）。

    :return: IBS 指标
    """
    ret = (CLOSE() - LOW()) / (HIGH() - LOW()) * 100
    ret.name = "IBS"
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
    s = sm['sz000001']
    k = s.get_kdata(Query(-200))
    ind = part()
    x = ind(k)
    print(x)

    import matplotlib.pyplot as plt
    ax1, ax2 = create_figure(2)
    k.plot(axes=ax1)
    x.plot(axes=ax2)
    plt.show()
