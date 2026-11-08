#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"


def part(rsi_n: int = 2, sell_th: float = 90.0):
    """
    RSI 均值回归卖出信号

    RSI 高于超买阈值时平仓。
    RSI 采用 Wilder 口径（SMA 平滑），与 hikyuu 内置 RSI 一致，直接使用内置指标。

    :param rsi_n: RSI 周期
    :param sell_th: RSI 超买卖出阈值
    :return: part instance
    """
    cond = RSI(CLOSE(), rsi_n) > sell_th
    ret = SG_OneSide(cond, False)
    ret.name = "卖出RSI超买"
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
    RSI(CLOSE, 2)(k).plot(axes=ax2)
    sg.plot(new=False, axes=ax2)
    plt.show()
