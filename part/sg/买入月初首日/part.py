#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"


def part():
    """
    Month-start buy signal.

    Buys on the first trading day of each calendar month: a bar whose (year, month)
    differs from the previous bar's marks the month's first trading day.

    :return: part instance
    """

    def calculate(self, k):
        if len(k) == 0:
            return
        prev = k[0].datetime
        for i in range(1, len(k)):
            cur = k[i].datetime
            if (cur.year, cur.month) != (prev.year, prev.month):
                self._add_buy_signal(cur)
            prev = cur

    ret = crtSG(calculate, params={}, name="买入月初首日")
    ret.set_param("alternate", False)
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
    sg = part()
    print(sg)

    stk = sm[options['stock_list'][0]]
    k = stk.get_kdata(Query(-500))
    sg.to = k

    import matplotlib.pyplot as plt
    ax1, ax2 = create_figure(2)
    k.plot(axes=ax1)
    sg.plot(new=False, axes=ax2)
    plt.show()
