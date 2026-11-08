#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hikyuu import *

author = "fasiondog"
version = "20261108"


def part(n: int = 30, initial_pct: float = 5.0, step_pct: float = 1.0):
    """
    SMA 偏离渐进开平仓信号

    做多一侧：
    - 收盘在 SMA 下方且向下偏离 ≥ initial_pct% 时首次买入；
    - 已持仓后，价格继续向下偏离上次买入日最低价 ≥ step_pct% 时加仓；
    - 收盘回到 SMA 上方时平掉全部多头（同 bar 出现买入则先对冲）。

    :param n: SMA 均线周期
    :param initial_pct: 首次入场向下偏离阈值（%）
    :param step_pct: 加仓向下偏离步长（%）
    :return: part instance
    """

    def calculate(self, k):
        ma = MA(CLOSE(k), n)
        last_buy_low = None
        for i in range(len(k)):
            d = k[i].datetime
            close = k[i].close
            low = k[i].low
            ma_val = ma[i]
            if i < ma.discard:
                continue
            # 回到 SMA 上方平掉全部多头
            if close >= ma_val:
                self._add_sell_signal(d)
                last_buy_low = None
                continue
            if low < ma_val:
                if last_buy_low is None:
                    if (ma_val - low) / ma_val * 100 >= initial_pct:
                        self._add_buy_signal(d)
                        last_buy_low = low
                else:
                    if low < last_buy_low and \
                       (last_buy_low - low) / last_buy_low * 100 >= step_pct:
                        self._add_buy_signal(d)
                        last_buy_low = low

    return crtSG(calculate,
                 params={"n": n, "initial_pct": initial_pct, "step_pct": step_pct},
                 name="SMA偏离渐进开平仓")


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
    MA(CLOSE, n=n)(k).plot(new=False, axes=ax1)
    sg.plot(new=False, axes=ax2)
    plt.show()
