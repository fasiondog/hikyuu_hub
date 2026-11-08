#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"


def part(n: int = 70, rsi_n: int = 2, buy_th: float = 10.0):
    """
    RSI 均值回归买入信号

    上升趋势中的短期超卖买入：收盘价在 n 日均线之上且 RSI 低于超卖阈值时买入。
    RSI 采用 Wilder 口径（SMA 平滑），与 hikyuu 内置 RSI 一致，直接使用内置指标。

    :param n: 趋势过滤均线周期
    :param rsi_n: RSI 周期
    :param buy_th: RSI 超卖买入阈值
    :return: part instance
    """
    cond = (CLOSE() > MA(CLOSE(), n)) & (RSI(CLOSE(), rsi_n) < buy_th)
    ret = SG_OneSide(cond, True)
    ret.name = "买入RSI超卖"
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

    local_hub = get_current_hub(__file__)
    update_hub(local_hub)

    import matplotlib.pyplot as plt
    ax1, ax2 = create_figure(2)
    k.plot(axes=ax1)
    MA(CLOSE, n=70)(k).plot(new=False, axes=ax1)
    RSI(CLOSE, 2)(k).plot(axes=ax2)
    sg.plot(new=False, axes=ax2)
    plt.show()
