#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"


def part(buy_th: float = 5.0):
    """
    IBS 均值回归买入信号

    收盘价贴近当日最低价（日内极端弱势）时买入，赌日内极端位置后的短期回归。

    :param buy_th: IBS 超卖买入阈值
    :return: part instance
    """
    ibs = (CLOSE() - LOW()) / (HIGH() - LOW()) * 100
    cond = ibs < buy_th
    ret = SG_OneSide(cond, True)
    ret.name = "买入IBS极端低位"
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
